// =============================================
// APPLICATION TODO LIST - todo-list.js
// =============================================
//
// Ce fichier contient TOUTE la logique de l'application.
// Il est chargé avec "defer" dans le HTML, donc il s'exécute
// après que tout le HTML est prêt.


// =============================================
// ÉTAPE 1 : Récupérer les éléments du DOM
// =============================================

const formulaire = document.getElementById("add-task");
// Le formulaire <form id="add-task">
// On en a besoin pour écouter l'événement "submit"

const listeTaches = document.getElementById("todo-list");
// La liste <ul id="todo-list">
// On va y ajouter des <li> pour chaque tâche


// =============================================
// ÉTAPE 2 : Écouter la soumission du formulaire
// =============================================

formulaire.addEventListener("submit", function (event) {
  // "submit" se déclenche quand :
  // 1. L'utilisateur clique sur le bouton "Ajouter"
  // 2. L'utilisateur appuie sur Entrée dans le champ

  event.preventDefault();
  //
  // TRÈS IMPORTANT !
  //
  // Par défaut, quand un formulaire est soumis, le navigateur
  // RECHARGE la page (il essaie d'envoyer les données à un serveur).
  //
  // On ne veut PAS ça ! On veut gérer la soumission nous-mêmes en JS.
  //
  // event.preventDefault() = "annule le comportement par défaut"
  //
  // Analogie : c'est comme dire au navigateur
  // "Non merci, je m'en occupe moi-même !"

  // Récupérer le texte saisi
  const inputTache = formulaire.elements["task-name"];
  //
  // formulaire.elements["task-name"]
  //   = accède au champ qui a name="task-name" dans le formulaire
  //
  // C'est une alternative à document.getElementById()
  // Plus pratique quand on travaille avec des formulaires

  const texte = inputTache.value.trim();
  //
  // .value = le texte tapé par l'utilisateur
  // .trim() = enlève les espaces au début et à la fin
  //   "  Faire les courses  " → "Faire les courses"
  //   "   " → "" (chaîne vide)

  // Vérifier que le texte n'est pas vide
  if (texte === "") {
    // L'attribut "required" du HTML empêche normalement
    // la soumission si le champ est vide, mais on vérifie quand même
    // (bonne pratique = toujours valider côté JS aussi)
    return;
  }

  // Créer la tâche et l'ajouter à la liste
  ajouterTache(texte);

  // Vider le champ de saisie
  inputTache.value = "";
  //
  // Remet le champ à vide après avoir ajouté la tâche.
  // L'utilisateur peut immédiatement taper la prochaine tâche.

  // Remettre le focus sur le champ
  inputTache.focus();
});


// =============================================
// ÉTAPE 3 : Créer un élément de tâche
// =============================================

function ajouterTache(texte) {
  // Cette fonction crée un <li> complet et l'ajoute à la liste

  // ---- Créer le <li> ----
  const li = document.createElement("li");
  //
  // document.createElement("li")
  //   = crée un élément <li> VIDE, pas encore dans la page
  //   C'est comme fabriquer une pièce de puzzle
  //   Il faut ensuite la poser au bon endroit

  // ---- Créer le <span> pour le texte ----
  const span = document.createElement("span");
  span.textContent = texte;
  //
  // .textContent = le texte à l'intérieur de l'élément
  // C'est plus sécurisé que .innerHTML car il n'interprète pas le HTML
  // (pas de risque d'injection XSS)

  // ---- Créer le conteneur de boutons ----
  const divBoutons = document.createElement("div");
  divBoutons.className = "boutons";
  // .className = la classe CSS de l'élément

  // ---- Bouton Monter (↑) ----
  const btnMonter = document.createElement("button");
  btnMonter.textContent = "↑";
  // ↑ = caractère Unicode "flèche vers le haut"
  btnMonter.className = "btn-monter";
  btnMonter.title = "Monter";
  // .title = texte qui apparaît quand la souris reste dessus (tooltip)

  btnMonter.addEventListener("click", function () {
    monterTache(li);
    // Quand on clique, on appelle la fonction monterTache
    // avec le <li> à monter
  });

  // ---- Bouton Descendre (↓) ----
  const btnDescendre = document.createElement("button");
  btnDescendre.textContent = "↓";
  btnDescendre.className = "btn-descendre";
  btnDescendre.title = "Descendre";

  btnDescendre.addEventListener("click", function () {
    descendreTache(li);
  });

  // ---- Bouton Supprimer (✕) ----
  const btnSupprimer = document.createElement("button");
  btnSupprimer.textContent = "✕";
  // ✕ = caractère Unicode "croix de multiplication"
  btnSupprimer.className = "btn-supprimer";
  btnSupprimer.title = "Supprimer";

  btnSupprimer.addEventListener("click", function () {
    supprimerTache(li);
  });

  // ---- Assembler les pièces du puzzle ----
  //
  // On construit le <li> en ajoutant les éléments un par un :
  //
  // <li>
  //   <span>texte de la tâche</span>
  //   <div class="boutons">
  //     <button>↑</button>
  //     <button>↓</button>
  //     <button>✕</button>
  //   </div>
  // </li>

  divBoutons.appendChild(btnMonter);
  divBoutons.appendChild(btnDescendre);
  divBoutons.appendChild(btnSupprimer);
  // Les 3 boutons sont dans le conteneur de boutons

  li.appendChild(span);
  li.appendChild(divBoutons);
  // Le span et les boutons sont dans le <li>

  listeTaches.appendChild(li);
  // Le <li> est ajouté À LA FIN de la liste <ul>
  //
  // appendChild = "ajoute comme dernier enfant"
  //
  // Avant : <ul> [tâche1] [tâche2] </ul>
  // Après : <ul> [tâche1] [tâche2] [nouvelleTâche] </ul>
}


