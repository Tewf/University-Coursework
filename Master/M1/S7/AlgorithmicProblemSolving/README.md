# Algorithmic Problem Solving

> [Lire en français](README.fr.md)

**Course:** Algorithmic Problem Solving, M1 Artificial Intelligence, Semester 7, Université Grenoble Alpes
**Teaching staff:** Nguyen Kim Thang (responsable), with Enikő Kevi and Lorena León on the projects

The course is taught by *apprentissage par problème*: four APP projects and two
tutorials, each solved on paper by a group across several sessions. Only APP1
comes with code, and even there the implementation is optional — so this folder
holds one C project and nothing else. The subjects, the lecture material and the
write-ups all live in the notes vault, which is where a problem solved on paper
belongs.

## APP1 — Be Amazed

[APP1-maze/](APP1-maze/) generates a random maze by dividing its area with a full
wall bearing one door, recursing on each half, then finds the unique path from
any position to the exit. A maze built that way is a binary tree, which is the
point of the exercise: its generation is divide and conquer, its solving is a
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

## Where everything else lives

Not here. The subject PDFs, the lecture slides, the concepts each question needs
— divide and conquer, the master theorem, tree traversals, dynamic programming,
flows and cuts, spanning trees, approximation ratios — and the paper solutions to
APP2–APP4, the two TDs and the past exam are all in a separate Obsidian vault,
one note per concept. A comment here that starts teaching theory belongs in that
note instead.

## Source material

The C skeleton shipped with APP1 is **not redistributed here**: see
[NOTICE](../../../../NOTICE). It stays on disk and `.gitignore` keeps it out of
the repository. What is committed is the implementation written against it.
