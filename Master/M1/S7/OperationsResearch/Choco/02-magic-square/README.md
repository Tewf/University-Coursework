# Magic square

Write a CP model in pychoco that finds an order-n magic square in standard form — every row, column and both diagonals summing to the same value, with the smallest corner cell first and the second cell smaller than its mirror.

## State

Not started. The question is pending. Its reasoning, what was rejected and the reference that settles it will be in [steps/](steps/index.html), where the abridged statement is listed too.

## What is provided

- `handout/02-magic-square.md` — the original Caseine statement, wording untouched
- `magic_square.py` — `MagicSquarePychoco`, every method a `#TODO` stub

## Running it

One conda environment for the whole subject, declared once in
[environment.yml](../../environment.yml):

```bash
conda env create -f ../../environment.yml
conda activate operations_research
```

Then:

```bash
python magic_square.py
```

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`. The map is `obsidian-note.local.md`, two levels up.

## Source material

The statement is a Caseine VPL exercise (course staff) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays local in `handout/`, and `.publishignore` keeps it out of the public repository.
