/*********************************************
 * OPL 12.6.0.0 Model
 * Lot sizing program
 * author: Olivier Briant and Hadrien Cambazard
 *********************************************/
 /* Reading dimensions */
int nbDays = ...;

/* Definition of sets */
range days = 1 .. nbDays;

 /* Reading data from .dat file */
float d[days] = ...;
float c[days] = ...;
float h[days] = ...;
float f[days] = ...;

/* Pre-computation of constants */
float M[days];
execute INITIALIZE {
  for (var t1 in days) {
    M[t1] = 0;
    for (var t2 = t1; t2 <= nbDays; t2++) {
      M[t1] += d[t2];
    }
  }       
}  

/* Definition of variables */
dvar float+ x[days];
dvar float+ I[days];
dvar boolean y[days];

/* objective = production costs + storage costs + fixed costs */
minimize sum (t in days) c[t] * x[t] + 
         sum (t in days) h[t] * I[t] + 
         sum (t in days) f[t] * y[t];

/* Contraintes */
subject to {
  
  /* flow constraints */
  x[1] - I[1] == d[1];
  
  forall (t in 2..nbDays)   
        x[t] + I[t-1] - I[t] == d[t];
          
  /* constraint to define y */
  forall (t in days)
      x[t] <= M[t] * y[t];
  
}         
 
/* show solution */
execute {
  writeln("The objective value is "+cplex.getObjValue());
  for (var t in days) {
    if (y[t] == 1) {
      writeln ("Production on day "+t+" of "+x[t]+" units"); 
    }
  }
}