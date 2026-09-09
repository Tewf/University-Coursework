"""Print the current weather at every location the map will show.

The GUI is question 6; this entry point exercises the API layer on its own.
"""
from current_weather import query_current_weather
from locations import FRANCE


def main() -> None:
    """Query and print the current temperature and WMO code for each location."""
    for name, (latitude, longitude) in FRANCE.items():
        current = query_current_weather(latitude, longitude)["current"]
        print(f"{name:<12} {current['temperature_2m']:>6} degC"
              f"   WMO code {current['weather_code']:<3} at {current['time']}")


if __name__ == "__main__":
    main()
