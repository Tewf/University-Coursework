# Algorithmic Problem Solving

> [Lire en français](README.fr.md)

**Course:** Algorithmic Problem Solving, M1 Artificial Intelligence, Semester 7, Université Grenoble Alpes
**Teaching staff:** Nguyen Kim Thang (responsable), with Enikő Kevi and Lorena León on the projects

The course is taught by *apprentissage par problème*: four APP projects, each
solved by a group across several sessions. Implementing one is optional — which
is exactly why all four have a folder here waiting, statement included. When a
project is worth coding, the place to code it already exists.

The two tutorials and the past exam are not here. They are worked on paper and
hand in nothing, so they live in the notes vault with the rest of the course.

## The projects

| Folder | Problem | Solved with | Code |
|---|---|---|---|
| [APP1-maze/](APP1-maze/) | Generate a random maze by recursive division, then find the unique path to its exit | Divide and conquer, binary trees, traversals | skeleton provided |
| [APP2-candy-crush/](APP2-candy-crush/) | Candy Crush | Where greedy fails, then dynamic programming | — |
| [APP3-scheduling/](APP3-scheduling/) | School scheduling | Maximum flow, minimum cut, reduction | — |
| [APP4-hole-drilling/](APP4-hole-drilling/) | Hole drilling | Minimum spanning tree, 2-approximation of the tour | — |

## APP1 — Be Amazed

The one subject that ships code. A maze built by dividing an area with a full
wall bearing one door, then recursing on each half, is a binary tree — which is
the point of the exercise: its generation is divide and conquer, its solving is a
tree traversal, and its cost analysis is the recurrence that falls out.

The provided skeleton is `main.c`, `maze.h`, `svg.c/.h` and a `Makefile` that
compiles with `gcc -g -Wall -O0 -Werror`. It is deliberately incomplete:
`maze.c`, holding `maze_random()` and `maze_svg()`, is the part to write.

```bash
cd APP1-maze && make      # fails until maze.c exists
```

Two things to expect on a first build. `make` cannot succeed before `maze.c`
exists, since `main.c` calls both of its functions. And `main.c` as shipped
declares an `unsigned int len;` it never uses, which `-Wall -Werror` turns into
an error under gcc 13.3 — that line has to go even once `maze.c` is there.

## Folder Structure

Each project keeps its statement in `handout/`, beside a `.txt` extraction that
makes it greppable next to the work. `.gitignore` excludes every one of them, so
what a folder shows on GitHub is the code and nothing else — and a folder with no
code yet shows nothing at all.

```
AlgorithmicProblemSolving/
|-- APP1-maze/
|   |-- handout/               <- the subject PDF beside its .txt extraction
|   |-- main.c maze.h svg.c/.h Makefile   <- the provided skeleton, and my maze.c
|   |-- code-as-downloaded.tar.gz
|-- APP2-candy-crush/ ... APP4-hole-drilling/
```

## Where the explanations live

Not here. The concepts each subject needs — divide and conquer, the master
theorem, tree traversals, dynamic programming, flows and cuts, spanning trees,
approximation ratios — are written up in a separate Obsidian vault, one note per
concept, alongside the lecture slides they come from and the paper solutions —
tutorials and exam included. Each subject there maps its questions to the
concepts they need. A comment here that starts teaching theory belongs in that
note instead.

## Source material

The subjects, and the C skeleton provided with APP1, are **not redistributed
here**: see [NOTICE](../../../../NOTICE). They stay on disk in each `handout/`
directory, and `.gitignore` keeps both them and the skeleton out of the
repository. What is committed is my own work.
