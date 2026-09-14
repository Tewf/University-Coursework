# Smartphone production allocation across plants

Model, as a linear program, how to split a fixed 2,000-unit smartphone order between two plants with different capacities and unit costs, each required to build at least 600 units a day, at the lowest total cost, allowing fractional units.

## State

Not started. The question is pending.

## What is provided

- `handout/05-apple-q4.md` — the original Caseine statement, wording untouched
- `pommeQ4.mod` — blank OPL template: the cost array is given, the objective and constraints are empty
- `configExe` — the Caseine grader config, names `pommeQ4.mod`

## Running it

This is a Caseine VPL exercise: the graded run happens on Caseine's own CPLEX grader, and `configExe` names the model it runs. To check a model locally, open it in IBM's free OPL/CPLEX IDE, or run it from the command line with `oplrun`, if installed.

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`.

## Source material

The statement is a Caseine VPL exercise (course staff) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays with the work on the private side, in `handout/`, and `.publishignore` keeps it out of this copy.
