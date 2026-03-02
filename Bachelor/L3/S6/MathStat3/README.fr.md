# Mathematiques et Statistiques 3

> [Read in English](README.md)

**Cours :** MathStat3 — Licence 3 MIASHS, Semestre 6, Universite Grenoble Alpes

Methodes statistiques avancees couvrant les tests d'hypothese, la regression, l'ANOVA et les tests non-parametriques. Chaque TP s'appuie sur le precedent, progressant des tests de normalite de base a l'analyse multi-facteurs complexe.

## Ce que vous apprendrez

- Evaluer la normalite avec les QQ-plots, Shapiro-Wilk et les tests du chi-deux
- Modeliser par regression lineaire simple et multiple
- Comparer des groupes par ANOVA a un et deux facteurs
- Utiliser des alternatives non-parametriques quand les hypotheses de normalite ne tiennent pas
- Interpreter des resultats statistiques et prendre des decisions basees sur les donnees

## Vue d'ensemble des TPs

| TP | Theme | Concepts cles | Jeux de donnees |
|----|-------|---------------|-----------------|
| **TP1** | Normalite & Chi-deux | QQ-plots, test de Shapiro-Wilk, test d'adequation du chi-deux | `titanic.csv` |
| **TP2** | Regression lineaire | Regression simple/multiple, interpretation des coefficients, R-carre | `tension.csv`, `audition2.csv` |
| **TP3** | ANOVA a un facteur | Test F, comparaison de moyennes, tests post-hoc | `murderusa.csv`, `crime16.csv`, `beignets.txt` |
| **TP4** | ANOVA a deux facteurs & Non-parametrique | Effets d'interaction, Kruskal-Wallis, Wilcoxon | `ozone.txt`, `engraisRegion.txt`, `dureteMeche.txt` |
| **Bonus** | Analyse notes & genre | Comparaison des notes d'algebre (H/F) sur 3 ans | `alg22.csv`, `alg23.csv`, `alg24.csv` |

## Prerequis

- Probabilites et statistiques de base (distributions, p-valeurs, intervalles de confiance)
- [MathStat2](../../S5/MathStat2/) recommande comme base
- Notions de programmation R

## Executer les notebooks

Chaque TP est disponible en deux formats : Quarto (`.qmd`) et Jupyter (`.ipynb`).

```sh
# Quarto
quarto preview TP1/tp1_normalite_chi2.qmd

# Jupyter
jupyter notebook TP1/tp1_normalite_chi2.ipynb
```

## Structure du dossier

```
MathStat3/
|-- TP Stat 3.pdf          <- Support de cours complet
|-- TP1/                   <- Tests de normalite & chi-deux
|-- TP2/                   <- Regression lineaire
|-- TP3/                   <- ANOVA (un facteur)
|-- TP4/                   <- ANOVA + tests non-parametriques
|   |-- TP_Bonus/          <- Analyse notes & genre
```

## Outils & Bibliotheques

- **R** avec les fonctions statistiques de base
- **Quarto** pour des rapports reproductibles
- **Jupyter** comme environnement de notebook alternatif
