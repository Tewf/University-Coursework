# The two windows

The same map, drawn twice, on purpose. Question 6 asks for "a tkinter canvas",
and both of these are one — the difference is who fills it in.

| | `weather_map_matplotlib.py` | `weather_map_tkinter.py` |
|---|---|---|
| Who draws the map | Matplotlib | our own code |
| How it reaches the canvas | rendered to a PNG in memory, then `create_image` | painted pixel by pixel, then `create_image` |
| City dots and names | `create_oval` / `create_text` | `create_oval` / `create_text` |
| Colour scale | Matplotlib's `colorbar` | 695 `create_line` calls |
| Axes, degrees marked | yes | no |
| Instructions to write | 44 | 57 (+ 99 in the modules it needs) |

## Version 1 — let Matplotlib do it

The figure is saved to a `BytesIO`, which behaves like a file but never touches
the disk, and handed to `PhotoImage`. The clever part is placing the city dots
afterwards: rather than working out where each city ended up, we *ask*
Matplotlib, because it already knows —

```python
x, y = axes.transData.transform((longitude, latitude))
return x, figure.bbox.height - y
```

`transData` is the very transformation Matplotlib used to draw the map. The
subtraction flips the vertical axis, because Matplotlib counts pixels upwards
from the bottom and Tkinter counts them downwards from the top.

## Version 2 — do it yourself

Nothing is borrowed. `map_projection.py` works out where a coordinate goes,
`colour_scale.py` mixes the colours, `map_image.py` writes every pixel, and
`weather_map_tkinter.py` traces the coastline with `create_line`.

Matplotlib is still imported in one place — `france_border.load_border_path`,
used for the single-point "is Paris in France?" test. That is geometry, not
drawing, and it is not on the path the window actually takes.

## Which should you copy?

**Version 1**, for almost anything. It is shorter, it gets axes and a colour bar
for nothing, and Matplotlib has already solved the problems you have not met
yet. Version 2 exists so that none of it is magic — and because when you do need
to draw something Matplotlib has no chart for, this is how.

---

← [how it works](how-it-works.md)  ·  next: [reusing the code](reusing-the-code.md)
