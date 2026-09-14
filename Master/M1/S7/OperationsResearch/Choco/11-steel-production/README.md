# Steel production, several instance sizes

Solve the steel-production instances Caseine provides, with the 'M2' CP model, over instances from 10 up to 111 orders, each run under a 5-second time limit.

The statement points at the course's CP exercise sheet for the problem description rather than restating it here.

## State

Not started. The question is pending.

## What is provided

- `handout/11-steel-production.md` — the original Caseine statement, wording untouched
- `steel_prod_solver_m2.py` — `SteelProdSlvM2`, the CP model class referred to as M2, with some methods left to fill in
- `steel_instance.py` — `SteelInstance`, reads orders, slabs and colours from a `.mill` file
- `executable.py` — solves a given instance file with a 5-second time limit
- `instances/*.mill` — nine steel-production benchmark instances, 10 to 111 orders

## Running it

One conda environment for the whole subject, declared once in
[environment.yml](../../environment.yml):

```bash
conda env create -f ../../environment.yml
conda activate operations_research
```

Then:

```bash
python executable.py
```

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`.

## Source material

The statement is a Caseine VPL exercise (Hadrien Cambazard) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays with the work on the private side, in `handout/`, and `.publishignore` keeps it out of this copy.
