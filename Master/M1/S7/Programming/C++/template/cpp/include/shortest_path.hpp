#pragma once

#include <cstddef>
#include <vector>

#include "graph.hpp"

// The vertices of a shortest path from `source` to `target` in `graph`,
// both ends included, by breadth-first search. Empty when no path exists.
// A path from a vertex to itself is that single vertex.
std::vector<std::size_t> shortest_path(const Graph& graph, std::size_t source, std::size_t target);
