// =============================================
// HASHAGE DE MOTS DE PASSE - lib/hash-password.js
// =============================================
//
// Ce fichier contient les fonctions pour :
// 1. HASHER un mot de passe (avant de le stocker)
// 2. VÉRIFIER un mot de passe (lors de la connexion)
//
// RÈGLE D'OR DE LA SÉCURITÉ :
// On ne stocke JAMAIS un mot de passe en clair dans la base de données !
//
// Pourquoi ?
// Si un pirate accède à la base de données, il aurait tous les mots de passe.
// Avec le hashage, il n'a que des chaînes incompréhensibles.
//
// Le HASH est une opération à SENS UNIQUE :
// "motdepasse" → "a3f2b8c9d1e5..." (facile, instantané)
// "a3f2b8c9d1e5..." → "motdepasse" (IMPOSSIBLE, même avec un superordinateur)


import { scrypt, randomBytes, timingSafeEqual } from "node:crypto";
//
// Node.js a un module "crypto" intégré pour la cryptographie.
//
// scrypt : algorithme de hashage sécurisé (lent exprès pour les mots de passe)
// randomBytes : génère des octets aléatoires (pour le sel)
// timingSafeEqual : comparaison sécurisée (résiste aux attaques timing)

import { promisify } from "node:util";
//
// promisify transforme une fonction à callback en fonction à Promise.
// scrypt utilise des callbacks, mais on préfère async/await.

const scryptAsync = promisify(scrypt);
// scryptAsync est maintenant utilisable avec await !


// ---- HASHER UN MOT DE PASSE ----

export async function hashPassword(password) {
  //
  // Prend un mot de passe en clair et retourne une version hashée.
  //
  // Le format retourné : "sel:hash"
  // Le sel et le hash sont stockés ensemble, séparés par ":"

  const salt = randomBytes(16).toString("hex");
  //
  // Le SEL (salt) = une chaîne ALÉATOIRE ajoutée au mot de passe avant le hashage.
  //
  // Pourquoi le sel ?
  // Sans sel : "password123" → toujours le même hash
  //   → Un pirate peut utiliser un "rainbow table" (dictionnaire de hashs pré-calculés)
  //
  // Avec sel : "password123" + "a1b2c3" → hash unique à chaque fois !
  //   → Même mot de passe → hash DIFFÉRENT à chaque inscription
  //   → Les rainbow tables deviennent inutiles
  //
  // randomBytes(16) = 16 octets aléatoires
  // .toString("hex") = convertit en texte hexadécimal (0-9, a-f)
  //   Ex: "3a7f9b2e1d5c8a4f0e6b7d3c9a1f2e8d"

  const hash = await scryptAsync(password, salt, 64);
  //
  // scrypt(motDePasse, sel, longueur)
  //   = hash le mot de passe avec le sel
  //   64 = longueur du hash en octets
  //
  // scrypt est VOLONTAIREMENT LENT.
  // Pourquoi vouloir un algorithme lent ?
  //   → Un pirate qui essaie des millions de mots de passe
  //     prendra des années au lieu de quelques secondes.
  //   → Pour un utilisateur légitime, le délai est imperceptible.

  return `${salt}:${hash.toString("hex")}`;
  //
  // On stocke le sel ET le hash ensemble.
  // Format : "sel:hash"
  // Ex: "3a7f9b2e...:8c4d1a9f..."
  //
  // On a BESOIN du sel pour vérifier le mot de passe plus tard.
  // Chaque utilisateur a un sel différent !
}


// ---- VÉRIFIER UN MOT DE PASSE ----

export async function verifyPassword(password, storedHash) {
  //
  // Vérifie si un mot de passe correspond au hash stocké.
  //
  // password = le mot de passe saisi par l'utilisateur (en clair)
  // storedHash = le hash stocké dans la base de données ("sel:hash")
  //
  // Retourne : true (correct) ou false (incorrect)

  const [salt, hash] = storedHash.split(":");
  //
  // Découpe "sel:hash" en deux parties :
  // [salt, hash] = destructuring
  //   salt = la partie avant ":"
  //   hash = la partie après ":"

  const hashBuffer = Buffer.from(hash, "hex");
  //
  // Convertit le hash stocké (texte hexadécimal) en Buffer (octets).
  // Buffer = un tableau d'octets bruts en mémoire.
  // On en a besoin pour la comparaison sécurisée.

  const derivedHash = await scryptAsync(password, salt, 64);
  //
  // Hash le mot de passe saisi avec LE MÊME SEL que lors de l'inscription.
  // Si le mot de passe est correct, le résultat sera IDENTIQUE au hash stocké.

  return timingSafeEqual(hashBuffer, derivedHash);
  //
  // timingSafeEqual = comparaison à TEMPS CONSTANT
  //
  // Pourquoi pas simplement hash === derivedHash ?
  //
  // Attaque par mesure du temps (timing attack) :
  // Une comparaison normale s'arrête dès qu'elle trouve une différence.
  // "abcd" vs "axyz" → s'arrête au 2ème caractère (rapide)
  // "abcd" vs "abcx" → s'arrête au 4ème caractère (plus lent)
  //
  // Un pirate pourrait MESURER le temps de réponse pour deviner
  // combien de caractères sont corrects !
  //
  // timingSafeEqual compare TOUJOURS tous les caractères,
  // même si les premiers sont déjà différents.
  // → Même durée que le mot de passe soit presque bon ou complètement faux.
}
