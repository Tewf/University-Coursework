# Complements de mathematiques 2 — Introduction au Machine Learning

> [Read in English](README.md)

**Cours :** ComplementMath2 — Licence 3 MIASHS, Semestre 6, Universite Grenoble Alpes

Une introduction a l'apprentissage automatique supervise en R, combinant des travaux pratiques (TPs) avec un projet de classification complet de bout en bout sur des donnees de parfums.

## Ce que vous apprendrez

- Analyse exploratoire et visualisation
- Ingenierie de features a partir de donnees textuelles et categorielles (10 familles olfactives)
- Regression logistique regularisee (LASSO / Elastic Net) avec validation croisee
- Arbres de decision elagues (impurete de Gini, parametre de complexite)
- Foret aleatoire avec `ranger` (bagging, tuning de mtry, importance des variables)
- k Plus Proches Voisins et malediction de la dimensionnalite
- Naive Bayes et K-means non supervise comme baselines complementaires
- Comparaison de modeles via ROC/AUC, regard critique, pipeline anti-leakage

## Projet : Prediction de la satisfaction pour les parfums

Un pipeline ML complet predisant la satisfaction des utilisateurs a partir d'un jeu de donnees de ~24 000 parfums (Fragrantica).

> **Lire le rapport complet :** [livre HTML](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/) · [PDF (24 pages)](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/pdf/Pr%C3%A9diction-de-la-Satisfaction-Client-pour-les-Parfums.pdf)

| Etape | Notebook | Description | Demo |
|-------|----------|-------------|------|
| 1 | [`01_exploration.qmd`](Projet/notebooks/01_exploration.qmd) | EDA : valeurs manquantes, construction de la cible, distributions | [voir](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/01_exploration.html) |
| 2 | [`02_preparation.qmd`](Projet/notebooks/02_preparation.qmd) | Feature engineering (10 familles olfactives), split 70/30 stratifie anti-leakage | [voir](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/02_preparation.html) |
| 3 | [`03_regression_logistique.qmd`](Projet/notebooks/03_regression_logistique.qmd) | **Regression Logistique LASSO** (Elastic Net, CV 5-fold) | [voir](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/03_regression_logistique.html) |
| 4 | [`04_arbre_decision.qmd`](Projet/notebooks/04_arbre_decision.qmd) | **Arbre de Decision** elague (Gini, `cp` optimal) | [voir](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/04_arbre_decision.html) |
| 5 | [`05_foret_aleatoire.qmd`](Projet/notebooks/05_foret_aleatoire.qmd) | **Foret Aleatoire** (`ranger`, 500 arbres, importance Gini) | [voir](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/05_foret_aleatoire.html) |
| 6 | [`06_knn.qmd`](Projet/notebooks/06_knn.qmd) | **k Plus Proches Voisins** avec diagnostic de la dimensionnalite | [voir](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/06_knn.html) |
| 7 | [`07_comparaison.qmd`](Projet/notebooks/07_comparaison.qmd) | Comparaison ROC, **Naive Bayes** & **K-means** (pistes ecartees), critique, IA | [voir](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/07_comparaison.html) |

### Structure du projet

```
Projet/
├── _quarto.yml             # Configuration du livre Quarto (HTML + PDF)
├── index.qmd               # Introduction / abstract
├── notebooks/              # Pipeline d'analyse sequentielle (7 etapes)
├── utils.R                 # Helpers partages (10 familles olfactives, CV control)
├── data/fra_cleaned.csv    # Jeu de donnees parfums (~24k lignes, gitignored)
├── output/*.rds            # Cache filesystem des modeles entraines (gitignored)
├── rapport/                # Livre HTML + PDF (servis via GitHub Pages)
├── references.bib          # Bibliographie
└── README.md
```

## Travaux Pratiques (TPs)

8 TPs couvrant les concepts fondamentaux du ML avec les jeux de donnees Titanic et Iris :

> **Parcourir tous les TPs :** [voir la page d'index](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/)

| TP | Theme | Demo |
|----|-------|------|
| **TP1** | Exploration des donnees | [voir](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/Correction%20TP%201.html) |
| **TP2** | Preprocessing des donnees | [voir](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/Correction%20TP2.html) |
| **TP3** | Metriques d'evaluation & validation croisee | [voir](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/Correction%20TP3.html) |
| **TP4** | Transformation de features & imputation | [voir](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/Correction%20TP4.html) |
| **TP5** | Classification KNN | [voir](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/Correction%20TP5.html) |
| **TP6** | Classification naive bayesienne | [voir](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/Correction%20TP6.html) |
| **TP7** | Arbres de decision | [voir](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/Correction%20TP7.html) |
| **TP8** | Apprentissage non supervise (clustering K-means) | [voir](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/TP/html/Correction%20TP8.html) |

Chaque dossier de TP contient l'enonce (`.Rmd`/`.pdf`) et les corrections (`.qmd`/`.pdf`).

## Prerequis

- Fondamentaux de statistiques (regression, tests d'hypothese)
- Programmation R avec tidyverse
- [MathStat2](../../S5/MathStat2/) et [MathStat3](../MathStat3/) recommandes

## Executer les notebooks

```sh
# Notebooks du projet
quarto preview Projet/notebooks/01_exploration.qmd

# Corrections des TPs
quarto preview TP/TP1/Correction\ TP\ 1.qmd
```

## Outils & Bibliotheques

- **R** : tidyverse, caret, glmnet, ranger, rpart, rpart.plot, naivebayes, pROC, corrplot
- **Quarto** : rapports reproductibles melant code et narration (livre HTML + PDF)
- **TeX Live / TinyTeX** : rendu PDF via lualatex

## Supports de cours

Les sujets de TP1 à TP5 ont été rédigés par **Lola Etiévant** (Université Grenoble Alpes). Les corrections de ce répertoire sont les miennes ; les énoncés auxquels elles répondent sont les siens.

Non redistribués ici — voir [NOTICE](../../../../NOTICE) pour les crédits complets.
