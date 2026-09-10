/*********************************************
 * OPL 12.6.0.0 Model
 * Cars program
 *********************************************/
 
//Make sure you use c[i] to access the i-th cost 
//and do not remove/change the following three lines
range cars = 1..15;
range lines = 1..2;
float c[cars] = [4, 4.5, 5, 4.1, 2.4, 5.2, 3.7, 3.5, 3.2, 4.5, 2.3, 3.3, 3.8, 4.6, 3];

minimize ;

subject to {

}

/* Affichage de la solution */
execute {
  writeln("Post-traitement: ");
  writeln("La valeur de l'objectif est de "+cplex.getObjValue());
} 