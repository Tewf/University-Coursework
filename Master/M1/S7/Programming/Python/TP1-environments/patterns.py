"""The three things TP1 turned out to be about, in a form worth copying later.

`meteo.py` is the answer to the practical. This file is the same three steps --
ask an API, read its answer, draw it -- written the way they should be written
once you know what goes wrong. Copy from a THE PATTERN marker to its END.

Run it to check it still works before trusting it:

    conda activate m1ai-programming
    python patterns.py

THE THREE TRAPS, and what says so
---------------------------------
1. Build a query string with `params=`, never an f-string. requests escapes
   what needs escaping and joins with ? and & correctly.
   https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls

2. Always pass `timeout`, and do not trust one attempt. requests: "Nearly all
   production code should use this parameter in nearly all requests", and
   without one "requests do not time out" at all.
   https://requests.readthedocs.io/en/latest/user/quickstart/#timeouts
   The retry loop below is in no document. It is here because this API answered
   with a 502 and timed out twice while TP1 was being written.

3. Check the status BEFORE trusting .json(). requests: "the success of the call
   to r.json() does not indicate the success of the response".
   https://requests.readthedocs.io/en/latest/user/quickstart/#json-response-content
   One `except requests.RequestException` covers every failure it raises.
   https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions

4. Draw through `fig, ax = plt.subplots()`. The implicit pyplot interface
   "keeps track of the last Figure and Axes created, and adds Artists to the
   object it thinks the user wants", so plotting twice stacks both into one
   image. Matplotlib suggests the OO style for "functions and scripts that are
   intended to be reused as part of a larger project".
   https://matplotlib.org/stable/users/explain/figure/api_interfaces.html
   https://matplotlib.org/stable/users/explain/quick_start.html

The API: https://open-meteo.com/en/docs/historical-weather-api -- free for
non-commercial use, no API key, ERA5 via the Copernicus Climate Change Service,
and it asks to be cited rather than merely used.
"""

import time
from typing import Any

import matplotlib.pyplot as plt
import requests


# ------------------------------------------------------- THE PATTERN: fetch
def fetch_json(url: str, params: dict, retries: int = 3) -> dict:
    """GET a URL with query parameters and return the parsed JSON."""
    for attempt in range(retries):
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()  # turns 404, 502... into an exception
            return response.json()
        except requests.RequestException:
            if attempt == retries - 1:  # the last try is allowed to fail loudly
                raise
            time.sleep(2 * (attempt + 1))
    raise RuntimeError("unreachable")
# ------------------------------------------------------------------- END


# --------------------------------------------------------- THE PATTERN: read
def dig(data: Any, *keys: str, default: Any = None) -> Any:
    """Follow a path of keys down a nested dict, stopping safely if it breaks.

    >>> dig({"daily": {"time": ["2025-12-01"]}}, "daily", "time")
    ['2025-12-01']
    """
    current = data
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current
# ------------------------------------------------------------------- END


# --------------------------------------------------------- THE PATTERN: plot
def plot_lines(
    x_values: list,
    series: dict[str, list[float]],
    title: str = "",
    x_label: str = "",
    y_label: str = "",
    save_to: str | None = None,
) -> None:
    """Draw every series in `series` against the same x-axis."""
    fig, ax = plt.subplots(figsize=(8, 4))
    for label, values in series.items():
        ax.plot(x_values, values, marker="o", label=label)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.grid(True, alpha=0.3)
    if len(series) > 1:
        ax.legend()  # a legend for one line just repeats the title
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
    fig.tight_layout()  # stops the rotated labels being cut off
    if save_to:
        fig.savefig(save_to, dpi=150)
        plt.close(fig)  # forgetting this leaks figures in a loop
    else:
        plt.show()
# ------------------------------------------------------------------- END


if __name__ == "__main__":
    answer = fetch_json(
        "https://archive-api.open-meteo.com/v1/archive",
        {
            "latitude": 45.183,
            "longitude": 5.7245,
            "start_date": "2025-12-01",
            "end_date": "2025-12-15",
            "daily": "temperature_2m_max,temperature_2m_min",
            "timezone": "auto",
        },
    )
    days = dig(answer, "daily", "time", default=[])
    highs = dig(answer, "daily", "temperature_2m_max", default=[])
    lows = dig(answer, "daily", "temperature_2m_min", default=[])
    print(f"{len(days)} days, coldest night {min(lows)} C")

    plot_lines(
        days,
        {"Maximum": highs, "Minimum": lows},
        title="Grenoble, first half of December 2025",
        x_label="Date",
        y_label="Temperature (°C)",
        save_to="patterns_demo.png",
    )
    print("wrote patterns_demo.png")
