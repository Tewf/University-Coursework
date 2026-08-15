# SQL : Bases de donnees relationnelles

> [Read in English](README.md) · [Ouvrir sur le site ↗](https://tewf.github.io/University-Coursework/Bachelor/SecondSemestreLanguage/SQL/)

**Cours :** Bases de donnees, Licence MIASHS, Universite Grenoble Alpes

Exercices pratiques couvrant le SQL des requetes de base aux transactions et vues. Chaque TP s'appuie progressivement sur le precedent.

## Ce que vous apprendrez

- Conception de schemas relationnels et creation de tables
- Requetes SELECT avec filtrage et tri
- Operations JOIN : interne, externe, croisee
- Operations ensemblistes : UNION, INTERSECT, EXCEPT
- Sous-requetes et requetes imbriquees
- Agregation : COUNT, SUM, AVG, GROUP BY, HAVING
- Transactions, vues et integrite des donnees

## Vue d'ensemble des TPs

| TP | Theme | Concepts SQL cles |
|----|-------|-------------------|
| **TP1** | Fondamentaux | CREATE TABLE, SELECT, WHERE, ORDER BY |
| **TP2** | Jointures & Ensembles | JOIN, UNION, INTERSECT, sous-requetes |
| **TP3** | Agregation | GROUP BY, HAVING, COUNT, SUM, AVG |
| **TP4** | Transactions | BEGIN, COMMIT, ROLLBACK, CREATE VIEW |

Chaque fichier `.sql` a un `.pdf` correspondant avec les instructions de l'exercice.

## Executer les scripts

```sh
# PostgreSQL
psql -d nom_base -f tp01.sql

# SQLite
sqlite3 base.db < tp01.sql

# MySQL
mysql -u utilisateur -p nom_base < tp01.sql
```

Creer d'abord la base depuis `bd/`, puis executer chaque fichier TP.

## Structure du dossier

```
SQL/
|-- tp01.sql / tp01.pdf    <- Schemas, SELECT de base
|-- tp02.sql / tp02.pdf    <- Jointures, operations ensemblistes
|-- tp03.sql / tp03.pdf    <- Agregation, regroupement
|-- tp04.sql / tp04.pdf    <- Transactions, vues
|-- bd/                    <- Fichiers de base de donnees
```

## Prerequis

- Aucune experience SQL prealable requise
- Comprehension des donnees tabulaires (lignes et colonnes)

## Ressources

- [Supports de cours](https://pellierd.github.io/homepage/teaching/databases/)

## Supports de cours

Les sujets de TP01 à TP04 ont été rédigés par l'équipe enseignante du cours de bases de données (UGA).

Non redistribués ici ; voir [NOTICE](../../../NOTICE) pour les crédits complets.
