# C++ templates

Two starting points, one source of truth:

| Template | Start here when | Adds |
|---|---|---|
| [cpp/](cpp/) | the project is a C++ program with tests: every practical but TP8 | nothing: library, executables, tests, presets |
| [cpp-python/](cpp-python/) | the C++ must also be imported from Python: TP8, and the TSP solver's measurements | `bindings/`, `cmake/pybind11.cmake`, the `python` preset |

`cpp-python/` holds only its additions. The script copies `cpp/` and lays the
chosen template over it, so an edit to the C++ template is the Python one's
edit too, and nothing exists twice.

[worked-example.md](worked-example.md) walks through a complete project on
the Python template, with the commands and what they printed.

## Start a project

```bash
./new-project.sh cpp ../TP9-something          # or cpp-python
cd ../TP9-something
cmake --preset debug && cmake --build --preset debug && ctest --preset debug
```

The script leaves `build/` behind and names the CMake project after the
destination folder (a third argument names it otherwise).
