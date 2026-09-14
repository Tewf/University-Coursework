#pragma once

#include "maze.hpp"

#include <cstddef>

/// Checks of the properties a finished maze is required to have. They are
/// separate from the generator on purpose: a generator that checked its own
/// work would only ever confirm its own assumptions.

/// True when every cell is reachable from every other.
bool isConnected(const Maze& maze);

/// True when the maze is a spanning tree of the grid: connected, and carrying
/// exactly one door fewer than it has cells. Those two together imply acyclic,
/// so a separate cycle hunt would be redundant.
bool isSpanningTree(const Maze& maze);

/// Largest number of doors on any one cell. Can never exceed 4, since a cell
/// has four sides.
std::size_t maxDoorsPerCell(const Maze& maze);
