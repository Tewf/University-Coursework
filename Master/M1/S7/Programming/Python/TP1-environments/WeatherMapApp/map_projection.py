"""Place geographic coordinates on a canvas without stretching the map sideways."""
from math import cos, radians

Bounds = tuple[float, float, float, float]   # lon_min, lat_min, lon_max, lat_max


def geographic_bounds(rings : list[list[tuple[float, float]]]) -> Bounds:
    """Return the (lon_min, lat_min, lon_max, lat_max) box enclosing every ring.

    Raises ValueError when there is nothing to enclose.
    """
    points = [point for ring in rings for point in ring]
    if not points:
        raise ValueError("No coordinates to take bounds of")
    longitudes = [longitude for longitude, _ in points]
    latitudes = [latitude for _, latitude in points]
    return min(longitudes), min(latitudes), max(longitudes), max(latitudes)


class MapProjection:
    """Equidistant cylindrical projection, fitted to a canvas of a given size.

    A degree of longitude is shorter than a degree of latitude everywhere but
    the equator, so plotting longitude directly against latitude makes France
    look too wide. Multiplying longitude by the cosine of a standard parallel --
    here the middle of the area drawn -- restores the proportions.
    One scale factor is used for both axes, so shapes keep their aspect ratio
    and the map is centred in whatever space is left over.
    """

    def __init__(self, bounds : Bounds, width : int, height : int, margin : int = 24):
        lon_min, lat_min, lon_max, lat_max = bounds
        if lon_max <= lon_min or lat_max <= lat_min:
            raise ValueError("Bounds must enclose a positive area")
        self._longitude_scale = cos(radians((lat_min + lat_max) / 2))

        span_x = (lon_max - lon_min) * self._longitude_scale
        span_y = lat_max - lat_min
        usable_width, usable_height = width - 2 * margin, height - 2 * margin
        self._scale = min(usable_width / span_x, usable_height / span_y)

        self._origin_x = (margin + (usable_width - span_x * self._scale) / 2
                          - lon_min * self._longitude_scale * self._scale)
        # Canvas y grows downwards while latitude grows upwards, hence the flip.
        self._origin_y = (margin + (usable_height - span_y * self._scale) / 2
                          + lat_max * self._scale)

    def project(self, latitude : float, longitude : float) -> tuple[float, float]:
        """Return the (x, y) canvas pixel for a latitude and longitude."""
        return (longitude * self._longitude_scale * self._scale + self._origin_x,
                self._origin_y - latitude * self._scale)

    def project_ring(self, ring : list[tuple[float, float]]) -> list[float]:
        """Project a ring of (longitude, latitude) points into a flat x, y, x, y list.

        Flat because that is the shape tkinter's canvas polygon and line items
        take; note the argument order is GeoJSON's, longitude first.
        """
        return [coordinate
                for longitude, latitude in ring
                for coordinate in self.project(latitude, longitude)]
