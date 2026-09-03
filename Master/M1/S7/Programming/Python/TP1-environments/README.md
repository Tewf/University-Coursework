# TP1 — Managing Environments and Packages

Two exercises on Open-Meteo's free weather API, where the real subject is the
tooling: `venv` and `pip` first, then `uv`, then notebooks against both.

## What is where

| File | Is |
|---|---|
| [meteo.py](meteo.py) | Exercise 1 — fetch past weather and plot it (Q1, Q2) |
| [venv-and-pip/](venv-and-pip/) | The `venv` + `pip` half: the frozen `requirements.txt` (Q3) and its notebook (Q8) |
| [uv-project/](uv-project/) | The same project managed by `uv` (Q4) and its notebook (Q7) |
| [WeatherMapApp/](WeatherMapApp/README.md) | Exercise 2 — real-time weather on a map of France (Q5, Q6) |
| `provided-files/` | The subject's own starter code, kept unmodified for comparison |

Both halves are kept rather than merged: the point of the practical is that the
same project can be managed two ways, and that is only visible side by side.

## Running it

```bash
conda activate m1ai-programming
python meteo.py
```

Or in either of the two environments the practical builds:

```bash
cd venv-and-pip && python3 -m venv .venv && ./.venv/bin/pip install -r requirements.txt
cd uv-project   && uv run python ../meteo.py
```

## Question 3, which is the one worth re-reading

Freezing an environment is easy; the question is whether the frozen file
actually rebuilds it. The cycle, and what it proved:

```bash
python3 -m venv .venv                       # 1. create
./.venv/bin/pip install requests matplotlib # 2. install what meteo.py imports
./.venv/bin/pip freeze > requirements.txt   # 3. freeze
rm -rf .venv                                # 4. destroy
python3 -m venv .venv                       # 5. recreate
./.venv/bin/pip install -r requirements.txt #    from the file alone
./.venv/bin/python meteo.py                 # 6. still works: 15 days fetched
```

**`pip freeze` inside a conda environment produces a file that installs
nowhere.** The first attempt at this folder was frozen from a conda env, so
every line came out as `numpy @ file:///home/conda/feedstock_root/...` — a path
to a build directory that exists on no machine, including this one after a
rebuild. `pip freeze` records where a package *came from*, and for conda
packages that is a local path. This is specified behaviour, not a bug:
[PEP 610](https://peps.python.org/pep-0610/) says tools like `pip freeze`
"SHOULD exploit `direct_url.json` if it is present, and give it priority over
the Version metadata in order to generate a higher fidelity output". Higher
fidelity here means a path that exists on exactly one machine. Freeze from a
real `venv`, or the file is decoration.

## Questions 7 and 8, the notebooks

Both notebooks print `sys.executable` before anything else. That single line is
what actually answers the question: if the path is not the environment you meant,
the kernel is attached elsewhere and every successful import below proves
nothing.

```
venv-and-pip/.venv/bin/python      ← Q8
uv-project/.venv/bin/python3       ← Q7
```

The `uv` half needed `uv add --dev ipykernel` for that path to be the project's
own environment. Without it, `uv run --with jupyter` builds a throwaway
environment in `~/.cache/uv/` and the notebook reports *that* path instead —
which looks like it worked and does not show what the question asks about.
uv's own [Jupyter guide](https://docs.astral.sh/uv/guides/integration/jupyter/)
says the same: `uv run --with jupyter` "runs in an isolated environment", and
reaching the project's packages means installing `ipykernel` as a development
dependency and registering a kernel from it.

## Type checking

The subject recommends `mypy`, and the starter code does not pass it: it
annotates two functions with `-> json`, where `json` is a module, not a type.
Corrected to `-> dict`, which takes `mypy meteo.py` from three errors to clean.

## Reusable pieces

[patterns.py](patterns.py) is the three steps this practical is really about --
ask an API, read its answer, draw it -- written the way they should be written
once you know what goes wrong, rather than the way the starter code writes them.
Copy between a `THE PATTERN` marker and its `END`; run the file to check it
still works first.

Its docstring carries the four traps and the page that backs each one, so the
reasoning sits next to the code instead of in a document that drifts from it.
The retry loop is marked as having no source on purpose: it is not in any
documentation, it is there because this API answered with a 502 and timed out
twice while this practical was being written.
