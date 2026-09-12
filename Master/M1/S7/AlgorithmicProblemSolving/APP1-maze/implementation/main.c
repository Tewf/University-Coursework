/* Generates one maze, solves it on each of its two outputs, and reports what
   each cost. Every solver returns the same route -- the maze is a spanning
   tree, so there is only one -- so the figure that differs is how much of the
   maze each had to examine. */

#include <stdio.h>
#include <stdlib.h>

#include "generator.h"
#include "invariants.h"
#include "solver.h"
#include "svg.h"

static void usage(const char *program) {
    fprintf(stderr, "usage: %s [width] [height] [seed] [output.svg]\n", program);
    fprintf(stderr, "  defaults: 24 16 1 maze.svg\n");
}

int main(int argc, char **argv) {
    int width = 24;
    int height = 16;
    unsigned long seed = 1;
    const char *svg_path = "maze.svg";
    Labyrinth labyrinth;
    Cell start = {0, 0};
    Cell exit_cell;
    Route route = {NULL, 0, 0};
    size_t i;

    static const Heuristic heuristics[] = {HEURISTIC_NONE, HEURISTIC_MANHATTAN,
                                           HEURISTIC_EUCLIDEAN,
                                           HEURISTIC_MANHATTAN,
                                           HEURISTIC_EUCLIDEAN};
    static const HeuristicUse uses[] = {GUIDE_TIE_BREAK, GUIDE_TIE_BREAK,
                                        GUIDE_TIE_BREAK, GUIDE_PRIORITY,
                                        GUIDE_PRIORITY};

    if (argc > 1) { width = atoi(argv[1]); }
    if (argc > 2) { height = atoi(argv[2]); }
    if (argc > 3) { seed = strtoul(argv[3], NULL, 10); }
    if (argc > 4) { svg_path = argv[4]; }
    if (width < 1 || height < 1) {
        usage(argv[0]);
        return EXIT_FAILURE;
    }

    labyrinth = labyrinth_generate(width, height, seed);
    if (labyrinth.graph == NULL) {
        fprintf(stderr, "error: could not generate a %dx%d maze\n", width, height);
        return EXIT_FAILURE;
    }
    exit_cell.x = width - 1;
    exit_cell.y = height - 1;

    printf("%dx%d, seed %lu: %zu cells, %zu doors, %zu corridors, tree depth %zu\n",
           width, height, seed, maze_cell_count(labyrinth.graph),
           maze_door_count(labyrinth.graph),
           region_leaf_count(labyrinth.tree), region_depth(labyrinth.tree));
    printf("  spanning tree: %s\n",
           maze_is_spanning_tree(labyrinth.graph) ? "yes" : "NO");

    printf("  graph output, Dijkstra:\n");
    for (i = 0; i < sizeof heuristics / sizeof *heuristics; ++i) {
        Route attempt = solve_on_graph(labyrinth.graph, start, exit_cell,
                                       heuristics[i], uses[i]);
        printf("    %-10s as %-10s %5zu steps, %6zu cells examined\n",
               heuristic_name(heuristics[i]), guide_name(uses[i]),
               route_steps(&attempt), attempt.examined);
        route_destroy(&route);
        route = attempt;
    }

    {
        Route on_tree = solve_on_tree(labyrinth.tree, start, exit_cell, NULL);
        printf("  tree output, common ancestor:\n");
        printf("    %-24s %5zu steps, %6zu nodes examined\n", "",
               route_steps(&on_tree), on_tree.examined);
        route_destroy(&on_tree);
    }

    if (!svg_write_maze(labyrinth.graph, svg_path, route.cells, route.length,
                        &exit_cell, NULL)) {
        fprintf(stderr, "error: could not write %s\n", svg_path);
        route_destroy(&route);
        labyrinth_destroy(&labyrinth);
        return EXIT_FAILURE;
    }
    printf("wrote %s\n", svg_path);

    route_destroy(&route);
    labyrinth_destroy(&labyrinth);
    return EXIT_SUCCESS;
}
