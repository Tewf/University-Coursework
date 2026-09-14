# Incompatible chemical product warehouse assignment

Model, as a mathematical program with the incompatibility data loaded from `InstanceA.dat`, the fewest warehouses needed to store a set of chemical products so that no two incompatible products share one.

## State

Not started. The question is pending.

## What is provided

- `handout/25-toxic-warehouse.md` — the original Caseine statement, wording untouched
- `entrepot.mod` — OPL template with the data-loading section given; variables, objective and constraints are empty
- `InstanceA.dat` — the product count and the pairwise incompatibility matrix for one instance
- `configExe` — the Caseine grader config, names `entrepot.mod` and `InstanceA.dat`

## Running it

This is a Caseine VPL exercise: the graded run happens on Caseine's own CPLEX grader, and `configExe` names the model it runs. To check a model locally, open it in IBM's free OPL/CPLEX IDE, or run it from the command line with `oplrun`, if installed.

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`.

## Source material

The statement is a Caseine VPL exercise (Pierre Lemaire) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays with the work on the private side, in `handout/`, and `.publishignore` keeps it out of this copy.
