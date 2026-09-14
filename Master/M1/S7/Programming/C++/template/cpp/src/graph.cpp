#include "graph.hpp"

#include <stdexcept>

Graph::Graph(std::size_t vertex_count) : adjacency_(vertex_count) {}

void Graph::add_edge(std::size_t u, std::size_t v) {
    if (u >= adjacency_.size() || v >= adjacency_.size()) {
        throw std::out_of_range("add_edge: vertex out of range");
    }
    adjacency_[u].push_back(v);
    adjacency_[v].push_back(u);
}

std::size_t Graph::vertex_count() const { return adjacency_.size(); }

const std::vector<std::size_t>& Graph::neighbours(std::size_t u) const { return adjacency_.at(u); }
