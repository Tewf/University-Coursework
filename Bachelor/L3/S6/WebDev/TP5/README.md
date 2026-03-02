# TP5 - JavaScript : Les Fondamentaux

## C'est quoi JavaScript ?

HTML = le squelette. CSS = les vêtements. Et **JavaScript** ? C'est le **cerveau** !

JavaScript (JS) rend les pages web **interactives** :
- Réagir aux clics de l'utilisateur
- Modifier le contenu de la page en temps réel
- Faire des calculs
- Communiquer avec des serveurs

> JavaScript n'a RIEN à voir avec Java ! C'est comme "hamster" et "hamburger" - ça commence pareil mais c'est complètement différent.

---

## Comment exécuter du JavaScript ?

### Méthode 1 : La console du navigateur
1. Ouvre ton navigateur (Chrome, Firefox)
2. Appuie sur **F12** (ou Ctrl+Shift+I)
3. Clique sur l'onglet **Console**
4. Tape du code JS et appuie sur Entrée

### Méthode 2 : Dans un fichier HTML
```html
<script src="exercices.js"></script>
```
Le navigateur exécute le fichier JS et affiche le résultat dans la console.

### Méthode 3 : Avec Node.js
```bash
node exercices.js
```

---

## Les bases de JavaScript

### Variables
```javascript
let nom = "Mohamed";     // Variable qui peut changer
const age = 22;          // Constante : ne change JAMAIS
var ancien = "obsolète"; // Ancienne façon, à éviter
```

### Types de données
```javascript
"texte"        // String (chaîne de caractères)
42             // Number (nombre)
true / false   // Boolean (vrai/faux)
{ a: 1, b: 2 } // Object (objet)
[1, 2, 3]      // Array (tableau)
null           // Rien (volontairement vide)
undefined      // Pas encore défini
```

### Fonctions
```javascript
// Déclaration classique
function direBonjour(nom) {
  return "Bonjour " + nom;
}

// Fonction fléchée (arrow function) - plus courte
const direBonjour = (nom) => "Bonjour " + nom;
```

### Closures (Fermetures)

Une **closure**, c'est une fonction qui "se souvient" des variables de son environnement.

> Analogie du sac à dos : quand une fonction est créée, elle met dans son sac à dos toutes les variables qu'elle voit autour d'elle. Même quand elle part ailleurs, elle a toujours son sac à dos.

```javascript
function creerCompteur() {
  let compte = 0;           // Variable dans le "sac à dos"
  return function() {
    compte++;               // La fonction se souvient de compte !
    return compte;
  };
}

const compteur = creerCompteur();
compteur(); // 1
compteur(); // 2
compteur(); // 3
```

### Callbacks

Un **callback** est une fonction passée en argument à une autre fonction.

> Analogie de la cuisine : "Quand la minuterie sonne (**événement**), sors le gâteau du four (**callback**)." Tu donnes les instructions À L'AVANCE.

```javascript
function faireSiPair(nombre, action) {
  if (nombre % 2 === 0) {
    action(nombre);  // Appelle la fonction passée en argument
  }
}

faireSiPair(4, (n) => console.log(n + " est pair")); // "4 est pair"
```

---

## Les 8 exercices

| # | Concept | Exercice |
|---|---------|----------|
| 1 | Boucles | Échiquier fixe 8x8 |
| 2 | Boucles | Échiquier dynamique (taille variable) |
| 3 | Objets | Intersection de deux objets |
| 4 | Chaînes | Fonction capitalize |
| 5 | Closures | Compteur préfixé |
| 6 | Closures | Compteur modifiable |
| 7 | Callbacks | Réimplémentation de filter |
| 8 | Currying | Fonction createFilter |

---

## Comment tester

1. Ouvre `index.html` dans ton navigateur
2. Ouvre la console (F12 → Console)
3. Les résultats des exercices s'affichent dans la console
4. Modifie `exercices.js` et rafraîchis pour voir les changements
