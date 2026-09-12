#include "svg.h"

#include <stdio.h>

SvgStyle svg_default_style(void) {
    SvgStyle style;
    style.cell_size = 20;
    style.margin = 10;
    style.wall_width = 2;
    style.route_width = 3;
    style.wall_colour = "#222222";
    style.route_colour = "#1565C0";
    style.exit_colour = "#E65100";
    return style;
}

static int at(const SvgStyle *style, int grid) {
    return style->margin + grid * style->cell_size;
}

static int centre(const SvgStyle *style, int grid) {
    return at(style, grid) + style->cell_size / 2;
}

static void line(FILE *out, int x1, int y1, int x2, int y2, const char *colour,
                 int width) {
    fprintf(out,
            "  <line x1=\"%d\" y1=\"%d\" x2=\"%d\" y2=\"%d\" stroke=\"%s\""
            " stroke-width=\"%d\" stroke-linecap=\"square\"/>\n",
            x1, y1, x2, y2, colour, width);
}

int svg_write_maze(const Maze *maze, const char *filename, const Cell *route,
                   size_t route_length, const Cell *exit_cell,
                   const SvgStyle *style) {
    SvgStyle defaults = svg_default_style();
    FILE *out;
    int width;
    int height;
    int x;
    int y;
    size_t i;

    if (style == NULL) {
        style = &defaults;
    }
    out = fopen(filename, "w");
    if (out == NULL) {
        return 0;
    }
    width = 2 * style->margin + maze_width(maze) * style->cell_size;
    height = 2 * style->margin + maze_height(maze) * style->cell_size;

    fprintf(out,
            "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"%d\""
            " height=\"%d\" viewBox=\"0 0 %d %d\">\n",
            width, height, width, height);
    fprintf(out, "  <rect width=\"100%%\" height=\"100%%\" fill=\"white\"/>\n");

    if (exit_cell != NULL) {
        fprintf(out,
                "  <rect x=\"%d\" y=\"%d\" width=\"%d\" height=\"%d\""
                " fill=\"%s\" fill-opacity=\"0.25\"/>\n",
                at(style, exit_cell->x), at(style, exit_cell->y),
                style->cell_size, style->cell_size, style->exit_colour);
    }

    /* The area is enclosed on every side: the exit is a cell, not a gap. */
    line(out, at(style, 0), at(style, 0), at(style, maze_width(maze)),
         at(style, 0), style->wall_colour, style->wall_width);
    line(out, at(style, 0), at(style, maze_height(maze)),
         at(style, maze_width(maze)), at(style, maze_height(maze)),
         style->wall_colour, style->wall_width);
    line(out, at(style, 0), at(style, 0), at(style, 0),
         at(style, maze_height(maze)), style->wall_colour, style->wall_width);
    line(out, at(style, maze_width(maze)), at(style, 0),
         at(style, maze_width(maze)), at(style, maze_height(maze)),
         style->wall_colour, style->wall_width);

    /* One segment wherever two neighbouring cells have no door between them. */
    for (y = 0; y < maze_height(maze); ++y) {
        for (x = 0; x < maze_width(maze); ++x) {
            Cell here;
            Cell east;
            Cell south;
            here.x = x;  here.y = y;
            east.x = x + 1; east.y = y;
            south.x = x; south.y = y + 1;

            if (x + 1 < maze_width(maze) && !maze_has_door(maze, here, east)) {
                line(out, at(style, x + 1), at(style, y), at(style, x + 1),
                     at(style, y + 1), style->wall_colour, style->wall_width);
            }
            if (y + 1 < maze_height(maze) && !maze_has_door(maze, here, south)) {
                line(out, at(style, x), at(style, y + 1), at(style, x + 1),
                     at(style, y + 1), style->wall_colour, style->wall_width);
            }
        }
    }

    for (i = 1; i < route_length; ++i) {
        line(out, centre(style, route[i - 1].x), centre(style, route[i - 1].y),
             centre(style, route[i].x), centre(style, route[i].y),
             style->route_colour, style->route_width);
    }

    fprintf(out, "</svg>\n");
    return fclose(out) == 0;
}
