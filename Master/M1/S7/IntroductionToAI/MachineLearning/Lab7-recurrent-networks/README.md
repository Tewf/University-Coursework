# Lab7: Recurrent networks for time-series prediction

Predicting building humidity from the CUBEMS sensor data with a hand-built
RNN and LSTM, one step ahead and then several.

## State

Not started. All five questions are pending. Each question's reasoning, what
was rejected and the reference that settled it are in [steps/](steps/index.html),
where the abridged questions are listed too.

## What the handout provides

`handout/` holds the subject notebook only. The lab root also carries a
windowing-and-training helper module, the CUBEMS humidity data as a CSV, and
the archive it was unpacked from.

## Running it

One conda environment serves every lab, declared in `../../environment.yml`:

```bash
conda env create -f ../../environment.yml
conda activate m1ai-intro-ai
```

Then copy the subject out of `handout/` and open the copy — the copy is what
gets committed, `handout/` never changes:

```bash
cp handout/Lab7-recurrent-networks.ipynb .
jupyter lab Lab7-recurrent-networks.ipynb
```

## Where the explanation lives

This folder holds code. The concept note for it is in the Notes vault, under
`S7/Introduction to AI/Labs - Machine Learning/Lab 7 - Deep Learning/Lab 7 - Deep Learning.md`.
The map of all of them is `obsidian-note.local.md`, two levels up, which is
gitignored because it names local paths.

## Source material

The lab notebook and its helper module are by Nguyen Kim Thang (UGA) and are
not redistributed here: see [NOTICE](../../../../../../NOTICE). `handout/` and
the helper both stay local, and `.publishignore` keeps them out of the public repository.
