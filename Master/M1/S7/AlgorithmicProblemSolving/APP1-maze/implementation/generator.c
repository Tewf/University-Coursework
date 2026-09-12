#include "generator.h"

#include <stdlib.h>

/* xorshift64*, so that a run depends on its seed and on nothing else: rand()
   would tie the measurements to whichever C library happened to build them. */
typedef struct {
    unsigned long long state;
} Random;

static unsigned long long random_next(Random *rng) {
    unsigned long long x = rng->state;
    x ^= x >> 12;
    x ^= x << 25;
    x ^= x >> 27;
    rng->state = x;
    return x * 2685821657736338717ULL;
}

/* Uniform in the inclusive range [low, high]. Requires low <= high, which the
   caller guarantees by never cutting an axis of extent 0. */
static int random_in(Random *rng, int low, int high) {
    unsigned long long span = (unsigned long long)(high - low) + 1ULL;
    return low + (int)(random_next(rng) % span);
}

/* Opens the doors of a region one cell thick, joining its cells end to end.
   One of the two loops is empty by construction, and on a single cell both
   are, so the same code covers a row, a column and one cell. */
static void span_corridor(Maze *maze, Cell p, Cell q) {
    int x;
    int y;

    for (x = p.x; x < q.x; ++x) {
        Cell a = {0, 0};
        Cell b = {0, 0};
        a.x = x;     a.y = p.y;
        b.x = x + 1; b.y = p.y;
        maze_open_door(maze, a, b);
    }
    for (y = p.y; y < q.y; ++y) {
        Cell a = {0, 0};
        Cell b = {0, 0};
        a.x = p.x; a.y = y;
        b.x = p.x; b.y = y + 1;
        maze_open_door(maze, a, b);
    }
}

static RegionNode *divide(Maze *maze, Random *rng, Cell p, Cell q,
                          RegionNode *parent) {
    RegionNode *node = region_create(p, q);
    int axis;
    int other;
    int wall;
    int door;
    Cell left_side;
    Cell right_side;

    if (node == NULL) {
        return NULL;
    }
    node->parent = parent;

    if (p.x == q.x || p.y == q.y) { /* a corridor: nothing left to decide */
        span_corridor(maze, p, q);
        return node;
    }

    /* Both sides are at least two cells, so both axes admit a wall and the
       coin needs no feasibility test in front of it. */
    axis = random_in(rng, 0, 1);
    other = 1 - axis;
    wall = random_in(rng, cell_on(p, axis), cell_on(q, axis) - 1);
    door = random_in(rng, cell_on(p, other), cell_on(q, other));

    node->axis = axis;
    node->wall = wall;
    node->door = door;
    region_door_cells(node, &left_side, &right_side);
    maze_open_door(maze, left_side, right_side);

    node->left = divide(maze, rng, p, cell_with(q, axis, wall), node);
    node->right = divide(maze, rng, cell_with(p, axis, wall + 1), q, node);
    return node;
}

Labyrinth labyrinth_generate(int width, int height, unsigned long seed) {
    Labyrinth labyrinth;
    Random rng;
    Cell origin = {0, 0};
    Cell far;

    labyrinth.graph = NULL;
    labyrinth.tree = NULL;

    labyrinth.graph = maze_create(width, height);
    if (labyrinth.graph == NULL) {
        return labyrinth;
    }
    /* A zero seed would leave xorshift stuck at zero for ever. */
    rng.state = (unsigned long long)seed * 6364136223846793005ULL + 1442695040888963407ULL;

    far.x = width - 1;
    far.y = height - 1;
    labyrinth.tree = divide(labyrinth.graph, &rng, origin, far, NULL);
    if (labyrinth.tree == NULL) {
        maze_destroy(labyrinth.graph);
        labyrinth.graph = NULL;
    }
    return labyrinth;
}

void labyrinth_destroy(Labyrinth *labyrinth) {
    if (labyrinth == NULL) {
        return;
    }
    maze_destroy(labyrinth->graph);
    region_destroy(labyrinth->tree);
    labyrinth->graph = NULL;
    labyrinth->tree = NULL;
}
