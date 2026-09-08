# Algorithmic Problem Solving

> [Read in English](README.md)

**Cours :** Algorithmic Problem Solving, M1 Intelligence Artificielle, semestre 7, Université Grenoble Alpes
**Équipe pédagogique :** Nguyen Kim Thang (responsable), avec Enikő Kevi et Lorena León sur les projets

Le cours se fait en apprentissage par problème : quatre projets APP et deux TD,
chacun résolu sur papier, en groupe, sur plusieurs séances. Seul l'APP1 est
accompagné de code, et l'implémentation y reste facultative — ce dossier
contient donc un projet C et rien d'autre. Les sujets, le matériel de cours et
les rédactions vivent dans le coffre de notes, là où a sa place un problème
résolu sur papier.

## APP1 — Be Amazed

[APP1-maze/](APP1-maze/) génère un labyrinthe aléatoire en divisant sa surface
par un mur plein percé d'une seule porte, puis en recommençant sur chaque
moitié ; il trouve ensuite l'unique chemin d'une position quelconque vers la
sortie. Un labyrinthe construit ainsi est un arbre binaire, et c'est tout
l'intérêt de l'exercice : sa génération est un diviser pour régner, sa
résolution un parcours d'arbre, et son analyse de coût la récurrence qui en
découle.

Le sujet est dans `handout/`, à côté de son extraction `.txt` pour que
l'énoncé soit greppable près du travail — on ne peut pas écrire la chose sans
lui. Le squelette fourni est `main.c`, `maze.h`, `svg.c/.h` et un `Makefile`
qui compile avec `gcc -g -Wall -O0 -Werror`. Il est volontairement incomplet :
`maze.c`, qui contient `maze_random()` et `maze_svg()`, est la partie à écrire.

```bash
cd APP1-maze && make      # échoue tant que maze.c n'existe pas
```

Deux choses à prévoir à la première compilation. `make` ne peut pas aboutir
avant que `maze.c` existe, puisque `main.c` appelle ses deux fonctions. Et
`main.c`, tel qu'il est fourni, déclare un `unsigned int len;` qu'il n'utilise
jamais, ce que `-Wall -Werror` transforme en erreur sous gcc 13.3 : cette ligne
doit disparaître, même une fois `maze.c` écrit.

## Où est le reste

Pas ici. Les PDF des sujets, les diapositives de cours, les concepts que chaque
question demande — diviser pour régner, le théorème maître, les parcours
d'arbres, la programmation dynamique, les flots et coupes, les arbres couvrants,
les rapports d'approximation — ainsi que les solutions papier des APP2 à APP4,
des deux TD et de l'examen passé sont dans un coffre Obsidian séparé, une note
par concept. Un commentaire d'ici qui se met à enseigner la théorie a sa place
dans cette note, pas dans le code.

## Matériel source

Le sujet et le squelette C fournis avec l'APP1 ne sont **pas redistribués
ici** : voir [NOTICE](../../../../NOTICE). Ils restent sur le disque et
`.gitignore` les exclut du dépôt. Ce qui est versionné est l'implémentation
écrite en réponse.
