"""The tkinter window: a map image of France with each town's weather drawn on it."""
import tkinter as tk

from canvas_labels import Anchor, draw_plated_text
from current_weather import query_current_weather_at
from france_map_image import ATTRIBUTION, MAP_BOUNDS, ensure_map_image
from locations import FRANCE
from map_projection import ImageProjection
from weather_codes import describe, temperature_colour

INK, FAINT = "#16222E", "#5C6B7A"
# "helvetica" rather than a named desktop font: the interpreter uv installs
# bundles a Tk built without fontconfig, which sees 65 core X11 families instead
# of the system's 445. A family it cannot find is not an error there, it is a
# silent fall back to a bitmap face, so this asks for one of the 65 by a name Tk
# resolves to a scalable font in either environment.
NAME_FONT = ("helvetica", 9)
READING_FONT = ("helvetica", 13, "bold")
SKY_FONT = ("helvetica", 8)
DOT_RADIUS = 5
LABEL_GAP = 10          # from a dot's centre down to the top of its label
EDGE_MARGIN = 60        # how near an edge a label may sit before it shifts inwards


class WeatherMap(tk.Frame):
    """A window showing every town in `locations.FRANCE` with its current weather.

    Drawing is split from fetching: the map is on screen as soon as the window
    opens and `refresh` adds the weather when the API answers, so nothing is
    blank while a request is in flight. One request covers every town, so a
    refresh costs a single round trip however many towns there are.
    """

    def __init__(self, master : tk.Misc):
        super().__init__(master)
        # This reference must outlive the constructor: tkinter keeps none of its
        # own, and a garbage-collected PhotoImage leaves the canvas silently blank.
        self.map_image = tk.PhotoImage(file=ensure_map_image())
        # The image's real size, not the width that was asked for: Commons serves
        # whichever rendering it already holds, so the file decides the geometry.
        width, height = self.map_image.width(), self.map_image.height()
        self.projection = ImageProjection(MAP_BOUNDS, width, height)

        self.canvas = tk.Canvas(self, width=width, height=height,
                                highlightthickness=0, bd=0)
        self.canvas.pack(fill="both", expand=True)
        footer = tk.Frame(self)
        footer.pack(fill="x")
        self.status = tk.Label(footer, text="", fg=FAINT, font=NAME_FONT,
                               anchor="w", padx=12, pady=6)
        self.status.pack(side="left")
        tk.Label(footer, text=ATTRIBUTION, fg=FAINT, font=SKY_FONT,
                 anchor="e", padx=12, pady=6).pack(side="right")
        self.canvas.create_image(0, 0, anchor="nw", image=self.map_image)

    def refresh(self) -> None:
        """Fetch the current weather for every town and draw it over the map."""
        self.canvas.delete("weather")
        self.status.config(text="Asking Open-Meteo…")
        self.update_idletasks()

        responses = query_current_weather_at(list(FRANCE.values()))
        for (name, (latitude, longitude)), response in zip(FRANCE.items(), responses):
            self.draw_location(name, latitude, longitude, response["current"])

        when = responses[0]["current"]["time"].replace("T", " ") if responses else "?"
        self.status.config(text=f"Open-Meteo · local time at each town · {when}")

    def draw_location(self, name : str, latitude : float, longitude : float,
                      current : dict) -> None:
        """Draw one town: a dot coloured by temperature, and its readings below it."""
        x, y = self.projection.project(latitude, longitude)
        celsius = current["temperature_2m"]
        colour = temperature_colour(celsius)

        self.canvas.create_oval(x - DOT_RADIUS, y - DOT_RADIUS,
                                x + DOT_RADIUS, y + DOT_RADIUS,
                                fill=colour, outline=INK, width=1, tags="weather")
        draw_plated_text(self.canvas, (x, y + LABEL_GAP),
                         [(name, NAME_FONT, INK),
                          (f"{celsius:.1f} °C", READING_FONT, colour),
                          (describe(current["weather_code"]), SKY_FONT, FAINT)],
                         anchor=self.label_anchor(x), tags="weather")

    def label_anchor(self, x : float) -> Anchor:
        """Return the anchor keeping a label at `x` inside the map.

        Near the right edge the text has to extend leftwards, near the left edge
        rightwards, and anywhere else it is centred on its dot.
        """
        if x > self.map_image.width() - EDGE_MARGIN:
            return "e"
        if x < EDGE_MARGIN:
            return "w"
        return "center"


def build_window() -> tuple[tk.Tk, WeatherMap]:
    """Create the window and its map without entering the event loop.

    Returned separately from `run` so a caller can draw, inspect or export the
    window without blocking on `mainloop`.
    """
    root = tk.Tk()
    root.title("Current weather · France · Open-Meteo")
    weather_map = WeatherMap(root)
    weather_map.pack(fill="both", expand=True)
    return root, weather_map


def run() -> None:
    """Open the window, fill it with the current weather, and hand over to tkinter."""
    root, weather_map = build_window()
    weather_map.refresh()
    root.mainloop()
