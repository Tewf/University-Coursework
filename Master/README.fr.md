# Master : Intelligence Artificielle

> [Read in English](README.md) · [Ouvrir sur le site ↗](https://tewf.github.io/University-Coursework/Master/)

[Master Intelligence Artificielle](https://m-ai.imag.fr/), Université Grenoble
Alpes, co-porté par l'UFR IM²AG et Ensimag (Grenoble INP).

Le M1 est en cours et [`M1/`](M1/) se remplit au fil de sa production. Les
travaux de Licence sont dans [`Bachelor/`](../Bachelor/).

## Où sont les choses

Semestre par semestre, sur le même modèle que la Licence :

| Année | Semestre | Cours | Dossier |
|-------|----------|-------|---------|
| M1 | S7 | Programmation — Python, C++, pybind11, un solveur TSP | [M1/S7/Programming/](M1/S7/Programming/) |

Le cursus complet du M1 est dans [`M1/README.fr.md`](M1/README.fr.md).

## Travailler ici

Chaque cours déclare ses propres dépendances plutôt que de partager un
environnement commun : un cours peut ainsi être repris des années plus tard sans
avoir à le résoudre contre les autres. Pour le cours de programmation :

```bash
conda env create -f M1/S7/Programming/environment.yml
conda activate m1ai-programming
```

## Supports

Les sujets de TP et le code fourni appartiennent à leurs auteurs et **ne sont pas
redistribués** ici ; voir [NOTICE](../NOTICE). Ils restent sur le disque à côté de
chaque TP, avec une extraction `.txt` qui permet de les chercher, et le
`.gitignore` tient les deux hors du dépôt. Ce qui est versionné est mon travail.
