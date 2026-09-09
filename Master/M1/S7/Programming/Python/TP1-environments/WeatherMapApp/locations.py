"""The places the weather map shows, as latitude/longitude pairs.

Coordinates are data, not code: adding a city to the map is an edit here and
nowhere else. Values are the cities' decimal degrees, north/east positive.
"""

FRANCE : dict[str, tuple[float, float]] = {
    "Brest": (48.3904, -4.4861),
    "Lille": (50.6292, 3.0573),
    "Strasbourg": (48.5734, 7.7521),
    "Paris": (48.8566, 2.3522),
    "Bordeaux": (44.8378, -0.5792),
    "Lyon": (45.7640, 4.8357),
    "Grenoble": (45.1830, 5.7245),
    "Marseille": (43.2965, 5.3698),
    "Toulouse": (43.6047, 1.4442),
    "Nice": (43.7102, 7.2620),
}
