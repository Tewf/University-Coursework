"""Draw text on a tkinter canvas so it stays readable over a busy background."""
import tkinter as tk
from typing import Literal, Sequence

# Where a label sits relative to the point it belongs to.
Anchor = Literal["w", "center", "e"]
# A tkinter font, as the family/size/style tuple the canvas accepts.
Font = tuple[str, int] | tuple[str, int, str]
# One line of a label: the text, the font to set it in, and its colour.
Line = tuple[str, Font, str]

PLATE_FILL, PLATE_EDGE = "#FFFFFF", "#AFBECD"
PLATE_PADDING = 4
# Stacking runs downwards from each line's top edge, so a line is anchored along
# its north side; these are the tkinter names for those three positions.
TOP_ANCHOR : dict[Anchor, Literal["nw", "n", "ne"]] = {
    "w": "nw", "center": "n", "e": "ne"}


def draw_plated_text(canvas : tk.Canvas, at : tuple[float, float],
                     lines : Sequence[Line], anchor : Anchor = "center",
                     tags : str = "") -> int:
    """Draw stacked lines of text at `at` over an opaque plate, and return the plate.

    Lines are drawn top to bottom from `at`, aligned on its x according to
    `anchor`. A canvas cannot outline or shade text, so the plate is measured
    from the text's own bounding box once the text exists and is then pushed
    underneath it; drawn in the other order there would be nothing to measure.
    Without the plate a label is illegible wherever the background has ink of
    its own. A label that would fall off the bottom is moved up to sit inside.
    """
    x, top = at
    items = []
    for text, font, colour in lines:
        item = canvas.create_text(x, top, text=text, font=font, fill=colour,
                                  anchor=TOP_ANCHOR[anchor], tags=tags)
        items.append(item)
        top = canvas.bbox(item)[3]

    boxes = [canvas.bbox(item) for item in items]
    plate = canvas.create_rectangle(
        min(box[0] for box in boxes) - PLATE_PADDING,
        min(box[1] for box in boxes) - PLATE_PADDING,
        max(box[2] for box in boxes) + PLATE_PADDING,
        max(box[3] for box in boxes) + PLATE_PADDING,
        fill=PLATE_FILL, outline=PLATE_EDGE, tags=tags)
    canvas.tag_lower(plate, items[0])

    # A label belonging to a point near the bottom would otherwise be drawn off
    # the canvas, where it is not clipped so much as simply never seen.
    overflow = canvas.bbox(plate)[3] - int(canvas.cget("height"))
    if overflow > 0:
        for item in (*items, plate):
            canvas.move(item, 0, -(overflow + PLATE_PADDING))
    return plate
