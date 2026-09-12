#ifndef MAZE_H
#define MAZE_H

#include <stddef.h>

#include "cell.h"

/* The first of the two structures generation returns: the maze as a graph.

   Every cell is a node holding the neighbours it has a door to. A door is
   recorded at both of its ends, and a wall is recorded nowhere -- it is simply
   a door that was never opened. A cell has four sides, so a node never holds
   more than four neighbours.

   Once a generator has finished the graph is a spanning tree of the grid:
   width * height - 1 doors, and exactly one simple path between any two
   cells. */
typedef struct Maze Maze;

/* A maze of width x height cells with no doors. Returns NULL if either
   dimension is below 1 or if memory runs out. */
Maze *maze_create(int width, int height);
void maze_destroy(Maze *maze);

int maze_width(const Maze *maze);
int maze_height(const Maze *maze);
size_t maze_cell_count(const Maze *maze);

/* Number of doors, each counted once. */
size_t maze_door_count(const Maze *maze);

/* Opens a door between two adjacent cells of the maze. Returns 0 and changes
   nothing if either cell is outside, if they do not share a side, or if the
   door is already open: a generator that opens one twice has a bug, and
   silence would hide it. */
int maze_open_door(Maze *maze, Cell a, Cell b);

/* Non-zero when a door joins a and b. Safe to ask about any pair. */
int maze_has_door(const Maze *maze, Cell a, Cell b);

/* The cells c has a door to. Writes how many into *count. The array belongs to
   the maze and stays valid until the next door is opened. */
const Cell *maze_neighbours(const Maze *maze, Cell c, size_t *count);

/* A dense index in [0, maze_cell_count) for c, so that an algorithm can hold
   one entry per cell in a flat array. Requires maze_contains(maze, c). */
size_t maze_index(const Maze *maze, Cell c);

int maze_contains(const Maze *maze, Cell c);

#endif /* MAZE_H */
