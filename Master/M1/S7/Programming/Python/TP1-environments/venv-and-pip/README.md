# Exercise 1 — venv and pip

Past weather for a location, fetched from Open-Meteo and plotted. The subject is
the environment around it: this half is built with the standard library's `venv`
and `pip`, and [`../WeatherMapApp/`](../WeatherMapApp/) is the same idea built
with `uv`, so the two can be read side by side.

## What is here

- [`meteo.py`](meteo.py) — the practical. `query_open_meteo` asks the archive API,
  `extract_temperatures` pulls the three daily series out of the response, and
  `plot_temperature` draws them. The first two came with the handout.
- [`test_meteo.py`](test_meteo.py) — nine tests, one per clause of a docstring.
  No network: the fixture is a trimmed real response, and `requests.get` is
  replaced by a stand-in.
- [`conftest.py`](conftest.py) — selects matplotlib's `Agg` backend before any
  test imports it, which is why the tests need no display.
- [`requirements.txt`](requirements.txt) — the environment, frozen. 34 pinned
  lines for the six packages actually asked for.

`.venv/` is not committed; the point of the file above is that it does not need
to be.

## Using it

```console
$ python3 -m venv .venv && source .venv/bin/activate
$ pip install -r requirements.txt
$ python -m pytest -q
.........                                                                [100%]
9 passed in 0.24s
$ python meteo.py            # prints the JSON, then opens the plot
```

`plot_temperature` is written to be reused rather than only run: give it an Axes
and it draws there instead of making its own figure, so several locations compose
onto one plot, and it returns the Axes without calling `show()`.

```python
from matplotlib.figure import Figure
from meteo import COORDINATES, query_open_meteo, plot_temperature

axes = Figure().add_subplot()
for city in ("Grenoble", "Lyon"):
    data = query_open_meteo(*COORDINATES[city], "2025-12-01", "2025-12-15")
    plot_temperature(data, city, ax=axes)
axes.figure.savefig("december.png")
```

## Reading further

How each question was worked through, and the reference behind each choice, is in
[`../steps/`](../steps/index.html). The concepts are explained in the Notes vault,
under `S7/Programming/TP - Python/TP1 - Environments and Packages`.
