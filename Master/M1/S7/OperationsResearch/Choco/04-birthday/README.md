# Guess a birth year from clues

Write a CP model in pychoco for the puzzle: in 2021 a person's age equalled the sum of their birth year's digits, and they were under 100; find the possible birth years.

## State

Not started. The question is pending. Its reasoning, what was rejected and the reference that settles it will be in [steps/](steps/index.html), where the abridged statement is listed too.

## What is provided

- `handout/04-birthday.md` — the original Caseine statement, wording untouched
- `birthday.py` — `Birthday`, a documented skeleton, body left to fill in

## Running it

One conda environment for the whole subject, declared once in
[environment.yml](../../environment.yml):

```bash
conda env create -f ../../environment.yml
conda activate operations_research
```

Then:

```bash
python birthday.py
```

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`. The map is `obsidian-note.local.md`, two levels up.

## Source material

The statement is a Caseine VPL exercise (course staff) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays local in `handout/`, and `.gitignore` keeps it out of the repository.
