# pybind11 modules: one per .cpp in bindings/, named after the file. The
# PYBIND11_MODULE(name, m) inside the file must use that same name.
#
# Usage:
#   a new module: bindings/<name>.cpp; the build makes build/python/<name>.*.so,
#     importable from that directory or with it on PYTHONPATH.
#   which Python: the environment active at configure time (conda activate
#     first). FindPython looks in $VIRTUAL_ENV, then $CONDA_PREFIX, before
#     PATH; -DPython_EXECUTABLE=... overrides both.
#   a newer pybind11: change GIT_TAG; the environment's copy is still tried first.
find_package(Python COMPONENTS Interpreter Development.Module REQUIRED)

# A pip or conda install of pybind11 ships its CMake config; the interpreter
# says where. When the environment has none, the pinned release is fetched.
execute_process(
  COMMAND "${Python_EXECUTABLE}" -m pybind11 --cmakedir
  OUTPUT_VARIABLE pybind11_DIR
  OUTPUT_STRIP_TRAILING_WHITESPACE
  ERROR_QUIET
)
include(FetchContent)
FetchContent_Declare(
  pybind11
  GIT_REPOSITORY https://github.com/pybind/pybind11.git
  GIT_TAG        v3.1.0
  FIND_PACKAGE_ARGS CONFIG
)
FetchContent_MakeAvailable(pybind11)

file(GLOB BINDING_SOURCES CONFIGURE_DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/bindings/*.cpp")
foreach(binding_source IN LISTS BINDING_SOURCES)
  get_filename_component(module_name "${binding_source}" NAME_WE)
  pybind11_add_module(${module_name} "${binding_source}")
  target_link_libraries(${module_name} PRIVATE project_library project_warnings)
endforeach()
