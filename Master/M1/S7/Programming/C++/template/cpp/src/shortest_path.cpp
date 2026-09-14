#include "shortest_path.hpp"

#include <algorithm>
#include <optional>
#include <queue>

std::vector<std::size_t> shortest_path(const Graph& graph, std::size_t source, std::size_t target) {
    // parent[v] is the vertex v was discovered from; the source is its own parent.
    std::vector<std::optional<std::size_t>> parent(graph.vertex_count());
    parent.at(source) = source;
    std::queue<std::size_t> frontier;
    frontier.push(source);
    while (!frontier.empty() && !parent.at(target)) {
        const std::size_t u = frontier.front();
        frontier.pop();
        for (const std::size_t v : graph.neighbours(u)) {
            if (!parent[v]) {
                parent[v] = u;
                frontier.push(v);
            }
        }
    }
    if (!parent[target]) {
        return {};
    }
    std::vector<std::size_t> path;
    for (std::size_t v = target; v != source; v = *parent[v]) {
        path.push_back(v);
    }
    path.push_back(source);
    std::reverse(path.begin(), path.end());
    return path;
}
