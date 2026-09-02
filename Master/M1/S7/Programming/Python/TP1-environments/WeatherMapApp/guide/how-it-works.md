# How it works

Six steps, from a web address to a coloured window.

```
  meteo.py            one HTTP request  ->  {"Lyon": 29.3, "Brest": 19.8, ...}
        |
  temperature_map.py  a weighted average ->  a temperature for all 460 000 pixels
        |
  france_border.py    a downloaded outline ->  169 loops of coordinates
        |
  colour_scale.py     a temperature      ->  "#b40426"
  map_projection.py   a longitude/latitude ->  an (x, y) on the canvas
        |
  map_image.py        all of the above   ->  one picture
        |
  weather_map_*.py    the picture        ->  a window you can look at
```

## 1. Ask for the weather — once

`fetch_city_temperatures` sends **one** request for all twelve cities, because
Open-Meteo accepts a comma-separated list of coordinates:

```
?latitude=50.62,48.39,48.85,...&longitude=3.05,-4.48,2.35,...
```

Twelve separate requests took 1.9 s and gave exactly the same answers as the one
request, which takes 0.2 s. The free tier allows 600 calls a minute, so twelve
was never going to be refused — it was just wasteful.

One trap: asking about **one** place returns a `dict`, asking about **several**
returns a `list`. Code that assumes a list would loop over the dict's *keys* and
produce nonsense without ever raising an error, so `fetch_city_temperatures`
checks with `isinstance` before looping.

## 2. Fill in the gaps

We know twelve temperatures and need 460 000. Each pixel takes a weighted
average of all twelve cities, with nearby cities weighing more — see
[the maths](the-maths.md).

## 3. Cut France out of the rectangle

The interpolation happily produces a temperature for the middle of the Atlantic,
so the coloured rectangle is cut down to the actual country. The two windows do
this differently: Matplotlib clips the image to a path, while the Tkinter one
builds a true/false mask of where the land is.

## 4. Colour, place, paint, show

A temperature becomes a colour, a longitude and latitude become an x and a y,
every pixel is written into one image, and the image goes on a `tkinter.Canvas`
with the city dots drawn on top of it.

---

← [guide](README.md)  ·  next: [the two windows](the-two-windows.md)
