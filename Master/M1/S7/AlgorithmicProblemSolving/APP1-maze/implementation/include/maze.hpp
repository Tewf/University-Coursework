#pragma once

#include "cell.hpp"

#include <cstddef>
#include <vector>

/// A maze on a `width` x `height` grid: every cell is a node carrying the
/// neighbours it has a door to. A door is recorded at both of its ends, and a
/// wall is recorded nowhere -- it is simply a door that was never opened.
///
/// A freshly built Maze has no doors. Once a generator has finished, the graph
/// is a spanning tree of the grid: exactly `width * height - 1` doors, and
/// exactly one simple path between any two cells.
class Maze {
public:
  /// A maze of `width` x `height` cells with no doors.
  /// Throws std::invalid_argument unless both dimensions are at least 1.
  Maze(int width, int height);

  int width() const { return width_; }
  int height() const { return height_; }
  std::size_t cellCount() const { return neighbours_.size(); }

  /// Number of doors, each counted once.
  std::size_t doorCount() const;

  /// Opens a door between two cells.
  /// Throws std::invalid_argument if either cell is outside the grid, if they
  /// are not adjacent, or if the door is already open: a generator that opens
  /// one twice has a bug, and silence would hide it.
  void openDoor(Cell a, Cell b);

  /// The cells `c` has a door to, in the order the doors were opened.
  /// Throws std::out_of_range if `c` is outside the grid.
  const std::vector<Cell>& neighbours(Cell c) const;

  /// True when a door joins `a` and `b`. False for cells that are not
  /// adjacent, so a caller may ask about any pair.
  bool hasDoor(Cell a, Cell b) const;

  bool contains(Cell c) const;

  /// A dense index in [0, cellCount()) for `c`, so that an algorithm can hold
  /// one entry per cell in a flat vector instead of a map.
  /// Requires `contains(c)`.
  std::size_t indexOf(Cell c) const;

private:

  int width_;
  int height_;
  std::vector<std::vector<Cell>> neighbours_;
};
