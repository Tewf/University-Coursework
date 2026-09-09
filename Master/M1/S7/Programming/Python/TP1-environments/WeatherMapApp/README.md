# Exercise 2 — the weather map, as a uv project

A tkinter map of France showing the current weather at ten cities, from
Open-Meteo. The counterpart to [`../venv-and-pip/`](../venv-and-pip/): same API,
same language, environment managed by `uv` instead of `venv` and `pip`.

## What is here

The API layer:

- [`current_weather.py`](current_weather.py) — the live temperature and WMO
  weather code for one location, or for many in a single request. This is the
  forecast endpoint, not the archive one exercise 1 uses, and its parameter
  names differ.
- [`locations.py`](locations.py) — the ten places shown, as data. Adding a city
  is an edit here and nowhere else.

The map:

- [`france_outline.py`](france_outline.py) — reads the coastline rings out of the
  GeoJSON file.
- [`map_projection.py`](map_projection.py) — turns latitude and longitude into
  canvas pixels, narrowing longitude by the cosine of the mid-latitude so France
  is not drawn too wide.
- [`weather_codes.py`](weather_codes.py) — the WMO code table, and the colour
  scale the dots are painted with.
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

`france_border.geojson` is **not committed**: it is downloaded, not written here.
`france_outline.py` says so with the exact command if it is missing.

```bash
curl -sSLo france_border.geojson \
  https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/metropole-version-simplifiee.geojson
```

It is IGN Admin Express via [gregoiredavid/france-geojson](https://github.com/gregoiredavid/france-geojson),
published under the [Licence ouverte](https://www.etalab.gouv.fr/licence-ouverte-open-licence/),
which allows reuse with attribution.

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
