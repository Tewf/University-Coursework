# Battleship AI Project

> [Lire en francais](README.fr.md)


**Authors:** HAMLIL Mohamed Ali Tewfik · SGHIOUAR IDRISSI Saad
*A two-person university project (Compléments d'IA, L3 MIASHS, Université Grenoble Alpes).*

Battleship in Java, with four targeting strategies and the tournament machinery
to tell which of them actually works.

## Results

Round-robin tournament, 300 games per bot, and self-play over 100 games to count
how many shots each needs to sink the fleet. Produced by the commands below; raw
output in [`Results/`](Results/).

| Strategy | Approach | Win rate | Mean shots to clear the board |
|---|---|---:|---:|
| **Markov** | Transition matrices over likely ship positions | **74.3%** ±2.5 | **54.8** ±1.2 |
| **Monte Carlo** | Simulation of remaining ship placements | 67.0% ±2.7 | 55.5 ±1.2 |
| **Smart** | Hybrid of several heuristics | 56.7% ±2.9 | 61.1 ±1.1 |
| **Uniform** | Random shots | 2.0% ±0.8 | 94.3 ±0.5 |

The board holds 100 cells, so uniform random needs 94 shots, essentially the
whole grid. Markov clears it in 55, a **42% reduction**, and wins 74% of its
games. Monte Carlo costs far more computation for a slightly worse result, which
is the interesting part: the cheap probabilistic model beats the expensive
simulation here.

## Running the Project

**Requirements:** JDK 11+, POSIX shell

```sh
# Compile
javac -d bin $(find src -name "*.java")

# Launch GUI
java --module-path bin -m ComplementIA/bataillenavale.Main

# Run tournament (e.g., 1000 matches per pair)
java --module-path bin -m ComplementIA/statistique.Tournament 1000

# Run performance analysis (e.g., 100 self-play games per bot)
java --module-path bin -m ComplementIA/statistique.Performance 100
```

## Project Structure

```
Complement_IA-main/
|-- src/
|   |-- bataillenavale/       <- Entry points & UI
|   |-- logique/              <- Core logic (grid, ships, coordinates)
|   |-- joueurs/              <- Players (human, bots)
|   |-- heuristic/            <- AI strategies (Uniform, Markov, MonteCarlo)
|   |-- interfacegraphique/   <- Swing GUI components
|   |-- statistique/          <- Tournament & performance tools
|-- bin/                      <- Compiled classes
|-- docs/
|   |-- api/                  <- Generated JavaDoc
|   |-- rapport/              <- LaTeX report sources
|-- Results/                  <- Experiment outputs (CSV, PNG)
```

## Outputs

`Results/` holds the numbers above: `tournament_summary.csv` and
`tournament_pairwise.csv` for the win rates, `performance_summary.csv` for the
shot counts, and `performance_gaussian_overlay.png` for their distributions.

## Documentation

```sh
# View generated API docs
xdg-open docs/api/index.html

# Compile LaTeX report
cd docs/rapport && make
```
