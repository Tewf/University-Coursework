# Python TP1: Environments and packages

Virtual environments with venv and pip, then uv, then notebooks running against each. Built around a weather API.

## State

Questions 1 to 5 are done and verified; question 6 (the tkinter GUI) is the
deliberate stopping point, and 7 and 8 follow it. Both exercises pass the
checkers the handout recommends: `pylint` 10.00/10, `mypy` clean. Each
question's reasoning, what was rejected and the reference that settled it are
in [steps/](steps/index.html) — the abridged questions are listed there too.

## What the handout provides

`meteo.py`, unpacked from `provided-files.zip` and set up in place so this
folder reads as a working project rather than an archive beside a drop zone.
`plot_temperature` is implemented into it, which makes it derived work; the
archive stays for reference, the `provided-files/` wrapper it unpacked into
does not.

## Layout

The practical is two projects, because that is the comparison it is built
around: the same weather API reached through two different environment tools.

| Path | What it is |
|------|-----------|
| `meteo.py` | Exercise 1. Provided file, with `plot_temperature` implemented into it. |
| `requirements.txt` | Exercise 1's environment, frozen: 30 pinned lines for 5 packages asked for. |
| `WeatherMapApp/` | Exercise 2, a `uv` project: `pyproject.toml` + `uv.lock`. |
| `WeatherMapApp/current_weather.py` | The real-time query (question 5). |
| `WeatherMapApp/locations.py` | The cities the map will show, as data. |
| `WeatherMapApp/main.py` | Prints the current weather for each; the GUI is question 6. |

Neither `.venv/` is committed: both rebuild from the files above, which is the
claim the practical asks you to verify.

## Running it

Exercise 1 uses `venv` and `pip`, as the handout sets out — not the course's
conda environment, since the tooling is the subject here:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python meteo.py            # prints the JSON, then plots Grenoble
```

Exercise 2 uses `uv`, which needs no activation step:

```bash
cd WeatherMapApp
uv run python main.py      # current weather for ten French cities
uv run pylint *.py && uv run mypy .
```

## References used

Beyond the handout. Each is cited with its trail on the step page that used it.

| Reference | What it settled | Step |
|---|---|---|
| [PEP 668](https://peps.python.org/pep-0668/) | Why the system interpreter refuses `pip install` | 1 |
| matplotlib [`fill_between_demo.py`](https://github.com/matplotlib/matplotlib/blob/v3.11.1/galleries/examples/lines_bars_and_markers/fill_between_demo.py) | The filled band, and lightening it with `alpha` | 2 |
| matplotlib [`ticks/date.py`](https://github.com/matplotlib/matplotlib/blob/v3.11.1/galleries/examples/ticks/date.py) | Why a date axis needs no configuring | 2 |
| matplotlib [`quick_start.py`](https://github.com/matplotlib/matplotlib/blob/v3.11.1/galleries/users_explain/quick_start.py) | The optional-`ax` helper signature | 2 |
| matplotlib [#27140](https://github.com/matplotlib/matplotlib/issues/27140) | The stub gap the `type: ignore` comments name | 2 |
| [`pip freeze`](https://pip.pypa.io/en/stable/cli/pip_freeze/) | What a freeze does and does not claim | 3 |
| [uv projects guide](https://docs.astral.sh/uv/guides/projects/) | What `uv init` generates, what to commit | 4 |
| [Open-Meteo docs](https://open-meteo.com/en/docs) | The forecast endpoint and `current=` | 5 |
| [requests quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/) | `params=` and `raise_for_status()` | 5 |

The three matplotlib examples were read from upstream source at the exact
installed tag, v3.11.1, because matplotlib.org refuses automated fetches.

## Where the explanation lives

This folder holds code. The concept note for it is in the Notes vault, under
`S7/Programming/TP - Python/TP1 - Environments and Packages.md`. The map of all of them is
`obsidian-note.local.md` at the course root, which is gitignored because it
names local paths.

## Source material

The handout is by E. Foussard (UGA) and is **not redistributed here**: see
[NOTICE](../../../../../../NOTICE). It sits in `handout/`, the PDF beside the `.txt`
extraction that makes it greppable, and `.gitignore` keeps that whole directory
out of the repository. The code the handout provides is listed above and is
credited in NOTICE.
