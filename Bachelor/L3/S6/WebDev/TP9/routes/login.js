// =============================================
// ROUTE : CONNEXION - routes/login.js
// =============================================
//
// POST /login → vérifie les identifiants et connecte l'utilisateur
//
// Étapes :
// 1. Récupérer username et password
// 2. Chercher l'utilisateur dans la base de données
// 3. Vérifier le mot de passe (comparer avec le hash)
// 4. Si correct → créer une session
// 5. Si incorrect → renvoyer une erreur 401


import { verifyPassword } from "../lib/hash-password.js";


export async function postLogin(req, res) {

  const { username, password } = req.body;

  // ---- VALIDATION ----

  if (!username || !password) {
    return res.status(400).json({ error: "Nom d'utilisateur et mot de passe requis" });
  }

  try {
    // ---- CHERCHER L'UTILISATEUR ----

    const user = await req.db.get(
      "SELECT * FROM users WHERE username = ?",
      username
    );
    //
    // SELECT * FROM users WHERE username = ?
    //   = cherche un utilisateur par son username
    //   * = toutes les colonnes (username, password, name)
    //
    // .get() retourne UNE SEULE ligne (ou undefined si non trouvé)
    // (contrairement à .all() qui retourne TOUTES les lignes correspondantes)

    if (!user) {
      // L'utilisateur n'existe pas dans la base de données
      return res.status(401).json({ error: "Identifiants incorrects" });
      //
      // 401 = Unauthorized = "vous n'êtes pas autorisé"
      //
      // ⚠️ SÉCURITÉ : On ne dit PAS "cet utilisateur n'existe pas" !
      // Pourquoi ? Parce qu'un pirate pourrait l'utiliser pour
      // deviner quels usernames existent dans la base.
      // On dit juste "identifiants incorrects" (message vague exprès).
    }

    // ---- VÉRIFIER LE MOT DE PASSE ----

    const motDePasseCorrect = await verifyPassword(password, user.password);
    //
    // verifyPassword(motDePasse, hashStocké)
    //   = hash le mot de passe saisi avec le même sel
    //     et compare le résultat au hash stocké
    //   → true si correct, false sinon

    if (!motDePasseCorrect) {
      return res.status(401).json({ error: "Identifiants incorrects" });
      // Même message que si l'utilisateur n'existe pas (sécurité)
    }

    // ---- CRÉER LA SESSION ----

    req.session.username = username;
    //
    // L'utilisateur est maintenant connecté !
    // Le cookie de session sera envoyé automatiquement.

    // ---- RÉPONSE ----

    res.status(200).json({ message: "Connexion réussie !" });

  } catch (error) {
    console.error("Erreur lors de la connexion :", error);
    res.status(500).json({ error: "Erreur interne du serveur" });
  }
}
