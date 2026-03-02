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

> **Browse all project notebooks:** [view index page](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/html/)

| Step | Notebook | Description | Live Demo |
|------|----------|-------------|-----------|
| 1 | `01_exploration.qmd` | Exploratory Data Analysis: distributions, missing values, visualizations | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/html/01_exploration.html) |
| 2 | `02_preparation.qmd` | Feature engineering, imputation, train/test split (70/30) | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/html/02_preparation.html) |
| 3 | `03_regression_logistique.qmd` | Logistic regression with Elastic Net (5-fold CV) | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/html/03_regression_logistique.html) |
| 4 | `04_foret_aleatoire.qmd` | Random Forest (500 trees) with tuning | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/html/04_foret_aleatoire.html) |
| 5 | `05_comparaison.qmd` | Model comparison, ROC curves, final evaluation | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/html/05_comparaison.html) |

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

> **Browse all TPs:** [view index page](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/)

| TP | Topic | Live Demo |
|----|-------|-----------|
| **TP1** | Data exploration | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/Correction%20TP%201.html) |
| **TP2** | Data preprocessing | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/Correction%20TP2.html) |
| **TP3** | Evaluation metrics & cross-validation | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/Correction%20TP3.html) |
| **TP4** | Feature transformation & imputation | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/Correction%20TP4.html) |
| **TP5** | KNN classification | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/Correction-TP5.html) |
| **TP6** | Naive Bayes classification | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/Correction%20TP6.html) |

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
