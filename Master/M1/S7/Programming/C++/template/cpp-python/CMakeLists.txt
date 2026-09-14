# The C++ template plus pybind11. new-project.sh lays this folder over ../cpp,
# so this file replaces the C++ one: same options, one more piece.
cmake_minimum_required(VERSION 3.24)  # FetchContent's FIND_PACKAGE_ARGS
project(change_me LANGUAGES CXX)      # new-project.sh renames this

option(BUILD_TESTS "Build the Google Test executable from tests/" OFF)
option(BUILD_PYTHON_LIB "Build one pybind11 module per file in bindings/" OFF)
option(ENABLE_SANITIZERS "Compile with AddressSanitizer and UBSan" OFF)
option(WARN_EFFCXX "Add -Weffc++ to the warning set" OFF)

include(cmake/targets.cmake)  # the library and the executables
if(BUILD_TESTS)
  include(cmake/googletest.cmake)
endif()
if(BUILD_PYTHON_LIB)
  include(cmake/pybind11.cmake)
endif()
