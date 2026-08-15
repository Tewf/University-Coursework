# Livrables Moodle : Bundle autonome

Bundle déposé sur Moodle, **auto-suffisant** : tous les fichiers nécessaires pour compiler le rapport sont dans ce dossier, aucun lien vers l'extérieur.

## Contenu

| Fichier | Taille | Description |
|---|---|---|
| `Rapport_Projet_Parfums.Rmd` | 60 KB | **Source R Markdown** (livrable principal) |
| `Rapport_Projet_Parfums.pdf` | 330 KB | **PDF compilé** (20 pages, livrable principal) |
| `Rapport_Projet_Parfums.Rproj` | 1 KB | Projet RStudio (ouvre auto en réglant le working dir) |
| `utils.R` | 4 KB | Helpers R (palette, mapping 10 familles, CV control) |
| `fra_cleaned.csv` | 6.5 MB | Dataset Fragrantica nettoyé (~24 000 parfums) |
| `output/*.rds` | 24 MB | Cache des modèles entraînés (instantané au render) |

**Total : ~31 MB**

## Compilation dans RStudio (rapide, avec cache)

1. **Ouvrir** `Rapport_Projet_Parfums.Rproj` : RStudio règle automatiquement le working directory sur ce dossier.
2. **Ouvrir** `Rapport_Projet_Parfums.Rmd` dans l'éditeur.
3. **Cliquer** sur le bouton **Knit** (ou `Ctrl+Shift+K`).

Le render prend **~30 secondes** car le dossier `output/` contient déjà les modèles pré-entraînés (cache `.rds`). Le code vérifie leur existence avant de réentraîner.

## Compilation depuis la ligne de commande

```r
setwd("chemin/vers/moodle")
rmarkdown::render("Rapport_Projet_Parfums.Rmd")
```

## Si vous voulez réentraîner à zéro

```r
setwd("chemin/vers/moodle")
unlink("output", recursive = TRUE)      # supprime le cache
rmarkdown::render("Rapport_Projet_Parfums.Rmd")
```

Le render complet prend alors **~5 à 10 minutes** (Régression Logistique, Arbre, Forêt Aléatoire, kNN, Naive Bayes, K-means) et régénère automatiquement le cache dans `output/`.

## Prérequis R

- **R** ≥ 4.0
- **Packages** : `tidyverse`, `caret`, `glmnet`, `ranger`, `rpart`, `rpart.plot`, `naivebayes`, `pROC`, `corrplot`, `knitr`, `stringr`, `scales`, `gridExtra`, `rmarkdown`
- **Moteur LaTeX** : `lualatex` (fourni par TinyTeX : `tinytex::install_tinytex()`)

Pour installer tous les packages R d'un coup :

```r
install.packages(c(
  "tidyverse", "caret", "glmnet", "ranger", "rpart", "rpart.plot",
  "naivebayes", "pROC", "corrplot", "knitr", "stringr", "scales",
  "gridExtra", "rmarkdown", "tinytex"
))
tinytex::install_tinytex()  # une seule fois, si pas déjà installé
```

## Structure du rapport

Le `.Rmd` suit une progression en 13 sections :

1. **Introduction** : contexte parfumerie, problématique
2. **Données** : présentation du dataset Fragrantica, valeurs manquantes
3. **Analyse Exploratoire** : distributions univariées, bivariées, corrélations
4. **Feature Engineering** : mapping vers 10 familles olfactives, split 70/30
5. **Régression Logistique LASSO** : Elastic Net (CV 5-fold)
6. **Arbre de Décision** : élagué par complexity parameter
7. **Forêt Aléatoire** : `ranger` 500 arbres (**meilleur modèle**)
8. **k Plus Proches Voisins** : illustration de la malédiction de la dimensionnalité
9. **Comparaison** : courbes ROC, table récapitulative
10. **Pistes non explorées** : Naive Bayes et K-means (justifications de non-rétention)
11. **Regard critique et limites**
12. **Synthèse et conclusion**
13. **Utilisation de l'IA + contributions individuelles + références**

## Source de vérité du contenu

Ce `.Rmd` est une **agrégation manuelle** du projet Quarto multi-chapitres disponible sur GitHub :

> <https://github.com/Tewf/University-Coursework/tree/main/Bachelor/L3/S6/ComplementMath2/Projet>

Le projet GitHub contient 7 chapitres `.qmd` modulaires (`notebooks/01..07_*.qmd`) qui produisent exactement le même contenu sous forme de livre HTML + PDF, servi via GitHub Pages :

> <https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/>

Le `.Rmd` monolithique de ce bundle est fourni uniquement pour respecter le format attendu par Moodle (slide 2 des consignes : « Rendre le fichier source `.Rmd` ou `.Rnw` en plus du PDF généré »).
