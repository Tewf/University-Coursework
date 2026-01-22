# Battleship AI Project

This project is a complete implementation of the classic game Battleship (*Bataille Navale*) in Java. It includes several automated players (Uniform, Markov, Monte Carlo, and Smart) as well as a graphical interface. The aim was to design and compare AI strategies for playing Battleship and to provide statistical tools for running tournaments and evaluating performance.

## Code structure

The `src` directory contains modular Java packages for game logic, AI players, heuristics, the graphical user interface, and statistics. The `docs` directory holds generated documentation and a LaTeX report. Outputs such as CSV summaries and performance graphics are saved in the `Results` folder.

## Running the project

Requirements: JDK 11 or newer, a POSIX shell, and Graphviz (optional). To compile the project:

```sh
javac -d out $(find src -name '*.java')
```

To run the graphical version:

```sh
java -cp out gui.Main
```

To launch tournaments and generate statistics, see the `Makefile` or run the provided shell scripts.

## Learning outcomes

Developing this project strengthened my object‑oriented design skills, taught me to implement heuristic and Monte‑Carlo algorithms, and introduced me to statistical evaluation of AI agents.
