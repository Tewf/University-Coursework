/*************************************************
 * OPL 12.6.0.0 Model
 * The generalized toy shop program
 * authors: Olivier briant and Hadrien cambazard
 *************************************************/

// Data
// You should not change the existing code for loading the data but you can add the code you want
int nbToys = ...;                // number of toys
int nbWorkshops = ...;           // number of workshops
int demand = ...;                // the number of toys to produce

range toys      = 1..nbToys;        // interval to denote the set of toys
range workshops = 1..nbWorkshops;   // interval to denote the set of workshops
float prices[toys]           = ...; // the prices of each toy
float capa[workshops]        = ...; // the capacities of each workshop
float times[workshops][toys] = ...; // the production time for each toy and each workshop
float setupCost[toys]        = ...; // the setup cost of each toy (only used in question 2)

// Variables
// TODO

// Objective
maximize ;

// Constraints
subject to {

}

/* Affichage de la solution */
execute {
  writeln("Post-treatment: ");
  writeln("The value of the objective is "+cplex.getObjValue());
} 