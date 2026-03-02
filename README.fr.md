# Travaux Universitaires

> [Read in English](README.md)

Une collection complete de travaux pratiques, projets et exercices realises durant mes etudes a l'**Universite Grenoble Alpes**. Ce repository sert a la fois de **portfolio d'apprentissage** et de **ressource pedagogique** pour les etudiants en mathematiques appliquees, informatique et economie.

## A propos

**Diplome :** Licence MIASHS (Mathematiques et Informatique Appliquees aux Sciences Humaines et Sociales)
**Specialisation :** Mathematiques, Informatique et Sciences Economiques (annees 2-3)
**Universite :** Universite Grenoble Alpes
**Programme :** [Page officielle](https://formations.univ-grenoble-alpes.fr/fr/catalogue-2021/licence-XA/licence-mathematiques-et-informatique-appliquees-aux-sciences-humaines-et-sociales-miashs-IDIVNLE7/parcours-mathematiques-informatique-et-sciences-economiques-2e-et-3e-annee-IGRNO2YS.html)

## Carte du repository

### [Bachelor/](Bachelor/)

| Domaine | Cours | Themes cles |
|---------|-------|-------------|
| **Mathematiques** | [ComplementMath1](Bachelor/L3/S5/ComplementMath1/), [ComplementMath2](Bachelor/L3/S6/ComplementMath2/) | Analyse de Fourier, equations differentielles, apprentissage automatique |
| **Statistiques** | [MathStat2](Bachelor/L3/S5/MathStat2/), [MathStat3](Bachelor/L3/S6/MathStat3/) | Estimation, tests d'hypothese, ANOVA, regression |
| **Economie** | [Econometrie1](Bachelor/L3/S5/Econometrie1/), [Econometrie2](Bachelor/L3/S6/Econometrie2/) | Regression lineaire, modelisation des prix immobiliers |
| **Developpement Web** | [WebDev](Bachelor/L3/S6/WebDev/) | HTML, CSS, JavaScript, Node.js, Express, SQLite |
| **Programmation** | [Java](Bachelor/Java/), [DrRacket](Bachelor/SecondSemestreLanguage/DrRacket/), [Prolog](Bachelor/SecondSemestreLanguage/Prolog/), [SQL](Bachelor/SecondSemestreLanguage/SQL/) | POO, fonctionnel, logique, relationnel |
| **Systemes & Reseaux** | [Reseaux](Bachelor/L3/S6/Reseaux/), [Systemes](Bachelor/L3/S6/Systemes/) | Configuration reseau, systemes d'exploitation |

### [Master/](Master/)
A venir.

## Competences & Technologies

| Categorie | Technologies |
|-----------|-------------|
| **Langages** | Java, R, Python, JavaScript, Racket, Prolog, SQL |
| **Web** | HTML5, CSS3, Node.js, Express.js |
| **Data Science** | R tidyverse, Quarto, Jupyter, modelisation statistique |
| **Bases de donnees** | PostgreSQL, MySQL, SQLite |
| **Outils** | Git, VS Code, Maven, Quarto, LaTeX |

## Parcours d'apprentissage recommandes

### Parcours 1 : Statistiques & Data Science
1. [MathStat2](Bachelor/L3/S5/MathStat2/) — Simulation, bootstrap, estimation
2. [MathStat3](Bachelor/L3/S6/MathStat3/) — Regression, ANOVA, tests non-parametriques
3. [Econometrie1](Bachelor/L3/S5/Econometrie1/) — Modelisation econometrique appliquee
4. [ComplementMath2](Bachelor/L3/S6/ComplementMath2/) — Apprentissage automatique

### Parcours 2 : Developpement Web
1. [WebDev TP0-TP1](Bachelor/L3/S6/WebDev/) — Les bases du HTML
2. [WebDev TP3-TP4](Bachelor/L3/S6/WebDev/) — Mise en forme CSS
3. [WebDev TP5-TP7](Bachelor/L3/S6/WebDev/) — JavaScript et DOM
4. [WebDev TP8-TP9](Bachelor/L3/S6/WebDev/) — Serveur avec Node.js et Express

### Parcours 3 : Paradigmes de programmation
1. [Java POO](Bachelor/Java/OOP/) — Programmation orientee objet
2. [DrRacket](Bachelor/SecondSemestreLanguage/DrRacket/) — Programmation fonctionnelle
3. [Prolog](Bachelor/SecondSemestreLanguage/Prolog/) — Programmation logique
4. [SQL](Bachelor/SecondSemestreLanguage/SQL/) — Bases de donnees relationnelles

### Parcours 4 : Mathematiques appliquees
1. [ComplementMath1](Bachelor/L3/S5/ComplementMath1/) — Analyse de Fourier, traitement du signal
2. [ComplementMath2](Bachelor/L3/S6/ComplementMath2/) — Techniques d'apprentissage automatique

## Comment naviguer

**Si vous etes etudiant :** Suivez les parcours d'apprentissage ci-dessus. Chaque dossier de cours a son propre README avec les prerequis, les concepts abordes et les instructions pour executer le code.

**Si vous etes recruteur :** Consultez les [projets phares dans Bachelor/](Bachelor/) pour des exemples concrets de travail applique, notamment le Battleship AI, l'analyse econometrique immobiliere et l'application web full-stack.

## Pour commencer

La plupart des projets utilisent R (notebooks Quarto) ou JavaScript (Node.js). Consultez le README de chaque cours pour les instructions specifiques.

```sh
# Projets R/Quarto
quarto preview chemin/vers/notebook.qmd

# Projets Node.js
cd chemin/vers/projet && npm install && npm run dev

# Projets Java
javac -d bin $(find src -name '*.java') && java -cp bin package.Main
```

## Licence

Ce projet est sous licence MIT. Voir [LICENSE](LICENSE) pour plus de details.
