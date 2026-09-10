/*********************************************
 * OPL 12.6.0.0 Model
 * Cocktail
 *********************************************/

//Assurez-vous d'utiliser c[i] pour acceder au i-eme cout 
//et ne supprimez pas et ne changez pas la ligne suivante
float c[1..2] = [0.1, 0.2];

maximize ;

subject to {

}

/* Affichage de la solution */
execute {
  writeln("Post-traitement: ");
  writeln("La valeur de l'objectif est de "+cplex.getObjValue());
} 