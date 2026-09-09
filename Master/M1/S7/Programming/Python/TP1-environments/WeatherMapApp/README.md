# Exercise 2 — the weather map, as a uv project

Real-time weather for several places at once, from Open-Meteo. The counterpart to
[`../venv-and-pip/`](../venv-and-pip/): same API, same language, environment
managed by `uv` instead of `venv` and `pip`. Question 6 puts the results on a
tkinter canvas; that part is not written yet.

## What is here

- [`current_weather.py`](current_weather.py) — `query_current_weather(lat, lon)`
  returns the live temperature and WMO weather code. This is the forecast
  endpoint, not the archive one exercise 1 uses, and its parameter names differ.
- [`locations.py`](locations.py) — the ten places the map will show, as data.
  Adding a city is an edit here and nowhere else.
- [`main.py`](main.py) — prints the current weather for each of them.
- [`test_current_weather.py`](test_current_weather.py) — seven tests. They assert
  what the module *asks the API for*, which is the part that fails silently when
  a parameter name is wrong, and they never touch the network.
- [`pyproject.toml`](pyproject.toml) + `uv.lock` — one declared dependency, and
  the exact six packages it resolves to. Compare with exercise 1's flat
  `requirements.txt`, which cannot tell the two apart.

## Using it

`uv` needs no activation step: it checks the lockfile and the environment before
each run.

```console
$ uv run python main.py
Brest          17.8 degC   WMO code 3   at 2026-09-09T14:30
Lille          18.4 degC   WMO code 1   at 2026-09-09T14:30
Strasbourg     19.8 degC   WMO code 3   at 2026-09-09T14:30
...
$ uv run pytest -q
.......                                                                  [100%]
7 passed in 0.04s
```

Anything that needs a location's live weather calls one function:

```python
from current_weather import query_current_weather

now = query_current_weather(45.183, 5.7245)["current"]
print(now["temperature_2m"], now["weather_code"])
```

## Reading further

How each question was worked through, and the reference behind each choice, is in
[`../steps/`](../steps/index.html). The concepts are explained in the Notes vault,
under `S7/Programming/TP - Python/TP1 - Environments and Packages`.
