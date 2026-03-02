# Prédiction de la Satisfaction des Parfums

![R](https://img.shields.io/badge/R-4.x-blue?logo=r)
![Quarto](https://img.shields.io/badge/Quarto-1.8-purple?logo=quarto)
![Licence](https://img.shields.io/badge/licence-académique-green)

> Projet de classification supervisée binaire -- Compléments de Mathématiques 2 (L3 MIASHS, 2025-2026)

## Description

Ce projet vise à **prédire la satisfaction des utilisateurs** vis-à-vis des parfums à partir de leurs caractéristiques (concentration, accords olfactifs, notes de tête/cœur/fond, année de sortie). Nous utilisons un jeu de données de ~60 000 parfums issu de [Parfumo via TidyTuesday](https://github.com/rfordatascience/tidytuesday/blob/main/data/2024/2024-12-10/readme.md).

La satisfaction est définie comme une variable binaire (Oui/Non) basée sur la médiane de `Rating_Value`.

## Structure du projet

```
.
├── _quarto.yml          # Configuration Quarto partagée
├── README.md
├── .gitignore
├── references.bib       # Bibliographie BibTeX
├── data/                # Données brutes
│   ├── README.md
│   └── parfumo_data_clean.csv
├── R/                   # Fonctions utilitaires partagées
│   └── utils.R
├── notebooks/           # Analyses Quarto (à exécuter dans l'ordre)
│   ├── 01_exploration.qmd
│   ├── 02_preparation.qmd
│   ├── 03_regression_logistique.qmd
│   ├── 04_foret_aleatoire.qmd
│   └── 05_comparaison.qmd
├── output/              # Fichiers intermédiaires (.rds)
├── rapport/             # PDFs générés
└── consignes/           # Consignes du projet
```

## Pipeline d'analyse

| Étape | Fichier | Description |
|-------|---------|-------------|
| 1 | `01_exploration.qmd` | Analyse exploratoire, valeurs manquantes, création de la variable cible |
| 2 | `02_preparation.qmd` | Feature engineering, imputation, séparation train/test (70/30) |
| 3 | `03_regression_logistique.qmd` | Régression logistique Elastic Net, validation croisée 5-fold |
| 4 | `04_foret_aleatoire.qmd` | Forêt aléatoire (500 arbres), importance des variables |
| 5 | `05_comparaison.qmd` | Comparaison des modèles, courbes ROC, conclusion |

## Prérequis

- **R** >= 4.0
- **Quarto** >= 1.4
- Packages R : `tidyverse`, `caret`, `glmnet`, `randomForest`, `pROC`, `corrplot`, `knitr`, `here`

## Exécution

Les notebooks doivent être exécutés **dans l'ordre** car chacun sauvegarde des fichiers `.rds` intermédiaires utilisés par le suivant.

```bash
# Depuis la racine du projet
quarto render notebooks/01_exploration.qmd
quarto render notebooks/02_preparation.qmd
quarto render notebooks/03_regression_logistique.qmd
quarto render notebooks/04_foret_aleatoire.qmd
quarto render notebooks/05_comparaison.qmd
```

## Auteurs

- HAMLIL Mohamed
- PARDO TERAN German
- EL KORAICHI Mohamed Yassine
- ANZID Keltoum

## Licence

Projet académique -- Université Grenoble Alpes, 2025-2026.
