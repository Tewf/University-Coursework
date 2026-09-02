"""
Every value you might want to change lives here, and nowhere else.

Nothing in this file *does* anything: it only gives names to numbers, colours
and web addresses that the other modules read. If you want to add a city, move
the map, or change how smooth it looks, this is the only file you edit. That is
the point -- you should never have to hunt for a number buried inside a
calculation.
"""

# ---------------------------------------------------------------------------
# The cities we show
# ---------------------------------------------------------------------------
# Each entry is  "name": (latitude, longitude),  both in degrees.
# Latitude runs south -> north, longitude runs west -> east, so a NEGATIVE
# longitude means "west of Greenwich" -- that is why Brest and Bordeaux have a
# minus sign and Strasbourg does not.
#
# They are spread across the whole country on purpose. The map is built by
# interpolating BETWEEN these points, so a map made from Paris and Lyon alone
# would really be a map of the Paris-Lyon axis, not a map of France.
CITY_COORDINATES: dict[str, tuple[float, float]] = {
    "Lille": (50.6292, 3.0573),
    "Brest": (48.3904, -4.4861),
    "Paris": (48.8566, 2.3522),
    "Strasbourg": (48.5734, 7.7521),
    "Nantes": (47.2184, -1.5536),
    "Clermont-Ferrand": (45.7772, 3.0870),
    "Lyon": (45.7640, 4.8357),
    "Grenoble": (45.1830, 5.7245),
    "Bordeaux": (44.8378, -0.5792),
    "Toulouse": (43.6047, 1.4442),
    "Nice": (43.7102, 7.2620),
    "Marseille": (43.2965, 5.3698),
}

# ---------------------------------------------------------------------------
# Where the map starts and stops
# ---------------------------------------------------------------------------
# A rectangle just big enough to hold metropolitan France, Corsica included.
# Change these four numbers and you get a map of a different place -- try
# (-10, 30) and (35, 70) for Europe.
MINIMUM_LONGITUDE: float = -5.2
MAXIMUM_LONGITUDE: float = 9.7
MINIMUM_LATITUDE: float = 41.3
MAXIMUM_LATITUDE: float = 51.1

# ---------------------------------------------------------------------------
# How the temperature is spread between the cities
# ---------------------------------------------------------------------------
# How far, in degrees, one city's temperature still counts for. Roughly 1 degree
# of latitude is 111 km, so 2.0 means a city noticeably influences the weather
# shown about 200 km around it.
#   - make it BIGGER  -> a smoother, blurrier map
#   - make it SMALLER -> each city becomes its own isolated blob
INFLUENCE_SPREAD_DEGREES: float = 2.0

# How many squares across and down we compute the temperature on. 300 x 300 is
# 90 000 points, which numpy handles instantly. Lower it to 50 if you want to
# SEE the individual squares while you are learning.
MAP_GRID_RESOLUTION: int = 300

# ---------------------------------------------------------------------------
# The Open-Meteo API
# ---------------------------------------------------------------------------
# The FORECAST endpoint, which serves real-time weather. This is not the same
# server as the ARCHIVE endpoint (archive-api.open-meteo.com) used in
# Exercise 1: that one only knows about the past.
OPEN_METEO_FORECAST_URL: str = "https://api.open-meteo.com/v1/forecast"

# ---------------------------------------------------------------------------
# The outline of France
# ---------------------------------------------------------------------------
# Downloaded once, then kept in the file below so we never ask for it twice.
# Source: github.com/gregoiredavid/france-geojson, built from IGN data (ODbL).
BORDER_SOURCE_URL: str = (
    "https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/metropole.geojson"
)
BORDER_CACHE_FILE: str = "france_border.geojson"

# ---------------------------------------------------------------------------
# Colours
# ---------------------------------------------------------------------------
# Everything outside the border: the sea, and the neighbouring countries.
OUTSIDE_FRANCE_COLOUR: str = "#eaeef2"

# The three colours the temperature scale runs through, coldest to hottest.
# Used by the pure-tkinter version, which has to build its own colour scale
# because it cannot borrow Matplotlib's.
COLDEST_COLOUR: str = "#3b4cc0"
MIDDLE_COLOUR: str = "#fffbbf"
HOTTEST_COLOUR: str = "#b40426"

# ---------------------------------------------------------------------------
# The window
# ---------------------------------------------------------------------------
# How tall the map itself is, in pixels. The WIDTH is not set here on purpose:
# the pure-Tkinter window works it out from the bounds above, so that France
# keeps its real proportions however you move the edges of the map.
MAP_HEIGHT_PIXELS: int = 660

# Blank space left around the map for the title and the colour scale.
MAP_MARGIN_PIXELS: int = 30
