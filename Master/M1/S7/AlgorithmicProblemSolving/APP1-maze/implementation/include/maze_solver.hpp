#pragma once

#include "cell.hpp"
#include "maze.hpp"

#include <cstddef>
#include <vector>

/// Which distance to the exit the search consults.
enum class Heuristic {
  None,       ///< no estimate: the search is guided only by cost so far
  Manhattan,  ///< |dx| + |dy|, the number of steps on an empty grid
  Euclidean,  ///< straight-line distance
};

/// How much weight that estimate is given.
///
/// `TieBreak` uses it only to order cells the search has reached at equal cost,
/// leaving every computed distance untouched. `Priority` adds it to the cost,
/// which is A*: the search then leans towards the exit instead of spreading
/// evenly.
enum class HeuristicUse {
  TieBreak,
  Priority,
};

const char* toString(Heuristic heuristic);
const char* toString(HeuristicUse use);

struct SearchResult {
  /// The route from start to exit, both included. Empty when the exit is not
  /// reachable, which on a finished maze cannot happen.
  std::vector<Cell> path;

  /// Cells taken out of the queue and settled. This is the cost measure: every
  /// setting returns the same route, so what separates them is how much of the
  /// maze each had to look at.
  std::size_t expanded = 0;

  /// Doors crossed, which is one fewer than the cells on the route.
  std::size_t steps() const { return path.empty() ? 0 : path.size() - 1; }
};

/// Shortest route from `start` to `exit`, every door counting as one step.
///
/// With `Heuristic::None` this is Dijkstra's algorithm. Both heuristics are
/// admissible on this graph -- neither can exceed the true number of doors
/// between two cells -- so the route returned is a shortest one under every
/// setting, and on a spanning tree it is the only one.
///
/// Throws std::out_of_range if either cell lies outside the grid.
SearchResult shortestPathToExit(const Maze& maze, Cell start, Cell exit,
                                Heuristic heuristic,
                                HeuristicUse use = HeuristicUse::TieBreak);
