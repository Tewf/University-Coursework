#include "maze_generator.hpp"

#include <algorithm>
#include <random>
#include <utility>

namespace {

/// Draws uniformly from the inclusive range [low, high]. Requires low <= high,
/// which the caller guarantees by never cutting an axis of extent 0.
int randomIn(std::mt19937_64& rng, int low, int high) {
  return std::uniform_int_distribution<int>(low, high)(rng);
}

/// Opens the doors of a region one cell thick, joining its cells end to end.
/// One of the two loops is empty by construction, and on a single cell both
/// are, so the same code covers a row, a column and one cell.
void spanCorridor(Maze& maze, Cell p, Cell q) {
  for (int x = p.x; x < q.x; ++x) maze.openDoor({x, p.y}, {x + 1, p.y});
  for (int y = p.y; y < q.y; ++y) maze.openDoor({p.x, y}, {p.x, y + 1});
}

std::unique_ptr<RegionNode> divide(Maze& maze, std::mt19937_64& rng, Cell p,
                                   Cell q) {
  auto node = std::make_unique<RegionNode>();
  node->upperLeft = p;
  node->lowerRight = q;

  if (p.x == q.x || p.y == q.y) {  // a corridor: nothing left to decide
    spanCorridor(maze, p, q);
    return node;
  }

  // Both sides are at least two cells, so both axes admit a wall and the coin
  // needs no feasibility test in front of it.
  const int axis = randomIn(rng, 0, 1);
  const int other = 1 - axis;
  const int wall = randomIn(rng, p[axis], q[axis] - 1);
  const int door = randomIn(rng, p[other], q[other]);

  maze.openDoor(Cell::onAxis(axis, wall, door),
                Cell::onAxis(axis, wall + 1, door));

  node->axis = axis;
  node->wallPosition = wall;
  node->doorPosition = door;
  node->left = divide(maze, rng, p, q.withAxis(axis, wall));
  node->right = divide(maze, rng, p.withAxis(axis, wall + 1), q);
  return node;
}

}  // namespace

GeneratedMaze generateMaze(int width, int height, std::uint64_t seed) {
  Maze maze(width, height);  // validates the dimensions
  std::mt19937_64 rng(seed);
  auto tree = divide(maze, rng, Cell{0, 0}, Cell{width - 1, height - 1});
  return GeneratedMaze{std::move(maze), std::move(tree)};
}

std::size_t countLeaves(const RegionNode& root) {
  if (root.isLeaf()) return 1;
  return countLeaves(*root.left) + countLeaves(*root.right);
}

std::size_t treeDepth(const RegionNode& root) {
  if (root.isLeaf()) return 0;
  return 1 + std::max(treeDepth(*root.left), treeDepth(*root.right));
}
