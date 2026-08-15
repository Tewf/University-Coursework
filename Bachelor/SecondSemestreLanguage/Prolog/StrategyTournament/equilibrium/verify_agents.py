"""Check that the Prolog in ../Code.pl plays the mixtures the analysis assumes.

Everything else here reasons about two probability vectors. This is the only
thing that ties them to the agents that were actually entered: it samples
joue/3 through SWI-Prolog and tests the picks that come back against the
declared weights. Writes:

    agent_sampling.csv   observed and expected share of each pick, per agent

Needs swipl. The Prolog generator is seeded, so the counts reproduce exactly;
two million draws of each agent take about a minute. Run it from this folder:

    python3 verify_agents.py
"""

import csv
import subprocess
from collections import defaultdict
from fractions import Fraction

from scipy.stats import chisquare

CODE = "../Code.pl"
DRAWS = 2_000_000
SEED = 20250415

# What each agent is supposed to play, read off its clause in ../Code.pl.
DECLARED = {
    "stage_test": [0.03, 0.444, 0.203, 0.323, 0.0],
    "nash_equilibrium": [Fraction(0), Fraction(0), Fraction(4, 9),
                         Fraction(2, 9), Fraction(1, 3)],
}

# One line per (agent, pick). clumped/2 drops picks that never came up, so the
# memberchk falls through to zero for those rather than leaving a hole.
SAMPLER = """
set_random(seed({seed})),
forall(member(Agent, [{agents}]),
       ( findall(Move, (between(1, {draws}, _), once(joue(Agent, [], Move))), Moves),
         msort(Moves, Sorted), clumped(Sorted, Counts),
         forall(between(1, 5, Pick),
                ( ( memberchk(Pick-Count, Counts) -> true ; Count = 0 ),
                  format("~w,~w,~w~n", [Agent, Pick, Count]) )) )),
halt
"""


def sampled(agents, draws=DRAWS, seed=SEED):
    """Counts per pick, from `draws` calls to joue/3 for each named agent."""
    goal = SAMPLER.format(seed=seed, draws=draws, agents=", ".join(agents))
    finished = subprocess.run(
        ["swipl", "-g", goal, "-t", "halt(1)", CODE],
        check=True, capture_output=True, text=True,
    )
    counts = defaultdict(lambda: [0] * 5)
    for line in finished.stdout.splitlines():
        agent, pick, count = line.split(",")
        counts[agent][int(pick) - 1] = int(count)
    return counts


def write(name, header, rows):
    with open(name, "w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)
    return rows


if __name__ == "__main__":
    counts = sampled(DECLARED)
    rows = []

    for agent, weights in DECLARED.items():
        drawn = counts[agent]
        if sum(drawn) != DRAWS:
            raise SystemExit(f"{agent}: {sum(drawn)} picks came back, expected {DRAWS}")

        # A pick with no weight must never be drawn, which no goodness-of-fit
        # test would notice, so it is checked separately before the chi-square.
        for pick, (weight, count) in enumerate(zip(weights, drawn), 1):
            if weight == 0 and count:
                raise SystemExit(f"{agent} played {pick} {count} times, weight is zero")
            rows.append((agent, pick, count, f"{float(weight):.6f}", f"{count / DRAWS:.6f}"))

        played = [pick for pick, weight in enumerate(weights) if weight > 0]
        statistic, probability = chisquare([drawn[pick] for pick in played],
                                           [float(weights[pick]) * DRAWS for pick in played])
        # At two million draws the chi-square notices deviations far too small to
        # matter, and its p-value is a lottery on the seed, so the size of the
        # worst deviation is what the check actually turns on.
        drift = max(abs(count / DRAWS - float(weight))
                    for weight, count in zip(weights, drawn))
        if drift > 0.005:
            raise SystemExit(f"{agent} is off its declared mixture by {drift:.4f}")
        if probability < 0.001:
            raise SystemExit(f"{agent} does not play its declared mixture: "
                             f"chi-square {statistic:.1f}, p = {probability:.2e}")
        print(f"{agent:<17} {DRAWS:,} draws, "
              f"never played {[p + 1 for p, w in enumerate(weights) if w == 0]}, "
              f"worst share off by {drift:.6f}, "
              f"chi-square {statistic:.3f} on {len(played) - 1} df, p = {probability:.3f}")

    write("agent_sampling.csv",
          ["agent", "pick", "drawn", "declared_share", "observed_share"], rows)
    print("wrote agent_sampling.csv")
