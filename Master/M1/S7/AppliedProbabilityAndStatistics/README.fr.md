# Applied Probability and Statistics

> [Read in English](README.md)

**Cours :** Applied Probability and Statistics, M1 Intelligence Artificielle, semestre 7, Université Grenoble Alpes (partagé avec le M1 Mathématiques Appliquées)

Quatre séances pratiques en R, d'une première heure avec le langage à une
prévision de températures sur la France par vecteurs gaussiens. Trois arrivent
en notebooks R Markdown à compléter, une en PDF seul ; chacune a son dossier
ici. Les feuilles d'exercices, les tests courts et l'examen d'entraînement se
traitent sur papier et ne sont pas ici.

## Les TP

| Dossier | Problème | Résolu avec | Fourni |
|---|---|---|---|
| [Lab0-first-manipulations-with-r/](Lab0-first-manipulations-with-r/) | Une prise en main de R : classes d'objets, code vectorisé plutôt que boucles, premiers tirages aléatoires | R de base, `sample()`, `runif()` | `.Rmd`, `saison_2022.csv`, `BreastCancer.csv` |
| [Lab1-real-random-variables/](Lab1-real-random-variables/) | Fonctions de répartition, densités, médianes et méthode d'inversion, à la main puis par simulation | `rexp`, `runif`, `ecdf`, `curve` | `.Rmd` |
| [Lab2-estimators-exponential-model/](Lab2-estimators-exponential-model/) | La loi des grands nombres et le théorème central limite par simulation, puis des estimateurs dans le modèle exponentiel | simulation, méthode des moments, vraisemblance | PDF |
| [Lab3-kriging/](Lab3-kriging/) | Simuler un vecteur gaussien à partir d'une racine carrée de sa covariance, puis prévoir les températures sur la France par krigeage | vecteurs gaussiens, conditionnement | PDF, `.Rmd`, `Lab-Solutions.r` officiel, trois `.Rdata` |

Deux choses à savoir avant d'en ouvrir un :

- **Le `BreastCancer.csv` du TP 0 n'est lu par aucun code.** Le notebook prend
  ce jeu de données dans le paquet `mlbench`. Le fichier a été livré avec le TP
  malgré tout et reste à côté de lui pour cette seule raison.
- **`Lab-Solutions.r` s'exécute depuis la racine du TP.** Il `load()` les trois
  `.Rdata` par leur nom nu : le lancer depuis `Lab3-kriging/`, pas depuis
  `handout/`.

## Mise en place

Un environnement conda, déclaré dans [environment.yml](environment.yml) :

```bash
conda env create -f environment.yml
conda activate m1ai-applied-stats
```

On commence un TP en copiant son notebook hors de `handout/` et en tricotant la copie :

```bash
cd Lab3-kriging
cp handout/Lab3-kriging.Rmd .
Rscript -e 'rmarkdown::render("Lab3-kriging.Rmd")'
```

Cette copie est le fichier versionné. Celui de `handout/` ne change jamais.

## Structure du dossier

Chaque TP garde ce que l'équipe a distribué dans `handout/` (le sujet `.Rmd` ou
PDF, une extraction `.txt` de tout PDF pour qu'il soit greppable, et la
solution officielle quand elle existe). Les jeux de données sont à la racine du
TP, là où le code les `load()`. `.publishignore` retient tout cela, donc ce qu'un
dossier montre sur GitHub est mon travail et rien d'autre : un README qui dit,
avec mes mots, ce qui est demandé, une page `steps/` par question, et le
notebook complété dès qu'il existe.

```
AppliedProbabilityAndStatistics/
|-- environment.yml              <- l'unique environnement conda
|-- Lab0-first-manipulations-with-r/
|   |-- handout/                 <- le sujet .Rmd
|   |-- README.md steps.json steps/   <- la demande avec mes mots, une page par question
|   |-- saison_2022.csv BreastCancer.csv
|-- Lab1-real-random-variables/
|-- Lab2-estimators-exponential-model/
|   |-- handout/                 <- le sujet PDF et son .txt
|-- Lab3-kriging/
|   |-- handout/                 <- PDF + .txt, le .Rmd, Lab-Solutions.r
|   |-- data_temperatures.Rdata frontieres_france.Rdata grille_france.Rdata
```

## Où sont les explications

Pas ici. Les concepts dont chaque TP a besoin — espaces probabilisés,
variables aléatoires réelles, simulation de variables aléatoires, vecteurs
aléatoires et espérance conditionnelle, estimation paramétrique, loi des grands
nombres et théorème central limite — sont rédigés dans un coffre Obsidian
séparé, une note par concept, avec les diapositives de cours dont ils viennent,
les feuilles d'exercices, les tests et les manuels. Chaque TP y associe ses
questions aux concepts qu'elles demandent. Un commentaire d'ici qui se met à
enseigner la théorie a sa place dans cette note.

## Matériel source

Les sujets, la solution officielle et les jeux de données ne sont **pas
redistribués ici** : voir [NOTICE](../../../../NOTICE). Ils restent sur le
disque dans chaque dossier de TP et `.publishignore` les retient du dépôt public. Ce qui
est versionné est le travail écrit en réponse.
