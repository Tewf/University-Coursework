/*********************************************
 * OPL 12.6.0.0 Model
 * Bin packing program
 *********************************************/


//Make sure you use c[i] to access the i-th size 
//and do not remove/change the four following lines:
int NbObj = 15;
int W = 20;
range N =1..NbObj;
float c[N] = [6,6,6,7,7,7,8,8,8,9,9,9,10,10,10];


minimize ;

subject to{


}  
/* show solution */
execute {
   writeln("Value of the objective is: "+cplex.getObjValue());
}
