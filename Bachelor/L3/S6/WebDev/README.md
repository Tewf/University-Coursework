# Introduction to Web Technologies (ITW)

> [Lire en francais](README.fr.md)

**Course:** ITW — Licence 3 MIASHS, Semester 6, Universite Grenoble Alpes
**Instructor:** Quentin Roy

A complete web development course progressing from HTML fundamentals to a full-stack Express.js application. All code files are **heavily commented in French** with simple analogies and common-mistake warnings.

## Learning Path

```
HTML (structure) -> CSS (style) -> JavaScript (logic) -> DOM (interactivity) -> Node.js (server)
```

## What You'll Learn

- Structure web pages with semantic HTML5
- Style with CSS3: selectors, flexbox, variables, responsive design
- Program in JavaScript: functions, objects, closures, callbacks
- Manipulate the DOM: selection, modification, events
- Build a pure Node.js HTTP server, then with Express.js
- Manage SQLite databases, password hashing, and sessions

## TP Overview

| TP | Topic | Key Concepts | Live Demo |
|----|-------|-------------|-----------|
| **TP0** | Setup | VS Code, Node.js, local server, terminal | — |
| **TP1** | HTML | Structure, tags, links, images, tables, SVG | [index](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/WebDev/TP1/index1.html), [cv](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/WebDev/TP1/cv1.html), [calendar](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/WebDev/TP1/calendar1.html) |
| **TP3** | CSS | Selectors, properties, flexbox, variables, hover, responsive | [gallery](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/WebDev/TP3/gallery.html), [cv](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/WebDev/TP3/cv.html) |
| **TP4** | CSS + Tables | Styling tables, 2 CSS files for 1 HTML | [shopping](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/WebDev/TP4/shopping.html) |
| **TP5** | JavaScript | Loops, objects, closures, callbacks, currying | — (console) |
| **TP6** | DOM | Selection, modification, events, forms | [calc](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/WebDev/TP6/calc.html), [degrees](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/WebDev/TP6/degrees.html), [hidden-number](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/WebDev/TP6/hidden-number.html) |
| **TP7** | Web App | Todo list, createElement, events, DOM manipulation | [todo](https://tewf.github.io/University-Coursework/Bachelor/L3/S6/WebDev/TP7/todo-list.html) |
| **TP8** | Node.js Server | HTTP, request/response, cookies, POST forms | — (server) |
| **TP9** | Full Express | Middleware, SQLite, hashing, sessions, authentication | — (server) |

> Note: TP2 does not exist in this course.

## How to Run

### TPs 0-7 (client-side HTML/CSS/JS)
Open `.html` files directly in your browser.

### TP8 (Node.js server)
```bash
cd TP8
npm start       # or npm run dev for auto-reload
# Then open http://localhost:8080
```

### TP9 (Express server)
```bash
cd TP9
npm install      # Install dependencies (first time)
npm run init-db  # Create the database (first time)
npm run dev      # Start the server
# Then open http://localhost:8080
```

## Skills Acquired

- **Frontend**: semantic HTML5, responsive CSS3, ES6+ JavaScript
- **Backend**: Node.js, Express.js, middleware, routing
- **Database**: SQLite, prepared statements
- **Security**: bcrypt hashing, session management
- **Architecture**: client/server separation, MVC, REST API

## Folder Structure

```
WebDev/
|-- README.md / README.fr.md
|-- Sources.md
|-- TP0/    <- Environment setup
|-- TP1/    <- HTML
|-- TP3/    <- CSS
|-- TP4/    <- CSS for tables
|-- TP5/    <- Core JavaScript
|-- TP6/    <- DOM manipulation
|-- TP7/    <- Todo List app
|-- TP8/    <- Pure Node.js server
|-- TP9/    <- Full Express server
```

## Technologies

| Technology | Used in | Description |
|------------|---------|-------------|
| **HTML5** | TP0-TP9 | Web page structure |
| **CSS3** | TP3-TP9 | Styling and design |
| **JavaScript** | TP5-TP9 | Logic and interactivity |
| **Node.js** | TP8-TP9 | Server-side JavaScript |
| **Express** | TP9 | Web server framework |
| **SQLite** | TP9 | Lightweight database |
| **SVG** | TP1, TP3 | Vector images |

## Resources

- [MDN Web Docs](https://developer.mozilla.org/) - Reference documentation
- [W3Schools](https://www.w3schools.com/) - Interactive tutorials
- [Original course subjects](https://miashs-www.univ-grenoble-alpes.fr/~royq/intro-web/tps/tp00/)
