#include "maze_solver.hpp"

#include <algorithm>
#include <cmath>
#include <limits>
#include <queue>
#include <stdexcept>
#include <vector>

namespace {

double estimateToExit(Cell c, Cell exit, Heuristic heuristic) {
  const double dx = static_cast<double>(c.x - exit.x);
  const double dy = static_cast<double>(c.y - exit.y);
  switch (heuristic) {
    case Heuristic::Manhattan:
      return std::abs(dx) + std::abs(dy);
    case Heuristic::Euclidean:
      return std::sqrt(dx * dx + dy * dy);
    case Heuristic::None:
      break;
  }
  return 0.0;
}

struct QueueEntry {
  double priority;   ///< what the queue sorts on
  double estimate;   ///< separates cells of equal priority
  long long distance;
  Cell cell;

  /// std::priority_queue pops the greatest, so this is reversed: smallest
  /// priority first, and among equals the cell closest to the exit.
  bool operator>(const QueueEntry& other) const {
    if (priority != other.priority) return priority > other.priority;
    return estimate > other.estimate;
  }
};

}  // namespace

const char* toString(Heuristic heuristic) {
  switch (heuristic) {
    case Heuristic::None: return "none";
    case Heuristic::Manhattan: return "manhattan";
    case Heuristic::Euclidean: return "euclidean";
  }
  return "unknown";
}

const char* toString(HeuristicUse use) {
  switch (use) {
    case HeuristicUse::TieBreak: return "tie-break";
    case HeuristicUse::Priority: return "priority";
  }
  return "unknown";
}

SearchResult shortestPathToExit(const Maze& maze, Cell start, Cell exit,
                                Heuristic heuristic, HeuristicUse use) {
  if (!maze.contains(start) || !maze.contains(exit)) {
    throw std::out_of_range("start or exit lies outside the maze");
  }

  constexpr long long kUnreached = std::numeric_limits<long long>::max();
  std::vector<long long> distance(maze.cellCount(), kUnreached);
  std::vector<Cell> parent(maze.cellCount());
  std::vector<bool> settled(maze.cellCount(), false);

  const auto enqueue = [&](std::priority_queue<QueueEntry,
                                               std::vector<QueueEntry>,
                                               std::greater<QueueEntry>>& queue,
                           Cell cell, long long through) {
    const double estimate = estimateToExit(cell, exit, heuristic);
    const double priority = use == HeuristicUse::Priority
                                ? static_cast<double>(through) + estimate
                                : static_cast<double>(through);
    queue.push({priority, estimate, through, cell});
  };

  std::priority_queue<QueueEntry, std::vector<QueueEntry>,
                      std::greater<QueueEntry>>
      queue;
  distance[maze.indexOf(start)] = 0;
  parent[maze.indexOf(start)] = start;
  enqueue(queue, start, 0);

  SearchResult result;
  while (!queue.empty()) {
    const QueueEntry entry = queue.top();
    queue.pop();
    const std::size_t here = maze.indexOf(entry.cell);
    if (settled[here]) continue;  // a stale copy left by an earlier relaxation
    settled[here] = true;
    ++result.expanded;

    if (entry.cell == exit) break;

    for (const Cell next : maze.neighbours(entry.cell)) {
      const std::size_t there = maze.indexOf(next);
      const long long through = entry.distance + 1;  // one door, one step
      if (through < distance[there]) {
        distance[there] = through;
        parent[there] = entry.cell;
        enqueue(queue, next, through);
      }
    }
  }

  if (distance[maze.indexOf(exit)] == kUnreached) return result;

  for (Cell c = exit;; c = parent[maze.indexOf(c)]) {
    result.path.push_back(c);
    if (c == start) break;
  }
  std::reverse(result.path.begin(), result.path.end());
  return result;
}
