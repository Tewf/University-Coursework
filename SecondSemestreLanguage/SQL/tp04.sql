-- TP04: La bibliothèque
-- Introduction aux bases de données relationnelles
-- SQL Queries for Library Management

-- Part 1: Database Creation (SQL DDL)

CREATE TABLE LeCatalogue (
  titre TEXT NOT NULL,
  nom TEXT NOT NULL,
  prénom TEXT NOT NULL,
  année INTEGER NOT NULL CHECK (année > 0),
  PRIMARY KEY (titre, nom, prénom)
);

CREATE TABLE LeFonds (
  cote INTEGER PRIMARY KEY,
  titre TEXT NOT NULL,
  FOREIGN KEY (titre) REFERENCES LeCatalogue(titre)
);

CREATE TABLE LesAdhérents (
  noAdh INTEGER PRIMARY KEY,
  datAdh DATE NOT NULL,
  nom TEXT NOT NULL,
  prénom TEXT NOT NULL,
  anNais INTEGER NOT NULL CHECK (anNais > 0),
  adresse TEXT NOT NULL
);

CREATE TABLE LesEmprunts (
  cote INTEGER NOT NULL,
  noAdh INTEGER NOT NULL,
  datEmp DATE NOT NULL,
  PRIMARY KEY (cote, noAdh, datEmp),
  FOREIGN KEY (cote) REFERENCES LeFonds(cote),
  FOREIGN KEY (noAdh) REFERENCES LesAdhérents(noAdh)
);

-- Part 2: Query Expressions

-- 1. Noms et prénoms des adhérents de la bibliothèque
SELECT nom, prénom 
FROM LesAdhérents;

-- 2. Titres des œuvres éditées pour la première fois avant 1900
SELECT DISTINCT titre 
FROM LeCatalogue 
WHERE année < 1900;

-- 3. Noms et prénoms des adhérents habitant Papeete, qui empruntent un livre de titre « Dune »
SELECT DISTINCT LesAdhérents.nom, LesAdhérents.prénom 
FROM LesAdhérents 
JOIN LesEmprunts ON LesAdhérents.noAdh = LesEmprunts.noAdh 
JOIN LeFonds ON LesEmprunts.cote = LeFonds.cote 
WHERE LesAdhérents.adresse LIKE '%Papeete%' 
  AND LeFonds.titre = 'Dune';

-- 4. Pour chaque emprunt dont la durée est supérieure ou égale à 15 jours,
-- numéro, nom, prénom et nombre de jours de dépassement
SELECT LesAdhérents.noAdh, LesAdhérents.nom, LesAdhérents.prénom, 
       CAST((julianday('now') - julianday(LesEmprunts.datEmp)) AS INTEGER) AS jours_emprunt,
       CAST((julianday('now') - julianday(LesEmprunts.datEmp)) AS INTEGER) - 15 AS jours_depassement
FROM LesAdhérents 
JOIN LesEmprunts ON LesAdhérents.noAdh = LesEmprunts.noAdh 
WHERE (julianday('now') - julianday(LesEmprunts.datEmp)) >= 15;

-- 5. Cotes des livres disponibles de titre « Dosadi » ou d'auteur Franck Herbert
SELECT DISTINCT LeFonds.cote 
FROM LeFonds 
JOIN LeCatalogue ON LeFonds.titre = LeCatalogue.titre 
WHERE (LeFonds.titre = 'Dosadi' OR LeCatalogue.nom = 'Herbert')
  AND LeFonds.cote NOT IN (
    SELECT DISTINCT cote FROM LesEmprunts
  );

-- 6. Nombre d'adhérents de la bibliothèque
SELECT COUNT(DISTINCT noAdh) AS nombre_adherents 
FROM LesAdhérents;

-- 7. Numéro, noms et prénoms des adhérents les plus jeunes.
-- Pour chacun, on donnera aussi les titres des livres empruntés
SELECT LesAdhérents.noAdh, LesAdhérents.nom, LesAdhérents.prénom, LeFonds.titre 
FROM LesAdhérents 
LEFT JOIN LesEmprunts ON LesAdhérents.noAdh = LesEmprunts.noAdh 
LEFT JOIN LeFonds ON LesEmprunts.cote = LeFonds.cote 
WHERE LesAdhérents.anNais = (SELECT MAX(anNais) FROM LesAdhérents)
ORDER BY LesAdhérents.noAdh;

