// =============================================
// TP5 - EXERCICES JAVASCRIPT
// =============================================
//
// Pour voir les résultats :
// 1. Ouvre index.html dans le navigateur
// 2. Ouvre la console : F12 → onglet Console
//
// console.log() = affiche un message dans la console
// C'est comme un "print" en Python ou un "cout" en C++


// =============================================================
// EXERCICE 1 : Échiquier fixe (8x8)
// =============================================================
//
// CONCEPT : Les boucles (for)
//
// Objectif : Créer une grille 8x8 avec des espaces " " et "#"
// qui alternent, séparés par des retours à la ligne "\n".
//
// Résultat attendu :
// # # # #
//  # # # #
// # # # #
//  # # # #
// ... (8 lignes au total)
//
// "\n" = retour à la ligne (newline)
// C'est un caractère SPÉCIAL : il n'affiche rien mais saute une ligne.

console.log("=== EXERCICE 1 : Échiquier fixe ===");

let echiquier = "";
// On commence avec une chaîne vide.
// On va y ajouter des caractères un par un.

for (let ligne = 0; ligne < 8; ligne++) {
  // Boucle pour chaque LIGNE (de 0 à 7 = 8 lignes)
  // let ligne = 0  → on commence à 0
  // ligne < 8      → tant que ligne est inférieur à 8
  // ligne++        → on ajoute 1 à chaque tour (0, 1, 2, 3, 4, 5, 6, 7)

  for (let colonne = 0; colonne < 8; colonne++) {
    // Boucle pour chaque COLONNE dans cette ligne (de 0 à 7 = 8 colonnes)

    if ((ligne + colonne) % 2 === 0) {
      // (ligne + colonne) % 2 === 0 signifie :
      // "Est-ce que la somme ligne + colonne est paire ?"
      //
      // % = modulo = le reste de la division
      // 4 % 2 = 0 (pair)    → on met "#"
      // 5 % 2 = 1 (impair)  → on met " "
      //
      // C'est l'astuce pour alterner les cases !
      // Comme sur un vrai échiquier :
      // (0,0)=pair="#"  (0,1)=impair=" "  (0,2)=pair="#" ...

      echiquier += "#";
      // += signifie "ajouter à la fin de la chaîne"
      // echiquier = echiquier + "#"
    } else {
      echiquier += " ";
      // Case impaire = espace
    }
  }

  echiquier += "\n";
  // À la fin de chaque ligne, on ajoute un retour à la ligne
}

console.log(echiquier);
// Affiche l'échiquier complet dans la console


// =============================================================
// EXERCICE 2 : Échiquier dynamique
// =============================================================
//
// CONCEPT : Variables et réutilisabilité
//
// Même chose que l'exercice 1, mais avec une variable `size`
// qui permet de changer la taille de l'échiquier.
// Changez `size` pour tester : 5, 10, 15...

console.log("=== EXERCICE 2 : Échiquier dynamique ===");

const size = 10; // Essaie de changer cette valeur !

let echiquierDyn = "";

for (let ligne = 0; ligne < size; ligne++) {
  for (let colonne = 0; colonne < size; colonne++) {
    if ((ligne + colonne) % 2 === 0) {
      echiquierDyn += "#";
    } else {
      echiquierDyn += " ";
    }
  }
  echiquierDyn += "\n";
}

console.log(echiquierDyn);


// =============================================================
// EXERCICE 3 : Intersection de deux objets
// =============================================================
//
// CONCEPT : Les objets JavaScript
//
// Un OBJET en JS, c'est comme un dictionnaire :
// des paires clé → valeur.
//
// { nom: "Mohamed", age: 22 }
//   clé    valeur   clé  valeur
//
// L'INTERSECTION de deux objets = garder uniquement les paires
// clé-valeur qui sont IDENTIQUES dans les deux objets.
//
// Exemple :
// intersection({ a: 1, b: 2 }, { a: 1, b: 0 })
// → { a: 1 }   (seul "a" a la même valeur dans les deux)
//
// IMPORTANT : la fonction doit être PURE
// = elle ne modifie PAS les objets d'entrée
// = elle retourne un NOUVEL objet

