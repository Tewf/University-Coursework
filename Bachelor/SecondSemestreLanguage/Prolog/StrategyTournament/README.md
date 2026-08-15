# Strategy Tournament: Prolog agents in a repeated game

> [Lire en français](README.fr.md) · [Open on the site ↗](https://tewf.github.io/University-Coursework/Bachelor/SecondSemestreLanguage/Prolog/StrategyTournament/)

**Authors:** HAMLIL Mohamed Ali Tewfik · [EL KORAICHI Mohamed Yassine](https://github.com/yassine-ek)
*A two-person project. Logic Programming, Licence MIASHS, Université Grenoble Alpes.*

Two strategies were derived on paper, written as Prolog agents, and entered into
a 16-agent tournament against the rest of the year. The interesting part is not
where they placed. It is what the standings turned out to measure.

## Results

![Sixteen agents ranked by cumulative score, log scale](results/leaderboard.png)

`stage_test` finished **7th of 16** with 6,163,877 points and `nash_equilibrium`
**8th** with 1,490,429. Those standings were on page 1 of a 636-page log.

Read the same log match by match and the ranking inverts:

| | agent | cumulative score | matches won |
|---|---|---:|---:|
| 1 | best_duo | 2.02 × 10⁶² | 6 of 15 |
| 2 | naenae | 2.58 × 10⁵⁷ | 9 of 15 |
| 6 | syntax_terror | 6.34 × 10²⁹ | **2 of 15** |
| **7** | **stage_test** | **6,163,877** | **7 of 15** |
| **8** | **nash_equilibrium** | **1,490,429** | 5 of 15 |
| 13 | un_pain_pita | 9,566 | 12 of 15 |
| 14 | ghost | 9,350 | **13 of 15** |

The champion won 6 of its 15 matches. The agent that won 13 of 15 finished 14th.
Across all sixteen, finishing lower correlates with winning **more** matches
(Spearman +0.62 against final rank, p = 0.011). Both entrants beat the eventual
champion in their direct match, 782 to 435 and 490,335 to 4,772.

So the tournament did not rank agents by how often they won. It ranked them by
how much they scored, and those are different objectives.

## Why the scores reach 10⁶²

The tournament ran a modified version of the game in which **repeating a number
multiplies its payoff by that number**, verified on 5,050 of 5,216 consecutive
repeats in the log. One run of `best_duo` playing 5 forty times in a row pays
5⁴⁰, which is 9 × 10²⁷ from a single round.

The two entered agents were derived for the plain version of the game, and both
are stateless: they sample from a fixed distribution and never read the history.

| agent | plays | longest run | repeats |
|---|---|---:|---:|
| `stage_test` | `[0.03, 0.444, 0.203, 0.323, 0.0]` | 10 | 32.9% |
| `nash_equilibrium` | `[0, 0, 4/9, 2/9, 1/3]` | 9 | 35.4% |

Those repeat rates are what independent sampling produces by chance, 34.4% and
35.8%. Every agent that placed above them reached runs of 37 to 100. A fixed
mixed strategy cannot exploit a rule that rewards deliberate repetition, which is
the whole of the gap between 7th and 1st.

## The game

Both players pick an integer from 1 to 5 at the same time. If the picks differ by
exactly one, whoever picked the **smaller** number takes the sum and the other
takes nothing. Otherwise each scores the number they picked. Undercutting by one
is rewarded, so every number invites being undercut.
[`Algorithme_Explication.pdf`](Algorithme_Explication.pdf) derives the 5 × 5
payoff matrix from that rule and sets up the strategy.

`stage_test` comes out of [`Equilibrium_Analysis.ipynb`](Equilibrium_Analysis.ipynb),
and the constants match to the rounding: `Fraction(27, 896)` → `0.03`,
`Fraction(440, 991)` → `0.444`, `Fraction(101, 497)` → `0.203`,
`Fraction(292, 905)` → `0.323`. The analysis and the shipped agent are one object.

`stage_test` also beat `nash_equilibrium` head to head, 1,414 to 661, which is
the ordering the analysis predicted.

## Files

| File | Contents |
|------|----------|
| `Code.pl` | Four agents behind `joue/3`: `stage_test` and `nash_equilibrium` (stateless), `khawa_khawa` (adaptive, best-responds to estimated opponent frequencies), `khawa_khawa_prime` |
| `Algorithme_Explication.pdf` | The game, its payoff matrices, and the proposed strategy |
| `Stage_test.pdf` | How the `stage_test` equilibrium was constructed |
| `Equilibrium_Analysis.ipynb` | The notebook the constants come from |
| `data2.pdf` | The tournament log, 636 pages |
| `results/` | The log turned into CSVs and the chart above |
| `equilibrium/` | The same derivation redone with a condition that is correct on a simplex |

`khawa_khawa` is the substantial agent, and it **does not appear in the log at
all**: zero rounds, against 1,805 for `stage_test` and 1,813 for
`nash_equilibrium`. It was built alongside the entrants rather than entered.

## Two defects in the file, recorded rather than repaired

Neither touched the tournament, because only the two stateless agents were
entered. Both are in the parts that were not.

`khawa_khawa_prime` **returns no move until the history reaches 7 rounds**.
`prefixe(L, N, P) :- length(P, N), append(P, _, L)` demands a prefix of exactly
N elements, so it fails on anything shorter, and `entropie_adv` asks it for 7.
A harness expecting a move every round would have got nothing from this agent
for the first seven of every match.

`random_member/2` is redefined at line 738 and **throws** where the library
version would have worked. It calls `random_between(0, N-1, I)`, passing the
compound term `N-1` where an integer is required, so any call raises
`Type error: integer expected, found 3-1`. Line 1 already imports
`library(random)`, which provides a correct `random_member/2`, and SWI-Prolog
warns on load that the local definition shadows it. It is reached through
`tirage_nash`.

## Running the code

```sh
swipl -s Code.pl          # then query, for example: joue(stage_test, [], Move).
cd results && python3 analyse_log.py && python3 plot_leaderboard.py
```

`analyse_log.py` checks each agent's match scores against its leaderboard total
and stops if they disagree, which is how a parsing bug surfaced.

## Prerequisites

SWI-Prolog for the agents. Python 3 with matplotlib, and poppler-utils for
`pdftotext`, to rebuild the results.

## Source material

The project brief belongs to the course and is not redistributed here; see
[NOTICE](../../../../NOTICE).
