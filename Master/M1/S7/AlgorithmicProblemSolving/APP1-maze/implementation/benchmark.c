/* Measures what each way of solving the maze costs, over many mazes and seeds.
   The report's tables come from this program; run it with no arguments to
   reproduce, or pass a seed count to change the sample. */

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#include "generator.h"
#include "invariants.h"
#include "solver.h"

typedef struct {
    double steps;
    double dijkstra;
    double tie_manhattan;
    double tie_euclidean;
    double star_manhattan;
    double star_euclidean;
    double tree_nodes;
    double leaves;
    double depth;
    double one_way;
    double two_way;
} Totals;

static double examined(const Maze *maze, Cell start, Cell exit_cell,
                       Heuristic heuristic, HeuristicUse use, double *steps) {
    Route route = solve_on_graph(maze, start, exit_cell, heuristic, use);
    double count = (double)route.examined;
    if (steps != NULL) {
        *steps = (double)route_steps(&route);
    }
    route_destroy(&route);
    return count;
}

int main(int argc, char **argv) {
    static const int sizes[][2] = {{16, 16}, {32, 32}, {64, 64},
                                   {128, 128}, {256, 256}};
    const size_t size_count = sizeof sizes / sizeof *sizes;
    unsigned long seeds = 200;
    size_t s;
    size_t checked = 0;

    if (argc > 1) {
        seeds = strtoul(argv[1], NULL, 10);
        if (seeds == 0) {
            fprintf(stderr, "usage: %s [seeds per size]\n", argv[0]);
            return EXIT_FAILURE;
        }
    }

    printf("%lu mazes per size, start (0,0), exit at the far corner\n\n", seeds);
    printf("%-10s%8s%8s   %-28s   %-18s%10s\n", "", "", "",
           "graph output: cells examined", "", "tree output");
    printf("%-10s%8s%8s%9s%9s%9s%9s%9s%11s\n", "size", "cells", "steps",
           "dijkstra", "tie:man", "tie:euc", "A*:man", "A*:euc", "nodes");

    for (s = 0; s < size_count; ++s) {
        int width = sizes[s][0];
        int height = sizes[s][1];
        Totals total = {0};
        unsigned long seed;

        for (seed = 0; seed < seeds; ++seed) {
            Labyrinth l = labyrinth_generate(width, height, seed);
            Cell start = {0, 0};
            Cell exit_cell;
            TreeBranching branching = {0, 0};
            Route on_tree;
            double steps = 0.0;

            exit_cell.x = width - 1;
            exit_cell.y = height - 1;

            total.dijkstra += examined(l.graph, start, exit_cell,
                                       HEURISTIC_NONE, GUIDE_TIE_BREAK, &steps);
            total.steps += steps;
            total.tie_manhattan += examined(l.graph, start, exit_cell,
                                            HEURISTIC_MANHATTAN, GUIDE_TIE_BREAK, NULL);
            total.tie_euclidean += examined(l.graph, start, exit_cell,
                                            HEURISTIC_EUCLIDEAN, GUIDE_TIE_BREAK, NULL);
            total.star_manhattan += examined(l.graph, start, exit_cell,
                                             HEURISTIC_MANHATTAN, GUIDE_PRIORITY, NULL);
            total.star_euclidean += examined(l.graph, start, exit_cell,
                                             HEURISTIC_EUCLIDEAN, GUIDE_PRIORITY, NULL);

            on_tree = solve_on_tree(l.tree, start, exit_cell, &branching);
            total.tree_nodes += (double)on_tree.examined;
            total.one_way += (double)branching.one_way;
            total.two_way += (double)branching.two_way;
            route_destroy(&on_tree);

            total.leaves += (double)region_leaf_count(l.tree);
            total.depth += (double)region_depth(l.tree);

            /* A generator that checked its own work would only confirm its own
               assumptions, so the invariant is verified out here. */
            if (!maze_is_spanning_tree(l.graph)) {
                fprintf(stderr, "not a spanning tree: %dx%d seed %lu\n",
                        width, height, seed);
                labyrinth_destroy(&l);
                return EXIT_FAILURE;
            }
            ++checked;
            labyrinth_destroy(&l);
        }

        printf("%-10s%8d%8.0f%9.0f%9.0f%9.0f%9.0f%9.0f%11.0f\n",
               (width == 16 ? "16x16" : width == 32 ? "32x32" :
                width == 64 ? "64x64" : width == 128 ? "128x128" : "256x256"),
               width * height, total.steps / (double)seeds,
               total.dijkstra / (double)seeds, total.tie_manhattan / (double)seeds,
               total.tie_euclidean / (double)seeds,
               total.star_manhattan / (double)seeds,
               total.star_euclidean / (double)seeds,
               total.tree_nodes / (double)seeds);

        {
            double one = total.one_way / (double)seeds;
            double two = total.two_way / (double)seeds;
            double p = one + two > 0.0 ? two / (one + two) : 0.0;
            double nodes = total.tree_nodes / (double)seeds;
            double n = (double)(width * height);
            fprintf(stderr,
                    "  %dx%d  leaves %.0f  depth %.1f  one-way %.0f  two-way %.0f"
                    "  p %.2f  log2(1+p) %.2f  fitted %.2f\n",
                    width, height, total.leaves / (double)seeds,
                    total.depth / (double)seeds, one, two, p, log2(1.0 + p),
                    log(nodes) / log(n));
        }
    }

    printf("\n%zu mazes checked: every one a spanning tree\n", checked);
    return EXIT_SUCCESS;
}
