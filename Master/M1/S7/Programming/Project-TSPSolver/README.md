# Project: TSP solver

The Travelling Salesman Problem, solved exactly and then approximately, and the
two measured against each other.

## State

Not started. Each question's reasoning, what was rejected and the reference
that settled it are in [steps/](steps/index.html), where the abridged
questions are listed too.

## What the handout provides

Unpacked in place, so this folder reads as a working project rather than an
archive beside a drop zone. Neither is redistributed here — see Source
material below.

- `instance_generator.py`
- `TSP-instances.zip`, unpacked into `TSP-instances/coord/` and
  `TSP-instances/lower_diag/`

## Running it

Nothing to run yet: no build script or sources exist. Once written, a single
`bash build-TSPsolver.sh` at the project root is meant to produce
`build/TSPsolver` — taking an instance path, an output path, and an optional
method flag — and `build/tests`.

## Where the explanation lives

This folder holds code. The concept note for it is in the Notes vault, under
`S7/Programming/Project - TSP Solver/Project - TSP Solver.md`. The map of all
of them is `obsidian-note.local.md` at the course root, which is gitignored
because it names local paths.

## Done with a partner

This folder is also the work tree of a private repository shared with a
partner, where nothing is ignored: the handout, the data and the work live
there in full, and what appears here is the subset the repository's
allowlist names. The mechanism is [private-projects/](../../../private-projects/README.md)
at the M1 level.

## Source material

The subject and `instance_generator.py` are by E. Foussard (UGA) and are **not
redistributed here**: see [NOTICE](../../../../../NOTICE). It sits in
`handout/`, the PDF beside the `.txt` extraction that makes it greppable, and
`.gitignore` keeps that whole directory, `instance_generator.py`, and
`TSP-instances/` out of the repository. The TSPLIB instances themselves belong
to their original authors and are cited, not claimed.
