-- TP02: Les employés
-- Introduction aux bases de données relationnelles
-- SQL Queries for Employee Management

-- Part 1: Basic Queries

-- 1. Donner le nom de tous les employés
SELECT ENAME 
FROM EMP;

-- 2. Donner le nom et la date d'embauche des employés du département 20
SELECT ENAME, HIREDATE 
FROM EMP 
WHERE DEPTNO = 20;

-- 3. Donner tous les salaires perçus par les employés de l'entreprise
SELECT SAL, COMM 
FROM EMP;

-- 4. Donner le nom et le numéro du département des employés travaillant à Dallas
SELECT EMP.ENAME, EMP.DEPTNO 
FROM EMP 
JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO 
WHERE DEPT.LOC = 'Dallas';

-- 5. Donner le nom et le salaire des employés dont le nom commence par un 'M' et dont le salaire est supérieur à 1290$
SELECT ENAME, SAL 
FROM EMP 
WHERE ENAME LIKE 'M%' 
  AND SAL > 1290;

-- 6. Donner les départements employant des CLERK, SALESMAN et des ANALYST
SELECT DISTINCT DEPTNO 
FROM EMP 
WHERE JOB IN ('CLERK', 'SALESMAN', 'ANALYST');

-- 7. Donner le nom des chefs dont les employés perçoivent des commissions
SELECT DISTINCT E2.ENAME 
FROM EMP E1 
JOIN EMP E2 ON E1.MGR = E2.EMPNO 
WHERE E1.COMM IS NOT NULL AND E1.COMM > 0;

-- 8. Donner le nom et le salaire des employés des départements de Chicago et Dallas dont le salaire est supérieur à 1000$
SELECT EMP.ENAME, EMP.SAL 
FROM EMP 
JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO 
WHERE DEPT.LOC IN ('Chicago', 'Dallas') 
  AND EMP.SAL > 1000;

-- 9. Donner le nom des employés qui gagnent plus que leur chef
SELECT E1.ENAME 
FROM EMP E1 
JOIN EMP E2 ON E1.MGR = E2.EMPNO 
WHERE E1.SAL > E2.SAL;

-- 10. Donner la hiérarchie de l'entreprise
SELECT E1.EMPNO, E1.ENAME, E1.JOB, E2.ENAME AS MANAGER 
FROM EMP E1 
LEFT JOIN EMP E2 ON E1.MGR = E2.EMPNO 
ORDER BY E1.MGR, E1.EMPNO;

-- 11. Donner le nombre d'employés par niveau de hiérarchie
SELECT E2.ENAME AS MANAGER, COUNT(E1.EMPNO) AS nombre_employes 
FROM EMP E1 
JOIN EMP E2 ON E1.MGR = E2.EMPNO 
GROUP BY E1.MGR, E2.ENAME;

-- 12. Donner la moyenne des salaires par niveau de hiérarchie
SELECT E2.ENAME AS MANAGER, AVG(E1.SAL) AS salaire_moyen 
FROM EMP E1 
JOIN EMP E2 ON E1.MGR = E2.EMPNO 
GROUP BY E1.MGR, E2.ENAME;

-- Part 2: Query Variants

-- Variant 1.1: Donner le nom de tous les employés (par ordre alphabétique)
SELECT ENAME 
FROM EMP 
ORDER BY ENAME ASC;

-- Variant 1.2: Donner le nom de tous les employés (par ordre alphabétique inverse)
SELECT ENAME 
FROM EMP 
ORDER BY ENAME DESC;

-- Variant 1.3: Donner le nom de tous les employés (avec alias)
SELECT ENAME AS 'NOM de L''EMPLOYE' 
FROM EMP;

-- Variant 2.1: Donner le nom et la date d'embauche des employés du département 20 (ordre chronologique)
SELECT ENAME, HIREDATE 
FROM EMP 
WHERE DEPTNO = 20 
ORDER BY HIREDATE ASC;

