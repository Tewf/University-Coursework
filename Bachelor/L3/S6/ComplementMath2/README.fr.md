# Complements de mathematiques 2 — Introduction au Machine Learning

> [Read in English](README.md)

**Cours :** ComplementMath2 — Licence 3 MIASHS, Semestre 6, Universite Grenoble Alpes

Une introduction a l'apprentissage automatique supervise en R, combinant des travaux pratiques (TPs) avec un projet de classification complet de bout en bout sur des donnees de parfums.

## Ce que vous apprendrez

- Analyse exploratoire des donnees et techniques de visualisation
- Ingenierie de features a partir de donnees textuelles et categorielles
- Regression logistique avec regularisation Elastic Net
- Classification par foret aleatoire et ajustement d'hyperparametres
- Evaluation de modeles : accuracy, courbes ROC, importance des variables
- Validation croisee et methodologie train/test

## Projet : Prediction de la satisfaction pour les parfums

Un pipeline ML complet predisant la satisfaction des utilisateurs a partir d'un jeu de donnees de ~60 000 parfums.

| Etape | Notebook | Description |
|-------|----------|-------------|
| 1 | `01_exploration.qmd` | Analyse exploratoire : distributions, valeurs manquantes, visualisations |
| 2 | `02_preparation.qmd` | Ingenierie de features, imputation, split train/test (70/30) |
| 3 | `03_regression_logistique.qmd` | Regression logistique avec Elastic Net (CV 5 plis) |
| 4 | `04_foret_aleatoire.qmd` | Foret aleatoire (500 arbres) avec tuning |
| 5 | `05_comparaison.qmd` | Comparaison des modeles, courbes ROC, evaluation finale |

### Structure du projet

```
Projet/
|-- data/parfumo_data_clean.csv    <- Jeu de donnees parfums (~60k lignes)
|-- R/utils.R                      <- Fonctions utilitaires partagees
|-- notebooks/                     <- Pipeline d'analyse sequentiel
|-- output/                        <- Fichiers .rds intermediaires
|-- rapport/                       <- Rapports PDF generes
```

## Travaux Pratiques (TPs)

6 TPs couvrant les concepts fondamentaux du ML avec le jeu de donnees Titanic :

| TP | Theme |
|----|-------|
| TP1-TP2 | Exploration et preprocessing des donnees |
| TP3-TP4 | Modeles de classification |
| TP5-TP6 | Evaluation et comparaison de modeles |

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
quarto preview TP/TP1/Correction\ TP1.qmd
```

## Outils & Bibliotheques

- **R** : tidyverse, caret, glmnet, randomForest, pROC
- **Quarto** : rapports reproductibles melant code et narration
