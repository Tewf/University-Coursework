#include <cstdlib>
#include <exception>
#include <iostream>
#include <string>
#include <vector>

#include "statistics.hpp"

// Usage: main <number>...
// Prints the mean of the numbers given on the command line. Exit status is
// EXIT_FAILURE when no number is given or one of them does not parse.
int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "usage: " << argv[0] << " <number>...\n";
        return EXIT_FAILURE;
    }
    try {
        std::vector<double> values;
        for (int i = 1; i < argc; ++i) {
            values.push_back(std::stod(argv[i]));
        }
        std::cout << mean(values) << '\n';
    } catch (const std::exception& error) {
        std::cerr << "error: " << error.what() << '\n';
        return EXIT_FAILURE;
    }
    return EXIT_SUCCESS;
}
