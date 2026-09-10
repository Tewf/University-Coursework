# Recherche opérationnelle

> [Read in English](README.md)

**Cours :** Introduction to Artificial Intelligence, partie 2 (moitié recherche opérationnelle), M1 Intelligence Artificielle, semestre 7, Université Grenoble Alpes
**Équipe pédagogique :** Hadrien Cambazard, Nicolas Catusse (cours) ; Maxime Ogier, Nadia Brauner (TD) ; chapitres MIP d'Olivier Briant

Programmation linéaire, dualité, programmation en nombres entiers et branch
and bound, puis programmation par contraintes avec Choco. Chaque exercice VPL
de Caseine a son dossier ici : modèles OPL résolus par CPLEX, modèles Choco
résolus par pychoco.

## OPL

| Dossier | Problème | Solveur | Fourni |
|---|---|---|---|
| [OPL/01-opl-example/](OPL/01-opl-example/) | Exemple traité du court tutoriel OPL | OPL (CPLEX) | handout/, example.mod, configExe |
| [OPL/02-vegetables/](OPL/02-vegetables/) | Planification d'une production de légumes | OPL (CPLEX) | handout/, legumes.mod, configExe |
| [OPL/03-sandbox/](OPL/03-sandbox/) | Modèle libre, bac à sable | OPL (CPLEX) | handout/, mymodel.mod, configExe |
| [OPL/04-dairy-q1/](OPL/04-dairy-q1/) | Choix de production d'une laiterie, question 1 | OPL (CPLEX) | handout/, laiterieQ1.mod, configExe |
| [OPL/05-apple-q4/](OPL/05-apple-q4/) | Répartition d'une production de smartphones entre usines | OPL (CPLEX) | handout/, pommeQ4.mod, configExe |
| [OPL/06-wines/](OPL/06-wines/) | Production de vins, données séparées du modèle | OPL (CPLEX) | handout/, wines.mod, InstanceA.dat, configExe |
| [OPL/07-jam/](OPL/07-jam/) | Planification d'une production de confitures | OPL (CPLEX) | handout/, confiture.mod, configExe |
| [OPL/08-alloy/](OPL/08-alloy/) | Mélange d'alliages d'acier | OPL (CPLEX) | handout/, steel.mod, configExe |
| [OPL/09-water-network/](OPL/09-water-network/) | Gestion des flux d'un réseau d'eau | OPL (CPLEX) | handout/, flot.mod, instanceA.dat, configExe |
| [OPL/10-bill-of-materials/](OPL/10-bill-of-materials/) | Planification de production avec nomenclature | OPL (CPLEX) | handout/, billmaterial.mod, data1.dat, configExe |
| [OPL/11-cocktail/](OPL/11-cocktail/) | Composition de cocktails | OPL (CPLEX) | handout/, cocktail.mod, configExe |
| [OPL/12-airline/](OPL/12-airline/) | Planification aérienne, données séparées du modèle | OPL (CPLEX) | handout/, airline.mod, data1.dat, configExe |
| [OPL/13-garden-sensitivity/](OPL/13-garden-sensitivity/) | Planification d'un jardin, analyse de sensibilité | OPL (CPLEX) | handout/, garden.mod, configExe |
| [OPL/14-wines-q2/](OPL/14-wines-q2/) | Tarification des vins à partir de la solution duale | OPL (CPLEX) | handout/, wines.mod, configExe |
| [OPL/15-vitamins/](OPL/15-vitamins/) | Problème de régime, besoins en vitamines | OPL (CPLEX) | handout/, vitamins.mod, configExe |
| [OPL/16-vitamins-q2/](OPL/16-vitamins-q2/) | Tarification concurrentielle de vitamines de synthèse | OPL (CPLEX) | handout/, vitamins2.mod |
| [OPL/17-dual-program/](OPL/17-dual-program/) | Écrire le dual d'un programme | OPL (CPLEX) | handout/, dual.mod, configExe |
| [OPL/18-bouquets/](OPL/18-bouquets/) | Choix de bouquets de fleurs | OPL (CPLEX) | handout/, bouquets.mod, configExe |
| [OPL/19-wipers/](OPL/19-wipers/) | Production d'essuie-glaces, en nombres entiers | OPL (CPLEX) | handout/, wipers.mod, wipers2.mod, configExe |
| [OPL/20-coals/](OPL/20-coals/) | Mélange de charbons, en nombres entiers | OPL (CPLEX) | handout/, coals.mod, configExe |
| [OPL/21-cars/](OPL/21-cars/) | Stationnement de voitures minimisant la longueur de rue | OPL (CPLEX) | handout/, cars.mod, configExe |
| [OPL/22-lot-sizing/](OPL/22-lot-sizing/) | Dimensionnement de lots avec fichiers .dat | OPL (CPLEX) | handout/, lotsizing.mod, data1.dat, configExe |
| [OPL/23-bin-packing/](OPL/23-bin-packing/) | Formulation du bin packing | OPL (CPLEX) | handout/, binpack.mod, configExe |
| [OPL/24-matrix-sum-euler-345/](OPL/24-matrix-sum-euler-345/) | Project Euler 345, somme matricielle | OPL (CPLEX) | handout/, euler.mod, data1.dat, configExe |
| [OPL/25-toxic-warehouse/](OPL/25-toxic-warehouse/) | Affectation d'entrepôts à des produits chimiques incompatibles | OPL (CPLEX) | handout/, entrepot.mod, InstanceA.dat, configExe |
| [OPL/26-toys/](OPL/26-toys/) | Planification d'une production de jouets | OPL (CPLEX) | handout/, toysQ1.mod, toysQ2.mod, InstanceA.dat, configExe |

