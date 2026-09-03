# Programmation

> [Read in English](README.md) · [Ouvrir sur le site ↗](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/)

**Cours :** Programmation, M1 Intelligence Artificielle, semestre 7, Université Grenoble Alpes
**Enseignant :** E. Foussard, avec J. Perier-Camby sur le TP3 Python

Douze TP répartis sur deux langages et un projet. Python pour l'outillage et les
données, C++ pour la mécanique en dessous, puis un pont entre les deux.

## Ce qu'on y apprend

- Construire et reproduire des environnements Python avec venv, pip, uv et conda
- Traiter les images comme des tableaux Numpy : padding, convolution, floutage, détection de contours
- Écrire des outils en ligne de commande qui parcourent le disque et hachent ce qu'ils trouvent
- Compiler du C++ avec CMake sous `-Wall -Wextra -Wpedantic -Werror`, et le tester avec Google Test
- Gérer la mémoire en C++ : destructeurs, sémantique de copie, et pointeurs intelligents
- Implémenter le contrat d'itérateur de la STL à la main, puis le rendre générique avec les templates
- Partager un état entre threads : mutex, variables de condition et atomiques
- Exposer du C++ à Python avec pybind11

## Les TP

Chaque TP a une page **steps** : les étapes qu'il demande, et pour le travail
déjà fait, ce que chaque étape a décidé et la référence qui l'a tranché.

### Python

| TP | Sujet | Dossier | Étapes |
|----|-------|---------|--------|
| TP1 | Environnements virtuels, pip, uv, notebooks | [Python/TP1-environments/](Python/TP1-environments/README.md) | [voir](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/Python/TP1-environments/steps/) |
| TP2 | Images en tableaux Numpy, convolution, détection de contours | [Python/TP2-image-processing/](Python/TP2-image-processing/README.md) | [voir](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/Python/TP2-image-processing/steps/) |
| TP3 | Un outil en ligne de commande qui repère les doublons | [Python/TP3-cli-tool/](Python/TP3-cli-tool/README.md) | [voir](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/Python/TP3-cli-tool/steps/) |
| TP4 | Le module `logging`, puis son propre logger | [Python/TP4-logger/](Python/TP4-logger/README.md) | [voir](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/Python/TP4-logger/steps/) |

### C++

| TP | Sujet | Dossier | Étapes |
|----|-------|---------|--------|
| TP1 | Premiers programmes, CMake, Boost, Google Test | [C++/TP1-first-programs/](C++/TP1-first-programs/README.md) | [voir](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/C++/TP1-first-programs/steps/) |
| TP2 | C++ sans objets : un vecteur 2D en fonctions libres | [C++/TP2-without-objects/](C++/TP2-without-objects/README.md) | [voir](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/C++/TP2-without-objects/steps/) |
| TP3 | Le même vecteur, cette fois en classe | [C++/TP3-custom-vectors/](C++/TP3-custom-vectors/README.md) | [voir](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/C++/TP3-custom-vectors/steps/) |
| TP4 | Programmation orientée objet et graphes | [C++/TP4-oop-graphs/](C++/TP4-oop-graphs/README.md) | [voir](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/C++/TP4-oop-graphs/steps/) |
| TP5 | Sous-ensembles, itérateurs | [C++/TP5-subsets/](C++/TP5-subsets/README.md) | [voir](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/C++/TP5-subsets/steps/) |
| TP6 | Templates | [C++/TP6-templates/](C++/TP6-templates/README.md) | [voir](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/C++/TP6-templates/steps/) |
| TP7 | Programmation concurrente | [C++/TP7-concurrency/](C++/TP7-concurrency/README.md) | [voir](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/C++/TP7-concurrency/steps/) |
| TP8 | Interopérabilité : lier C++ et Python avec pybind11 | [C++/TP8-interoperability/](C++/TP8-interoperability/README.md) | [voir](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/C++/TP8-interoperability/steps/) |

### Projet

[Project-TSPSolver/](Project-TSPSolver/README.md) résout le problème du voyageur
de commerce, exactement avec Held-Karp puis approximativement, et mesure l'un
contre l'autre. [Étapes ↗](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/Project-TSPSolver/steps/)

## Prérequis

Python et un langage compilé. Le côté C++ ne suppose pas de C++ antérieur, mais
il suppose des pointeurs déjà croisés : `C++/reference/` contient la note du
cours sur les pointeurs et les références.

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
l'environnement conda. Lancer `git clone https://github.com/pybind/pybind11.git`
depuis le dossier du TP, comme l'indique son sujet.

Chaque TP C++ part du même squelette, `C++/cmake-template/`, avec la
bibliothèque dans `src/`, les en-têtes dans `include/` et les tests dans
`tests/` :

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

## Structure du dossier

Chaque TP a la même forme. Une archive est décompressée dans le dossier auquel
elle appartient plutôt que laissée à côté, pour que chacun se lise comme un
projet qui tourne : le dossier `provided-files/` disparaît une fois vidé, et ce
qui en est sorti est listé dans le README du dossier.

```
Programming/
|-- environment.yml          <- l'unique environnement conda, pour tous les TP Python
|-- Python/
|   |-- TP1-environments/
|   |   |-- handout/         <- le sujet en PDF, à côté de son extraction .txt
|   |   |-- steps/           <- index.html, puis une page par étape
|   |   |-- README.md        <- ce qu'il demande, ce qu'il fournit, comment le lancer
|   |   |-- meteo.py         <- le code fourni, installé à sa place
|   |-- TP2-image-processing/ ... TP4-logger/
|-- C++/
|   |-- cmake-template/      <- le squelette dont part chaque TP C++
|   |-- reference/           <- la note du cours sur les pointeurs et références
|   |-- TP1-first-programs/ ... TP8-interoperability/
|-- Project-TSPSolver/       <- le projet, et les instances TSPLIB
```

`handout/` est gitignoré partout : les sujets ne sont pas à moi pour être republiés.

## Outils et bibliothèques

| Outil | Utilisé dans | Pour |
|-------|--------------|------|
| conda | tous les TP Python | l'unique environnement déclaré |
| venv, pip, uv | TP1 Python | le sujet même du TP |
| Numpy, Pillow | TP2, TP3 Python | les images comme tableaux |
| click, tqdm | TP3 Python | l'outil en ligne de commande |
| CMake | tous les TP C++ | compilation, tests, et les options d'avertissement |
| Boost, Google Test | C++ TP1 et suivants | utilitaires et tests unitaires |
| pybind11 | C++ TP8 | exposer le C++ à Python |

## Comment le code est écrit ici

Propre, réutilisable, et commenté de façon à survivre à un copier-coller dans un
autre projet. Au-delà, une règle gouverne : **facile à lire, et efficace en
effort.** Le code se lit du premier coup, l'effort s'arrête là où le polissage
rapporte moins qu'il ne coûte, et tout choix non évident porte sa référence *et*
la piste qui l'a trouvée, pour pouvoir être revérifié plutôt que cru sur parole.
Les pages `steps/` sont l'endroit où cette piste est écrite.

Les explications des concepts eux-mêmes vivent dans un coffre Obsidian séparé,
pas ici : un commentaire qui se met à enseigner la théorie appartient à la note.

## Supports

Les sujets de TP, et le code fourni avec eux, **ne sont pas redistribués ici** :
voir [NOTICE](../../../../NOTICE). Ils restent sur le disque à côté de chaque TP,
avec une extraction `.txt` qui les rend cherchables, et le `.gitignore` tient les
deux hors du dépôt. Ce qui est versionné est mon travail.
