/*************************************************
 * OPL 12.6.0.0 Model
 * Entrepôts pour produits toxiques
 * author: Pierre Lemaire
 *************************************************/
 
//Data
// You should not change the existing code for loading the data but you can add the code you want
int n = ...;           // nombre de produits
range I = 1..n;
int c[I][I] = ...;     // matrice d'incompatibilités

//Variables

//Objective
minimize ;

//Constraints
subject to {

}

/* Affichage de la solution */
execute {
  writeln("Post-traitement: ");
  writeln("La valeur de l'objectif est de "+cplex.getObjValue());
} 