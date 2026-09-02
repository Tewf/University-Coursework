"""
Turn a temperature into a colour.

Matplotlib has dozens of ready-made colour scales, but the pure-Tkinter window
cannot use them, so this file builds one by hand. It is worth reading even if
you never write your own: a colour scale is just a straight-line blend between
a few chosen colours, and seeing it written out demystifies the ones you get
for free elsewhere.

    uv run python colour_scale.py
"""

from configuration import COLDEST_COLOUR, HOTTEST_COLOUR, MIDDLE_COLOUR


def hex_to_rgb(colour: str) -> tuple[int, int, int]:
    """Split a "#rrggbb" string into its three 0-255 numbers.

    Example:
        >>> hex_to_rgb("#3b4cc0")
        (59, 76, 192)
    """
    #  int(text, 16) reads text as base 16. "3b" is 3*16 + 11 = 59.
    red = int(colour[1:3], 16)
    green = int(colour[3:5], 16)
    blue = int(colour[5:7], 16)
    return red, green, blue


def rgb_to_hex(red: int, green: int, blue: int) -> str:
    """Put three 0-255 numbers back together into a "#rrggbb" string.

    Example:
        >>> rgb_to_hex(59, 76, 192)
        '#3b4cc0'
    """
    #  "%02x" means "in base 16, padded to two digits with a zero".
    return "#%02x%02x%02x" % (red, green, blue)


def blend(first_colour: str, second_colour: str, fraction: float) -> str:
    """Mix two colours. fraction=0 gives the first, 1 the second, 0.5 halfway.

    Example:
        >>> blend("#000000", "#ffffff", 0.5)
        '#7f7f7f'
    """
    first_red, first_green, first_blue = hex_to_rgb(first_colour)
    second_red, second_green, second_blue = hex_to_rgb(second_colour)

    #  The same straight-line formula on each of the three channels:
    #  result = start + (end - start) * fraction
    red = int(first_red + (second_red - first_red) * fraction)
    green = int(first_green + (second_green - first_green) * fraction)
    blue = int(first_blue + (second_blue - first_blue) * fraction)
    return rgb_to_hex(red, green, blue)


def temperature_to_colour(temperature: float, coldest: float, hottest: float) -> str:
    """Place a temperature on the cold-to-hot scale and return its colour.

    The scale has three stops rather than two, because blending straight from
    blue to red passes through a muddy purple. Going blue -> pale yellow -> red
    keeps the middle readable, which is how most weather maps do it.

    Args:
        temperature: The value to colour.
        coldest: The temperature that should come out fully blue.
        hottest: The temperature that should come out fully red.

    Returns:
        A "#rrggbb" string Tkinter understands.

    Example:
        >>> temperature_to_colour(20, coldest=20, hottest=30)
        '#3b4cc0'
        >>> temperature_to_colour(25, coldest=20, hottest=30)
        '#fffbbf'
    """
    if hottest == coldest:
        #  Every city reads the same. Any single colour will do, and this avoids
        #  dividing by zero on the next line.
        return MIDDLE_COLOUR

    position = (temperature - coldest) / (hottest - coldest)
    #  Clamp, so a value slightly outside the range does not produce a colour
    #  outside it -- min/max here are the plain Python built-ins.
    position = max(0.0, min(1.0, position))

    if position < 0.5:
        #  The first half of the scale: rescale 0.0-0.5 onto 0.0-1.0.
        return blend(COLDEST_COLOUR, MIDDLE_COLOUR, position * 2)
    #  The second half: rescale 0.5-1.0 onto 0.0-1.0.
    return blend(MIDDLE_COLOUR, HOTTEST_COLOUR, (position - 0.5) * 2)


if __name__ == "__main__":
    print("20 °C to 30 °C, in steps of 1:")
    for degrees in range(20, 31):
        print(f"  {degrees} °C -> {temperature_to_colour(degrees, 20, 30)}")
