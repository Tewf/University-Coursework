# Operations Research

> [Lire en français](README.fr.md)

**Course:** Introduction to Artificial Intelligence, part 2 (operations research half), M1 Artificial Intelligence, Semester 7, Université Grenoble Alpes
**Teaching staff:** Hadrien Cambazard, Nicolas Catusse (lectures); Maxime Ogier, Nadia Brauner (tutorials); MIP chapters by Olivier Briant

Linear programming, duality, integer programming and branch and bound, then
constraint programming with Choco. Every Caseine VPL exercise is a folder
here: OPL models solved with CPLEX, Choco models solved with pychoco.

## OPL

| Folder | Problem | Solver | Provided |
|---|---|---|---|
| [OPL/01-opl-example/](OPL/01-opl-example/) | Worked example from the short OPL tutorial | OPL (CPLEX) | handout/, example.mod, configExe |
| [OPL/02-vegetables/](OPL/02-vegetables/) | Vegetable production planning | OPL (CPLEX) | handout/, legumes.mod, configExe |
| [OPL/03-sandbox/](OPL/03-sandbox/) | Free-form sandbox model | OPL (CPLEX) | handout/, mymodel.mod, configExe |
| [OPL/04-dairy-q1/](OPL/04-dairy-q1/) | Dairy product mix, question 1 | OPL (CPLEX) | handout/, laiterieQ1.mod, configExe |
| [OPL/05-apple-q4/](OPL/05-apple-q4/) | Smartphone production allocation across plants | OPL (CPLEX) | handout/, pommeQ4.mod, configExe |
| [OPL/06-wines/](OPL/06-wines/) | Wine production with data abstraction | OPL (CPLEX) | handout/, wines.mod, InstanceA.dat, configExe |
| [OPL/07-jam/](OPL/07-jam/) | Jam production planning | OPL (CPLEX) | handout/, confiture.mod, configExe |
| [OPL/08-alloy/](OPL/08-alloy/) | Steel alloy blending | OPL (CPLEX) | handout/, steel.mod, configExe |
| [OPL/09-water-network/](OPL/09-water-network/) | Water network flow management | OPL (CPLEX) | handout/, flot.mod, instanceA.dat, configExe |
| [OPL/10-bill-of-materials/](OPL/10-bill-of-materials/) | Bill-of-materials production planning | OPL (CPLEX) | handout/, billmaterial.mod, data1.dat, configExe |
| [OPL/11-cocktail/](OPL/11-cocktail/) | Cocktail blending | OPL (CPLEX) | handout/, cocktail.mod, configExe |
| [OPL/12-airline/](OPL/12-airline/) | Airline scheduling with data abstraction | OPL (CPLEX) | handout/, airline.mod, data1.dat, configExe |
| [OPL/13-garden-sensitivity/](OPL/13-garden-sensitivity/) | Garden planning, sensitivity analysis | OPL (CPLEX) | handout/, garden.mod, configExe |
| [OPL/14-wines-q2/](OPL/14-wines-q2/) | Wine pricing from dual solution | OPL (CPLEX) | handout/, wines.mod, configExe |
| [OPL/15-vitamins/](OPL/15-vitamins/) | Diet problem, vitamin requirements | OPL (CPLEX) | handout/, vitamins.mod, configExe |
| [OPL/16-vitamins-q2/](OPL/16-vitamins-q2/) | Competitive pricing for synthetic vitamins | OPL (CPLEX) | handout/, vitamins2.mod |
| [OPL/17-dual-program/](OPL/17-dual-program/) | Write the dual of a program | OPL (CPLEX) | handout/, dual.mod, configExe |
| [OPL/18-bouquets/](OPL/18-bouquets/) | Flower bouquet selection | OPL (CPLEX) | handout/, bouquets.mod, configExe |
| [OPL/19-wipers/](OPL/19-wipers/) | Windscreen wiper production, integer | OPL (CPLEX) | handout/, wipers.mod, wipers2.mod, configExe |
| [OPL/20-coals/](OPL/20-coals/) | Coal blending, integer | OPL (CPLEX) | handout/, coals.mod, configExe |
| [OPL/21-cars/](OPL/21-cars/) | Car parking minimizing street length | OPL (CPLEX) | handout/, cars.mod, configExe |
| [OPL/22-lot-sizing/](OPL/22-lot-sizing/) | Lot sizing with .dat files | OPL (CPLEX) | handout/, lotsizing.mod, data1.dat, configExe |
| [OPL/23-bin-packing/](OPL/23-bin-packing/) | Bin packing formulation | OPL (CPLEX) | handout/, binpack.mod, configExe |
| [OPL/24-matrix-sum-euler-345/](OPL/24-matrix-sum-euler-345/) | Project Euler 345, matrix sum | OPL (CPLEX) | handout/, euler.mod, data1.dat, configExe |
| [OPL/25-toxic-warehouse/](OPL/25-toxic-warehouse/) | Incompatible chemical product warehouse assignment | OPL (CPLEX) | handout/, entrepot.mod, InstanceA.dat, configExe |
| [OPL/26-toys/](OPL/26-toys/) | Toy production planning | OPL (CPLEX) | handout/, toysQ1.mod, toysQ2.mod, InstanceA.dat, configExe |

