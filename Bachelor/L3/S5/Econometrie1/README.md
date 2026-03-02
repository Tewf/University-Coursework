# Econometrics 1

> [Lire en francais](README.fr.md)

**Course:** Econometrie1 — Licence 3 MIASHS, Semester 5, Universite Grenoble Alpes

An applied econometrics project analysing real-estate sales data from Grenoble using public DVF (Demandes de Valeurs Foncieres) data.

## What You'll Learn

- Real-world data preprocessing and cleaning
- Econometric literature review methodology
- Linear regression modeling and interpretation
- Model extension with machine learning (Random Forest)
- End-to-end data analysis pipeline

## Project: Real-Estate Price Analysis in Grenoble

| Phase | Folder | Description |
|-------|--------|-------------|
| **Data** | `DataPreprocessing/` | Cleaning and preparing DVF data, documentation of variables |
| **Literature** | `RevueDeLitterature/` | Academic papers and context for the analysis |
| **Modeling** | `ModelTraining/` | Linear regression implementation and results |
| **Extension** | `ModelTraining/Extension/` | Random Forest model for comparison |

## Folder Structure

```
Econometrie1/
|-- ProjetEconometrie/
|   |-- DataPreprocessing/
|   |   |-- DataDocumentation/     <- Variable descriptions (PDF)
|   |   |-- PreprocessedData/      <- Cleaned datasets
|   |   |-- *.ipynb                <- Preprocessing notebooks
|   |-- ModelTraining/
|   |   |-- LinearRegression.ipynb <- Main regression model
|   |   |-- Extension/
|   |       |-- RandomForest.ipynb <- ML extension
|   |-- RevueDeLitterature/        <- Academic references
|   |-- README.md                  <- Detailed project README
```

## Prerequisites

- Statistics: regression, hypothesis testing, R-squared
- Python or R basics for data manipulation
- Understanding of economic data sources

## Tools

- **Python** (Jupyter notebooks) for preprocessing and modeling
- **R** for statistical analysis
- **pandas, scikit-learn** for data manipulation and ML
