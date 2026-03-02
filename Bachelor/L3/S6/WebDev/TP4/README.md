# TP4 - CSS et Tableaux : "Faisons les courses !"

## Objectif

Apprendre à utiliser CSS pour mettre en forme des tableaux HTML.

Le principe est simple et puissant : **un seul fichier HTML, deux feuilles de style CSS différentes**. En changeant juste le fichier CSS lié, le même tableau change complètement d'apparence !

> C'est la magie du CSS : séparer le **contenu** (HTML) de la **présentation** (CSS).

---

## Le concept : un HTML, deux looks

```
shopping.html ──── utilise ──── styles-a.css  →  Look "Moderne & Zébré"
     │
     └──── OU utilise ──── styles-b.css  →  Look "Classique avec cadre"
```

Pour basculer entre les deux :
1. Ouvre `shopping.html` dans ton éditeur
2. Trouve la ligne `<link rel="stylesheet" href="styles-a.css">`
3. Change `styles-a.css` en `styles-b.css` (ou inversement)
4. Rafraîchis la page dans le navigateur (F5)

---

## Concepts CSS importants

### `border-collapse`

C'est LA propriété la plus importante pour les tableaux CSS.

**`border-collapse: separate`** (par défaut)
```
┌───┐ ┌───┐
│ A │ │ B │    ← Chaque cellule a SA propre bordure
└───┘ └───┘       (espace visible entre les cellules)
┌───┐ ┌───┐
│ C │ │ D │
└───┘ └───┘
```

**`border-collapse: collapse`**
```
┌───┬───┐
│ A │ B │    ← Les bordures FUSIONNENT
├───┼───┤       (pas d'espace entre les cellules)
│ C │ D │
└───┴───┘
```

### `border-spacing`
Fonctionne UNIQUEMENT avec `border-collapse: separate`.
Contrôle l'espace entre les cellules.

### Lignes alternées (zebra striping)
```css
tr:nth-child(even) { background-color: #f5f5f5; }
tr:nth-child(odd)  { background-color: white; }
```

---

## Fichiers de ce TP

| Fichier | Description |
|---------|-------------|
| `shopping.html` | La liste de courses (HTML pur) |
| `styles-a.css` | Style A : moderne, zébré, sans total |
| `styles-b.css` | Style B : classique avec cadre et total |

---

## Comment tester

1. Ouvre `shopping.html` dans le navigateur
2. Observe le style A
3. Modifie le `<link>` pour pointer vers `styles-b.css`
4. Rafraîchis et compare !
