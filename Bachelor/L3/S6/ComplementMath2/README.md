# Complement of Mathematics 2 — Introduction to Machine Learning

> [Lire en francais](README.fr.md)

**Course:** ComplementMath2 — Licence 3 MIASHS, Semester 6, Universite Grenoble Alpes

An introduction to supervised machine learning in R, combining practical exercises (TPs) with a comprehensive end-to-end classification project on perfume data.

## What You'll Learn

- Exploratory data analysis and visualization techniques
- Feature engineering from text and categorical data
- Logistic regression with Elastic Net regularization
- Random Forest classification and hyperparameter tuning
- Model evaluation: accuracy, ROC curves, variable importance
- Cross-validation and train/test methodology

## Project: Perfume Satisfaction Prediction

A complete ML pipeline predicting user satisfaction from a dataset of ~60,000 perfumes.

| Step | Notebook | Description |
|------|----------|-------------|
| 1 | `01_exploration.qmd` | Exploratory Data Analysis: distributions, missing values, visualizations |
| 2 | `02_preparation.qmd` | Feature engineering, imputation, train/test split (70/30) |
| 3 | `03_regression_logistique.qmd` | Logistic regression with Elastic Net (5-fold CV) |
| 4 | `04_foret_aleatoire.qmd` | Random Forest (500 trees) with tuning |
| 5 | `05_comparaison.qmd` | Model comparison, ROC curves, final evaluation |

### Project Structure

```
Projet/
|-- data/parfumo_data_clean.csv    <- Perfume dataset (~60k rows)
|-- R/utils.R                      <- Shared utility functions
|-- notebooks/                     <- Sequential analysis pipeline
|-- output/                        <- Intermediate .rds files
|-- rapport/                       <- Generated PDF reports
```

## Practical Sessions (TPs)

6 TPs covering foundational ML concepts using the Titanic dataset:

| TP | Topic |
|----|-------|
| TP1-TP2 | Data exploration and preprocessing |
| TP3-TP4 | Classification models |
| TP5-TP6 | Model evaluation and comparison |

Each TP folder contains the problem statement (`.Rmd`/`.pdf`) and corrections (`.qmd`/`.pdf`).

## Prerequisites

- Statistics fundamentals (regression, hypothesis testing)
- R programming with tidyverse
- [MathStat2](../../S5/MathStat2/) and [MathStat3](../MathStat3/) recommended

## Running the Notebooks

```sh
# Project notebooks
quarto preview Projet/notebooks/01_exploration.qmd

# TP corrections
quarto preview TP/TP1/Correction\ TP1.qmd
```

## Tools & Libraries

- **R**: tidyverse, caret, glmnet, randomForest, pROC
- **Quarto**: reproducible reports with code and narrative