console.log("=== EXERCICE 3 : Intersection ===");

function intersection(obj1, obj2) {
  // On crée un nouvel objet vide pour le résultat
  const resultat = {};

  // On parcourt toutes les clés du premier objet
  for (const cle in obj1) {
    // "for...in" parcourt les CLÉS (propriétés) d'un objet
    // À chaque tour, `cle` prend le nom d'une propriété

    if (obj2[cle] !== undefined && obj1[cle] === obj2[cle]) {
      // CONDITION 1 : obj2[cle] !== undefined
      //   → La clé existe aussi dans obj2
      //
      // CONDITION 2 : obj1[cle] === obj2[cle]
      //   → Les VALEURS sont identiques
      //
      // === (triple égal) vérifie l'égalité STRICTE :
      //   1 === 1     → true
      //   1 === "1"   → false (nombre ≠ chaîne)
      //   1 == "1"    → true  (comparaison laxiste, à ÉVITER !)

      resultat[cle] = obj1[cle];
      // On ajoute cette paire clé-valeur au résultat
    }
  }

  return resultat;
  // On retourne le nouvel objet (obj1 et obj2 n'ont PAS été modifiés !)
}

// Tests
console.log(intersection({ a: 1, b: 2 }, { a: 1, b: 2 }));
// → { a: 1, b: 2 } (tout est identique)

console.log(intersection({ a: 1, b: 2 }, { a: 1, b: 0 }));
// → { a: 1 } (seul "a" est identique)

console.log(intersection({ a: 1, b: 2 }, { c: 3 }));
// → {} (aucune clé en commun)


// =============================================================
// EXERCICE 4 : Fonction capitalize
// =============================================================
//
// CONCEPT : Manipulation de chaînes de caractères (strings)
//
// capitalize("hello world") → "Hello World"
// = Met la première lettre de chaque mot en MAJUSCULE
//
// Méthodes utiles sur les strings :
// - .split(" ") : découpe la chaîne aux espaces → tableau de mots
// - .toUpperCase() : met en majuscules
// - .toLowerCase() : met en minuscules
// - .charAt(0) : premier caractère (position 0)
// - .slice(1) : tout SAUF le premier caractère
// - .join(" ") : recolle un tableau en chaîne avec des espaces

console.log("=== EXERCICE 4 : Capitalize ===");

function capitalize(phrase) {
  // Étape 1 : Découper la phrase en mots
  const mots = phrase.split(" ");
  // "hello world" → ["hello", "world"]
  // split(" ") découpe la chaîne à chaque espace

  // Étape 2 : Transformer chaque mot
  const motsMajuscules = mots.map(function (mot) {
    // .map() applique une FONCTION à chaque élément du tableau
    // et retourne un NOUVEAU tableau avec les résultats

    if (mot.length === 0) return mot;
    // Si le mot est vide (double espace par ex.), on le laisse

    const premiereLettreEnMaj = mot.charAt(0).toUpperCase();
    // mot.charAt(0) = première lettre
    // .toUpperCase() = la met en majuscule

    const resteDuMot = mot.slice(1);
    // mot.slice(1) = tout le mot SAUF la première lettre
    // "hello".slice(1) → "ello"

    return premiereLettreEnMaj + resteDuMot;
    // "H" + "ello" = "Hello"
  });

  // Étape 3 : Recoller les mots
  return motsMajuscules.join(" ");
  // ["Hello", "World"].join(" ") → "Hello World"
}

// Tests
console.log(capitalize("hello world"));         // → "Hello World"
console.log(capitalize("bonjour le monde"));    // → "Bonjour Le Monde"
console.log(capitalize("javascript est cool")); // → "Javascript Est Cool"


