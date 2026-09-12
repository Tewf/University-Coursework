#ifndef GENERATOR_H
#define GENERATOR_H

#include "maze.h"
#include "region_tree.h"

/* What one generation produced. The two fields are the same maze seen twice:
   the graph a cell-by-cell search walks, and the binary tree that records how
   it was built. Neither is derived from the other -- the generator fills both
   as it goes, at no extra asymptotic cost. */
typedef struct {
    Maze *graph;
    RegionNode *tree;
} Labyrinth;

/* Builds a random maze on width x height cells by recursive division.

   A region thicker than one cell in both directions is cut by a full wall
   across a randomly chosen axis; the wall carries a single door, and the two
   halves are divided the same way. A region one cell thick is a corridor: it
   admits exactly one spanning tree, so it is laid down end to end and the
   recursion stops.

   The graph returned is a spanning tree of the grid. seed makes a run
   reproducible. On failure both fields are NULL. */
Labyrinth labyrinth_generate(int width, int height, unsigned long seed);

void labyrinth_destroy(Labyrinth *labyrinth);

#endif /* GENERATOR_H */
