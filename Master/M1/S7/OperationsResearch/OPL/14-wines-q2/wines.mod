/*********************************************
 * OPL 12.6.0.0 Model
 * Wines (Q2)
 *********************************************/

//Make sure you use c[i] to access the i-th cost 
//and do not remove/change the following line
float c[1..3] = [5000, 1000, 4000];

minimize ;

subject to {

}

/* Affichage de la solution */
execute {
  writeln("Post-traitement: ");
  writeln("La valeur de l'objectif est de "+cplex.getObjValue());
} 