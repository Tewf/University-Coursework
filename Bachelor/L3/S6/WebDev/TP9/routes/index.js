// =============================================
// ROUTE : PAGE D'ACCUEIL - routes/index.js
// =============================================
//
// GET / → affiche la page d'accueil
// Le contenu change selon que l'utilisateur est connecté ou non.


export function getIndex(req, res) {
  //
  // req.user est défini par notre middleware dans server.js.
  // Si l'utilisateur est connecté, req.user contient ses infos.
  // Sinon, req.user est null.

  let contenu;

  if (req.user) {
    // ---- UTILISATEUR CONNECTÉ ----
    contenu = `
      <h2>Bonjour ${req.user.name} !</h2>
      <p>Vous êtes connecté en tant que <strong>${req.user.username}</strong>.</p>

      <form method="POST" action="/logout">
        <button type="submit" class="btn btn-danger">Se déconnecter</button>
      </form>
    `;
    //
    // Le bouton de déconnexion est un FORMULAIRE avec method="POST".
    // Pourquoi POST et pas un simple lien (GET) ?
    // Parce que la déconnexion MODIFIE l'état du serveur (supprime la session).
    // En HTTP, les actions qui modifient des données doivent être en POST.
  } else {
    // ---- UTILISATEUR NON CONNECTÉ ----
    contenu = `
      <h2>Bienvenue !</h2>
      <p>Connectez-vous ou créez un compte pour commencer.</p>
      <div class="actions">
        <a href="/sign-up" class="btn">S'inscrire</a>
        <a href="/login" class="btn btn-secondary">Se connecter</a>
      </div>
    `;
  }

  // ---- ENVOYER LE HTML ----
  res.send(`
    <!DOCTYPE html>
    <html lang="fr">
    <head>
      <meta charset="UTF-8">
      <title>Accueil - Mon Application</title>
      <link rel="stylesheet" href="/shared.css">
    </head>
    <body>
      <div class="container">
        <h1>Mon Application Web</h1>
        ${contenu}
      </div>
    </body>
    </html>
  `);
  //
  // res.send() = envoie la réponse au client.
  // Express détecte automatiquement que c'est du HTML
  // et ajoute le header Content-Type: text/html.
  //
  // Différence avec TP8 :
  // TP8 : response.writeHead(200, {...}); response.end(html);
  // TP9 : res.send(html);  ← BEAUCOUP plus simple !
}
