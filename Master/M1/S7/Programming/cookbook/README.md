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
