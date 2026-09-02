"""
Turn a handful of measured city temperatures into a temperature for every point
on the map.

We only ever know the weather in twelve places, but the map has 90 000 squares.
The gap is filled by INTERPOLATION: each square takes a weighted average of all
twelve cities, where a nearby city counts for a lot and a distant one counts for
almost nothing.

No drawing happens here, and no network either -- this module is pure
arithmetic, which is what makes it usable by both windows in this folder.

    uv run python temperature_map.py
"""

import numpy as np

from configuration import (
    CITY_COORDINATES,
    INFLUENCE_SPREAD_DEGREES,
    MAP_GRID_RESOLUTION,
    MAXIMUM_LATITUDE,
    MAXIMUM_LONGITUDE,
    MINIMUM_LATITUDE,
    MINIMUM_LONGITUDE,
)


def build_grid(
    columns: int = MAP_GRID_RESOLUTION, rows: int | None = None
) -> tuple[np.ndarray, np.ndarray]:
    """Lay a regular grid of points over the map rectangle.

    np.linspace(a, b, n) makes n numbers evenly spaced from a to b. np.meshgrid
    then crosses the two axes so that, for every square of the map, we have both
    its longitude and its latitude.

    Args:
        columns: How many points from west to east.
        rows: How many from south to north. Left out, it matches `columns` and
            you get a square grid. The Tkinter window passes the pixel width and
            height of its canvas here, so that one grid point is one pixel.

    Returns:
        Two 2-D arrays shaped (rows, columns): all the longitudes, and all the
        latitudes. Note the order -- rows first, the way images are measured.

    Example:
        >>> longitudes, latitudes = build_grid(columns=4)
        >>> longitudes.shape
        (4, 4)
        >>> build_grid(columns=760, rows=680)[0].shape
        (680, 760)
    """
    if rows is None:
        rows = columns
    longitude_axis = np.linspace(MINIMUM_LONGITUDE, MAXIMUM_LONGITUDE, columns)
    latitude_axis = np.linspace(MINIMUM_LATITUDE, MAXIMUM_LATITUDE, rows)
    return np.meshgrid(longitude_axis, latitude_axis)


def interpolate(
    temperatures: dict[str, float],
    longitudes: np.ndarray,
    latitudes: np.ndarray,
) -> np.ndarray:
    """Estimate the temperature everywhere on the grid, from the cities we know.

    The recipe, for one square of the map:

      1. measure the distance d from that square to each city;
      2. give each city the weight  w = exp(-d^2 / (2 * spread^2))  -- the bell
         curve, worth 1 at the city itself and fading fast with distance;
      3. answer  (sum of w * temperature) / (sum of w).

    Step 3 is a WEIGHTED AVERAGE, and dividing by the total weight is what makes
    it one. It also guarantees the result can never be colder than the coldest
    city nor hotter than the hottest -- handy, because it means the colour scale
    can be pinned to those two numbers and be exactly right.

    The loop below runs once per CITY, not once per square: every line inside it
    works on the whole 300 x 300 grid at once. That is what numpy is for, and it
    is roughly a thousand times faster than writing two nested Python loops over
    the squares.

    Args:
        temperatures: City name -> temperature, as fetch_city_temperatures gives.
        longitudes: The 2-D grid of longitudes from build_grid.
        latitudes: The matching 2-D grid of latitudes.

    Returns:
        A 2-D array of temperatures, the same shape as the grid.

    Example:
        >>> longitudes, latitudes = build_grid(columns=100)
        >>> field = interpolate({"Lyon": 29.3, "Brest": 19.8}, longitudes, latitudes)
        >>> round(float(field.min()), 1), round(float(field.max()), 1)
        (19.8, 29.3)
    """
    #  Two accumulators, both starting at zero and both the shape of the grid.
    #  zeros_like copies the shape of an existing array, so we do not have to
    #  repeat "300 by 300" anywhere.
    weighted_sum = np.zeros_like(longitudes)
    total_weight = np.zeros_like(longitudes)

    for city, temperature in temperatures.items():
        latitude, longitude = CITY_COORDINATES[city]

        #  Squared distance, so no square root is needed: the bell curve wants
        #  d^2 anyway. This is Pythagoras, applied to every square at once.
        squared_distance = (longitudes - longitude) ** 2 + (latitudes - latitude) ** 2
        weight = np.exp(-squared_distance / (2 * INFLUENCE_SPREAD_DEGREES**2))

        weighted_sum = weighted_sum + weight * temperature
        total_weight = total_weight + weight

    return weighted_sum / total_weight


if __name__ == "__main__":
    from meteo import fetch_city_temperatures

    measured = fetch_city_temperatures(CITY_COORDINATES)
    grid_longitudes, grid_latitudes = build_grid()
    estimated = interpolate(measured, grid_longitudes, grid_latitudes)
    print(f"measured in {len(measured)} cities: {min(measured.values())} .. {max(measured.values())} °C")
    print(f"estimated on {estimated.size} points: {estimated.min():.1f} .. {estimated.max():.1f} °C")
