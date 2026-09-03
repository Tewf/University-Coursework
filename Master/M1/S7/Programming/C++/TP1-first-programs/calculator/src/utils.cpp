#include "utils.hpp"

int gcd(int a, int b)
{
    if (a == 0)
        return b;
    return gcd(b % a, a);
    // TODO : implement the function
}
