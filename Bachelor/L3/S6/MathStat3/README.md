# Mathematical Statistics 3

> [Lire en francais](README.fr.md)

**Course:** MathStat3, Licence 3 MIASHS, Semester 6, Universite Grenoble Alpes

Advanced statistical methods covering hypothesis testing, regression, ANOVA, and non-parametric tests. Each TP builds on the previous one, progressing from basic normality tests to complex multi-factor analysis.

## What You'll Learn

- How to assess normality with QQ-plots, Shapiro-Wilk, and chi-square tests
- Simple and multiple linear regression modeling
- One-way and two-way ANOVA for group comparisons
- Non-parametric alternatives when normality assumptions fail
- Interpreting statistical output and making data-driven decisions

## TP Overview

> **Browse all notebooks:** [view index page](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/MathStat3/html/)

| TP | Topic | Key Concepts | Datasets | Live Demo |
|----|-------|-------------|----------|-----------|
| **TP1** | Normality & Chi-square | QQ-plots, Shapiro-Wilk test, chi-square goodness-of-fit | `titanic.csv` | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/MathStat3/html/tp1_normalite_chi2.html) |
| **TP2** | Linear Regression | Simple/multiple regression, coefficient interpretation, R-squared | `tension.csv`, `audition2.csv` | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/MathStat3/html/tp2_regression_lineaire.html) |
| **TP3** | One-way ANOVA | F-test, group means comparison, post-hoc tests | `murderusa.csv`, `crime16.csv`, `beignets.txt` | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/MathStat3/html/tp3_anova_un_facteur.html) |
| **TP4** | Two-way ANOVA & Non-parametric | Interaction effects, Kruskal-Wallis, Wilcoxon tests | `ozone.txt`, `engraisRegion.txt`, `dureteMeche.txt` | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/MathStat3/html/tp4_anova_tests_np.html) |
| **Bonus** | Gender & Grades Analysis | Comparing algebra grades (M/F) over 3 years | `alg22.csv`, `alg23.csv`, `alg24.csv` | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/MathStat3/html/tp_bonus_notes_sexe.html) |

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

## Source material

The 35-page practical handout for this course was written by its teaching staff (UGA).

Not redistributed here; see [NOTICE](../../../../NOTICE) for full credits.
