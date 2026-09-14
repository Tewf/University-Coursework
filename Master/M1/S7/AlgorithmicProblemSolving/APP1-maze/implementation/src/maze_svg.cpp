#include "maze_svg.hpp"

#include <fstream>
#include <stdexcept>

namespace {

struct Painter {
  std::ofstream& out;
  const SvgOptions& options;

  int at(int gridCoordinate) const {
    return options.margin + gridCoordinate * options.cellSize;
  }
  int centreOf(int gridCoordinate) const {
    return at(gridCoordinate) + options.cellSize / 2;
  }

  void line(int x1, int y1, int x2, int y2, const std::string& colour,
            int width) const {
    out << "  <line x1=\"" << x1 << "\" y1=\"" << y1 << "\" x2=\"" << x2
        << "\" y2=\"" << y2 << "\" stroke=\"" << colour << "\" stroke-width=\""
        << width << "\" stroke-linecap=\"square\"/>\n";
  }
};

}  // namespace

void writeMazeSvg(const Maze& maze, const std::string& filename,
                  const std::vector<Cell>& path, std::optional<Cell> exit,
                  const SvgOptions& options) {
  std::ofstream out(filename);
  if (!out) throw std::runtime_error("cannot write " + filename);

  const Painter paint{out, options};
  const int fullWidth = 2 * options.margin + maze.width() * options.cellSize;
  const int fullHeight = 2 * options.margin + maze.height() * options.cellSize;

  out << "<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"" << fullWidth
      << "\" height=\"" << fullHeight << "\" viewBox=\"0 0 " << fullWidth << " "
      << fullHeight << "\">\n";
  out << "  <rect width=\"100%\" height=\"100%\" fill=\"white\"/>\n";

  if (exit) {
    out << "  <rect x=\"" << paint.at(exit->x) << "\" y=\"" << paint.at(exit->y)
        << "\" width=\"" << options.cellSize << "\" height=\""
        << options.cellSize << "\" fill=\"" << options.exitColour
        << "\" fill-opacity=\"0.25\"/>\n";
  }

  // The area is enclosed on every side: the exit is a cell, not a gap.
  paint.line(paint.at(0), paint.at(0), paint.at(maze.width()), paint.at(0),
             options.wallColour, options.wallWidth);
  paint.line(paint.at(0), paint.at(maze.height()), paint.at(maze.width()),
             paint.at(maze.height()), options.wallColour, options.wallWidth);
  paint.line(paint.at(0), paint.at(0), paint.at(0), paint.at(maze.height()),
             options.wallColour, options.wallWidth);
  paint.line(paint.at(maze.width()), paint.at(0), paint.at(maze.width()),
             paint.at(maze.height()), options.wallColour, options.wallWidth);

  // One segment wherever two neighbouring cells have no door between them.
  for (int y = 0; y < maze.height(); ++y) {
    for (int x = 0; x < maze.width(); ++x) {
      const Cell here{x, y};
      if (x + 1 < maze.width() && !maze.hasDoor(here, {x + 1, y})) {
        paint.line(paint.at(x + 1), paint.at(y), paint.at(x + 1),
                   paint.at(y + 1), options.wallColour, options.wallWidth);
      }
      if (y + 1 < maze.height() && !maze.hasDoor(here, {x, y + 1})) {
        paint.line(paint.at(x), paint.at(y + 1), paint.at(x + 1),
                   paint.at(y + 1), options.wallColour, options.wallWidth);
      }
    }
  }

  for (std::size_t i = 1; i < path.size(); ++i) {
    paint.line(paint.centreOf(path[i - 1].x), paint.centreOf(path[i - 1].y),
               paint.centreOf(path[i].x), paint.centreOf(path[i].y),
               options.pathColour, options.pathWidth);
  }

  out << "</svg>\n";
}
