#include "invariants.h"

#include <stdlib.h>

int maze_is_connected(const Maze *maze) {
    size_t cells = maze_cell_count(maze);
    char *seen = calloc(cells, 1);
    Cell *stack = malloc(cells * sizeof *stack);
    size_t top = 0;
    size_t reached = 1;
    Cell origin = {0, 0};
    int connected;

    if (seen == NULL || stack == NULL) {
        free(seen);
        free(stack);
        return 0;
    }
    seen[maze_index(maze, origin)] = 1;
    stack[top++] = origin;

    while (top > 0) {
        Cell here = stack[--top];
        size_t count;
        const Cell *neighbours = maze_neighbours(maze, here, &count);
        size_t i;

        for (i = 0; i < count; ++i) {
            size_t index = maze_index(maze, neighbours[i]);
            if (seen[index]) {
                continue;
            }
            seen[index] = 1;
            ++reached;
            stack[top++] = neighbours[i];
        }
    }
    connected = reached == cells;
    free(seen);
    free(stack);
    return connected;
}

int maze_is_spanning_tree(const Maze *maze) {
    return maze_door_count(maze) + 1 == maze_cell_count(maze) &&
           maze_is_connected(maze);
}

size_t maze_max_doors_per_cell(const Maze *maze) {
    size_t most = 0;
    int x;
    int y;

    for (y = 0; y < maze_height(maze); ++y) {
        for (x = 0; x < maze_width(maze); ++x) {
            Cell c;
            size_t count;
            c.x = x;
            c.y = y;
            maze_neighbours(maze, c, &count);
            if (count > most) {
                most = count;
            }
        }
    }
    return most;
}
