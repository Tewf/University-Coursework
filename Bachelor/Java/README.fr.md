# Programmation Java

> [Read in English](README.md)

**Cours :** Java & IA — Licence MIASHS, Universite Grenoble Alpes

Travaux de programmation Java couvrant les fondamentaux de la programmation orientee objet et un projet d'IA complet.

## Cours

| Projet | Description | Dossier |
|--------|-------------|---------|
| **Battleship IA** | Jeu d'IA multi-strategies avec interface graphique, tournois et analyse statistique | [Complement_IA-main/](Complement_IA-main/) |
| **Exercices POO** | Exercices progressifs des classes de base aux design patterns | [OOP/](OOP/) |

## Points forts

### Battleship IA
Un jeu de bataille navale complet avec **4 strategies IA** :
- **Uniforme** — Tir aleatoire
- **Markov** — Ciblage probabiliste par matrices de transition
- **Monte Carlo** — Evaluation de strategies par simulation
- **Smart** — Approche heuristique combinee

Inclut une interface graphique (Swing), un systeme de tournois et du benchmarking de performance avec sorties statistiques (CSV, PNG).

### Exercices POO
Exercices progressifs couvrant :
- Classes, encapsulation, heritage, polymorphisme
- Interfaces, classes abstraites, generiques
- Gestion des exceptions, entrees/sorties fichiers
- Mini-projets appliquant les design patterns

## Prerequis

- JDK 11+
- Familiarite basique avec la ligne de commande

## Demarrage rapide

```sh
# Compiler
javac -d bin $(find src -name '*.java')

# Executer (exemple)
java -cp bin package.ClassName
```

Voir le README de chaque sous-dossier pour les instructions specifiques.