## Choco

| Dossier | Problème | Solveur | Fourni |
|---|---|---|---|
| [Choco/01-toy-meeting/](Choco/01-toy-meeting/) | Planification d'une réunion, exemple jouet | pychoco | handout/, toy_meeting.py, extended_toy_meeting.py, main.py |
| [Choco/02-magic-square/](Choco/02-magic-square/) | Carré magique | pychoco | handout/, magic_square.py |
| [Choco/03-abcde/](Choco/03-abcde/) | Trouver les chiffres tels que ABCDE×4 = EDCBA | pychoco | handout/, abcde.py |
| [Choco/04-birthday/](Choco/04-birthday/) | Deviner une année de naissance à partir d'indices | pychoco | handout/, birthday.py |
| [Choco/05-sujiko/](Choco/05-sujiko/) | Puzzle Sujiko | pychoco | handout/, sujiko.py |
| [Choco/06-heterosquare/](Choco/06-heterosquare/) | Puzzle hétérocarré | pychoco | handout/, heterosquare.py |
| [Choco/07-magic-series/](Choco/07-magic-series/) | Séries magiques | pychoco | handout/, magic_series.py |
| [Choco/08-n-queens/](Choco/08-n-queens/) | N reines | pychoco | handout/, n_queens.py |
| [Choco/09-warehouse-location/](Choco/09-warehouse-location/) | Problème de localisation d'entrepôts | pychoco | handout/, warehouse_location.py |
| [Choco/10-car-sequencing/](Choco/10-car-sequencing/) | Séquencement de voitures, plusieurs tailles d'instance | pychoco | handout/, car_seq_solver.py, car_seq_instance.py, executable.py, instances/*.car |
| [Choco/11-steel-production/](Choco/11-steel-production/) | Production d'acier, plusieurs tailles d'instance | pychoco | handout/, steel_prod_solver_m2.py, steel_instance.py, executable.py, instances/*.mill |

## Mise en place

OPL/CPLEX tourne sur le correcteur de Caseine ; rien n'est à installer en
local pour soumettre un modèle. La moitié Choco tient dans un environnement
conda, déclaré une fois dans [environment.yml](environment.yml) :

```bash
conda env create -f environment.yml
conda activate operations_research
```

## Structure du dossier

Chaque exercice garde l'énoncé Caseine dans `handout/` (mot pour mot) et le
modèle ou script de départ livré avec lui, à la racine de l'exercice, là où le
correcteur l'attend. `.gitignore` exclut `handout/`, la configuration du
correcteur `configExe`, les fichiers `.dat` requis et les `instances/` CSPLib,
donc rien de ce que Caseine distribue n'apparaît sur GitHub ; le fichier de
départ, si, puisque le correcteur le modifie sur place plutôt que de produire
un fichier de sortie à part — un README dit ce qui est demandé, avec mes
mots, et une page `steps/` enregistre le travail dès qu'il y en a. Les
supports du cours (tutoriels OPL, aide-mémoire pychoco, activité de
modélisation) sont dans un `handout/` à ce niveau, exclu de la même façon.

```
OperationsResearch/
|-- environment.yml               <- l'unique environnement conda, pour la moitié Choco
|-- handout/                      <- les supports du cours : tutoriels OPL, aide-mémoire pychoco
|-- OPL/
|   |-- 01-opl-example/
|   |   |-- handout/               <- l'énoncé Caseine
|   |   |-- README.md steps.json steps/   <- la demande avec mes mots, une page par question
|   |   |-- example.mod            <- le modèle de départ, modifié sur place
|   |   |-- configExe              <- la configuration du correcteur, gardée en local
|   |-- 02-vegetables/ ... 26-toys/
|-- Choco/
|   |-- 01-toy-meeting/
|   |   |-- handout/
|   |   |-- toy_meeting.py extended_toy_meeting.py main.py
|   |-- 02-magic-square/ ... 11-steel-production/
```

`configExe` est la configuration du correcteur Caseine pour cet exercice VPL :
elle nomme le modèle (et le fichier de données, s'il y en a un) que CPLEX ou
l'`executable.py` pychoco lance sur Moodle. Elle n'est pas nécessaire pour
exécuter un modèle en local.

## Où sont les explications

Pas ici. Les concepts dont chaque exercice a besoin — programmation linéaire
et dualité, programmation en nombres entiers et branch and bound,
programmation par contraintes — sont rédigés dans un coffre Obsidian à part,
une note par concept, à côté des transparents de cours dont ils viennent. Un
commentaire ici qui se met à enseigner la théorie a sa place dans cette note.

## Matériel source

Les énoncés des exercices, les supports du cours, les configurations du
correcteur, les fichiers `.dat` et les instances ne sont **pas redistribués
ici** : voir [NOTICE](../../../../NOTICE). Chaque énoncé reste sur disque dans
le `handout/` de son exercice, mot pour mot, les supports du cours dans celui
du cours, et `.gitignore` garde tout cela hors du dépôt. Le modèle ou script de
départ que Caseine livre avec chaque énoncé est publié tel quel — c'est ce que
le correcteur modifie sur place, il reste donc dans le dépôt jusqu'à ce qu'une
version remplie le remplace.
