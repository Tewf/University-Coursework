# Algorithmic Problem Solving

> [Read in English](README.md)

**Cours :** Algorithmic Problem Solving, M1 Intelligence Artificielle, semestre 7, Université Grenoble Alpes
**Équipe pédagogique :** Nguyen Kim Thang (responsable), avec Enikő Kevi et Lorena León sur les projets

Le cours se fait en apprentissage par problème : quatre projets APP, chacun
résolu en groupe sur plusieurs séances. Implémenter reste facultatif — et c'est
précisément pour cela que les quatre ont ici un dossier qui les attend, énoncé
compris. Quand un projet mérite d'être codé, l'endroit où le coder existe déjà.

Les deux TD et l'examen passé ne sont pas ici. Ils se traitent sur papier et ne
rendent rien, donc ils vivent dans le coffre de notes avec le reste du cours.

## Les projets

| Dossier | Problème | Résolu avec | Code |
|---|---|---|---|
| [APP1-maze/](APP1-maze/) | Générer un labyrinthe aléatoire par division récursive, puis trouver l'unique chemin vers sa sortie | Diviser pour régner, arbres binaires, parcours | squelette fourni |
| [APP2-candy-crush/](APP2-candy-crush/) | Candy Crush | Là où le glouton échoue, puis programmation dynamique | — |
| [APP3-scheduling/](APP3-scheduling/) | Emploi du temps scolaire | Flot maximum, coupe minimum, réduction | — |
| [APP4-hole-drilling/](APP4-hole-drilling/) | Perçage de trous | Arbre couvrant minimum, 2-approximation du tour | — |

## APP1 — Be Amazed

Le seul sujet accompagné de code. Un labyrinthe construit en divisant une
surface par un mur plein percé d'une seule porte, puis en recommençant sur
chaque moitié, est un arbre binaire — et c'est tout l'intérêt de l'exercice : sa
génération est un diviser pour régner, sa résolution un parcours d'arbre, et son
analyse de coût la récurrence qui en découle.

Le squelette fourni est `main.c`, `maze.h`, `svg.c/.h` et un `Makefile` qui
compile avec `gcc -g -Wall -O0 -Werror`. Il est volontairement incomplet :
`maze.c`, qui contient `maze_random()` et `maze_svg()`, est la partie à écrire.

```bash
cd APP1-maze && make      # échoue tant que maze.c n'existe pas
```

Deux choses à prévoir à la première compilation. `make` ne peut pas aboutir
avant que `maze.c` existe, puisque `main.c` appelle ses deux fonctions. Et
`main.c`, tel qu'il est fourni, déclare un `unsigned int len;` qu'il n'utilise
jamais, ce que `-Wall -Werror` transforme en erreur sous gcc 13.3 : cette ligne
doit disparaître, même une fois `maze.c` écrit.

## Structure du dossier

Chaque projet garde son énoncé dans `handout/`, à côté d'une extraction `.txt`
qui le rend greppable près du travail. `.gitignore` les exclut tous, donc ce
qu'un dossier montre sur GitHub est mon travail et rien d'autre : un README qui
dit, avec mes mots, ce qui est demandé, une page `steps/` par question, et le
code dès qu'il y en a.

```
AlgorithmicProblemSolving/
|-- APP1-maze/
|   |-- handout/               <- le PDF du sujet à côté de son extraction .txt
|   |-- README.md steps.json steps/   <- la demande avec mes mots, une page par question
|   |-- report/                <- le livrable, un dossier LaTeX par section
|   |-- implementation/        <- mon C++ : generation, recherche, tests, mesures
|   |-- main.c maze.h svg.c/.h Makefile   <- le squelette fourni, et mon maze.c
|   |-- code-as-downloaded.tar.gz
|-- APP2-candy-crush/ ... APP4-hole-drilling/
```

## Où sont les explications

Pas ici. Les concepts dont chaque sujet a besoin — diviser pour régner, le
théorème maître, les parcours d'arbres, la programmation dynamique, les flots et
coupes, les arbres couvrants, les rapports d'approximation — sont rédigés dans un
coffre Obsidian séparé, une note par concept, avec les diapositives de cours dont
ils viennent et les solutions papier, TD et examen compris. Chaque sujet y
associe ses questions aux concepts qu'elles demandent. Un commentaire d'ici qui
se met à enseigner la théorie a sa place dans cette note, pas dans le code.

## Matériel source

Les sujets, et le squelette C fourni avec l'APP1, ne sont **pas redistribués
ici** : voir [NOTICE](../../../../NOTICE). Ils restent sur le disque dans chaque
dossier `handout/`, et `.gitignore` les en exclut, squelette compris. Ce qui est
versionné est mon propre travail.
