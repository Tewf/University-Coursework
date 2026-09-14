# Lab3: Unsupervised learning on digit images

k-means clustering on handwritten digits, then PCA and t-SNE, and why
clustering noisy high-dimensional data needs dimensionality reduction first.

## State

Not started. All eight questions are pending.

## What the handout provides

`handout/` holds the subject notebook and the staff's own worked solution. The
digit images are scikit-learn's bundled dataset, so nothing else is provided.

## Running it

One conda environment serves every lab, declared in `../../environment.yml`:

```bash
conda env create -f ../../environment.yml
conda activate m1ai-intro-ai
```

Then copy the subject out of `handout/` and open the copy — the copy is what
gets committed, `handout/` never changes:

```bash
cp handout/Lab3-unsupervised-learning.ipynb .
jupyter lab Lab3-unsupervised-learning.ipynb
```

## Where the explanation lives

This folder holds code. The concept note for it is in the Notes vault, under
`S7/Introduction to AI/Labs - Machine Learning/Lab 3 - Unsupervised Learning.md`.

## Source material

The lab notebook and its official solution are by Nguyen Kim Thang (UGA) and
are not redistributed here: see [NOTICE](../../../../../../NOTICE). Both sit in
`handout/`, and `.publishignore` keeps that directory out of this copy.
