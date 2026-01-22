# Mathématiques et Statistiques 2 – Practical sessions

This directory contains practical sessions (TPs) for the MathStat2 course.

## Overview

The `TPs` folder holds Quarto notebooks that explore various statistical topics:

- **Simulation and bootstrap** – generating data and using resampling methods.
- **Estimation and estimator comparison** – studying bias, variance, convergence, confidence intervals, and maximum‑likelihood estimators.
- **Tests de conformité et d'homogénéité** – implementing chi‑square and other goodness‑of‑fit tests.
- **Synthèse / fil conducteur** – integrating multiple concepts.

PDF versions of the instructions are in `TPs/PDFVersion`.

## Data

The `data` folder includes datasets used in the practicals, such as `post-199413-Intima_Media.txt` and `post-199414-prevalsidafric.xls`. A separate README in `data` describes each dataset and its variables.

## Scripts

The `scripts` folder contains auxiliary R functions, for example `sigma2.test.R`, which implements a chi‑square variance test. Each script is documented with usage examples.

## Running the notebooks

Install R and tidyverse packages. Use Quarto to render the `.qmd` files:

```sh
quarto preview TPs/code/TP_Statistiques.qmd
```

Replace the filename to run other labs.

## What I learned

These sessions deepened my understanding of simulation, estimation, hypothesis testing, and the use of R for statistical analysis.
