#include "maze_invariants.hpp"

#include "cell.hpp"

#include <vector>

bool isConnected(const Maze& maze) {
  std::vector<bool> seen(maze.cellCount(), false);
  std::vector<Cell> stack{Cell{0, 0}};
  seen[maze.indexOf(Cell{0, 0})] = true;
  std::size_t reached = 1;

  while (!stack.empty()) {
    const Cell here = stack.back();
    stack.pop_back();
    for (const Cell next : maze.neighbours(here)) {
      const std::size_t index = maze.indexOf(next);
      if (seen[index]) continue;
      seen[index] = true;
      ++reached;
      stack.push_back(next);
    }
  }
  return reached == maze.cellCount();
}

bool isSpanningTree(const Maze& maze) {
  return maze.doorCount() + 1 == maze.cellCount() && isConnected(maze);
}

std::size_t maxDoorsPerCell(const Maze& maze) {
  std::size_t most = 0;
  for (int y = 0; y < maze.height(); ++y) {
    for (int x = 0; x < maze.width(); ++x) {
      const std::size_t here = maze.neighbours(Cell{x, y}).size();
      if (here > most) most = here;
    }
  }
  return most;
}
