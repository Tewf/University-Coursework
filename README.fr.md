# Travaux universitaires

[![CI](https://github.com/Tewf/University-Coursework/actions/workflows/ci.yml/badge.svg)](https://github.com/Tewf/University-Coursework/actions/workflows/ci.yml)

> [Read in English](README.md) · [Lire le rapport de machine learning en ligne ↗](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/)

Travaux de ma **Licence MIASHS** (Mathématiques et Informatique Appliquées aux
Sciences Humaines et Sociales) à l'**Université Grenoble Alpes**, poursuivis
aujourd'hui dans le [**Master of Artificial Intelligence**](https://m-ai.imag.fr/),
co-porté par l'**UFR IM²AG** et **Ensimag** (Grenoble INP).

Chaque projet est publié avec ses sources et son rendu : rien à cloner ni à
exécuter pour le lire.

---

## Projets

Chaque cours, et ce qu'il contient réellement. Chaque répertoire a son propre README.

### Apprentissage automatique et statistiques

| | |
|---|---|
| [**Satisfaction client — parfums**](Bachelor/L3/S6/ComplementMath2/Projet/) | Cinq classifieurs — régression logistique, arbre de décision, forêt aléatoire, kNN, naive Bayes — comparés sur ROC et matrices de confusion, avec séparation anti-fuite et modèles persistés. 8 `.qmd`, un site publié et un rapport rédigé. *Projet de groupe.* [Lire ↗](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/) |
| [**TP de classification**](Bachelor/L3/S6/ComplementMath2/TP/) | Huit TP corrigés sur les données Titanic : prétraitement, construction de variables, et les classifieurs ci-dessus appliqués tour à tour. 16 `.qmd`. |
| [**Estimation et tests**](Bachelor/L3/S5/MathStat2/) | Simulation et bootstrap, biais/variance/EQM des estimateurs, maximum de vraisemblance et information de Fisher, quantités pivotales et probabilité de couverture, tests du khi-deux. 6 `.qmd`. *Solo.* |
| [**Régression et ANOVA**](Bachelor/L3/S6/MathStat3/) | Tests de normalité et du khi-deux, régression linéaire, ANOVA à un facteur, tests non paramétriques, sur données réelles. 5 `.qmd`. *Solo.* |
| [**Analyse de Fourier et EDO**](Bachelor/L3/S5/ComplementMath1/) | Séries et transformée de Fourier, traitement du signal, et résolution numérique d'équations différentielles — Euler et Runge-Kutta. *Solo.* |

### Économie

| | |
|---|---|
| [**Prix de l'immobilier grenoblois**](Bachelor/L3/S5/Econometrie1/ProjetEconometrie/) | Modélisation hédonique sur les données ouvertes DVF : nettoyage, MCO avec diagnostics d'hétéroscédasticité et de multicolinéarité, puis une forêt aléatoire qui ramène le RMSE de 265 k€ à 59 k€. Avec une revue de littérature en LaTeX. *Projet de groupe.* |

### Programmation

| | |
|---|---|
| [**IA de bataille navale**](Bachelor/Java/Complement_IA-main/) | Moteur Java 17 avec bots de ciblage probabiliste (Markov, Monte-Carlo), protocole de tournoi produisant CSV et graphiques, interface Swing, Javadoc et intégration continue. 20 `.java`. *Projet en binôme.* |
| [**Programmation orientée objet**](Bachelor/Java/OOP/) | Le cours de Java lui-même — 59 fichiers source entre les TD et les travaux notés. |
| [**Programmation fonctionnelle**](Bachelor/SecondSemestreLanguage/DrRacket/) | 7 programmes Racket. |
| [**Programmation logique**](Bachelor/SecondSemestreLanguage/Prolog/) | 7 programmes Prolog. |
| [**Bases de données relationnelles**](Bachelor/SecondSemestreLanguage/SQL/) | 4 TP SQL avec leurs bases SQLite. |
| [**Web full-stack**](Bachelor/L3/S6/WebDev/) | TP0 à TP9, du HTML statique à une application Node.js/Express sur SQLite. |

## Carte du dépôt

| Domaine | Cours | Notions clés |
|---|---|---|
| **Apprentissage automatique** | [ComplementMath2](Bachelor/L3/S6/ComplementMath2/) | Classification, comparaison de modèles, ROC, feature engineering |
| **Statistiques** | [MathStat2](Bachelor/L3/S5/MathStat2/), [MathStat3](Bachelor/L3/S6/MathStat3/) | Estimation, bootstrap, MV, tests d'hypothèses, ANOVA |
| **Économétrie** | [Econometrie1](Bachelor/L3/S5/Econometrie1/) | Prix hédoniques, diagnostics MCO, données de panel |
| **Mathématiques appliquées** | [ComplementMath1](Bachelor/L3/S5/ComplementMath1/) | Analyse de Fourier, équations différentielles, Runge-Kutta |
| **Paradigmes de programmation** | [Java](Bachelor/Java/), [Racket](Bachelor/SecondSemestreLanguage/DrRacket/), [Prolog](Bachelor/SecondSemestreLanguage/Prolog/), [SQL](Bachelor/SecondSemestreLanguage/SQL/) | Objet, fonctionnel, logique, relationnel |
| **Web** | [WebDev](Bachelor/L3/S6/WebDev/) | HTML, CSS, JavaScript, Node.js, Express, SQLite |

**Master/** — [Master of Artificial Intelligence](https://m-ai.imag.fr/), M1 en
cours (semestres S7–S8) ; le contenu y sera ajouté au fil de sa production.

---

## Stack

| | |
|---|---|
| **Langages** | R · Python · Java · JavaScript · Racket · Prolog · SQL |
| **Science des données** | tidyverse · scikit-learn · statsmodels · Quarto · Jupyter |
| **Outils** | Git · LaTeX · Maven · GitHub Actions |

---

## Exécuter le code

```sh
quarto preview chemin/vers/notebook.qmd        # R / Quarto
javac -d bin $(find src -name '*.java') && java -cp bin package.Main
cd chemin/vers/projet && npm install && npm run dev
```

Chaque répertoire de cours a son propre README avec les prérequis et les
spécificités.

---

## Licence et crédits

Le code et les textes sont sous licence MIT — voir [LICENSE](LICENSE).

**[NOTICE](NOTICE) compte ici.** La licence MIT ne couvre que mon propre
travail. Les sujets de TP, polycopiés, articles publiés et documentations de
jeux de données appartiennent à leurs auteurs, ne sont pas redistribués dans ce
dépôt, et sont crédités dans NOTICE ainsi que dans chaque README de cours.
NOTICE précise également les cas où mes corrections sont largement dérivées des
corrigés de l'enseignante plutôt qu'écrites indépendamment.
