# Steel alloy blending

Model, as a linear program, the cheapest blend of aluminium, iron and zinc that produces at least 60 tonnes of alloy within given carbon- and manganese-percentage ranges.

## State

Not started. The question is pending.

## What is provided

- `handout/08-alloy.md` — the original Caseine statement, wording untouched
- `steel.mod` — blank OPL template: the cost array is given, the objective and constraints are empty
- `configExe` — the Caseine grader config, names `steel.mod`

## Running it

This is a Caseine VPL exercise: the graded run happens on Caseine's own CPLEX grader, and `configExe` names the model it runs. To check a model locally, open it in IBM's free OPL/CPLEX IDE, or run it from the command line with `oplrun`, if installed.

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`.

## Source material

The statement is a Caseine VPL exercise (course staff) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays with the work on the private side, in `handout/`, and `.publishignore` keeps it out of this copy.
