# Names the project and picks its pieces. Nothing about which files exist is
# written here: the folders are read at build time (cmake/targets.cmake).
#
# To add ...                   do this
#   an executable              drop <name>.cpp in apps/; it becomes the program <name>
#   library code               a .cpp in src/ and its header in include/
#   a test                     a .cpp in tests/; the tests program and CTest pick it up
#   a system library (Boost)   cmake/targets.cmake, the "External dependencies" block
#   a compiler flag            cmake/compiler-options.cmake
#   a build configuration      cmake/base-presets.json
#   an on/off feature          an option() below, then if(...) include(cmake/<feature>.cmake)
# Nothing above needs a configure step: the next `cmake --build` sees it.
cmake_minimum_required(VERSION 3.24)  # FetchContent's FIND_PACKAGE_ARGS
project(shortest-path LANGUAGES CXX)  # new-project.sh renames this

option(BUILD_TESTS "Build the Google Test executable from tests/" OFF)
option(ENABLE_SANITIZERS "Compile with AddressSanitizer and UBSan" OFF)
option(WARN_EFFCXX "Add -Weffc++ to the warning set" OFF)

include(cmake/targets.cmake)  # the library and the executables
if(BUILD_TESTS)
  include(cmake/googletest.cmake)
endif()
