#ifndef SVG_H
#define SVG_H

#include <stddef.h>

#include "cell.h"
#include "maze.h"

/* Everything the drawing lets a caller choose, so that no size or colour is
   written into the drawing code. */
typedef struct {
    int cell_size;   /* side of one cell, in SVG units */
    int margin;      /* blank border around the maze */
    int wall_width;
    int route_width;
    const char *wall_colour;
    const char *route_colour;
    const char *exit_colour;
} SvgStyle;

/* The defaults, so that a caller who does not care writes nothing. */
SvgStyle svg_default_style(void);

/* Writes the maze to filename as SVG: one line per wall, plus the outer
   boundary, which is drawn closed because the exit is a cell and not a gap.

   route, when non-NULL, is drawn through the centres of its cells. exit_cell,
   when non-NULL, is filled. Returns 0 if the file cannot be written. */
int svg_write_maze(const Maze *maze, const char *filename, const Cell *route,
                   size_t route_length, const Cell *exit_cell,
                   const SvgStyle *style);

#endif /* SVG_H */
