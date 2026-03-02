# TP7 - Application Liste de Tâches (Todo List)

## Ce qu'on construit

Une application web complète pour gérer une liste de tâches :
- **Ajouter** des tâches via un formulaire
- **Monter/Descendre** les tâches (changer l'ordre)
- **Supprimer** des tâches

> C'est un projet classique en développement web. Chaque développeur a fait une todo list dans sa carrière !

---

## Comment ça marche ?

### Les 3 fichiers travaillent ensemble

| Fichier | Rôle | Analogie |
|---------|------|----------|
| `todo-list.html` | La structure de la page | Le squelette |
| `todo-list.css` | L'apparence | Les vêtements |
| `todo-list.js` | Le comportement | Le cerveau |

### Le flux de données

```
Utilisateur tape une tâche → Submit du formulaire →
JavaScript intercepte → Crée un <li> avec boutons →
L'ajoute au <ul> → L'utilisateur voit la tâche !
```

---

## Concepts clés

### `event.preventDefault()`
Quand un formulaire est soumis, le navigateur recharge la page par défaut. On ne veut PAS ça ! `preventDefault()` empêche ce comportement.

### `document.createElement()`
Crée un nouvel élément HTML en JavaScript, prêt à être ajouté à la page.

### `appendChild()` et `insertBefore()`
- `parent.appendChild(enfant)` = ajoute à la fin
- `parent.insertBefore(nouveau, existant)` = insère AVANT un élément

### `element.remove()`
Supprime un élément de la page.

---

## Comment tester

1. Ouvre `todo-list.html` dans le navigateur
2. Tape une tâche et clique "Ajouter" (ou Entrée)
3. Utilise les boutons pour monter, descendre ou supprimer
