# TP9 - Serveur Web Complet avec Express

## C'est quoi Express ?

> **Analogie :**
> - **Node.js HTTP** (TP8) = construire une voiture pièce par pièce
> - **Express** = acheter un kit de voiture avec les pièces déjà assemblées
>
> Express fait la même chose que Node.js HTTP, mais en BEAUCOUP plus simple !

Express est un **framework** (boîte à outils) pour créer des serveurs web. Il gère pour nous :
- Le routage (quelle fonction pour quelle URL)
- Le middleware (chaîne de traitements)
- Les fichiers statiques (CSS, images, JS client)
- Et bien plus...

---

## Le concept de Middleware

> **Analogie de la chaîne de montage :**
> Dans une usine, chaque ouvrier sur la chaîne fait UNE chose :
> 1. Le 1er met les roues
> 2. Le 2ème peint la carrosserie
> 3. Le 3ème installe le moteur
>
> Un **middleware**, c'est un "ouvrier" de la chaîne.
> Chaque middleware traite la requête et la passe au SUIVANT.

```javascript
app.use((req, res, next) => {
  console.log("Je suis le middleware 1");
  next(); // Passe au suivant !
});

app.use((req, res, next) => {
  console.log("Je suis le middleware 2");
  next();
});
```

`next()` = "J'ai fini, passe au suivant sur la chaîne."

---

## Base de données SQLite

> **Analogie du classeur :**
> SQLite est un **classeur** numérique.
> - Les **tables** = les dossiers dans le classeur
> - Les **colonnes** = les catégories (nom, prénom, âge)
> - Les **lignes** = les fiches individuelles

### Commandes SQL de base
```sql
-- Créer une table (un dossier)
CREATE TABLE users (username TEXT, password TEXT, name TEXT);

-- Ajouter une fiche
INSERT INTO users VALUES ('jean', 'motdepasse123', 'Jean Dupont');

-- Chercher une fiche
SELECT * FROM users WHERE username = 'jean';
```

---

## Pourquoi hasher les mots de passe ?

> **RÈGLE D'OR : On ne stocke JAMAIS un mot de passe en clair !**

> **Analogie du coffre-fort :**
> - Mot de passe en clair = écrire le code sur un post-it
> - Mot de passe hashé = le mettre dans un coffre qu'on ne peut pas ouvrir à l'envers
>
> Le hash est une opération à SENS UNIQUE :
> `"motdepasse"` → `"a3f2b8c9d1..."` (facile)
> `"a3f2b8c9d1..."` → `"motdepasse"` (IMPOSSIBLE)

---

## Sessions

> **Analogie du bracelet de concert :**
> Quand tu arrives à un concert, on te met un bracelet VIP.
> À chaque espace VIP, tu montres ton bracelet et on te laisse passer.
> Tu n'as pas besoin de montrer ton billet à chaque fois !

Une **session** = un bracelet numérique. Le serveur crée un cookie de session, et à chaque requête le navigateur le renvoie.

---

## Codes HTTP utilisés

| Code | Nom | Quand ? |
|------|-----|---------|
| 200 | OK | Tout va bien |
| 201 | Created | Inscription réussie |
| 400 | Bad Request | Données invalides |
| 401 | Unauthorized | Mauvais identifiants |
| 409 | Conflict | Nom d'utilisateur déjà pris |
| 500 | Server Error | Erreur interne |

---

## Comment lancer le projet

```bash
# 1. Installer les dépendances
npm install

# 2. Initialiser la base de données
npm run init-db

# 3. Lancer le serveur
npm run dev
```

Puis ouvre `http://localhost:8080`

---

## Fichiers du projet

```
TP9/
├── server.js               # Serveur Express principal
├── package.json             # Configuration et dépendances
├── scripts/
│   └── init-db.js          # Initialisation de la base de données
├── lib/
│   └── hash-password.js    # Fonctions de hashage
├── routes/
│   ├── index.js            # Page d'accueil
│   ├── sign-up.js          # Inscription
│   ├── login.js            # Connexion
│   └── logout.js           # Déconnexion
└── public/
    ├── shared.css           # Styles CSS
    ├── sign-up.html         # Page d'inscription
    ├── login.html           # Page de connexion
    └── sign-up.js           # JS côté client (inscription)
```
