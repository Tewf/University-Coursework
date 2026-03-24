# Prédiction de la Satisfaction des Parfums

![R](https://img.shields.io/badge/R-4.x-blue?logo=r)
![Quarto](https://img.shields.io/badge/Quarto-1.8-purple?logo=quarto)
![Licence](https://img.shields.io/badge/licence-académique-green)

> Projet de classification supervisée binaire -- Compléments de Mathématiques 2 (L3 MIASHS, 2025-2026)

## Description

Prédire la **satisfaction des utilisateurs** vis-à-vis de parfums à partir de leurs caractéristiques olfactives. Le dataset provient de [Fragrantica Fragrance Dataset -- Kaggle](https://www.kaggle.com/datasets/olgagmiufana1/fragrantica-com-fragrance-dataset) (~24 000 parfums).

La satisfaction est une variable binaire (Oui/Non) basée sur la médiane de `Rating_Value`.

## Structure

```
.
├── _quarto.yml              # Config Quarto (type: book → PDF unique)
├── index.qmd                # Introduction du rapport
├── notebooks/               # Analyses (exécuter dans l'ordre)
│   ├── 01_exploration.qmd
│   ├── 02_preparation.qmd
│   ├── 03_regression_logistique.qmd
│   ├── 04_foret_aleatoire.qmd
│   └── 05_comparaison.qmd
├── R/utils.R                # Fonctions partagées (familles olfactives, CV)
├── data/
│   ├── fra_cleaned.csv      # Dataset (gitignored, voir lien Kaggle)
│   └── README.md            # Dictionnaire des variables
├── output/                  # Cache .rds (gitignored)
├── rapport/                 # HTML + PDF rendus (gitignored)
├── post-render.sh           # Tri auto HTML/PDF après render
├── references.bib
├── custom.css
└── consignes/               # Consignes du projet
```

## Pipeline

> **Consulter le rapport en ligne :** [page d'accueil](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/)

| Étape | Fichier | Description | HTML |
|-------|---------|-------------|------|
| 1 | `01_exploration.qmd` | Analyse exploratoire, valeurs manquantes, variable cible | [voir](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/01_exploration.html) |
| 2 | `02_preparation.qmd` | Feature engineering par familles olfactives, imputation, split 70/30 | [voir](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/02_preparation.html) |
| 3 | `03_regression_logistique.qmd` | Elastic Net, validation croisée 5-fold, AUC | [voir](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/03_regression_logistique.html) |
| 4 | `04_foret_aleatoire.qmd` | Random Forest (500 arbres), importance des variables | [voir](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/04_foret_aleatoire.html) |
| 5 | `05_comparaison.qmd` | Comparaison, courbes ROC, regard critique, conclusion | [voir](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/05_comparaison.html) |

## Exécution

Les notebooks s'exécutent **dans l'ordre** (chacun sauvegarde des `.rds` pour le suivant). Les modèles sont cachés : s'ils existent dans `output/`, ils ne sont pas re-entraînés.

```bash
# Render tout le projet (un seul PDF + site HTML)
quarto render

# Ou notebook par notebook
quarto render notebooks/01_exploration.qmd
quarto render notebooks/02_preparation.qmd
quarto render notebooks/03_regression_logistique.qmd
quarto render notebooks/04_foret_aleatoire.qmd
quarto render notebooks/05_comparaison.qmd
```

## Prérequis

- **R** >= 4.0
- **Quarto** >= 1.4
- Packages R : `tidyverse`, `caret`, `glmnet`, `ranger`, `pROC`, `corrplot`, `knitr`, `here`, `stringi`

## Auteurs

- HAMLIL Mohamed
- PARDO TERAN German
- EL KORAICHI Mohamed Yassine
- ANZID Keltoum

## Licence

Projet académique -- Université Grenoble Alpes, 2025-2026.
