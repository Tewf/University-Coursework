"""
The weather map, version 1 of 2: Matplotlib draws it, Tkinter shows it.

Matplotlib produces the picture (the smooth colours, the coastline, the colour
bar), we hand that picture to a real tkinter.Canvas with create_image, and then
we place the city dots and their temperatures ON TOP as ordinary canvas items.

So the canvas really is a tkinter.Canvas, and the pretty drawing is still done
by the tool that is good at it. Compare with weather_map_tkinter.py, which
refuses Matplotlib's help and draws every pixel itself.

    uv run python weather_map_matplotlib.py
"""

import base64
import tkinter as tk
from io import BytesIO
from tkinter import messagebox

from matplotlib.figure import Figure

from configuration import CITY_COORDINATES, MAXIMUM_LONGITUDE, MINIMUM_LONGITUDE
from meteo import fetch_city_temperatures
from plots import draw_temperature_map

WINDOW_TITLE = "Weather Map — Matplotlib"

#  7.6 inches at 100 dots per inch makes an image exactly 760 pixels wide. Keeping
#  those two numbers tied together is what lets us convert degrees into canvas
#  pixels further down without a fudge factor.
FIGURE_SIZE_INCHES = (7.6, 7.8)
FIGURE_DOTS_PER_INCH = 100


def render_map_image(temperatures: dict[str, float]) -> tuple[tk.PhotoImage, Figure, object]:
    """Draw the map with Matplotlib and turn it into an image Tkinter can show.

    Tkinter cannot display a Matplotlib figure directly, so the figure is saved
    to a PNG *in memory* (a BytesIO, which behaves like a file but never touches
    the disk) and handed to PhotoImage.

    Args:
        temperatures: City name -> current temperature in Celsius.

    Returns:
        The image, plus the figure and axes it came from -- we need those two to
        work out where each city landed in the picture.
    """
    figure = Figure(figsize=FIGURE_SIZE_INCHES, dpi=FIGURE_DOTS_PER_INCH, layout="constrained")
    axes = figure.add_subplot()
    #  with_labels=False: the names are drawn later, as canvas items instead.
    draw_temperature_map(axes, temperatures, with_labels=False)

    memory_file = BytesIO()
    #  Save at the figure's own dpi, and do NOT crop with bbox_inches="tight":
    #  cropping would shift everything and break the coordinates below.
    figure.savefig(memory_file, format="png", dpi=FIGURE_DOTS_PER_INCH)

    #  PhotoImage wants the PNG as base64 text rather than raw bytes.
    image = tk.PhotoImage(data=base64.b64encode(memory_file.getvalue()))
    return image, figure, axes


def degrees_to_pixels(figure: Figure, axes, longitude: float, latitude: float) -> tuple[float, float]:
    """Find where a longitude/latitude ended up in the rendered picture.

    Matplotlib already knows this: `axes.transData` is the very transformation
    it used to place things, so we borrow it instead of re-deriving the maths.

    The one catch is that Matplotlib counts pixels UPWARDS from the bottom-left,
    while Tkinter counts them DOWNWARDS from the top-left, so the vertical
    coordinate has to be flipped.

    Args:
        figure: The figure that was rendered.
        axes: The axes the map was drawn on.
        longitude: Degrees east (negative for west).
        latitude: Degrees north.

    Returns:
        The (x, y) position in canvas pixels.
    """
    x, y = axes.transData.transform((longitude, latitude))
    return x, figure.bbox.height - y


def draw_cities_on_canvas(canvas: tk.Canvas, figure: Figure, axes, temperatures: dict[str, float]):
    """Draw one dot and one label per city, as Tkinter canvas items.

    This is the part Q6 is really about: create_oval and create_text put real
    objects on the canvas. They can be moved, recoloured or deleted later by
    their id, which is something a flat picture cannot do.
    """
    middle_longitude = (MINIMUM_LONGITUDE + MAXIMUM_LONGITUDE) / 2

    for city, temperature in temperatures.items():
        latitude, longitude = CITY_COORDINATES[city]
        x, y = degrees_to_pixels(figure, axes, longitude, latitude)

        #  create_oval takes the corners of the box the circle fits in, so a dot
        #  of radius 3 around (x, y) means the box (x-3, y-3) to (x+3, y+3).
        radius = 3
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="black")

        #  Write the name towards the middle of the map, for the same two reasons
        #  as in plots.py: names on the outside edge would fall off the picture,
        #  and Clermont-Ferrand and Lyon share a latitude. "w" anchors the text
        #  by its West (left) edge so it runs rightwards; "e" runs leftwards.
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
            font=("TkDefaultFont", 8),
        )


def build_window() -> tk.Tk:
    """Build the window: fetch the weather, draw the map, place it on a canvas."""
    window = tk.Tk()
    window.title(WINDOW_TITLE)

    try:
        #  requests' own errors all descend from OSError, so these two names
        #  between them cover a broken network as well as a refusing API.
        temperatures = fetch_city_temperatures(CITY_COORDINATES)
        image, figure, axes = render_map_image(temperatures)
    except (RuntimeError, OSError) as error:
        messagebox.showerror(WINDOW_TITLE, f"Could not build the map:\n{error}")
        window.destroy()
        raise

    canvas = tk.Canvas(window, width=image.width(), height=image.height(), highlightthickness=0)
    canvas.pack()
    canvas.create_image(0, 0, image=image, anchor="nw")
    draw_cities_on_canvas(canvas, figure, axes, temperatures)

    #  Tkinter does not keep images alive by itself: if the only reference is a
    #  local variable, Python frees it the moment this function returns and the
    #  canvas goes blank. Parking it on the canvas object keeps it alive.
    canvas.map_image = image
    return window


if __name__ == "__main__":
    build_window().mainloop()
