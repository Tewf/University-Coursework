"""A tkinter map of France showing the current temperature in ten towns.

The whole program is this file. It fetches the map picture once, asks Open-Meteo
for every town in a single request, and writes each answer at the pixel that
town sits on. There is no map projection anywhere: each town already knows both
where it is on the picture and where it is on Earth, so nothing has to convert
between the two at run time.

To change what the map shows, see TOWNS below; to change how it looks, see the
drawing constants under it. Both are meant to be edited.
"""
import tkinter as tk
from pathlib import Path
from typing import NamedTuple

import requests

# --- the map picture -------------------------------------------------------

MAP_FILE = Path(__file__).parent / "france_map.png"
MAP_URL = ("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/"
           "France_location_map-Regions_and_departements-2016.svg/"
           "960px-France_location_map-Regions_and_departements-2016.svg.png")
# The pixels in TOWNS describe this picture at this size and no other, so the
# size is checked on load rather than assumed. See `main`.
MAP_SIZE = (960, 923)
ATTRIBUTION = "Map: Superbenjamin / Wikimedia Commons, CC BY-SA 4.0"
# Wikimedia answers requests that do not identify themselves with 403.
USER_AGENT = "TP1-WeatherMapApp/1.0 (https://github.com/Tewf; university coursework)"

# --- the weather API -------------------------------------------------------

FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
REQUEST_TIMEOUT_SECONDS = 10
DOWNLOAD_TIMEOUT_SECONDS = 30


class Town(NamedTuple):
    """One place on the map: where it is on the picture, and where it is on Earth.

    `x` and `y` are pixels on the map image and decide where the reading is
    drawn. `latitude` and `longitude` are decimal degrees and are what gets sent
    to the weather API. They describe the same place twice on purpose, which is
    what removes the need for a projection.
    """

    x : int
    y : int
    latitude : float
    longitude : float


# The places the map shows. This is the table to edit: adding a town here is the
# only change needed, and removing one is a deleted line.
#
# To find x and y for a new town, convert its degrees with the geographic box
# this picture is published with (west -5.8, south 41.0, east 10.0, north 51.5):
#
#     x = (longitude - -5.8) / (10.0 - -5.8) * 960
#     y = (51.5 - latitude)  / (51.5 - 41.0) * 923
#
# Latitude subtracts the other way round because pixels count down the screen
# while degrees count up the globe. The box comes from Wikipedia's location-map
# data for France, which is why this particular picture was chosen:
# https://en.wikipedia.org/wiki/Module:Location_map/data/France
#
# Two towns closer than about a hundred kilometres overlap each other's labels
# at this size, which is why Lyon and Nice are absent: they sit on Grenoble and
# Marseille. `test_no_two_towns_share_a_label_position` catches only exact ties.
TOWNS : dict[str, Town] = {
    "Lille":      Town(538,  77, 50.6292,  3.0573),
    "Brest":      Town( 80, 273, 48.3904, -4.4861),
    "Paris":      Town(495, 232, 48.8566,  2.3522),
    "Strasbourg": Town(823, 257, 48.5734,  7.7521),
    "Nantes":     Town(258, 376, 47.2184, -1.5536),
    "Bordeaux":   Town(317, 586, 44.8378, -0.5792),
    "Grenoble":   Town(700, 555, 45.1830,  5.7245),
    "Toulouse":   Town(440, 694, 43.6047,  1.4442),
    "Marseille":  Town(679, 721, 43.2965,  5.3698),
    "Ajaccio":    Town(883, 842, 41.9267,  8.7369),
}

# --- how it looks ----------------------------------------------------------

# Upper bound in degrees Celsius, and the colour for everything below it. Read in
# order, so the first bound a temperature falls under wins. Tunable on sight:
# these are display thresholds, not meteorology.
TEMPERATURE_COLOURS = ((0.0, "#4A6FA5"), (10.0, "#5B9BB5"), (16.0, "#5EA37E"),
                       (22.0, "#B4820E"), (28.0, "#C97A3B"))
HOTTEST_COLOUR = "#C63B3B"

INK, FAINT = "#16222E", "#5C6B7A"
PLATE_FILL, PLATE_EDGE = "#FFFFFF", "#AFBECD"
LABEL_FONT = ("helvetica", 10, "bold")
# "helvetica" rather than a named desktop font: the interpreter uv installs
# bundles a Tk built without fontconfig, which sees 65 core X11 families where
# the system one sees 445. A family it cannot find is not an error there, it is
# a silent fall back to a bitmap face, so this asks for one Tk always resolves.
CREDIT_FONT = ("helvetica", 8)
DOT_RADIUS = 5
LABEL_GAP = 9                       # from a dot's centre down to its label
PLATE_PADDING_X, PLATE_PADDING_Y = 4, 3


