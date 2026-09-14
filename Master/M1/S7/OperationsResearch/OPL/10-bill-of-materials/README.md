# Bill-of-materials production planning

Three questions. 1. By hand, work out the optimal weekly plan for the example instance: two products, each assembled from bought sub-components and processed on four time-capped machines, maximising profit. 2. Redo that hand computation after product P's time on machine C rises from 15 to 20 minutes, and find the new optimum. 3. Write the general linear program for the bill-of-materials plan, with the machine-time data for an instance loaded from `data1.dat`.

The statement points at a diagram (`assets/exoPDP.png`) that was not included in the download.

## State

Not started. All three questions are pending. Each one's reasoning, what was rejected and the reference that settles it will be in [steps/](steps/index.html), where the abridged statements are listed too.

## What is provided

- `handout/10-bill-of-materials.md` — the original Caseine statement, wording untouched
- `billmaterial.mod` — blank OPL template: data-loading section given, objective and constraints empty
- `data1.dat` — the products, machines, processing times, prices and machine-hour caps for one instance
- `configExe` — the Caseine grader config, names `billmaterial.mod` and `data1.dat`

## Running it

This is a Caseine VPL exercise: the graded run happens on Caseine's own CPLEX grader, and `configExe` names the model it runs. To check a model locally, open it in IBM's free OPL/CPLEX IDE, or run it from the command line with `oplrun`, if installed.

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`. The map is `obsidian-note.local.md`, two levels up.

## Source material

The statement is a Caseine VPL exercise (Hadrien Cambazard, Fabien Mangione) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays local in `handout/`, and `.publishignore` keeps it out of the public repository.
