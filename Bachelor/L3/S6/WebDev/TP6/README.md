# TP6 - Le DOM : Manipuler les Pages Web avec JavaScript

## C'est quoi le DOM ?

Le **DOM** (Document Object Model) est la représentation de ta page HTML sous forme d'un **arbre** que JavaScript peut manipuler.

> **Analogie :** Imagine que le HTML est une **recette de cuisine** écrite sur papier. Le DOM, c'est le **plat réel** que le navigateur a cuisiné à partir de cette recette. Tu ne peux pas modifier la recette une fois le plat servi, mais tu PEUX modifier le plat lui-même (ajouter du sel, enlever un ingrédient...).

```
document                    ← La racine (le plat entier)
 └── html                   ← L'élément <html>
      ├── head              ← Le <head>
      │    └── title        ← Le <title>
      └── body              ← Le <body>
           ├── h1           ← Un titre
           ├── p            ← Un paragraphe
           └── button       ← Un bouton
```

---

## Les méthodes essentielles

### Sélectionner des éléments (trouver un ingrédient dans le plat)
```javascript
document.getElementById("monId")           // Par son ID (unique)
document.querySelector(".maClasse")        // Le PREMIER qui correspond
document.querySelectorAll("p")             // TOUS les paragraphes
```

### Modifier le contenu
```javascript
element.textContent = "Nouveau texte";     // Change le texte (sécurisé)
element.innerHTML = "<strong>Gras</strong>"; // Change le HTML (attention XSS !)
```

### Créer et ajouter des éléments
```javascript
const div = document.createElement("div"); // Crée un élément
div.textContent = "Bonjour";               // Lui donne du contenu
document.body.appendChild(div);             // L'ajoute à la page
```

### Écouter des événements
```javascript
bouton.addEventListener("click", function() {
  alert("Cliqué !");
});
```

---

## Les 3 projets de ce TP

| Fichier | Projet | Concepts |
|---------|--------|----------|
| `calc.html` | Calculatrice | Bug parseFloat, événements, querySelector |
| `degrees.html` | Convertisseur de température | Formulaires, conditions, calculs |
| `hidden-number.html` | Devinez le nombre | Math.random, boucle de jeu, historique |

---

## Le piège du + en JavaScript

```javascript
"5" + "3"  // → "53" (concaténation de chaînes !)
5 + 3      // → 8   (addition de nombres)

parseFloat("5") + parseFloat("3") // → 8 (conversion puis addition)
```

Les `<input>` HTML retournent TOUJOURS des **chaînes de caractères**, même pour les nombres ! Il faut les **convertir** avec `parseFloat()` ou `parseInt()`.
