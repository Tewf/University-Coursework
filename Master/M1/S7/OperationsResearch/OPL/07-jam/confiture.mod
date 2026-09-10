/*********************************************
 * OPL 12.6.0.0 Model
 * Jam - Confiture
 *********************************************/

//Make sure you use c[i] to access the i-th cost 
//and do not remove/change the following line
float c[1..2] = [3, 5];

maximize ;

subject to {

}

// Display
execute {
  writeln("Post treatment: ");
  writeln("The objectif's value is  "+cplex.getObjValue());
}