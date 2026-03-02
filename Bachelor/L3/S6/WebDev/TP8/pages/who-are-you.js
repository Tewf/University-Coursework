// =============================================
// PAGE "QUI ÊTES-VOUS ?" - pages/who-are-you.js
// =============================================
//
// Deux fonctions :
// 1. getFormulaire() = affiche le formulaire (requête GET)
// 2. traiterFormulaire() = traite les données soumises (requête POST)
//
// Le formulaire demande le nom de l'utilisateur.
// Quand il est soumis, le serveur :
// 1. Récupère le nom
// 2. Crée un cookie avec ce nom
// 3. Redirige vers la page d'accueil
// 4. La page d'accueil lit le cookie et affiche "Bonjour [nom] !"


export function getFormulaire() {
  //
  // Cette fonction retourne le HTML du FORMULAIRE.
  // C'est la page que l'utilisateur voit quand il va sur /who-are-you

  return `
    <!DOCTYPE html>
    <html lang="fr">
    <head>
      <meta charset="UTF-8">
      <title>Qui êtes-vous ?</title>
      <style>
        body {
          font-family: "Gill Sans", sans-serif;
          max-width: 500px;
          margin: 40px auto;
          padding: 0 20px;
          background-color: #f8f9fa;
          color: #333;
        }
        h1 { color: #2c3e50; }
        form {
          background: white;
          padding: 25px;
          border-radius: 12px;
          box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        label {
          display: block;
          margin-bottom: 8px;
          font-weight: bold;
          color: #555;
        }
        input[type="text"] {
          width: 100%;
          padding: 12px;
          font-size: 16px;
          border: 2px solid #ddd;
          border-radius: 8px;
          box-sizing: border-box;
          margin-bottom: 15px;
        }
        input[type="text"]:focus {
          border-color: #4a90d9;
          outline: none;
        }
        button {
          width: 100%;
          padding: 12px;
          font-size: 16px;
          background-color: #4a90d9;
          color: white;
          border: none;
          border-radius: 8px;
          cursor: pointer;
        }
        button:hover { background-color: #357abd; }
        a { color: #4a90d9; }
      </style>
    </head>
    <body>
      <h1>Qui êtes-vous ?</h1>

      <form method="POST" action="/who-are-you">
        <!--
          method="POST" : les données sont envoyées dans le CORPS de la requête
            (pas visibles dans l'URL, contrairement à GET)

          action="/who-are-you" : l'URL qui recevra les données.
            Le serveur traite les requêtes POST sur cette URL.
        -->

        <label for="name">Votre prénom :</label>
        <input type="text" id="name" name="name" placeholder="Mohamed" required>
        <!--
          name="name" : le nom du champ.
          C'est la CLÉ utilisée pour récupérer la valeur côté serveur.
          Dans le corps de la requête : "name=Mohamed"
        -->

        <button type="submit">Me présenter</button>
      </form>

      <p><a href="/">Retour à l'accueil</a></p>

      <footer>
        <hr>
        <small>&copy; 2026 - TP8 Serveur Node.js</small>
      </footer>
    </body>
    </html>
  `;
}


export function traiterFormulaire() {
  //
  // Note : le traitement réel du POST se fait dans server.js
  // car il a besoin d'accéder à request et response directement.
  //
  // Cette fonction est exportée au cas où on voudrait séparer
  // la logique plus tard, mais pour ce TP le traitement
  // est directement dans server.js pour plus de clarté.
}
