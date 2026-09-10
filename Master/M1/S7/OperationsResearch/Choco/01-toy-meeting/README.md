# Toy meeting scheduling

Look at the CP model already built for this problem in OPL, then run the given pychoco version to see the same model in pychoco's syntax: four one-hour meetings scheduled between 8h and 13h under two deadlines, one ordering constraint, and one spaced-gap constraint.

This is a worked introductory example to run and read, not a model to write from scratch.

## State

Not started. The question is pending. Its reasoning, what was rejected and the reference that settles it will be in [steps/](steps/index.html), where the abridged statement is listed too.

## What is provided

- `handout/01-toy-meeting.md` — the original Caseine statement, wording untouched
- `toy_meeting.py` — `ToyMeetingChoco`, a worked model and solve for the introductory example
- `extended_toy_meeting.py` — `ExtToyMeetingChoco`, the same model with full solution enumeration, a checker and solver statistics
- `main.py` — runs the two classes above

## Running it

One conda environment for the whole subject, declared once in
[environment.yml](../../environment.yml):

```bash
conda env create -f ../../environment.yml
conda activate operations_research
```

Then:

```bash
python main.py
```

## Where the explanation lives

Not here: the concept notes for Operations Research live in the Notes vault, under `S7/Operations Research/`. The map is `obsidian-note.local.md`, two levels up.

## Source material

The statement is a Caseine VPL exercise (course staff) and is not redistributed here: see [NOTICE](../../../../../../NOTICE). It stays local in `handout/`, and `.gitignore` keeps it out of the repository.
