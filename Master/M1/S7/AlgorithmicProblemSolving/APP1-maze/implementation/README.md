# APP1 maze — C++ implementation

Generates a random maze by recursive division, then finds the route out of it,
measuring how much of the maze each search setting had to look at.

The handout leaves code optional and provides a C skeleton. This is written in
C++ instead, against the algorithms derived in [../report/](../report/).

## Building and running

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build

./build/maze 24 16 7 maze.svg   # width height seed output
./build/benchmark 200           # the report's tables, 200 mazes per size
```

Tests need GoogleTest, which CMake fetches on first configure:

```bash
cmake -S . -B build-tests -DBUILD_TESTS=ON && cmake --build build-tests
./build-tests/tests
```

C++20, `-Wall -Wextra -Wpedantic -Werror`, the course's `cmake-template` layout.

## Layout

| File | Role |
|---|---|
| `include/cell.hpp` | a cell, and the two axis operations the division needs |
| `maze.{hpp,cpp}` | node records: coordinates and neighbour lists |
| `maze_generator.{hpp,cpp}` | recursive division, and the region tree it builds |
| `maze_solver.{hpp,cpp}` | Dijkstra, with a distance estimate as tie-break or as priority |
| `maze_invariants.{hpp,cpp}` | the properties a finished maze must have |
| `maze_svg.{hpp,cpp}` | drawing a maze, and a route through it |
| `tests/tests.cpp` | the invariants, on shapes including 1x1, 1x40, 40x1 |
| `tests/benchmark.cpp` | the measurements the report's tables come from |

The invariants are their own module because a generator that checked its own
work would only confirm its own assumptions.

## What it found

Every setting returns the same route — the maze is a spanning tree, so there is
only one — and what separates them is cells expanded. On 128x128, mean of 200
mazes: Dijkstra 14128, either estimate as a tie-break 14124, A* with Manhattan
13303, A* with Euclidean 13489. Manhattan as a priority wins; as a tie-break
neither estimate does anything, for the reason Section 4 of the report proves.

## Where the explanation lives

Not here. The concepts are in the Notes vault under
`S7/Algorithmic Problem Solving/`, and the design decisions behind these
algorithms are in `Projects/APP1 - Maze - Report Design Decisions.md` there.
