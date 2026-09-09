"""Tests for the weather map: the town table, the colour scale, the request.

None of these opens a window or touches the network. The one test that cares
about the request replaces requests.get with a stub and reads what it was handed.
"""
import pytest

import main

# The box this map is published with, repeated here on purpose: if the copy in
# main's comment is edited, this one disagrees and the tests say so.
WEST, SOUTH, EAST, NORTH = -5.8, 41.0, 10.0, 51.5


class StubResponse:
    """Stands in for a requests.Response that succeeded."""

    def __init__(self, payload):
        self.payload = payload

    def raise_for_status(self) -> None:
        """A successful response raises nothing."""

    def json(self):
        """Return the decoded body the stub was built with."""
        return self.payload


def test_each_pixel_matches_the_coordinates_beside_it():
    """The two halves of a row must describe the same place.

    A hand-typed pixel is the one thing in this program that can silently
    disagree with the coordinates sent to the API, which would print a real
    temperature over the wrong part of the country. Recomputing it from the
    published box is what makes adding a town safe.
    """
    width, height = main.MAP_SIZE
    for name, town in main.TOWNS.items():
        expected_x = (town.longitude - WEST) / (EAST - WEST) * width
        expected_y = (NORTH - town.latitude) / (NORTH - SOUTH) * height
        assert town.x == pytest.approx(expected_x, abs=1), name
        assert town.y == pytest.approx(expected_y, abs=1), name


def test_every_town_sits_inside_the_map_image():
    """A pixel outside the image would be drawn where nothing is ever seen."""
    width, height = main.MAP_SIZE
    outside = [name for name, town in main.TOWNS.items()
               if not (0 <= town.x <= width and 0 <= town.y <= height)]
    assert not outside


def test_every_town_is_actually_in_france():
    """The coordinates sent to the API must match the country being drawn."""
    for name, town in main.TOWNS.items():
        assert SOUTH <= town.latitude <= NORTH, name
        assert WEST <= town.longitude <= EAST, name


def test_no_two_towns_share_a_label_position():
    """Two labels at one pixel would silently hide a reading."""
    positions = [(town.x, town.y) for town in main.TOWNS.values()]
    assert len(set(positions)) == len(positions)


def test_temperature_colour_separates_cold_from_hot():
    """The scale has to distinguish, and to cover both extremes."""
    assert main.colour_for(-8) != main.colour_for(31)
    assert main.colour_for(99) == main.HOTTEST_COLOUR
    assert main.colour_for(-40).startswith("#")


def test_one_request_asks_for_every_town_in_order(monkeypatch):
    """Any number of towns must cost one round trip, in table order."""
    seen = {}

    def stub_get(url, timeout, params):
        seen.update(url=url, timeout=timeout, params=params)
        return StubResponse([{"current": {"temperature_2m": 12.0}}
                             for _ in main.TOWNS])

    monkeypatch.setattr(main.requests, "get", stub_get)
    temperatures = main.fetch_temperatures()

    assert seen["url"] == main.FORECAST_URL
    assert seen["params"]["latitude"].split(",") == [
        str(town.latitude) for town in main.TOWNS.values()]
    assert seen["params"]["current"] == "temperature_2m"
    assert len(temperatures) == len(main.TOWNS)


def test_another_table_can_be_queried(monkeypatch):
    """The default table is a default, not a hard-coded assumption."""
    seen = {}

    def stub_get(_url, timeout, params):        # pylint: disable=unused-argument
        seen.update(params=params)
        return StubResponse([{"current": {"temperature_2m": 1.0}}])

    monkeypatch.setattr(main.requests, "get", stub_get)
    main.fetch_temperatures({"Berlin": main.Town(0, 0, 52.52, 13.405)})
    assert seen["params"]["latitude"] == "52.52"


def test_a_cached_map_is_not_downloaded_again(tmp_path, monkeypatch):
    """The download happens once; every later run reads the file."""
    cached = tmp_path / "france_map.png"
    cached.write_bytes(b"already here")

    def refuse(*_args, **_kwargs):
        raise AssertionError("download_map went to the network for a cached file")

    monkeypatch.setattr(main.requests, "get", refuse)
    assert main.download_map(cached) == cached
