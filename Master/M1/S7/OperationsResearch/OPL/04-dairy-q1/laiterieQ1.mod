/*********************************************
 * OPL 12.6.0.0 Model
 * Laiterie - Question 1
 *********************************************/

//Assurez-vous d'utiliser c[i] pour acceder au i-eme cout 
//et ne supprimez pas et ne changez pas la ligne suivante
float c[1..4] = [20, 25, 15, 0.25];

maximize ;

subject to {

}

/* Affichage de la solution */
execute {
  writeln("Post-traitement: ");
  writeln("La valeur de l'objectif est de "+cplex.getObjValue());
} 