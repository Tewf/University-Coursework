"""Contract tests for the API layer, runnable offline.

`requests.get` is replaced by a recorder, so the tests can assert what the module
*asks the API for* -- the part that fails silently when a parameter name is wrong
-- without a network call and without depending on today's weather.
"""
from types import SimpleNamespace

import pytest
import requests

import current_weather
from locations import FRANCE

# A trimmed real response: enough of the shape that the module documents.
CURRENT_RESPONSE = {
    "latitude": 45.18,
    "longitude": 5.72,
    "current_units": {"temperature_2m": "°C", "weather_code": "wmo code"},
    "current": {"time": "2026-09-09T14:15", "temperature_2m": 18.4, "weather_code": 80},
}


@pytest.fixture(name="recorded")
def fixture_recorded(monkeypatch) -> dict:
    """Replace requests.get with a recorder, and hand back what it was called with.

    The dictionary fills in when the module under test makes its call, so a test
    reads it after calling rather than before.
    """
    recorded : dict = {}

    def recording_get(url : str, **kwargs) -> SimpleNamespace:
        recorded["url"] = url
        recorded.update(kwargs)
        return SimpleNamespace(json=lambda: CURRENT_RESPONSE,
                               raise_for_status=lambda: None)

    monkeypatch.setattr(requests, "get", recording_get)
    return recorded


def test_it_calls_the_forecast_endpoint_not_the_archive_one(recorded):
    """The two Open-Meteo hosts answer different questions; this is the live one."""
    current_weather.query_current_weather(45.183, 5.7245)
    assert recorded["url"] == "https://api.open-meteo.com/v1/forecast"


def test_it_asks_for_the_current_variables_by_their_documented_names(recorded):
    """`current`, not `current_weather`; `weather_code`, not the archive's `weathercode`."""
    current_weather.query_current_weather(45.183, 5.7245)
    assert recorded["params"]["current"] == "temperature_2m,weather_code"


def test_it_passes_the_coordinates_it_was_given(recorded):
    """Latitude and longitude reach the API unchanged and the right way round."""
    current_weather.query_current_weather(45.183, 5.7245)
    assert recorded["params"]["latitude"] == 45.183
    assert recorded["params"]["longitude"] == 5.7245


def test_it_always_sets_a_timeout(recorded):
    """Without one, a silent network stall would hang the GUI for good."""
    current_weather.query_current_weather(45.183, 5.7245)
    assert recorded["timeout"] == current_weather.REQUEST_TIMEOUT_SECONDS


def test_it_returns_the_decoded_body(recorded):
    """The caller gets parsed JSON, not a Response object."""
    assert current_weather.query_current_weather(45.183, 5.7245) == CURRENT_RESPONSE
    assert recorded["url"].startswith("https://")


def test_it_lets_an_error_status_surface(monkeypatch):
    """Failure is raise_for_status', so every error status is covered, not just 200."""
    failing = SimpleNamespace(
        json=dict,
        raise_for_status=_raise_http_error)
    monkeypatch.setattr(requests, "get", lambda *_a, **_k: failing)
    with pytest.raises(requests.HTTPError):
        current_weather.query_current_weather(999, 999)


def _raise_http_error() -> None:
    """Stand in for a 400 answer from the API."""
    raise requests.HTTPError("400 Client Error")


def test_every_location_sits_inside_metropolitan_france():
    """The map's data table is data, and wrong data is a bug the map cannot show."""
    for name, (latitude, longitude) in FRANCE.items():
        assert 41.0 <= latitude <= 51.5, name
        assert -5.5 <= longitude <= 9.6, name
