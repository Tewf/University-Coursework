-- TP03: L'agence de voyages
-- Introduction aux bases de données relationnelles
-- SQL Queries for Travel Agency Management

-- Part 1: Integrity Checks and Updates
-- (These are conceptual SQL statements for the modifications described)

-- 1.1: Ajout d'une étape au circuit 10 en dernier rang (Londres, 2 jours)
-- Check if circuit 10 exists:
-- SELECT * FROM CIRCUIT WHERE NC = 10;
-- Update the circuit stage count:
-- UPDATE CIRCUIT SET NBETAPES = NBETAPES + 1 WHERE NC = 10;
-- Insert the new stage:
-- INSERT INTO ETAPE (NOMV, NC, NUMETAPE, DUREE) 
-- SELECT 'Londres', 10, MAX(NUMETAPE) + 1, 2 FROM ETAPE WHERE NC = 10;

-- 1.2: Réservation de 3 places par Mila pour le circuit 7 partant le 5/5/02
-- Check if Mila exists:
-- SELECT * FROM RESERVATION WHERE NOMC = 'Mila';
-- Check if the circuit programming exists:
-- SELECT * FROM PROGRAMMATION WHERE NC = 7 AND DATE = '2002-05-05';
-- Check available places:
-- SELECT PLACES FROM PROGRAMMATION WHERE NC = 7 AND DATE = '2002-05-05';
-- Insert the reservation and update available places:
-- INSERT INTO RESERVATION (NC, NR, NOMC, PLACES, DATE) VALUES (7, <NR>, 'Mila', 3, '2002-05-05');
-- UPDATE PROGRAMMATION SET PLACES = PLACES - 3 WHERE NC = 7 AND DATE = '2002-05-05';

-- 1.3: Suppression de toutes les programmations terminées (dates passées)
-- DELETE FROM PROGRAMMATION WHERE DATE < CURRENT_DATE;

-- 1.4: Londres ne peut plus accueillir de visiteurs du 1/02/02 au 1/04/02
-- Check all circuits visiting London during this period:
-- SELECT DISTINCT C.NC, P.DATE FROM CIRCUIT C 
-- JOIN ETAPE E ON C.NC = E.NC AND E.NOMV = 'Londres'
-- JOIN PROGRAMMATION P ON C.NC = P.NC 
-- WHERE P.DATE BETWEEN '2002-02-01' AND '2002-04-01';

-- Part 2: Schema Modifications (Conceptual - Not Executable)
-- The refined schema should include:
-- 1. Multiple programmations at different times: Add HEURE (time) column to PROGRAMMATION
-- ALTER TABLE PROGRAMMATION ADD COLUMN HEURE TIME;
-- PROGRAMMATION Primary Key: (NC, DATE, HEURE)

-- 2. Multiple cities visited per day: ETAPE structure remains the same
--    Add NUMETAPE_MINUTE to track time within an etape

-- 3. Travel time between cities: Add new table
-- CREATE TABLE TRAJET (
--   VILLE_DEPART VARCHAR NOT NULL,
--   VILLE_ARRIVEE VARCHAR NOT NULL,
--   DUREE_TRAJET TIME NOT NULL,
--   PRIMARY KEY (VILLE_DEPART, VILLE_ARRIVEE),
--   FOREIGN KEY (VILLE_DEPART) REFERENCES VILLE(NOMV),
--   FOREIGN KEY (VILLE_ARRIVEE) REFERENCES VILLE(NOMV)
-- );

-- Part 3: Query Expressions

-- Question 3.1: Ville de départ du circuit 10?
SELECT VILLE.NOMV, VILLA.PAYS
FROM ETAPE 
JOIN VILLE ON ETAPE.NOMV = VILLE.NOMV 
WHERE ETAPE.NC = 10 
  AND ETAPE.NUMETAPE = (SELECT MIN(NUMETAPE) FROM ETAPE WHERE NC = 10);

