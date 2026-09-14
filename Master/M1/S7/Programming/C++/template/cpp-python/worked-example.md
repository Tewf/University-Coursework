# A worked example: `shortest-path`, imported from Python

The C++ template's [worked example](../cpp/worked-example.md), started with
`../new-project.sh cpp-python ../shortest-path` instead, plus one file. Read
that page for the library, the programs and the tests; this one covers only
what the Python side adds. Run on this machine on 2026-09-14.

```
shortest-path/
├── bindings/graphs.cpp                PYBIND11_MODULE(graphs, m): Graph and shortest_path
└── everything else                    as in the C++ example
```

## The binding file

`graphs.cpp` is glue only: it names the C++ entry points and adds nothing.

```cpp
PYBIND11_MODULE(graphs, m) {                       // `graphs` because the file is graphs.cpp
    py::class_<Graph>(m, "Graph")
        .def(py::init<std::size_t>(), py::arg("vertex_count"))
        .def("add_edge", &Graph::add_edge, py::arg("u"), py::arg("v"))
        .def("neighbours", &Graph::neighbours, py::arg("u"))
        .def_property_readonly("vertex_count", &Graph::vertex_count);
    m.def("shortest_path", &shortest_path, py::arg("graph"), py::arg("source"), py::arg("target"));
}
```

`#include <pybind11/stl.h>` is what lets `neighbours` and `shortest_path` return
a `std::vector` as a Python list. Nothing in `src/` knows Python exists.

## The loop, with what came out

| Step | Command | Output |
|---|---|---|
| The env the module will import from | `conda activate m1ai-programming` | pybind11 3.1.0 is found there, nothing is fetched |
| Configure and build | `cmake --preset python && cmake --build --preset python` | `Built target graphs`, then `build/python/graphs.cpython-311-x86_64-linux-gnu.so` |
| Import | from `build/python/`: `import graphs` | |
| Use | `g = graphs.Graph(5)`, four `g.add_edge(u, v)`, `graphs.shortest_path(g, 1, 3)` | `[1, 0, 3]`, the same path the C++ program printed |
| Read | `g.neighbours(0)`, `g.vertex_count` | `[1, 3]`, `5` |
| A refusal | `g.add_edge(0, 9)` | `IndexError: add_edge: vertex out of range`: the C++ `std::out_of_range`, translated by pybind11 |

The `python` preset is `release` plus `BUILD_PYTHON_LIB=ON`, so `build/python/`
also holds `shortest-path`, `benchmark` and `tests`, built with `-O3`. The
module is importable only from a directory that contains the `.so`, or with
that directory on `PYTHONPATH`; installing it as a package is outside the
template.
