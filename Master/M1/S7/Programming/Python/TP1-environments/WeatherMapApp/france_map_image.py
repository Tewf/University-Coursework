"""Fetch and cache the map image the canvas draws on, with the box it covers."""
from pathlib import Path

import requests

MAP_FILE = Path(__file__).parent / "france_map.png"

# The image, and the geographic box its four edges correspond to. Both are taken
# from Wikipedia's location-map data for France, which publishes the box exactly
# so that markers can be placed on this image; the pairing is its contract, so
# the two constants are changed together or not at all.
# https://en.wikipedia.org/wiki/Module:Location_map/data/France
COMMONS_FILE = "File:France location map-Regions and departements-2016.svg"
MAP_BOUNDS = (-5.8, 41.0, 10.0, 51.5)          # west, south, east, north
ATTRIBUTION = "Map: Superbenjamin / Wikimedia Commons, CC BY-SA 4.0"

COMMONS_API = "https://commons.wikimedia.org/w/api.php"
REQUEST_TIMEOUT_SECONDS = 30
THUMBNAIL_WIDTH = 960
# Wikimedia answers anonymous requests with 403, so identify the caller.
USER_AGENT = "TP1-WeatherMapApp/1.0 (https://github.com/Tewf; university coursework)"


def ensure_map_image(path : Path = MAP_FILE,
                     width : int = THUMBNAIL_WIDTH) -> Path:
    """Return the cached map image, downloading it once if it is not there yet.

    The image is deliberately not committed, so the first run fetches it and
    every later run reads the file. `width` is a request, not a guarantee:
    Commons serves whichever rendered width it already holds, so a caller must
    read the real size from the image itself rather than assume this number.
    Raises requests.HTTPError or requests.Timeout if the download fails.
    """
    if path.exists():
        return path
    response = requests.get(thumbnail_url(width), headers={"User-Agent": USER_AGENT},
                            timeout=REQUEST_TIMEOUT_SECONDS)
    response.raise_for_status()
    path.write_bytes(response.content)
    return path


def thumbnail_url(width : int = THUMBNAIL_WIDTH) -> str:
    """Ask the Commons API where a PNG rendering of the map lives.

    The URL is queried rather than assembled because it carries a content hash
    that cannot be derived from the file name, and because Commons refuses
    widths it has not already rendered. Raises KeyError if the file is gone.
    """
    parameters : dict[str, str | int] = {
        "action": "query", "titles": COMMONS_FILE, "prop": "imageinfo",
        "iiprop": "url", "iiurlwidth": width, "format": "json"}
    response = requests.get(COMMONS_API, params=parameters,
                            headers={"User-Agent": USER_AGENT},
                            timeout=REQUEST_TIMEOUT_SECONDS)
    response.raise_for_status()
    pages = response.json()["query"]["pages"]
    return next(iter(pages.values()))["imageinfo"][0]["thumburl"]
