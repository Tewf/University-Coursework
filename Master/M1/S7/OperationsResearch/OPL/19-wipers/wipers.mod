/*********************************************
 * OPL 12.6.0.0 Model
 * Wipers program (QUESTION 1)
 *********************************************/
 
//Make sure you use c[i] to access the i-th cost 
//and do not remove/change the following line
float c[1..6] = [400, 600, 200, 250, 150, 230];


minimize ;

subject to {

}

/* Affichage de la solution */
execute {
  writeln("Post-traitement: ");
  writeln("La valeur de l'objectif est de "+cplex.getObjValue());
} 