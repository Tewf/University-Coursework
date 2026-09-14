#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "graph.hpp"
#include "shortest_path.hpp"

namespace py = pybind11;

// Python module `graphs`, named after this file. std::out_of_range crosses
// into Python as IndexError.
PYBIND11_MODULE(graphs, m) {
    m.doc() = "Undirected graphs and breadth-first shortest paths, in C++";
    py::class_<Graph>(m, "Graph")
        .def(py::init<std::size_t>(), py::arg("vertex_count"))
        .def("add_edge", &Graph::add_edge, py::arg("u"), py::arg("v"))
        .def("neighbours", &Graph::neighbours, py::arg("u"))
        .def_property_readonly("vertex_count", &Graph::vertex_count);
    m.def("shortest_path", &shortest_path, py::arg("graph"), py::arg("source"), py::arg("target"));
}
