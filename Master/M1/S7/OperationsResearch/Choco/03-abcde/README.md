# Find digits where ABCDE*4=EDCBA

Write a CP model in pychoco for the digit puzzle ABCDE×4=EDCBA: five different digits satisfying that scalar relation.

## State

Not started. The question is pending.

## What is provided

- `handout/03-abcde.md` — the original Caseine statement, wording untouched
- `abcde.py` — `ABCDE`, a documented skeleton with a scalar-constraint hint, body left to fill in

## Running it

One conda environment for the whole subject, declared once in
[environment.yml](../../environment.yml):

```bash
conda env create -f ../../environment.yml
conda activate operations_research
```

Then:

```bash
python abcde.py
```

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`. The map is `obsidian-note.local.md`, two levels up.

## Source material

The statement is a Caseine VPL exercise (course staff) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays local in `handout/`, and `.publishignore` keeps it out of the public repository.
