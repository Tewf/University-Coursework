"""
Provide the outline of metropolitan France.

The outline is a GeoJSON file of about 600 kB. It is downloaded the FIRST time
you run the app and then written next to this file, so every later run reads it
off the disk in a hundredth of a second. Deleting france_border.geojson simply
makes the next run fetch it again.

Run it directly to check the download and the shape:

    uv run python france_border.py
"""

import json
from pathlib import Path

import requests
from matplotlib.path import Path as MatplotlibPath

from configuration import BORDER_CACHE_FILE, BORDER_SOURCE_URL

#  Path(__file__) is this very file. .parent is the folder holding it. Building
#  the cache path this way means the app works no matter which directory you
#  launch it from -- "france_border.geojson" alone would be looked for in
#  whatever folder your terminal happens to be sitting in.
CACHE_PATH = Path(__file__).parent / BORDER_CACHE_FILE


def _cached_geojson_text() -> str:
    """Read the outline off the disk, downloading it first if it is not there yet.

    Raises:
        RuntimeError: if the file has to be downloaded and the download fails.
    """
    if not CACHE_PATH.exists():
        response = requests.get(BORDER_SOURCE_URL, timeout=30)
        if response.status_code != 200:
            raise RuntimeError(f"Error downloading the border of France: {response.status_code}")
        CACHE_PATH.write_bytes(response.content)
    return CACHE_PATH.read_text()


def load_border_polygons() -> list[list[list[list[float]]]]:
    """Return the outline grouped into polygons, keeping the holes separate.

    GeoJSON nests three levels deep here. A MultiPolygon is a list of POLYGONS;
    each polygon is a list of RINGS; each ring is a list of POINTS. Inside one
    polygon the FIRST ring is the land and any others are holes punched out of
    it -- France has exactly two: Llivia, the Spanish village surrounded by
    French territory, and the Etang de Berre lagoon next to Marseille.

    Use this when the difference matters (filling a shape); use
    load_border_rings below when it does not (tracing an outline).

    Returns:
        A list of polygons, each a list of rings, each a list of
        [longitude, latitude] points.

    Example:
        >>> polygons = load_border_polygons()
        >>> len(polygons)
        167
        >>> sum(1 for polygon in polygons if len(polygon) > 1)   # with holes
        1
    """
    geojson = json.loads(_cached_geojson_text())
    return geojson["geometry"]["coordinates"]


def load_border_rings() -> list[list[list[float]]]:
    """Return France's outline as a plain list of rings, downloading it once.

    A "ring" is one closed loop of points: the mainland is one, Corsica is
    another, every island is its own, and a few are holes punched inside a
    bigger loop. France needs 169 of them. Each point is a two-item list
    [longitude, latitude] -- note the order, GeoJSON puts longitude FIRST,
    which is the opposite of how we usually say it.

    Returns:
        A list of rings; each ring is a list of [longitude, latitude] points.

    Raises:
        RuntimeError: if the file has to be downloaded and the download fails.

    Example:
        >>> rings = load_border_rings()
        >>> len(rings)
        169
        >>> rings[0][0]
        [7.13035, 47.50303]
    """
    #  We do not care here which polygon a ring belongs to, nor whether it is
    #  land or a hole, so the two levels are flattened into one list of rings.
    rings = []
    for polygon in load_border_polygons():
        for ring in polygon:
            rings.append(ring)
    return rings


def load_border_path() -> MatplotlibPath:
    """Return the same outline as one Matplotlib Path object.

    A Path is Matplotlib's way of describing a shape made of several loops. We
    need it for two jobs the plain list of rings cannot do:
      - clipping, so the colours stop at the coast;
      - asking "is this point inside France?" for thousands of points at once.

    Building one means listing every point, plus a matching list of "codes"
    saying what to do at each point: MOVETO starts a new loop, LINETO continues
    it, CLOSEPOLY shuts it.

    Returns:
        A Path covering mainland France, Corsica and the coastal islands.

    Example:
        >>> border = load_border_path()
        >>> border.contains_point((2.35, 48.86))    # Paris
        True
        >>> border.contains_point((-0.13, 51.51))   # London
        False
    """
    all_points = []
    all_codes = []
    for ring in load_border_rings():
        for point in ring:
            all_points.append(point)

        #  A GeoJSON ring already repeats its first point at the end, and
        #  CLOSEPOLY is exactly the code for "that last point closes the loop",
        #  so the number of codes still matches the number of points.
        all_codes.append(MatplotlibPath.MOVETO)
        for _ in range(len(ring) - 2):
            all_codes.append(MatplotlibPath.LINETO)
        all_codes.append(MatplotlibPath.CLOSEPOLY)

    return MatplotlibPath(all_points, all_codes)


if __name__ == "__main__":
    border_rings = load_border_rings()
    total_points = sum(len(ring) for ring in border_rings)
    print(f"{len(border_rings)} rings, {total_points} points, cached in {CACHE_PATH.name}")
    france = load_border_path()
    for place, position in [("Paris", (2.35, 48.86)), ("London", (-0.13, 51.51))]:
        print(f"  {place:<8} inside France? {france.contains_point(position)}")
