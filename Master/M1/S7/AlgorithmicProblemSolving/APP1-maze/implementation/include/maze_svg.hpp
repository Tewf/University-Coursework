#pragma once

#include "cell.hpp"
#include "maze.hpp"

#include <optional>
#include <string>
#include <vector>

/// Everything the drawing lets a caller choose, so that no size or colour is
/// written into the drawing code.
struct SvgOptions {
  int cellSize = 20;              ///< side of one cell, in SVG units
  int margin = 10;                ///< blank border around the maze
  std::string wallColour = "#222222";
  std::string pathColour = "#1565C0";
  std::string exitColour = "#E65100";
  int wallWidth = 2;
  int pathWidth = 3;
};

/// Writes the maze to `filename` as SVG: one line per wall, plus the outer
/// boundary, which is drawn closed because the exit is a cell and not a gap.
///
/// `path`, when non-empty, is drawn through the centres of its cells. `exit`,
/// when given, is filled.
///
/// Throws std::runtime_error if the file cannot be opened.
void writeMazeSvg(const Maze& maze, const std::string& filename,
                  const std::vector<Cell>& path = {},
                  std::optional<Cell> exit = std::nullopt,
                  const SvgOptions& options = {});
