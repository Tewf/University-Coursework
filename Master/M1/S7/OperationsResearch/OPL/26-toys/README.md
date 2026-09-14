# Toy production planning

Two questions. 1. Model, as an integer program with data loaded from `InstanceA.dat`, which toys to produce, each needing processing time on every workshop and sharing one component capped at a fixed total demand, to maximise profit. 2. Extend that model with a fixed cost, charged for any toy type produced at all, for the dedicated test machine its quality check needs.

(A generalisation of an earlier Caseine exercise, ‘Toy Shop’, not part of this repository.)

## State

Not started. All two questions are pending. Each one's reasoning, what was rejected and the reference that settles it will be in [steps/](steps/index.html), where the abridged statements are listed too.

## What is provided

- `handout/26-toys.md` — the original Caseine statement, wording untouched
- `toysQ1.mod` — OPL template for question 1, data-loading given, variables/objective/constraints empty
- `toysQ2.mod` — OPL template for question 2, with a placeholder `fake` variable/objective so it compiles before editing
- `InstanceA.dat` — the toy prices, workshop capacities, per-toy processing times and the shared demand cap
- `configExe` — the Caseine grader config, names which model and `InstanceA.dat`

## Running it

This is a Caseine VPL exercise: the graded run happens on Caseine's own CPLEX grader, and `configExe` names the model it runs. To check a model locally, open it in IBM's free OPL/CPLEX IDE, or run it from the command line with `oplrun`, if installed.

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`. The map is `obsidian-note.local.md`, two levels up.

## Source material

The statement is a Caseine VPL exercise (Hadrien Cambazard, Olivier Briant) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays local in `handout/`, and `.publishignore` keeps it out of the public repository.
