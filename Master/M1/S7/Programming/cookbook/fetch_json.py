"""Ask a web API for JSON and get a dict back.

Run it to see it work:

    python fetch_json.py
"""

import time

import requests

# ---------------------------------------------------------------- THE PATTERN
#  Copy from here to the end of the function. It is the whole recipe.


def fetch_json(url: str, params: dict, retries: int = 3) -> dict:
    """GET a URL with query parameters and return the parsed JSON.

    Args:
        url: The address, WITHOUT a "?" or any parameters glued on.
        params: The query parameters. requests turns {"a": 1} into "?a=1"
            and escapes anything that needs escaping, which is why you should
            never build the URL with an f-string yourself.
        retries: How many times to try before giving up. Public APIs return
            502 and time out often enough that one attempt is not enough.

    Returns:
        The answer, already turned from JSON text into Python.

    Raises:
        requests.HTTPError: if the server kept refusing after every attempt.
    """
    for attempt in range(retries):
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()  # turns 404, 502... into an exception
            return response.json()
        except requests.RequestException:
            #  The last attempt is allowed to fail loudly; earlier ones wait
            #  and try again, a little longer each time.
            if attempt == retries - 1:
                raise
            time.sleep(2 * (attempt + 1))
    raise RuntimeError("unreachable")


# -------------------------------------------------------------- END OF PATTERN


if __name__ == "__main__":
    #  Open-Meteo needs no API key, which makes it a good thing to test against.
    weather = fetch_json(
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
    print("top-level keys:", list(weather))
    print("days returned: ", len(weather["daily"]["time"]))
