# A worked example: `shortest-path`

A whole project on this template: a graph library, a shortest-path algorithm
on it, two programs and their tests. Built and run on this machine on 2026-09-14.

## The project

```
shortest-path/
  CMakeLists.txt (names the project, declares the options, includes the cmake/ pieces; untouched)
  CMakePresets.json (includes cmake/base-presets.json; untouched)
  square.txt (test data: 5 vertices, then the edges 0 1, 1 2, 2 3, 0 3; vertex 4 is isolated)

cmake/
  targets.cmake (turns src/ into the library and each apps/ file into a program; untouched)
  compiler-options.cmake (the -Wall -Wextra -Wpedantic -Werror set, applied to every target; untouched)
  googletest.cmake (builds tests/ into the tests program, registers each test with CTest; untouched)
  base-presets.json (the debug, asan and release configurations; untouched)

include/
  graph.hpp (declares class Graph: constructor from a vertex count, add_edge, neighbours, vertex_count; add_edge's contract says it throws std::out_of_range on an unknown vertex)
  shortest_path.hpp (declares shortest_path(graph, source, target): the vertices of a shortest path, empty when there is none)

src/
  graph.cpp (defines Graph: adjacency lists, the range check, both directions of an edge)
  shortest_path.cpp (defines shortest_path: breadth-first search, parents recorded, the path rebuilt backwards)

apps/
  shortest-path.cpp (the program shortest-path: reads an edge file and two vertices from the command line, prints the path or "no path"; parsing and printing only)
  benchmark.cpp (the program benchmark: builds a grid graph, runs one query per std::thread, prints the wall time)

tests/
  test_graph.cpp (three Google Tests on Graph: starts empty, edges go both ways, an unknown vertex throws)
  test_shortest_path.cpp (three on shortest_path: takes the shortcut, source equals target, disconnected gives empty)

build/
  debug/, release/, asan/ (generated, one folder per preset, never committed)
```

## How they work together

At build time, `cmake/targets.cmake` reads the folders and draws this graph:

```
include/*.hpp ─┐
src/*.cpp ─────┴─► project_library  (build/<preset>/libshortest-path.a)
                       ├─► apps/shortest-path.cpp ─► build/<preset>/shortest-path
                       ├─► apps/benchmark.cpp ─────► build/<preset>/benchmark
                       └─► tests/*.cpp + Google Test ─► build/<preset>/tests ─► ctest
compiler-options.cmake ─► the same flags on every box above
CMakePresets.json ──────► which <preset>: debug (-g), release (-O3), asan
```

The library is compiled once and linked three times. A program never includes
another program; a test never includes a program: everything shared is in
`src/` and reached through `include/`. Adding `src/dijkstra.cpp` tomorrow puts
it in the library and in every program and test at the next build, no CMake edit.

At run time, `./build/debug/shortest-path square.txt 1 3` flows the other way:
`main` opens `square.txt`, feeds each line to `Graph::add_edge`, calls
`shortest_path(graph, 1, 3)`, and prints what comes back. The library does the
work and knows nothing about files or the terminal, which is why the same
functions serve `benchmark`, the tests, and, in the `cpp-python` template's
[worked example](../cpp-python/worked-example.md), Python.

## The commands, and what they printed

| Command | Output |
|---|---|
| `cmake --preset debug && cmake --build --preset debug` | `Built target project_library`, `benchmark`, `shortest-path`, `tests` |
| `ctest --preset debug` | `100% tests passed, 0 tests failed out of 6`, each test listed by name |
| `./build/debug/shortest-path square.txt 1 3` | `1`, `0`, `3`: the shortcut, not `1 2 3` |
| `./build/debug/shortest-path square.txt 0 4` | `no path`, exit status 1 |
| `cmake --preset release && cmake --build --preset release && ./build/release/benchmark 300 4` | `4 queries on 90000 vertices: 0.0027 s, path length 599` |
| `./build/debug/benchmark 300 4` | `0.0120 s`: four times slower, so timings are taken in `release` |
| `cmake --preset asan && cmake --build --preset asan && ctest --preset asan` | `100% tests passed`, no sanitizer report |
