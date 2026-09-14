# Lab1: Real random variables: CDFs, densities and simulation

Distribution functions, densities and expectations for the exponential and
normal laws, worked by hand and checked by simulation, plus a change-of-variable
construction for a piecewise mixture variable built out of two uniforms.

## State

Not started. Each question's reasoning, what was rejected and the reference
that settled it are in [steps/](steps/index.html), where the abridged
questions are listed too.

## What the handout provides

`Lab1-real-random-variables.Rmd`, the R Markdown subject to complete in
place. No datasets: every question draws its own sample.

## Running it

```bash
conda activate m1ai-applied-stats
cp handout/Lab1-real-random-variables.Rmd .
Rscript -e 'rmarkdown::render("Lab1-real-random-variables.Rmd")'
```

## Where the explanation lives

This folder holds code. The concept note for it is in the Notes vault, under
`S7/Applied Probability and Statistics/Labs/Lab 1 - Real Random Variables.md`.
The map of all of them is `obsidian-note.local.md` at the course root, which
is gitignored because it names local paths.

## Source material

The handout is by the teaching staff of Applied Probability and Statistics
(M1AM, UGA) and is **not redistributed here**: see
[NOTICE](../../../../../NOTICE). It sits in `handout/`, and `.publishignore`
keeps that directory out of the public repository.
