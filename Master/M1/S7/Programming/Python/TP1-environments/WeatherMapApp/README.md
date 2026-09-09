# Exercise 2 — the weather map, as a uv project

A tkinter map of France showing the current temperature in ten towns, from
Open-Meteo. The counterpart to [`../venv-and-pip/`](../venv-and-pip/): same API,
same language, environment managed by `uv` instead of `venv` and `pip`.

## What is here

- [`main.py`](main.py) — the whole program. Fetch the map picture, ask the API
  for every town at once, write each answer at the pixel that town sits on.
- [`test_main.py`](test_main.py) — 6 tests. None opens a window or touches the
  network; the one that cares about the request replaces `requests.get` with a
  stub and reads what it was handed.
- [`environment_check.ipynb`](environment_check.ipynb) — question 7's notebook.
- [`pyproject.toml`](pyproject.toml) + `uv.lock` — one declared dependency and
  the six packages it resolves to. Next door the same information is 119
  undifferentiated lines.

## How a town gets on the map

One table holds each town twice: where it is on the picture, and where it is on
Earth.

```python
"Paris": (495, 232, 48.8566, 2.3522),
```

The pair on the right goes to Open-Meteo. The pair on the left is where the
answer is drawn. Nothing in the program converts one into the other, which is
the whole reason there is no projection code.

The pixels were not measured by eye. They were computed once from the
[geographic box](https://en.wikipedia.org/wiki/Module:Location_map/data/France)
Wikipedia publishes for this image, then written into the table. That is also
their limit: they describe *this* picture at *this* size, so `main.py` checks
the image is 960×923 on load and stops with a clear message if it is not.
Adding a town means finding its pixel, which is the price of not carrying a
projection.

## The map image

`france_map.png` is **not committed**: the first run downloads it, and every run
after that is offline. It is
[this map](https://commons.wikimedia.org/wiki/File:France_location_map-Regions_and_departements-2016.svg)
by Superbenjamin on Wikimedia Commons, under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), credited in the
window itself.

## Using it

`uv` needs no activation step: it checks the lockfile and the environment before
each run.

```console
$ uv run python main.py                        # opens the map
$ uv run pytest -q
......                                                                   [100%]
6 passed in 0.05s
$ uv run --with jupyter jupyter lab            # question 7's notebook
```

Ten towns cost one request, because Open-Meteo takes comma-separated coordinate
lists and answers in the order asked.

```python
from main import TOWNS, fetch_temperatures

for name, celsius in zip(TOWNS, fetch_temperatures()):
    print(name, celsius)
```

## Reading further

How each question was worked through, and the reference behind each choice, is in
[`../steps/`](../steps/index.html). The concepts are explained in the Notes vault,
under `S7/Programming/TP - Python/TP1 - Environments and Packages`.
