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

## Commencer ici

Si vous n'ouvrez qu'une seule chose, ouvrez la première.

### 🧪 [Prédiction de la satisfaction client — parfums](Bachelor/L3/S6/ComplementMath2/Projet/) · [lire le rapport ↗](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/ComplementMath2/Projet/rapport/)

Une chaîne complète d'apprentissage supervisé en R/Quarto : exploration →
préparation → **régression logistique, arbre de décision, forêt aléatoire, kNN
et naive Bayes**, comparés sur courbes ROC et matrices de confusion, avec une
séparation à l'épreuve des fuites de données, des modèles persistés et un
rapport rédigé. 1 398 lignes réparties sur 8 fichiers `.qmd`.
*Projet de groupe — HAMLIL · PARDO TERAN · EL KORAICHI · ANZID.*

### 📈 [Prix de l'immobilier grenoblois](https://github.com/Tewf/grenoble-housing-prices) *(dépôt dédié)*

Modélisation hédonique des prix sur les données ouvertes **DVF** : nettoyage,
régression MCO avec diagnostics d'hétéroscédasticité et de multicolinéarité,
puis une extension par forêt aléatoire qui ramène le RMSE de 265 k€ à 59 k€.
*Projet de groupe — HAMLIL · ANZID · EL KORAICHI.*

### 🎯 [IA de bataille navale](https://github.com/Tewf/Complement_IA) *(dépôt dédié)*

2 500 lignes de Java 17 modulaire : bots à **ciblage probabiliste par chaînes de
Markov et Monte-Carlo**, protocole de tournoi reproductible produisant CSV et
graphiques, interface Swing, Javadoc et intégration continue.
*Projet en binôme — HAMLIL · SGHIOUAR IDRISSI.*

### Travaux entièrement personnels

Les TP de statistiques et de mathématiques appliquées sont des travaux
individuels : [MathStat2](Bachelor/L3/S5/MathStat2/) (simulation, bootstrap,
maximum de vraisemblance, information de Fisher, quantités pivotales),
[MathStat3](Bachelor/L3/S6/MathStat3/) (régression, ANOVA, tests non
paramétriques) et [ComplementMath1](Bachelor/L3/S5/ComplementMath1/) (analyse de
Fourier, traitement du signal, résolution numérique d'équations différentielles).

---

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
