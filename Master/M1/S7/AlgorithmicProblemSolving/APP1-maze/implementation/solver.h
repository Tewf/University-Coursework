#ifndef SOLVER_H
#define SOLVER_H

#include <stddef.h>

#include "cell.h"
#include "maze.h"
#include "region_tree.h"

/* Which distance to the exit the graph search consults. */
typedef enum {
    HEURISTIC_NONE,      /* no estimate: cost so far is the only guide */
    HEURISTIC_MANHATTAN, /* |dx| + |dy|, the steps needed on an empty grid */
    HEURISTIC_EUCLIDEAN  /* straight-line distance */
} Heuristic;

/* How much weight that estimate is given. TIE_BREAK orders cells reached at
   equal cost and changes no computed distance; PRIORITY adds it to the cost,
   which is A*. */
typedef enum {
    GUIDE_TIE_BREAK,
    GUIDE_PRIORITY
} HeuristicUse;

const char *heuristic_name(Heuristic heuristic);
const char *guide_name(HeuristicUse use);

/* A route, and what it cost to find.

   Every solver here returns the same cells -- the maze is a spanning tree, so
   there is only one route -- so `examined` is what separates them: cells
   settled by the graph search, or tree nodes visited by the tree search. */
typedef struct {
    Cell *cells;     /* cells[0] is the start, cells[length-1] the exit */
    size_t length;   /* 0 when the exit was not reached */
    size_t examined;
} Route;

void route_destroy(Route *route);

/* Doors crossed, one fewer than the cells on the route. */
size_t route_steps(const Route *route);

/* Dijkstra's algorithm over the maze graph, every door counting as one step.

   With HEURISTIC_NONE this is Dijkstra unadorned. Both estimates are
   admissible on this graph, so the route returned is a shortest one under
   every setting. Returns an empty route if either cell is outside the grid or
   memory runs out. */
Route solve_on_graph(const Maze *maze, Cell start, Cell exit,
                     Heuristic heuristic, HeuristicUse use);

/* How a run of the tree search branched. At each division either both
   endpoints fell on one side, and half the region was discarded in one step,
   or they were separated and both halves had to be entered. The ratio decides
   the cost: the recurrence is T(m) = (1 + two_way/(one_way+two_way)) T(m/2). */
typedef struct {
    size_t one_way;
    size_t two_way;
} TreeBranching;

/* The same route, read off the binary tree instead.

   A division's door lies on the route exactly when that division separates the
   two endpoints, and that is decided by comparing coordinates against a
   rectangle -- so the maze graph is never consulted. branching may be NULL.
   Returns an empty route if either cell lies outside the tree's region or
   memory runs out. */
Route solve_on_tree(const RegionNode *root, Cell start, Cell exit,
                    TreeBranching *branching);

#endif /* SOLVER_H */
