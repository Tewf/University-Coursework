#ifndef REGION_TREE_H
#define REGION_TREE_H

#include <stddef.h>

#include "cell.h"

/* The second of the two structures generation returns: the maze as a binary
   tree.

   Each division of a region creates one node, which records where its wall
   went and where its single door was left, and whose two children are the two
   sub-mazes the division created. A leaf is a corridor -- a region one cell
   thick -- which admits exactly one spanning tree and so was laid down whole.

   Every cell therefore has an address: the sequence of turns from the root to
   the leaf whose region contains it. */
typedef struct RegionNode RegionNode;

struct RegionNode {
    Cell upper_left;
    Cell lower_right;

    /* Internal nodes only. axis is the axis the wall cut (0 for x, 1 for y),
       wall the boundary it sat on, door the place on the other axis where its
       single door was left. axis is -1 on a leaf. */
    int axis;
    int wall;
    int door;

    RegionNode *left;
    RegionNode *right;
    RegionNode *parent;
};

RegionNode *region_create(Cell upper_left, Cell lower_right);
void region_destroy(RegionNode *node);

int region_is_leaf(const RegionNode *node);

/* Non-zero when c lies inside the node's rectangle. This is the whole of the
   address test: it reads no cell of the maze. */
int region_holds(const RegionNode *node, Cell c);

/* The two cells the node's door joins, the first in its left child. Requires
   an internal node. */
void region_door_cells(const RegionNode *node, Cell *left_side,
                       Cell *right_side);

/* Number of leaves, which is the number of corridors the generator stopped at.
   A tree with L leaves has L-1 internal nodes, one per division. */
size_t region_leaf_count(const RegionNode *node);

/* Longest root-to-leaf path, counting edges: the depth of the recursion that
   built the maze, and so the stack it needed. */
size_t region_depth(const RegionNode *node);

/* The leaf whose region contains c, found by descending from node. Returns
   NULL if the node does not contain c at all. */
const RegionNode *region_leaf_holding(const RegionNode *node, Cell c);

#endif /* REGION_TREE_H */
