#include "statistics.hpp"

#include <numeric>
#include <stdexcept>

double mean(const std::vector<double>& values) {
    if (values.empty()) {
        throw std::invalid_argument("mean: empty input");
    }
    const double sum = std::accumulate(values.begin(), values.end(), 0.0);
    return sum / static_cast<double>(values.size());
}