## Choco

| Folder | Problem | Solver | Provided |
|---|---|---|---|
| [Choco/01-toy-meeting/](Choco/01-toy-meeting/) | Toy meeting scheduling | pychoco | handout/, toy_meeting.py, extended_toy_meeting.py, main.py |
| [Choco/02-magic-square/](Choco/02-magic-square/) | Magic square | pychoco | handout/, magic_square.py |
| [Choco/03-abcde/](Choco/03-abcde/) | Find digits where ABCDE*4=EDCBA | pychoco | handout/, abcde.py |
| [Choco/04-birthday/](Choco/04-birthday/) | Guess a birth year from clues | pychoco | handout/, birthday.py |
| [Choco/05-sujiko/](Choco/05-sujiko/) | Sujiko puzzle | pychoco | handout/, sujiko.py |
| [Choco/06-heterosquare/](Choco/06-heterosquare/) | Heterosquare puzzle | pychoco | handout/, heterosquare.py |
| [Choco/07-magic-series/](Choco/07-magic-series/) | Magic series | pychoco | handout/, magic_series.py |
| [Choco/08-n-queens/](Choco/08-n-queens/) | N-queens | pychoco | handout/, n_queens.py |
| [Choco/09-warehouse-location/](Choco/09-warehouse-location/) | Warehouse location problem | pychoco | handout/, warehouse_location.py |
| [Choco/10-car-sequencing/](Choco/10-car-sequencing/) | Car sequencing, several instance sizes | pychoco | handout/, car_seq_solver.py, car_seq_instance.py, executable.py, instances/*.car |
| [Choco/11-steel-production/](Choco/11-steel-production/) | Steel production, several instance sizes | pychoco | handout/, steel_prod_solver_m2.py, steel_instance.py, executable.py, instances/*.mill |

## Setting up

OPL/CPLEX runs on Caseine's own grader; nothing needs installing locally to
submit a model. The Choco half is one conda environment, declared once in
[environment.yml](environment.yml):

```bash
conda env create -f environment.yml
conda activate operations_research
```

## Folder structure

Each exercise keeps the Caseine statement in `handout/` (the wording
untouched) and the starter model or script it shipped with, at the exercise
root, where the grader expects it. `.gitignore` excludes `handout/`, the grader
configuration `configExe`, the required `.dat` files and the CSPLib
`instances/`, so nothing Caseine distributed shows on GitHub; the starter
file does, since the grader edits it in place rather than producing a
separate output file — a README says what it asks, in my words, and a
`steps/` page records the work once there is some. The course's own
handouts (the OPL tutorials, the pychoco cheat sheet, the modelling
activity) sit in a `handout/` at this level, excluded the same way.

```
OperationsResearch/
|-- environment.yml               <- the one conda environment, for the Choco half
|-- handout/                      <- the course handouts: OPL tutorials, pychoco cheat sheet
|-- OPL/
|   |-- 01-opl-example/
|   |   |-- handout/               <- the Caseine statement
|   |   |-- README.md steps.json steps/   <- the ask in my words, one page per question
|   |   |-- example.mod            <- the starter model, edited in place
|   |   |-- configExe              <- the grader configuration, kept local
|   |-- 02-vegetables/ ... 26-toys/
|-- Choco/
|   |-- 01-toy-meeting/
|   |   |-- handout/
|   |   |-- toy_meeting.py extended_toy_meeting.py main.py
|   |-- 02-magic-square/ ... 11-steel-production/
```

`configExe` is the Caseine grader configuration for that VPL exercise: it
names the model (and data file, where there is one) CPLEX or the pychoco
`executable.py` runs on Moodle. It is not needed to run a model locally.

## Where the explanations live

Not here. The concepts each exercise needs — linear programming and duality,
integer programming and branch and bound, constraint programming — are
written up in a separate Obsidian vault, one note per concept, alongside the
lecture slides they come from. A comment here that starts teaching theory
belongs in that note instead.

## Source material

The exercise statements, the course handouts, the grader configurations,
the `.dat` files and the instances are **not redistributed here**: see
[NOTICE](../../../../NOTICE). Each statement stays on disk in its exercise's
`handout/`, wording untouched, the course handouts in the course's, and
`.gitignore` keeps all of it out of the repository. The starter model or script Caseine ships alongside each
statement is committed as given — it is what the grader edits in place, so
it stays in the repository until a filled-in version replaces it.
