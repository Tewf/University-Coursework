"""Draw the final standings from leaderboard.csv, for the README.

The site page charts the same file client-side; this is the static copy that
markdown can show. Run analyse_log.py first, then:

    python3 plot_leaderboard.py
"""

import csv

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

MINE = {"stage_test", "nash_equilibrium"}

with open("leaderboard.csv", newline="") as handle:
    standings = [(row["agent"], float(row["cumulative_score"]))  # exact ints reach 10**62
                 for row in csv.DictReader(handle)]              # and overflow the C long

names = [name for name, _ in standings][::-1]
scores = [score for _, score in standings][::-1]
colours = ["#2ca02c" if name in MINE else "#c0c4c8" for name in names]

figure, axes = plt.subplots(figsize=(9, 6))
axes.barh(names, scores, color=colours)
axes.set_xscale("log")
axes.set_xlabel("cumulative score, log scale")
axes.set_title("Tournoi n° 1, April 2025, L2 MIASHS UGA: 16 agents")
for row, (name, score) in enumerate(zip(names, scores)):
    if name in MINE:
        axes.text(score * 1.6, row, f"{int(score):,}", va="center",
                  fontsize=9, color="#1a7431")
axes.spines[["top", "right"]].set_visible(False)
figure.tight_layout()
figure.savefig("leaderboard.png", dpi=110, bbox_inches="tight")
print("wrote leaderboard.png")
