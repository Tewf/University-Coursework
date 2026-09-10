/*********************************************
 * OPL 12.6.0.0 Model
 * Example
 *********************************************/

float c[1..3] = [4, -2, 1];

dvar float+ x;
dvar float  y;
dvar float  w;

maximize c[1]*x + c[2]*y + c[3]*w;

subject to {
    2*x +   y       >= 14;
            y -   w <= 10;
      x - 2*y + 2*w == 3;
                  w <= 0;
}

/* Show optimal solution */
execute {
  writeln("Post-processing: ");
  writeln("Value of the objective is: "+cplex.getObjValue());
  writeln("x: "+x);
  writeln("y: "+y);
  writeln("w: "+w);
} 