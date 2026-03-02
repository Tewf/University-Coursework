// =============================================
// ROUTE : INSCRIPTION - routes/sign-up.js
// =============================================
//
// POST /sign-up → crée un nouveau compte utilisateur
//
// Étapes :
// 1. Vérifier que les champs ne sont pas vides
// 2. Hasher le mot de passe (JAMAIS le stocker en clair !)
// 3. Insérer dans la base de données
// 4. Gérer les erreurs (username déjà pris, etc.)
// 5. Créer une session (l'utilisateur est automatiquement connecté)


import { hashPassword } from "../lib/hash-password.js";
// On importe notre fonction de hashage


export async function postSignUp(req, res) {
  //
  // async car on fait des opérations asynchrones (base de données, hashage)

  // ---- ÉTAPE 1 : Récupérer et valider les données ----

  const { username, password, name } = req.body;
  //
  // req.body = les données envoyées par le client (formulaire ou JSON)
  // Le middleware express.json() ou express.urlencoded() l'a déjà parsé.
  //
  // Destructuring : { username, password, name } = req.body
  //   → extrait les propriétés en variables séparées
  //   C'est équivalent à :
  //   const username = req.body.username;
  //   const password = req.body.password;
  //   const name = req.body.name;

  // Vérifier que tous les champs sont remplis
  if (!username || !password || !name) {
    //
    // !username = true si username est undefined, null, "" (vide), 0, false
    // || = OU logique : si l'un OU l'autre est vide

    return res.status(400).json({ error: "Tous les champs sont obligatoires" });
    //
    // res.status(400) = définit le code HTTP à 400 (Bad Request)
    // .json({...}) = envoie une réponse au format JSON
    //
    // 400 = Bad Request = "ta demande est mal formulée"
    //
    // return = arrête la fonction ici (ne continue pas l'inscription)
  }

  // Vérifier que les champs sont des chaînes non vides
  if (typeof username !== "string" || typeof password !== "string" || typeof name !== "string") {
    return res.status(400).json({ error: "Les champs doivent être du texte" });
  }

  try {
    // ---- ÉTAPE 2 : Hasher le mot de passe ----

    const hashedPassword = await hashPassword(password);
    //
    // hashPassword("monMotDePasse")
    //   → "a3f9b2e1...:8c4d1a9f7b..."  (sel:hash)
    //
    // Le mot de passe original n'est PLUS JAMAIS stocké nulle part.
    // Même nous, les développeurs, on ne peut pas le retrouver !

    // ---- ÉTAPE 3 : Insérer dans la base de données ----

    await req.db.run(
      "INSERT INTO users (username, password, name) VALUES (?, ?, ?)",
      username,
      hashedPassword,
      name
    );
    //
    // INSERT INTO users (...) VALUES (?, ?, ?)
    //   = ajoute une nouvelle ligne dans la table users
    //
    // Les ? sont des PARAMÈTRES DE REQUÊTE.
    // Les valeurs réelles sont passées séparément (username, hashedPassword, name).
    //
    // ⚠️ SÉCURITÉ : Toujours utiliser ? au lieu de concaténer !
    // ❌ `INSERT INTO users VALUES ('${username}', '${password}', '${name}')`
    //     → Un pirate pourrait entrer username: "'; DROP TABLE users; --"
    //     → INJECTION SQL : la table est supprimée !
    //
    // ✅ "INSERT INTO users VALUES (?, ?, ?)", username, password, name
    //     → Les ? sont échappés automatiquement, l'injection est IMPOSSIBLE

    // ---- ÉTAPE 4 : Créer la session ----

    req.session.username = username;
    //
    // On stocke le username dans la SESSION.
    // Le middleware cookie-session va automatiquement créer un cookie
    // chiffré contenant cette information.
    //
    // À chaque requête suivante, le navigateur renverra ce cookie,
    // et le middleware le déchiffrera pour retrouver le username.

    // ---- ÉTAPE 5 : Répondre avec succès ----

    res.status(201).json({ message: "Compte créé avec succès !" });
    //
    // 201 = Created = "la ressource a été créée avec succès"
    // C'est le code approprié pour une inscription réussie.

  } catch (error) {
    // ---- GESTION DES ERREURS ----
    //
    // try/catch attrape les erreurs qui se produisent dans le try.

    if (error.message && error.message.includes("UNIQUE constraint failed")) {
      // L'erreur UNIQUE constraint signifie que le username existe déjà.
      // (username est PRIMARY KEY, donc unique)

      return res.status(409).json({ error: "Ce nom d'utilisateur est déjà pris" });
      //
      // 409 = Conflict = "il y a un conflit avec l'état actuel"
    }

    // Erreur inattendue (problème de base de données, etc.)
    console.error("Erreur lors de l'inscription :", error);
    res.status(500).json({ error: "Erreur interne du serveur" });
    //
    // 500 = Internal Server Error = "quelque chose s'est mal passé de notre côté"
    // On ne donne JAMAIS les détails de l'erreur au client (sécurité)
    // Mais on les affiche dans la console du serveur pour le débogage
  }
}
