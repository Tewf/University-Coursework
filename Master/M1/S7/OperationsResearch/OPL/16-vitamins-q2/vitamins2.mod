/*********************************************
 * OPL 12.6.0.0 Model
 * Vitamins 2
 *********************************************/

//Data declarations.
//Make sure you use c[i] to access the i-th cost 
//and do not remove/change the following line
int nbVitamins = 2;
range vitamins = 1 .. nbVitamins;

float c[vitamins] = [9,19];

//Decision variables.
dvar ;

//Objective function.
maximize;

//Constraints
subject to {
    ;
}

// Display
execute {
  writeln("Post treatment: ");
  writeln("The objectif's value is  "+cplex.getObjValue());
} 