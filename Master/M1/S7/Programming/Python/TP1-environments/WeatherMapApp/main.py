"""A tkinter map of France showing the current temperature in ten towns.

The whole program is this file: fetch the map picture once, ask Open-Meteo for
every town in a single request, and write each answer at the pixel that town
sits on. The pixel positions are part of the table below, so nothing here has
to know anything about map projections.
"""
import tkinter as tk
from pathlib import Path

import requests

MAP_FILE = Path(__file__).parent / "france_map.png"
MAP_URL = ("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/"
           "France_location_map-Regions_and_departements-2016.svg/"
           "960px-France_location_map-Regions_and_departements-2016.svg.png")
MAP_SIZE = (960, 923)
ATTRIBUTION = "Map: Superbenjamin / Wikimedia Commons, CC BY-SA 4.0"
# Wikimedia answers requests that do not identify themselves with 403.
USER_AGENT = "TP1-WeatherMapApp/1.0 (https://github.com/Tewf; university coursework)"

FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
REQUEST_TIMEOUT_SECONDS = 10

# name: (x, y on the map image, latitude, longitude).
# The two halves are the same place said twice: where the town is on this
# picture, and where it is on Earth. The pixels were computed from the map's
# published geographic bounds rather than measured by eye, and they belong to
# this image at MAP_SIZE -- a different picture needs a different column.
TOWNS : dict[str, tuple[int, int, float, float]] = {
    "Lille": (538, 77, 50.6292, 3.0573),
    "Brest": (80, 273, 48.3904, -4.4861),
    "Paris": (495, 232, 48.8566, 2.3522),
    "Strasbourg": (823, 257, 48.5734, 7.7521),
    "Nantes": (258, 376, 47.2184, -1.5536),
    "Bordeaux": (317, 586, 44.8378, -0.5792),
    "Grenoble": (700, 555, 45.1830, 5.7245),
    "Toulouse": (440, 694, 43.6047, 1.4442),
    "Marseille": (679, 721, 43.2965, 5.3698),
    "Ajaccio": (883, 842, 41.9267, 8.7369),
}

# Upper bound in degrees Celsius, and the colour for everything below it. Read
# in order, so the first bound a temperature falls under wins.
TEMPERATURE_COLOURS = ((0.0, "#4A6FA5"), (10.0, "#5B9BB5"), (16.0, "#5EA37E"),
                       (22.0, "#B4820E"), (28.0, "#C97A3B"))
HOTTEST_COLOUR = "#C63B3B"


def download_map(path : Path = MAP_FILE) -> Path:
    """Return the map image, fetching it once if it is not already on disk.

    The picture is not committed, so the first run downloads it and every run
    after that is offline. Raises requests.HTTPError if Wikimedia refuses.
    """
    if not path.exists():
        response = requests.get(MAP_URL, headers={"User-Agent": USER_AGENT},
                                timeout=REQUEST_TIMEOUT_SECONDS * 3)
        response.raise_for_status()
        path.write_bytes(response.content)
    return path


def fetch_temperatures() -> list[float]:
    """Return the current temperature of every town, in the order TOWNS lists them.

    Open-Meteo accepts comma-separated coordinate lists and answers with one
    block per location in the order asked, so ten towns cost one round trip
    rather than ten. Raises requests.HTTPError if the API answers with an error.
    """
    response = requests.get(FORECAST_URL, timeout=REQUEST_TIMEOUT_SECONDS, params={
        "latitude": ",".join(str(latitude) for _, _, latitude, _ in TOWNS.values()),
        "longitude": ",".join(str(longitude) for *_, longitude in TOWNS.values()),
        "current": "temperature_2m"})
    response.raise_for_status()
    return [block["current"]["temperature_2m"] for block in response.json()]


def colour_for(celsius : float) -> str:
    """Return the hex colour standing for a temperature on the map."""
    for upper_bound, colour in TEMPERATURE_COLOURS:
        if celsius < upper_bound:
            return colour
    return HOTTEST_COLOUR


def draw_reading(canvas : tk.Canvas, x : int, y : int,
                 name : str, celsius : float) -> None:
    """Draw one town at (x, y): a dot coloured by temperature, and a label under it.

    The label sits on a white plate because a canvas cannot outline text and the
    map has ink of its own. The plate is drawn after the text so it can be sized
    from the text's own bounding box, then pushed underneath it.
    """
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5,
                       fill=colour_for(celsius), outline="#16222E")
    label = canvas.create_text(x, y + 9, anchor="n", justify="center",
                               text=f"{name}\n{celsius:.1f} °C",
                               font=("helvetica", 10, "bold"), fill="#16222E")
    left, top, right, bottom = canvas.bbox(label)
    plate = canvas.create_rectangle(left - 4, top - 3, right + 4, bottom + 3,
                                    fill="#FFFFFF", outline="#AFBECD")
    canvas.tag_lower(plate, label)


def main() -> None:
    """Open the window, fill it with the current temperatures, and run it."""
    root = tk.Tk()
    root.title("Current weather · France · Open-Meteo")

    # This name has to stay alive for as long as the window does: tkinter keeps
    # no reference of its own, and a collected image leaves a blank canvas.
    image = tk.PhotoImage(file=download_map())
    if (image.width(), image.height()) != MAP_SIZE:
        raise SystemExit(f"Map image is {image.width()}x{image.height()}, expected "
                         f"{MAP_SIZE[0]}x{MAP_SIZE[1]}; the pixels in TOWNS are for "
                         "that size, so every town would be placed wrongly.")

    canvas = tk.Canvas(root, width=image.width(), height=image.height(),
                       highlightthickness=0, bd=0)
    canvas.pack()
    canvas.create_image(0, 0, anchor="nw", image=image)
    for (name, (x, y, _, _)), celsius in zip(TOWNS.items(), fetch_temperatures()):
        draw_reading(canvas, x, y, name, celsius)

    tk.Label(root, text=ATTRIBUTION, fg="#5C6B7A", font=("helvetica", 8),
             anchor="e", padx=10, pady=4).pack(fill="x")
    root.mainloop()


if __name__ == "__main__":
    main()
