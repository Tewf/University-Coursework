"""Turn the 636-page tournament log into the tables the README quotes.

Reads ../data2.pdf, the log the course harness produced, and writes:

    leaderboard.csv    final standings, from the result block on page 1
    head_to_head.csv   final score of every pairing, both directions
    repetition.csv     per agent, how much of its play is repetition

Needs poppler-utils for pdftotext. Run it from this folder:

    python3 analyse_log.py
"""

import csv
import re
import subprocess
from collections import Counter

LOG = "../data2.pdf"

STANDING = re.compile(r"\[(\w+),(\d+)\]")
# Whitespace-tolerant on purpose: a round whose payoff runs to tens of digits is
# wrapped across two lines in the PDF, and 248 rounds in this log are.
ROUND = re.compile(
    r"(\w+)\s+joue\s+(\d),\s+(\w+)\s+joue\s+(\d)\s*:\s*"
    r"\[(\d+),(\d+)\]\.\s*Cumul:\s*\[(\d+),(\d+)\]"
)


def read_log(path):
    """The log as plain text, laid out as the harness printed it."""
    return subprocess.run(
        ["pdftotext", "-layout", path, "-"],
        check=True, capture_output=True, text=True, errors="replace",
    ).stdout


def rounds_played(text):
    """Every round in the log as (first, pick, second, pick, gains, cumulative).

    Scanned over the whole text rather than line by line, so wrapped rounds count.
    """
    for match in ROUND.finditer(text):
        yield (match.group(1), match.group(2), match.group(3), match.group(4),
               *(int(match.group(index)) for index in (5, 6, 7, 8)))


def standings(text):
    """Final scores, in order, from the result block that precedes the first round."""
    header, _, _ = text.partition("go.")
    return [(name, int(score)) for name, score in STANDING.findall(header)]


def finals(text):
    """Last cumulative score of each ordered pairing, which is how that match ended."""
    last = {}
    for first, _, second, _, gain_one, gain_two, cumul_one, cumul_two in rounds_played(text):
        last[(first, second)] = (cumul_one, cumul_two)
    return last


def repetition(text):
    """Per agent: rounds played, share spent repeating its previous pick, longest run.

    A run is consecutive rounds on the same number. It matters because this
    version of the game pays a repeated number a power rather than its face value.
    """
    rounds, repeats, longest, run = Counter(), Counter(), Counter(), {}
    for first, pick_one, second, pick_two, gain_one, gain_two, cumul_one, cumul_two in rounds_played(text):
        if (cumul_one, cumul_two) == (gain_one, gain_two):
            run = {}                      # a new pairing starts its cumulative score over
        for who, pick in ((first, pick_one), (second, pick_two)):
            previous, length = run.get(who, (None, 0))
            length = length + 1 if previous == pick else 1
            run[who] = (pick, length)
            rounds[who] += 1
            repeats[who] += length > 1
            longest[who] = max(longest[who], length)
    return rounds, repeats, longest


def record(name, played):
    """(score, opponent score) for every match this agent played.

    The log prints each pairing once, in one order, so both orders are scanned.
    """
    for (first, second), (one, two) in played.items():
        if name == first:
            yield one, two
        elif name == second:
            yield two, one


def write(name, header, rows):
    with open(name, "w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)
    return rows


MINE = {"stage_test", "nash_equilibrium"}

if __name__ == "__main__":
    text = read_log(LOG)
    scores = standings(text)
    played = finals(text)
    rounds, repeats, longest = repetition(text)
    rank = {name: position for position, (name, _) in enumerate(scores, 1)}

    write("leaderboard.csv", ["rank", "agent", "cumulative_score"],
          [(rank[name], name, score) for name, score in scores])

    write("head_to_head.csv", ["agent", "opponent", "score", "opponent_score", "won"],
          sorted((first, second, one, two, int(one > two))
                 for (first, second), (one, two) in played.items()))

    write("repetition.csv", ["rank", "agent", "rounds", "repeat_share", "longest_run"],
          [(rank[name], name, rounds[name], f"{repeats[name] / rounds[name]:.3f}", longest[name])
           for name, _ in scores if rounds[name]])

    # Each agent's leaderboard total is the sum of its matches. Checking it catches
    # dropped rounds, which is how the wrapped-line bug showed up in the first place.
    for name, score in scores:
        total = sum(mine for mine, _ in record(name, played))
        if total != score:
            raise SystemExit(f"{name}: matches sum to {total}, leaderboard says {score}")

    for name in sorted(MINE, key=rank.get):
        matches = list(record(name, played))
        print(f"{name:<17} {rank[name]:>2} of {len(scores)}, {dict(scores)[name]:>9,} points, "
              f"won {sum(one > two for one, two in matches)} of {len(matches)}, "
              f"longest run {longest[name]}, repeats {repeats[name] / rounds[name]:.1%}")
    print(f"khawa_khawa appears in {rounds['khawa_khawa']} rounds")
    print("wrote leaderboard.csv, head_to_head.csv, repetition.csv")
