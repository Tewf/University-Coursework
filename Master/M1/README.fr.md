# M1 Intelligence Artificielle

> [Read in English](README.md)

Première année du [Master Intelligence Artificielle](https://m-ai.imag.fr/) de
l'Université Grenoble Alpes, co-porté par l'UFR IM²AG et Ensimag (Grenoble INP).
Tous les cours du M1 sont obligatoires : les dossiers ci-dessous se remplissent
donc dans l'ordre où les semestres sont enseignés.

## Semestre 7

| Cours | Sujet | Langages | Dossier |
|-------|-------|----------|---------|
| Programmation | Outillage et données en Python, C++ et CMake, interop pybind11, un solveur TSP | Python, C++ | [S7/Programming/](S7/Programming/README.fr.md) |
| Algorithmic Problem Solving | Diviser pour régner, programmation dynamique, flots et coupes, arbres couvrants, approximation ; quatre projets APP résolus sur papier, un avec un squelette C | C | [S7/AlgorithmicProblemSolving/](S7/AlgorithmicProblemSolving/README.fr.md) |
| Introduction to AI | Sept notebooks d'apprentissage automatique, de l'évaluation des modèles aux réseaux récurrents ; Datalog et programmation par contraintes | Python | [S7/IntroductionToAI/](S7/IntroductionToAI/README.fr.md) |
| Applied Probability and Statistics | Simulation, estimateurs, vecteurs gaussiens et krigeage, en R Markdown | R | [S7/AppliedProbabilityAndStatistics/](S7/AppliedProbabilityAndStatistics/README.fr.md) |
| Operations Research | Programmation linéaire et en nombres entiers, dualité, branch and bound, programmation par contraintes ; 37 exercices Caseine en OPL et pychoco | OPL, Python | [S7/OperationsResearch/](S7/OperationsResearch/README.fr.md) |

## Semestre 8

Pas encore commencé.

## Environnements

Chaque dossier de cours déclare ses propres dépendances. Le cours de
programmation utilise un environnement conda pour Python et `apt` pour les
bibliothèques C++ ; voir [S7/Programming/README.fr.md](S7/Programming/README.fr.md).
Introduction to AI et Applied Probability and Statistics déclarent chacun leur
environnement conda (`m1ai-intro-ai`, `m1ai-applied-stats`) ; Algorithmic
Problem Solving n'a besoin que de `gcc` et `make`.

