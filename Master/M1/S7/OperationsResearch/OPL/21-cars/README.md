# Car parking minimizing street length

Formulate, as a mathematical program, how to split 15 cars of given lengths between the two sides of a street so the longer side's occupied length is as short as possible, and solve it.

(From L. Liberti.)

## State

Not started. The question is pending. Its reasoning, what was rejected and the reference that settles it will be in [steps/](steps/index.html), where the abridged statement is listed too.

## What is provided

- `handout/21-cars.md` — the original Caseine statement, wording untouched
- `cars.mod` — blank OPL template: the car-length array given, objective and constraints empty
- `configExe` — the Caseine grader config, names `cars.mod`

## Running it

This is a Caseine VPL exercise: the graded run happens on Caseine's own CPLEX grader, and `configExe` names the model it runs. To check a model locally, open it in IBM's free OPL/CPLEX IDE, or run it from the command line with `oplrun`, if installed.

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`. The map is `obsidian-note.local.md`, two levels up.

## Source material

The statement is a Caseine VPL exercise (Hadrien Cambazard) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays local in `handout/`, and `.publishignore` keeps it out of the public repository.