def download_map(path : Path = MAP_FILE) -> Path:
    """Return the map image, fetching it once if it is not already on disk.

    The picture is not committed, so the first run downloads it and every run
    after that is offline. Raises requests.HTTPError if Wikimedia refuses the
    request, and requests.Timeout if it does not answer in time.
    """
    if not path.exists():
        response = requests.get(MAP_URL, headers={"User-Agent": USER_AGENT},
                                timeout=DOWNLOAD_TIMEOUT_SECONDS)
        response.raise_for_status()
        path.write_bytes(response.content)
    return path


def fetch_temperatures(towns : dict[str, Town] | None = None) -> list[float]:
    """Return each town's current temperature, in the order the table lists them.

    Open-Meteo accepts comma-separated coordinate lists and answers with one
    block per location in the order asked, so any number of towns costs a single
    round trip. Defaults to TOWNS; pass a table to query somewhere else.
    Raises requests.HTTPError if the API answers with an error status.
    """
    places = list((towns if towns is not None else TOWNS).values())
    response = requests.get(FORECAST_URL, timeout=REQUEST_TIMEOUT_SECONDS, params={
        "latitude": ",".join(str(town.latitude) for town in places),
        "longitude": ",".join(str(town.longitude) for town in places),
        "current": "temperature_2m"})
    response.raise_for_status()
    return [block["current"]["temperature_2m"] for block in response.json()]


def colour_for(celsius : float) -> str:
    """Return the hex colour standing for a temperature on the map."""
    for upper_bound, colour in TEMPERATURE_COLOURS:
        if celsius < upper_bound:
            return colour
    return HOTTEST_COLOUR


def draw_reading(canvas : tk.Canvas, town : Town,
                 name : str, celsius : float) -> None:
    """Draw one town: a dot coloured by its temperature, and a label beneath it.

    The label sits on a white plate because a canvas cannot outline or shade
    text and the map has ink of its own. The plate is drawn after the text so it
    can be measured from the text's own bounding box, then pushed underneath;
    drawn in the other order there would be nothing to measure.
    """
    canvas.create_oval(town.x - DOT_RADIUS, town.y - DOT_RADIUS,
                       town.x + DOT_RADIUS, town.y + DOT_RADIUS,
                       fill=colour_for(celsius), outline=INK)
    label = canvas.create_text(town.x, town.y + LABEL_GAP, anchor="n",
                               justify="center", font=LABEL_FONT, fill=INK,
                               text=f"{name}\n{celsius:.1f} °C")
    left, top, right, bottom = canvas.bbox(label)
    plate = canvas.create_rectangle(left - PLATE_PADDING_X, top - PLATE_PADDING_Y,
                                    right + PLATE_PADDING_X, bottom + PLATE_PADDING_Y,
                                    fill=PLATE_FILL, outline=PLATE_EDGE)
    canvas.tag_lower(plate, label)


def main() -> None:
    """Open the window, fill it with the current temperatures, and run it."""
    root = tk.Tk()
    root.title("Current weather · France · Open-Meteo")

    # This name has to stay alive for as long as the window does: tkinter keeps
    # no reference of its own, and a collected image leaves a blank canvas with
    # no error to explain it.
    image = tk.PhotoImage(file=download_map())
    if (image.width(), image.height()) != MAP_SIZE:
        raise SystemExit(
            f"Map image is {image.width()}x{image.height()}, expected "
            f"{MAP_SIZE[0]}x{MAP_SIZE[1]}. The pixels in TOWNS belong to that "
            "size, so every town would be placed wrongly. Delete "
            f"{MAP_FILE.name} to fetch it again, or recompute TOWNS.")

    canvas = tk.Canvas(root, width=image.width(), height=image.height(),
                       highlightthickness=0, bd=0)
    canvas.pack()
    canvas.create_image(0, 0, anchor="nw", image=image)
    for (name, town), celsius in zip(TOWNS.items(), fetch_temperatures()):
        draw_reading(canvas, town, name, celsius)

    tk.Label(root, text=ATTRIBUTION, fg=FAINT, font=CREDIT_FONT,
             anchor="e", padx=10, pady=4).pack(fill="x")
    root.mainloop()


if __name__ == "__main__":
    main()
