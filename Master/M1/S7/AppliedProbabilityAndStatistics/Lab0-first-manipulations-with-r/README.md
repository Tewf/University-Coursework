# Lab0: Objects, vectorised code and first random draws

A first R session: object classes, vectorised alternatives to loops, and
simulating from a discrete distribution, worked against a season of football
results and a tumour-measurement dataset.

## State

Not started.

## What the handout provides

`Lab0-first-manipulations-with-r.Rmd`, the R Markdown subject to complete in
place. `saison_2022.csv` and `BreastCancer.csv` sit at the lab root rather
than in `handout/`, since the code loads them directly by that path.
`BreastCancer.csv` is never actually read: the notebook pulls that dataset
from the `mlbench` package instead, and the file simply ships alongside it.

## Running it

```bash
conda activate m1ai-applied-stats
cp handout/Lab0-first-manipulations-with-r.Rmd .
Rscript -e 'rmarkdown::render("Lab0-first-manipulations-with-r.Rmd")'
```

## Where the explanation lives

This folder holds code. The concept note for it is in the Notes vault, under
`S7/Applied Probability and Statistics/Labs/Lab 0 - First Manipulations with R.md`.

## Source material

The handout is by the teaching staff of Applied Probability and Statistics
(M1AM, UGA) and is **not redistributed here**: see
[NOTICE](../../../../../NOTICE). It sits in `handout/`, and `.publishignore`
keeps that directory, along with the two datasets at the lab root, out of
this copy.