-- 8. Noms et adresses des adhérents qui empruntent au moins 2 livres,
-- et qui sont auteurs d'au moins une œuvre de la bibliothèque
SELECT DISTINCT LesAdhérents.nom, LesAdhérents.adresse 
FROM LesAdhérents 
JOIN LesEmprunts ON LesAdhérents.noAdh = LesEmprunts.noAdh 
WHERE (
  SELECT COUNT(DISTINCT cote) FROM LesEmprunts 
  WHERE LesEmprunts.noAdh = LesAdhérents.noAdh
) >= 2
AND (LesAdhérents.nom, LesAdhérents.prénom) IN (
  SELECT nom, prénom FROM LeCatalogue
);

-- Additional Useful Queries

-- A.1: List all books with authors and publication years
SELECT titre, nom, prénom, année 
FROM LeCatalogue 
ORDER BY titre;

-- A.2: Current loans with due information
SELECT LesAdhérents.noAdh, LesAdhérents.nom, LesAdhérents.prénom,
       LeFonds.cote, LeFonds.titre, LesEmprunts.datEmp,
       CAST((julianday('now') - julianday(LesEmprunts.datEmp)) AS INTEGER) AS jours_empruntés
FROM LesAdhérents 
JOIN LesEmprunts ON LesAdhérents.noAdh = LesEmprunts.noAdh 
JOIN LeFonds ON LesEmprunts.cote = LeFonds.cote 
ORDER BY LesEmprunts.datEmp;

-- A.3: Books in stock (not borrowed)
SELECT DISTINCT LeFonds.cote, LeFonds.titre 
FROM LeFonds 
WHERE LeFonds.cote NOT IN (
  SELECT DISTINCT cote FROM LesEmprunts
)
ORDER BY LeFonds.titre;

-- A.4: Most borrowed books
SELECT LeFonds.titre, COUNT(LesEmprunts.cote) AS times_borrowed 
FROM LeFonds 
LEFT JOIN LesEmprunts ON LeFonds.cote = LesEmprunts.cote 
GROUP BY LeFonds.titre 
ORDER BY times_borrowed DESC;

-- A.5: Members with overdue books (more than 30 days)
SELECT DISTINCT LesAdhérents.noAdh, LesAdhérents.nom, LesAdhérents.prénom,
       LeFonds.titre, 
       CAST((julianday('now') - julianday(LesEmprunts.datEmp)) AS INTEGER) AS jours_en_retard
FROM LesAdhérents 
JOIN LesEmprunts ON LesAdhérents.noAdh = LesEmprunts.noAdh 
JOIN LeFonds ON LesEmprunts.cote = LeFonds.cote 
WHERE (julianday('now') - julianday(LesEmprunts.datEmp)) > 30
ORDER BY LesAdhérents.noAdh;

-- A.6: Authors who are also library members
SELECT DISTINCT LeCatalogue.nom, LeCatalogue.prénom 
FROM LeCatalogue 
WHERE (LeCatalogue.nom, LeCatalogue.prénom) IN (
  SELECT nom, prénom FROM LesAdhérents
);

-- A.7: Books by each author currently in the library
SELECT LeCatalogue.nom, LeCatalogue.prénom, 
       COUNT(DISTINCT LeFonds.cote) AS nombre_exemplaires 
FROM LeCatalogue 
LEFT JOIN LeFonds ON LeCatalogue.titre = LeFonds.titre 
GROUP BY LeCatalogue.nom, LeCatalogue.prénom 
ORDER BY LeCatalogue.nom, LeCatalogue.prénom;

-- A.8: Member borrowing history summary
SELECT LesAdhérents.nom, LesAdhérents.prénom,
       COUNT(DISTINCT LesEmprunts.cote) AS nombre_emprunts_distincts,
       COUNT(LesEmprunts.cote) AS nombre_total_emprunts
FROM LesAdhérents 
LEFT JOIN LesEmprunts ON LesAdhérents.noAdh = LesEmprunts.noAdh 
GROUP BY LesAdhérents.noAdh
ORDER BY nombre_total_emprunts DESC;
