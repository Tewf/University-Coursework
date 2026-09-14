# APP1: Maze generation and exit-path search

A rectangle carved into a maze by repeated single-doored partitions, solved on
paper as a divide-and-conquer, binary-tree exercise; an implementation in C is
optional.

## State

Written. The deliverable is [report/](report/), seven pages, one LaTeX folder
per section: the problem as a graph problem, the generator and the two
structures it returns, A* on the graph, a lowest-common-ancestor descent on the
tree, the two compared on measurements, and a conclusion.

Implementing it was optional; it is done anyway, in
[implementation/](implementation/), C11 with no dependency outside the standard
library.

## What the handout provides

`main.c`, `maze.h`, `svg.c`, `svg.h` and `Makefile`, unpacked from
`code-as-downloaded.tar.gz` and set up in place. They are consumed unchanged,
not implemented into.

## Running it

```bash
cd implementation && make
./maze 24 16 7 maze.svg   # width height seed output
./benchmark 200           # the report's measurements
make test                 # 1121 assertions
```

The provided C skeleton is not built. It is kept as it was downloaded; the
course [README](../README.md) says what keeps a first build of it from
succeeding.

## Where the explanation lives

Not here. The concept note for it is in the Notes vault, under
`S7/Algorithmic Problem Solving/Projects/APP1 - Maze.md`.

## Source material

The subject, and the C skeleton listed above, are by Nguyen Kim Thang, Enikő
Kevi and Lorena León (UGA) and are **not redistributed here**: see
[NOTICE](../../../../../NOTICE). Both sit outside version control: the
subject in `handout/`, PDF beside its `.txt` extraction, and the skeleton
beside it, unchanged from how it was downloaded.
