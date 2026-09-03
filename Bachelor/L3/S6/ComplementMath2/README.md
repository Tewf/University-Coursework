# Complement of Mathematics 2: Introduction to Machine Learning

> [Lire en francais](README.fr.md) · [Compare the models ↗](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/)

**Course:** ComplementMath2, Licence 3 MIASHS, Semester 6, Universite Grenoble Alpes

An introduction to supervised machine learning in R, combining practical exercises (TPs) with a comprehensive end-to-end classification project on perfume data.

## What You'll Learn

- Exploratory data analysis and visualization techniques
- Feature engineering from text and categorical data (10 olfactory families)
- Regularized logistic regression (LASSO / Elastic Net) with cross-validation
- Pruned decision trees (Gini impurity, complexity-parameter pruning)
- Random Forest with `ranger` (bagging, mtry tuning, variable importance)
- k-Nearest Neighbors and the curse of dimensionality
- Naive Bayes and unsupervised K-means as complementary baselines
- Model comparison via ROC/AUC, critical analysis, anti-leakage pipeline

## Project: Perfume Satisfaction Prediction

A complete ML pipeline predicting user satisfaction from a dataset of ~24,000 perfumes (Fragrantica).

> **Read the full report:** [HTML book](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/) · [PDF (24 pages)](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/pdf/Pr%C3%A9diction-de-la-Satisfaction-Client-pour-les-Parfums.pdf)

| Step | Notebook | Description | Live Demo |
|------|----------|-------------|-----------|
| 1 | [`01_exploration.qmd`](Projet/notebooks/01_exploration.qmd) | EDA: missing values, target construction, univariate/bivariate distributions | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/01_exploration.html) |
| 2 | [`02_preparation.qmd`](Projet/notebooks/02_preparation.qmd) | Feature engineering (10 olfactory families), stratified 70/30 split (anti-leakage) | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/02_preparation.html) |
| 3 | [`03_regression_logistique.qmd`](Projet/notebooks/03_regression_logistique.qmd) | **LASSO Logistic Regression** (Elastic Net, 5-fold CV) | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/03_regression_logistique.html) |
| 4 | [`04_arbre_decision.qmd`](Projet/notebooks/04_arbre_decision.qmd) | **Pruned Decision Tree** (Gini, optimal `cp`) | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/04_arbre_decision.html) |
| 5 | [`05_foret_aleatoire.qmd`](Projet/notebooks/05_foret_aleatoire.qmd) | **Random Forest** (`ranger`, 500 trees, Gini importance) | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/05_foret_aleatoire.html) |
| 6 | [`06_knn.qmd`](Projet/notebooks/06_knn.qmd) | **k-Nearest Neighbors** with curse-of-dimensionality diagnosis | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/06_knn.html) |
| 7 | [`07_comparaison.qmd`](Projet/notebooks/07_comparaison.qmd) | ROC comparison, **Naive Bayes** & **K-means** (rejected paths), critique, AI usage | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/07_comparaison.html) |

### Project Structure

```
Projet/
├── _quarto.yml             # Quarto book configuration (HTML + PDF)
├── index.qmd               # Introduction / abstract
├── notebooks/              # 7-step sequential analysis pipeline
├── utils.R                 # Shared helpers (10 olfactory families, CV control)
├── data/fra_cleaned.csv    # Perfume dataset (~24k rows, gitignored)
├── output/*.rds            # Filesystem cache for trained models (gitignored)
├── rapport/                # Rendered HTML book + PDF (served via GitHub Pages)
├── references.bib          # Bibliography
└── README.md
```

## Practical Sessions (TPs)

8 TPs covering foundational ML concepts using the Titanic and Iris datasets:

> **Browse all TPs:** [view index page](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/)

| TP | Topic | Live Demo |
|----|-------|-----------|
| **TP1** | Data exploration | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/Correction%20TP%201.html) |
| **TP2** | Data preprocessing | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/Correction%20TP2.html) |
| **TP3** | Evaluation metrics & cross-validation | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/Correction%20TP3.html) |
| **TP4** | Feature transformation & imputation | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/Correction%20TP4.html) |
| **TP5** | KNN classification | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/Correction%20TP5.html) |
| **TP6** | Naive Bayes classification | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/Correction%20TP6.html) |
| **TP7** | Decision trees | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/Correction%20TP7.html) |
| **TP8** | Unsupervised learning (K-means clustering) | [view](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/Correction%20TP8.html) |

Each TP folder contains the problem statement (`.Rmd`/`.pdf`) and corrections (`.qmd`/`.pdf`).

## Prerequisites

- Statistics fundamentals (regression, hypothesis testing)
- R programming with tidyverse
- [MathStat2](../../S5/MathStat2/README.md) and [MathStat3](../MathStat3/README.md) recommended

## Running the Notebooks

```sh
# Project notebooks
quarto preview Projet/notebooks/01_exploration.qmd

# TP corrections
quarto preview TP/TP1/Correction\ TP\ 1.qmd
```

## Tools & Libraries

- **R**: tidyverse, caret, glmnet, ranger, rpart, rpart.plot, naivebayes, pROC, corrplot
- **Quarto**: reproducible reports with code and narrative (HTML book + PDF)
- **TeX Live / TinyTeX**: PDF rendering via lualatex

## Source material

Practical subjects TP1–TP5 were written by **Lola Etiévant** (Université Grenoble Alpes). The solutions in this directory are mine; the questions they answer are hers.

Not redistributed here; see [NOTICE](../../../../NOTICE) for full credits.
