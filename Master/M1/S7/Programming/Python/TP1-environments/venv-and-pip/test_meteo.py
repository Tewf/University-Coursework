"""Contract tests for meteo.py, one test per clause of a docstring.

Nothing here reaches the network: the fixture is a trimmed real Open-Meteo
archive response, so the tests pin the shape the module actually receives rather
than one invented to suit them, and `query_open_meteo` is exercised against a
stand-in for `requests.get`.
"""
from types import SimpleNamespace

import pytest
import requests
from matplotlib.axes import Axes
from matplotlib.figure import Figure

import meteo

# Three days of Grenoble, cut down from a real response. Keeping the units and
# the echoed coordinates matters: two of the tests below are about those.
ARCHIVE_RESPONSE = {
    "latitude": 45.166958,
    "longitude": 5.747664,
    "daily_units": {"temperature_2m_max": "°C", "temperature_2m_min": "°C"},
    "daily": {
        "time": ["2025-12-01", "2025-12-02", "2025-12-03"],
        "temperature_2m_min": [-3.1, -4.5, 3.7],
        "temperature_2m_max": [4.1, 7.1, 6.0],
    },
}


@pytest.fixture(name="axes")
def fixture_axes() -> Axes:
    """A bare Axes on a figure of its own.

    Built through Figure rather than pyplot, so no backend, no figure registry
    and no window are involved: the drawing happens entirely in memory.
    """
    return Figure().add_subplot()


def fake_response(status_code : int, payload : dict | None = None) -> SimpleNamespace:
    """A stand-in for requests.Response carrying only what the module reads."""
    return SimpleNamespace(status_code=status_code, json=lambda: payload or {})


def test_extract_temperatures_returns_three_aligned_lists():
    """The three lists describe the same days, in the same order."""
    days, min_temps, max_temps = meteo.extract_temperatures(ARCHIVE_RESPONSE)
    assert days == ["2025-12-01", "2025-12-02", "2025-12-03"]
    assert len(min_temps) == len(max_temps) == len(days)
    assert all(low <= high for low, high in zip(min_temps, max_temps))


def test_extract_temperatures_tolerates_a_response_without_daily_data():
    """A missing "daily" block yields empty lists rather than a KeyError."""
    assert meteo.extract_temperatures({}) == ([], [], [])


def test_plot_temperature_draws_both_series_and_the_band(axes):
    """Two lines for the minimum and maximum, one filled collection between."""
    meteo.plot_temperature(ARCHIVE_RESPONSE, "Grenoble", ax=axes)
    assert len(axes.lines) == 2
    assert len(axes.collections) == 1


def test_plot_temperature_labels_the_axis_with_the_unit_the_api_states(axes):
    """The unit is read from daily_units, never hardcoded."""
    meteo.plot_temperature(ARCHIVE_RESPONSE, "Grenoble", ax=axes)
    assert "°C" in axes.get_ylabel()


def test_plot_temperature_titles_with_the_coordinates_when_unnamed(axes):
    """Without a location name, the title falls back to what the API echoed."""
    meteo.plot_temperature(ARCHIVE_RESPONSE, ax=axes)
    assert "45.166958" in axes.get_title()


def test_plot_temperature_composes_several_locations_on_one_axes(axes):
    """Drawing on a caller's Axes accumulates instead of replacing."""
    meteo.plot_temperature(ARCHIVE_RESPONSE, "Grenoble", ax=axes)
    meteo.plot_temperature(ARCHIVE_RESPONSE, "Lyon", ax=axes)
    assert len(axes.lines) == 4


def test_plot_temperature_rejects_a_response_with_no_temperatures(axes):
    """The documented ValueError, rather than an empty plot."""
    with pytest.raises(ValueError):
        meteo.plot_temperature({}, ax=axes)


def test_query_open_meteo_returns_the_decoded_body(monkeypatch):
    """A 200 is handed back as parsed JSON."""
    monkeypatch.setattr(requests, "get",
                        lambda *_a, **_k: fake_response(200, ARCHIVE_RESPONSE))
    assert meteo.query_open_meteo(45.183, 5.7245, "2025-12-01", "2025-12-03") \
        == ARCHIVE_RESPONSE


def test_query_open_meteo_raises_on_an_error_status(monkeypatch):
    """Any status other than 200 becomes a RuntimeError naming the code."""
    monkeypatch.setattr(requests, "get", lambda *_a, **_k: fake_response(404))
    with pytest.raises(RuntimeError, match="404"):
        meteo.query_open_meteo(45.183, 5.7245, "2025-12-01", "2025-12-03")
