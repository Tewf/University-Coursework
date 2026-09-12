#pragma once

/// A cell of the grid, addressed by column `x` and row `y`, both counted from 0
/// at the upper-left corner.
///
/// Coordinates are reachable by index as well as by name, so that an algorithm
/// working on "the axis being cut" needs no separate case per axis: axis 0 is
/// x, axis 1 is y, and `1 - axis` is the other one.
struct Cell {
  int x = 0;
  int y = 0;

  /// Coordinate on `axis`. Requires `axis` to be 0 or 1.
  constexpr int operator[](int axis) const { return axis == 0 ? x : y; }

  /// A copy of this cell with its `axis` coordinate replaced by `value`.
  /// Requires `axis` to be 0 or 1.
  constexpr Cell withAxis(int axis, int value) const {
    return axis == 0 ? Cell{value, y} : Cell{x, value};
  }

  /// The cell whose `axis` coordinate is `along` and whose other coordinate is
  /// `across`. Requires `axis` to be 0 or 1.
  static constexpr Cell onAxis(int axis, int along, int across) {
    return axis == 0 ? Cell{along, across} : Cell{across, along};
  }

  friend constexpr bool operator==(const Cell&, const Cell&) = default;
};

/// True when the two cells share a side, which is the only way a door can join
/// them.
constexpr bool areAdjacent(Cell a, Cell b) {
  const int dx = a.x > b.x ? a.x - b.x : b.x - a.x;
  const int dy = a.y > b.y ? a.y - b.y : b.y - a.y;
  return dx + dy == 1;
}
