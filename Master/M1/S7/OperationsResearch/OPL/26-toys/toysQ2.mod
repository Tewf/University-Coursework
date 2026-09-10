/*************************************************
 * OPL 12.6.0.0 Model
 * The toy shop program with setup costs
 * authors: Olivier briant and Hadrien cambazard
 *************************************************/

// Data
// load the data
// You should not change the existing code for loading the data but you can add the code you want

int nbToys = ...;                // number of toys
int nbWorkshops = ...;           // number of workshops
int demand = ...;                // the number of toys to produce

range toys      = 1..nbToys;        // interval to denote the set of toys
range workshops = 1..nbWorkshops;   // interval to denote the set of workshops
float prices[toys]           = ...; // the prices of each toy
float capa[workshops]        = ...; // the capacities of each workshop
float times[workshops][toys] = ...; // the production time for each toy and in workshop
float setupCost[toys]        = ...; // the setup cost of each toy (only used in question 2)

// Variables
// TODO
dvar float fake; //to make sure the model compiles so you can remove that variable you do the question yourself

// Objective
maximize fake;

// Constraints
subject to {

}

/* Affichage de la solution */
execute {
  writeln("Post-traitement: ");
  writeln("La valeur de l'objectif est de "+cplex.getObjValue());
} 