# Water network flow management

Model, as a linear program with its data loaded from `instanceA.dat`, how to route water from sources through intermediate stations that lose a fixed percentage in transit, to destinations with fixed demand, minimising the total drawn from the sources subject to every pipe's capacity.

## State

Not started. The question is pending.

## What is provided

- `handout/09-water-network.md` — the original Caseine statement, wording untouched
- `flot.mod` — OPL template with the data-loading section given; variables, objective and constraints are empty
- `instanceA.dat` — the sources, destinations, stations, pipe capacities, supply caps, demands and station loss rates for one instance
- `configExe` — the Caseine grader config, names `flot.mod` and `instanceA.dat`

## Running it

This is a Caseine VPL exercise: the graded run happens on Caseine's own CPLEX grader, and `configExe` names the model it runs. To check a model locally, open it in IBM's free OPL/CPLEX IDE, or run it from the command line with `oplrun`, if installed.

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`.

## Source material

The statement is a Caseine VPL exercise (course staff) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays with the work on the private side, in `handout/`, and `.publishignore` keeps it out of this copy.
