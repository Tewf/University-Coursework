#include <gtest/gtest.h>
#include "utils.hpp"

TEST(GcdTest, BasicCases) {
    EXPECT_EQ(gcd(10, 4), 2);
    EXPECT_EQ(gcd(18, 48), 6);
    EXPECT_EQ(gcd(0, 5), 5);
    EXPECT_EQ(gcd(5, 0), 5);
    EXPECT_EQ(gcd(0, 0), 0);
}

TEST(GcdTest, PrimeNumbers) {
    EXPECT_EQ(gcd(13, 17), 1);
    EXPECT_EQ(gcd(17, 13), 1);
}

// TODO : add more tests e.g. negative numbers, edge cases such as 1, same numbers etc.
// TODO : add tests for the other utility functions you will implement 
