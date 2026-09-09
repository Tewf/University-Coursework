"""Tests for the weather map: the town table, the colour scale, the request.

None of these open a window or touch the network; the one test that cares about
the request replaces requests.get with a stub and reads what it was handed.
"""
import main


class StubResponse:
    """Stands in for a requests.Response that succeeded."""

    def __init__(self, payload):
        self.payload = payload

    def raise_for_status(self) -> None:
        """A successful response raises nothing."""

    def json(self):
        """Return the decoded body the stub was built with."""
        return self.payload


def test_every_town_sits_inside_the_map_image():
    """A pixel outside the image would be drawn where nothing is ever seen."""
    width, height = main.MAP_SIZE
    outside = [name for name, (x, y, _, _) in main.TOWNS.items()
               if not (0 <= x <= width and 0 <= y <= height)]
    assert not outside


def test_every_town_is_actually_in_france():
    """The coordinates sent to the API must match the country being drawn."""
    for name, (_, _, latitude, longitude) in main.TOWNS.items():
        assert 41.0 <= latitude <= 51.5, name
        assert -5.8 <= longitude <= 10.0, name


def test_no_two_towns_share_a_label_position():
    """Two labels at the same pixel would silently hide one of the readings."""
    positions = [(x, y) for x, y, _, _ in main.TOWNS.values()]
    assert len(set(positions)) == len(positions)


def test_temperature_colour_separates_cold_from_hot():
    """The scale has to distinguish, and to cover both extremes."""
    assert main.colour_for(-8) != main.colour_for(31)
    assert main.colour_for(99) == main.HOTTEST_COLOUR
    assert main.colour_for(-40).startswith("#")


def test_one_request_asks_for_every_town_in_order(monkeypatch):
    """Ten towns must cost one round trip, with the coordinates in TOWNS order."""
    seen = {}

    def stub_get(url, timeout, params):
        seen.update(url=url, timeout=timeout, params=params)
        return StubResponse([{"current": {"temperature_2m": 12.0}}
                             for _ in main.TOWNS])

    monkeypatch.setattr(main.requests, "get", stub_get)
    temperatures = main.fetch_temperatures()

    assert seen["url"] == main.FORECAST_URL
    assert seen["params"]["latitude"].split(",") == [
        str(latitude) for _, _, latitude, _ in main.TOWNS.values()]
    assert seen["params"]["current"] == "temperature_2m"
    assert len(temperatures) == len(main.TOWNS)


def test_a_cached_map_is_not_downloaded_again(tmp_path, monkeypatch):
    """The download happens once; every later run reads the file."""
    cached = tmp_path / "france_map.png"
    cached.write_bytes(b"already here")

    def refuse(*_args, **_kwargs):
        raise AssertionError("download_map went to the network for a cached file")

    monkeypatch.setattr(main.requests, "get", refuse)
    assert main.download_map(cached) == cached
