# M1 Artificial Intelligence

> [Lire en français](README.fr.md)

First year of the [Master of Artificial Intelligence](https://m-ai.imag.fr/) at
Université Grenoble Alpes, jointly delivered by UFR IM²AG and Ensimag
(Grenoble INP). Every M1 course is compulsory, so the folders below fill in the
order the semesters are taught.

## Semester 7

| Course | Topic | Languages | Folder |
|--------|-------|-----------|--------|
| Programming | Python tooling and data, C++ and CMake, pybind11 interop, a TSP solver | Python, C++ | [S7/Programming/](S7/Programming/README.md) |
| Algorithmic Problem Solving | Divide and conquer, dynamic programming, flows and cuts, spanning trees, approximation; four APP projects solved on paper, one with a C skeleton | C | [S7/AlgorithmicProblemSolving/](S7/AlgorithmicProblemSolving/README.md) |
| Introduction to AI | Seven machine-learning notebooks from model evaluation to recurrent networks; Datalog and constraint programming | Python | [S7/IntroductionToAI/](S7/IntroductionToAI/README.md) |
| Applied Probability and Statistics | Simulation, estimators, Gaussian vectors and kriging, in R Markdown | R | [S7/AppliedProbabilityAndStatistics/](S7/AppliedProbabilityAndStatistics/README.md) |

## Semester 8

Not started.

## Runtimes

Each course folder declares its own dependencies. The Programming course uses a
conda environment for Python and `apt` for the C++ libraries; see
[S7/Programming/README.md](S7/Programming/README.md). Introduction to AI and
Applied Probability and Statistics each declare a conda environment of their
own (`m1ai-intro-ai`, `m1ai-applied-stats`); Algorithmic Problem Solving needs
only `gcc` and `make`.

