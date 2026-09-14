# C++ templates

Two starting points, one source of truth:

| Template | Start here when | Adds |
|---|---|---|
| [cpp/](cpp/) | the project is a C++ program with tests: every practical but TP8 | nothing: library, executables, tests, presets |
| [cpp-python/](cpp-python/) | the C++ must also be imported from Python: TP8, and the TSP solver's measurements | `bindings/`, `cmake/pybind11.cmake`, the `python` preset |

Each template folder is a worked example that builds, the project
`shortest-path`; `cpp-python/` holds only what it adds to `cpp/`. The script
copies the skeleton of `cpp/`, lays the chosen template's over it, and leaves
the source folders empty, so an edit to the C++ template is the Python one's
edit too, and nothing exists twice.

Each template has a worked example, a whole project on its layout with the
commands and what they printed: [cpp/worked-example.md](cpp/worked-example.md)
and [cpp-python/worked-example.md](cpp-python/worked-example.md).

## Start a project

```bash
./new-project.sh cpp ../TP9-something          # or cpp-python
cd ../TP9-something
cmake --preset debug && cmake --build --preset debug && ctest --preset debug
```

The script names the CMake project after the destination folder (a third
argument names it otherwise). Every CMake file it copies opens with a comment
saying what to edit for each kind of change.
