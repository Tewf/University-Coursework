# Google Test for tests/: the system package when one is installed
# (libgtest-dev on Ubuntu), otherwise the pinned release is fetched at
# configure time. FIND_PACKAGE_ARGS is what makes FetchContent try
# find_package first (CMake >= 3.24).
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
  message(FATAL_ERROR "BUILD_TESTS is ON but tests/ holds no .cpp file")
endif()

enable_testing()
add_executable(tests ${TEST_SOURCES})
target_link_libraries(tests PRIVATE ${PROJECT_NAME} GTest::gtest_main project_warnings)

# Registers each TEST() with CTest by name, so `ctest` reports them one by one
# and `ctest -R Mean` runs a subset.
include(GoogleTest)
gtest_discover_tests(tests)
