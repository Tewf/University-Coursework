/*********************************************
 * OPL 12.6.0.0 Model
 * Dyeing plant program
 *********************************************/

range products = 1..5; //Products: P, Q, MP1, MP2, MP3
range machines = 1..4; //Machines A, B, C, D
float s[products][machines] = ...; //resource consumption of each product on each machine in minutes
float c[products] = ...; //selling price of each product (if positive) or buying price (if negative)


maximize 

subject to {
}

/* Display */
execute {
  writeln("Post-processing: ");
  writeln("The value of the objective is "+cplex.getObjValue());
} 