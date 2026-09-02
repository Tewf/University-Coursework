"""
Place a position on Earth at a position on the canvas.

This is "projecting a map", stripped to its simplest form. Nothing here knows
about weather or about colours, so you can reuse it for any map at all: change
the four bounds in configuration.py and the same code puts Europe, or Brittany,
or Corsica on a canvas.

    uv run python map_projection.py
"""

import math

from configuration import (
    MAP_HEIGHT_PIXELS,
    MAP_MARGIN_PIXELS,
    MAXIMUM_LATITUDE,
    MAXIMUM_LONGITUDE,
    MINIMUM_LATITUDE,
    MINIMUM_LONGITUDE,
)

LONGITUDE_SPAN = MAXIMUM_LONGITUDE - MINIMUM_LONGITUDE
LATITUDE_SPAN = MAXIMUM_LATITUDE - MINIMUM_LATITUDE
MIDDLE_LATITUDE = (MINIMUM_LATITUDE + MAXIMUM_LATITUDE) / 2

#  The width is WORKED OUT, not chosen. France spans 14.9 degrees of longitude
#  and 9.8 of latitude, but the Earth is round: the lines of longitude squeeze
#  together as you go north, so a degree of longitude is only cos(latitude) as
#  wide as a degree of latitude -- about 0.69 in the middle of France. Choose the
#  width by hand instead and the country comes out visibly fat.
MAP_WIDTH_PIXELS = round(
    MAP_HEIGHT_PIXELS * LONGITUDE_SPAN * math.cos(math.radians(MIDDLE_LATITUDE)) / LATITUDE_SPAN
)


def degrees_to_image_pixels(longitude: float, latitude: float) -> tuple[float, float]:
    """Same as degrees_to_pixels, but measured from the map's own top-left corner.

    The canvas has a margin around the map; the map IMAGE does not. Anything
    drawn onto the image itself -- the land mask, for instance -- wants these
    coordinates, and anything drawn on the canvas around it wants the ones from
    degrees_to_pixels below.

    Example:
        >>> degrees_to_image_pixels(MINIMUM_LONGITUDE, MAXIMUM_LATITUDE)
        (0.0, 0.0)
    """
    x_fraction = (longitude - MINIMUM_LONGITUDE) / LONGITUDE_SPAN
    y_fraction = (latitude - MINIMUM_LATITUDE) / LATITUDE_SPAN
    return x_fraction * (MAP_WIDTH_PIXELS - 1), (1 - y_fraction) * (MAP_HEIGHT_PIXELS - 1)


def degrees_to_pixels(longitude: float, latitude: float) -> tuple[float, float]:
    """Turn a longitude and latitude into an (x, y) position on the canvas.

    Two steps, and that is all a simple map projection is:
      1. how far along the range does this value sit? 0.0 at one edge, 1.0 at
         the other -- that is the "fraction" below;
      2. multiply by the size in pixels, and shift by the margin.

    The vertical axis gets `1 -` in front of it because the two coordinate
    systems disagree: latitude grows NORTHWARDS, but a screen's y grows
    DOWNWARDS from the top. Forget it and France appears upside down.

    Args:
        longitude: Degrees east, negative for west.
        latitude: Degrees north.

    Returns:
        The (x, y) pixel position on the canvas.

    Example:
        >>> degrees_to_pixels(MINIMUM_LONGITUDE, MAXIMUM_LATITUDE)   # top-left
        (30.0, 30.0)
        >>> round(degrees_to_pixels(2.3522, 48.8566)[0])             # Paris
        382
    """
    image_x, image_y = degrees_to_image_pixels(longitude, latitude)
    return MAP_MARGIN_PIXELS + image_x, MAP_MARGIN_PIXELS + image_y


if __name__ == "__main__":
    print(f"map is {MAP_WIDTH_PIXELS} x {MAP_HEIGHT_PIXELS} pixels")
    for corner_name, position in [
        ("north-west", (MINIMUM_LONGITUDE, MAXIMUM_LATITUDE)),
        ("south-east", (MAXIMUM_LONGITUDE, MINIMUM_LATITUDE)),
        ("Paris", (2.3522, 48.8566)),
    ]:
        x, y = degrees_to_pixels(position[0], position[1])
        print(f"  {corner_name:<11} -> x={x:7.1f}  y={y:7.1f}")
