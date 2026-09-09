"""Turn Open-Meteo's numeric weather and temperature values into things to read.

The table is the WMO weather interpretation codes (WW) as Open-Meteo publishes
them; the API returns the number and documents nothing else about it. Codes the
table groups on one row ("1, 2, 3: Mainly clear, partly cloudy, and overcast")
are split into one entry each, which is how they arrive.
"""

WMO_DESCRIPTIONS : dict[int, str] = {
    0: "Clear sky",
    1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 48: "Depositing rime fog",
    51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
    56: "Light freezing drizzle", 57: "Dense freezing drizzle",
    61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
    66: "Light freezing rain", 67: "Heavy freezing rain",
    71: "Slight snowfall", 73: "Moderate snowfall", 75: "Heavy snowfall",
    77: "Snow grains",
    80: "Slight rain showers", 81: "Moderate rain showers", 82: "Violent rain showers",
    85: "Slight snow showers", 86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail", 99: "Thunderstorm with heavy hail",
}

# Upper bound in degrees Celsius, and the colour for everything below it. Read in
# order, so the first bound a temperature falls under wins. Tunable on sight:
# these are display thresholds, not meteorology.
TEMPERATURE_COLOURS : list[tuple[float, str]] = [
    (0.0, "#4A6FA5"), (10.0, "#5B9BB5"), (16.0, "#5EA37E"),
    (22.0, "#B4820E"), (28.0, "#C97A3B"), (float("inf"), "#C63B3B"),
]


def describe(code : int) -> str:
    """Return the WMO code's meaning, or a readable placeholder for a new code."""
    return WMO_DESCRIPTIONS.get(code, f"WMO code {code}")


def temperature_colour(celsius : float) -> str:
    """Return the hex colour standing for a temperature on the map."""
    for upper_bound, colour in TEMPERATURE_COLOURS:
        if celsius < upper_bound:
            return colour
    return TEMPERATURE_COLOURS[-1][1]
