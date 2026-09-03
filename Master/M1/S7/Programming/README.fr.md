# Programmation

> [Read in English](README.md)

M1 Intelligence Artificielle, semestre 7, Université Grenoble Alpes. Enseigné par
E. Foussard. Douze TP répartis sur deux langages et un projet : Python pour
l'outillage et les données, C++ pour la mécanique en dessous, puis un pont entre
les deux.

## Installation

Le côté Python tient dans un seul environnement conda, déclaré une fois dans
[environment.yml](environment.yml) :

```bash
conda env create -f environment.yml
conda activate m1ai-programming
```

Cet environnement s'enregistre aussi comme noyau Jupyter
*Python 3.11 (m1ai-programming)*, ce que demande la question 7 du TP1.

Le côté C++ prend ses bibliothèques dans `apt`, pour que le `find_package()` de
CMake les trouve dans `/usr` comme n'importe quelle bibliothèque système :

```bash
sudo apt install libboost-all-dev libgtest-dev
```

Le TP8 fait exception : son `CMakeLists.txt` appelle `add_subdirectory(pybind11)`
et attend donc une copie clonée dans le projet plutôt que celle de
l'environnement conda — `git clone https://github.com/pybind/pybind11.git` depuis
le dossier du TP, comme l'indique son sujet.

## Python

| TP | Sujet | Dossier |
|----|-------|---------|
| TP1 | Environnements virtuels, pip, uv, notebooks | [Python/TP1-environments/](Python/TP1-environments/README.md) |
| TP2 | Images en tableaux Numpy, convolution, détection de contours | [Python/TP2-image-processing/](Python/TP2-image-processing/) |
| TP3 | Un outil en ligne de commande qui repère les doublons | [Python/TP3-cli-tool/](Python/TP3-cli-tool/) |
| TP4 | Le module `logging`, puis son propre logger | [Python/TP4-logger/](Python/TP4-logger/) |

Le TP1 a pour sujet l'outillage d'environnement lui-même : son dossier garde donc
les deux réponses côte à côte. [venv-and-pip/](Python/TP1-environments/venv-and-pip/)
contient le `requirements.txt` figé, [uv-project/](Python/TP1-environments/uv-project/)
le même projet fait avec `uv`. Son exercice 2 est devenu
[WeatherMapApp](Python/TP1-environments/WeatherMapApp/README.md), une application Tkinter
qui cartographie les températures de France en direct ; ce dossier a son propre
README.

## C++

| TP | Sujet | Dossier |
|----|-------|---------|
| TP1 | Premiers programmes, CMake, Boost, Google Test | [C++/TP1-first-programs/](C++/TP1-first-programs/) |
| TP2 | C++ sans objets : un vecteur 2D en fonctions libres | [C++/TP2-without-objects/](C++/TP2-without-objects/) |
| TP3 | Le même vecteur, cette fois en classe | [C++/TP3-custom-vectors/](C++/TP3-custom-vectors/) |
| TP4 | Programmation orientée objet et graphes | [C++/TP4-oop-graphs/](C++/TP4-oop-graphs/) |
| TP5 | Sous-ensembles, itérateurs | [C++/TP5-subsets/](C++/TP5-subsets/) |
| TP6 | Templates | [C++/TP6-templates/](C++/TP6-templates/) |
| TP7 | Programmation concurrente | [C++/TP7-concurrency/](C++/TP7-concurrency/) |
| TP8 | Interopérabilité : lier C++ et Python avec pybind11 | [C++/TP8-interoperability/](C++/TP8-interoperability/) |

Chaque TP C++ part du même squelette, `C++/cmake-template/` — la bibliothèque
dans `src/`, les en-têtes dans `include/`, les tests dans `tests/` :

```bash
cmake -S . -B build          # ajouter -DBUILD_TESTS=ON pour compiler les tests
cmake --build build
./build/main                 # ./build/tests
```

**Un dossier de TP neuf doit échouer à sa première compilation.** Le squelette
compile avec `-Wall -Wextra -Wpedantic -Werror`, et les sources fournies sont des
souches qui font `throw std::runtime_error("Not implemented yet")` : chaque
paramètre inutilisé est donc une erreur tant que la fonction n'est pas écrite.
C'est l'exercice, pas une installation cassée.

## Où sont les explications

Chaque TP se documente lui-même. Ce qu'il a répondu, ce qu'il a coûté à
comprendre et les motifs à réutiliser restent dans son propre dossier plutôt
que dans un document commun : un dossier se lit ainsi seul, des années après.
Ceux du TP1 sont dans [Python/TP1-environments/](Python/TP1-environments/README.md).

## Projet

[Project-TSPSolver/](Project-TSPSolver/) — résolution du problème du voyageur de
commerce. `instance_generator.py` fabrique des instances aléatoires ;
`TSP-instances/` contient les jeux de référence TSPLIB pour se mesurer.

## Supports

Les sujets de TP, et le code fourni avec eux par E. Foussard, **ne sont pas
redistribués ici** — voir [NOTICE](../../../../NOTICE). Ils restent sur le disque
à côté de chaque TP, avec une extraction `.txt` qui les rend cherchables, et le
`.gitignore` tient les deux hors du dépôt. Ce qui est versionné est mon travail.
