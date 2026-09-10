/*********************************************
 * OPL 12.6.0.0 Model
 * Pomme - Question 4
 *********************************************/

//Assurez-vous d'utiliser c[i] pour acceder au i-eme cout 
//et ne supprimez pas et ne changez pas la ligne suivante
float c[1..8] = [1.6, 1.85, 0.53, 2.73, 1.43, 2.05, 110, 130];

minimize ;

subject to {

}

/* Affichage de la solution */
execute {
  writeln("Post-traitement: ");
  writeln("La valeur de l'objectif est de "+cplex.getObjValue());
} 