# University Coursework

[![CI](https://github.com/Tewf/University-Coursework/actions/workflows/ci.yml/badge.svg)](https://github.com/Tewf/University-Coursework/actions/workflows/ci.yml)

> [Lire en français](README.fr.md)

My whole academic path at **Université Grenoble Alpes**: the
[Licence MIASHS](https://formations.univ-grenoble-alpes.fr/fr/catalogue-2021/licence-XA/licence-mathematiques-et-informatique-appliquees-aux-sciences-humaines-et-sociales-miashs-IDIVNLE7/parcours-mathematiques-informatique-et-sciences-economiques-2e-et-3e-annee-IGRNO2YS.html)
in [`Bachelor/`](Bachelor/), and the
[Master of Artificial Intelligence](https://m-ai.imag.fr/) in [`Master/`](Master/)
as it is produced.

Source sits next to its rendered output, so everything reads without cloning.
The M1 is under way and [`Master/`](Master/) fills as it goes.

**[Browse it as a site ↗](https://tewf.github.io/University-Coursework/)**, where the
results are charted from the files that produced them and the Battleship bot can be
watched playing a recorded game.

## Projects

Graded work that runs end to end and reports a measured result.

**[Perfume satisfaction](Bachelor/L3/S6/ComplementMath2/Projet/)** (R, Quarto).
Binary classification over roughly 24 000 fragrances. LASSO logistic regression, a
pruned decision tree, a random forest and kNN compared on ROC curves and confusion
matrices; Naive Bayes and K-means were tried and rejected on stated grounds. Features
map to 10 olfactory families and the 70/30 split is built against leakage.
[Read the report ↗](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/),
24 pages, also served as a navigable HTML book. *Group project.*

**[Grenoble housing prices](Bachelor/L3/S5/Econometrie1/ProjetEconometrie/)** (R, Python).
Hedonic pricing on DVF open data. The log transform is what makes the linear model
work, lifting R² from 0.096 to 0.275. A random forest then cuts RMSE from €265,214 to
€58,750, about 4.5 times better, by giving up exactly the interpretable implicit prices
the hedonic method exists to produce. The write-up argues the two models answer
different questions. *Group project.*

**[Battleship AI](Bachelor/Java/BattleshipAI/)** (Java).
Four targeting strategies benchmarked head to head over 300 games each. Markov
transition matrices win **74.3%** of games and clear the board in 54.8 shots against
94.3 for uniform random, a 42% reduction. Monte Carlo costs far more computation for a
slightly worse result, which is the interesting part. *Pair project.*

**[Full-stack web application](Bachelor/L3/S6/WebDev/)** (Node.js, Express, SQLite).
Nine practicals building up to a complete server: middleware, SQLite persistence,
password hashing, sessions and authentication. *Solo.*

## Skills, and where they are used

| | |
|---|---|
| **R** | tidyverse, caret, glmnet, ranger, rpart, pROC, deSolve. [Machine learning](Bachelor/L3/S6/ComplementMath2/), [econometrics](Bachelor/L3/S5/Econometrie1/), [statistics](Bachelor/L3/S6/MathStat3/), [analysis](Bachelor/L3/S5/ComplementMath1/) |
| **Java** | Object-oriented design, modules, GUI, tournaments under CI. [Battleship AI](Bachelor/Java/BattleshipAI/), [the OOP course](Bachelor/Java/OOP/) |
| **JavaScript** | Node.js, Express, SQLite, sessions and authentication. [Web](Bachelor/L3/S6/WebDev/) |
| **SQL, Prolog, Racket** | Relational, logic and functional paradigms. [Language modules](Bachelor/SecondSemestreLanguage/) |
| **Reporting** | Quarto, R Markdown, LaTeX. Every report here renders from its source |

## The rest of the coursework

Full curriculum, semester by semester, in [`Bachelor/`](Bachelor/README.md).

| Subject | | |
|---|---|---|
| Statistics | [Estimation and testing](Bachelor/L3/S5/MathStat2/) | Bootstrap, maximum likelihood, Fisher information, chi-squared. *Solo.* |
| Statistics | [Regression and ANOVA](Bachelor/L3/S6/MathStat3/) | Linear regression, one-factor ANOVA, non-parametric tests. *Solo.* |
| Analysis | [Fourier and ODEs](Bachelor/L3/S5/ComplementMath1/) | Fourier series and transform, Euler and Runge-Kutta solvers. *Solo.* |
| ML | [Classification practicals](Bachelor/L3/S6/ComplementMath2/TP/) | Eight worked practicals on the Titanic data. |
| Economics | [Advanced econometrics](Bachelor/L3/S6/Econometrie2/) | Follows on from the housing-price study above. |
| Programming | [Object-oriented programming](Bachelor/Java/OOP/) | The Java course, 59 source files. |
| Programming | [Functional](Bachelor/SecondSemestreLanguage/DrRacket/) · [Logic](Bachelor/SecondSemestreLanguage/Prolog/) · [Relational](Bachelor/SecondSemestreLanguage/SQL/) | Racket, Prolog and SQL practicals. |

## Licence and credits

Code and writing are MIT; see [LICENSE](LICENSE). **[NOTICE](NOTICE) matters
here**: MIT covers my own work only. Practical subjects, handouts and published
papers belong to their authors and are cited rather than redistributed.
