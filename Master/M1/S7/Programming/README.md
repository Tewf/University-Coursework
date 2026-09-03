# Programming

> [Lire en français](README.fr.md)

M1 Artificial Intelligence, semester 7, Université Grenoble Alpes. Taught by
E. Foussard. Twelve practicals across two languages and one project: Python for
tooling and data, C++ for the machinery underneath, then a bridge between them.

## Setting up

The Python side is one conda environment, declared once in
[environment.yml](environment.yml):

```bash
conda env create -f environment.yml
conda activate m1ai-programming
```

That environment also registers itself as the Jupyter kernel
*Python 3.11 (m1ai-programming)*, which is what TP1 question 7 asks for.

The C++ side takes its libraries from `apt`, so CMake's `find_package()` finds
them in `/usr` like any system library:

```bash
sudo apt install libboost-all-dev libgtest-dev
```

TP8 is the exception: its `CMakeLists.txt` calls `add_subdirectory(pybind11)`,
so it wants a checkout inside the project rather than the copy in the conda
environment. Run `git clone https://github.com/pybind/pybind11.git` from the TP
folder, as its handout says.

## Python

| TP | Topic | Folder |
|----|-------|--------|
| TP1 | Virtual environments, pip, uv, notebooks | [Python/TP1-environments/](Python/TP1-environments/README.md) |
| TP2 | Images as Numpy arrays, convolution, edge detection | [Python/TP2-image-processing/](Python/TP2-image-processing/) |
| TP3 | A command-line tool that finds duplicate files | [Python/TP3-cli-tool/](Python/TP3-cli-tool/) |
| TP4 | The `logging` module, then a logger of your own | [Python/TP4-logger/](Python/TP4-logger/) |

## C++

| TP | Topic | Folder |
|----|-------|--------|
| TP1 | First programs, CMake, Boost, Google Test | [C++/TP1-first-programs/](C++/TP1-first-programs/) |
| TP2 | C++ without objects: a 2D vector as free functions | [C++/TP2-without-objects/](C++/TP2-without-objects/) |
| TP3 | The same vector, now a class | [C++/TP3-custom-vectors/](C++/TP3-custom-vectors/) |
| TP4 | Object-oriented programming and graphs | [C++/TP4-oop-graphs/](C++/TP4-oop-graphs/) |
| TP5 | Subsets, iterators | [C++/TP5-subsets/](C++/TP5-subsets/) |
| TP6 | Templates | [C++/TP6-templates/](C++/TP6-templates/) |
| TP7 | Concurrent programming | [C++/TP7-concurrency/](C++/TP7-concurrency/) |
| TP8 | Interoperability: binding C++ to Python with pybind11 | [C++/TP8-interoperability/](C++/TP8-interoperability/) |

Every C++ TP starts from the same skeleton, `C++/cmake-template/`, with the
library in `src/`, headers in `include/` and tests in `tests/`:

```bash
cmake -S . -B build          # add -DBUILD_TESTS=ON to build the tests too
cmake --build build
./build/main                 # ./build/tests
```

**A fresh TP folder is expected to fail its first build.** The template compiles
with `-Wall -Wextra -Wpedantic -Werror`, and the provided sources are stubs that
`throw std::runtime_error("Not implemented yet")`, so every unused parameter is
an error until you implement the function. That is the exercise, not a broken
setup.

## Project

[Project-TSPSolver/](Project-TSPSolver/) solves the Travelling Salesman
Problem. `instance_generator.py` builds random instances; `TSP-instances/` holds
the TSPLIB benchmarks to measure against.

## Handouts

The TP subjects, and the code E. Foussard provides with them, are **not
redistributed here**: see [NOTICE](../../../../NOTICE). They stay on disk next
to each TP, alongside a `.txt` extraction that makes them greppable, and
`.gitignore` keeps both out of the repository. What is committed is my own work.
