// Measures what the three tie-breaking rules cost, over many mazes and seeds.
// The report's table comes from this program; run it with no arguments to
// reproduce, or pass a seed count to change the sample.

#include "maze_generator.hpp"
#include "maze_invariants.hpp"
#include "maze_solver.hpp"

#include <cstdint>
#include <cstdlib>
#include <exception>
#include <cmath>
#include <iomanip>
#include <iostream>
#include <vector>

namespace {

struct Sample {
  double meanExpanded = 0.0;
  double meanSteps = 0.0;
};

Sample measure(int width, int height, std::uint64_t seeds, Heuristic heuristic,
               HeuristicUse use) {
  Sample sample;
  for (std::uint64_t seed = 0; seed < seeds; ++seed) {
    const Maze maze = generateMaze(width, height, seed).maze;
    const SearchResult result = shortestPathToExit(
        maze, Cell{0, 0}, Cell{width - 1, height - 1}, heuristic, use);
    sample.meanExpanded += static_cast<double>(result.expanded);
    sample.meanSteps += static_cast<double>(result.steps());
  }
  sample.meanExpanded /= static_cast<double>(seeds);
  sample.meanSteps /= static_cast<double>(seeds);
  return sample;
}

}  // namespace

int main(int argc, char** argv) {
  std::uint64_t seeds = 200;
  if (argc > 1) {
    try {
      seeds = std::stoull(argv[1]);
    } catch (const std::exception&) {
      std::cerr << "usage: " << argv[0] << " [seeds per size]\n";
      return EXIT_FAILURE;
    }
  }

  const std::vector<std::pair<int, int>> sizes = {
      {8, 8}, {16, 16}, {32, 32}, {64, 64}, {128, 128}};

  std::cout << seeds << " mazes per size, start (0,0), exit at the far corner\n"
            << "cells expanded by the search, mean over the seeds\n\n";
  std::cout << std::left << std::setw(10) << "size" << std::right
            << std::setw(8) << "cells" << std::setw(8) << "steps"
            << std::setw(10) << "dijkstra" << std::setw(10) << "tie:man"
            << std::setw(10) << "tie:euc" << std::setw(10) << "A*:man"
            << std::setw(10) << "A*:euc" << "\n";

  for (const auto& [width, height] : sizes) {
    const Sample plain =
        measure(width, height, seeds, Heuristic::None, HeuristicUse::TieBreak);
    const Sample tieMan = measure(width, height, seeds, Heuristic::Manhattan,
                                  HeuristicUse::TieBreak);
    const Sample tieEuc = measure(width, height, seeds, Heuristic::Euclidean,
                                  HeuristicUse::TieBreak);
    const Sample starMan = measure(width, height, seeds, Heuristic::Manhattan,
                                   HeuristicUse::Priority);
    const Sample starEuc = measure(width, height, seeds, Heuristic::Euclidean,
                                   HeuristicUse::Priority);

    const std::string label =
        std::to_string(width) + "x" + std::to_string(height);
    std::cout << std::left << std::setw(10) << label << std::right
              << std::setw(8) << width * height << std::setw(8) << std::fixed
              << std::setprecision(1) << plain.meanSteps << std::setw(10)
              << plain.meanExpanded << std::setw(10) << tieMan.meanExpanded
              << std::setw(10) << tieEuc.meanExpanded << std::setw(10)
              << starMan.meanExpanded << std::setw(10) << starEuc.meanExpanded
              << "\n";
  }

  std::cout << "\nregion tree, mean over the same seeds\n";
  std::cout << std::left << std::setw(10) << "size" << std::right
            << std::setw(10) << "leaves" << std::setw(10) << "depth"
            << std::setw(14) << "balanced" << "\n";
  for (const auto& [width, height] : sizes) {
    double leaves = 0.0;
    double depth = 0.0;
    for (std::uint64_t seed = 0; seed < seeds; ++seed) {
      const GeneratedMaze generated = generateMaze(width, height, seed);
      leaves += static_cast<double>(countLeaves(*generated.regionTree));
      depth += static_cast<double>(treeDepth(*generated.regionTree));
    }
    leaves /= static_cast<double>(seeds);
    depth /= static_cast<double>(seeds);
    const std::string label =
        std::to_string(width) + "x" + std::to_string(height);
    std::cout << std::left << std::setw(10) << label << std::right
              << std::setw(10) << std::fixed << std::setprecision(1) << leaves
              << std::setw(10) << depth << std::setw(14)
              << std::log2(leaves) << "\n";
  }

  // A generator that checked its own work would only confirm its assumptions,
  // so the invariant is verified here, on the same mazes the table measured.
  std::size_t checked = 0;
  for (const auto& [width, height] : sizes) {
    for (std::uint64_t seed = 0; seed < seeds; ++seed) {
      if (!isSpanningTree(generateMaze(width, height, seed).maze)) {
        std::cerr << "not a spanning tree: " << width << "x" << height
                  << " seed " << seed << "\n";
        return EXIT_FAILURE;
      }
      ++checked;
    }
  }
  std::cout << "\n" << checked << " mazes checked: every one a spanning tree\n";
  return EXIT_SUCCESS;
}
