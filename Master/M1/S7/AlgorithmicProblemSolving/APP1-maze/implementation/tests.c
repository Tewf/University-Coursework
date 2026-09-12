/* What the report claims about the two outputs, checked on real runs.
   Plain assertions and a tally, so the suite needs nothing but a C compiler. */

#include <stdio.h>
#include <stdlib.h>

#include "generator.h"
#include "invariants.h"
#include "solver.h"

static int checks = 0;
static int failures = 0;

static void check(int condition, const char *what) {
    ++checks;
    if (!condition) {
        ++failures;
        printf("  FAIL  %s\n", what);
    }
}

/* Sizes that exercise the corridor base case as well as the ordinary one. */
static const int sizes[][2] = {{1, 1},  {1, 2},   {2, 1},   {1, 40}, {40, 1},
                               {2, 2},  {3, 7},   {8, 5},   {16, 16}, {31, 17}};
static const size_t size_count = sizeof sizes / sizeof *sizes;

static void generation_produces_a_spanning_tree(void) {
    size_t s;
    unsigned long seed;

    for (s = 0; s < size_count; ++s) {
        for (seed = 0; seed < 20; ++seed) {
            Labyrinth l = labyrinth_generate(sizes[s][0], sizes[s][1], seed);
            check(l.graph != NULL, "generation succeeded");
            check(maze_door_count(l.graph) + 1 == maze_cell_count(l.graph),
                  "door count is one fewer than the cell count");
            check(maze_is_spanning_tree(l.graph), "the maze is a spanning tree");
            check(maze_max_doors_per_cell(l.graph) <= 4, "no cell exceeds four doors");
            labyrinth_destroy(&l);
        }
    }
}

static void generation_refuses_empty_dimensions(void) {
    Labyrinth a = labyrinth_generate(0, 5, 1);
    Labyrinth b = labyrinth_generate(5, 0, 1);
    check(a.graph == NULL, "a zero width is refused");
    check(b.graph == NULL, "a zero height is refused");
}

static void a_corridor_is_laid_down_whole(void) {
    Labyrinth l = labyrinth_generate(1, 40, 7);
    check(region_leaf_count(l.tree) == 1, "a 1x40 area is one corridor");
    check(region_is_leaf(l.tree), "its region tree is a single leaf");
    check(maze_door_count(l.graph) == 39, "it holds 39 doors");
    labyrinth_destroy(&l);
}

static void the_same_seed_gives_the_same_maze(void) {
    Labyrinth first = labyrinth_generate(12, 9, 4242);
    Labyrinth second = labyrinth_generate(12, 9, 4242);
    int x;
    int y;
    int identical = 1;

    for (y = 0; y < 9; ++y) {
        for (x = 0; x < 12; ++x) {
            Cell c;
            Cell east;
            c.x = x; c.y = y;
            east.x = x + 1; east.y = y;
            if (maze_has_door(first.graph, c, east) !=
                maze_has_door(second.graph, c, east)) {
                identical = 0;
            }
        }
    }
    check(identical, "two runs of one seed agree");
    labyrinth_destroy(&first);
    labyrinth_destroy(&second);
}

static void the_maze_refuses_doors_that_are_not_doors(void) {
    Maze *maze = maze_create(4, 4);
    Cell a = {0, 0};
    Cell far = {2, 0};
    Cell outside = {4, 0};
    Cell east = {1, 0};

    check(!maze_open_door(maze, a, far), "cells that do not touch are refused");
    check(!maze_open_door(maze, a, outside), "a cell outside is refused");
    check(maze_open_door(maze, a, east), "an adjacent pair is accepted");
    check(!maze_open_door(maze, a, east), "the same door twice is refused");
    check(!maze_open_door(maze, east, a), "and refused from the other end");
    maze_destroy(maze);
}

