# Mathematiques et Statistiques 2

> [Read in English](README.md)

**Cours :** MathStat2 — Licence 3 MIASHS, Semestre 5, Universite Grenoble Alpes

Travaux pratiques de statistiques en R couvrant la simulation, l'estimation et les tests d'hypothese. Ces seances construisent une base solide pour l'analyse statistique appliquee.

## Ce que vous apprendrez

- Simulation Monte Carlo et reeechantillonnage bootstrap
- Estimation ponctuelle : biais, variance, convergence, maximum de vraisemblance
- Construction d'intervalles de confiance
- Tests du chi-deux : adequation, conformite, homogeneite
- Application pratique de la theorie statistique sur des donnees reelles

## Vue d'ensemble des TPs

| TP | Theme | Concepts cles |
|----|-------|---------------|
| **TP1** | Simulation & Bootstrap | Generation aleatoire, reeechantillonnage, distributions empiriques |
| **TP2** | Estimation | Biais, variance, EQM, convergence des estimateurs |
| **TP3** | Maximum de vraisemblance | Derivation du MLE, information de Fisher, proprietes asymptotiques |
| **TP4** | Intervalles de confiance | Quantites pivotales, probabilite de couverture, taille d'echantillon |
| **TP5** | Tests d'hypothese | Tests du chi-deux, conformite, homogeneite, independance |

## Jeux de donnees

- `post-199413-Intima_Media.txt` — Mesures d'epaisseur de l'intima-media post-transverse
- `post-199414-prevalsidafric.xls` — Donnees de prevalence du VIH en Afrique
- Voir `data/README.md` pour la description detaillee des variables.

## Prerequis

- Introduction aux probabilites (distributions, esperance, variance)
- Programmation R de base
- Concepts statistiques fondamentaux (moyenne, mediane, ecart-type)

## Executer les notebooks

```sh
# Rendre un notebook Quarto
quarto preview TPs/code/TP_Statistiques.qmd

# Remplacer le nom de fichier pour les autres TPs
```

## Structure du dossier

```
MathStat2/
|-- TPs/
|   |-- code/          <- Notebooks Quarto (.qmd)
|   |-- PDFVersion/    <- Instructions en PDF
|-- data/              <- Jeux de donnees avec documentation
|-- scripts/           <- Fonctions R auxiliaires (ex: sigma2.test.R)
```

## Outils & Bibliotheques

- **R** avec stats de base, tidyverse
- **Quarto** pour des rapports reproductibles
- Scripts auxiliaires personnalises dans `scripts/`
