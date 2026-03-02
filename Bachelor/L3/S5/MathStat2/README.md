# Mathematical Statistics 2

> [Lire en francais](README.fr.md)

**Course:** MathStat2 — Licence 3 MIASHS, Semester 5, Universite Grenoble Alpes

Statistical practicals in R covering simulation, estimation, and hypothesis testing. These sessions build a solid foundation for applied statistical analysis.

## What You'll Learn

- Monte Carlo simulation and bootstrap resampling
- Point estimation: bias, variance, convergence, maximum likelihood
- Confidence interval construction
- Chi-square tests: goodness-of-fit, conformity, homogeneity
- Practical application of statistical theory with real datasets

## TP Overview

| TP | Topic | Key Concepts |
|----|-------|-------------|
| **TP1** | Simulation & Bootstrap | Random generation, resampling, empirical distributions |
| **TP2** | Estimation | Bias, variance, MSE, convergence of estimators |
| **TP3** | Maximum Likelihood | MLE derivation, Fisher information, asymptotic properties |
| **TP4** | Confidence Intervals | Pivotal quantities, coverage probability, sample size |
| **TP5** | Hypothesis Testing | Chi-square tests, conformity, homogeneity, independence |

## Datasets

- `post-199413-Intima_Media.txt` — Post-transverse intima-media thickness measurements
- `post-199414-prevalsidafric.xls` — HIV prevalence data in Africa
- See `data/README.md` for detailed variable descriptions.

## Prerequisites

- Introduction to probability (distributions, expectation, variance)
- Basic R programming
- Fundamental statistical concepts (mean, median, standard deviation)

## Running the Notebooks

```sh
quarto preview TPs/code/TP_Statistiques.qmd
```

## Folder Structure

```
MathStat2/
|-- TPs/
|   |-- code/          <- Quarto notebooks (.qmd)
|   |-- PDFVersion/    <- PDF instructions
|-- data/              <- Datasets with documentation
|-- scripts/           <- Helper R functions (e.g., sigma2.test.R)
```

## Tools & Libraries

- **R** with base stats, tidyverse
- **Quarto** for reproducible reports
- Custom helper scripts in `scripts/`
