#include <pybind11/pybind11.h>

namespace py=pybind11;

const float pi = 3.1415;
const float e = 2.7183;
const float golden_ratio = 1.6181;

int gcd(int a, int b){
    int tmp;
    while(b > 0){
        tmp = b;
        b = a % b;
        a = tmp;
    }
    return a;
}

int lcm(int a, int b)
{
    return (a / gcd(a, b)) * b;
}


// TODO : Add the missing variables and functions to the module

PYBIND11_MODULE(my_math, m, py::mod_gil_not_used()){
    m.doc() = "A small arithmetics library";
    m.attr("pi") = pi;
    m.def("gcd", &gcd, "A function that computes the gcd between two numbers");
}