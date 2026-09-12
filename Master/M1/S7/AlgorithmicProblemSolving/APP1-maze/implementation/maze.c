#include "maze.h"

#include <stdlib.h>

/* A cell has four sides, so its neighbours fit in a fixed array and the maze
   needs no dynamic growth anywhere. */
typedef struct {
    Cell neighbour[4];
    size_t count;
} MazeNode;

struct Maze {
    int width;
    int height;
    MazeNode *nodes;
};

Maze *maze_create(int width, int height) {
    Maze *maze;
    size_t cells;

    if (width < 1 || height < 1) {
        return NULL;
    }
    maze = malloc(sizeof *maze);
    if (maze == NULL) {
        return NULL;
    }
    cells = (size_t)width * (size_t)height;
    maze->nodes = calloc(cells, sizeof *maze->nodes);
    if (maze->nodes == NULL) {
        free(maze);
        return NULL;
    }
    maze->width = width;
    maze->height = height;
    return maze;
}

void maze_destroy(Maze *maze) {
    if (maze == NULL) {
        return;
    }
    free(maze->nodes);
    free(maze);
}

int maze_width(const Maze *maze) { return maze->width; }
int maze_height(const Maze *maze) { return maze->height; }

size_t maze_cell_count(const Maze *maze) {
    return (size_t)maze->width * (size_t)maze->height;
}

size_t maze_index(const Maze *maze, Cell c) {
    return (size_t)c.y * (size_t)maze->width + (size_t)c.x;
}

int maze_contains(const Maze *maze, Cell c) {
    return c.x >= 0 && c.x < maze->width && c.y >= 0 && c.y < maze->height;
}

size_t maze_door_count(const Maze *maze) {
    size_t ends = 0;
    size_t i;
    size_t cells = maze_cell_count(maze);

    for (i = 0; i < cells; ++i) {
        ends += maze->nodes[i].count;
    }
    return ends / 2; /* every door is recorded at both of its ends */
}

int maze_has_door(const Maze *maze, Cell a, Cell b) {
    const MazeNode *node;
    size_t i;

    if (!maze_contains(maze, a) || !maze_contains(maze, b)) {
        return 0;
    }
    node = &maze->nodes[maze_index(maze, a)];
    for (i = 0; i < node->count; ++i) {
        if (cell_equal(node->neighbour[i], b)) {
            return 1;
        }
    }
    return 0;
}

int maze_open_door(Maze *maze, Cell a, Cell b) {
    MazeNode *from;
    MazeNode *to;

    if (!maze_contains(maze, a) || !maze_contains(maze, b)) {
        return 0;
    }
    if (!cell_adjacent(a, b) || maze_has_door(maze, a, b)) {
        return 0;
    }
    from = &maze->nodes[maze_index(maze, a)];
    to = &maze->nodes[maze_index(maze, b)];
    if (from->count >= 4 || to->count >= 4) {
        return 0; /* unreachable on a grid, but the array must not overrun */
    }
    from->neighbour[from->count++] = b;
    to->neighbour[to->count++] = a;
    return 1;
}

const Cell *maze_neighbours(const Maze *maze, Cell c, size_t *count) {
    const MazeNode *node = &maze->nodes[maze_index(maze, c)];
    *count = node->count;
    return node->neighbour;
}
