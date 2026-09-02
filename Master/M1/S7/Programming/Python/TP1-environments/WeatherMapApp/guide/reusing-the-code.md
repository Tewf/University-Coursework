# Reusing the code

Every module works on its own. Copy the file, or import from it — nothing here
needs the window to be running. All of these snippets are tested.

## Get the weather for one place

```python
from meteo import query_open_meteo, extract_current_temperature

answer = query_open_meteo(45.183, 5.7245)        # Grenoble
print(extract_current_temperature(answer))       # 30.7, whatever it is right now
```

## Get many places, in one request

```python
from meteo import fetch_city_temperatures

fetch_city_temperatures({"Lyon": (45.764, 4.8357), "Brest": (48.3904, -4.4861)})
# {'Lyon': 29.3, 'Brest': 19.8}  — live, so yours will differ
```

Pass your own dict — it does not have to be French, or a city.

## Save the map as a picture, with no window at all

Useful in a Jupyter notebook, or for a report:

```python
from matplotlib.figure import Figure
from meteo import fetch_city_temperatures
from configuration import CITY_COORDINATES
from plots import draw_temperature_map

figure = Figure(figsize=(8, 7.5), layout="constrained")
draw_temperature_map(figure.add_subplot(), fetch_city_temperatures(CITY_COORDINATES))
figure.savefig("france.png", dpi=150)
```

`draw_temperature_map` takes the axes to draw *on*, which is why the same call
works for a PNG, a notebook cell and a window. Write your own drawing functions
that way and they will travel just as well.

## Colour your own numbers

Nothing in `colour_scale.py` knows about temperature:

```python
from colour_scale import temperature_to_colour

temperature_to_colour(72, coldest=0, hottest=100)   # '#de8e7b' — a score out of 100
```

## Interpolate your own measurements

Rainfall, population, prices — anything measured in a few places and wanted
everywhere:

```python
from temperature_map import build_grid, interpolate

longitudes, latitudes = build_grid(columns=200)
field = interpolate({"Lyon": 12.0, "Brest": 3.5}, longitudes, latitudes)
```

The names say "temperature" because that is this application's job, but the
arithmetic does not care what the numbers mean. The one requirement is that the
keys exist in `CITY_COORDINATES`.

## Map somewhere else entirely

Change the four bounds in `configuration.py` and put your own places in
`CITY_COORDINATES`. `map_projection.py` recomputes the width so the shape stays
right, and both windows follow. The one thing that will not follow is the
outline — `BORDER_SOURCE_URL` points at a file that only contains France.

---

← [the two windows](the-two-windows.md)  ·  next: [the maths](the-maths.md)
