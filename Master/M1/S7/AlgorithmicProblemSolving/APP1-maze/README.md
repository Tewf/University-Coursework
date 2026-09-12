# APP1: Maze generation and exit-path search

A rectangle carved into a maze by repeated single-doored partitions, solved on
paper as a divide-and-conquer, binary-tree exercise; an implementation in C is
optional.

## State

Written. The deliverable is [report/](report/), one LaTeX folder per section:
the maze stated as a graph problem, generation derived and proved, one door
costed at one step, the search that follows, and the costs measured against
what the literature says. Implementing it was optional; it is done anyway, in
C++ rather than the provided C skeleton, in [implementation/](implementation/).

Each question's reasoning, what was rejected and the reference that settled it
are in [steps/](steps/index.html), where the abridged questions are listed too.

## What the handout provides

`main.c`, `maze.h`, `svg.c`, `svg.h` and `Makefile`, unpacked from
`code-as-downloaded.tar.gz` and set up in place. They are consumed unchanged,
not implemented into.

## Running it

```bash
cd implementation && cmake -S . -B build && cmake --build build
./build/maze 24 16 7 maze.svg   # width height seed output
./build/benchmark 200           # the report's measurements
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
