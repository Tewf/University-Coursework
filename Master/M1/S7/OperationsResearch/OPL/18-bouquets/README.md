# Flower bouquet selection

Model, as an integer program, which of four one-off flower bunches to buy to reach at least 40 flowers at the lowest total cost.

## State

Not started. The question is pending. Its reasoning, what was rejected and the reference that settles it will be in [steps/](steps/index.html), where the abridged statement is listed too.

## What is provided

- `handout/18-bouquets.md` — the original Caseine statement, wording untouched
- `bouquets.mod` — blank OPL template: objective and constraints empty
- `configExe` — the Caseine grader config, names `bouquets.mod`

## Running it

This is a Caseine VPL exercise: the graded run happens on Caseine's own CPLEX grader, and `configExe` names the model it runs. To check a model locally, open it in IBM's free OPL/CPLEX IDE, or run it from the command line with `oplrun`, if installed.

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`. The map is `obsidian-note.local.md`, two levels up.

## Source material

The statement is a Caseine VPL exercise (Pierre Lemaire) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays local in `handout/`, and `.gitignore` keeps it out of the repository.
