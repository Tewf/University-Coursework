"""The tkinter window: France drawn on a canvas, with the current weather on it."""
import tkinter as tk
from typing import Literal

from current_weather import query_current_weather_at
from france_outline import load_border_rings
from locations import FRANCE
from map_projection import MapProjection, geographic_bounds
from weather_codes import describe, temperature_colour

CANVAS_WIDTH, CANVAS_HEIGHT = 900, 760
SEA, LAND, COAST, INK, FAINT = "#0F1B2A", "#1C3047", "#4A6FA5", "#E7EEF6", "#93A5BA"
DOT_RADIUS = 6
# Where a label sits relative to its dot; tkinter names these positions.
Anchor = Literal["w", "center", "e"]
# How close to an edge a label may sit before it is anchored inwards instead.
EDGE_MARGIN = 110


class WeatherMap(tk.Frame):
    """A canvas showing every location in `locations.FRANCE` with its weather.

    Drawing is split from fetching: `draw_map` puts up the coastline immediately,
    and `refresh` fills in the weather when the API answers, so the window is
    never blank while the request is in flight. One request covers all the
    locations, so refreshing costs a single round trip.
    """

    def __init__(self, master : tk.Misc):
        super().__init__(master, bg=SEA)
        self.canvas = tk.Canvas(self, width=CANVAS_WIDTH, height=CANVAS_HEIGHT,
                                bg=SEA, highlightthickness=0, bd=0)
        self.canvas.pack(fill="both", expand=True)
        self.status = tk.Label(self, text="", bg=SEA, fg=FAINT,
                               font=("DejaVu Sans", 10), anchor="w", padx=14, pady=8)
        self.status.pack(fill="x")

        rings = load_border_rings()
        self.projection = MapProjection(geographic_bounds(rings),
                                        CANVAS_WIDTH, CANVAS_HEIGHT)
        self.draw_map(rings)

    def draw_map(self, rings : list[list[tuple[float, float]]]) -> None:
        """Draw the sea and the coastline. Called once; the weather goes over it."""
        # The sea is a drawn item rather than the widget's background colour, so
        # that canvas.postscript() exports what the window actually shows.
        self.canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT,
                                     fill=SEA, outline=SEA)
        for ring in rings:
            points = self.projection.project_ring(ring)
            if len(points) >= 6:                      # a polygon needs three points
                self.canvas.create_polygon(points, fill=LAND, outline=COAST, width=1)

    def refresh(self) -> None:
        """Fetch the current weather for every location and draw it on the map."""
        self.canvas.delete("weather")
        self.status.config(text="Asking Open-Meteo…")
        self.update_idletasks()

        responses = query_current_weather_at(list(FRANCE.values()))
        for (name, (latitude, longitude)), response in zip(FRANCE.items(), responses):
            self.draw_location(name, latitude, longitude, response["current"])

        when = responses[0]["current"]["time"].replace("T", " ") if responses else "?"
        self.status.config(text=f"Open-Meteo, local time at each location · {when}")

    def draw_location(self, name : str, latitude : float, longitude : float,
                      current : dict) -> None:
        """Draw one location: a dot coloured by temperature, and its readings."""
        x, y = self.projection.project(latitude, longitude)
        celsius = current["temperature_2m"]
        colour = temperature_colour(celsius)

        self.canvas.create_oval(x - DOT_RADIUS, y - DOT_RADIUS,
                                x + DOT_RADIUS, y + DOT_RADIUS,
                                fill=colour, outline=SEA, width=2, tags="weather")
        # Centred text runs off the canvas for anything near an edge -- Brest and
        # Strasbourg both do. Anchoring the label towards the middle keeps it in.
        anchor = self.label_anchor(x)
        self.canvas.create_text(x, y - 16, text=f"{name}  {celsius:.1f}°C",
                                fill=INK, font=("DejaVu Sans", 11, "bold"),
                                anchor=anchor, tags="weather")
        self.canvas.create_text(x, y + 17, text=describe(current["weather_code"]),
                                fill=FAINT, font=("DejaVu Sans", 9),
                                anchor=anchor, tags="weather")

    @staticmethod
    def label_anchor(x : float) -> Anchor:
        """Return the tkinter anchor keeping a label at `x` inside the canvas.

        Near the right edge the text has to extend leftwards ("e"), near the left
        edge rightwards ("w"), and anywhere else it is centred.
        """
        if x > CANVAS_WIDTH - EDGE_MARGIN:
            return "e"
        if x < EDGE_MARGIN:
            return "w"
        return "center"


def build_window() -> tuple[tk.Tk, WeatherMap]:
    """Create the application window and its map, without entering the event loop.

    Returned separately from `run` so a caller can draw, inspect or screenshot the
    window without blocking on `mainloop`.
    """
    root = tk.Tk()
    root.title("Current weather · France · Open-Meteo")
    root.configure(bg=SEA)
    weather_map = WeatherMap(root)
    weather_map.pack(fill="both", expand=True)
    return root, weather_map


def run() -> None:
    """Open the window, fill it with the current weather, and hand over to tkinter."""
    root, weather_map = build_window()
    weather_map.refresh()
    root.mainloop()
