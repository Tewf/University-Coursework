/*********************************************
 * OPL 12.6.0.0 Model
 * Dyeing plant program
 *********************************************/

int n = ...;
float c[1..n][1..n] = ...;

execute {
  writeln("Pre-processing: ");
  //you can compute here any constants (in particular the M values) needed by your model and that depends
  //on the data.
} 

maximize ;

subject to {

}

/* Affichage de la solution */
execute {
  writeln("Post-processing: ");
  writeln("The value of the objective is "+cplex.getObjValue());
} 