# APP1: Maze generation and exit-path search

A rectangle carved into a maze by repeated single-doored partitions, solved on
paper as a divide-and-conquer, binary-tree exercise; an implementation in C is
optional.

## State

Under way. The deliverable is written in [report/](report/), one LaTeX folder
per section: the maze is stated as a graph problem and the generation
algorithm is derived and proved, the four sections after that are headings so
far. Implementing it in C is still optional and untouched.

Each question's reasoning, what was rejected and the reference that settled it
are in [steps/](steps/index.html), where the abridged questions are listed too.

## What the handout provides

`main.c`, `maze.h`, `svg.c`, `svg.h` and `Makefile`, unpacked from
`code-as-downloaded.tar.gz` and set up in place. They are consumed unchanged,
not implemented into.

## Running it

Implementing this in C is optional. Once the missing source file exists,
`make` builds the binary from the skeleton above; the course
[README](../README.md) says what keeps a first build from succeeding.

## Where the explanation lives

Not here. The concept note for it is in the Notes vault, under
`S7/Algorithmic Problem Solving/Projects/APP1 - Maze.md`.

## Source material

The subject, and the C skeleton listed above, are by Nguyen Kim Thang, Enikő
Kevi and Lorena León (UGA) and are **not redistributed here**: see
[NOTICE](../../../../../NOTICE). Both sit outside version control: the
subject in `handout/`, PDF beside its `.txt` extraction, and the skeleton
beside it, unchanged from how it was downloaded.
