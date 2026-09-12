// What the report claims about generation and search, checked on real runs.

#include "maze_generator.hpp"
#include "maze_invariants.hpp"
#include "maze_solver.hpp"

#include <gtest/gtest.h>

#include <stdexcept>
#include <vector>

namespace {

/// Sizes that exercise the base case as well as the ordinary one: a single
/// cell, corridors in both directions, and squat, tall and square areas.
const std::vector<std::pair<int, int>> kSizes = {
    {1, 1},  {1, 2},  {2, 1},  {1, 40}, {40, 1}, {2, 2},
    {3, 7},  {8, 5},  {16, 16}, {31, 17}};

}  // namespace

TEST(Generation, RejectsEmptyDimensions) {
  EXPECT_THROW(generateMaze(0, 5, 1), std::invalid_argument);
  EXPECT_THROW(generateMaze(5, 0, 1), std::invalid_argument);
  EXPECT_THROW(generateMaze(-1, 5, 1), std::invalid_argument);
}

TEST(Generation, ProducesASpanningTree) {
  for (const auto& [width, height] : kSizes) {
    for (std::uint64_t seed = 0; seed < 20; ++seed) {
      const Maze maze = generateMaze(width, height, seed).maze;
      EXPECT_EQ(maze.doorCount() + 1, maze.cellCount())
          << width << "x" << height << " seed " << seed;
      EXPECT_TRUE(isSpanningTree(maze)) << width << "x" << height;
      EXPECT_LE(maxDoorsPerCell(maze), 4u);
    }
  }
}

TEST(Generation, CorridorsAreLaidDownWhole) {
  // A one-cell-wide area is its own corridor: the recursion stops at once, so
  // the region tree is a single leaf and every door is the corridor's.
  const GeneratedMaze generated = generateMaze(1, 40, 7);
  EXPECT_EQ(countLeaves(*generated.regionTree), 1u);
  EXPECT_EQ(generated.maze.doorCount(), 39u);
  EXPECT_TRUE(generated.regionTree->isLeaf());
}

TEST(Generation, IsReproducibleFromItsSeed) {
  const Maze first = generateMaze(12, 9, 4242).maze;
  const Maze second = generateMaze(12, 9, 4242).maze;
  for (int y = 0; y < first.height(); ++y) {
    for (int x = 0; x < first.width(); ++x) {
      EXPECT_EQ(first.neighbours({x, y}), second.neighbours({x, y}));
    }
  }
}

TEST(Maze, RefusesDoorsThatAreNotDoors) {
  Maze maze(4, 4);
  EXPECT_THROW(maze.openDoor({0, 0}, {2, 0}), std::invalid_argument);
  EXPECT_THROW(maze.openDoor({0, 0}, {4, 0}), std::invalid_argument);
  maze.openDoor({0, 0}, {1, 0});
  EXPECT_THROW(maze.openDoor({0, 0}, {1, 0}), std::invalid_argument);
  EXPECT_THROW(maze.openDoor({1, 0}, {0, 0}), std::invalid_argument);
}

TEST(Search, FindsTheSameRouteWhateverTheGuide) {
  for (const auto& [width, height] : kSizes) {
    for (std::uint64_t seed = 0; seed < 10; ++seed) {
      const Maze maze = generateMaze(width, height, seed).maze;
      const Cell start{0, 0};
      const Cell exit{width - 1, height - 1};

      const SearchResult plain =
          shortestPathToExit(maze, start, exit, Heuristic::None);
      for (const Heuristic heuristic :
           {Heuristic::Manhattan, Heuristic::Euclidean}) {
        for (const HeuristicUse use :
             {HeuristicUse::TieBreak, HeuristicUse::Priority}) {
          const SearchResult guided =
              shortestPathToExit(maze, start, exit, heuristic, use);
          EXPECT_EQ(plain.path, guided.path)
              << toString(heuristic) << " as " << toString(use);
        }
      }
      EXPECT_EQ(plain.path.front(), start);
      EXPECT_EQ(plain.path.back(), exit);
    }
  }
}

TEST(Search, ReturnsAWalkableRoute) {
  const Maze maze = generateMaze(20, 14, 11).maze;
  const SearchResult result = shortestPathToExit(
      maze, {0, 0}, {19, 13}, Heuristic::Manhattan);
  ASSERT_FALSE(result.path.empty());
  for (std::size_t i = 1; i < result.path.size(); ++i) {
    EXPECT_TRUE(maze.hasDoor(result.path[i - 1], result.path[i]))
        << "step " << i << " crosses a wall";
  }
  EXPECT_EQ(result.steps(), result.path.size() - 1);
}

TEST(Search, RejectsCellsOutsideTheGrid) {
  const Maze maze = generateMaze(5, 5, 1).maze;
  EXPECT_THROW(shortestPathToExit(maze, {-1, 0}, {4, 4}, Heuristic::Manhattan),
               std::out_of_range);
  EXPECT_THROW(shortestPathToExit(maze, {0, 0}, {5, 5}, Heuristic::Manhattan),
               std::out_of_range);
}
