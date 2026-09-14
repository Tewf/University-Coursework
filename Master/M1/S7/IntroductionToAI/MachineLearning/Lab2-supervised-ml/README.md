# Lab2: Supervised learning with SVMs and trees

A short SVM warm-up on synthetic blobs, then avalanche prediction from real
weather and snow data with SVMs, decision trees and random forests.

## State

Not started. All fourteen questions are pending. Each question's reasoning,
what was rejected and the reference that settled it are in
[steps/](steps/index.html), where the abridged questions are listed too.

## What the handout provides

`handout/` holds the subject notebook and the staff's own worked solution. The
lab root also carries the avalanche dataset as a CSV, the two reference
figures the subject points at, and the archive they were unpacked from.

## Running it

One conda environment serves every lab, declared in `../../environment.yml`:

```bash
conda env create -f ../../environment.yml
conda activate m1ai-intro-ai
```

Then copy the subject out of `handout/` and open the copy — the copy is what
gets committed, `handout/` never changes:

```bash
cp handout/Lab2-supervised-ml.ipynb .
jupyter lab Lab2-supervised-ml.ipynb
```

## Where the explanation lives

This folder holds code. The concept note for it is in the Notes vault, under
`S7/Introduction to AI/Labs - Machine Learning/Lab 2 - Supervised ML/Lab 2 - Supervised ML.md`.
The map of all of them is `obsidian-note.local.md`, two levels up, which is
gitignored because it names local paths.

## Source material

The lab notebook, its official solution, and the dataset it loads are by
Nguyen Kim Thang (UGA) and are not redistributed here: see
[NOTICE](../../../../../../NOTICE). `handout/` and the dataset both stay local,
and `.publishignore` keeps them out of the public repository.