-- Variant 2.2: Donner le nom et la date d'embauche des employés du département 20 (ordre chronologique inverse)
SELECT ENAME, HIREDATE 
FROM EMP 
WHERE DEPTNO = 20 
ORDER BY HIREDATE DESC;

-- Variant 2.3: Donner le nom et l'année d'embauche des employés du département 20
SELECT ENAME, CAST(strftime('%Y', HIREDATE) AS INTEGER) AS ANNEE 
FROM EMP 
WHERE DEPTNO = 20;

-- Variant 3.1: Donner tous les salaires (ordre croissant)
SELECT SAL 
FROM EMP 
ORDER BY SAL ASC;

-- Variant 3.2: Donner tous les salaires avec nom (ordre alphabétique des employés)
SELECT ENAME, SAL 
FROM EMP 
ORDER BY ENAME ASC;

-- Variant 4.1: Donner le nom, numéro du département et job des employés à Dallas
SELECT ENAME, DEPTNO, JOB 
FROM EMP 
JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO 
WHERE DEPT.LOC = 'Dallas' 
ORDER BY JOB ASC;

-- Variant 4.2: Donner le nom en majuscule et minuscule
SELECT UPPER(ENAME) AS nom_majuscule, LOWER(ENAME) AS nom_minuscule 
FROM EMP 
JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO 
WHERE DEPT.LOC = 'Dallas';

-- Variant 5.1: Noms commençant par 'M' avec salaire > 1290 (ordre alphabétique)
SELECT ENAME, SAL 
FROM EMP 
WHERE ENAME LIKE 'M%' AND SAL > 1290 
ORDER BY ENAME ASC;

-- Variant 5.2: Noms commençant par 'M' avec salaire > 1290 (ordre décroissant de salaire)
SELECT ENAME, SAL 
FROM EMP 
WHERE ENAME LIKE 'M%' AND SAL > 1290 
ORDER BY SAL DESC;

-- Variant 5.3: Noms commençant par 'M' avec salaire > 1290 (salaire seulement)
SELECT SAL 
FROM EMP 
WHERE ENAME LIKE 'M%' AND SAL > 1290;

-- Variant 5.4: Noms commençant par 'M' avec salaire + commissions
SELECT ENAME, SAL, COMM, (SAL + COALESCE(COMM, 0)) AS total_revenu 
FROM EMP 
WHERE ENAME LIKE 'M%' AND (SAL + COALESCE(COMM, 0)) > 1290;

-- Variant 6.1: Nom et numéro de département des chefs dont employés ont commissions
SELECT DISTINCT E2.ENAME, E2.DEPTNO 
FROM EMP E1 
JOIN EMP E2 ON E1.MGR = E2.EMPNO 
WHERE E1.COMM IS NOT NULL AND E1.COMM > 0 
ORDER BY E2.DEPTNO ASC;

-- Variant 7.1: Chicago et Dallas, salaire > 1000 (salaire + commissions cumulés)
SELECT EMP.ENAME, EMP.SAL, EMP.COMM, (EMP.SAL + COALESCE(EMP.COMM, 0)) AS total_revenu 
FROM EMP 
JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO 
WHERE DEPT.LOC IN ('Chicago', 'Dallas') 
  AND (EMP.SAL + COALESCE(EMP.COMM, 0)) > 1000;

-- Variant 7.2: Chicago et Dallas (ordre décroissant de revenu, puis alphabétique)
SELECT EMP.ENAME, (EMP.SAL + COALESCE(EMP.COMM, 0)) AS total_revenu 
FROM EMP 
JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO 
WHERE DEPT.LOC IN ('Chicago', 'Dallas') 
  AND (EMP.SAL + COALESCE(EMP.COMM, 0)) > 1000 
ORDER BY total_revenu DESC, EMP.ENAME ASC;

-- Variant 8.1: Employés gagnant plus que leur chef (info complète)
SELECT E1.ENAME, E1.SAL, E1.DEPTNO, E2.ENAME AS manager_name, E2.SAL AS manager_sal 
FROM EMP E1 
JOIN EMP E2 ON E1.MGR = E2.EMPNO 
WHERE E1.SAL > E2.SAL;
