// =============================================
// SERVEUR WEB NODE.JS (sans framework)
// =============================================
//
// Ce fichier crée un serveur HTTP minimal.
// Pas d'Express, pas de framework : juste Node.js pur !
//
// Pour lancer : npm start (ou npm run dev pour le mode auto-reload)
// Puis ouvre http://localhost:8080 dans ton navigateur.


// ---- IMPORT DU MODULE HTTP ----
import http from "node:http";
//
// "http" est un MODULE intégré à Node.js (pas besoin de npm install).
// Un module = un fichier/paquet qui fournit des fonctionnalités.
//
// import ... from "node:..." = syntaxe ES modules (moderne)
// Le préfixe "node:" indique que c'est un module intégré à Node.js.
//
// Ce module contient tout ce qu'il faut pour créer un serveur HTTP.


// ---- IMPORT DES PAGES ----
import { getAccueil } from "./pages/index.js";
import { get404 } from "./pages/404.js";
import { getFormulaire, traiterFormulaire } from "./pages/who-are-you.js";
//
// On importe les fonctions qui génèrent le HTML de chaque page.
// Chaque page est dans son propre fichier = meilleure organisation.


// ---- FONCTION UTILITAIRE : Lire le corps d'une requête ----
function readableToString(readable) {
  //
  // Quand le client envoie des données (formulaire POST),
  // les données arrivent en MORCEAUX (chunks), pas d'un coup.
  //
  // C'est comme recevoir un long message lettre par lettre.
  // Cette fonction rassemble toutes les lettres en un message complet.
  //
  // Elle retourne une PROMISE :
  // = une "promesse" de résultat futur
  // = "je te donnerai le résultat quand j'aurai fini de tout lire"

  return new Promise((resolve, reject) => {
    let data = "";
    // On accumule les morceaux ici

    readable.on("data", (chunk) => {
      // "data" = événement déclenché pour chaque MORCEAU reçu
      data += chunk;
      // On ajoute le morceau au texte complet
    });

    readable.on("end", () => {
      // "end" = événement déclenché quand TOUT est reçu
      resolve(data);
      // resolve = "la promesse est tenue, voici le résultat"
    });

    readable.on("error", (err) => {
      // "error" = si quelque chose se passe mal
      reject(err);
      // reject = "la promesse est rompue, voici l'erreur"
    });
  });
}


// ---- FONCTION POUR LIRE LES COOKIES ----
function parseCookies(cookieHeader) {
  //
  // Les cookies arrivent dans le header de la requête sous forme de texte :
  // "nom=Mohamed; age=22; ville=Grenoble"
  //
  // On doit les transformer en objet JavaScript :
  // { nom: "Mohamed", age: "22", ville: "Grenoble" }

  const cookies = {};

  if (!cookieHeader) {
    // S'il n'y a pas de cookies, on retourne un objet vide
    return cookies;
  }

  cookieHeader.split(";").forEach((cookie) => {
    // .split(";") découpe la chaîne aux points-virgules
    // ["nom=Mohamed", " age=22", " ville=Grenoble"]

    const [cle, ...reste] = cookie.trim().split("=");
    // .trim() enlève les espaces
    // .split("=") sépare la clé de la valeur
    // [cle, ...reste] : destructuring
    //   cle = "nom"
    //   reste = ["Mohamed"] (un tableau, au cas où la valeur contient "=")

    cookies[cle] = reste.join("=");
    // On recolle la valeur (au cas où elle contenait des "=")
  });

  return cookies;
}


