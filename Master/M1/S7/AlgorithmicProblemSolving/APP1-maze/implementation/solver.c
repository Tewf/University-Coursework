#include "solver.h"

#include <math.h>
#include <stdlib.h>

/* ---------------------------------------------------------------- names --- */

const char *heuristic_name(Heuristic heuristic) {
    switch (heuristic) {
        case HEURISTIC_NONE:      return "none";
        case HEURISTIC_MANHATTAN: return "manhattan";
        case HEURISTIC_EUCLIDEAN: return "euclidean";
    }
    return "unknown";
}

const char *guide_name(HeuristicUse use) {
    switch (use) {
        case GUIDE_TIE_BREAK: return "tie-break";
        case GUIDE_PRIORITY:  return "priority";
    }
    return "unknown";
}

void route_destroy(Route *route) {
    if (route == NULL) {
        return;
    }
    free(route->cells);
    route->cells = NULL;
    route->length = 0;
}

size_t route_steps(const Route *route) {
    return route->length == 0 ? 0 : route->length - 1;
}

/* ------------------------------------------------------- a growable list --- */

typedef struct {
    Cell *cells;
    size_t count;
    size_t capacity;
    int failed;
} CellList;

static void list_push(CellList *list, Cell c) {
    if (list->failed) {
        return;
    }
    if (list->count == list->capacity) {
        size_t wanted = list->capacity == 0 ? 64 : list->capacity * 2;
        Cell *grown = realloc(list->cells, wanted * sizeof *grown);
        if (grown == NULL) {
            list->failed = 1;
            return;
        }
        list->cells = grown;
        list->capacity = wanted;
    }
    list->cells[list->count++] = c;
}

/* ------------------------------------------------- a binary min-heap ------ */

typedef struct {
    double priority;
    double estimate;
    long distance;
    Cell cell;
} HeapItem;

typedef struct {
    HeapItem *items;
    size_t count;
    size_t capacity;
} Heap;

static int item_before(const HeapItem *a, const HeapItem *b) {
    if (a->priority != b->priority) {
        return a->priority < b->priority;
    }
    return a->estimate < b->estimate;
}

static int heap_push(Heap *heap, HeapItem item) {
    size_t i;

    if (heap->count == heap->capacity) {
        size_t wanted = heap->capacity == 0 ? 64 : heap->capacity * 2;
        HeapItem *grown = realloc(heap->items, wanted * sizeof *grown);
        if (grown == NULL) {
            return 0;
        }
        heap->items = grown;
        heap->capacity = wanted;
    }
    i = heap->count++;
    while (i > 0) {
        size_t parent = (i - 1) / 2;
        if (!item_before(&item, &heap->items[parent])) {
            break;
        }
        heap->items[i] = heap->items[parent];
        i = parent;
    }
    heap->items[i] = item;
    return 1;
}

static HeapItem heap_pop(Heap *heap) {
    HeapItem best = heap->items[0];
    HeapItem last = heap->items[--heap->count];
    size_t i = 0;

    while (1) {
        size_t left = 2 * i + 1;
        size_t smallest = i;

        if (left < heap->count && item_before(&heap->items[left], &last)) {
            smallest = left;
        }
        if (left + 1 < heap->count &&
            item_before(&heap->items[left + 1],
                        smallest == i ? &last : &heap->items[left])) {
            smallest = left + 1;
        }
        if (smallest == i) {
            break;
        }
        heap->items[i] = heap->items[smallest];
        i = smallest;
    }
    if (heap->count > 0) {
        heap->items[i] = last;
    }
    return best;
}

/* ------------------------------------------------------- the graph search - */

static double estimate_to(Cell c, Cell exit, Heuristic heuristic) {
    double dx = (double)(c.x - exit.x);
    double dy = (double)(c.y - exit.y);

    switch (heuristic) {
        case HEURISTIC_MANHATTAN: return fabs(dx) + fabs(dy);
        case HEURISTIC_EUCLIDEAN: return sqrt(dx * dx + dy * dy);
        case HEURISTIC_NONE:      break;
    }
    return 0.0;
}

