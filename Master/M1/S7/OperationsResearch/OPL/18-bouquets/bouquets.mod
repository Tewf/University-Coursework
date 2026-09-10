/*********************************************
 * OPL 12.6.0.0 Model
 * C'est le bouquet !
 * Pierre Lemaire, 2017-10-18
 *********************************************/
 
//Make sure you use c[i] to access the i-th cost 
//and do not remove/change the following line
float c[1..4] = [11,23,15,20];


minimize ;

subject to {

}

/* Affichage de la solution */
execute {
  writeln("Post-traitement: ");
  writeln("La valeur de l'objectif est de "+cplex.getObjValue());
} 