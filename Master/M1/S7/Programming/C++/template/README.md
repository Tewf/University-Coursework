# C++ project template

The layout every C++ practical and project here starts from: a static library
in `src/` with its headers in `include/`, one executable per file in `apps/`,
Google Test in `tests/`, and one Python module per file in `bindings/` when
asked for. C++20, compiled under `-Wall -Wextra -Wpedantic -Werror`. It is the
course's skeleton reworked; [cmake/README.md](cmake/README.md) lists every
option and the reason behind each choice.

## Layout

| Path | Role |
|---|---|
| `CMakeLists.txt` | Targets only: the library, the executables, the options |
| `CMakePresets.json` | The build configurations: `debug`, `asan`, `release`, `python` |
| `cmake/` | Compiler flags and each optional dependency, one file each |
| `include/` | Public headers, one per unit, a contract comment on every declaration |
| `src/` | The library's sources; leave it empty for a header-only library |
| `apps/` | One `.cpp` per executable, named after the file: `apps/main.cpp` builds `main` |
| `tests/` | Google Test sources, one file per unit under test |
| `bindings/` | One `.cpp` per pybind11 module, named after the file; built with `BUILD_PYTHON_LIB` |
| `build/<preset>/` | Generated, never committed |

The worked example is one function, `mean`, present in all five folders to
show where each kind of file goes. Replace it.

## Start a project

```bash
./new-project.sh ../TP9-something        # any path outside this folder
cd ../TP9-something
cmake --preset debug && cmake --build --preset debug && ctest --preset debug
```

The script copies everything but `build/`, names the CMake project after the
destination folder, and does not copy itself.

## Build, run, test

| Want | Run |
|---|---|
| Debug build with tests | `cmake --preset debug`, then `cmake --build --preset debug` |
| Run | `./build/debug/main 1 2 3` |
| Tests | `ctest --preset debug`, or `./build/debug/tests` for Google Test's own report |
| Release (`-O3`) | the same with `release`; output lands in `build/release/` |
| Memory errors | `cmake --preset asan`, then build and test as above; or `valgrind ./build/debug/main` |
| Python module | activate the course env, `cmake --preset python`, `cmake --build --preset python`, then `import cpp_statistics` from inside `build/python/` |
| Handout's form | `cmake -S . -B build && cmake --build build`: Release, no tests, output in `build/` |
| Debugger | `gdb ./build/debug/main`, or VS Code's CMake Tools, which reads the presets |

A file added to `src/`, `apps/`, `tests/` or `bindings/` needs no CMake edit:
the next build picks it up. So does an edit to `CMakeLists.txt` or `cmake/`.
A concurrency exercise is observed in `debug` (no optimisation), a timing one in `release`.

## From a handout's provided files

| The handout gives | Put it in |
|---|---|
| `include/*.hpp`, `src/*.cpp`, `tests/*.cpp` | the same folders |
| `src/main.cpp`, or any file that defines `main` | `apps/` |
| a pybind11 `*_binding_module.cpp` | `bindings/<name>.cpp`, the stem being the `PYBIND11_MODULE` name |
| its own `CMakeLists.txt` | nowhere: this one covers it; diff them when a flag differs |
| a cloned `pybind11/` folder | nowhere: `cmake/pybind11.cmake` uses the env's copy or fetches one |

## What the code must look like

A contract comment on every public declaration (what it takes, returns and
guarantees, never how it works), no exercise-specific constant inside `src/`,
and a test for anything meant to be reused. The example files show the register.
