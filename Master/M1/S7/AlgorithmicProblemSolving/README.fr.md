# Algorithmic Problem Solving

> [Read in English](README.md)

**Cours :** Algorithmic Problem Solving, M1 Intelligence Artificielle, semestre 7, Université Grenoble Alpes
**Équipe pédagogique :** Nguyen Kim Thang (responsable), avec Enikő Kevi et Lorena León sur les projets

Quatre projets APP, deux TD et un sujet d'examen. Le cours se fait en
apprentissage par problème : chaque APP se résout sur papier, en groupe, sur
quatre séances, et l'implémentation reste facultative. Ce dossier est le côté
pratique — les sujets, le code fourni avec eux, et ce que j'écris en réponse.

## Contenu

| Dossier | Sujet | Résolu avec |
|---|---|---|
| [APP1-maze/](APP1-maze/) | Générer un labyrinthe aléatoire par division récursive, puis trouver l'unique chemin vers sa sortie | Diviser pour régner, arbres binaires, parcours, complexité |
| [APP2-candy-crush/](APP2-candy-crush/) | Candy Crush | Là où le glouton échoue, puis programmation dynamique |
| [APP3-scheduling/](APP3-scheduling/) | Emploi du temps scolaire | Flot maximum, coupe minimum, réduction |
| [APP4-hole-drilling/](APP4-hole-drilling/) | Perçage de trous | Arbre couvrant minimum, 2-approximation du tour |
| [TD1-optimal-bst/](TD1-optimal-bst/) | Arbre binaire de recherche optimal | Programmation dynamique |
| [TD2-bipartite-matching/](TD2-bipartite-matching/) | Couplage biparti de cardinalité maximum | Réduction au flot maximum |
| [exam-2024/](exam-2024/) | Examen du 5 décembre 2024 | Couplage, sac à dos (PD puis glouton), chemins disjoints |

Seul l'APP1 fournit du code. Son squelette (`main.c`, `maze.h`, `svg.c/.h`,
`Makefile`) compile avec `gcc -g -Wall -O0 -Werror` et est volontairement
incomplet : `maze.c`, qui contient `maze_random()` et `maze_svg()`, est la partie
à écrire.

```bash
cd APP1-maze/code && make      # échoue tant que maze.c n'existe pas
```

## Structure du dossier

Chaque sujet a son dossier, avec le PDF et son extraction `.txt` dans
`handout/`, pour que l'énoncé soit greppable à côté du travail.

```
AlgorithmicProblemSolving/
|-- APP1-maze/
|   |-- handout/               <- le PDF du sujet à côté de son extraction .txt
|   |-- code/                  <- le squelette C fourni, et mon maze.c
|   |-- code-as-downloaded.tar.gz
|-- APP2-candy-crush/ ... APP4-hole-drilling/
|-- TD1-optimal-bst/ TD2-bipartite-matching/
|-- exam-2024/
```

## Où sont les explications

Pas ici. Les concepts dont chaque sujet a besoin — diviser pour régner, le
théorème maître, les parcours d'arbres, la programmation dynamique, les flots et
coupes, les arbres couvrants, les rapports d'approximation — sont rédigés dans un
coffre Obsidian séparé, une note par concept, avec les diapositives de cours dont
ils viennent. Chaque sujet y associe ses questions aux concepts qu'elles
demandent. Un commentaire d'ici qui se met à enseigner la théorie a sa place dans
cette note, pas dans le code.

## Matériel source

Les sujets, et le squelette C fourni avec l'APP1, ne sont **pas redistribués
ici** : voir [NOTICE](../../../../NOTICE). Ils restent sur le disque dans chaque
dossier `handout/`, et `.gitignore` les en exclut, squelette compris. Ce qui est
versionné est mon propre travail.
