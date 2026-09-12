#ifndef CELL_H
#define CELL_H

/* A cell of the grid, addressed by column x and row y, both counted from 0 at
   the upper-left corner.

   Coordinates are reachable by index as well as by name, so that code working
   on "the axis being cut" needs no separate case per axis: axis 0 is x, axis 1
   is y, and 1 - axis is the other one. */
typedef struct {
    int x;
    int y;
} Cell;

/* Coordinate of c on the given axis. Requires axis to be 0 or 1. */
int cell_on(Cell c, int axis);

/* A copy of c with its axis coordinate replaced. Requires axis to be 0 or 1. */
Cell cell_with(Cell c, int axis, int value);

/* The cell whose axis coordinate is along and whose other one is across.
   Requires axis to be 0 or 1. */
Cell cell_at(int axis, int along, int across);

/* Non-zero when the two cells share a side, which is the only way a door can
   join them. */
int cell_adjacent(Cell a, Cell b);

/* Non-zero when the two cells are the same. */
int cell_equal(Cell a, Cell b);

#endif /* CELL_H */
