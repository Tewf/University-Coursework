# Heterosquare puzzle

Write a CP model in pychoco that finds order-3 heterosquares in standard form — every row, column and diagonal summing to a *different* value — and use it to check the claim that 3,120 essentially different ones exist.

## State

Not started. The question is pending.

## What is provided

- `handout/06-heterosquare.md` — the original Caseine statement, wording untouched
- `heterosquare.py` — `HeteroSquarePychoco`, a skeleton with commented `#TODO` hints, body left to fill in

## Running it

One conda environment for the whole subject, declared once in
[environment.yml](../../environment.yml):

```bash
conda env create -f ../../environment.yml
conda activate operations_research
```

Then:

```bash
python heterosquare.py
```

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`. The map is `obsidian-note.local.md`, two levels up.

## Source material

The statement is a Caseine VPL exercise (course staff) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays local in `handout/`, and `.publishignore` keeps it out of the public repository.
