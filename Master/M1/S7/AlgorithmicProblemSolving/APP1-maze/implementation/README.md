# APP1 maze — C implementation

Generates a maze by recursive division, returning **two** structures, and finds
the route out of each — then measures what each way cost.

C11, one Makefile, nothing outside the standard library, built with
`-Wall -Wextra -Wpedantic -Werror`.

## Running it

```bash
make
./maze 24 16 7 maze.svg   # width height seed output
./benchmark 200           # the report's tables, 200 mazes per size
make test                 # 1121 assertions
```

## Layout

| File | Role |
|---|---|
| `cell.{h,c}` | a cell, and the axis operations the division needs |
| `maze.{h,c}` | **first output**: cells, coordinates, neighbour lists |
| `region_tree.{h,c}` | **second output**: divisions, doors, addresses |
| `generator.{h,c}` | recursive division, filling both outputs at once |
| `solver.{h,c}` | Dijkstra on the graph; common-ancestor descent on the tree |
| `invariants.{h,c}` | the properties a finished maze must have |
| `svg.{h,c}` | drawing a maze, and a route through it |
| `tests.c` `benchmark.c` | the checks, and the measurements |

Two deliberate choices. The invariants are their own module, because a
generator that checked its own work would only confirm its own assumptions. And
randomness comes from a small `xorshift` rather than `rand()`, so a seed
determines a maze on any machine.

## What it found

Both solvers return the same route, cell for cell — the maze is a spanning
tree, so there is only one. What differs is how much each examines. At
256×256, mean of 200 mazes:

| | examined |
|---|---|
| Dijkstra | 56 193 |
| A\* with Manhattan | 53 753 |
| **common ancestor on the tree** | **1 776** |

A factor of thirty, and the gap widens with size: `Theta(n^0.68)` against
`Theta(n)`.

## Where the explanation lives

Not here. The concepts are in the Notes vault under
`S7/Algorithmic Problem Solving/`, and the design decisions behind these
algorithms in `Projects/APP1 - Maze - Report Design Decisions.md` there.
