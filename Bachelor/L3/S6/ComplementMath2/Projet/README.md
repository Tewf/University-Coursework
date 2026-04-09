# Prédiction de la Satisfaction des Parfums

![R](https://img.shields.io/badge/R-4.x-blue?logo=r)
![Quarto](https://img.shields.io/badge/Quarto-1.8-purple?logo=quarto)

> Classification supervisée binaire — Compléments de Mathématiques 2 (L3 MIASHS, 2025-2026)
> Auteurs : HAMLIL · PARDO TERAN · EL KORAICHI · ANZID

## 📖 Lire le projet

| Format | Lien | Pour quoi faire |
|---|---|---|
| 📄 **PDF (24 p)** | [télécharger](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/pdf/Pr%C3%A9diction-de-la-Satisfaction-Client-pour-les-Parfums.pdf) | Lecture linéaire imprimable |
| 🌐 **Livre HTML** | [ouvrir](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/) | Sidebar de navigation, **code R dépliable** |
| 💻 **Code source** | [`notebooks/`](notebooks/) | Chunks R commentés (`.qmd` = `.Rmd` moderne) |

## Pipeline (7 chapitres)

| # | Chapitre | Modèle / contenu | Rendu |
|---|---|---|---|
| 1 | [`01_exploration.qmd`](notebooks/01_exploration.qmd) | EDA : manquantes, cible, univariée/bivariée, accords, notes | [HTML](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/01_exploration.html) |
| 2 | [`02_preparation.qmd`](notebooks/02_preparation.qmd) | Feature engineering : 10 familles olfactives, split 70/30 anti-leakage | [HTML](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/02_preparation.html) |
| 3 | [`03_regression_logistique.qmd`](notebooks/03_regression_logistique.qmd) | **Régression Logistique LASSO** (Elastic Net, CV 5-fold) | [HTML](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/03_regression_logistique.html) |
| 4 | [`04_arbre_decision.qmd`](notebooks/04_arbre_decision.qmd) | **Arbre de Décision** élagué (Gini, `cp` optimal) | [HTML](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/04_arbre_decision.html) |
| 5 | [`05_foret_aleatoire.qmd`](notebooks/05_foret_aleatoire.qmd) | **Forêt Aléatoire** (`ranger`, 500 arbres, importance Gini) | [HTML](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/05_foret_aleatoire.html) |
| 6 | [`06_knn.qmd`](notebooks/06_knn.qmd) | **k Plus Proches Voisins** (malédiction de la dimensionnalité) | [HTML](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/06_knn.html) |
| 7 | [`07_comparaison.qmd`](notebooks/07_comparaison.qmd) | ROC, **Naive Bayes** & **K-means** (rejetés), critique, IA, refs | [HTML](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/notebooks/07_comparaison.html) |

Helpers partagés : [`utils.R`](utils.R) · Config Quarto : [`_quarto.yml`](_quarto.yml) · Bibliographie : [`references.bib`](references.bib).

## Structure

```
.
├── _quarto.yml        ← Config livre Quarto (HTML + PDF)
├── index.qmd          ← Introduction + abstract
├── notebooks/         ← 7 chapitres séquentiels
├── utils.R            ← Helpers (palette, 10 familles, CV control)
├── data/              ← fra_cleaned.csv (gitignored, lien Kaggle dans data/README.md)
├── moodle/            ← Bundle officiel Rmd + PDF déposé sur Moodle
├── output/            ← Cache .rds modèles (gitignored, régénéré)
├── rapport/           ← HTML + PDF rendus (servis par GitHub Pages)
└── consignes/         ← Sujet officiel + classification olfactive
```

## Exécution

```bash
# 1er render : ~5–10 min (entraîne les 5 modèles + NB + K-means)
# Renders suivants : ~30 s (cache output/*.rds réutilisé)
conda run -n r_env quarto render
```

## Prérequis

- **R** ≥ 4.0 · **Quarto** ≥ 1.4 · **TinyTeX** (lualatex)
- Packages R : `tidyverse`, `caret`, `glmnet`, `ranger`, `rpart`, `rpart.plot`, `naivebayes`, `pROC`, `corrplot`, `knitr`, `here`, `stringr`, `scales`, `gridExtra`

Dataset : [Fragrantica Fragrance Dataset (Kaggle)](https://www.kaggle.com/datasets/olgagmiufana1/fragrantica-com-fragrance-dataset), ~24 000 parfums. Cible binaire = `Rating_Value ≥ médiane`.

Projet académique — Université Grenoble Alpes, 2025-2026.
