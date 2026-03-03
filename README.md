# University Coursework

[![CI](https://github.com/Tewf/University-Coursework/actions/workflows/ci.yml/badge.svg)](https://github.com/Tewf/University-Coursework/actions/workflows/ci.yml)

> [Lire en francais](README.fr.md)

A comprehensive collection of coursework, projects, and assignments from my university studies at **Universite Grenoble Alpes**. This repository serves as both a **learning portfolio** and a **pedagogical resource** for students in applied mathematics, computer science, and economics.

## About

**Degree:** Licence MIASHS (Mathematiques et Informatique Appliquees aux Sciences Humaines et Sociales)
**Specialization:** Mathematiques, Informatique et Sciences Economiques (Years 2-3)
**University:** Universite Grenoble Alpes
**Program:** [Official page](https://formations.univ-grenoble-alpes.fr/fr/catalogue-2021/licence-XA/licence-mathematiques-et-informatique-appliquees-aux-sciences-humaines-et-sociales-miashs-IDIVNLE7/parcours-mathematiques-informatique-et-sciences-economiques-2e-et-3e-annee-IGRNO2YS.html)

## Repository Map

### [Bachelor/](Bachelor/)

| Domain | Courses | Key Topics |
|--------|---------|------------|
| **Mathematics** | [ComplementMath1](Bachelor/L3/S5/ComplementMath1/), [ComplementMath2](Bachelor/L3/S6/ComplementMath2/) | Fourier analysis, differential equations, machine learning |
| **Statistics** | [MathStat2](Bachelor/L3/S5/MathStat2/), [MathStat3](Bachelor/L3/S6/MathStat3/) | Estimation, hypothesis testing, ANOVA, regression |
| **Economics** | [Econometrie1](Bachelor/L3/S5/Econometrie1/), [Econometrie2](Bachelor/L3/S6/Econometrie2/) | Linear regression, real-estate price modeling |
| **Web Development** | [WebDev](Bachelor/L3/S6/WebDev/) | HTML, CSS, JavaScript, Node.js, Express, SQLite |
| **Programming** | [Java](Bachelor/Java/), [DrRacket](Bachelor/SecondSemestreLanguage/DrRacket/), [Prolog](Bachelor/SecondSemestreLanguage/Prolog/), [SQL](Bachelor/SecondSemestreLanguage/SQL/) | OOP, functional, logic, relational paradigms |
| **Systems & Networks** | [Reseaux](Bachelor/L3/S6/Reseaux/), [Systemes](Bachelor/L3/S6/Systemes/) | Network configuration, operating systems |

### [Master/](Master/)
Coming soon.

## Skills & Technologies

| Category | Technologies |
|----------|-------------|
| **Languages** | Java, R, Python, JavaScript, Racket, Prolog, SQL |
| **Web** | HTML5, CSS3, Node.js, Express.js |
| **Data Science** | R tidyverse, Quarto, Jupyter, statistical modeling |
| **Databases** | PostgreSQL, MySQL, SQLite |
| **Tools** | Git, VS Code, Maven, Quarto, LaTeX |

## Recommended Learning Paths

### Path 1: Statistics & Data Science
1. [MathStat2](Bachelor/L3/S5/MathStat2/) — Simulation, bootstrap, estimation
2. [MathStat3](Bachelor/L3/S6/MathStat3/) — Regression, ANOVA, non-parametric tests
3. [Econometrie1](Bachelor/L3/S5/Econometrie1/) — Applied econometric modeling
4. [ComplementMath2](Bachelor/L3/S6/ComplementMath2/) — Machine learning

### Path 2: Web Development
1. [WebDev TP0-TP1](Bachelor/L3/S6/WebDev/) — HTML fundamentals
2. [WebDev TP3-TP4](Bachelor/L3/S6/WebDev/) — CSS styling and layout
3. [WebDev TP5-TP7](Bachelor/L3/S6/WebDev/) — JavaScript and DOM
4. [WebDev TP8-TP9](Bachelor/L3/S6/WebDev/) — Server-side with Node.js and Express

### Path 3: Programming Paradigms
1. [Java OOP](Bachelor/Java/OOP/) — Object-oriented programming
2. [DrRacket](Bachelor/SecondSemestreLanguage/DrRacket/) — Functional programming
3. [Prolog](Bachelor/SecondSemestreLanguage/Prolog/) — Logic programming
4. [SQL](Bachelor/SecondSemestreLanguage/SQL/) — Relational databases

### Path 4: Applied Mathematics
1. [ComplementMath1](Bachelor/L3/S5/ComplementMath1/) — Fourier analysis, signal processing
2. [ComplementMath2](Bachelor/L3/S6/ComplementMath2/) — Machine learning techniques

## How to Navigate

**If you're a student:** Follow the learning paths above. Each course folder has its own README with prerequisites, concepts covered, and instructions for running the code.

**If you're a recruiter:** Check out the [project highlights in Bachelor/](Bachelor/) for concrete examples of applied work, including the Battleship AI, the econometrics real-estate analysis, and the full-stack web application.

## Getting Started

Most projects use R (Quarto notebooks) or JavaScript (Node.js). See each course's README for specific setup instructions.

```sh
# R/Quarto projects
quarto preview path/to/notebook.qmd

# Node.js projects
cd path/to/project && npm install && npm run dev

# Java projects
javac -d bin $(find src -name '*.java') && java -cp bin package.Main
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
