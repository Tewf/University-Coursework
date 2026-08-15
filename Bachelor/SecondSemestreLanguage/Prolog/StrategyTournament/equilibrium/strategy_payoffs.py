"""Score every strategy against every other, for the charts the project page draws.

Rebuilds the 5x5 game from its rule and writes:

    strategy_payoffs.csv   payoff and regret for each strategy against each
                           opponent, over the five pure picks plus the two
                           mixtures Code.pl ships

The pure-against-pure rows are the payoff matrix itself, so the file holds the
game and the comparison at once. equilibrium_recomputed.ipynb keeps its own copy
of the two definitions below so it reads as a standalone argument; this is what
produces the committed CSV. Run it from this folder:

    python3 strategy_payoffs.py
"""

import csv
from fractions import Fraction

import numpy as np

PICKS = (1, 2, 3, 4, 5)

# The two mixtures behind joue/3 in ../Code.pl. stage_test is rebuilt from the
# fractions the original notebook printed, which round to the shipped constants.
STAGE_TEST = (Fraction(27, 896), Fraction(440, 991), Fraction(101, 497),
              Fraction(292, 905), Fraction(0))
NASH = (Fraction(0), Fraction(0), Fraction(4, 9), Fraction(2, 9), Fraction(1, 3))


def build_game(picks=PICKS):
    """Payoff to the row player: differ by one and the smaller pick takes the sum."""
    payoff = np.zeros((len(picks), len(picks)))
    for row, mine in enumerate(picks):
        for column, theirs in enumerate(picks):
            if abs(mine - theirs) != 1:
                payoff[row, column] = mine
            else:
                payoff[row, column] = mine + theirs if mine < theirs else 0
    return payoff


def regret(mine, theirs, payoff):
    """What the row player leaves on the table by not playing a best reply."""
    return (payoff @ theirs).max() - mine @ payoff @ theirs


def normalised(weights):
    """A mixture as floats summing to one, from the exact fractions above."""
    vector = np.array([float(weight) for weight in weights])
    return vector / vector.sum()


def strategies():
    """Every strategy compared here: the five pure picks, then the two mixtures."""
    for index, pick in enumerate(PICKS):
        yield str(pick), np.eye(len(PICKS))[index]
    yield "stage_test", normalised(STAGE_TEST)
    yield "nash_equilibrium", normalised(NASH)


def write(name, header, rows):
    with open(name, "w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)
    return rows


if __name__ == "__main__":
    payoff = build_game()
    named = list(strategies())
    against = dict(named)

    write("strategy_payoffs.csv", ["strategy", "opponent", "payoff", "regret"],
          [(name, opponent, f"{mine @ payoff @ theirs:.4f}",
            f"{regret(mine, theirs, payoff):.4f}")
           for name, mine in named for opponent, theirs in named])

    stage_test, nash = against["stage_test"], against["nash_equilibrium"]

    # Every number the write-ups quote, checked against this run rather than
    # against the prose. A mismatch means the two have drifted apart.
    quoted = {
        "nash against nash": (nash @ payoff @ nash, 3.8889),
        "stage_test against nash": (stage_test @ payoff @ nash, 3.5552),
        "nash against stage_test": (nash @ payoff @ stage_test, 3.1521),
        "stage_test regret against itself": (regret(stage_test, stage_test, payoff), 0.5684),
        "nash regret against itself": (regret(nash, nash, payoff), 0.0),
    }
    for label, (found, expected) in quoted.items():
        if round(found, 4) != expected:
            raise SystemExit(f"{label}: computed {found:.4f}, the write-ups say {expected}")

    # The support is exactly the picks that tie for the best reply to Nash.
    support = [pick for index, pick in enumerate(PICKS)
               if abs((payoff @ nash)[index] - (payoff @ nash).max()) < 1e-9]
    if support != [3, 4, 5]:
        raise SystemExit(f"support of the best reply to Nash is {support}, expected [3, 4, 5]")

    # Payoff is linear in the opponent's mixture, so beating stage_test against
    # every pure pick is the same as beating it against every mixture.
    edge = (nash - stage_test) @ payoff
    if not (edge > 0).all():
        raise SystemExit(f"Nash does not out-earn stage_test everywhere: {np.round(edge, 4)}")

    print("payoff to each pick against a Nash opponent: "
          f"{np.round(payoff @ nash, 4)}, so the support is {support}")
    print(f"stage_test earns {stage_test @ payoff @ nash:.4f} against Nash "
          f"and Nash earns {nash @ payoff @ stage_test:.4f} back, "
          f"against {nash @ payoff @ nash:.4f} for Nash against itself")
    print(f"Nash out-earns stage_test against every opponent, by at least {edge.min():.4f}")
    print("wrote strategy_payoffs.csv")
