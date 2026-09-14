# Coal blending, integer

Model, as a mixed-integer linear program, exactly which four of eight coal types to blend into one kilogram of coke mix, each used coal at least 5 % of the mix, respecting a silicon cap and two conditional-inclusion rules, at minimum cost.

## State

Not started. The question is pending.

## What is provided

- `handout/20-coals.md` — the original Caseine statement, wording untouched
- `coals.mod` — blank OPL template: objective and constraints empty
- `configExe` — the Caseine grader config, names `coals.mod`

## Running it

This is a Caseine VPL exercise: the graded run happens on Caseine's own CPLEX grader, and `configExe` names the model it runs. To check a model locally, open it in IBM's free OPL/CPLEX IDE, or run it from the command line with `oplrun`, if installed.

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`. The map is `obsidian-note.local.md`, two levels up.

## Source material

The statement is a Caseine VPL exercise (course staff) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays local in `handout/`, and `.publishignore` keeps it out of the public repository.
