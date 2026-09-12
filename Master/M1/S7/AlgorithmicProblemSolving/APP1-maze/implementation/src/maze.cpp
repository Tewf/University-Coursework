#include "maze.hpp"

#include <algorithm>
#include <stdexcept>
#include <string>

namespace {
std::string describe(Cell c) {
  return "(" + std::to_string(c.x) + "," + std::to_string(c.y) + ")";
}
}  // namespace

Maze::Maze(int width, int height) : width_(width), height_(height) {
  if (width < 1 || height < 1) {
    throw std::invalid_argument(
        "a maze needs at least one cell in each dimension, got " +
        std::to_string(width) + "x" + std::to_string(height));
  }
  neighbours_.resize(static_cast<std::size_t>(width) *
                     static_cast<std::size_t>(height));
}

bool Maze::hasDoor(Cell a, Cell b) const {
  if (!contains(a) || !contains(b)) return false;
  const auto& fromA = neighbours_[indexOf(a)];
  return std::find(fromA.begin(), fromA.end(), b) != fromA.end();
}

bool Maze::contains(Cell c) const {
  return c.x >= 0 && c.x < width_ && c.y >= 0 && c.y < height_;
}

std::size_t Maze::indexOf(Cell c) const {
  return static_cast<std::size_t>(c.y) * static_cast<std::size_t>(width_) +
         static_cast<std::size_t>(c.x);
}

std::size_t Maze::doorCount() const {
  std::size_t ends = 0;
  for (const auto& list : neighbours_) ends += list.size();
  return ends / 2;  // every door is recorded at both of its ends
}

void Maze::openDoor(Cell a, Cell b) {
  if (!contains(a) || !contains(b)) {
    throw std::invalid_argument("door " + describe(a) + "-" + describe(b) +
                                " leaves the grid");
  }
  if (!areAdjacent(a, b)) {
    throw std::invalid_argument("door " + describe(a) + "-" + describe(b) +
                                " joins cells that do not share a side");
  }
  auto& fromA = neighbours_[indexOf(a)];
  if (std::find(fromA.begin(), fromA.end(), b) != fromA.end()) {
    throw std::invalid_argument("door " + describe(a) + "-" + describe(b) +
                                " is already open");
  }
  fromA.push_back(b);
  neighbours_[indexOf(b)].push_back(a);
}

const std::vector<Cell>& Maze::neighbours(Cell c) const {
  if (!contains(c)) {
    throw std::out_of_range("cell " + describe(c) + " is outside the grid");
  }
  return neighbours_[indexOf(c)];
}
