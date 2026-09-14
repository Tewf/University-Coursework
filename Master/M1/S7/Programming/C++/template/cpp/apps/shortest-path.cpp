#include <cstdlib>
#include <exception>
#include <fstream>
#include <iostream>
#include <string>

#include "graph.hpp"
#include "shortest_path.hpp"

// Usage: shortest-path <edges file> <source> <target>
// The file's first line is the vertex count, each following line one edge
// "u v". Prints the path one vertex per line, or "no path".
int main(int argc, char* argv[]) {
    if (argc != 4) {
        std::cerr << "usage: " << argv[0] << " <edges file> <source> <target>\n";
        return EXIT_FAILURE;
    }
    try {
        std::ifstream edges(argv[1]);
        if (!edges) {
            throw std::runtime_error(std::string("cannot open ") + argv[1]);
        }
        std::size_t vertex_count = 0;
        edges >> vertex_count;
        Graph graph(vertex_count);
        for (std::size_t u = 0, v = 0; edges >> u >> v;) {
            graph.add_edge(u, v);
        }
        const auto path = shortest_path(graph, std::stoul(argv[2]), std::stoul(argv[3]));
        if (path.empty()) {
            std::cout << "no path\n";
            return EXIT_FAILURE;
        }
        for (const std::size_t v : path) {
            std::cout << v << '\n';
        }
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << '\n';
        return EXIT_FAILURE;
    }
    return EXIT_SUCCESS;
}
