#include <gtest/gtest.h>

#include <stdexcept>

#include "graph.hpp"

TEST(Graph, StartsWithoutEdges) {
    const Graph graph(3);
    EXPECT_EQ(graph.vertex_count(), 3u);
    EXPECT_TRUE(graph.neighbours(0).empty());
}

TEST(Graph, EdgesAreUndirected) {
    Graph graph(2);
    graph.add_edge(0, 1);
    EXPECT_EQ(graph.neighbours(0), std::vector<std::size_t>{1});
    EXPECT_EQ(graph.neighbours(1), std::vector<std::size_t>{0});
}

TEST(Graph, RefusesUnknownVertices) {
    Graph graph(2);
    EXPECT_THROW(graph.add_edge(0, 2), std::out_of_range);
}
