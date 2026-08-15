# What the two shipped mixtures are actually worth

[`README.md`](README.md) argues about how the equilibrium was *found*. This scores
what was *entered*: the five pure picks and the two mixtures behind `joue/3` in
[`../Code.pl`](../Code.pl), each against each.

```sh
python3 verify_agents.py       # the Prolog plays what it says it plays
python3 strategy_payoffs.py    # writes strategy_payoffs.csv
```

## The agents that actually ran

`verify_agents.py` calls `joue/3` 2,000,000 times per agent and compares the picks
that come back with the declared weights. The generator is seeded, so
`agent_sampling.csv` reproduces exactly.

| agent | worst share off by | never played | chi-square | p |
|---|---:|---|---:|---:|
| `stage_test` | 0.000204 | 5 | 1.490 on 3 df | 0.684 |
| `nash_equilibrium` | 0.000818 | 1, 2 | 6.365 on 2 df | 0.041 |

At two million draws the chi-square notices deviations far too small to matter and
its p-value is a lottery on the seed, so the script turns on the worst deviation
instead. Nothing below is about paper vectors.

## The game, and why the support is 3, 4 and 5

Payoff to the row player. Bold is the undercut: pick one below the opponent and you
take the sum while they take nothing.

| pick | vs 1 | vs 2 | vs 3 | vs 4 | vs 5 | vs Nash | regret |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 3 | 1 | 1 | 1 | 1.0000 | 2.8889 |
| 2 | 0 | 2 | **5** | 2 | 2 | 3.3333 | 0.5556 |
| 3 | 3 | 0 | 3 | **7** | 3 | **3.8889** | 0 |
| 4 | 4 | 4 | 0 | 4 | **9** | **3.8889** | 0 |
| 5 | 5 | 5 | 5 | 0 | 5 | **3.8889** | 0 |

The first five columns are the payoff matrix; the last two are each pick played
against `[0, 0, 4/9, 2/9, 1/3]`. Picks 3, 4 and 5 pay exactly 35/9 while 1 and 2 fall
short, so a best reply can put weight on the first three and none on the last two.
That flat top is the equilibrium condition itself, and it is what the original
derivation was hunting by the wrong criterion.

`stage_test` carries regret 0.3337 against that opponent and 0.5684 against itself.
The best reply to `stage_test` is pick 5, the one pick it never plays: against it the
picks pay 1.8880, 2.5494, 2.9586, 3.1871 and 3.3867, rising all the way to the action
it discarded.

## The round robin

| opponent | `stage_test` | Nash | Nash's margin |
|---|---:|---:|---:|
| 1 | 1.9304 | 3.8889 | +1.9585 |
| 2 | 2.2690 | 2.5556 | +0.2866 |
| 3 | 2.8598 | 3.0000 | +0.1402 |
| 4 | 3.6313 | 4.0000 | +0.3687 |
| 5 | 4.4316 | 5.0000 | +0.5684 |
| `stage_test` | 2.8184 | 3.1521 | +0.3337 |
| Nash | 3.5552 | 3.8889 | +0.3337 |

`stage_test` wins the one column the original notebook looked at, the head to head,
3.5552 against 3.1521. It loses every row of this table. Payoff is linear in the
opponent's mixture, so a strategy beaten against all five pure picks is beaten
against every mixture of them: **the Nash mixture strictly dominates `stage_test`,
by at least 0.1402 whatever the opponent does.** There is no opponent at all against
which `stage_test` does better than simply playing Nash would have.

## Where the margin comes from

`stage_test` wins the head to head by dragging the opponent down further than it
drags itself. Nash falls from 3.8889 to 3.1521, and the loss decomposes by pick:

| Nash's pick | weight | vs Nash | vs `stage_test` | contribution |
|---|---:|---:|---:|---:|
| 3 | 4/9 | 3.8889 | 2.9586 | -0.4135 |
| 4 | 2/9 | 3.8889 | 3.1871 | -0.1559 |
| 5 | 1/3 | 3.8889 | 3.3867 | -0.1674 |

More than half the damage lands on pick 3, and the payoff matrix says why:
`stage_test` puts 0.444 on pick 2, its largest weight, and pick 2 against pick 3 pays
5 to the 2 and 0 to the 3. It buys a 0.4031 margin by giving up 0.3337 of its own
payoff, a good trade when the scoring is a margin and a bad one when it is a total.
The tournament scored totals.
