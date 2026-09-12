cmake_minimum_required(VERSION 3.14)
project(app1_maze CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

set(CMAKE_CXX_FLAGS "-Wall -Wextra -Wpedantic -Werror")
set(CMAKE_CXX_FLAGS_DEBUG "-g")
set(CMAKE_CXX_FLAGS_RELEASE "-O3")

set(SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src)
set(INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/include)
set(TEST_DIR ${CMAKE_CURRENT_SOURCE_DIR}/tests)

file(GLOB SOURCES "${SOURCE_DIR}/*.cpp")
file(GLOB HEADERS "${INCLUDE_DIR}/*.hpp")
list(REMOVE_ITEM SOURCES "${SOURCE_DIR}/main.cpp")

add_library(${PROJECT_NAME} STATIC ${SOURCES} ${HEADERS})
target_include_directories(${PROJECT_NAME} PUBLIC ${INCLUDE_DIR})

add_executable(maze ${SOURCE_DIR}/main.cpp)
target_link_libraries(maze PRIVATE ${PROJECT_NAME})

# Measures the three tie-breaking rules over many mazes; this is what the
# report's figures come from.
add_executable(benchmark ${CMAKE_CURRENT_SOURCE_DIR}/tests/benchmark.cpp)
target_link_libraries(benchmark PRIVATE ${PROJECT_NAME})

# Tests need GoogleTest, which CMake fetches; build with -DBUILD_TESTS=ON.
if(BUILD_TESTS)
  include(FetchContent)
  FetchContent_Declare(
    googletest
    GIT_REPOSITORY https://github.com/google/googletest.git
    GIT_TAG        v1.17.0
  )
  FetchContent_MakeAvailable(googletest)

  enable_testing()
  add_executable(tests ${TEST_DIR}/tests.cpp)
  target_link_libraries(tests PRIVATE ${PROJECT_NAME} GTest::gtest_main)
  target_include_directories(tests PRIVATE ${INCLUDE_DIR})
  add_test(NAME tests COMMAND tests)
endif()
