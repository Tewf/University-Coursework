# Battleship AI Project

> [Lire en francais](README.fr.md)

**Authors:** HAMLIL Mohamed Ali Tewfik · SGHIOUAR IDRISSI Saad
*A two-person university project (Compléments d'IA, L3 MIASHS, Université Grenoble Alpes).*

A complete implementation of the classic Battleship game in Java, with multiple AI strategies, a graphical interface, and statistical tools for evaluating performance.

## What You'll Learn

- Object-oriented design with modular Java packages
- Heuristic and probabilistic AI algorithms
- Monte Carlo simulation techniques
- Statistical evaluation and benchmarking of AI agents
- GUI programming with Java Swing

## AI Strategies

| Strategy | Approach | Description |
|----------|----------|-------------|
| **Uniform** | Random | Shoots randomly across the grid |
| **Markov** | Probabilistic | Uses transition matrices to target likely ship positions |
| **Monte Carlo** | Simulation | Runs simulations to evaluate shot outcomes |
| **Smart** | Hybrid | Combines multiple heuristics for optimal play |

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

All experiment results are saved in `Results/`:
- `tournament_pairwise.csv` — Pairwise win matrix
- `tournament_summary.csv` — Per-bot summary (games, wins, win rate, rank)
- `performance_summary.csv` — Self-play stats (average shots, standard error)
- `performance_gaussian_overlay.png` — Distribution visualization

## Documentation

```sh
# View generated API docs
xdg-open docs/api/index.html

# Compile LaTeX report
cd docs/rapport && make
```
