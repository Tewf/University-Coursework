"""Pull values out of a nested JSON answer without crashing on a missing key.

Run it to see it work:

    python read_json.py
"""

from typing import Any

# ---------------------------------------------------------------- THE PATTERN
#  Two rules cover almost every case:
#
#    data["key"]         crashes with KeyError if "key" is absent
#    data.get("key", {}) gives you {} instead, so the NEXT .get still works
#
#  Chaining .get with an empty default is what lets you reach three levels
#  down without four if-statements.


def dig(data: Any, *keys: str, default: Any = None) -> Any:
    """Follow a path of keys down a nested dict, stopping safely if it breaks.

    Args:
        data: The nested structure, usually straight from response.json().
        *keys: The path, one key per level: dig(d, "daily", "time").
        default: What to return if any step of the path is missing.

    Returns:
        Whatever is at the end of the path, or `default`.

    Example:
        >>> dig({"daily": {"time": ["2025-12-01"]}}, "daily", "time")
        ['2025-12-01']
        >>> dig({"daily": {}}, "daily", "time", default=[])
        []
    """
    current = data
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current


# -------------------------------------------------------------- END OF PATTERN


if __name__ == "__main__":
    #  A cut-down version of what Open-Meteo actually answers.
    answer = {
        "latitude": 45.18,
        "daily": {
            "time": ["2025-12-01", "2025-12-02", "2025-12-03"],
            "temperature_2m_max": [8.1, 6.4, 9.9],
        },
    }

    print("present:      ", dig(answer, "daily", "time"))
    print("absent:       ", dig(answer, "daily", "humidity", default=[]))
    print("wrong depth:  ", dig(answer, "latitude", "value", default="n/a"))

    #  The common shape: several equal-length lists that line up by index.
    #  zip walks them together, which beats indexing with range(len(...)).
    days = dig(answer, "daily", "time", default=[])
    highs = dig(answer, "daily", "temperature_2m_max", default=[])
    for day, high in zip(days, highs):
        print(f"  {day}  {high:5.1f} C")
