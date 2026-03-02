# SQL — Relational Databases

> [Lire en francais](README.fr.md)

**Course:** Databases — Licence MIASHS, Universite Grenoble Alpes

Practical exercises covering SQL from basic queries to transactions and views. Each TP builds progressively on the previous one.

## What You'll Learn

- Relational schema design and table creation
- SELECT queries with filtering and sorting
- JOIN operations: inner, outer, cross
- Set operations: UNION, INTERSECT, EXCEPT
- Subqueries and nested queries
- Aggregation: COUNT, SUM, AVG, GROUP BY, HAVING
- Transactions, views, and data integrity

## TP Overview

| TP | Topic | Key SQL Concepts |
|----|-------|-----------------|
| **TP1** | Foundations | CREATE TABLE, SELECT, WHERE, ORDER BY |
| **TP2** | Joins & Sets | JOIN, UNION, INTERSECT, subqueries |
| **TP3** | Aggregation | GROUP BY, HAVING, COUNT, SUM, AVG |
| **TP4** | Transactions | BEGIN, COMMIT, ROLLBACK, CREATE VIEW |

Each `.sql` file has a corresponding `.pdf` with the assignment instructions.

## Running the Scripts

```sh
# PostgreSQL
psql -d database_name -f tp01.sql

# SQLite
sqlite3 database.db < tp01.sql

# MySQL
mysql -u user -p database_name < tp01.sql
```

Create the database from `bd/` first, then execute each TP file.

## Folder Structure

```
SQL/
|-- tp01.sql / tp01.pdf    <- Schemas, basic SELECT
|-- tp02.sql / tp02.pdf    <- Joins, set operations
|-- tp03.sql / tp03.pdf    <- Aggregation, grouping
|-- tp04.sql / tp04.pdf    <- Transactions, views
|-- bd/                    <- Database files
```

## Prerequisites

- No prior SQL experience needed
- Understanding of tabular data (rows and columns)

## Resources

- [Course materials](https://pellierd.github.io/homepage/teaching/databases/)
