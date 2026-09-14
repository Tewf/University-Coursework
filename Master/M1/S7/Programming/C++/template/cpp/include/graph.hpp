#pragma once

#include <cstddef>
#include <vector>

// An undirected graph on the vertices 0 .. vertex_count() - 1, stored as
// adjacency lists. Edges are added once and never removed.
class Graph {
public:
    // A graph with `vertex_count` vertices and no edge.
    explicit Graph(std::size_t vertex_count);

    // Adds the edge {u, v}. Throws std::out_of_range when u or v is not a vertex.
    void add_edge(std::size_t u, std::size_t v);

    std::size_t vertex_count() const;

    // The vertices adjacent to `u`, in insertion order.
    const std::vector<std::size_t>& neighbours(std::size_t u) const;

private:
    std::vector<std::vector<std::size_t>> adjacency_;
};
