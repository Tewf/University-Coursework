# Introduction aux Technologies du Web (ITW)

> [Read in English](README.md)

**Cours :** ITW — Licence 3 MIASHS, Semestre 6, Universite Grenoble Alpes
**Enseignant :** Quentin Roy

Ce dossier contient l'ensemble des Travaux Pratiques du cours d'Introduction aux Technologies du Web. Le code est **richement commente en francais** avec des analogies simples et des avertissements sur les erreurs courantes.

## Parcours d'apprentissage

```
HTML (structure) -> CSS (style) -> JavaScript (logique) -> DOM (interactivite) -> Node.js (serveur)
```

## Ce que vous apprendrez

- Structurer des pages web avec HTML5 semantique
- Styliser avec CSS3 : selecteurs, flexbox, variables, responsive design
- Programmer en JavaScript : fonctions, objets, closures, callbacks
- Manipuler le DOM : selection, modification, evenements
- Construire un serveur Node.js pur, puis avec Express.js
- Gerer une base SQLite, le hashage de mots de passe et les sessions

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

## Comment utiliser ces TPs

### TPs 0 a 7 (HTML/CSS/JS cote client)
Ouvrir les fichiers `.html` directement dans le navigateur.

### TP8 (serveur Node.js)
```bash
cd TP8
npm start       # ou npm run dev pour le mode auto-reload
# Puis ouvrir http://localhost:8080
```

### TP9 (serveur Express)
```bash
cd TP9
npm install      # Installer les dependances (premiere fois)
npm run init-db  # Creer la base de donnees (premiere fois)
npm run dev      # Lancer le serveur
# Puis ouvrir http://localhost:8080
```

## Competences acquises

- **Frontend** : HTML5 semantique, CSS3 responsive, JavaScript ES6+
- **Backend** : Node.js, Express.js, middleware, routage
- **Base de donnees** : SQLite, requetes preparees
- **Securite** : hashage bcrypt, gestion de sessions
- **Architecture** : separation client/serveur, MVC, API REST

## Structure du dossier

```
WebDev/
|-- README.md / README.fr.md
|-- Sources.md
|-- TP0/    <- Setup de l'environnement
|-- TP1/    <- HTML
|-- TP3/    <- CSS
|-- TP4/    <- CSS pour tableaux
|-- TP5/    <- JavaScript fondamental
|-- TP6/    <- Manipulation du DOM
|-- TP7/    <- Application Todo List
|-- TP8/    <- Serveur Node.js pur
|-- TP9/    <- Serveur Express complet
```

## Technologies

| Technologie | Utilisee dans | Description |
|-------------|---------------|-------------|
| **HTML5** | TP0-TP9 | Structure des pages web |
| **CSS3** | TP3-TP9 | Mise en forme et design |
| **JavaScript** | TP5-TP9 | Logique et interactivite |
| **Node.js** | TP8-TP9 | JavaScript cote serveur |
| **Express** | TP9 | Framework serveur web |
| **SQLite** | TP9 | Base de donnees legere |
| **SVG** | TP1, TP3 | Images vectorielles |

## Ressources

- [MDN Web Docs](https://developer.mozilla.org/fr/) - Documentation de reference
- [W3Schools](https://www.w3schools.com/) - Tutoriels interactifs
- [Sujets originaux du cours](https://miashs-www.univ-grenoble-alpes.fr/~royq/intro-web/tps/tp00/)
