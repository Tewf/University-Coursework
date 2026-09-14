# cmake/ (Python additions)

Laid over [../../cpp/cmake/](../../cpp/cmake/) by `new-project.sh`, whose README
lists every option and the decisions behind the C++ side. Added here:

| File | Role | Included |
|---|---|---|
| `pybind11.cmake` | one Python module per file in `bindings/` | `BUILD_PYTHON_LIB=ON` |

| Option | Default | Effect |
|---|---|---|
| `BUILD_PYTHON_LIB` | `OFF`; the `python` preset sets `ON` | builds `bindings/*.cpp` into importable modules |
| `Python_EXECUTABLE` | the activated venv or conda interpreter | which Python the modules are built for |

## Decisions, and the trail behind each

- **pybind11: the environment's copy first, then fetch.** TP8's handout clones pybind11 into
  the project; the course env already ships 3.1.0 with its CMake config, found through
  `python -m pybind11 --cmakedir`, the route pybind11's own documentation gives for CMake.
  `FIND_PACKAGE_ARGS CONFIG` tries it first and fetches the pinned release otherwise.
- **The interpreter is the activated env's.** FindPython looks in `VIRTUAL_ENV`, then
  `CONDA_PREFIX`, before PATH (`Python_FIND_VIRTUALENV`, default `FIRST`, read in its source).
  Observed on this machine: a shell that still exported `VIRTUAL_ENV` from an earlier venv
  made CMake pick that interpreter over the conda env activated afterwards; `-DPython_EXECUTABLE`
  overrides.
- **An overlay rather than a second copy or symlinks.** With the option off, the C++ template
  still carried a `bindings/` folder, a preset and a cmake file about Python. A full second
  template would hold every shared file twice; symlinks are refused by this repository's
  pre-commit hook (ergonomic conventions §9, a Windows or Android clone breaks on them). So
  this folder holds only the additions, and the script composes the two.
