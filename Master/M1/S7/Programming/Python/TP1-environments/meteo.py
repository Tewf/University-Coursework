"""
This module contains functions to query and process weather data from the Open-Meteo API.
"""

import json

import matplotlib.pyplot as plt
import requests

COORDINATES: dict[str, tuple[float, float]] = {
    "Grenoble": (45.183, 5.7245),
    "Paris": (48.8566, 2.3522),
    "Lyon": (45.764, 4.8357),
}


def query_open_meteo(
    latitude: float, longitude: float, start_date: str, end_date: str
) -> json:
    """Query the Open-Meteo API for weather data at the given latitude and longitude between the two dates."""
    #  Note: this is just a multiline string concatenation (to avoid very long lines)
    #        + fstrings (formatted strings) are used for easier variable insertion
    url = (
        f"https://archive-api.open-meteo.com/v1/archive?latitude={latitude}&longitude={longitude}"
        f"&current_weather=true&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,"
        "temperature_2m_min,weathercode&timezone=auto"
    )
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        data = response.json()
        return data
    # If we reach here, something went wrong
    raise RuntimeError(f"Error querying Open-Meteo API: {response.status_code}")


def extract_temperatures(data: json) -> tuple[list[str], list[float], list[float]]:
    """Process the weather data to extract daily maximum and minimum temperatures in the form of three lists: dates, minimum temperatures, maximum temperatures."""
    daily_data = data.get("daily", {})
    days = daily_data.get("time", [])
    min_temps = daily_data.get("temperature_2m_min", [])
    max_temps = daily_data.get("temperature_2m_max", [])
    return days, min_temps, max_temps


def plot_temperatures(days: list[str], min_temps: list[float], max_temps: list[float]):
    """Plot the minimum and maximum temperatures over time."""
    fig, ax = plt.subplots()  # Create a figure containing a single Axes.
    ax.plot(days, min_temps, label="Minimum Temperature")
    ax.plot(days, max_temps, label="Maximum Temperature")
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Weather Data")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    # since the values of the coordinates in the COORDINATES dictionary
    # are tuples of (latitude, longitude), we need to unpack them when passing
    # them as arguments to the query_open_meteo function using the * operator
    grenoble_data = query_open_meteo(
        COORDINATES["Grenoble"][0],
        COORDINATES["Grenoble"][1],
        "2025-12-01",
        "2025-12-15",
    )
    print(json.dumps(grenoble_data, indent=4))
    plot_temperatures(*extract_temperatures(grenoble_data))