// =============================================================
// EXERCICE 5 : Compteur préfixé (Closures)
// =============================================================
//
// CONCEPT : Les closures (fermetures)
//
// counter("page") retourne une FONCTION.
// Chaque fois qu'on appelle cette fonction, elle retourne :
// "page1", "page2", "page3"...
//
// La CLOSURE permet à la fonction retournée de "se souvenir"
// du compteur interne, même après que counter() a fini.
//
// Analogie du sac à dos :
// La fonction retournée emporte le compteur dans son sac à dos.
// Même quand elle est appelée ailleurs, elle a toujours son sac.

console.log("=== EXERCICE 5 : Compteur préfixé ===");

function counter(prefix) {
  // `prefix` est le texte à mettre devant le nombre

  let compteur = 0;
  // Le compteur interne commence à 0.
  // C'est cette variable qui est dans le "sac à dos" !

  // On RETOURNE une fonction (pas un résultat !)
  return function () {
    compteur++;
    // Incrémente le compteur : 0→1, 1→2, 2→3...
    // La fonction "se souvient" de la valeur précédente grâce à la closure

    return prefix + compteur;
    // Colle le préfixe et le nombre
    // "page" + 1 = "page1"
    // "page" + 2 = "page2"
  };
}

// Utilisation
const pageCounter = counter("page");
// pageCounter est maintenant une FONCTION (pas une valeur !)

console.log(pageCounter()); // → "page1"
console.log(pageCounter()); // → "page2"
console.log(pageCounter()); // → "page3"

// Chaque appel de counter() crée un compteur INDÉPENDANT
const visitorCounter = counter("visiteur-");
console.log(visitorCounter()); // → "visiteur-1"
console.log(visitorCounter()); // → "visiteur-2"

// pageCounter et visitorCounter ont chacun leur PROPRE compteur !
console.log(pageCounter()); // → "page4" (continue de compter)


// =============================================================
// EXERCICE 6 : Compteur modifiable
// =============================================================
//
// CONCEPT : Closures avancées
//
// Même chose que l'exercice 5, mais la fonction retournée
// accepte un argument OPTIONNEL pour RÉINITIALISER le compteur.
//
// counter("page")()  → "page1" (normal)
// counter("page")(5) → "page5" (réinitialise à 5)

console.log("=== EXERCICE 6 : Compteur modifiable ===");

function counterModifiable(prefix) {
  let compteur = 0;

  return function (nouvelleValeur) {
    // `nouvelleValeur` est OPTIONNEL
    // Si on ne passe rien, il sera `undefined`

    if (nouvelleValeur !== undefined) {
      // Si un argument est passé, on réinitialise le compteur
      compteur = nouvelleValeur;
    } else {
      // Sinon, on incrémente normalement
      compteur++;
    }

    return prefix + compteur;
  };
}

// Utilisation
const compteurPages = counterModifiable("p");
console.log(compteurPages());   // → "p1"
console.log(compteurPages());   // → "p2"
console.log(compteurPages());   // → "p3"
console.log(compteurPages(10)); // → "p10" (réinitialise à 10)
console.log(compteurPages());   // → "p11" (continue depuis 10)


// =============================================================
// EXERCICE 7 : Réimplémentation de filter (Callbacks)
// =============================================================
//
// CONCEPT : Les callbacks et les fonctions d'ordre supérieur
//
// Array.filter() garde uniquement les éléments qui passent un test.
// On doit la RÉIMPLÉMENTER sans utiliser la vraie .filter()
//
// Notre fonction prend :
// 1. Un tableau
// 2. Un "prédicat" (fonction qui retourne true ou false)
//
// Elle retourne un NOUVEAU tableau avec seulement les éléments
// pour lesquels le prédicat retourne true.

console.log("=== EXERCICE 7 : Filter maison ===");

function filtrer(tableau, predicat) {
  // predicat = une FONCTION qui prend un élément et retourne true/false
  // C'est un CALLBACK : une fonction passée en argument

  const resultat = [];
  // Nouveau tableau vide pour les résultats

  for (let i = 0; i < tableau.length; i++) {
    // On parcourt chaque élément du tableau

    if (predicat(tableau[i])) {
      // On appelle la fonction predicat avec l'élément courant
      // Si elle retourne true, on garde l'élément

      resultat.push(tableau[i]);
      // .push() ajoute un élément À LA FIN du tableau
    }
  }

  return resultat;
  // On retourne le nouveau tableau (l'original n'est PAS modifié)
}