// =============================================
// ÉTAPE 4 : Monter une tâche
// =============================================

function monterTache(li) {
  // li = le <li> de la tâche à monter

  const precedent = li.previousElementSibling;
  //
  // .previousElementSibling
  //   = l'élément juste AVANT dans la liste (le frère précédent)
  //
  // Exemple : [A] [B] [C]
  // B.previousElementSibling = A
  // A.previousElementSibling = null (pas de précédent)
  //
  // "Sibling" = frère/sœur (même parent)

  if (precedent === null) {
    // S'il n'y a pas d'élément avant, on ne peut pas monter !
    // La tâche est déjà en haut de la liste
    return;
  }

  listeTaches.insertBefore(li, precedent);
  //
  // insertBefore(nouvelElement, elementReference)
  //   = insère nouvelElement JUSTE AVANT elementReference
  //
  // Avant : [A] [B] [C]  (on veut monter B)
  // insertBefore(B, A) = insère B avant A
  // Après : [B] [A] [C]
  //
  // C'est comme prendre un livre sur l'étagère et le poser
  // juste avant le livre qui était au-dessus
}


// =============================================
// ÉTAPE 5 : Descendre une tâche
// =============================================

function descendreTache(li) {
  const suivant = li.nextElementSibling;
  //
  // .nextElementSibling
  //   = l'élément juste APRÈS dans la liste (le frère suivant)
  //
  // [A] [B] [C]
  // B.nextElementSibling = C
  // C.nextElementSibling = null (pas de suivant)

  if (suivant === null) {
    // Déjà en bas de la liste
    return;
  }

  listeTaches.insertBefore(li, suivant.nextElementSibling);
  //
  // L'astuce : pour mettre li APRÈS suivant,
  // on l'insère AVANT le frère de suivant.
  //
  // Avant : [A] [B] [C] [D]  (on veut descendre B)
  // suivant = C
  // suivant.nextElementSibling = D
  // insertBefore(B, D) = insère B avant D
  // Après : [A] [C] [B] [D]
  //
  // Si suivant est le DERNIER élément :
  // suivant.nextElementSibling = null
  // insertBefore(li, null) = appendChild(li) = ajoute à la fin
}


// =============================================
// ÉTAPE 6 : Supprimer une tâche
// =============================================

function supprimerTache(li) {
  li.remove();
  //
  // .remove() = supprime l'élément de la page
  //
  // C'est aussi simple que ça !
  // L'élément disparaît complètement du DOM.
  //
  // Avant : <ul> [A] [B] [C] </ul>
  // B.remove()
  // Après : <ul> [A] [C] </ul>
  //
  // Note : l'élément est supprimé du DOM mais reste en mémoire
  // tant que des variables le référencent.
  // Le garbage collector de JavaScript le nettoiera automatiquement.
}
