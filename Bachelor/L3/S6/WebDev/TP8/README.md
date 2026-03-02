# TP8 - Mon Premier Serveur Web (Node.js pur)

## C'est quoi un serveur web ?

> **Analogie du restaurant :**
> - Le **client** (toi avec ton navigateur) = le client au restaurant
> - Le **serveur web** = le serveur (la personne) au restaurant
> - La **page HTML** = le plat commandé
>
> 1. Tu demandes le menu (tu tapes une URL)
> 2. Le serveur note ta commande (le serveur reçoit la requête HTTP)
> 3. Le serveur va en cuisine (le serveur cherche/génère la page)
> 4. Le serveur apporte ton plat (le serveur envoie la réponse)

Jusqu'ici, on utilisait `http-server` (un serveur tout fait). Maintenant, on va **construire notre propre serveur** !

---

## C'est quoi Node.js ?

JavaScript existe normalement dans le **navigateur**. Node.js permet d'utiliser JavaScript **en dehors du navigateur**, directement sur l'ordinateur.

C'est comme si JavaScript sortait de sa cage (le navigateur) pour explorer le monde extérieur (le système de fichiers, le réseau...).

---

## Le protocole HTTP

HTTP = **HyperText Transfer Protocol** = le langage que parlent les navigateurs et les serveurs.

### Requête (client → serveur)
```
GET /cv.html HTTP/1.1        ← "Je veux la page cv.html"
Host: localhost:8080          ← "Sur ce serveur"
```

### Réponse (serveur → client)
```
HTTP/1.1 200 OK               ← "Tout va bien, voici ta page"
Content-Type: text/html        ← "C'est du HTML"

<html>...</html>               ← Le contenu de la page
```

### Codes de statut HTTP
| Code | Signification | Analogie restaurant |
|------|---------------|---------------------|
| 200 | OK | "Voici votre plat !" |
| 303 | Redirection | "Allez à la table 5 !" |
| 404 | Non trouvé | "Ce plat n'est pas au menu" |
| 500 | Erreur serveur | "La cuisine est en feu !" |

---

## Les Cookies

> **Analogie du badge :**
> Tu vas à une conférence et on te donne un **badge avec ton nom**.
> Chaque fois que tu vas au buffet, le serveur lit ton badge
> et sait qui tu es, sans te redemander ton nom !

Un cookie, c'est un petit texte que le serveur colle sur le navigateur. Le navigateur le renvoie à chaque requête.

---

## Comment lancer le serveur

```bash
npm start        # Lance le serveur normalement
npm run dev      # Lance avec redémarrage automatique (--watch)
```

Puis ouvre `http://localhost:8080` dans ton navigateur.

---

## Fichiers de ce TP

| Fichier | Rôle |
|---------|------|
| `package.json` | Configuration du projet Node.js |
| `server.js` | Le serveur principal |
| `pages/index.js` | Page d'accueil (dynamique avec cookie) |
| `pages/404.js` | Page d'erreur 404 |
| `pages/who-are-you.js` | Formulaire + traitement du nom |
