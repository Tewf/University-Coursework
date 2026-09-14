# Exercise 2 — the weather map, as a uv project

A tkinter map of France showing the current temperature in ten towns, from
Open-Meteo. The counterpart to [`../venv-and-pip/`](../venv-and-pip/): same API,
same language, environment managed by `uv` instead of `venv` and `pip`.

## What is here

- [`main.py`](main.py) — the whole program. Fetch the map picture, ask the API
  for every town at once, write each answer at the pixel that town sits on.
- [`test_main.py`](test_main.py) — 8 tests. None opens a window or touches the
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
"Paris": Town(495, 232, 48.8566, 2.3522),
#             x    y   latitude  longitude
```

The right pair goes to Open-Meteo. The left pair is where the answer is drawn.
Nothing in the program converts one into the other, which is the whole reason
there is no projection code.

## Changing what it shows

Adding a town is one line in `TOWNS`. To get its `x` and `y`, convert its
degrees with the box this picture is published with, which `main.py` repeats
above the table:

```python
x = (longitude - -5.8) / (10.0 - -5.8) * 960
y = (51.5 - latitude)  / (51.5 - 41.0) * 923
```

Latitude subtracts the other way round because pixels count down the screen
while degrees count up the globe. You do not have to trust your arithmetic:
`test_each_pixel_matches_the_coordinates_beside_it` recomputes every row and
fails if a pixel and its coordinates disagree by more than one pixel. That test
is the reason hand-written pixels are safe to add.

Two towns closer than about a hundred kilometres will overlap each other's
labels at this size. That is why Lyon and Nice are absent: they sit on top of
Grenoble and Marseille.

The pixels describe *this* picture at *this* size. `main.py` checks the image is
960×923 when it loads and stops with a message saying what to do if it is not,
because failing on the first line beats placing ten towns wrongly and looking
plausible.

Colours, fonts, the dot size and the label spacing are named constants under the
table, meant to be edited on sight.

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
........                                                                   [100%]
8 passed in 0.05s
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

The concepts are explained in the Notes vault, under
`S7/Programming/TP - Python/TP1 - Environments and Packages`.
