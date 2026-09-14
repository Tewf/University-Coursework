# Free-form sandbox model

Pose and solve any model of your own, up to 30 model/data files; `configExe` names which model and data file to run, the thread count, the time limit and whether CPLEX should stop adding cuts on its own.

## State

Not started. The question is pending.

## What is provided

- `handout/03-sandbox.md` — the original Caseine statement, wording untouched
- `mymodel.mod` — an empty scaffold: pre-processing, objective and constraints blocks all blank
- `configExe` — the Caseine grader config, names `mymodel.mod` and the run options above

## Running it

This is a Caseine VPL exercise: the graded run happens on Caseine's own CPLEX grader, and `configExe` names the model it runs. To check a model locally, open it in IBM's free OPL/CPLEX IDE, or run it from the command line with `oplrun`, if installed.

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`.

## Source material

The statement is a Caseine VPL exercise (Nicolas Catusse, Hadrien Cambazard) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays with the work on the private side, in `handout/`, and `.publishignore` keeps it out of this copy.