-- Question 3.2: Noms des monuments visités par Mafalda?
SELECT DISTINCT MONUMENT.NOMM 
FROM RESERVATION 
JOIN CIRCUIT ON RESERVATION.NC = CIRCUIT.NC 
JOIN ETAPE ON CIRCUIT.NC = ETAPE.NC 
JOIN MONUMENT ON ETAPE.NOMV = MONUMENT.NOMV 
WHERE RESERVATION.NOMC = 'Mafalda';

-- Question 3.3: Nombre de places mises à la vente pour le circuit 5 à la date du 9/11/02?
SELECT PLACES 
FROM PROGRAMMATION 
WHERE NC = 5 AND DATE = '2002-11-09';

-- Question 4: Additional Queries (based on context)

-- 4.1: List all circuits with their duration
SELECT CIRCUIT.NC, CIRCUIT.NBETAPES, CIRCUIT.PRIX, SUM(ETAPE.DUREE) AS total_duree 
FROM CIRCUIT 
JOIN ETAPE ON CIRCUIT.NC = ETAPE.NC 
GROUP BY CIRCUIT.NC;

-- 4.2: List all reservations with client names and circuit prices
SELECT RESERVATION.NR, RESERVATION.NOMC, RESERVATION.NC, RESERVATION.PLACES, 
       RESERVATION.DATE, CIRCUIT.PRIX 
FROM RESERVATION 
JOIN CIRCUIT ON RESERVATION.NC = CIRCUIT.NC 
ORDER BY RESERVATION.DATE DESC;

-- 4.3: Clients who visited London
SELECT DISTINCT RESERVATION.NOMC 
FROM RESERVATION 
JOIN CIRCUIT ON RESERVATION.NC = CIRCUIT.NC 
JOIN ETAPE ON CIRCUIT.NC = ETAPE.NC 
WHERE ETAPE.NOMV = 'Londres';

-- 4.4: Circuits visiting all monuments in a city
SELECT CIRCUIT.NC, ETAPE.NOMV, COUNT(MONUMENT.NOMM) AS nb_monuments 
FROM CIRCUIT 
JOIN ETAPE ON CIRCUIT.NC = ETAPE.NC 
LEFT JOIN MONUMENT ON ETAPE.NOMV = MONUMENT.NOMV 
GROUP BY CIRCUIT.NC, ETAPE.NOMV;

-- 4.5: Most popular circuits (by number of reservations)
SELECT CIRCUIT.NC, COUNT(RESERVATION.NR) AS nb_reservations 
FROM CIRCUIT 
LEFT JOIN RESERVATION ON CIRCUIT.NC = RESERVATION.NC 
GROUP BY CIRCUIT.NC 
ORDER BY nb_reservations DESC;

-- 4.6: Total revenue by circuit
SELECT CIRCUIT.NC, CIRCUIT.PRIX, COUNT(RESERVATION.NR) AS nb_reservations, 
       (CIRCUIT.PRIX * COUNT(RESERVATION.NR)) AS total_revenue 
FROM CIRCUIT 
LEFT JOIN RESERVATION ON CIRCUIT.NC = RESERVATION.NC 
GROUP BY CIRCUIT.NC;

-- 4.7: Clients with most bookings
SELECT RESERVATION.NOMC, COUNT(RESERVATION.NR) AS nb_reservations, 
       SUM(RESERVATION.PLACES) AS total_places 
FROM RESERVATION 
GROUP BY RESERVATION.NOMC 
ORDER BY nb_reservations DESC;

-- 4.8: Circuits and their starting cities
SELECT DISTINCT CIRCUIT.NC, MIN(ETAPE.NUMETAPE) AS first_stage, 
       ETAPE.NOMV AS starting_city 
FROM CIRCUIT 
JOIN ETAPE ON CIRCUIT.NC = ETAPE.NC 
WHERE ETAPE.NUMETAPE = 1 
GROUP BY CIRCUIT.NC;
