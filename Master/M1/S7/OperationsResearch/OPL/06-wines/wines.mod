/*************************************************
 * OPL 12.6.0.0 Model
 * The wine production problem
 * authors: Hadrien cambazard
 *************************************************/
 
//Data
// You should not change the existing code for loading the data but you can add the code you want
int n = ...; //load n (the number of wines) from the file 
int m = ...; //load m (the number of blends) from the file
range wines = 1..n;
range grapes = 1..m;
float c[wines] = ...; // load the cost c_j of each wine j
float s[grapes] = ...; // load the stock s_i of each grape i
int p[grapes][wines] = ...; // load p_ij the pourcentage (an integer in {0,...,100}) of grape i needed for wine j
float d[wines] = ...; // load d_j the minimum demand of wine j
float v = ...; //price of resell of one liter of blend (any type of grape)

//Variables
//TODO

//Pre-processing
execute INITIALIZE {
    
}  

//Objective
maximize ;

//Constraints
subject to {

}

/* Affichage de la solution */
execute {
  writeln("Post-traitement: ");
  writeln("La valeur de l'objectif est de "+cplex.getObjValue());
} 