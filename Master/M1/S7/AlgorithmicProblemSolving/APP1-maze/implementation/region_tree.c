#include "region_tree.h"

#include <stdlib.h>

RegionNode *region_create(Cell upper_left, Cell lower_right) {
    RegionNode *node = malloc(sizeof *node);

    if (node == NULL) {
        return NULL;
    }
    node->upper_left = upper_left;
    node->lower_right = lower_right;
    node->axis = -1;
    node->wall = 0;
    node->door = 0;
    node->left = NULL;
    node->right = NULL;
    node->parent = NULL;
    return node;
}

void region_destroy(RegionNode *node) {
    if (node == NULL) {
        return;
    }
    region_destroy(node->left);
    region_destroy(node->right);
    free(node);
}

int region_is_leaf(const RegionNode *node) {
    return node->left == NULL;
}

int region_holds(const RegionNode *node, Cell c) {
    return c.x >= node->upper_left.x && c.x <= node->lower_right.x &&
           c.y >= node->upper_left.y && c.y <= node->lower_right.y;
}

void region_door_cells(const RegionNode *node, Cell *left_side,
                       Cell *right_side) {
    *left_side = cell_at(node->axis, node->wall, node->door);
    *right_side = cell_at(node->axis, node->wall + 1, node->door);
}

size_t region_leaf_count(const RegionNode *node) {
    if (region_is_leaf(node)) {
        return 1;
    }
    return region_leaf_count(node->left) + region_leaf_count(node->right);
}

size_t region_depth(const RegionNode *node) {
    size_t left;
    size_t right;

    if (region_is_leaf(node)) {
        return 0;
    }
    left = region_depth(node->left);
    right = region_depth(node->right);
    return 1 + (left > right ? left : right);
}

const RegionNode *region_leaf_holding(const RegionNode *node, Cell c) {
    if (!region_holds(node, c)) {
        return NULL;
    }
    while (!region_is_leaf(node)) {
        node = region_holds(node->left, c) ? node->left : node->right;
    }
    return node;
}
