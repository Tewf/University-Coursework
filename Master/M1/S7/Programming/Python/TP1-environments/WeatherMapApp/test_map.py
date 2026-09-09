"""Tests for the drawing side: the border file, the projection, the code table.

The projection is the only part with real arithmetic in it, so most of this file
is about it. None of these tests open a window.
"""
import pytest

import france_outline
import weather_codes
from map_projection import MapProjection, geographic_bounds

# A one-degree square somewhere near France, small enough to reason about by hand.
SQUARE = [[(2.0, 45.0), (3.0, 45.0), (3.0, 46.0), (2.0, 46.0), (2.0, 45.0)]]


def test_geographic_bounds_encloses_every_point():
    """The box is the extremes of all rings taken together."""
    assert geographic_bounds(SQUARE) == (2.0, 45.0, 3.0, 46.0)


def test_geographic_bounds_rejects_having_nothing_to_enclose():
    """An empty ring list is a caller error, not an empty box."""
    with pytest.raises(ValueError):
        geographic_bounds([])


def test_projection_puts_north_above_south():
    """Canvas y grows downwards while latitude grows upwards."""
    projection = MapProjection(geographic_bounds(SQUARE), 400, 400)
    _, y_north = projection.project(46.0, 2.5)
    _, y_south = projection.project(45.0, 2.5)
    assert y_north < y_south


def test_projection_puts_east_right_of_west():
    """Longitude grows eastwards, and so does canvas x."""
    projection = MapProjection(geographic_bounds(SQUARE), 400, 400)
    x_west, _ = projection.project(45.5, 2.0)
    x_east, _ = projection.project(45.5, 3.0)
    assert x_west < x_east


def test_projection_narrows_longitude_by_the_standard_parallel():
    """One degree east-west is shorter than one degree north-south away from the equator.

    This is the whole point of the cosine factor: without it France comes out
    visibly too wide.
    """
    projection = MapProjection(geographic_bounds(SQUARE), 400, 400)
    x_west, _ = projection.project(45.5, 2.0)
    x_east, _ = projection.project(45.5, 3.0)
    _, y_north = projection.project(46.0, 2.5)
    _, y_south = projection.project(45.0, 2.5)
    assert (x_east - x_west) < (y_south - y_north)


def test_projection_keeps_the_drawing_inside_the_canvas():
    """Every corner of the bounds lands within the canvas, margin included."""
    projection = MapProjection(geographic_bounds(SQUARE), 400, 300, margin=20)
    for latitude in (45.0, 46.0):
        for longitude in (2.0, 3.0):
            x, y = projection.project(latitude, longitude)
            assert 20 - 1e-9 <= x <= 380 + 1e-9
            assert 20 - 1e-9 <= y <= 280 + 1e-9


def test_projection_centres_what_it_cannot_fill():
    """The unused axis is padded equally at both ends rather than left-aligned."""
    projection = MapProjection(geographic_bounds(SQUARE), 800, 300, margin=0)
    x_west, _ = projection.project(45.5, 2.0)
    x_east, _ = projection.project(45.5, 3.0)
    assert x_west == pytest.approx(800 - x_east)


def test_projection_rejects_bounds_with_no_area():
    """A single point has no extent to scale to."""
    with pytest.raises(ValueError):
        MapProjection((2.0, 45.0, 2.0, 45.0), 400, 400)


def test_border_file_loads_and_covers_metropolitan_france():
    """The downloaded outline is the right country, Corsica included."""
    rings = france_outline.load_border_rings()
    lon_min, lat_min, lon_max, lat_max = geographic_bounds(rings)
    assert len(rings) > 1                       # mainland plus islands
    assert -5.5 < lon_min and lon_max < 9.8     # Brittany to Corsica
    assert 41.0 < lat_min and lat_max < 51.5    # Bonifacio to Dunkirk


def test_missing_border_file_says_how_to_get_it(tmp_path):
    """The file is not committed, so the error has to be actionable."""
    with pytest.raises(FileNotFoundError, match="curl"):
        france_outline.load_border_rings(tmp_path / "absent.geojson")


def test_known_weather_codes_are_described():
    """Codes the API actually returned during this practical."""
    assert weather_codes.describe(0) == "Clear sky"
    assert weather_codes.describe(80) == "Slight rain showers"


def test_an_unknown_weather_code_still_reads_as_something():
    """A code added to the table upstream must not crash the map."""
    assert "42" in weather_codes.describe(42)


def test_temperature_colour_separates_cold_from_hot():
    """The scale has to actually distinguish, and cover both extremes."""
    assert weather_codes.temperature_colour(-8) != weather_codes.temperature_colour(31)
    assert weather_codes.temperature_colour(99).startswith("#")
