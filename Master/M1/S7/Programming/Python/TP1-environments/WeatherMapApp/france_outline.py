"""Read the France border rings out of the GeoJSON file sitting beside this one."""
import json
from pathlib import Path

BORDER_FILE = Path(__file__).parent / "france_border.geojson"

# One closed ring of the coastline, as (longitude, latitude) pairs -- GeoJSON's
# own axis order, which is the reverse of how coordinates are usually spoken.
Ring = list[tuple[float, float]]


def load_border_rings(path : Path = BORDER_FILE) -> list[Ring]:
    """Return every ring of the border, flattened across polygons.

    The file is a GeoJSON Feature whose geometry is a MultiPolygon: one polygon
    per landmass (the mainland, Corsica, the larger islands), each made of an
    outer ring and any holes. Holes are returned alongside outer rings because
    drawing an outline treats them identically; a filled renderer would not.
    Raises FileNotFoundError naming the download if the file is absent, since
    it is deliberately not committed.
    """
    if not path.exists():
        raise FileNotFoundError(
            f"{path.name} is missing. It is not committed; download it with:\n"
            "  curl -sSLo france_border.geojson https://raw.githubusercontent.com/"
            "gregoiredavid/france-geojson/master/metropole-version-simplifiee.geojson")
    geometry = json.loads(path.read_text())["geometry"]
    return [[(point[0], point[1]) for point in ring]
            for polygon in geometry["coordinates"] for ring in polygon]
