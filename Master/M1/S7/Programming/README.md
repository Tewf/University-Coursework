# Programming

> [Lire en français](README.fr.md) · [Open on the site ↗](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/)

**Course:** Programming, M1 Artificial Intelligence, Semester 7, Université Grenoble Alpes
**Instructor:** E. Foussard, with J. Perier-Camby on Python TP3

Twelve practicals across two languages and one project. Python for tooling and
data, C++ for the machinery underneath, then a bridge between the two.

## What You'll Learn

- Build and reproduce Python environments with venv, pip, uv and conda
- Treat images as Numpy arrays: padding, convolution, blurring, edge detection
- Write command-line tools that walk a filesystem and hash what they find
- Compile C++ with CMake under `-Wall -Wextra -Wpedantic -Werror`, and test it with Google Test
- Manage memory in C++: destructors, copy semantics, and smart pointers
- Implement the STL iterator contract by hand, then make it generic with templates
- Share state between threads: mutexes, condition variables and atomics
- Expose C++ to Python with pybind11

## TP Overview

Each practical has a **steps** page: the steps it asks for, and for work already
done, what each step decided and the reference that settled it.

### Python

| TP | Topic | Folder | Steps |
|----|-------|--------|-------|
| TP1 | Virtual environments, pip, uv, notebooks | [Python/TP1-environments/](Python/TP1-environments/README.md) | [view](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/Python/TP1-environments/steps/) |
| TP2 | Images as Numpy arrays, convolution, edge detection | [Python/TP2-image-processing/](Python/TP2-image-processing/README.md) | [view](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/Python/TP2-image-processing/steps/) |
| TP3 | A command-line tool that finds duplicate files | [Python/TP3-cli-tool/](Python/TP3-cli-tool/README.md) | [view](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/Python/TP3-cli-tool/steps/) |
| TP4 | The `logging` module, then a logger of your own | [Python/TP4-logger/](Python/TP4-logger/README.md) | [view](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/Python/TP4-logger/steps/) |

### C++

| TP | Topic | Folder | Steps |
|----|-------|--------|-------|
| TP1 | First programs, CMake, Boost, Google Test | [C++/TP1-first-programs/](C++/TP1-first-programs/README.md) | [view](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/C++/TP1-first-programs/steps/) |
| TP2 | C++ without objects: a 2D vector as free functions | [C++/TP2-without-objects/](C++/TP2-without-objects/README.md) | [view](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/C++/TP2-without-objects/steps/) |
| TP3 | The same vector, now a class | [C++/TP3-custom-vectors/](C++/TP3-custom-vectors/README.md) | [view](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/C++/TP3-custom-vectors/steps/) |
| TP4 | Object-oriented programming and graphs | [C++/TP4-oop-graphs/](C++/TP4-oop-graphs/README.md) | [view](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/C++/TP4-oop-graphs/steps/) |
| TP5 | Subsets, iterators | [C++/TP5-subsets/](C++/TP5-subsets/README.md) | [view](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/C++/TP5-subsets/steps/) |
| TP6 | Templates | [C++/TP6-templates/](C++/TP6-templates/README.md) | [view](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/C++/TP6-templates/steps/) |
| TP7 | Concurrent programming | [C++/TP7-concurrency/](C++/TP7-concurrency/README.md) | [view](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/C++/TP7-concurrency/steps/) |
| TP8 | Interoperability: binding C++ to Python with pybind11 | [C++/TP8-interoperability/](C++/TP8-interoperability/README.md) | [view](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/C++/TP8-interoperability/steps/) |

### Project

[Project-TSPSolver/](Project-TSPSolver/README.md) solves the Travelling Salesman
Problem, exactly with Held-Karp and then approximately, and measures one against
the other. [Steps ↗](https://tewf.github.io/University-Coursework/Master/M1/S7/Programming/Project-TSPSolver/steps/)

## Prerequisites

Python and one compiled language. The C++ side assumes no prior C++, but it does
assume you have met pointers before: `C++/reference/` holds the course's own note
on pointers and references.

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

## Folder Structure

Every practical has the same shape. An archive is unpacked into the folder it
belongs to rather than left sitting beside it, so each one reads as a working
project: the `provided-files/` wrapper is removed once emptied, and what came
out of it is listed in that folder's README.

```
Programming/
|-- environment.yml          <- the one conda environment, for every Python TP
|-- Python/
|   |-- TP1-environments/
|   |   |-- handout/         <- the subject PDF beside its .txt extraction
|   |   |-- steps/           <- index.html, then one page per step
|   |   |-- README.md        <- what it asks, what it provides, how to run it
|   |   |-- meteo.py         <- the provided code, set up in place
|   |-- TP2-image-processing/ ... TP4-logger/
|-- C++/
|   |-- cmake-template/      <- the skeleton every C++ TP starts from
|   |-- reference/           <- the course note on pointers and references
|   |-- TP1-first-programs/ ... TP8-interoperability/
|-- Project-TSPSolver/       <- the project, and the TSPLIB instances
```

`handout/` is gitignored everywhere: the subjects are not mine to republish.

## Tools & Libraries

| Tool | Used in | For |
|------|---------|-----|
| conda | all Python TPs | the one declared environment |
| venv, pip, uv | TP1 Python | the subject of the practical itself |
| Numpy, Pillow | TP2, TP3 Python | images as arrays |
| click, tqdm | TP3 Python | the command-line tool |
| CMake | all C++ TPs | building, testing, and the warning flags |
| Boost, Google Test | C++ TP1 onward | utilities and unit tests |
| pybind11 | C++ TP8 | exposing C++ to Python |

## How the code here is written

Clean, reusable, and commented so it survives being lifted into another project.
Beyond that, one rule governs: **easy to read, and efficient in effort.** Code
reads obviously on first pass, effort stops where more polish buys less than it
costs, and every non-obvious choice carries its reference *and* the trail that
found it, so it can be rechecked rather than taken on trust. The `steps/` pages
are where that trail is written down.

Explanations of the concepts themselves live in a separate Obsidian vault, not
here: a comment that starts teaching theory belongs in the note instead.

## Source material

The TP subjects, and the code provided with them, are **not redistributed
here**: see [NOTICE](../../../../NOTICE). They stay on disk next to each TP,
alongside a `.txt` extraction that makes them greppable, and `.gitignore` keeps
both out of the repository. What is committed is my own work.
