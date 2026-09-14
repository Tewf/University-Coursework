# Car sequencing, several instance sizes

Solve the car-sequencing instances Caseine provides, sequencing cars on a line so that no option's per-window occupancy ratio is exceeded, comparing a reified-IfThen formulation against an Element formulation across instances from 10 up to 100 cars.

The statement points at the course's CP exercise sheet for the problem description rather than restating it here.

## State

Not started. The question is pending.

## What is provided

- `handout/10-car-sequencing.md` — the original Caseine statement, wording untouched
- `car_seq_solver.py` — `CarSeqSolver`, the CP model class, with some methods left to fill in
- `car_seq_instance.py` — `CarSeqInstance`, reads a `.car` file and checks a candidate solution
- `executable.py` — runs the solver over the instance files, one instance uncommented by default
- `configExe` — the Caseine grader config, names `executable.py`
- `instances/*.car` — seven Ford car-sequencing benchmark instances, 10 to 100 cars

## Running it

One conda environment for the whole subject, declared once in
[environment.yml](../../environment.yml):

```bash
conda env create -f ../../environment.yml
conda activate operations_research
```

Then:

```bash
python executable.py
```

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`. The map is `obsidian-note.local.md`, two levels up.

## Source material

The statement is a Caseine VPL exercise (Hadrien Cambazard) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays local in `handout/`, and `.publishignore` keeps it out of the public repository.
