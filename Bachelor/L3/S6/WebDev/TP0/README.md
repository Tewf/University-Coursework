# TP0 - Mise en Place de l'Environnement

## C'est quoi le développement web ?

Imagine que tu veux construire une maison. Tu as besoin de :
- **Des briques** (c'est le **HTML** - la structure de ta page)
- **De la peinture et de la décoration** (c'est le **CSS** - les couleurs, les polices, la mise en page)
- **L'électricité et la plomberie** (c'est le **JavaScript** - tout ce qui bouge et réagit)

Le **développement web**, c'est l'art de construire des sites internet. Et comme pour une maison, on a besoin d'outils !

---

## Les outils dont on a besoin

### 1. Un éditeur de code : Visual Studio Code (VS Code)

C'est comme un **cahier intelligent** pour écrire du code. Il comprend ce que tu écris et t'aide avec :
- Des couleurs pour différencier les mots (coloration syntaxique)
- L'auto-complétion (il devine ce que tu veux écrire)
- La détection d'erreurs

**Installation :** [https://code.visualstudio.com/](https://code.visualstudio.com/)

### 2. Node.js (version LTS)

Node.js, c'est un **moteur** qui permet d'exécuter du JavaScript en dehors du navigateur. On en a besoin pour lancer un serveur web local.

> **LTS** = Long Term Support = la version stable et fiable. Toujours choisir la LTS !

**Installation :** [https://nodejs.org/](https://nodejs.org/)

### 3. Un navigateur web

C'est là où tu verras le résultat de ton travail ! Chrome, Firefox, Edge... peu importe, tant que c'est un navigateur moderne.

---

## Préparer son espace de travail

### Créer les dossiers

Comme un bon élève range ses cahiers, on va ranger notre code :

```
Bureau/
└── itw/              <-- Dossier principal du cours
    └── tp00/         <-- Dossier de ce TP
```

1. Crée un dossier `itw` (Introduction aux Technologies du Web)
2. À l'intérieur, crée un dossier `tp00`

### Ouvrir le dossier dans VS Code

**Ne jamais ouvrir un fichier seul !** Toujours ouvrir le **dossier entier**.

Comment faire :
1. Ouvre VS Code
2. **Glisse-dépose** le dossier `tp00` dans la fenêtre de VS Code
3. Ou bien : Menu Fichier → Ouvrir un dossier → choisis `tp00`

> Pourquoi le dossier entier ? Parce que VS Code comprend mieux ton projet quand il voit tous les fichiers ensemble. C'est comme lire un livre entier plutôt qu'une seule page.

---

## Ta première page web

Le fichier `test-protocol.html` dans ce dossier est ta toute première page web ! Ouvre-le dans VS Code pour voir le code, et dans un navigateur pour voir le résultat.

---

## C'est quoi un serveur web ?

### L'analogie du restaurant

Imagine un **restaurant** :
- Toi (le client) = le **navigateur** (Chrome, Firefox)
- Le menu = la **page HTML**
- Le serveur (la personne) = le **serveur web**

Quand tu vas au restaurant :
1. Tu **demandes** un plat (le navigateur demande une page)
2. Le serveur **va en cuisine** chercher ton plat (le serveur web cherche le fichier)
3. Le serveur te **rapporte** ton plat (le serveur web envoie la page)

> **Important :** Même pour des pages simples (statiques), on a besoin d'un serveur web ! Certaines fonctionnalités ne marchent pas si tu ouvres juste le fichier en double-cliquant.

### Lancer un serveur web local

On utilise `http-server`, un petit serveur web très simple.

#### Ouvrir le terminal dans VS Code

Le terminal, c'est une **boîte de dialogue avec l'ordinateur** où tu tapes des commandes textuelles.

- **Raccourci :** `Ctrl + ù` (ou `Ctrl + backtick`)
- **Ou :** Menu → Terminal → Nouveau Terminal

#### Lancer le serveur

Dans le terminal, tape :

```bash
npx http-server -c-1 -d
```

Décortiquons cette commande :
- `npx` : "Execute un paquet Node.js" (pas besoin de l'installer d'abord)
- `http-server` : le nom du programme (un serveur web simple)
- `-c-1` : désactive le cache (les fichiers sont toujours frais, pas de version ancienne)
- `-d` : affiche la liste des fichiers quand il n'y a pas de page `index.html`

### Qu'est-ce que localhost:8080 ?

Quand le serveur démarre, il affiche quelque chose comme :

```
Available on:
  http://localhost:8080
```

- **localhost** = "moi-même" = ton propre ordinateur
- **8080** = le numéro de la "porte" (port) par laquelle le serveur écoute

C'est comme si ton ordinateur jouait au restaurant : il est à la fois le client ET le serveur !

Ouvre ton navigateur et va à l'adresse : `http://localhost:8080`

### Arrêter le serveur

Pour arrêter le serveur, appuie sur `Ctrl + C` dans le terminal.

> **Ctrl + C** dans un terminal = "Arrête ce programme !" (pas copier-coller ici !)

---

## Résumé

| Concept | Explication simple |
|---------|-------------------|
| VS Code | Cahier intelligent pour écrire du code |
| Node.js | Moteur pour exécuter JavaScript |
| Navigateur | Fenêtre pour voir le résultat |
| Terminal | Boîte de dialogue texte avec l'ordinateur |
| Serveur web | Le "serveur" au restaurant qui amène les pages |
| localhost | Ton propre ordinateur |
| Port 8080 | La "porte" par laquelle le serveur écoute |
| Ctrl + C | Arrêter le serveur |

---

## Prochaine étape

Une fois que tout fonctionne, passe au **TP1** pour créer ta première vraie page HTML !
