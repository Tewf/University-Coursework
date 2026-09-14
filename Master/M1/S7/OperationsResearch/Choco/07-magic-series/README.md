# Magic series

Write a CP model in pychoco that finds a magic series of a given length n — a sequence of n values between 0 and n−1 where each value i occurs exactly as many times as the sequence's i-th entry says — strong enough not to time out.

## State

Not started. The question is pending.

## What is provided

- `handout/07-magic-series.md` — the original Caseine statement, wording untouched
- `magic_series.py` — `MagicSeriesPychoco`, bare method stubs, body left to fill in

## Running it

One conda environment for the whole subject, declared once in
[environment.yml](../../environment.yml):

```bash
conda env create -f ../../environment.yml
conda activate operations_research
```

Then:

```bash
python magic_series.py
```

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`.

## Source material

The statement is a Caseine VPL exercise (course staff) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays with the work on the private side, in `handout/`, and `.publishignore` keeps it out of this copy.