// Tests

// Garder uniquement les nombres pairs
const nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const pairs = filtrer(nombres, function (n) {
  return n % 2 === 0;
  // n % 2 === 0 → true si n est pair
});
console.log("Pairs:", pairs); // → [2, 4, 6, 8, 10]

// Garder uniquement les mots de plus de 4 lettres
const mots = ["chat", "maison", "le", "ordinateur", "rue", "voiture"];
const motsLongs = filtrer(mots, function (mot) {
  return mot.length > 4;
});
console.log("Mots longs:", motsLongs); // → ["maison", "ordinateur", "voiture"]

// Avec une fonction fléchée (arrow function) - plus court
const positifs = filtrer([-3, -1, 0, 2, 5], (n) => n > 0);
console.log("Positifs:", positifs); // → [2, 5]


// =============================================================
// EXERCICE 8 : Currying avec createFilter
// =============================================================
//
// CONCEPT : Le currying
//
// Le CURRYING, c'est transformer une fonction à 2 arguments
// en une chaîne de fonctions à 1 argument chacune.
//
// Au lieu de : f(a, b) → résultat
// On fait :    f(a)(b) → résultat
//
// Pourquoi ? Pour créer des fonctions SPÉCIALISÉES réutilisables !
//
// createFilter prend UN prédicat et retourne UNE FONCTION
// qui prend un tableau et le filtre avec ce prédicat.
//
// C'est comme "préparer un filtre" et l'utiliser plus tard.
//
// Analogie : tu prépares un tamis de cuisine (le prédicat = la taille des trous).
// Ensuite tu peux l'utiliser autant de fois que tu veux sur différents ingrédients.

console.log("=== EXERCICE 8 : Currying - createFilter ===");

function createFilter(predicat) {
  // On retourne une FONCTION qui attend un tableau
  return function (tableau) {
    // Cette fonction interne utilise notre `filtrer` de l'exercice 7
    return filtrer(tableau, predicat);
  };
}

// Créer des filtres SPÉCIALISÉS (réutilisables !)
const garderPairs = createFilter((n) => n % 2 === 0);
// garderPairs est maintenant une FONCTION prête à l'emploi

const garderPositifs = createFilter((n) => n > 0);
// garderPositifs est une AUTRE fonction spécialisée

const garderMotsCourts = createFilter((mot) => mot.length <= 4);
// garderMotsCourts filtre les mots de 4 lettres ou moins

// Utilisation : on peut les appliquer à N'IMPORTE QUEL tableau
console.log(garderPairs([1, 2, 3, 4, 5, 6]));
// → [2, 4, 6]

console.log(garderPairs([10, 15, 20, 25, 30]));
// → [10, 20, 30]  (même filtre, tableau différent !)

console.log(garderPositifs([-5, -2, 0, 3, 7]));
// → [3, 7]

console.log(garderMotsCourts(["chat", "maison", "le", "ordinateur", "rue"]));
// → ["chat", "le", "rue"]


// =============================================================
// RÉSUMÉ DES CONCEPTS
// =============================================================
//
// 1. BOUCLES for : répéter des actions un nombre précis de fois
//
// 2. OBJETS : des "dictionnaires" clé → valeur
//    for...in parcourt les clés d'un objet
//
// 3. STRINGS : .split(), .join(), .charAt(), .slice(), .toUpperCase()
//    .map() transforme chaque élément d'un tableau
//
// 4. CLOSURES : une fonction "se souvient" de son environnement
//    = le sac à dos des variables
//
// 5. CALLBACKS : passer une fonction en argument à une autre
//    = donner des instructions à exécuter plus tard
//
// 6. CURRYING : transformer f(a, b) en f(a)(b)
//    = créer des fonctions spécialisées réutilisables
//
// =============================================================

console.log("=== Tous les exercices terminés ! ===");
