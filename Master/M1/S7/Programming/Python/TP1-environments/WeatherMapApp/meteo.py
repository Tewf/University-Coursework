"""
Ask the Open-Meteo API for the weather, and pull the useful numbers out of its
answer.

This module never draws anything and never opens a window. It only deals with
the network and with dictionaries. That separation is deliberate: you can import
it from a plain script, from a Jupyter notebook, or from either of the two
windows in this folder, and it behaves the same way every time.

Run it directly to see what it gets:

    uv run python meteo.py
"""

import requests

from configuration import CITY_COORDINATES, OPEN_METEO_FORECAST_URL


def query_open_meteo(latitude: float | str, longitude: float | str) -> dict | list[dict]:
    """Ask Open-Meteo for the weather at one place, or at several at once.

    Args:
        latitude: A single latitude (45.18), OR several joined by commas
            ("45.18,48.85,43.29") to ask about many places in one go.
        longitude: The matching longitude, in the same format.

    Returns:
        What the API answered, already turned from JSON text into Python.
        Careful, the SHAPE changes with the number of places asked for:
          - one place  -> a dict
          - two or more -> a list of dicts, in the order you asked
        `fetch_city_temperatures` below shows how to cope with both.

    Raises:
        RuntimeError: if the API answers with anything other than 200 (OK).

    Example:
        >>> answer = query_open_meteo(45.183, 5.7245)      # Grenoble
        >>> answer["current"]["temperature_2m"]
        29.1
    """
    #  Note: this is just a multiline string concatenation (to avoid very long
    #        lines) + fstrings (formatted strings) for easier variable insertion.
    #
    #  What we are asking for:
    #    current = temperature_2m  -> the temperature RIGHT NOW, 2 m above ground
    #    daily   = ..._max/_min    -> the next seven days, for the graph
    #    timezone=auto             -> give me local times, not UTC
    url = (
        f"{OPEN_METEO_FORECAST_URL}?latitude={latitude}&longitude={longitude}"
        "&current=temperature_2m,weather_code"
        "&daily=temperature_2m_max,temperature_2m_min,weather_code&timezone=auto"
    )
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        data = response.json()
        return data
    # If we reach here, something went wrong
    raise RuntimeError(f"Error querying Open-Meteo API: {response.status_code}")


def extract_temperatures(data: dict) -> tuple[list[str], list[float], list[float]]:
    """Pull the day-by-day forecast out of one place's answer.

    We use .get() with a default everywhere instead of data["daily"], because
    .get() returns the default when the key is missing while [] would crash. An
    incomplete answer then gives empty lists, which the caller can test for.

    Args:
        data: The answer for ONE place (a dict, not the list).

    Returns:
        Three lists of the same length: the dates, the minimum temperatures,
        and the maximum temperatures.

    Example:
        >>> days, minimums, maximums = extract_temperatures(answer)
        >>> days[0], maximums[0]
        ('2026-09-02', 30.7)
    """
    daily_data = data.get("daily", {})
    days = daily_data.get("time", [])
    min_temps = daily_data.get("temperature_2m_min", [])
    max_temps = daily_data.get("temperature_2m_max", [])
    return days, min_temps, max_temps


def extract_current_temperature(data: dict) -> float:
    """Pull the single right-now temperature out of one place's answer.

    Args:
        data: The answer for ONE place (a dict, not the list).

    Returns:
        The temperature in degrees Celsius, measured 2 m above the ground.

    Raises:
        RuntimeError: if the answer carries no current temperature at all.

    Example:
        >>> extract_current_temperature(answer)
        30.7
    """
    current_data = data.get("current", {})
    temperature = current_data.get("temperature_2m")
    if temperature is None:
        raise RuntimeError("Open-Meteo returned no current temperature")
    return temperature


def fetch_city_temperatures(coordinates: dict[str, tuple[float, float]]) -> dict[str, float]:
    """Get the current temperature of every city, using ONE request for all of them.

    Why one request and not one per city? Because Open-Meteo accepts a whole
    list of coordinates at once, and asking twelve times in a row is twelve
    times slower for exactly the same answers (1.9 s against 0.2 s when this was
    measured). Being polite to a free API is also just good manners.

    Args:
        coordinates: Cities and their positions, shaped like CITY_COORDINATES.

    Returns:
        A dict of city name -> current temperature in Celsius, in the same
        order the cities were given.

    Raises:
        RuntimeError: if the API answers about a different number of places
            than we asked about.

    Example:
        >>> fetch_city_temperatures({"Lyon": (45.764, 4.8357)})
        {'Lyon': 29.3}
    """
    #  Step 1: turn {"Lyon": (45.76, 4.83), ...} into two strings the URL wants,
    #          "45.76,43.29,..." and "4.83,5.36,...". They must stay in step,
    #          which is why they are built in the same loop.
    city_names = []
    latitude_texts = []
    longitude_texts = []
    for city, position in coordinates.items():
        latitude, longitude = position
        city_names.append(city)
        latitude_texts.append(str(latitude))
        longitude_texts.append(str(longitude))

    joined_latitudes = ",".join(latitude_texts)
    joined_longitudes = ",".join(longitude_texts)

    #  Step 2: the one and only network call.
    answer = query_open_meteo(joined_latitudes, joined_longitudes)

    #  Step 3: one place comes back on its own rather than in a list, so wrap it
    #          to make the loop below work in both cases. Forgetting this is a
    #          nasty bug: looping over a dict gives you its KEYS, so the code
    #          would run happily and produce nonsense.
    if isinstance(answer, list):
        answers_per_city = answer
    else:
        answers_per_city = [answer]

    if len(answers_per_city) != len(city_names):
        raise RuntimeError(
            f"Asked about {len(city_names)} cities but got {len(answers_per_city)} answers"
        )

    #  Step 4: walk the two lists side by side. enumerate() gives us the position
    #          in the list as well as the name, and the positions match because
    #          the API answers in the order it was asked.
    temperatures = {}
    for index, city in enumerate(city_names):
        temperatures[city] = extract_current_temperature(answers_per_city[index])
    return temperatures


if __name__ == "__main__":
    #  A tiny self-test, so `uv run python meteo.py` shows the module working.
    for city_name, celsius in fetch_city_temperatures(CITY_COORDINATES).items():
        print(f"{city_name:<18} {celsius:5.1f} °C")