static void both_outputs_agree_on_the_route(void) {
    size_t s;
    unsigned long seed;

    for (s = 0; s < size_count; ++s) {
        for (seed = 0; seed < 10; ++seed) {
            Labyrinth l = labyrinth_generate(sizes[s][0], sizes[s][1], seed);
            Cell start = {0, 0};
            Cell exit_cell;
            Route graph_route;
            Route tree_route;
            size_t i;
            int same = 1;

            exit_cell.x = sizes[s][0] - 1;
            exit_cell.y = sizes[s][1] - 1;
            graph_route = solve_on_graph(l.graph, start, exit_cell,
                                         HEURISTIC_NONE, GUIDE_TIE_BREAK);
            tree_route = solve_on_tree(l.tree, start, exit_cell, NULL);

            check(graph_route.length > 0, "the graph search found a route");
            check(graph_route.length == tree_route.length,
                  "both outputs return routes of the same length");
            if (graph_route.length == tree_route.length) {
                for (i = 0; i < graph_route.length; ++i) {
                    if (!cell_equal(graph_route.cells[i], tree_route.cells[i])) {
                        same = 0;
                    }
                }
                check(same, "both outputs return the same cells, in order");
            }
            route_destroy(&graph_route);
            route_destroy(&tree_route);
            labyrinth_destroy(&l);
        }
    }
}

static void every_guide_returns_the_same_route(void) {
    static const Heuristic heuristics[] = {HEURISTIC_MANHATTAN, HEURISTIC_EUCLIDEAN};
    static const HeuristicUse uses[] = {GUIDE_TIE_BREAK, GUIDE_PRIORITY};
    Labyrinth l = labyrinth_generate(20, 14, 11);
    Cell start = {0, 0};
    Cell exit_cell = {19, 13};
    Route plain = solve_on_graph(l.graph, start, exit_cell, HEURISTIC_NONE,
                                 GUIDE_TIE_BREAK);
    size_t h;
    size_t u;

    for (h = 0; h < 2; ++h) {
        for (u = 0; u < 2; ++u) {
            Route guided = solve_on_graph(l.graph, start, exit_cell,
                                          heuristics[h], uses[u]);
            check(guided.length == plain.length,
                  "a guided search returns the same route length");
            route_destroy(&guided);
        }
    }
    route_destroy(&plain);
    labyrinth_destroy(&l);
}

static void the_route_is_walkable(void) {
    Labyrinth l = labyrinth_generate(20, 14, 11);
    Cell start = {0, 0};
    Cell exit_cell = {19, 13};
    Route route = solve_on_tree(l.tree, start, exit_cell, NULL);
    size_t i;
    int walkable = 1;

    for (i = 1; i < route.length; ++i) {
        if (!maze_has_door(l.graph, route.cells[i - 1], route.cells[i])) {
            walkable = 0;
        }
    }
    check(route.length > 0, "the tree search found a route");
    check(walkable, "every step of it crosses a door");
    check(cell_equal(route.cells[0], start), "it starts at the start");
    check(cell_equal(route.cells[route.length - 1], exit_cell), "it ends at the exit");
    route_destroy(&route);
    labyrinth_destroy(&l);
}

static void cells_outside_the_grid_are_refused(void) {
    Labyrinth l = labyrinth_generate(5, 5, 1);
    Cell inside = {0, 0};
    Cell outside = {5, 5};
    Route a = solve_on_graph(l.graph, outside, inside, HEURISTIC_NONE, GUIDE_TIE_BREAK);
    Route b = solve_on_tree(l.tree, inside, outside, NULL);

    check(a.length == 0, "the graph search refuses a cell outside");
    check(b.length == 0, "the tree search refuses a cell outside");
    route_destroy(&a);
    route_destroy(&b);
    labyrinth_destroy(&l);
}

int main(void) {
    generation_refuses_empty_dimensions();
    generation_produces_a_spanning_tree();
    a_corridor_is_laid_down_whole();
    the_same_seed_gives_the_same_maze();
    the_maze_refuses_doors_that_are_not_doors();
    both_outputs_agree_on_the_route();
    every_guide_returns_the_same_route();
    the_route_is_walkable();
    cells_outside_the_grid_are_refused();

    printf("%d checks, %d failed\n", checks, failures);
    return failures == 0 ? EXIT_SUCCESS : EXIT_FAILURE;
}
