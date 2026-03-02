# Bataille Navale — Projet IA

> [Read in English](README.md)

Une implementation complete du jeu classique de la bataille navale en Java, avec plusieurs strategies IA, une interface graphique et des outils statistiques pour evaluer les performances.

## Ce que vous apprendrez

- Conception orientee objet avec des packages Java modulaires
- Algorithmes d'IA heuristiques et probabilistes
- Techniques de simulation Monte Carlo
- Evaluation statistique et benchmarking d'agents IA
- Programmation d'interface graphique avec Java Swing

## Strategies IA

| Strategie | Approche | Description |
|-----------|----------|-------------|
| **Uniforme** | Aleatoire | Tire aleatoirement sur la grille |
| **Markov** | Probabiliste | Utilise des matrices de transition pour cibler les positions probables |
| **Monte Carlo** | Simulation | Execute des simulations pour evaluer les resultats des tirs |
| **Smart** | Hybride | Combine plusieurs heuristiques pour un jeu optimal |

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
Complement_IA-main/
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

Tous les resultats d'experiences sont dans `Results/` :
- `tournament_pairwise.csv` — Matrice de victoires pairwise
- `tournament_summary.csv` — Resume par bot (parties, victoires, taux, rang)
- `performance_summary.csv` — Stats d'auto-parties (moyenne de coups, erreur standard)
- `performance_gaussian_overlay.png` — Visualisation des distributions

## Documentation

```sh
# Voir la documentation API generee
xdg-open docs/api/index.html

# Compiler le rapport LaTeX
cd docs/rapport && make
```
