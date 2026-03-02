// =============================================
// JAVASCRIPT CÔTÉ CLIENT - Inscription
// =============================================
//
// Ce fichier s'exécute dans le NAVIGATEUR (pas sur le serveur !).
//
// Il intercepte la soumission du formulaire d'inscription
// et envoie les données au serveur via fetch() (requête AJAX).
//
// fetch() permet d'envoyer des requêtes HTTP SANS recharger la page.
// C'est la base des applications web modernes "single-page".


// ---- Récupérer les éléments du DOM ----

const form = document.getElementById("signup-form");
const messageDiv = document.getElementById("message");


// ---- Écouter la soumission du formulaire ----

form.addEventListener("submit", async function (event) {
  //
  // async = cette fonction utilise await (opérations asynchrones)

  event.preventDefault();
  //
  // INDISPENSABLE !
  // Sans ça, le navigateur recharge la page et on perd tout.
  // On veut gérer l'envoi nous-mêmes avec fetch().

  // ---- Récupérer les valeurs des champs ----

  const username = document.getElementById("username").value.trim();
  const name = document.getElementById("name").value.trim();
  const password = document.getElementById("password").value;
  // On ne fait PAS de .trim() sur le mot de passe
  // (les espaces pourraient être intentionnels)

  // ---- Validation côté client ----

  if (!username || !name || !password) {
    afficherMessage("Veuillez remplir tous les champs", "error");
    return;
  }

  try {
    // ---- Envoyer les données au serveur ----

    const response = await fetch("/sign-up", {
      //
      // fetch(url, options) = envoie une requête HTTP
      //
      // C'est comme envoyer une lettre :
      // - url = l'adresse du destinataire ("/sign-up")
      // - options = le contenu et le format de la lettre

      method: "POST",
      // POST = on ENVOIE des données (pas juste demander une page)
      // GET  = on DEMANDE une page
      // POST = on ENVOIE des données pour créer quelque chose

      headers: {
        "Content-Type": "application/json",
        //
        // On dit au serveur : "les données que je t'envoie sont au format JSON"
        // Sans ça, le serveur ne saurait pas comment les lire.
        //
        // C'est comme mettre une étiquette sur un colis :
        // "Contient : des données JSON"
      },

      body: JSON.stringify({ username, name, password }),
      //
      // body = le CORPS de la requête (les données à envoyer)
      //
      // JSON.stringify() = convertit un objet JavaScript en texte JSON
      //
      // { username: "jean", name: "Jean Dupont", password: "secret" }
      // devient :
      // '{"username":"jean","name":"Jean Dupont","password":"secret"}'
      //
      // Le serveur (Express + express.json() middleware) le reconvertira
      // en objet JavaScript et le mettra dans req.body.
    });

    // ---- Lire la réponse du serveur ----

    const data = await response.json();
    //
    // response.json() = lit le corps de la réponse au format JSON
    // Le serveur a répondu avec res.json({ message: "..." })
    // On récupère cet objet ici.

    if (response.ok) {
      //
      // response.ok = true si le code HTTP est entre 200 et 299
      // 201 (Created) → ok = true
      // 400, 409, 500 → ok = false

      afficherMessage("Compte créé avec succès ! Redirection...", "success");

      // Rediriger vers la page d'accueil après 1 seconde
      setTimeout(() => {
        window.location.href = "/";
        //
        // window.location.href = "/" change l'URL de la page
        // Le navigateur charge la page d'accueil
      }, 1000);
      //
      // setTimeout(fonction, délai)
      //   = exécute la fonction APRÈS le délai (en millisecondes)
      //   1000 ms = 1 seconde
      //   On attend 1 seconde pour que l'utilisateur voie le message de succès

    } else {
      // Le serveur a renvoyé une erreur (400, 409, 500...)
      afficherMessage(data.error, "error");
    }

  } catch (error) {
    //
    // catch attrape les erreurs RÉSEAU (serveur injoignable, timeout...)
    // Pas les erreurs du serveur (celles-ci sont dans response.ok)

    afficherMessage("Impossible de contacter le serveur. Vérifiez votre connexion.", "error");
    console.error("Erreur fetch :", error);
  }
});


// ---- Fonction utilitaire pour afficher un message ----

function afficherMessage(texte, type) {
  //
  // texte = le message à afficher
  // type = "error" ou "success"

  messageDiv.textContent = texte;
  messageDiv.className = `message message-${type} visible`;
  //
  // On ajoute les classes CSS :
  // - "message" : styles de base
  // - "message-error" ou "message-success" : couleur selon le type
  // - "visible" : passe de display:none à display:block
}
