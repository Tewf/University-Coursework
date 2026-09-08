# Algorithmic Problem Solving

> [Lire en français](README.fr.md)

**Course:** Algorithmic Problem Solving, M1 Artificial Intelligence, Semester 7, Université Grenoble Alpes
**Teaching staff:** Nguyen Kim Thang (responsable), with Enikő Kevi and Lorena León on the projects

Four APP projects, two tutorials and a past exam. The course is taught by
*apprentissage par problème*: each APP is solved on paper by a group across four
sessions, and an implementation is optional. This folder is the practical side —
the subjects, the code provided with them, and whatever I write against them.

## What's Here

| Folder | Subject | Solves it with |
|---|---|---|
| [APP1-maze/](APP1-maze/) | Generate a random maze by recursive division, then find the unique path to its exit | Divide and conquer, binary trees, traversals, complexity |
| [APP2-candy-crush/](APP2-candy-crush/) | Candy Crush | Where greedy fails, then dynamic programming |
| [APP3-scheduling/](APP3-scheduling/) | School scheduling | Maximum flow, minimum cut, reduction |
| [APP4-hole-drilling/](APP4-hole-drilling/) | Hole drilling | Minimum spanning tree, 2-approximation of the tour |
| [TD1-optimal-bst/](TD1-optimal-bst/) | Optimal binary search tree | Dynamic programming |
| [TD2-bipartite-matching/](TD2-bipartite-matching/) | Maximum-cardinality bipartite matching | Reduction to maximum flow |
| [exam-2024/](exam-2024/) | Exam of 5 December 2024 | Matching, knapsack (DP then greedy), disjoint paths |

Only APP1 ships code. Its skeleton (`main.c`, `maze.h`, `svg.c/.h`, `Makefile`)
builds with `gcc -g -Wall -O0 -Werror` and is deliberately incomplete: `maze.c`,
holding `maze_random()` and `maze_svg()`, is the part to write.

```bash
cd APP1-maze/code && make      # fails until maze.c exists
```

## Folder Structure

Each subject gets its own folder, with the PDF and a `.txt` extraction of it in
`handout/` so the statement is greppable next to the work.

```
AlgorithmicProblemSolving/
|-- APP1-maze/
|   |-- handout/               <- the subject PDF beside its .txt extraction
|   |-- code/                  <- the provided C skeleton, and my maze.c
|   |-- code-as-downloaded.tar.gz
|-- APP2-candy-crush/ ... APP4-hole-drilling/
|-- TD1-optimal-bst/ TD2-bipartite-matching/
|-- exam-2024/
```

## Where the explanations live

Not here. The concepts each subject needs — divide and conquer, the master
theorem, tree traversals, dynamic programming, flows and cuts, spanning trees,
approximation ratios — are written up in a separate Obsidian vault, one note per
concept, along with the lecture slides they come from. Each subject there maps
its questions to the concepts they need. A comment here that starts teaching
theory belongs in that note instead.

## Source material

The subjects, and the C skeleton provided with APP1, are **not redistributed
here**: see [NOTICE](../../../../NOTICE). They stay on disk in each `handout/`
directory, and `.gitignore` keeps both them and the skeleton out of the
repository. What is committed is my own work.
