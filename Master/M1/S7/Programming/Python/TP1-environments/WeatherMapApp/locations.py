"""The places the weather map shows, as latitude/longitude pairs.

Coordinates are data, not code: adding a town to the map is an edit here and
nowhere else. Values are decimal degrees, north and east positive.

The ten are chosen to spread across the drawn area rather than to be the ten
largest, since two towns closer than about a hundred kilometres overlap each
other's labels at this scale. That is why Lyon and Nice are absent: they sit on
top of Grenoble and Marseille respectively. Ajaccio is present because the map
includes Corsica, and an empty island reads as an oversight.
"""

FRANCE : dict[str, tuple[float, float]] = {
    "Lille": (50.6292, 3.0573),
    "Brest": (48.3904, -4.4861),
    "Paris": (48.8566, 2.3522),
    "Strasbourg": (48.5734, 7.7521),
    "Nantes": (47.2184, -1.5536),
    "Bordeaux": (44.8378, -0.5792),
    "Grenoble": (45.1830, 5.7245),
    "Toulouse": (43.6047, 1.4442),
    "Marseille": (43.2965, 5.3698),
    "Ajaccio": (41.9267, 8.7369),
}