// ---- CRÉATION DU SERVEUR ----
const server = http.createServer(async (request, response) => {
  //
  // http.createServer(callback)
  //   = crée un serveur HTTP
  //   Le callback est appelé pour CHAQUE requête reçue
  //
  // request = la requête du client (ce qu'il demande)
  //   - request.method = "GET" ou "POST"
  //   - request.url = l'URL demandée ("/", "/cv.html", etc.)
  //   - request.headers = les en-têtes (dont les cookies)
  //
  // response = la réponse qu'on va envoyer au client
  //   - response.writeHead(code, headers) = définit le statut et les en-têtes
  //   - response.end(contenu) = envoie le contenu et termine la réponse
  //
  // async = cette fonction peut utiliser "await" (attendre des résultats)

  // ---- LOG DE CHAQUE REQUÊTE ----
  console.log(`${request.method} ${request.url}`);
  //
  // Affiche dans le terminal chaque requête reçue :
  // GET /
  // GET /who-are-you
  // POST /who-are-you
  // GET /page-inexistante

  // ---- LIRE LES COOKIES ----
  const cookies = parseCookies(request.headers.cookie);
  // request.headers.cookie = la chaîne de cookies envoyée par le navigateur

  // ---- ROUTAGE ----
  //
  // Le ROUTAGE = diriger la requête vers la bonne page
  // selon l'URL et la méthode HTTP.
  //
  // C'est comme un standard téléphonique :
  // "Tapez 1 pour l'accueil, 2 pour le CV..."

  if (request.method === "GET" && request.url === "/") {
    // ---- PAGE D'ACCUEIL ----
    const html = getAccueil(cookies.name);
    // On passe le nom du cookie à la page d'accueil
    // Si le cookie n'existe pas, cookies.name sera undefined

    response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
    //
    // writeHead(codeStatut, en-têtes)
    //
    // 200 = "OK, tout va bien"
    //
    // "Content-Type": "text/html; charset=utf-8"
    //   = "Le contenu est du HTML en UTF-8"
    //   C'est comme dire au serveur du restaurant :
    //   "Je vous apporte une pizza" (pas une salade)
    //   Le navigateur sait comment l'afficher grâce à cette info.

    response.end(html);
    // Envoie le HTML au client et TERMINE la réponse

  } else if (request.method === "GET" && request.url === "/who-are-you") {
    // ---- FORMULAIRE (page GET) ----
    const html = getFormulaire();
    response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
    response.end(html);

  } else if (request.method === "POST" && request.url === "/who-are-you") {
    // ---- TRAITEMENT DU FORMULAIRE (POST) ----
    //
    // Quand l'utilisateur soumet le formulaire,
    // le navigateur envoie une requête POST avec les données.

    const body = await readableToString(request);
    // Lire le corps de la requête (les données du formulaire)
    // await = "attends que la lecture soit terminée"

    const params = new URLSearchParams(body);
    //
    // URLSearchParams parse les données du formulaire.
    // Le corps ressemble à : "name=Mohamed"
    // URLSearchParams le transforme en objet interrogeable.

    const nom = params.get("name");
    // Récupère la valeur du champ "name"

    // ---- CRÉER UN COOKIE ----
    response.writeHead(303, {
      // 303 = "See Other" = REDIRECTION
      // Le navigateur va automatiquement aller à l'URL indiquée par Location

      "Location": "/",
      // Redirige vers la page d'accueil

      "Set-Cookie": `name=${nom}; HttpOnly; Path=/`,
      //
      // Set-Cookie = créer un cookie
      //
      // name=${nom} : le cookie s'appelle "name" et contient le nom saisi
      //
      // HttpOnly : le cookie n'est PAS accessible en JavaScript côté client
      //   (document.cookie ne le verra pas)
      //   C'est une PROTECTION de sécurité : un script malveillant
      //   ne peut pas voler ce cookie
      //
      // Path=/ : le cookie est envoyé pour TOUTES les pages du site
    });

    response.end();
    // Pas de contenu car on redirige

  } else {
    // ---- PAGE 404 (non trouvée) ----
    //
    // Si aucune des conditions ci-dessus ne correspond,
    // c'est que la page demandée n'existe pas !

    const html = get404(request.url);
    response.writeHead(404, { "Content-Type": "text/html; charset=utf-8" });
    // 404 = "Not Found" = "Cette page n'existe pas"
    response.end(html);
  }
});


// ---- DÉMARRER LE SERVEUR ----
const PORT = 8080;

server.listen(PORT, () => {
  //
  // server.listen(port, callback)
  //   = démarre le serveur et écoute sur le port indiqué
  //   Le callback est appelé quand le serveur est prêt
  //
  // Le serveur est maintenant en ÉCOUTE permanente.
  // Il attend des requêtes et les traite une par une.

  console.log(`Serveur démarré sur http://localhost:${PORT}`);
  console.log("Appuyez sur Ctrl+C pour arrêter");
});
