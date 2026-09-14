# Lab2: N-queens, Sudoku, cryptarithmetic and family models

Four constraint-programming models in OR-Tools: N-queens two ways, a Sudoku
solver, a generic cryptarithmetic solver, and family queries over the Game
of Thrones dataset.

## State

Not started.

## What the handout provides

`Lab2-constraint-programming.pdf` is the subject. `got.csv` is the same
character dataset the Datalog lab uses, this time loaded as integers for
OR-Tools.

## Running it

```bash
conda activate m1ai-intro-ai
```

`ortools` is already declared in the course's `environment.yml`. The Sudoku
question additionally needs `dokusan`, installed separately with
`pip install dokusan` inside that environment, since the shared file does
not carry it.

## Where the explanation lives

This folder holds code. The concept note for it is in the Notes vault, under
`S7/Introduction to AI/Labs - Symbolic AI/Lab 2 - Constraint Programming.md`.
The map of all of them is `obsidian-note.local.md` at the course root, which
is gitignored because it names local paths.

## Source material

The subject is by Sylvain Bouveret (Grenoble INP, UGA) and is **not
redistributed here**: see [NOTICE](../../../../../../NOTICE). It sits in
`handout/` beside its `.txt` extraction, and `.publishignore` keeps that
directory and the dataset out of the public repository.
