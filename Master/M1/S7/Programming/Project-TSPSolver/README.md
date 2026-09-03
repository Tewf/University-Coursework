# Project: TSP solver

The Travelling Salesman Problem, solved exactly and then approximately, and the
two measured against each other.

## State

Not started. [steps/](steps/index.html) lists the stages, ready to be filled in
as the work happens.

## Stages

| # | Stage | What it is |
|---|-------|-----------|
| 1 | Read the instance format | Parse TSPLIB files: NODE_COORD_SECTION for coordinates and the lower-diagonal form for explicit distance matrices. |
| 2 | Build the distance matrix | Turn an instance into the matrix every algorithm below consumes, so the solvers never touch the file format. |
| 3 | Trivial method | Return the tour of vertices sorted by index, as the handout specifies. |
| 4 | Held-Karp | The exact dynamic-programming method the handout sets out, built on c(v, S). |
| 5 | A heuristic | An approximate method, for instances the exact one cannot reach. |
| 6 | Performance evaluation | Execution time and tour length against instance size, on the provided TSPLIB benchmarks and on instances from instance_generator.py, written up with figures. |

## Instances

`TSP-instances/` holds the TSPLIB benchmarks, in two forms: `coord/` for
instances given as coordinates, `lower_diag/` for those given as an explicit
lower-diagonal distance matrix. `instance_generator.py` makes random ones.

## Source material

The subject and `instance_generator.py` are by E. Foussard (UGA) and are **not
redistributed here**: see [NOTICE](../../../../../NOTICE). TSPLIB instances
belong to their authors and are cited, not claimed.
