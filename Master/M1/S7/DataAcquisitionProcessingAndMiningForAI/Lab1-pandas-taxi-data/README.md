# Lab1: pandas on New York taxi data

A 200 000-row Parquet sample of January 2025 Yellow Taxi trips, worked from
first load to a bar chart of demand by hour.

## State

Not started. All nine exercises are pending. Each exercise's reasoning, what was
rejected and the reference that settled it are in [steps/](steps/index.html),
where the abridged exercises are listed too.

## What the handout provides

`handout/` holds the subject notebook, with the `...` placeholders left to fill.
`data/raw/taxi_2025_01_sample.parquet` is the dataset it reads; the notebook
points at it by a relative path, so it stays where it was shipped.

## Running it

The course's one conda environment, declared in the staff's `environment.yml`
in the setup bundle:

```bash
conda env create -f ../Setup/handout/environment.yml
conda activate datacq
```

Then copy the subject out of `handout/` and open the copy — the copy is what
gets committed, `handout/` never changes:

```bash
cp handout/lab1.ipynb Lab1-pandas-taxi-data.ipynb
jupyter lab Lab1-pandas-taxi-data.ipynb
```

The notebook resolves `DATA` against its own location. Opened at the lab root
rather than at the depth the Moodle bundle used, that relative path needs
adjusting to `data/raw/taxi_2025_01_sample.parquet` — the first cell says as
much.

## Where the explanation lives

This folder holds code. The concepts it needs — columnar storage and Parquet,
boolean masking, split-apply-combine, and why a mean and a median disagree on
skewed data — are notes in the Notes vault, one per concept.

## Source material

The subject notebook and the taxi sample are the course staff's and are not
redistributed here: see [NOTICE](../../../../../NOTICE). Both stay on disk,
in `handout/` and `data/`, and `.publishignore` keeps them out of the public repository.
