-- TP01: Le grand bazard
-- Introduction aux bases de données relationnelles
-- SQL Queries for Product and Sales Management

-- 1. Donner les noms et couleurs de tous les produits
SELECT NOMP, COULEUR 
FROM PRODUIT;

-- 2. Donner les noms et quantités en stock des produits de couleur rouge
SELECT NOMP, QTP 
FROM PRODUIT 
WHERE COULEUR = 'rouge';

-- 3. Donner les numéros de vente, le nom du client, la quantité vendue pour les ventes du
-- produit de nom « torchon », réalisées avant le 12/09/87
SELECT VENTE.NVEN, VENTE.NOMC, VENTE.QTV 
FROM VENTE 
JOIN PRODUIT ON VENTE.NPRV = PRODUIT.NPRO 
WHERE PRODUIT.NOMP = 'torchon' 
  AND VENTE.DATEV < '1987-09-12';

-- 4. Donner les noms des clients ayant acheté au moins un produit de couleur verte
SELECT DISTINCT VENTE.NOMC 
FROM VENTE 
JOIN PRODUIT ON VENTE.NPRV = PRODUIT.NPRO 
WHERE PRODUIT.COULEUR = 'verte';

-- 5. Donner les noms des fournisseurs qui sont également des clients
SELECT DISTINCT ACHAT.NOMF 
FROM ACHAT 
WHERE ACHAT.NOMF IN (SELECT DISTINCT VENTE.NOMC FROM VENTE);

-- 6. Donner les noms des fournisseurs qui fournissent les produits de couleur bleu et dont la
-- quantité en stock (actuellement) est inférieur à 100
SELECT DISTINCT ACHAT.NOMF 
FROM ACHAT 
JOIN PRODUIT ON ACHAT.NPRA = PRODUIT.NPRO 
WHERE PRODUIT.COULEUR = 'bleu' 
  AND PRODUIT.QTP < 100;

-- 7. Donner le nom des fournisseurs avec lesquels aucune commande de produit n'a été réalisée
-- depuis le 30/06/87
SELECT NOMF 
FROM (
  SELECT DISTINCT NOMF FROM ACHAT
) AS AllFournisseurs 
WHERE NOMF NOT IN (
  SELECT DISTINCT NOMF FROM ACHAT 
  WHERE DATEA >= '1987-06-30'
);

-- 8. Donner pour chaque produit, les noms des fournisseurs du produit et les noms des clients l'ayant acheté
SELECT PRODUIT.NOMP, ACHAT.NOMF, VENTE.NOMC 
FROM PRODUIT 
LEFT JOIN ACHAT ON PRODUIT.NPRO = ACHAT.NPRA 
LEFT JOIN VENTE ON PRODUIT.NPRO = VENTE.NPRV 
ORDER BY PRODUIT.NOMP;

-- 9. Donner les noms des clients ayant acheté au moins une fois de tous les produits disponibles
SELECT VENTE.NOMC 
FROM VENTE 
GROUP BY VENTE.NOMC 
HAVING COUNT(DISTINCT VENTE.NPRV) = (SELECT COUNT(DISTINCT NPRO) FROM PRODUIT);

-- 10. Donner les noms des fournisseurs qui fournissent tous les produits
SELECT NOMF 
FROM ACHAT 
GROUP BY NOMF 
HAVING COUNT(DISTINCT NPRA) = (SELECT COUNT(DISTINCT NPRO) FROM PRODUIT);

-- 11. Donner, pour chaque couleur, le nombre de produits de cette couleur
SELECT COULEUR, COUNT(*) AS nombre 
FROM PRODUIT 
GROUP BY COULEUR;

-- 12. Donner le nom et le nombre des produits vendus lors de la plus grosse vente
SELECT PRODUIT.NOMP, VENTE.QTV 
FROM VENTE 
JOIN PRODUIT ON VENTE.NPRV = PRODUIT.NPRO 
WHERE VENTE.QTV = (SELECT MAX(QTV) FROM VENTE);
