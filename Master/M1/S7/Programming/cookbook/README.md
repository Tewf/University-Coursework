# Cookbook

Patterns from this course's practicals, kept in a form that survives an exam:
**every file runs on its own, imports nothing from the others, and marks the
lines worth copying.**

## How to use it

Each file is bracketed like this:

```python
# ---------------------------------------------------------------- THE PATTERN
def fetch_json(...):
    ...
# -------------------------------------------------------------- END OF PATTERN
```

Copy what is between the two lines. Below them there is always a
`if __name__ == "__main__":` block that runs the pattern on real data, so you
can check the file still works before trusting it:

```bash
conda activate m1ai-programming
python fetch_json.py
```

Nothing here imports anything else here on purpose. A shared `utils.py` is
better engineering and worse for an exam: it turns "copy 20 lines" into "copy
the right 20 lines from the right three files".

## What is here

| I need to... | Open | The function |
|---|---|---|
| Ask a web API for data | [fetch_json.py](fetch_json.py) | `fetch_json(url, params)` |
| Get a value out of the answer | [read_json.py](read_json.py) | `dig(data, "a", "b")` |
| Draw one or more series | [plot_lines.py](plot_lines.py) | `plot_lines(x, {"label": y})` |

## The three traps these encode

Each of these cost real time in TP1, which is why they are written down rather
than remembered.

**Build query strings with `params=`, never an f-string.** `requests` escapes
what needs escaping and joins with `?` and `&` correctly. An f-string URL
breaks the first time a value contains a space or an accent.

**One attempt is not enough.** While writing TP1 this API returned a 502 and
timed out twice in ten minutes. A script with `timeout=10` and no retry fails
in front of whoever is marking it, which is why `fetch_json` retries three
times with a growing wait.

**Use `fig, ax = plt.subplots()`.** The `plt.plot()` shortcut draws into a
hidden current figure, so plotting twice in one script silently stacks both
charts into one image.

## Scope

Web and plotting only, because that is what TP1 actually produced. Patterns for
images, the command line and logging belong here too once TP2, TP3 and TP4 have
been done and there is something proven to copy. Writing them before then would
be guessing at what those practicals need.

## References

What each choice rests on. Where a source says something stronger than the
comment in the file, the source is what to believe.

| Claim | Source |
|---|---|
| `params=` builds the query string and escapes it, so an f-string URL is the wrong tool | requests, [Passing Parameters In URLs](https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls) |
| every request needs a `timeout` | requests, [Timeouts](https://requests.readthedocs.io/en/latest/user/quickstart/#timeouts): "Nearly all production code should use this parameter in nearly all requests", and "If no timeout is specified explicitly, requests do not time out" |
| check the status *before* trusting `.json()` | requests, [JSON Response Content](https://requests.readthedocs.io/en/latest/user/quickstart/#json-response-content): "the success of the call to `r.json()` does **not** indicate the success of the response" |
| one `except requests.RequestException` catches every failure mode | requests, [Errors and Exceptions](https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions): all its exceptions inherit from it |
| what `plt.plot()` actually does | Matplotlib, [Application Interfaces](https://matplotlib.org/stable/users/explain/figure/api_interfaces.html): the implicit pyplot interface "keeps track of the last Figure and Axes created, and adds Artists to the object it thinks the user wants" |
| …and why to prefer `fig, ax = plt.subplots()` here | Matplotlib, [Quick start guide](https://matplotlib.org/stable/users/explain/quick_start.html): "we suggest using the OO style, particularly for complicated plots, and functions and scripts that are intended to be reused as part of a larger project" — which is what this folder is |
| the archive endpoint, its parameters, and the `daily` object of parallel arrays | Open-Meteo, [Historical Weather API](https://open-meteo.com/en/docs/historical-weather-api) |

**Open-Meteo** is free for non-commercial use and needs no API key; its data
comes from ERA5 and ERA5-Land via the Copernicus Climate Change Service, and
the API asks to be cited rather than merely used.

Reading is half of it. The retry loop is not in any of those documents: it is
here because this API answered with a 502 and timed out twice while TP1 was
being written. Every file in this folder was run before being committed, and
`fetch_json.py` was run against the live API.
