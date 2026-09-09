# Exercise 2 — the weather map, as a uv project

A tkinter map of France showing the current weather at ten towns, from
Open-Meteo. The counterpart to [`../venv-and-pip/`](../venv-and-pip/): same API,
same language, environment managed by `uv` instead of `venv` and `pip`.

## What is here

The API layer:

- [`current_weather.py`](current_weather.py) — the live temperature and WMO
  weather code for one location, or for many in a single request. This is the
  forecast endpoint, not the archive one exercise 1 uses, and its parameter
  names differ.
- [`locations.py`](locations.py) — the ten places shown, as data. Adding a town
  is an edit here and nowhere else.

The map:

- [`france_map_image.py`](france_map_image.py) — fetches and caches the map
  image, and holds the geographic box its four edges correspond to.
- [`map_projection.py`](map_projection.py) — turns latitude and longitude into
  pixels on that image, which is interpolation and nothing more.
- [`canvas_labels.py`](canvas_labels.py) — stacked text on an opaque plate, so a
  reading stays legible over the map's own ink.
- [`weather_codes.py`](weather_codes.py) — the WMO code table, and the colour
  scale the dots and readings are painted with.
- [`weather_map.py`](weather_map.py) — the tkinter window itself.
- [`main.py`](main.py) — opens it.

Checks and environment:

- [`test_map.py`](test_map.py) and
  [`test_current_weather.py`](test_current_weather.py) — 23 tests. They assert
  what the module *asks the API for*, which is where Open-Meteo fails silently,
  and the projection's arithmetic. None touch the network.
- [`environment_check.ipynb`](environment_check.ipynb) — question 7's notebook.
- [`pyproject.toml`](pyproject.toml) + `uv.lock` — one declared dependency and
  the six packages it resolves to. Next door the same information is 119
  undifferentiated lines.

## The map image

`france_map.png` is **not committed**: the first run downloads it, and every run
after that reads the file. It is
[this map](https://commons.wikimedia.org/wiki/File:France_location_map-Regions_and_departements-2016.svg)
by Superbenjamin on Wikimedia Commons, under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), credited in the
window itself.

It is a Wikipedia *location map*, which is the only reason it can be drawn on:
Wikipedia publishes the
[geographic box](https://en.wikipedia.org/wiki/Module:Location_map/data/France)
its four edges correspond to, so turning a latitude and longitude into a pixel
is interpolation. The image and that box are one fact in two halves, and
changing either alone moves every town by the same silent amount, which is what
`test_the_image_has_the_shape_its_bounds_imply` exists to catch.

## Using it

`uv` needs no activation step: it checks the lockfile and the environment before
each run.

```console
$ uv run python main.py                        # opens the map
$ uv run pytest -q
.......................                                                  [100%]
23 passed in 0.05s
$ uv run --with jupyter jupyter lab            # question 7's notebook
```

Anything needing a location's live weather calls one function; ten locations
still cost one request.

```python
from current_weather import query_current_weather_at
from locations import FRANCE

for name, response in zip(FRANCE, query_current_weather_at(list(FRANCE.values()))):
    print(name, response["current"]["temperature_2m"])
```

## Reading further

How each question was worked through, and the reference behind each choice, is in
[`../steps/`](../steps/index.html). The concepts are explained in the Notes vault,
under `S7/Programming/TP - Python/TP1 - Environments and Packages`.