Route solve_on_graph(const Maze *maze, Cell start, Cell exit,
                     Heuristic heuristic, HeuristicUse use) {
    Route route = {NULL, 0, 0};
    size_t cells;
    long *distance = NULL;
    Cell *parent = NULL;
    char *settled = NULL;
    Heap heap = {NULL, 0, 0};
    CellList reversed = {NULL, 0, 0, 0};
    Cell walk;
    size_t i;

    if (!maze_contains(maze, start) || !maze_contains(maze, exit)) {
        return route;
    }
    cells = maze_cell_count(maze);
    distance = malloc(cells * sizeof *distance);
    parent = malloc(cells * sizeof *parent);
    settled = calloc(cells, 1);
    if (distance == NULL || parent == NULL || settled == NULL) {
        goto done;
    }
    for (i = 0; i < cells; ++i) {
        distance[i] = -1; /* -1 stands for "not reached" */
    }

    {
        HeapItem first;
        double h = estimate_to(start, exit, heuristic);
        first.distance = 0;
        first.estimate = h;
        first.priority = use == GUIDE_PRIORITY ? h : 0.0;
        first.cell = start;
        distance[maze_index(maze, start)] = 0;
        parent[maze_index(maze, start)] = start;
        if (!heap_push(&heap, first)) {
            goto done;
        }
    }

    while (heap.count > 0) {
        HeapItem item = heap_pop(&heap);
        size_t here = maze_index(maze, item.cell);
        size_t count;
        const Cell *neighbours;

        if (settled[here]) {
            continue; /* a stale copy left by an earlier relaxation */
        }
        settled[here] = 1;
        ++route.examined;
        if (cell_equal(item.cell, exit)) {
            break;
        }

        neighbours = maze_neighbours(maze, item.cell, &count);
        for (i = 0; i < count; ++i) {
            Cell next = neighbours[i];
            size_t there = maze_index(maze, next);
            long through = item.distance + 1; /* one door, one step */

            if (distance[there] >= 0 && distance[there] <= through) {
                continue;
            }
            distance[there] = through;
            parent[there] = item.cell;
            {
                HeapItem pushed;
                double h = estimate_to(next, exit, heuristic);
                pushed.distance = through;
                pushed.estimate = h;
                pushed.priority = use == GUIDE_PRIORITY
                                      ? (double)through + h
                                      : (double)through;
                pushed.cell = next;
                if (!heap_push(&heap, pushed)) {
                    goto done;
                }
            }
        }
    }

    if (distance[maze_index(maze, exit)] < 0) {
        goto done;
    }
    walk = exit;
    while (1) {
        list_push(&reversed, walk);
        if (cell_equal(walk, start)) {
            break;
        }
        walk = parent[maze_index(maze, walk)];
    }
    if (reversed.failed) {
        free(reversed.cells);
        goto done;
    }
    route.cells = malloc(reversed.count * sizeof *route.cells);
    if (route.cells == NULL) {
        free(reversed.cells);
        goto done;
    }
    for (i = 0; i < reversed.count; ++i) {
        route.cells[i] = reversed.cells[reversed.count - 1 - i];
    }
    route.length = reversed.count;
    free(reversed.cells);

done:
    free(distance);
    free(parent);
    free(settled);
    free(heap.items);
    return route;
}

/* -------------------------------------------------------- the tree search - */

/* Appends the cells from a to b, excluding a, along a corridor: the region is
   one cell thick, so they differ on at most one axis. */
static void append_corridor(CellList *out, Cell a, Cell b) {
    while (!cell_equal(a, b)) {
        if (a.x != b.x) {
            a.x += a.x < b.x ? 1 : -1;
        } else {
            a.y += a.y < b.y ? 1 : -1;
        }
        list_push(out, a);
    }
}

static void route_in_region(const RegionNode *node, Cell a, Cell b,
                            CellList *out, size_t *examined,
                            TreeBranching *branching) {
    Cell near_side;
    Cell far_side;

    ++*examined;
    if (region_is_leaf(node)) {
        append_corridor(out, a, b);
        return;
    }
    region_door_cells(node, &near_side, &far_side);

    if (region_holds(node->left, a) && region_holds(node->left, b)) {
        if (branching != NULL) { ++branching->one_way; }
        route_in_region(node->left, a, b, out, examined, branching);
        return;
    }
    if (region_holds(node->right, a) && region_holds(node->right, b)) {
        if (branching != NULL) { ++branching->one_way; }
        route_in_region(node->right, a, b, out, examined, branching);
        return;
    }
    /* Separated, so the door is on the route. */
    if (branching != NULL) { ++branching->two_way; }
    if (region_holds(node->left, a)) {
        route_in_region(node->left, a, near_side, out, examined, branching);
        list_push(out, far_side);
        route_in_region(node->right, far_side, b, out, examined, branching);
    } else {
        route_in_region(node->right, a, far_side, out, examined, branching);
        list_push(out, near_side);
        route_in_region(node->left, near_side, b, out, examined, branching);
    }
}

Route solve_on_tree(const RegionNode *root, Cell start, Cell exit,
                    TreeBranching *branching) {
    Route route = {NULL, 0, 0};
    CellList out = {NULL, 0, 0, 0};

    if (!region_holds(root, start) || !region_holds(root, exit)) {
        return route;
    }
    list_push(&out, start);
    route_in_region(root, start, exit, &out, &route.examined, branching);
    if (out.failed) {
        free(out.cells);
        route.examined = 0;
        return route;
    }
    route.cells = out.cells;
    route.length = out.count;
    return route;
}
