"""
The weather map, version 2 of 2: Tkinter draws all of it, on its own.

No Matplotlib picture is borrowed here. The colours are mixed by hand
(colour_scale.py), painted pixel by pixel into a Tkinter image (map_image.py),
and the coastline and cities are put on the canvas with create_line,
create_oval and create_text.

It has no zoom and it took longer to write, but nothing is hidden. If you want
to understand how a map gets from degrees onto a screen, read this one; if you
want the same map with less code, read weather_map_matplotlib.py.

    uv run python weather_map_tkinter.py
"""

import tkinter as tk
from tkinter import messagebox

from configuration import (
    CITY_COORDINATES,
    MAP_HEIGHT_PIXELS,
    MAP_MARGIN_PIXELS,
    MAXIMUM_LONGITUDE,
    MINIMUM_LONGITUDE,
)
from france_border import load_border_rings
from map_image import COLOUR_STEPS, build_map_image, build_palette
from map_projection import MAP_WIDTH_PIXELS, degrees_to_pixels
from meteo import fetch_city_temperatures

WINDOW_TITLE = "Weather Map — pure Tkinter"

#  Room under the map for the colour scale and its two end labels.
LEGEND_HEIGHT_PIXELS = 46
LABEL_FONT = ("TkDefaultFont", 8)


def draw_border(canvas: tk.Canvas):
    """Trace the coastline and the land borders, one closed loop at a time."""
    for ring in load_border_rings():
        if len(ring) < 2:
            continue  # create_line needs at least two points to draw anything

        #  create_line wants one flat list -- x1, y1, x2, y2, ... -- not pairs.
        flat_points = []
        for longitude, latitude in ring:
            x, y = degrees_to_pixels(longitude, latitude)
            flat_points.append(x)
            flat_points.append(y)
        canvas.create_line(flat_points, fill="#333333", width=1)


def draw_cities(canvas: tk.Canvas, temperatures: dict[str, float]):
    """Put a dot and a "name temperature" label on each city.

    This is what Question 6 is really asking for: create_oval and create_text
    make real OBJECTS on the canvas, each with an id, which can be moved,
    recoloured or deleted later. A flat picture cannot do any of that.
    """
    middle_longitude = (MINIMUM_LONGITUDE + MAXIMUM_LONGITUDE) / 2

    for city, temperature in temperatures.items():
        latitude, longitude = CITY_COORDINATES[city]
        x, y = degrees_to_pixels(longitude, latitude)

        #  create_oval takes the corners of the box the circle fits inside, so a
        #  dot of radius 3 around (x, y) is the box (x-3, y-3) to (x+3, y+3).
        radius = 3
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="black")

        #  Write the name towards the middle of the map: a name on the outer edge
        #  would fall off the canvas, and Clermont-Ferrand and Lyon sit at the
        #  same latitude, so they would otherwise write over each other. Anchor
        #  "w" holds the text by its West (left) edge so it runs rightwards.
        if longitude < middle_longitude:
            sideways_shift = 6
            anchor = "w"
        else:
            sideways_shift = -6
            anchor = "e"

        canvas.create_text(
            x + sideways_shift,
            y - 6,
            text=f"{city} {temperature:.0f}°",
            anchor=anchor,
            font=LABEL_FONT,
        )


def draw_colour_scale(canvas: tk.Canvas, coldest: float, hottest: float):
    """Draw the cold-to-hot strip under the map, so the colours mean something.

    A picture of a temperature without its scale is decoration, not data.
    """
    strip_top = MAP_MARGIN_PIXELS + MAP_HEIGHT_PIXELS + 14
    strip_bottom = strip_top + 14
    palette = build_palette(coldest, hottest)

    #  One thin vertical line per pixel of width, each a step further along.
    for offset in range(MAP_WIDTH_PIXELS):
        step = round(offset / (MAP_WIDTH_PIXELS - 1) * (COLOUR_STEPS - 1))
        x = MAP_MARGIN_PIXELS + offset
        canvas.create_line(x, strip_top, x, strip_bottom, fill=palette[step])

    label_y = strip_bottom + 10
    canvas.create_text(
        MAP_MARGIN_PIXELS, label_y, text=f"{coldest:.1f} °C", anchor="w", font=LABEL_FONT
    )
    canvas.create_text(
        MAP_MARGIN_PIXELS + MAP_WIDTH_PIXELS,
        label_y,
        text=f"{hottest:.1f} °C",
        anchor="e",
        font=LABEL_FONT,
    )


def build_window() -> tk.Tk:
    """Build the window: fetch the weather, then draw the map onto a canvas."""
    window = tk.Tk()
    window.title(WINDOW_TITLE)

    try:
        #  requests' own errors all descend from OSError, so these two names
        #  between them cover a broken network as well as a refusing API.
        temperatures = fetch_city_temperatures(CITY_COORDINATES)
        #  Note the order: the Tk window has to exist before a PhotoImage can.
        image = build_map_image(temperatures)
    except (RuntimeError, OSError) as error:
        messagebox.showerror(WINDOW_TITLE, f"Could not build the map:\n{error}")
        window.destroy()
        raise

    canvas = tk.Canvas(
        window,
        width=MAP_WIDTH_PIXELS + 2 * MAP_MARGIN_PIXELS,
        height=MAP_HEIGHT_PIXELS + 2 * MAP_MARGIN_PIXELS + LEGEND_HEIGHT_PIXELS,
        background="white",
        highlightthickness=0,
    )
    canvas.pack()

    canvas.create_image(MAP_MARGIN_PIXELS, MAP_MARGIN_PIXELS, image=image, anchor="nw")
    draw_border(canvas)
    draw_cities(canvas, temperatures)
    draw_colour_scale(canvas, min(temperatures.values()), max(temperatures.values()))
    canvas.create_text(
        MAP_MARGIN_PIXELS,
        MAP_MARGIN_PIXELS - 12,
        text="Temperature across France, right now",
        anchor="w",
    )

    #  Tkinter does not keep images alive by itself: if the only reference to it
    #  is a local variable, Python frees it the moment this function returns and
    #  the map goes blank. Parking it on the canvas object keeps it alive.
    canvas.map_image = image
    return window


if __name__ == "__main__":
    build_window().mainloop()
