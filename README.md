# University Coursework

[![CI](https://github.com/Tewf/University-Coursework/actions/workflows/ci.yml/badge.svg)](https://github.com/Tewf/University-Coursework/actions/workflows/ci.yml)

> [Lire en français](README.fr.md) · [Read the machine-learning report online ↗](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/)

Coursework from my **Licence MIASHS** (Mathematics, Computer Science and
Economics applied to Social Sciences) at **Université Grenoble Alpes**, now
continued in the [**Master of Artificial Intelligence**](https://m-ai.imag.fr/),
jointly delivered by **UFR IM²AG** and **Ensimag** (Grenoble INP).

Everything here is source plus its rendered output, so you can read the work
without cloning or running anything.

---

## Start here

If you only open one thing, open the first.

### 🧪 [Perfume satisfaction prediction](Bachelor/L3/S6/ComplementMath2/Projet/) · [read the report ↗](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/)

A full supervised-learning pipeline in R/Quarto: exploration → preparation →
**logistic regression, decision tree, random forest, kNN and naive Bayes**,
compared on ROC and confusion matrices, with a leakage-proof split, persisted
models and a written report. 1,398 lines across 8 `.qmd` files.
*Group project — HAMLIL · PARDO TERAN · EL KORAICHI · ANZID.*

### 📈 [Grenoble housing prices](https://github.com/Tewf/grenoble-housing-prices) *(own repo)*

Hedonic price modelling on the French **DVF land-registry open data**: cleaning,
an OLS baseline with heteroskedasticity and multicollinearity diagnostics, then
a random-forest extension that cuts RMSE from €265k to €59k.
*Group project — HAMLIL · ANZID · EL KORAICHI.*

### 🎯 [Battleship AI](https://github.com/Tewf/Complement_IA) *(own repo)*

2,500 lines of modular Java 17: **Markov and Monte-Carlo probabilistic
targeting** bots, a reproducible tournament harness emitting CSV and plots, a
Swing GUI, Javadoc, and continuous integration.
*Pair project — HAMLIL · SGHIOUAR IDRISSI.*

### Written entirely by me

The statistics and applied-maths practicals are solo work:
[MathStat2](Bachelor/L3/S5/MathStat2/) (simulation, bootstrap, maximum
likelihood, Fisher information, pivotal quantities),
[MathStat3](Bachelor/L3/S6/MathStat3/) (regression, ANOVA, non-parametric
tests), and [ComplementMath1](Bachelor/L3/S5/ComplementMath1/) (Fourier
analysis, signal processing, numerical ODE solvers).

---

## Repository map

| Domain | Courses | Key topics |
|---|---|---|
| **Machine learning** | [ComplementMath2](Bachelor/L3/S6/ComplementMath2/) | Classification, model comparison, ROC, feature engineering |
| **Statistics** | [MathStat2](Bachelor/L3/S5/MathStat2/), [MathStat3](Bachelor/L3/S6/MathStat3/) | Estimation, bootstrap, MLE, hypothesis testing, ANOVA |
| **Econometrics** | [Econometrie1](Bachelor/L3/S5/Econometrie1/) | Hedonic pricing, OLS diagnostics, panel data |
| **Applied maths** | [ComplementMath1](Bachelor/L3/S5/ComplementMath1/) | Fourier analysis, differential equations, Runge-Kutta |
| **Programming paradigms** | [Java](Bachelor/Java/), [Racket](Bachelor/SecondSemestreLanguage/DrRacket/), [Prolog](Bachelor/SecondSemestreLanguage/Prolog/), [SQL](Bachelor/SecondSemestreLanguage/SQL/) | Object-oriented, functional, logic, relational |
| **Web** | [WebDev](Bachelor/L3/S6/WebDev/) | HTML, CSS, JavaScript, Node.js, Express, SQLite |

**Master/** — [Master of Artificial Intelligence](https://m-ai.imag.fr/), M1 in
progress (semesters S7–S8); content will land here as it is produced.

---

## Stack

| | |
|---|---|
| **Languages** | R · Python · Java · JavaScript · Racket · Prolog · SQL |
| **Data science** | tidyverse · scikit-learn · statsmodels · Quarto · Jupyter |
| **Tools** | Git · LaTeX · Maven · GitHub Actions |

---

## Running the code

```sh
quarto preview path/to/notebook.qmd            # R / Quarto
javac -d bin $(find src -name '*.java') && java -cp bin package.Main
cd path/to/project && npm install && npm run dev
```

Each course directory has its own README with prerequisites and specifics.

---

## Licence and credits

Code and writing are MIT — see [LICENSE](LICENSE).

**[NOTICE](NOTICE) matters here.** MIT covers my own work only. Practical
subjects, lecture handouts, published papers and dataset documentation belong
to their authors, are not redistributed in this repository, and are credited
there and in each course README. NOTICE also records where my solutions are
substantially derived from a lecturer's own worked solutions rather than
independently written.
