# Names the project and picks its pieces. What gets built is in
# cmake/targets.cmake, the flags in cmake/compiler-options.cmake, each
# optional dependency in its own cmake/*.cmake; cmake/README.md explains them.
cmake_minimum_required(VERSION 3.24)  # FetchContent's FIND_PACKAGE_ARGS
project(change_me LANGUAGES CXX)      # new-project.sh renames this

option(BUILD_TESTS "Build the Google Test executable from tests/" OFF)
option(ENABLE_SANITIZERS "Compile with AddressSanitizer and UBSan" OFF)
option(WARN_EFFCXX "Add -Weffc++ to the warning set" OFF)

include(cmake/targets.cmake)  # the library and the executables
if(BUILD_TESTS)
  include(cmake/googletest.cmake)
endif()
