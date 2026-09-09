"""Place geographic coordinates on a georeferenced map image."""

Bounds = tuple[float, float, float, float]     # west, south, east, north


class ImageProjection:
    """Maps latitude and longitude onto the pixels of a georeferenced image.

    The image must be an equidistant cylindrical rendering whose four edges are
    the given bounds, which is what a Wikipedia location map is. On such an
    image both axes are linear in degrees, so placing a point is interpolation
    and nothing else. No cosine appears here even though a degree of longitude
    is shorter than a degree of latitude: that correction is already spent, as
    the ratio the image was drawn at. Pass bounds belonging to a different image
    and every point is wrong by the same silent amount, which is why the two
    travel together.
    """

    def __init__(self, bounds : Bounds, width : int, height : int):
        self._west, self._south, self._east, self._north = bounds
        if self._east <= self._west or self._north <= self._south:
            raise ValueError("Bounds must enclose a positive area")
        if width <= 0 or height <= 0:
            raise ValueError("An image must have a positive size")
        self._width, self._height = width, height

    def project(self, latitude : float, longitude : float) -> tuple[float, float]:
        """Return the (x, y) pixel a latitude and longitude falls on.

        A location outside the bounds projects outside the image rather than
        being clamped to its edge, so that `contains` stays the only thing
        deciding whether a location belongs on the map.
        """
        x = (longitude - self._west) / (self._east - self._west) * self._width
        # Pixel y grows downwards while latitude grows upwards, hence the flip.
        y = (self._north - latitude) / (self._north - self._south) * self._height
        return x, y

    def contains(self, latitude : float, longitude : float) -> bool:
        """Whether a location falls within the area the image covers."""
        return (self._west <= longitude <= self._east
                and self._south <= latitude <= self._north)
