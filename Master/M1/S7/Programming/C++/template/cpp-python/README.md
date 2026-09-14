# C++ project template, with Python bindings

What TP8 adds to [../cpp/](../cpp/): one Python module per file in
`bindings/`, built only when asked for. This folder holds the additions
alone, with the example's binding in `bindings/graphs.cpp`;
`../new-project.sh cpp-python <destination>` copies the C++ skeleton, lays
these files over it, and leaves `bindings/` empty. Read the C++ README first.

| Path | Role |
|---|---|
| `bindings/` | One `.cpp` per pybind11 module, named after the file: `bindings/graphs.cpp`, the example, builds `graphs` |
| `cmake/pybind11.cmake` | Finds the activated environment's Python and pybind11, or fetches pybind11 |
| `cmake/README.md` | The option and the decisions this template adds |
| `CMakeLists.txt` | Replaces the C++ one: the same options plus `BUILD_PYTHON_LIB` |
| `CMakePresets.json` | Replaces the C++ one: the same included presets plus `python` |

A whole project with a module: [worked-example.md](worked-example.md).

## Build and import

```bash
conda activate m1ai-programming            # the env the module will import from
cmake --preset python && cmake --build --preset python
cd build/python && python -c 'import graphs'      # the stem of the bindings/ file
```

`PYBIND11_MODULE(name, m)` in a binding file must use the file's own stem: that
is what names the target and the `.so`. A binding is compiled under the same
flags as the rest; pybind11's headers are system includes and stay silent.

## From TP8's provided files

| The handout gives | Put it in |
|---|---|
| `*_binding_module.cpp` | `bindings/<module_name>.cpp` |
| a cloned `pybind11/` folder | nowhere: the env's copy is used, or a pinned release is fetched |
| `-DBUILD_PYTHON_LIB=ON` | the `python` preset |
