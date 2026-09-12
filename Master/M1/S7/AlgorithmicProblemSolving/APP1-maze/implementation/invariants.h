#ifndef INVARIANTS_H
#define INVARIANTS_H

#include <stddef.h>

#include "maze.h"

/* Checks of the properties a finished maze is required to have. They are kept
   apart from the generator on purpose: a generator that checked its own work
   would only ever confirm its own assumptions. */

/* Non-zero when every cell is reachable from every other. */
int maze_is_connected(const Maze *maze);

/* Non-zero when the maze is a spanning tree of the grid: connected, and
   carrying exactly one door fewer than it has cells. Those two together imply
   acyclic, so a separate cycle hunt would be redundant. */
int maze_is_spanning_tree(const Maze *maze);

/* Largest number of doors on any one cell. Can never exceed 4. */
size_t maze_max_doors_per_cell(const Maze *maze);

#endif /* INVARIANTS_H */
