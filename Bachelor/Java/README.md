# Java Programming

> [Lire en francais](README.fr.md) · [Open on the site ↗](https://tewf.github.io/University-Coursework/Bachelor/Java/)

**Course:** Java & AI, Licence MIASHS, Universite Grenoble Alpes

Java coursework covering object-oriented programming fundamentals and a comprehensive AI project.

## Courses

| Project | Description | Folder |
|---------|-------------|--------|
| **Battleship AI** | Multi-strategy AI game with GUI, tournaments, and statistical analysis | [BattleshipAI/](BattleshipAI/README.md) |
| **OOP Exercises** | Progressive exercises from basic classes to design patterns | [OOP/](OOP/README.md) |

## Highlights

### Battleship AI
A complete Battleship game featuring **4 AI strategies**:
- **Uniform**: Random shooting
- **Markov**: Probability-based targeting using transition matrices
- **Monte Carlo**: Simulation-based strategy evaluation
- **Smart**: Combined heuristic approach

Includes a graphical interface (Swing), tournament system, and performance benchmarking with statistical output (CSV, PNG).

### OOP Exercises
Progressive exercises covering:
- Classes, encapsulation, inheritance, polymorphism
- Interfaces, abstract classes, generics
- Exception handling, file I/O
- Mini-projects applying design patterns

## Prerequisites

- JDK 11+
- Basic command-line familiarity

## Quick Start

```sh
# Compile
javac -d bin $(find src -name '*.java')

# Run (example)
java -cp bin package.ClassName
```

See each subfolder's README for specific instructions.
