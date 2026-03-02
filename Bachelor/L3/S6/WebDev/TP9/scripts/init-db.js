// =============================================
// INITIALISATION DE LA BASE DE DONNÉES
// =============================================
//
// Ce script crée la base de données SQLite et ses tables.
// Il doit être exécuté UNE SEULE FOIS avant de lancer le serveur.
//
// Commande : npm run init-db
//
// Analogie : c'est comme préparer un classeur VIDE
// avec les dossiers et les étiquettes,
// avant de commencer à y ranger des fiches.


import { open } from "sqlite";
import sqlite3 from "sqlite3";


async function initialiserDB() {
  // async = cette fonction contient des opérations asynchrones (await)

  console.log("Initialisation de la base de données...");

  // ---- Ouvrir (ou créer) la base de données ----
  const db = await open({
    filename: "./database.sqlite",
    //
    // Le fichier où la base de données sera stockée.
    // SQLite stocke TOUT dans un SEUL fichier (contrairement à MySQL, PostgreSQL...).
    // Si le fichier n'existe pas, il sera créé automatiquement.

    driver: sqlite3.Database,
    // Le moteur de base de données à utiliser
  });

  // ---- Créer la table "users" ----
  await db.run(`
    CREATE TABLE IF NOT EXISTS users (
      username TEXT PRIMARY KEY,
      password TEXT NOT NULL,
      name TEXT NOT NULL
    )
  `);
  //
  // db.run() = exécute une commande SQL (sans retourner de données)
  //
  // CREATE TABLE = crée une nouvelle table (un nouveau dossier dans le classeur)
  //
  // IF NOT EXISTS = ne crée la table que si elle n'existe PAS déjà
  //   (évite une erreur si on exécute le script plusieurs fois)
  //
  // users = le nom de la table
  //
  // Les COLONNES :
  //
  // username TEXT PRIMARY KEY
  //   - TEXT = type texte (chaîne de caractères)
  //   - PRIMARY KEY = clé primaire = identifiant UNIQUE
  //     Chaque username est unique, comme un numéro de sécurité sociale
  //     Si on essaie d'insérer un username qui existe déjà → ERREUR
  //
  // password TEXT NOT NULL
  //   - NOT NULL = ne peut pas être vide
  //   - Contiendra le mot de passe HASHÉ (jamais en clair !)
  //
  // name TEXT NOT NULL
  //   - Le nom complet de l'utilisateur (ex: "Mohamed HAMLIL")

  console.log("Table 'users' créée avec succès !");
  console.log("La base de données est prête.");

  // ---- Fermer la connexion ----
  await db.close();
  // Toujours fermer la connexion quand on a fini !
}


// ---- Exécuter l'initialisation ----
initialiserDB().catch((err) => {
  //
  // .catch() intercepte les erreurs qui se produisent dans la fonction async.
  // Si quelque chose se passe mal (fichier non accessible, SQL invalide...),
  // l'erreur est attrapée ici et affichée.

  console.error("Erreur lors de l'initialisation :", err);
  process.exit(1);
  // process.exit(1) = arrête le programme avec un code d'erreur
  // 0 = succès, 1 = erreur
});
