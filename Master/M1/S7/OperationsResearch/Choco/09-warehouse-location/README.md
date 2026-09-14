# Warehouse location problem

Write a CP model in pychoco for the CSPLib warehouse-location problem: which candidate warehouses to open and which store connects to which, each warehouse capped in how many stores it serves, to minimise total fixed and connection cost.

## State

Not started. The question is pending.

## What is provided

- `handout/09-warehouse-location.md` — the original Caseine statement, wording untouched
- `warehouse_location.py` — `WarehouseLocation`, a documented skeleton, body left to fill in

## Running it

One conda environment for the whole subject, declared once in
[environment.yml](../../environment.yml):

```bash
conda env create -f ../../environment.yml
conda activate operations_research
```

Then:

```bash
python warehouse_location.py
```

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`. The map is `obsidian-note.local.md`, two levels up.

## Source material

The statement is a Caseine VPL exercise (course staff) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays local in `handout/`, and `.publishignore` keeps it out of the public repository.
