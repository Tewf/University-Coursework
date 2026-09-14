# C++ project template

The layout every C++ practical and project here starts from: a static library
in `src/` with its headers in `include/`, one executable per file in `apps/`,
Google Test in `tests/`. C++20, compiled under `-Wall -Wextra -Wpedantic
-Werror`. It is the course's skeleton reworked; [cmake/README.md](cmake/README.md)
lists every option and the reason behind each choice. A project that must
also be imported from Python starts from [../cpp-python/](../cpp-python/) instead.

## Layout

| Path | Role |
|---|---|
| `CMakeLists.txt` | Names the project, declares the options, picks the pieces |
| `CMakePresets.json` | Includes `cmake/base-presets.json`: `debug`, `asan`, `release` |
| `cmake/` | The targets, the compiler flags and each optional dependency, one file each |
| `include/` | Public headers, one per unit, a contract comment on every declaration |
| `src/` | The library's sources; leave it empty for a header-only library |
| `apps/` | One `.cpp` per executable, named after the file: `apps/main.cpp` builds `main` |
| `tests/` | Google Test sources, one file per unit under test |
| `build/<preset>/` | Generated, never committed |

The four folders start empty. A blank project configures and builds: the
library is header-only until `src/` has a file, the `tests` program appears
with the first file in `tests/`. A whole project on this layout, file by file:
[worked-example.md](worked-example.md).

## Start a project

```bash
../new-project.sh cpp ../../TP9-something   # any path outside template/
cd ../../TP9-something
cmake --preset debug && cmake --build --preset debug && ctest --preset debug
```

The script copies everything but `build/` and names the CMake project after
the destination folder.

## Build, run, test

| Want | Run |
|---|---|
| Debug build with tests | `cmake --preset debug`, then `cmake --build --preset debug` |
| Run | `./build/debug/<program>`, one per file in `apps/` |
| Tests | `ctest --preset debug`, or `./build/debug/tests` for Google Test's own report |
| Release (`-O3`) | the same with `release`; output lands in `build/release/` |
| Memory errors | `cmake --preset asan`, then build and test as above; or `valgrind ./build/debug/main` |
| Handout's form | `cmake -S . -B build && cmake --build build`: Release, no tests, output in `build/` |
| Debugger | `gdb ./build/debug/main`, or VS Code's CMake Tools, which reads the presets |

A file added to `src/`, `apps/` or `tests/` needs no CMake edit:
the next build picks it up. So does an edit to `CMakeLists.txt` or `cmake/`.
A concurrency exercise is observed in `debug` (no optimisation), a timing one in `release`.

## From a handout's provided files

| The handout gives | Put it in |
|---|---|
| `include/*.hpp`, `src/*.cpp`, `tests/*.cpp` | the same folders |
| `src/main.cpp`, or any file that defines `main` | `apps/` |
| its own `CMakeLists.txt` | nowhere: this one covers it; diff them when a flag differs |

## What the code must look like

A contract comment on every public declaration (what it takes, returns and
guarantees, never how it works), no exercise-specific constant inside `src/`,
and a test for anything meant to be reused. The example files show the register.
