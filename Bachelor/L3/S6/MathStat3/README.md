# Mathematical Statistics 3

> [Lire en francais](README.fr.md)

**Course:** MathStat3 — Licence 3 MIASHS, Semester 6, Universite Grenoble Alpes

Advanced statistical methods covering hypothesis testing, regression, ANOVA, and non-parametric tests. Each TP builds on the previous one, progressing from basic normality tests to complex multi-factor analysis.

## What You'll Learn

- How to assess normality with QQ-plots, Shapiro-Wilk, and chi-square tests
- Simple and multiple linear regression modeling
- One-way and two-way ANOVA for group comparisons
- Non-parametric alternatives when normality assumptions fail
- Interpreting statistical output and making data-driven decisions

## TP Overview

| TP | Topic | Key Concepts | Datasets |
|----|-------|-------------|----------|
| **TP1** | Normality & Chi-square | QQ-plots, Shapiro-Wilk test, chi-square goodness-of-fit | `titanic.csv` |
| **TP2** | Linear Regression | Simple/multiple regression, coefficient interpretation, R-squared | `tension.csv`, `audition2.csv` |
| **TP3** | One-way ANOVA | F-test, group means comparison, post-hoc tests | `murderusa.csv`, `crime16.csv`, `beignets.txt` |
| **TP4** | Two-way ANOVA & Non-parametric | Interaction effects, Kruskal-Wallis, Wilcoxon tests | `ozone.txt`, `engraisRegion.txt`, `dureteMeche.txt` |
| **Bonus** | Gender & Grades Analysis | Comparing algebra grades (M/F) over 3 years | `alg22.csv`, `alg23.csv`, `alg24.csv` |

## Prerequisites

- Basic probability and statistics (distributions, p-values, confidence intervals)
- [MathStat2](../../S5/MathStat2/) recommended as a foundation
- R programming fundamentals

## Running the Notebooks

Each TP is available in two formats: Quarto (`.qmd`) and Jupyter (`.ipynb`).

```sh
# Quarto
quarto preview TP1/tp1_normalite_chi2.qmd

# Jupyter
jupyter notebook TP1/tp1_normalite_chi2.ipynb
```

## Folder Structure

```
MathStat3/
|-- TP Stat 3.pdf          <- Full course material
|-- TP1/                   <- Normality & chi-square tests
|-- TP2/                   <- Linear regression
|-- TP3/                   <- ANOVA (one factor)
|-- TP4/                   <- ANOVA + non-parametric tests
|   |-- TP_Bonus/          <- Gender & grades analysis
```

## Tools & Libraries

- **R** with base stats functions
- **Quarto** for reproducible reports
- **Jupyter** as an alternative notebook environment
