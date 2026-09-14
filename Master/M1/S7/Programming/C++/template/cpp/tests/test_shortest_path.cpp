#include <gtest/gtest.h>

#include "graph.hpp"
#include "shortest_path.hpp"

namespace {
// 0 - 1 - 2 - 3, plus the shortcut 0 - 3; 4 is isolated.
Graph line_with_shortcut() {
    Graph graph(5);
    graph.add_edge(0, 1);
    graph.add_edge(1, 2);
    graph.add_edge(2, 3);
    graph.add_edge(0, 3);
    return graph;
}
}  // namespace

TEST(ShortestPath, TakesTheShortcut) {
    const auto path = shortest_path(line_with_shortcut(), 1, 3);
    EXPECT_EQ(path, (std::vector<std::size_t>{1, 0, 3}));
}

TEST(ShortestPath, SingleVertexWhenSourceIsTarget) {
    EXPECT_EQ(shortest_path(line_with_shortcut(), 2, 2), std::vector<std::size_t>{2});
}

TEST(ShortestPath, EmptyWhenDisconnected) {
    EXPECT_TRUE(shortest_path(line_with_shortcut(), 0, 4).empty());
}
