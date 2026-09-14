# Airline scheduling with data abstraction

Two questions. 1. Model, as an integer linear program with its data loaded from `data1.dat`, how many agents to assign to each of five overlapping shifts to cover the demand in every time slot at minimum cost, and notice which coverage constraints are redundant. 2. Force the assignment variables to be integers and see what changes, as a check on how tight the linear relaxation already was.

(Hillier and Lieberman, *Introduction to Operations Research*, is the source of this instance.)

## State

Not started. All two questions are pending. Each one's reasoning, what was rejected and the reference that settles it will be in [steps/](steps/index.html), where the abridged statements are listed too.

## What is provided

- `handout/12-airline.md` — the original Caseine statement, wording untouched
- `airline.mod` — OPL template with the data-loading section given; variables, objective and constraints are empty
- `data1.dat` — the shift definitions, per-slot demand and per-shift cost for one instance
- `configExe` — the Caseine grader config, names `airline.mod` and `data1.dat`

## Running it

This is a Caseine VPL exercise: the graded run happens on Caseine's own CPLEX grader, and `configExe` names the model it runs. To check a model locally, open it in IBM's free OPL/CPLEX IDE, or run it from the command line with `oplrun`, if installed.

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`. The map is `obsidian-note.local.md`, two levels up.

## Source material

The statement is a Caseine VPL exercise (course staff) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays local in `handout/`, and `.publishignore` keeps it out of the public repository.
