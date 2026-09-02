"""
Paint the temperature field into an image Tkinter can display.

This is the pure-Tkinter answer to "how do I show a smooth colour gradient
without Matplotlib?". The trick is PhotoImage.put(), which fills a whole image
from one big string of colours in a single call.

    uv run python map_image.py
"""

import tkinter as tk

import numpy as np

from PIL import Image, ImageDraw

from colour_scale import temperature_to_colour
from configuration import MAP_HEIGHT_PIXELS, OUTSIDE_FRANCE_COLOUR
from france_border import load_border_polygons
from map_projection import MAP_WIDTH_PIXELS, degrees_to_image_pixels
from temperature_map import build_grid, interpolate

#  How many different colours the scale is cut into. 256 is far more than the
#  eye can tell apart, so the result looks perfectly smooth, and mixing them
#  once up front is much quicker than mixing a colour for every single pixel.
COLOUR_STEPS = 256


def build_land_mask() -> np.ndarray:
    """Say, for every pixel of the map, whether it is on French land.

    The obvious way -- ask "is this point inside the border?" once per pixel --
    is correct but hopeless: 459 000 pixels against 31 558 border points took
    15.4 seconds when it was measured. Filling the shape instead takes 0.009 s,
    because drawing a filled polygon is exactly what drawing libraries are built
    to do quickly.

    So we DRAW France, in white on a black picture, and then read the picture
    back: white means land. Holes are drawn back in black afterwards, which is
    why load_border_polygons is used here rather than load_border_rings -- it
    keeps land and holes apart.

    Returns:
        A 2-D array of True/False, MAP_HEIGHT_PIXELS rows by MAP_WIDTH_PIXELS
        columns, True on land. Row 0 is the NORTH edge, as in any image.

    Example:
        >>> mask = build_land_mask()
        >>> mask.shape
        (660, 695)
    """
    #  Mode "1" is a one-bit-per-pixel picture: every pixel is 0 or 1.
    mask_picture = Image.new("1", (MAP_WIDTH_PIXELS, MAP_HEIGHT_PIXELS), 0)
    drawer = ImageDraw.Draw(mask_picture)

    for polygon in load_border_polygons():
        for ring_index, ring in enumerate(polygon):
            pixel_points = []
            for longitude, latitude in ring:
                pixel_points.append(degrees_to_image_pixels(longitude, latitude))

            if len(pixel_points) < 3:
                continue  # a polygon needs three corners to enclose anything

            #  The first ring of a polygon is land, so fill it in; any later ring
            #  is a hole, so paint it back out.
            if ring_index == 0:
                drawer.polygon(pixel_points, fill=1)
            else:
                drawer.polygon(pixel_points, fill=0)

    return np.array(mask_picture, dtype=bool)


def build_palette(coldest: float, hottest: float) -> list[str]:
    """Mix the COLOUR_STEPS colours of the scale once, ready to be looked up.

    A lookup table like this is a habit worth keeping: any time you would call
    the same slow-ish function with only a few hundred distinct answers, compute
    the answers once and index into them instead.

    Example:
        >>> palette = build_palette(20, 30)
        >>> palette[0], palette[-1]
        ('#3b4cc0', '#b40426')
    """
    palette = []
    for step in range(COLOUR_STEPS):
        fraction = step / (COLOUR_STEPS - 1)
        temperature = coldest + fraction * (hottest - coldest)
        palette.append(temperature_to_colour(temperature, coldest, hottest))
    return palette


def temperature_levels(field: np.ndarray, coldest: float, hottest: float) -> np.ndarray:
    """Say which palette entry each point of the field wants.

    Args:
        field: The 2-D temperatures from temperature_map.interpolate.
        coldest: The temperature mapped to palette entry 0.
        hottest: The temperature mapped to the last palette entry.

    Returns:
        A 2-D array of whole numbers between 0 and COLOUR_STEPS - 1.
    """
    if hottest == coldest:
        #  Everywhere reads the same, so everything takes the first colour. This
        #  also avoids dividing by zero on the next line.
        return np.zeros(field.shape, dtype=int)

    levels = np.round((field - coldest) / (hottest - coldest) * (COLOUR_STEPS - 1))
    return np.clip(levels, 0, COLOUR_STEPS - 1).astype(int)


def build_map_image(temperatures: dict[str, float]) -> tk.PhotoImage:
    """Colour every pixel of the map and pack them into a Tkinter image.

    PhotoImage.put() accepts a big string laid out as
    "{row1col1 row1col2 ...} {row2col1 ...}" -- braces around each row, colours
    separated by spaces. Writing the whole image in one call takes about half a
    second; setting pixels one at a time would take minutes.

    A Tk window must already exist before you call this: PhotoImage needs Tk to
    be running, and asking for one first gives "too early to create image".

    Args:
        temperatures: City name -> current temperature in Celsius.

    Returns:
        An image MAP_WIDTH_PIXELS by MAP_HEIGHT_PIXELS, French land coloured by
        temperature and everything outside it left flat grey.
    """
    coldest = min(temperatures.values())
    hottest = max(temperatures.values())

    #  One grid point per pixel, so the image needs no resizing afterwards.
    longitudes, latitudes = build_grid(columns=MAP_WIDTH_PIXELS, rows=MAP_HEIGHT_PIXELS)
    field = interpolate(temperatures, longitudes, latitudes)

    palette = build_palette(coldest, hottest)
    levels = temperature_levels(field, coldest, hottest)

    #  [::-1] flips top to bottom: row 0 of an image is the TOP of the picture,
    #  which is the NORTH, which is the LAST row of a grid that starts in the
    #  south. .tolist() turns the numpy arrays into ordinary Python lists,
    #  because reading numpy values one at a time in a loop is far slower.
    level_rows = levels[::-1].tolist()
    #  The mask is already the right way up -- it was drawn as a picture -- so
    #  only the temperature grid needs flipping.
    inside_rows = build_land_mask().tolist()

    text_rows = []
    for row_index in range(MAP_HEIGHT_PIXELS):
        level_row = level_rows[row_index]
        inside_row = inside_rows[row_index]
        pixel_colours = []
        for column_index in range(MAP_WIDTH_PIXELS):
            if inside_row[column_index]:
                pixel_colours.append(palette[level_row[column_index]])
            else:
                pixel_colours.append(OUTSIDE_FRANCE_COLOUR)
        text_rows.append("{" + " ".join(pixel_colours) + "}")

    image = tk.PhotoImage(width=MAP_WIDTH_PIXELS, height=MAP_HEIGHT_PIXELS)
    image.put(" ".join(text_rows), to=(0, 0))
    return image


if __name__ == "__main__":
    import time

    from configuration import CITY_COORDINATES
    from meteo import fetch_city_temperatures

    root = tk.Tk()  # PhotoImage needs a running Tk, even if we never show it.
    root.withdraw()
    measured = fetch_city_temperatures(CITY_COORDINATES)
    started = time.time()
    picture = build_map_image(measured)
    print(f"{picture.width()} x {picture.height()} image painted in {time.time() - started:.2f} s")
    root.destroy()
