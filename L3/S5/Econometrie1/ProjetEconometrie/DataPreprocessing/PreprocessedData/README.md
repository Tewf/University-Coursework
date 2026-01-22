# Données Prétraitées

Ce dossier contient les ensembles de données qui ont été prétraités et nettoyés.

## Fichiers

- **df_grenoble_vente.csv** : Données complètes sur les ventes à Grenoble
- **df_grenoble_vente_panel.csv** : Données au format panel (données de coupe transversale et temporelle)

## Description

Ces fichiers CSV contiennent les données prêtes pour :
- L'analyse exploratoire
- L'entraînement de modèles
- L'évaluation statistique

## Format

- **Délimiteur** : virgule (,)
- **Encodage** : UTF-8
- **En-têtes** : Oui (première ligne)

## Utilisation

Charger les données avec :
```python
import pandas as pd
df = pd.read_csv('df_grenoble_vente.csv')
```
