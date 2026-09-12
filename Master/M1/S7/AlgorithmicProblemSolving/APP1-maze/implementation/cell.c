#include "cell.h"

int cell_on(Cell c, int axis) {
    return axis == 0 ? c.x : c.y;
}

Cell cell_with(Cell c, int axis, int value) {
    if (axis == 0) {
        c.x = value;
    } else {
        c.y = value;
    }
    return c;
}

Cell cell_at(int axis, int along, int across) {
    Cell c;
    c.x = axis == 0 ? along : across;
    c.y = axis == 0 ? across : along;
    return c;
}

int cell_adjacent(Cell a, Cell b) {
    int dx = a.x > b.x ? a.x - b.x : b.x - a.x;
    int dy = a.y > b.y ? a.y - b.y : b.y - a.y;
    return dx + dy == 1;
}

int cell_equal(Cell a, Cell b) {
    return a.x == b.x && a.y == b.y;
}
