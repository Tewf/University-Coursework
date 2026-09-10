/*********************************************
 * OPL 12.6.0.0 Model
 * Airline
 *********************************************/

//Data declarations.
// do not remove/change the following lines
int n = ...; // number of shifts
int h = ...; // number of time intervals where a specific demand has been identified
range timeslots = 1..h; // interval to represent all timeslots
range shifts = 1..n;    // interval to represent all shifts
int demand[timeslots] = ...; // number of workers expected in each timeslots
float c[shifts] = ...; //cost of a worker in a given shift
int shiftdef[timeslots][shifts] = ...; // shiftdef[i][j] = 1 iff the j-th shift covers the i-th timeslot


//Decision variables.


//Objective function.
minimize ;

//Constraints
subject to {

}

// Display
execute {
  writeln("Post treatment: ");
  writeln("The objectif's value is  "+cplex.getObjValue());
} 