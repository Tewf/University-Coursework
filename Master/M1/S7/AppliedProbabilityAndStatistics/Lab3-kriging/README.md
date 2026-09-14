# Lab3: Gaussian vectors and kriging for temperature forecasts

Simulating a Gaussian vector from a square root of its covariance, then a
kriging forecast of August 2003 temperatures across France from a handful of
weather stations.

## State

Not started.

## What the handout provides

`Lab3-kriging.pdf`, the subject, with a `.txt` extraction alongside it, and
`Lab3-kriging.Rmd`, the notebook to complete in place. The teaching staff's
own `Lab-Solutions.r` sits beside them. `data_temperatures.Rdata`,
`frontieres_france.Rdata` and `grille_france.Rdata` sit at the lab root
rather than in `handout/`, since the code loads them directly by that path.

## Running it

```bash
conda activate m1ai-applied-stats
cp handout/Lab3-kriging.Rmd .
Rscript -e 'rmarkdown::render("Lab3-kriging.Rmd")'
```

## Where the explanation lives

This folder holds code. The concept note for it is in the Notes vault, under
`S7/Applied Probability and Statistics/Labs/Lab 3 - Meteorological Forecast by Kriging.md`.
The map of all of them is `obsidian-note.local.md` at the course root, which
is gitignored because it names local paths.

## Source material

The handout is by the teaching staff of Applied Probability and Statistics
(M1AM, UGA) and is **not redistributed here**: see
[NOTICE](../../../../../NOTICE). It sits in `handout/`, and `.publishignore`
keeps that directory, along with the three `.Rdata` files at the lab root,
out of the public repository.
