"""
This module contains functions to query and process weather data from the Open-Meteo API.
"""
import json
from datetime import date
from typing import Any

import matplotlib.pyplot as plt
import requests
from matplotlib.axes import Axes

# A decoded Open-Meteo JSON response. Named so the signatures below say what
# they carry; `json` is a module, and mypy rejects it as an annotation.
WeatherResponse = dict[str, Any]

COORDINATES : dict[str, tuple[float, float]] = {
    "Grenoble": (45.183, 5.7245),
    "Paris": (48.8566, 2.3522),
    "Lyon": (45.764, 4.8357)
}

def query_open_meteo(latitude : float, longitude : float,
                     start_date : str, end_date : str) -> WeatherResponse:
    """Query the Open-Meteo API for weather data at the given latitude and
    longitude between the two dates."""
    #  Note: this is just a multiline string concatenation (to avoid very long lines)
    #        + fstrings (formatted strings) are used for easier variable insertion
    url = (f"https://archive-api.open-meteo.com/v1/archive"
           f"?latitude={latitude}&longitude={longitude}&current_weather=true"
           f"&start_date={start_date}&end_date={end_date}"
           "&daily=temperature_2m_max,temperature_2m_min,weathercode&timezone=auto")
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        data = response.json()
        return data
    # If we reach here, something went wrong
    raise RuntimeError(f"Error querying Open-Meteo API: {response.status_code}")

def extract_temperatures(data : WeatherResponse) -> tuple[list[str], list[float],list[float]]:
    """Process the weather data to extract daily maximum and minimum temperatures
    in the form of three lists: dates, minimum temperatures, maximum temperatures."""
    daily_data = data.get("daily", {})
    days = daily_data.get("time", [])
    min_temps = daily_data.get("temperature_2m_min", [])
    max_temps = daily_data.get("temperature_2m_max", [])
    return days, min_temps, max_temps


def plot_temperature(data : WeatherResponse, location_name : str = "",
                     ax : Axes | None = None) -> Axes:
    """Plot the daily minimum and maximum temperatures of an Open-Meteo archive response.

    `data` is a response from `query_open_meteo`; it must carry a "daily" block
    holding "time", "temperature_2m_min" and "temperature_2m_max" of equal length.
    `location_name` titles the plot, and falls back to the coordinates echoed
    back by the API. Draws on `ax` when one is given -- so a caller can compose
    several locations onto one figure -- and creates a new figure otherwise.
    Returns the Axes drawn on; showing or saving it is left to the caller.
    Raises ValueError when the response carries no daily temperatures.
    """
    days, min_temps, max_temps = extract_temperatures(data)
    if not days:
        raise ValueError("Response carries no daily temperature data")

    # Matplotlib registers a unit converter for datetime objects, which is what
    # puts real dates (not string labels) on the x axis and picks the ticks.
    dates = [date.fromisoformat(day) for day in days]

    if ax is None:
        _, ax = plt.subplots(figsize=(10, 5))

    # The API states its own units; reading them back beats hardcoding degrees.
    unit = data.get("daily_units", {}).get("temperature_2m_max", "")
    title_place = location_name or f"{data.get('latitude')}, {data.get('longitude')}"

    # Dates plot fine at runtime; matplotlib's stubs just do not describe the
    # unit converters yet -- matplotlib issue #27140.
    ax.plot(dates, max_temps, marker="o", label="Daily maximum")  # type: ignore[arg-type]
    ax.plot(dates, min_temps, marker="o", label="Daily minimum")  # type: ignore[arg-type]
    # A filled band reads as one daily range rather than two unrelated curves;
    # alpha keeps it from overpowering the lines it belongs to.
    ax.fill_between(dates, min_temps, max_temps,  # type: ignore[arg-type]
                    alpha=0.2, color="tab:grey", label="Daily range")

    ax.set_title(f"Daily temperatures -- {title_place}")
    ax.set_xlabel("Date")
    ax.set_ylabel(f"Temperature ({unit})" if unit else "Temperature")
    ax.legend()
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.figure.autofmt_xdate()  # date labels overlap unless rotated
    return ax


if __name__ == "__main__":
    # since the values of the coordinates in the COORDINATES dictionary
    # are tuples of (latitude, longitude), we need to unpack them when passing
    # them as arguments to the query_open_meteo function using the * operator
    grenoble_data = query_open_meteo(*COORDINATES["Grenoble"], "2025-12-01", "2025-12-15")
    print(json.dumps(grenoble_data, indent=4))
    plot_temperature(grenoble_data, "Grenoble")
    plt.show()
