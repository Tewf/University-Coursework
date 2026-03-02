// =============================================
// PAGE 404 - pages/404.js
// =============================================
//
// Cette page s'affiche quand l'URL demandée n'existe pas.
// 404 = "Not Found" = "Non trouvé"
//
// C'est comme aller au restaurant et commander
// un plat qui n'est pas au menu !


export function get404(url) {
  //
  // url = l'URL que l'utilisateur a essayé d'atteindre
  // On l'affiche pour qu'il comprenne son erreur

  return `
    <!DOCTYPE html>
    <html lang="fr">
    <head>
      <meta charset="UTF-8">
      <title>404 - Page non trouvée</title>
      <style>
        body {
          font-family: "Gill Sans", sans-serif;
          max-width: 600px;
          margin: 40px auto;
          padding: 0 20px;
          text-align: center;
          background-color: #f8f9fa;
          color: #333;
        }
        .erreur-404 {
          font-size: 120px;
          color: #e74c3c;
          margin: 0;
          line-height: 1;
        }
        h1 { color: #e74c3c; }
        .url-demandee {
          background-color: #fff3cd;
          padding: 10px;
          border-radius: 8px;
          font-family: monospace;
          margin: 20px 0;
        }
        a { color: #4a90d9; }
      </style>
    </head>
    <body>
      <p class="erreur-404">404</p>
      <h1>Page non trouvée !</h1>
      <p>Oups ! La page que vous cherchez n'existe pas.</p>

      <div class="url-demandee">
        URL demandée : <strong>${url}</strong>
      </div>

      <p>
        <a href="/">Retourner à l'accueil</a>
      </p>

      <footer>
        <hr>
        <small>&copy; 2026 - TP8 Serveur Node.js</small>
      </footer>
    </body>
    </html>
  `;
}
