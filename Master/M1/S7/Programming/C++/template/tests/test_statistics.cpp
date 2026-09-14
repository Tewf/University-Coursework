#include <gtest/gtest.h>

#include <stdexcept>

#include "statistics.hpp"

TEST(Mean, AveragesItsInput) {
    EXPECT_DOUBLE_EQ(mean({1.0, 2.0, 3.0}), 2.0);
    EXPECT_DOUBLE_EQ(mean({5.0}), 5.0);
    EXPECT_DOUBLE_EQ(mean({-1.0, 1.0}), 0.0);
}

TEST(Mean, RefusesEmptyInput) {
    EXPECT_THROW(mean({}), std::invalid_argument);
}
