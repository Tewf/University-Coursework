# Data Acquisition, Processing and Mining for AI

> [Read in English](README.md)

**Cours :** Data Acquisition, Processing and Mining for AI, M1 Intelligence Artificielle, semestre 7, Université Grenoble Alpes

Une chaîne de traitement, construite deux fois. Les TP hebdomadaires enseignent
chaque étape sur un jeu de données fourni par l'équipe pédagogique ; le projet
en binôme reprend ensuite les mêmes étapes de bout en bout sur une API vivante
que l'on choisit soi-même — récupérer les données, les nettoyer, et terminer sur
un résultat de fouille lisible par quelqu'un d'autre.

## Les TP

| Dossier | Problème | Résolu avec | Fourni |
|---|---|---|---|
| [Lab1-pandas-taxi-data/](Lab1-pandas-taxi-data/) | 200 000 courses de taxi new-yorkais : charger le Parquet, masquer les lignes impossibles, dériver durée et heure de prise en charge, agréger et tracer | pandas, NumPy, matplotlib | notebook sujet, l'échantillon Parquet |

Les semaines suivantes s'ajoutent au fur et à mesure.

## Le projet

En binôme fixe, noté sur 20, décrit dans `Project/handout/`. Quatre dépôts Moodle le
jalonnent :

| Jalon | Échéance | Contient |
|---|---|---|
| M0 | avant le TP de la semaine 3 | le binôme, la source choisie, et la tranche de données sur laquelle on s'engage |
| M1 | avant le TP de la semaine 4 | un journal de ce qui a été récupéré, le code qui l'a récupéré, et les dimensions de chaque fichier Parquet produit |
| M2 | avant le TP de la semaine 6 | la fiche de données d'une page et le notebook exploratoire |
| M3 | soutenance au TP de la semaine 8, fichiers une semaine plus tard | le notebook de la chaîne complète, un rapport de 3 à 5 pages, la fiche de données finale |

Huit sources sont proposées — Crossref, GitHub, Hacker News, Open-Meteo, TMDB,
MediaWiki, data.gouv.fr et Twitch. Quatre contraintes valent quelle que soit
celle retenue : interroger l'API plutôt que de scraper, garder les gros
téléchargements hors des heures de TP, lire chaque identifiant depuis
l'environnement plutôt que depuis une cellule de notebook, et indiquer dans le
rapport quelles données personnelles ont été collectées et lesquelles ont été
écartées.

**Aucune donnée collectée n'est versionnée ici.** Le Parquet brut reste sur le
disque ; ce que le dépôt porte, c'est le code qui l'a produit et ce qui en est
écrit.

## Mise en place

Le cours fournit un seul environnement conda, `datacq`, épinglé dans un
`environment.yml` livré avec l'archive de mise en place sur Moodle. C'est le
fichier de l'équipe pédagogique et il n'est pas rediffusé ici (voir
[NOTICE](../../../../NOTICE)) ; il vit dans `Setup/handout/` avec le reste de
l'archive de mise en place, et il épingle Python 3.12 avec pandas, NumPy,
DuckDB, pyarrow, requests, BeautifulSoup, matplotlib, seaborn, scikit-learn,
mlxtend et Jupyter.

```bash
conda env create -f Setup/handout/environment.yml
conda activate datacq
python Setup/handout/verify_setup.py   # affiche SETUP OK quand tous les imports passent
```

## Structure des dossiers

Chaque unité garde son propre `handout/` : ce que l'équipe pédagogique a fourni
pour ce travail-là vit à côté de ce travail-là, plutôt qu'en un seul tas à la
racine du cours. `.publishignore` les retient tous : ce qu'un dossier montre est donc
mon travail — un README qui dit ce qui est demandé avec mes mots, et le notebook
complété quand il existe.

```
DataAcquisitionProcessingAndMiningForAI/
|-- Setup/
|   |-- handout/               <- guide de mise en place, environment.yml, verify_setup.py
|-- Lab1-pandas-taxi-data/
|   |-- handout/               <- le notebook sujet, l'archive telle que téléchargée
|   |-- data/raw/              <- l'échantillon Parquet que lit le notebook
|   |-- README.md
|-- Project/
|   |-- handout/               <- le sujet du projet, le modèle de fiche de données
|   |-- README.md
```

## Où vivent les explications

Pas ici. Parquet et stockage en colonnes, pagination et limites de débit des
API, données bien rangées, les décisions de nettoyage qui méritent d'être
consignées, règles d'association et clustering — chacun est une note dans un
coffre Obsidian séparé, à côté du cours dont elle vient. Un commentaire d'ici
qui se met à enseigner la théorie a sa place dans cette note.

## Matériel source

Le sujet du projet, le modèle de fiche de données, le guide de mise en place,
`environment.yml`, `verify_setup.py`, les notebooks de TP et les jeux de données
qu'ils lisent ne sont **pas rediffusés ici** : voir
[NOTICE](../../../../NOTICE). Chacun reste sur le disque dans le `handout/` de
l'unité à laquelle il appartient, et `.publishignore` les retient tous du dépôt public.
Ce qui est versionné est écrit contre eux.
