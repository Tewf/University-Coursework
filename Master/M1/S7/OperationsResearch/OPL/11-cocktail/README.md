# Cocktail blending

Three questions. 1. Model, as a linear program, the mix of two drinks that maximises a barman's profit under a minimum total volume, a taste ratio between the drinks, a cap on one of them, and a cap on total alcohol; solve it graphically by hand before checking the OPL run. 2. From the sensitivity table OPL reports, read off how far drink b2's profit per centilitre can move without changing which recipe is optimal. 3. From the same table, read off how much the alcohol cap could be relaxed before a different recipe becomes optimal.

## State

Not started. All three questions are pending.

## What is provided

- `handout/11-cocktail.md` — the original Caseine statement, wording untouched
- `cocktail.mod` — blank OPL template: objective and constraints empty
- `configExe` — the Caseine grader config, names `cocktail.mod`

## Running it

This is a Caseine VPL exercise: the graded run happens on Caseine's own CPLEX grader, and `configExe` names the model it runs. To check a model locally, open it in IBM's free OPL/CPLEX IDE, or run it from the command line with `oplrun`, if installed.

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`. The map is `obsidian-note.local.md`, two levels up.

## Source material

The statement is a Caseine VPL exercise (course staff) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays local in `handout/`, and `.publishignore` keeps it out of the public repository.
