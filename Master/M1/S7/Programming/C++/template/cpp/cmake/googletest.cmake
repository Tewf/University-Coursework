# Google Test for tests/: the system package when one is installed
# (libgtest-dev on Ubuntu), otherwise the pinned release is fetched at
# configure time. FIND_PACKAGE_ARGS is what makes FetchContent try
# find_package first (CMake >= 3.24).
#
# Usage:
#   a new test file: tests/<unit>.cpp with #include <gtest/gtest.h> and
#     TEST(Suite, Name) blocks; no main, gtest_main provides it.
#   run everything: ctest --preset debug; one suite: ctest --preset debug -R Suite;
#     Google Test's own report: ./build/debug/tests [--gtest_filter=Suite.*]
#   a newer release: change GIT_TAG; the system package is still tried first.
include(FetchContent)
set(INSTALL_GTEST OFF)
FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG        v1.17.0
  FIND_PACKAGE_ARGS NAMES GTest
)
FetchContent_MakeAvailable(googletest)

file(GLOB TEST_SOURCES CONFIGURE_DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/tests/*.cpp")
if(NOT TEST_SOURCES)
  message(STATUS "tests/ holds no .cpp file yet: no tests target")
  return()
endif()

enable_testing()
add_executable(tests ${TEST_SOURCES})
target_link_libraries(tests PRIVATE project_library GTest::gtest_main project_warnings)

# Registers each TEST() with CTest by name, so `ctest` reports them one by one
# and `ctest -R Mean` runs a subset.
include(GoogleTest)
gtest_discover_tests(tests)
