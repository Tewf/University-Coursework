// Generates one maze, solves it once per tie-breaking rule, and reports what
// each rule cost. The three runs return the same route -- on a spanning tree
// there is only one -- so the figure that differs is the number of cells each
// search had to expand to find it.

#include "maze_generator.hpp"
#include "maze_solver.hpp"
#include "maze_svg.hpp"

#include <cstdint>
#include <cstdlib>
#include <exception>
#include <iostream>
#include <string>
#include <vector>

namespace {

struct Arguments {
  int width = 24;
  int height = 16;
  std::uint64_t seed = 1;
  std::string svgPath = "maze.svg";
};

void printUsage(const char* programName) {
  std::cerr << "usage: " << programName
            << " [width] [height] [seed] [output.svg]\n"
            << "  defaults: 24 16 1 maze.svg\n";
}

}  // namespace

int main(int argc, char** argv) {
  Arguments arguments;
  try {
    if (argc > 1) arguments.width = std::stoi(argv[1]);
    if (argc > 2) arguments.height = std::stoi(argv[2]);
    if (argc > 3) arguments.seed = std::stoull(argv[3]);
    if (argc > 4) arguments.svgPath = argv[4];
  } catch (const std::exception&) {
    printUsage(argv[0]);
    return EXIT_FAILURE;
  }

  try {
    const GeneratedMaze generated =
        generateMaze(arguments.width, arguments.height, arguments.seed);
    const Maze& maze = generated.maze;

    // Any cell may be the exit; the far corner simply makes a long route.
    const Cell start{0, 0};
    const Cell exit{maze.width() - 1, maze.height() - 1};

    std::cout << maze.width() << "x" << maze.height() << ", seed "
              << arguments.seed << ": " << maze.cellCount() << " cells, "
              << maze.doorCount() << " doors, "
              << countLeaves(*generated.regionTree) << " corridors\n";

    struct Setting {
      Heuristic heuristic;
      HeuristicUse use;
    };
    const Setting settings[] = {
        {Heuristic::None, HeuristicUse::TieBreak},
        {Heuristic::Manhattan, HeuristicUse::TieBreak},
        {Heuristic::Euclidean, HeuristicUse::TieBreak},
        {Heuristic::Manhattan, HeuristicUse::Priority},
        {Heuristic::Euclidean, HeuristicUse::Priority},
    };

    std::vector<Cell> route;
    for (const Setting& setting : settings) {
      const SearchResult result = shortestPathToExit(
          maze, start, exit, setting.heuristic, setting.use);
      std::cout << "  " << toString(setting.heuristic) << " as "
                << toString(setting.use) << ": " << result.steps()
                << " steps, " << result.expanded << " cells expanded\n";
      route = result.path;
    }

    writeMazeSvg(maze, arguments.svgPath, route, exit);
    std::cout << "wrote " << arguments.svgPath << "\n";
  } catch (const std::exception& error) {
    std::cerr << "error: " << error.what() << "\n";
    return EXIT_FAILURE;
  }
  return EXIT_SUCCESS;
}
