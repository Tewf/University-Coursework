// =============================================
// PAGE D'ACCUEIL - pages/index.js
// =============================================
//
// Cette fonction génère le HTML de la page d'accueil.
// Si un cookie "name" existe, elle affiche un message personnalisé.
// Sinon, elle affiche un message générique avec un lien vers le formulaire.


export function getAccueil(nom) {
  //
  // export = rend cette fonction accessible depuis d'autres fichiers
  //   (dans server.js, on fait : import { getAccueil } from "./pages/index.js")
  //
  // nom = la valeur du cookie "name" (peut être undefined si pas de cookie)

  // On construit le contenu qui change selon qu'on a un nom ou pas
  let contenuPersonnalise;

  if (nom) {
    // Si le cookie existe, on affiche un message personnalisé
    contenuPersonnalise = `
      <h2>Bonjour ${nom} !</h2>
      <p>Bienvenue sur votre page personnalisée.</p>
      <p>Le serveur vous a reconnu grâce au cookie "name" !</p>
    `;
    // Les backticks (`) permettent d'écrire du HTML sur plusieurs lignes
    // et d'insérer des variables avec ${...}
  } else {
    // Si pas de cookie, on propose de se présenter
    contenuPersonnalise = `
      <h2>Bienvenue, visiteur !</h2>
      <p>Je ne vous connais pas encore.</p>
      <p><a href="/who-are-you">Cliquez ici pour vous présenter</a></p>
    `;
  }

  // On retourne le HTML COMPLET de la page
  return `
    <!DOCTYPE html>
    <html lang="fr">
    <head>
      <meta charset="UTF-8">
      <title>Accueil - Mon Serveur</title>
      <style>
        body {
          font-family: "Gill Sans", sans-serif;
          max-width: 600px;
          margin: 40px auto;
          padding: 0 20px;
          background-color: #f8f9fa;
          color: #333;
        }
        h1 { color: #2c3e50; }
        h2 { color: #4a90d9; }
        a { color: #4a90d9; }
        a:hover { color: #357abd; }
        .info {
          background-color: #e3f2fd;
          padding: 15px;
          border-radius: 8px;
          border-left: 4px solid #4a90d9;
          margin: 20px 0;
        }
      </style>
    </head>
    <body>
      <h1>Mon Premier Serveur Web</h1>

      ${contenuPersonnalise}

      <div class="info">
        <p><strong>Comment ça marche ?</strong></p>
        <p>Cette page est générée par Node.js côté SERVEUR, pas côté client !</p>
        <p>Le HTML n'existe pas comme fichier : il est créé à la volée par du JavaScript sur le serveur.</p>
      </div>

      <nav>
        <p>
          <a href="/">Accueil</a> |
          <a href="/who-are-you">Se présenter</a>
        </p>
      </nav>

      <footer>
        <hr>
        <small>&copy; 2026 - TP8 Serveur Node.js</small>
      </footer>
    </body>
    </html>
  `;
}
