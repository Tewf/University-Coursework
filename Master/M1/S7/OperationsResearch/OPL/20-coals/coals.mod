/*********************************************
 * OPL 12.6.0.0 Model
 * Coals program
 *********************************************/
 
//Make sure you use c[i] to access the i-th cost 
//and do not remove/change the following line
float c[1..8] = [12, 14, 17, 10, 13, 9, 15, 11];
float s[1..8] = [0.02, 0.025, 0.01, 0.05, 0.01, 0.05, 0.02, 0.015];

minimize ;

subject to {

}

/* Affichage de la solution */
execute {
  writeln("Post-traitement: ");
  writeln("La valeur de l'objectif est de "+cplex.getObjValue());
} 