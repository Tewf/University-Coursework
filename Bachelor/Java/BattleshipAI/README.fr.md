# Bataille Navale : Projet IA

> [Read in English](README.md) · [Regarder le bot jouer ↗](https://tewf.github.io/University-Coursework/Bachelor/Java/BattleshipAI/)


**Auteurs :** HAMLIL Mohamed Ali Tewfik · SGHIOUAR IDRISSI Saad
*Projet universitaire à deux (Compléments d'IA, L3 MIASHS, Université Grenoble Alpes).*

La bataille navale en Java, avec quatre strategies de ciblage et le protocole de
tournoi permettant de dire laquelle fonctionne reellement.

## Resultats

Tournoi toutes rondes, 300 parties par bot, et auto-parties sur 100 parties pour
compter le nombre de tirs necessaires a couler la flotte. Produits par les
commandes ci-dessous ; sorties brutes dans [`Results/`](Results/).

| Strategie | Approche | Taux de victoire | Tirs moyens pour vider la grille |
|---|---|---:|---:|
| **Markov** | Matrices de transition sur les positions probables | **74,3 %** ±2,5 | **54,8** ±1,2 |
| **Monte Carlo** | Simulation des placements restants | 67,0 % ±2,7 | 55,5 ±1,2 |
| **Smart** | Hybride de plusieurs heuristiques | 56,7 % ±2,9 | 61,1 ±1,1 |
| **Uniforme** | Tirs aleatoires | 2,0 % ±0,8 | 94,3 ±0,5 |

La grille compte 100 cases : le tir aleatoire en demande 94, soit quasiment
toute la grille. Markov la vide en 55, une **reduction de 42 %**, et gagne 74 %
de ses parties. Monte Carlo coute bien plus de calcul pour un resultat
legerement inferieur ; c'est la partie interessante : ici le modele
probabiliste bon marche bat la simulation couteuse.

## Execution du projet

**Prerequis :** JDK 11+, shell POSIX

```sh
# Compiler
javac -d bin $(find src -name "*.java")

# Lancer l'interface graphique
java --module-path bin -m ComplementIA/bataillenavale.Main

# Lancer un tournoi (ex: 1000 matchs par paire)
java --module-path bin -m ComplementIA/statistique.Tournament 1000

# Lancer l'analyse de performance (ex: 100 auto-parties par bot)
java --module-path bin -m ComplementIA/statistique.Performance 100
```

## Structure du projet

```
BattleshipAI/
|-- src/
|   |-- bataillenavale/       <- Points d'entree & UI
|   |-- logique/              <- Logique centrale (grille, navires, coordonnees)
|   |-- joueurs/              <- Joueurs (humain, bots)
|   |-- heuristic/            <- Strategies IA (Uniforme, Markov, MonteCarlo)
|   |-- interfacegraphique/   <- Composants Swing
|   |-- statistique/          <- Outils de tournoi & performance
|-- bin/                      <- Classes compilees
|-- docs/
|   |-- api/                  <- JavaDoc generee
|   |-- rapport/              <- Sources LaTeX du rapport
|-- Results/                  <- Sorties des experiences (CSV, PNG)
```

## Sorties

`Results/` contient les chiffres ci-dessus : `tournament_summary.csv` et
`tournament_pairwise.csv` pour les taux de victoire, `performance_summary.csv`
pour le nombre de tirs, et `performance_gaussian_overlay.png` pour leurs
distributions.

## Documentation

```sh
# Voir la documentation API generee
xdg-open docs/api/index.html

# Compiler le rapport LaTeX
cd docs/rapport && make
```
