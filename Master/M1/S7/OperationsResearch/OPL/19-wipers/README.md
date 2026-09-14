# Windscreen wiper production, integer

Two questions. 1. Model, as a mixed-integer linear program in `wipers.mod`, which of four machines to run and for how long each day to meet fixed minimum outputs of two wiper types at the lowest cost, including each machine's fixed cost where it has one. 2. Extend that model in `wipers2.mod` with two logical constraints: machines A and C are mutually exclusive, and using machine B at all forces at least an hour of machine C.

## State

Not started. All two questions are pending.

## What is provided

- `handout/19-wipers.md` — the original Caseine statement, wording untouched
- `wipers.mod` — blank OPL template for question 1: the cost array given, objective and constraints empty
- `wipers2.mod` — blank OPL template for question 2, to extend with the logical constraints
- `configExe` — the Caseine grader config, names which model runs

## Running it

This is a Caseine VPL exercise: the graded run happens on Caseine's own CPLEX grader, and `configExe` names the model it runs. To check a model locally, open it in IBM's free OPL/CPLEX IDE, or run it from the command line with `oplrun`, if installed.

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`. The map is `obsidian-note.local.md`, two levels up.

## Source material

The statement is a Caseine VPL exercise (course staff) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays local in `handout/`, and `.publishignore` keeps it out of the public repository.
