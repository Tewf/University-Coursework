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
| Operations Research | Linear and integer programming, duality, branch and bound, constraint programming; 37 Caseine exercises in OPL and pychoco | OPL, Python | [S7/OperationsResearch/](S7/OperationsResearch/README.md) |
| Data Acquisition, Processing and Mining for AI | Pulling data from a live API, cleaning and exploring it, and mining it for something interpretable; weekly labs and a paired project marked out of 20 | Python | [S7/DataAcquisitionProcessingAndMiningForAI/](S7/DataAcquisitionProcessingAndMiningForAI/README.md) |

## Semester 8

Not started.

## Projects done with a partner

The TSP solver and the data-mining project are shared with a partner through
a private repository each, where nothing is ignored. Their folders here are
the work tree of both repositories at once: plain `git` is this one, and
`private-git NAME` the private one. How it works, and the one-line setup on a
new clone: [private-projects/](private-projects/README.md).

## Runtimes

Each course folder declares its own dependencies. The Programming course uses a
conda environment for Python and `apt` for the C++ libraries; see
[S7/Programming/README.md](S7/Programming/README.md). Introduction to AI and
Applied Probability and Statistics each declare a conda environment of their
own (`m1ai-intro-ai`, `m1ai-applied-stats`); Algorithmic Problem Solving needs
only `gcc` and `make`. Data Acquisition, Processing and Mining for AI runs in
`datacq`, an environment the staff ship rather than one written here, so its
`environment.yml` stays in that course's `handout/` with the rest of their
material.

