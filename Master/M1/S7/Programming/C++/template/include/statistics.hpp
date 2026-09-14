#pragma once

#include <vector>

// Arithmetic mean of `values`.
// Throws std::invalid_argument when `values` is empty: a mean of nothing has
// no value, and returning NaN would let the mistake travel silently.
double mean(const std::vector<double>& values);
