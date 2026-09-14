#include <atomic>
#include <chrono>
#include <cstdlib>
#include <iostream>
#include <thread>
#include <vector>

#include "graph.hpp"
#include "shortest_path.hpp"

// Usage: benchmark [side] [threads]
// Builds a side x side grid graph and answers one corner-to-corner query per
// thread, all at once; prints the wall time. Meant for the release preset.
int main(int argc, char* argv[]) {
    const std::size_t side = argc > 1 ? std::stoul(argv[1]) : 300;
    const unsigned thread_count = argc > 2 ? static_cast<unsigned>(std::stoul(argv[2])) : 4;

    Graph grid(side * side);
    for (std::size_t row = 0; row < side; ++row) {
        for (std::size_t column = 0; column + 1 < side; ++column) {
            grid.add_edge(row * side + column, row * side + column + 1);  // right
            grid.add_edge(column * side + row, (column + 1) * side + row);  // down
        }
    }

    std::atomic<std::size_t> total_length{0};
    const auto start = std::chrono::steady_clock::now();
    std::vector<std::thread> workers;
    for (unsigned i = 0; i < thread_count; ++i) {
        workers.emplace_back([&] { total_length += shortest_path(grid, 0, side * side - 1).size(); });
    }
    for (auto& worker : workers) {
        worker.join();
    }
    const std::chrono::duration<double> elapsed = std::chrono::steady_clock::now() - start;
    std::cout << thread_count << " queries on " << side * side << " vertices: " << elapsed.count()
              << " s, path length " << total_length / thread_count << '\n';
    return EXIT_SUCCESS;
}
