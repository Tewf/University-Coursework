# Travaux universitaires

[![CI](https://github.com/Tewf/University-Coursework/actions/workflows/ci.yml/badge.svg)](https://github.com/Tewf/University-Coursework/actions/workflows/ci.yml)

> [Read in English](README.md)

Tout mon parcours académique à l'**Université Grenoble Alpes** : la
[Licence MIASHS](https://formations.univ-grenoble-alpes.fr/fr/catalogue-2021/licence-XA/licence-mathematiques-et-informatique-appliquees-aux-sciences-humaines-et-sociales-miashs-IDIVNLE7/parcours-mathematiques-informatique-et-sciences-economiques-2e-et-3e-annee-IGRNO2YS.html)
dans [`Bachelor/`](Bachelor/), et le
[Master of Artificial Intelligence](https://m-ai.imag.fr/) dans
[`Master/`](Master/) au fil de sa production.

Les sources sont à côté de leur rendu : rien à cloner pour lire.
Le M1 est en cours et [`Master/`](Master/) se remplit au fil de l'année.

**[Parcourir le site ↗](https://tewf.github.io/University-Coursework/)**, où les résultats
sont tracés depuis les fichiers qui les ont produits et où l'on peut regarder le bot de
bataille navale jouer une partie enregistrée.

## Projets

Des travaux notés, menés de bout en bout, avec un résultat mesuré.

**[Satisfaction client pour des parfums](Bachelor/L3/S6/ComplementMath2/Projet/)** (R, Quarto).
Classification binaire sur environ 24 000 parfums. Régression logistique LASSO, arbre
de décision élagué, forêt aléatoire et k plus proches voisins comparés sur courbes ROC
et matrices de confusion ; Naive Bayes et K-means ont été essayés puis écartés, avec
justification. Les variables sont ramenées à 10 familles olfactives et la séparation
70/30 est construite contre les fuites de données.
[Lire le rapport ↗](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/),
24 pages, également servi en livre HTML navigable. *Projet de groupe.*

**[Prix de l'immobilier grenoblois](Bachelor/L3/S5/Econometrie1/ProjetEconometrie/)** (R, Python).
Prix hédoniques sur les données ouvertes DVF. C'est la transformation logarithmique qui
fait fonctionner le modèle linéaire : le R² passe de 0,096 à 0,275. Une forêt aléatoire
ramène ensuite le RMSE de 265 214 € à 58 750 €, environ 4,5 fois mieux, en abandonnant
précisément les prix implicites interprétables qui sont l'objet de la démarche hédonique.
Le rapport soutient que les deux modèles répondent à des questions différentes.
*Projet de groupe.*

**[IA de bataille navale](Bachelor/Java/BattleshipAI/)** (Java).
Quatre stratégies de ciblage confrontées sur 300 parties chacune. Les matrices de
transition de Markov gagnent **74,3 %** des parties et vident la grille en 54,8 tirs,
contre 94,3 pour le tir aléatoire, soit 42 % de moins. Monte-Carlo coûte bien plus de
calcul pour un résultat légèrement inférieur, et c'est là que c'est intéressant.
*Projet en binôme.*

**[Tournoi de stratégies](Bachelor/SecondSemestreLanguage/Prolog/StrategyTournament/)** (Prolog).
Deux stratégies déterminées sur le papier, écrites comme agents, puis engagées face à
treize agents d'autres étudiants. Elles finissent 7e et 8e sur 16. Relire le journal de
636 pages match par match montre que le classement mesure autre chose que le fait de
gagner : le vainqueur a gagné **6 de ses 15 matchs**, l'agent qui en a gagné 13 finit 14e,
et les deux agents engagés battent le vainqueur en tête-à-tête. Sur l'ensemble, finir plus
bas est corrélé au fait de gagner plus de matchs. Revérifier l'équilibre qui les
sous-tend montre que la distribution de Nash **domine strictement** celle qui a été
soumise : elle rapporte davantage face à chaque adversaire, d'au moins 0,1402, tout
en perdant le tête-à-tête. *Projet en binôme.*

**[Application web full-stack](Bachelor/L3/S6/WebDev/)** (Node.js, Express, SQLite).
Neuf TP menant à un serveur complet : middleware, persistance SQLite, hachage des mots
de passe, sessions et authentification. *Solo.*

## Compétences, et où elles servent

| | |
|---|---|
| **R** | tidyverse, caret, glmnet, ranger, rpart, pROC, deSolve. [Apprentissage automatique](Bachelor/L3/S6/ComplementMath2/), [économétrie](Bachelor/L3/S5/Econometrie1/), [statistiques](Bachelor/L3/S6/MathStat3/), [analyse](Bachelor/L3/S5/ComplementMath1/) |
| **Java** | Conception objet, modules, interface graphique, tournois sous CI. [IA de bataille navale](Bachelor/Java/BattleshipAI/), [le cours de POO](Bachelor/Java/OOP/) |
| **JavaScript** | Node.js, Express, SQLite, sessions et authentification. [Web](Bachelor/L3/S6/WebDev/) |
| **SQL, Prolog, Racket** | Paradigmes relationnel, logique et fonctionnel. [Modules de langages](Bachelor/SecondSemestreLanguage/), [le tournoi Prolog](Bachelor/SecondSemestreLanguage/Prolog/StrategyTournament/) |
| **Rédaction** | Quarto, R Markdown, LaTeX. Chaque rapport ici est rendu depuis sa source |

## Le reste des travaux

Cursus complet, semestre par semestre, dans [`Bachelor/`](Bachelor/README.fr.md).

| Matière | | |
|---|---|---|
| Statistiques | [Estimation et tests](Bachelor/L3/S5/MathStat2/) | Bootstrap, maximum de vraisemblance, information de Fisher, khi-deux. *Solo.* |
| Statistiques | [Régression et ANOVA](Bachelor/L3/S6/MathStat3/) | Régression linéaire, ANOVA à un facteur, tests non paramétriques. *Solo.* |
| Analyse | [Fourier et EDO](Bachelor/L3/S5/ComplementMath1/) | Séries et transformée de Fourier, solveurs d'Euler et Runge-Kutta. *Solo.* |
| Apprentissage | [TP de classification](Bachelor/L3/S6/ComplementMath2/TP/) | Huit TP corrigés sur les données Titanic. |
| Économie | [Économétrie avancée](Bachelor/L3/S6/Econometrie2/) | Fait suite à l'étude des prix de l'immobilier ci-dessus. |
| Programmation | [Programmation orientée objet](Bachelor/Java/OOP/) | Le cours de Java, 59 fichiers source. |
| Programmation | [Fonctionnel](Bachelor/SecondSemestreLanguage/DrRacket/) · [Logique](Bachelor/SecondSemestreLanguage/Prolog/) · [Relationnel](Bachelor/SecondSemestreLanguage/SQL/) | TP Racket, Prolog et SQL. |

## Licence et crédits

Le code et les textes sont sous licence MIT ; voir [LICENSE](LICENSE).
**[NOTICE](NOTICE) compte ici** : la licence MIT ne couvre que mon propre
travail. Les sujets de TP, polycopiés et articles publiés appartiennent à leurs
auteurs et sont cités, non redistribués.
