# Vegetable production planning

Model, as a linear program, how much of three vegetables a farm should grow from its labour time and two fertilizer budgets, to meet a 120 kg demand floor at the lowest total labour cost.

## State

Not started. The question is pending. Its reasoning, what was rejected and the reference that settles it will be in [steps/](steps/index.html), where the abridged statement is listed too.

## What is provided

- `handout/02-vegetables.md` — the original Caseine statement, wording untouched
- `legumes.mod` — blank OPL template: the cost array is given, the objective and constraints are empty
- `configExe` — the Caseine grader config, names `legumes.mod`

## Running it

This is a Caseine VPL exercise: the graded run happens on Caseine's own CPLEX grader, and `configExe` names the model it runs. To check a model locally, open it in IBM's free OPL/CPLEX IDE, or run it from the command line with `oplrun`, if installed.

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`. The map is `obsidian-note.local.md`, two levels up.

## Source material

The statement is a Caseine VPL exercise (course staff) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays local in `handout/`, and `.gitignore` keeps it out of the repository.
