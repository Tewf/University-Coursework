/*********************************************
 * OPL 12.6.0.0 Model
 * Vitamins
 *********************************************/

//Data declarations.
//Make sure you use c[i] to access the i-th cost 
//and do not remove/change the following line
int nbFood = 6;
range food = 1 .. nbFood;

float c[food] = [35, 30, 60, 50, 27, 22];

//Decision variables.
dvar ;

//Objective function.
minimize ;

//Constraints
subject to {
    ;
}

// Display
execute {
  writeln("Post treatment: ");
  writeln("The objectif's value is  "+cplex.getObjValue());
} 