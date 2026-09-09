"""Tests for the drawing side: the map image, the projection, the code table.

The projection is the only part with arithmetic in it, so most of this file is
about it. None of these tests open a window, and none of them need the network.
"""
from math import cos, radians

import pytest

import weather_codes
from france_map_image import MAP_BOUNDS, MAP_FILE, ensure_map_image
from locations import FRANCE
from map_projection import ImageProjection

# A one-degree square with a 100x50 image over it, small enough to check by hand.
SQUARE = (2.0, 45.0, 3.0, 46.0)          # west, south, east, north
WIDTH, HEIGHT = 100, 50


def png_size(path) -> tuple[int, int]:
    """Return a PNG's pixel size, read from the IHDR chunk at a fixed offset.

    Read from the bytes rather than through tkinter so that these tests need
    neither a display nor an event loop.
    """
    header = path.read_bytes()[16:24]
    return int.from_bytes(header[:4], "big"), int.from_bytes(header[4:], "big")


def test_projection_puts_north_above_south():
    """Pixel y grows downwards while latitude grows upwards."""
    projection = ImageProjection(SQUARE, WIDTH, HEIGHT)
    assert projection.project(46.0, 2.5)[1] < projection.project(45.0, 2.5)[1]


def test_projection_puts_east_right_of_west():
    """Longitude grows eastwards, and so does pixel x."""
    projection = ImageProjection(SQUARE, WIDTH, HEIGHT)
    assert projection.project(45.5, 2.0)[0] < projection.project(45.5, 3.0)[0]


def test_projection_maps_the_bounds_onto_the_whole_image():
    """The four corners of the box are the four corners of the image, exactly."""
    projection = ImageProjection(SQUARE, WIDTH, HEIGHT)
    assert projection.project(46.0, 2.0) == pytest.approx((0.0, 0.0))
    assert projection.project(45.0, 3.0) == pytest.approx((WIDTH, HEIGHT))


def test_projection_is_linear_in_both_axes():
    """Halfway along in degrees is halfway across in pixels.

    Linearity is what makes this projection interpolation rather than
    trigonometry, so it is worth pinning rather than assuming.
    """
    projection = ImageProjection(SQUARE, WIDTH, HEIGHT)
    assert projection.project(45.5, 2.5) == pytest.approx((WIDTH / 2, HEIGHT / 2))


def test_projection_does_not_clamp_what_falls_outside():
    """A location off the map projects off the image, so a caller can tell."""
    projection = ImageProjection(SQUARE, WIDTH, HEIGHT)
    x, _ = projection.project(45.5, 1.0)
    assert x < 0
    assert not projection.contains(45.5, 1.0)
    assert projection.contains(45.5, 2.5)


def test_projection_rejects_bounds_with_no_area():
    """A single point has no extent to interpolate across."""
    with pytest.raises(ValueError):
        ImageProjection((2.0, 45.0, 2.0, 45.0), WIDTH, HEIGHT)


def test_projection_rejects_an_image_with_no_size():
    """Dividing a box across zero pixels is a caller error, not an empty map."""
    with pytest.raises(ValueError):
        ImageProjection(SQUARE, 0, HEIGHT)


def test_every_town_falls_inside_the_mapped_area():
    """A town outside the bounds would be drawn off the image without complaint."""
    projection = ImageProjection(MAP_BOUNDS, 960, 923)
    outside = [name for name, (lat, lon) in FRANCE.items()
               if not projection.contains(lat, lon)]
    assert not outside


@pytest.mark.skipif(not MAP_FILE.exists(), reason="map image not downloaded yet")
def test_the_image_has_the_shape_its_bounds_imply():
    """The image and the bounds must describe the same drawing.

    They are two constants that only agree by intent, and nothing at runtime
    would notice them disagreeing: every town would simply be placed wrongly by
    the same amount. An equidistant cylindrical map is as many pixels wide as
    its longitude span shortened by the cosine of its middle latitude, so that
    ratio is a consequence the pair can be checked against.
    """
    west, south, east, north = MAP_BOUNDS
    width, height = png_size(MAP_FILE)
    expected = (east - west) * cos(radians((south + north) / 2)) / (north - south)
    assert width / height == pytest.approx(expected, rel=0.01)


def test_a_cached_image_is_not_downloaded_again(tmp_path):
    """The download happens once; every later run reads the file."""
    cached = tmp_path / "already-here.png"
    cached.write_bytes(b"not really a png")
    assert ensure_map_image(cached) == cached
    assert cached.read_bytes() == b"not really a png"


def test_known_weather_codes_are_described():
    """Codes the API actually returned during this practical."""
    assert weather_codes.describe(0) == "Clear sky"
    assert weather_codes.describe(80) == "Slight rain showers"


def test_an_unknown_weather_code_still_reads_as_something():
    """A code added upstream must not crash the map."""
    assert "42" in weather_codes.describe(42)


def test_temperature_colour_separates_cold_from_hot():
    """The scale has to actually distinguish, and cover both extremes."""
    assert weather_codes.temperature_colour(-8) != weather_codes.temperature_colour(31)
    assert weather_codes.temperature_colour(99).startswith("#")
