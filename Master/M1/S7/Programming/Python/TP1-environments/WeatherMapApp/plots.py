"""
Draw the map and the graph with Matplotlib.

Only the Matplotlib version of the window uses this file. The pure-tkinter
version (weather_map_tkinter.py) deliberately draws everything itself, so that
you can compare the two ways of doing the same job.

Every function here takes an `axes` to draw ON, rather than making its own
figure. That is the habit to get into: it lets the same drawing code end up in a
pop-up window, inside a Tkinter app, or saved straight to a PNG, without
changing a line.

    uv run python plots.py        # saves a PNG you can open
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.patches import PathPatch

from configuration import (
    CITY_COORDINATES,
    MAXIMUM_LATITUDE,
    MAXIMUM_LONGITUDE,
    MINIMUM_LATITUDE,
    MINIMUM_LONGITUDE,
    OUTSIDE_FRANCE_COLOUR,
)
from france_border import load_border_path
from temperature_map import build_grid, interpolate


def label_cities(axes: Axes, temperatures: dict[str, float]):
    """Put a dot and a "name temperature" label on each city.

    Args:
        axes: The Matplotlib axes to draw on.
        temperatures: City name -> temperature in Celsius.
    """
    middle_longitude = (MINIMUM_LONGITUDE + MAXIMUM_LONGITUDE) / 2

    for city, temperature in temperatures.items():
        latitude, longitude = CITY_COORDINATES[city]
        axes.plot(longitude, latitude, "k.", zorder=3)

        #  Write the name towards the MIDDLE of the map. Two reasons: a name on
        #  the outside edge would run off the picture (Brest, Strasbourg), and
        #  two cities at the same latitude would otherwise write on top of each
        #  other (Clermont-Ferrand and Lyon).
        if longitude < middle_longitude:
            sideways_shift = 5
            alignment = "left"
        else:
            sideways_shift = -5
            alignment = "right"

        axes.annotate(
            f"{city} {temperature:.0f}°",
            (longitude, latitude),
            textcoords="offset points",
            xytext=(sideways_shift, 3),
            horizontalalignment=alignment,
            fontsize=8,
            zorder=3,
        )


def draw_temperature_map(axes: Axes, temperatures: dict[str, float], with_labels: bool = True):
    """Draw France, coloured by the interpolated temperature.

    Args:
        axes: The Matplotlib axes to draw on.
        temperatures: City name -> current temperature in Celsius.
        with_labels: Set to False to leave the city names off, which is what the
            Matplotlib window does when it plans to draw them itself as Tkinter
            canvas items on top.

    Example:
        >>> from matplotlib.figure import Figure
        >>> figure = Figure()
        >>> draw_temperature_map(figure.add_subplot(), {"Lyon": 29.3})
        >>> figure.savefig("map.png")
    """
    longitudes, latitudes = build_grid()
    field = axes.imshow(
        interpolate(temperatures, longitudes, latitudes),
        #  imshow normally numbers pixels 0, 1, 2...; `extent` tells it to use
        #  our degrees instead, so everything else can be placed in degrees too.
        extent=(MINIMUM_LONGITUDE, MAXIMUM_LONGITUDE, MINIMUM_LATITUDE, MAXIMUM_LATITUDE),
        #  Images are normally drawn top row first, but our grid starts at the
        #  SOUTH, so without this France would come out upside down.
        origin="lower",
        cmap="RdYlBu_r",
        interpolation="bilinear",
        #  A weighted average never leaves the range of its inputs, so these two
        #  numbers are the exact span of the picture -- no colour is wasted.
        vmin=min(temperatures.values()),
        vmax=max(temperatures.values()),
    )

    #  The coloured square becomes France: clip it to the border, then draw the
    #  border itself on top so the coastline is a crisp line.
    border = load_border_path()
    field.set_clip_path(border, transform=axes.transData)
    axes.add_patch(PathPatch(border, facecolor="none", edgecolor="#333333", linewidth=0.6))
    axes.set_facecolor(OUTSIDE_FRANCE_COLOUR)
    axes.get_figure().colorbar(field, ax=axes, label="Temperature now (°C)")

    if with_labels:
        label_cities(axes, temperatures)

    #  One degree of longitude is only cos(latitude) as wide as one of latitude,
    #  so without this France comes out visibly squashed sideways.
    middle_latitude = (MINIMUM_LATITUDE + MAXIMUM_LATITUDE) / 2
    axes.set_aspect(1 / np.cos(np.radians(middle_latitude)))
    axes.set_xlim(MINIMUM_LONGITUDE, MAXIMUM_LONGITUDE)
    axes.set_ylim(MINIMUM_LATITUDE, MAXIMUM_LATITUDE)
    axes.set_xlabel("Longitude (°)")
    axes.set_ylabel("Latitude (°)")
    axes.set_title("Temperature across France, right now")


def plot_temperatures(days: list[str], min_temps: list[float], max_temps: list[float]):
    """Plot the minimum and maximum temperatures over time.

    Kept from Exercise 1, unchanged in how you call it. It opens its own window,
    so use it from a script or a notebook -- NOT from inside the Tkinter app,
    where two window systems would fight over the same event loop.

    Example:
        >>> from meteo import query_open_meteo, extract_temperatures
        >>> answer = query_open_meteo(45.183, 5.7245)
        >>> plot_temperatures(*extract_temperatures(answer))
    """
    fig, ax = plt.subplots()  # Create a figure containing a single Axes.
    ax.plot(days, min_temps, marker="o", label="Minimum Temperature")
    ax.plot(days, max_temps, marker="o", label="Maximum Temperature")
    ax.set_xlabel("Date")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Weather Data")
    ax.legend()
    plt.show()


if __name__ == "__main__":
    from matplotlib.figure import Figure

    from meteo import fetch_city_temperatures

    figure = Figure(figsize=(8, 7.5), layout="constrained")
    draw_temperature_map(figure.add_subplot(), fetch_city_temperatures(CITY_COORDINATES))
    figure.savefig("map_preview.png", dpi=110)
    print("written to map_preview.png")
