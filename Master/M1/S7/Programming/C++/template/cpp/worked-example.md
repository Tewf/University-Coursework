# A worked example: `shortest-path`

A project that uses every part of this template: a graph library, a
shortest-path algorithm on it, two programs and their tests. Every command and
output below was run on this machine on 2026-09-14.

```
shortest-path/                         ../new-project.sh cpp ../shortest-path
├── include/graph.hpp                  class Graph: vertices, add_edge, neighbours
├── include/shortest_path.hpp          shortest_path(graph, source, target)
├── src/graph.cpp                      the library: what both programs and the
├── src/shortest_path.cpp                tests share, and nothing else
├── apps/shortest-path.cpp             reads an edge file, prints the path
├── apps/benchmark.cpp                 grid graph, one query per std::thread, wall time
├── tests/test_graph.cpp               one test file per header
├── tests/test_shortest_path.cpp
├── square.txt                         a data file: vertex count, then one "u v" edge per line
└── CMakeLists.txt, CMakePresets.json, cmake/   untouched from the template
```

## What goes where, and why

- **`include/` declares, `src/` defines.** The header carries the contract, the
  source the work. `graph.hpp` says `add_edge` throws `std::out_of_range` on an
  unknown vertex; `graph.cpp` is where the check lives.
- **`apps/` holds `main` and nothing reusable.** `shortest-path.cpp` only parses
  arguments, opens the file, and prints. Both programs link the library; neither
  is in it, so `benchmark` and `shortest-path` cannot collide.
- **`tests/` mirrors `include/`.** Three tests per header: the normal case, the
  edge case (source equals target), the refusal (`EXPECT_THROW`, disconnected).
- **The data file sits at the root**, read by path from the command line, so no
  path is hard-coded in `src/`.

## The loop, with what came out

| Step | Command | Output |
|---|---|---|
| Configure and build | `cmake --preset debug && cmake --build --preset debug` | `Built target project_library`, `benchmark`, `shortest-path`, `tests` |
| Test | `ctest --preset debug` | `6/6 ... 100% tests passed`, each `TEST()` listed by name |
| Run | `./build/debug/shortest-path square.txt 1 3` | `1 0 3`: the shortcut, not the long way round |
| A failure | `./build/debug/shortest-path square.txt 0 4` | `no path`, exit status 1 |
| The archive | `ls build/debug/*.a` | `libshortest-path.a`: the project's name, not the target's |
| Time it | `cmake --preset release && cmake --build --preset release`, then `./build/release/benchmark 300 4` | `4 queries on 90000 vertices: 0.0027 s` |
| Same in debug | `./build/debug/benchmark 300 4` | `0.0120 s`: four times slower, which is why timings are taken in `release` |
| Memory check | `cmake --preset asan && cmake --build --preset asan && ctest --preset asan` | `100% tests passed`, no report |

The three build directories coexist, so switching from a Debug session under
`gdb` to a Release timing is one `--preset` word, never a rebuild of the other.

## What the example checked in the template

Building it found one defect: the library target was named after the project,
so `apps/shortest-path.cpp` in a project called `shortest-path` could not exist.
The target is now `project_library` (see `cmake/README.md`). Everything else held:
`std::thread` linked without a flag, the system or fetched Google Test was found,
and `-Wall -Wextra -Wpedantic -Werror` passed on all eight source files at the
first build. The same project with a Python module: the `cpp-python` template's
[worked example](../cpp-python/worked-example.md).
