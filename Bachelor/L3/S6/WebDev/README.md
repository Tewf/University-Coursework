# Introduction aux Technologies du Web (ITW)

## Licence 3 MIASHS - Semestre 6 - Universit Grenoble Alpes

Ce dossier contient l'ensemble des Travaux Pratiques du cours d'Introduction aux Technologies du Web, dispens par Quentin Roy.

---

## Parcours d'apprentissage

Le cours suit une progression logique, du plus simple au plus complexe :

```
HTML (structure) -> CSS (style) -> JavaScript (logique) -> DOM (interactivit) -> Node.js (serveur)
```

---

## Vue d'ensemble des TPs

| TP | Theme | Ce qu'on apprend | Fichiers cles |
|----|-------|------------------|---------------|
| **TP0** | Mise en place | VS Code, Node.js, serveur local, terminal | `test-protocol.html` |
| **TP1** | HTML | Structure, balises, liens, images, tableaux, SVG | `index1.html`, `cv1.html`, `calendar1.html` |
| **TP3** | CSS | Selecteurs, proprietes, flexbox, variables, hover, responsive | `shared.css`, `menu.css`, `gallery.html` |
| **TP4** | CSS + Tableaux | Styliser des tableaux, 2 CSS pour 1 HTML | `shopping.html`, `styles-a.css`, `styles-b.css` |
| **TP5** | JavaScript | Boucles, objets, closures, callbacks, currying | `exercices.js` (8 exercices) |
| **TP6** | DOM | Selection, modification, evenements, formulaires | `calc.html`, `degrees.html`, `hidden-number.html` |
| **TP7** | Application web | Todo list, createElement, evenements, manipulation DOM | `todo-list.js` |
| **TP8** | Serveur Node.js | HTTP, requetes/reponses, cookies, formulaires POST | `server.js`, `pages/` |
| **TP9** | Express complet | Middleware, SQLite, hashage, sessions, authentification | `server.js`, `routes/`, `lib/` |

> Note : Le TP2 n'existe pas dans le programme du cours.

---

## Structure du dossier

```
WebDev/
|-- README.md              <- Ce fichier
|-- Sources.md             <- Liens vers les sujets originaux
|-- test/                  <- Fichiers de test initiaux
|-- TP0/                   <- Setup de l'environnement
|-- TP1/                   <- HTML (structure et semantique)
|-- TP3/                   <- CSS (mise en forme)
|   |-- shared/shared.css  <- Variables et styles communs
|   |-- menu.css           <- Barre de navigation
|   |-- *.html             <- Pages stylisees
|-- TP4/                   <- CSS pour tableaux
|-- TP5/                   <- JavaScript fondamental
|-- TP6/                   <- Manipulation du DOM
|-- TP7/                   <- Application Todo List
|-- TP8/                   <- Serveur Node.js pur
|   |-- server.js
|   |-- pages/
|-- TP9/                   <- Serveur Express complet
    |-- server.js
    |-- routes/
    |-- lib/
    |-- scripts/
    |-- public/
```

---

## Comment utiliser ces TPs

### TPs 0 a 7 (HTML/CSS/JS cote client)
Ouvre les fichiers `.html` directement dans ton navigateur (double-clic ou glisser-deposer).

### TP8 (serveur Node.js)
```bash
cd TP8
npm start       # ou npm run dev pour le mode auto-reload
# Puis ouvre http://localhost:8080
```

### TP9 (serveur Express)
```bash
cd TP9
npm install      # Installe les dependances (premiere fois)
npm run init-db  # Cree la base de donnees (premiere fois)
npm run dev      # Lance le serveur
# Puis ouvre http://localhost:8080
```

---

## Approche pedagogique

Chaque fichier de code est **richement commente** en francais, avec :
- Des explications de chaque concept comme si c'etait la premiere fois
- Des analogies simples (restaurant, cuisine, sac a dos, etc.)
- Des avertissements sur les erreurs courantes
- Des resumes en fin de fichier

---

## Technologies utilisees

| Technologie | Utilisee dans | Description |
|-------------|---------------|-------------|
| **HTML5** | TP0-TP9 | Structure des pages web |
| **CSS3** | TP3-TP9 | Mise en forme et design |
| **JavaScript** | TP5-TP9 | Logique et interactivite |
| **Node.js** | TP8-TP9 | JavaScript cote serveur |
| **Express** | TP9 | Framework serveur web |
| **SQLite** | TP9 | Base de donnees legere |
| **SVG** | TP1, TP3 | Images vectorielles |

---

## Ressources

- [MDN Web Docs](https://developer.mozilla.org/fr/) - Documentation de reference
- [W3Schools](https://www.w3schools.com/) - Tutoriels interactifs
- [Sujets originaux du cours](https://miashs-www.univ-grenoble-alpes.fr/~royq/intro-web/tps/tp00/)
