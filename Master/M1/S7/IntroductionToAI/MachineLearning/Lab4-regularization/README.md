# Lab4: Regularized regression for IBD prediction

Predicting a patient's inflammatory-bowel-disease status from gut-microbe
abundances, where descriptors outnumber patients roughly five to one.

## State

Not started. All ten questions are pending (the last one optional). Each
question's reasoning, what was rejected and the reference that settled it are
in [steps/](steps/index.html), where the abridged questions are listed too.

## What the handout provides

`handout/` holds the subject notebook only — this lab has no official
solution. The lab root also carries the microbial-abundance table, the status
labels, and the archive they were unpacked from.

## Running it

One conda environment serves every lab, declared in `../../environment.yml`:

```bash
conda env create -f ../../environment.yml
conda activate m1ai-intro-ai
```

Then copy the subject out of `handout/` and open the copy — the copy is what
gets committed, `handout/` never changes:

```bash
cp handout/Lab4-regularization.ipynb .
jupyter lab Lab4-regularization.ipynb
```

## Where the explanation lives

This folder holds code. The concept note for it is in the Notes vault, under
`S7/Introduction to AI/Labs - Machine Learning/Lab 4 - Regularization/Lab 4 - Regularization.md`.
The map of all of them is `obsidian-note.local.md`, two levels up, which is
gitignored because it names local paths.

## Source material

The lab notebook and the dataset it loads are by Nguyen Kim Thang (UGA) and
are not redistributed here: see [NOTICE](../../../../../../NOTICE). `handout/`
and the dataset both stay local, and `.gitignore` keeps them out of the
repository.
