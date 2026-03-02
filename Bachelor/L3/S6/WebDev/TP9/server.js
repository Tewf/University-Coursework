// =============================================
// SERVEUR EXPRESS COMPLET - server.js
// =============================================
//
// Ce fichier est le CŒUR de notre application web.
// Il configure Express et met en place tous les middlewares et routes.
//
// Pour lancer :
//   npm install     (installe les dépendances la première fois)
//   npm run init-db (crée la base de données la première fois)
//   npm run dev     (lance le serveur en mode développement)


// ---- IMPORTS ----

import express from "express";
//
// Express = le framework qui simplifie la création de serveurs web.
// Au lieu de gérer chaque requête manuellement (comme en TP8),
// Express fournit des outils pour le routage, les middlewares, etc.

import cookieSession from "cookie-session";
//
// cookie-session = middleware pour gérer les SESSIONS.
// Une session = un espace de stockage temporaire associé à un utilisateur.
// Les données de session sont stockées dans un cookie chiffré.

import { open } from "sqlite";
import sqlite3 from "sqlite3";
//
// sqlite + sqlite3 = pour la base de données.
// sqlite = interface Promise (async/await)
// sqlite3 = le moteur de base de données

// Import des routes
import { getIndex } from "./routes/index.js";
import { postSignUp } from "./routes/sign-up.js";
import { postLogin } from "./routes/login.js";
import { postLogout } from "./routes/logout.js";


// ---- CRÉATION DE L'APPLICATION EXPRESS ----

const app = express();
//
// express() crée une APPLICATION Express.
// C'est l'objet central qui gère tout : routes, middlewares, etc.
//
// Analogie : c'est le CHEF D'ORCHESTRE de notre serveur.


// ---- MIDDLEWARE 1 : Logging (journalisation) ----

app.use((req, res, next) => {
  //
  // app.use() = ajoute un MIDDLEWARE à la chaîne.
  // Ce middleware s'exécute pour CHAQUE requête, quelle que soit l'URL.
  //
  // req = request (la requête du client)
  // res = response (la réponse qu'on va envoyer)
  // next = la fonction pour passer au middleware SUIVANT
  //
  // IMPORTANT : si on n'appelle pas next(), la requête reste BLOQUÉE ici !

  console.log(`${req.method} ${req.url}`);
  // Affiche chaque requête dans le terminal :
  // GET /
  // POST /sign-up
  // GET /shared.css

  next();
  // Passe au middleware suivant dans la chaîne
});


// ---- MIDDLEWARE 2 : Session ----

app.use(cookieSession({
  name: "session",
  // Nom du cookie de session

  keys: ["cle-secrete-tp9-2026"],
  //
  // Clé de CHIFFREMENT du cookie.
  // Le cookie de session est CHIFFRÉ pour que le client
  // ne puisse pas lire ou modifier son contenu.
  //
  // En production, cette clé doit être :
  // 1. Longue et aléatoire
  // 2. Stockée dans une variable d'environnement (pas dans le code !)
  // 3. Différente pour chaque serveur

  maxAge: 24 * 60 * 60 * 1000,
  // Durée de vie : 24 heures (en millisecondes)
  // 24 heures × 60 minutes × 60 secondes × 1000 millisecondes
}));


// ---- MIDDLEWARE 3 : Parser le corps des requêtes ----

app.use(express.json());
//
// Permet de lire les corps de requête au format JSON.
// Quand le client envoie { "username": "jean", "password": "123" },
// express.json() le transforme en objet JavaScript accessible via req.body

app.use(express.urlencoded({ extended: true }));
//
// Permet de lire les données de formulaires HTML classiques.
// Quand un formulaire HTML est soumis, les données arrivent encodées :
// "username=jean&password=123"
// urlencoded les transforme en objet : { username: "jean", password: "123" }


// ---- MIDDLEWARE 4 : Fichiers statiques ----

app.use(express.static("public", { extensions: ["html"] }));
//
// express.static("public")
//   = sert les fichiers du dossier "public" tels quels.
//
//   Le client demande /shared.css → le serveur envoie public/shared.css
//   Le client demande /sign-up    → le serveur envoie public/sign-up.html
//
// { extensions: ["html"] }
//   = si l'URL n'a pas d'extension, essaie d'ajouter ".html"
//   /sign-up → cherche public/sign-up.html
//
// C'est comme un self-service : le client se sert directement
// sans passer par le serveur (pas de code JS exécuté).


// ---- MIDDLEWARE 5 : Connexion à la base de données ----

app.use(async (req, res, next) => {
  //
  // Ce middleware ouvre la base de données et la rend disponible
  // dans req.db pour tous les middlewares et routes suivants.

  req.db = await open({
    filename: "./database.sqlite",
    driver: sqlite3.Database,
  });
  //
  // open() ouvre (ou crée) la base de données SQLite.
  // await = attend que la connexion soit établie avant de continuer.
  //
  // req.db = la connexion est attachée à la requête.
  // Comme ça, chaque route peut faire req.db.get(...) ou req.db.run(...)

  next();
});


// ---- MIDDLEWARE 6 : Charger l'utilisateur connecté ----

app.use(async (req, res, next) => {
  //
  // Si un utilisateur est connecté (session avec username),
  // on charge ses infos depuis la base de données.

  if (req.session.username) {
    // La session contient un username → l'utilisateur est connecté

    const user = await req.db.get(
      "SELECT username, name FROM users WHERE username = ?",
      req.session.username
    );
    //
    // req.db.get() = exécute une requête SQL et retourne UNE ligne
    //
    // "SELECT username, name FROM users WHERE username = ?"
    //   = "Sélectionne le username et le name de la table users
    //      où le username correspond"
    //
    // Le ? est un PARAMÈTRE. La valeur réelle (req.session.username)
    // est passée séparément pour éviter les INJECTIONS SQL.
    //
    // ⚠️ SÉCURITÉ : TOUJOURS utiliser ? au lieu de concaténer :
    // ❌ `WHERE username = '${username}'`  → INJECTION SQL possible !
    // ✅ `WHERE username = ?`, username    → SÉCURISÉ

    req.user = user || null;
    // Si l'utilisateur existe → on le stocke dans req.user
    // Si non (compte supprimé ?) → null
  } else {
    req.user = null;
    // Pas de session → pas d'utilisateur connecté
  }

  next();
});


// ---- ROUTES ----

// Page d'accueil
app.get("/", getIndex);
//
// app.get("/", handler)
//   = quand quelqu'un fait une requête GET sur "/", exécute handler
//
// C'est comme dire :
// "Si le client demande la page d'accueil, appelle la fonction getIndex"

// Inscription
app.post("/sign-up", postSignUp);
//
// app.post("/sign-up", handler)
//   = quand un formulaire est soumis en POST vers "/sign-up"

// Connexion
app.post("/login", postLogin);

// Déconnexion
app.post("/logout", postLogout);


// ---- DÉMARRAGE DU SERVEUR ----

const PORT = 8080;

app.listen(PORT, () => {
  console.log(`Serveur Express démarré sur http://localhost:${PORT}`);
  console.log("Appuyez sur Ctrl+C pour arrêter");
});
