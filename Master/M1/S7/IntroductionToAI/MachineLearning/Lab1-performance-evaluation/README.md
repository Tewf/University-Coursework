# Lab1: Classifier performance evaluation

Three classifiers and three baselines on the breast-cancer dataset, scored and ranked with scikit-learn's evaluation metrics.

## State

Not started. All eleven questions are pending.

## What the handout provides

`handout/` holds the subject notebook and the staff's own worked solution. The
dataset itself is scikit-learn's bundled breast-cancer set, so nothing else is
provided.

## Running it

One conda environment serves every lab, declared in `../../environment.yml`:

```bash
conda env create -f ../../environment.yml
conda activate m1ai-intro-ai
```

Then copy the subject out of `handout/` and open the copy — the copy is what
gets committed, `handout/` never changes:

```bash
cp handout/Lab1-performance-evaluation.ipynb .
jupyter lab Lab1-performance-evaluation.ipynb
```

## Where the explanation lives

This folder holds code. The concept note for it is in the Notes vault, under
`S7/Introduction to AI/Labs - Machine Learning/Lab 1 - Performance Evaluation.md`.
The map of all of them is `obsidian-note.local.md`, two levels up, which is
gitignored because it names local paths.

## Source material

The lab notebook and its official solution are by Nguyen Kim Thang (UGA) and
are not redistributed here: see [NOTICE](../../../../../../NOTICE). Both sit in
`handout/`, and `.publishignore` keeps that directory out of the public repository.
