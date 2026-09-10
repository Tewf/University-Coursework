# Operations Research

**Course:** Introduction to Artificial Intelligence, part 2 (operations research half), M1 Artificial Intelligence, Semester 7, Université Grenoble Alpes
**Teaching staff:** Hadrien Cambazard, Nicolas Catusse (lectures); Maxime Ogier, Nadia Brauner (tutorials); MIP chapters by Olivier Briant

Linear programming, duality, integer programming and branch and bound, then
constraint programming with Choco. Every Caseine VPL exercise is a folder
here: OPL models solved with CPLEX, Choco models solved with pychoco.

## OPL

| Folder | Problem | Solver | Provided |
|---|---|---|---|
| [OPL/01-opl-example/](OPL/01-opl-example/) | Worked example from the short OPL tutorial | OPL (CPLEX) | statement.md, example.mod, configExe |
| [OPL/02-vegetables/](OPL/02-vegetables/) | Vegetable production planning | OPL (CPLEX) | statement.md, legumes.mod, configExe |
| [OPL/03-sandbox/](OPL/03-sandbox/) | Free-form sandbox model | OPL (CPLEX) | statement.md, mymodel.mod, configExe |
| [OPL/04-dairy-q1/](OPL/04-dairy-q1/) | Dairy product mix, question 1 | OPL (CPLEX) | statement.md, laiterieQ1.mod, configExe |
| [OPL/05-apple-q4/](OPL/05-apple-q4/) | Smartphone production allocation across plants | OPL (CPLEX) | statement.md, pommeQ4.mod, configExe |
| [OPL/06-wines/](OPL/06-wines/) | Wine production with data abstraction | OPL (CPLEX) | statement.md, wines.mod, InstanceA.dat, configExe |
| [OPL/07-jam/](OPL/07-jam/) | Jam production planning | OPL (CPLEX) | statement.md, confiture.mod, configExe |
| [OPL/08-alloy/](OPL/08-alloy/) | Steel alloy blending | OPL (CPLEX) | statement.md, steel.mod, configExe |
| [OPL/09-water-network/](OPL/09-water-network/) | Water network flow management | OPL (CPLEX) | statement.md, flot.mod, instanceA.dat, configExe |
| [OPL/10-bill-of-materials/](OPL/10-bill-of-materials/) | Bill-of-materials production planning | OPL (CPLEX) | statement.md, billmaterial.mod, data1.dat, configExe |
| [OPL/11-cocktail/](OPL/11-cocktail/) | Cocktail blending | OPL (CPLEX) | statement.md, cocktail.mod, configExe |
| [OPL/12-airline/](OPL/12-airline/) | Airline scheduling with data abstraction | OPL (CPLEX) | statement.md, airline.mod, data1.dat, configExe |
| [OPL/13-garden-sensitivity/](OPL/13-garden-sensitivity/) | Garden planning, sensitivity analysis | OPL (CPLEX) | statement.md, garden.mod, configExe |
| [OPL/14-wines-q2/](OPL/14-wines-q2/) | Wine pricing from dual solution | OPL (CPLEX) | statement.md, wines.mod, configExe |
| [OPL/15-vitamins/](OPL/15-vitamins/) | Diet problem, vitamin requirements | OPL (CPLEX) | statement.md, vitamins.mod, configExe |
| [OPL/16-vitamins-q2/](OPL/16-vitamins-q2/) | Competitive pricing for synthetic vitamins | OPL (CPLEX) | statement.md, vitamins2.mod |
| [OPL/17-dual-program/](OPL/17-dual-program/) | Write the dual of a program | OPL (CPLEX) | statement.md, dual.mod, configExe |
| [OPL/18-bouquets/](OPL/18-bouquets/) | Flower bouquet selection | OPL (CPLEX) | statement.md, bouquets.mod, configExe |
| [OPL/19-wipers/](OPL/19-wipers/) | Windscreen wiper production, integer | OPL (CPLEX) | statement.md, wipers.mod, wipers2.mod, configExe |
| [OPL/20-coals/](OPL/20-coals/) | Coal blending, integer | OPL (CPLEX) | statement.md, coals.mod, configExe |
| [OPL/21-cars/](OPL/21-cars/) | Car parking minimizing street length | OPL (CPLEX) | statement.md, cars.mod, configExe |
| [OPL/22-lot-sizing/](OPL/22-lot-sizing/) | Lot sizing with .dat files | OPL (CPLEX) | statement.md, lotsizing.mod, data1.dat, configExe |
| [OPL/23-bin-packing/](OPL/23-bin-packing/) | Bin packing formulation | OPL (CPLEX) | statement.md, binpack.mod, configExe |
| [OPL/24-matrix-sum-euler-345/](OPL/24-matrix-sum-euler-345/) | Project Euler 345, matrix sum | OPL (CPLEX) | statement.md, euler.mod, data1.dat, configExe |
| [OPL/25-toxic-warehouse/](OPL/25-toxic-warehouse/) | Incompatible chemical product warehouse assignment | OPL (CPLEX) | statement.md, entrepot.mod, InstanceA.dat, configExe |
| [OPL/26-toys/](OPL/26-toys/) | Toy production planning | OPL (CPLEX) | statement.md, toysQ1.mod, toysQ2.mod, InstanceA.dat, configExe |

## Choco

| Folder | Problem | Solver | Provided |
|---|---|---|---|
| [Choco/01-toy-meeting/](Choco/01-toy-meeting/) | Toy meeting scheduling | pychoco | statement.md, toy_meeting.py, extended_toy_meeting.py, main.py |
| [Choco/02-magic-square/](Choco/02-magic-square/) | Magic square | pychoco | statement.md, magic_square.py |
| [Choco/03-abcde/](Choco/03-abcde/) | Find digits where ABCDE*4=EDCBA | pychoco | statement.md, abcde.py |
| [Choco/04-birthday/](Choco/04-birthday/) | Guess a birth year from clues | pychoco | statement.md, birthday.py |
| [Choco/05-sujiko/](Choco/05-sujiko/) | Sujiko puzzle | pychoco | statement.md, sujiko.py |
| [Choco/06-heterosquare/](Choco/06-heterosquare/) | Heterosquare puzzle | pychoco | statement.md, heterosquare.py |
| [Choco/07-magic-series/](Choco/07-magic-series/) | Magic series | pychoco | statement.md, magic_series.py |
| [Choco/08-n-queens/](Choco/08-n-queens/) | N-queens | pychoco | statement.md, n_queens.py |
| [Choco/09-warehouse-location/](Choco/09-warehouse-location/) | Warehouse location problem | pychoco | statement.md, warehouse_location.py |
| [Choco/10-car-sequencing/](Choco/10-car-sequencing/) | Car sequencing, several instance sizes | pychoco | statement.md, car_seq_solver.py, car_seq_instance.py, executable.py, instances/*.car |
| [Choco/11-steel-production/](Choco/11-steel-production/) | Steel production, several instance sizes | pychoco | statement.md, steel_prod_solver_m2.py, steel_instance.py, executable.py, instances/*.mill |

## Where the explanations live

Not here: `~/Desktop/Etude/Notes/S7/Operations Research/`, one note per
concept, alongside the lecture slides and exercises they come from.

`configExe` is the Caseine grader configuration for that VPL exercise (how it
was compiled and run on Moodle); it is not needed to run the model locally.
