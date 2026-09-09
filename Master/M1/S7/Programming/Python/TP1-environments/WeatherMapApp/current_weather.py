"""Query the Open-Meteo forecast API for the weather happening right now."""
from typing import Any

import requests

# A decoded Open-Meteo JSON response.
WeatherResponse = dict[str, Any]

# Endpoint and variables kept as constants: the forecast API is a different host
# from the archive one used in exercise 1, and the variable list is the only
# thing a caller wanting more than temperature and sky state has to change.
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
CURRENT_VARIABLES = ("temperature_2m", "weather_code")
REQUEST_TIMEOUT_SECONDS = 10


def query_current_weather(latitude : float, longitude : float) -> WeatherResponse:
    """Query the Open-Meteo forecast API for the current weather at a location.

    Returns the decoded JSON response, whose "current" block holds "time",
    "temperature_2m" and "weather_code" (a WMO code), and whose "current_units"
    block states the unit of each. Timezone resolution is left to the API, so
    "time" is local to the coordinates asked about.
    Raises requests.HTTPError if the API answers with an error status, and
    requests.Timeout if it does not answer within REQUEST_TIMEOUT_SECONDS.
    """
    # requests builds and percent-encodes the query string from `params`, which
    # is why nothing here concatenates a URL by hand.
    # Annotated because a mixed float/str literal infers as dict[str, object],
    # which requests' stubs reject.
    params : dict[str, float | str] = {
        "latitude": latitude,
        "longitude": longitude,
        "current": ",".join(CURRENT_VARIABLES),
        "timezone": "auto",
    }
    response = requests.get(FORECAST_URL, params=params,
                            timeout=REQUEST_TIMEOUT_SECONDS)
    response.raise_for_status()
    return response.json()
