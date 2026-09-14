# Lab6: Fine-tuning a pretrained ResNet18

Turning an ImageNet-pretrained ResNet18 into an object detector for VOC
images, by training a classifier-and-regressor head on top of its features.

## State

Not started, and it cannot run yet as shipped: the subject imports two Python
modules and loads three saved tensors that were never distributed with it, so
the folder holds only the subject until they turn up. All five questions are
pending. Each question's reasoning, what was rejected and the reference that
settled it are in [steps/](steps/index.html), where the abridged questions are
listed too.

## What the handout provides

`handout/` holds the subject notebook, and nothing else: the two Python
modules it imports and the three saved tensors it loads are missing from what
the staff distributed.

## Running it

One conda environment serves every lab, declared in `../../environment.yml`:

```bash
conda env create -f ../../environment.yml
conda activate m1ai-intro-ai
```

Copying the subject out of `handout/` is the same first step as every other
lab, but running it further needs the missing modules and tensors above:

```bash
cp handout/Lab6-fine-tuning.ipynb .
jupyter lab Lab6-fine-tuning.ipynb
```

## Where the explanation lives

This folder holds code. The concept note for it is in the Notes vault, under
`S7/Introduction to AI/Labs - Machine Learning/Lab 6 - Fine-Tuning a Pretrained Model.md`.
The map of all of them is `obsidian-note.local.md`, two levels up, which is
gitignored because it names local paths.

## Source material

The lab notebook is by Nguyen Kim Thang (UGA) and is not redistributed here:
see [NOTICE](../../../../../../NOTICE). It sits in `handout/`, and
`.publishignore` keeps that directory out of the public repository.
