// =============================================
// ROUTE : DÉCONNEXION - routes/logout.js
// =============================================
//
// POST /logout → déconnecte l'utilisateur
//
// La déconnexion est TRÈS simple :
// On supprime la session → le cookie de session est invalidé
// → Le navigateur ne reconnaîtra plus l'utilisateur


export function postLogout(req, res) {

  req.session = null;
  //
  // Mettre la session à null = SUPPRIMER la session.
  //
  // Le middleware cookie-session va :
  // 1. Supprimer le cookie de session du navigateur
  // 2. L'utilisateur est déconnecté
  //
  // C'est comme enlever le bracelet VIP au concert :
  // tu ne peux plus accéder aux espaces VIP.

  res.redirect("/");
  //
  // res.redirect("/") = redirige vers la page d'accueil
  //
  // En coulisses, Express envoie :
  //   HTTP/1.1 302 Found
  //   Location: /
  //
  // Le navigateur reçoit cette réponse et va automatiquement
  // faire une nouvelle requête GET vers "/".
  //
  // L'utilisateur arrive sur la page d'accueil,
  // mais cette fois sans session → il voit le message "Bienvenue !"
  // avec les boutons "S'inscrire" et "Se connecter".
}
