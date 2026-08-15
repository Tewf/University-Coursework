# Econometrie 1

> [Read in English](README.md)

**Cours :** Econometrie1, Licence 3 MIASHS, Semestre 5, Universite Grenoble Alpes

Un projet d'econometrie appliquee analysant les donnees de ventes immobilieres a Grenoble a partir des donnees publiques DVF (Demandes de Valeurs Foncieres).

## Ce que vous apprendrez

- Preprocessing et nettoyage de donnees reelles
- Methodologie de revue de litterature econometrique
- Modelisation par regression lineaire et interpretation
- Extension du modele avec le machine learning (foret aleatoire)
- Pipeline d'analyse de donnees de bout en bout

## Projet : Analyse des prix immobiliers a Grenoble

| Phase | Dossier | Description |
|-------|---------|-------------|
| **Donnees** | `DataPreprocessing/` | Nettoyage et preparation des donnees DVF, documentation des variables |
| **Litterature** | `RevueDeLitterature/` | Articles academiques et contexte de l'analyse |
| **Modelisation** | `ModelTraining/` | Implementation de la regression lineaire et resultats |
| **Extension** | `ModelTraining/Extension/` | Modele foret aleatoire pour comparaison |

## Structure du dossier

```
Econometrie1/
|-- ProjetEconometrie/
|   |-- DataPreprocessing/
|   |   |-- DataDocumentation/     <- Descriptions des variables (PDF)
|   |   |-- PreprocessedData/      <- Jeux de donnees nettoyes
|   |   |-- *.ipynb                <- Notebooks de preprocessing
|   |-- ModelTraining/
|   |   |-- LinearRegression.ipynb <- Modele de regression principal
|   |   |-- Extension/
|   |       |-- RandomForest.ipynb <- Extension ML
|   |-- RevueDeLitterature/        <- References academiques
|   |-- README.md                  <- README detaille du projet
```

## Prerequis

- Statistiques : regression, tests d'hypothese, R-carre
- Bases de Python ou R pour la manipulation de donnees
- Comprehension des sources de donnees economiques

## Outils

- **Python** (notebooks Jupyter) pour le preprocessing et la modelisation
- **R** pour l'analyse statistique
- **pandas, scikit-learn** pour la manipulation de donnees et le ML
