#include <pybind11/pybind11.h>
#include <pybind11/stl.h>  // converts a Python sequence to std::vector

#include "statistics.hpp"

namespace py = pybind11;

// Python module `cpp_statistics`: the name must equal this file's stem, which
// is what cmake/pybind11.cmake calls the target and the .so it produces.
// std::invalid_argument crosses into Python as ValueError.
PYBIND11_MODULE(cpp_statistics, m) {
    m.doc() = "Statistics on sequences of numbers, computed in C++";
    m.def("mean", &mean, "Arithmetic mean of a non-empty sequence", py::arg("values"));
}
