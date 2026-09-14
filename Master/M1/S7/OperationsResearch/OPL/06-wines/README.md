# Wine production with data abstraction

Model, as a linear program with its data loaded from `InstanceA.dat`, how much of each wine a cooperative should blend from its grape stocks to maximise profit, meeting each wine's minimum demand and allowing leftover grape juice to be sold off at a fixed price.

## State

Not started. The question is pending. Its reasoning, what was rejected and the reference that settles it will be in [steps/](steps/index.html), where the abridged statement is listed too.

## What is provided

- `handout/06-wines.md` — the original Caseine statement, wording untouched
- `wines.mod` — OPL template with the data-loading section given; variables, objective and constraints are empty
- `InstanceA.dat` — the wine count, grape count, costs, stocks, blend proportions and demands for one instance
- `configExe` — the Caseine grader config, names `wines.mod` and `InstanceA.dat`

## Running it

This is a Caseine VPL exercise: the graded run happens on Caseine's own CPLEX grader, and `configExe` names the model it runs. To check a model locally, open it in IBM's free OPL/CPLEX IDE, or run it from the command line with `oplrun`, if installed.

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`. The map is `obsidian-note.local.md`, two levels up.

## Source material

The statement is a Caseine VPL exercise (Hadrien Cambazard) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays local in `handout/`, and `.publishignore` keeps it out of the public repository.
