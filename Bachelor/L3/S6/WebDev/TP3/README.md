# TP3 - CSS : Mise en Forme du Site Web

## C'est quoi le CSS ?

Tu te rappelles le HTML ? C'était le **squelette** de ta page. Maintenant, on va l'habiller !

**Analogie :**
- **HTML** = Le squelette (la structure, les os)
- **CSS** = Les vêtements, la coiffure, le maquillage (l'apparence)

CSS veut dire **Cascading Style Sheets** = "Feuilles de Style en Cascade".

> "En cascade" signifie que les styles se superposent comme des couches : si tu mets un style sur le `<body>`, tous les éléments à l'intérieur en héritent, sauf si tu les surcharges.

---

## Comment ça marche ?

Le CSS fonctionne avec 3 concepts :

### 1. Le sélecteur (QUI ?)
Quel élément tu veux styliser ?

```css
h1 {           /* Tous les <h1> de la page */
  color: red;
}
```

### 2. La propriété (QUOI ?)
Qu'est-ce que tu veux changer ?

```css
h1 {
  color: red;     /* La couleur du texte */
  font-size: 24px; /* La taille de la police */
}
```

### 3. La valeur (COMMENT ?)
Quelle valeur tu donnes ?

```css
h1 {
  color: red;       /* red = rouge */
  font-size: 24px;  /* 24px = 24 pixels de haut */
}
```

### La syntaxe complète

```css
sélecteur {
  propriété: valeur;
  propriété: valeur;
}
```

> N'oublie JAMAIS le `;` à la fin de chaque ligne ! Et les `{ }` autour du bloc.

---

## 3 façons d'ajouter du CSS

### 1. CSS en ligne (inline) - ÉVITER
```html
<p style="color: red;">Texte rouge</p>
```
Directement dans la balise. Pratique pour tester, mais **mauvaise pratique** en général.

### 2. CSS interne (dans `<style>`) - ACCEPTABLE
```html
<head>
  <style>
    p { color: red; }
  </style>
</head>
```
Dans le `<head>` de la page. OK pour les petits projets.

### 3. CSS externe (fichier .css) - LA MEILLEURE FAÇON
```html
<head>
  <link rel="stylesheet" href="shared/shared.css">
</head>
```
Un fichier séparé. **C'est ce qu'on utilise dans ce TP !**

> Pourquoi externe ? Parce qu'un même fichier CSS peut être partagé entre TOUTES les pages du site. Changement à un endroit = changement partout !

---

## Les Variables CSS (Custom Properties)

Imagine que tu utilises la couleur `#6d6875` à 50 endroits dans ton CSS. Si tu veux la changer, il faut modifier les 50 endroits !

Solution : les **variables CSS** !

```css
:root {
  --ma-couleur: #6d6875;   /* Déclaration de la variable */
}

h1 {
  color: var(--ma-couleur); /* Utilisation de la variable */
}
```

- `:root` = s'applique à tout le document
- `--nom` = convention pour nommer les variables (commence par --)
- `var(--nom)` = utiliser la variable

---

## Le Modèle de Boîte (Box Model)

Chaque élément HTML est une **boîte** avec 4 couches :

```
┌──────────────────────────── margin (marge externe) ──┐
│  ┌──────────────────────── border (bordure) ────────┐ │
│  │  ┌──────────────────── padding (marge interne) ─┐ │ │
│  │  │                                               │ │ │
│  │  │         CONTENU (texte, image...)             │ │ │
│  │  │                                               │ │ │
│  │  └───────────────────────────────────────────────┘ │ │
│  └─────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────┘
```

- **content** = le contenu lui-même
- **padding** = espace ENTRE le contenu et la bordure (marge intérieure)
- **border** = la bordure (le cadre)
- **margin** = espace AUTOUR de la boîte (marge extérieure)

---

## Flexbox (la disposition flexible)

Flexbox permet d'aligner des éléments facilement :

```css
.menu {
  display: flex;           /* Active Flexbox */
  justify-content: center; /* Centre horizontalement */
  align-items: center;     /* Centre verticalement */
  gap: 10px;               /* Espace entre les éléments */
}
```

Analogie : imagine une **étagère**. Flexbox te permet de dire :
- "Mets les livres au centre" (`justify-content: center`)
- "Espace-les de 10px" (`gap: 10px`)
- "Mets-les en ligne" (`flex-direction: row`)

---

## Les sélecteurs principaux

| Sélecteur | Cible | Exemple |
|-----------|-------|---------|
| `h1` | Toutes les balises `<h1>` | `h1 { color: red; }` |
| `.classe` | Les éléments avec `class="classe"` | `.menu { display: flex; }` |
| `#id` | L'élément avec `id="id"` | `#logo { width: 50px; }` |
| `a:hover` | Un lien quand la souris est dessus | `a:hover { color: blue; }` |
| `nav a` | Les `<a>` qui sont DANS un `<nav>` | `nav a { text-decoration: none; }` |

---

## Fichiers de ce TP

| Fichier | Description |
|---------|-------------|
| `shared/shared.css` | Styles partagés par toutes les pages (variables, police) |
| `menu.css` | Styles de la barre de navigation |
| `index.html` | Page d'accueil avec les logos |
| `cv.html` | Page CV avec mise en forme |
| `calendar.html` | Emploi du temps stylisé |
| `gallery.html` | Galerie de photos avec CSS Grid |

---

## Comment tester

1. Ouvre `index.html` dans ton navigateur
2. Navigue entre les pages via le menu
3. Modifie les fichiers CSS et rafraîchis la page (F5) pour voir les changements
4. Utilise F12 → onglet "Elements" pour inspecter les styles en direct !
