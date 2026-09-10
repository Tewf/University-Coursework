# Lab5: From linear regression to CNNs in PyTorch

Hitters salaries by linear and Lasso regression, then a hand-written PyTorch
training loop, first on FashionMNIST and then on CIFAR-10.

## State

Not started. All six questions are pending. Each question's reasoning, what
was rejected and the reference that settled it are in [steps/](steps/index.html),
where the abridged questions are listed too.

## What the handout provides

`handout/` holds the subject notebook only. The lab root also carries a
training-and-plotting helper module, a `data/` folder with the Hitters salary
table, and the archive it was unpacked from; the notebook downloads
FashionMNIST and CIFAR-10 into `data/` on first run, which is why that whole
directory is gitignored.

## Running it

One conda environment serves every lab, declared in `../../environment.yml`:

```bash
conda env create -f ../../environment.yml
conda activate m1ai-intro-ai
```

Then copy the subject out of `handout/` and open the copy — the copy is what
gets committed, `handout/` never changes:

```bash
cp handout/Lab5-deep-learning.ipynb .
jupyter lab Lab5-deep-learning.ipynb
```

## Where the explanation lives

This folder holds code. The concept note for it is in the Notes vault, under
`S7/Introduction to AI/Labs - Machine Learning/Lab 5 - Deep Learning/Lab 5 - Deep Learning.md`.
The map of all of them is `obsidian-note.local.md`, two levels up, which is
gitignored because it names local paths.

## Source material

The lab notebook and its training helper are by Nguyen Kim Thang (UGA) and are
not redistributed here: see [NOTICE](../../../../../../NOTICE). `handout/` and
the helper both stay local, and `.gitignore` keeps them out of the repository.
