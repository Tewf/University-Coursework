#pragma once

#include "cell.hpp"
#include "maze.hpp"

#include <cstddef>
#include <cstdint>
#include <memory>

/// One node of the region decomposition the generator builds.
///
/// An internal node records the division it made and has the two regions that
/// division created as children. A leaf is a corridor -- a region one cell
/// thick -- which the generator laid down whole rather than dividing further.
struct RegionNode {
  Cell upperLeft;
  Cell lowerRight;

  /// Set on internal nodes only. `axis` is the axis the wall cut (0 for x, 1
  /// for y), `wallPosition` the boundary it sat on, `doorPosition` the place on
  /// the other axis where its single door was left.
  int axis = -1;
  int wallPosition = 0;
  int doorPosition = 0;

  std::unique_ptr<RegionNode> left;
  std::unique_ptr<RegionNode> right;

  bool isLeaf() const { return left == nullptr; }
};

/// What one generation produced: the maze itself, and the tree that built it.
struct GeneratedMaze {
  Maze maze;
  std::unique_ptr<RegionNode> regionTree;
};

/// Builds a random maze on `width` x `height` cells by recursive division.
///
/// A region thicker than one cell in both directions is cut by a full wall
/// across a randomly chosen axis; the wall carries a single door, and the two
/// halves are divided the same way. A region one cell thick is a corridor: it
/// admits exactly one spanning tree, so it is laid down end to end and the
/// recursion stops.
///
/// Returns a spanning tree of the grid graph: `width * height - 1` doors, every
/// cell reachable from every other by exactly one simple path. `seed` makes a
/// run reproducible; two different seeds need not agree.
///
/// Throws std::invalid_argument unless both dimensions are at least 1.
GeneratedMaze generateMaze(int width, int height, std::uint64_t seed);

/// Number of leaves in a region tree, which is the number of corridors the
/// generator stopped at. A tree with L leaves has L-1 internal nodes, one per
/// division.
std::size_t countLeaves(const RegionNode& root);

/// Longest root-to-leaf path, counting edges. This is the depth of the
/// recursion that built the maze, and so the stack it needed.
std::size_t treeDepth(const RegionNode& root);
