cmake_minimum_required(VERSION 3.5)
project(compute-circle)

# Specify C++ version (uncomment these two lines)
# set(CMAKE_CXX_STANDARD 20)
# set(CMAKE_CXX_STANDARD_REQUIRED True)

# Set release mode by default
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

# Set compiler flags for debug and release mode
set(CMAKE_CXX_FLAGS_DEBUG "-g")
set(CMAKE_CXX_FLAGS_RELEASE "-O3")

# Add extra warnings, turn warnings into error
set(CMAKE_CXX_FLAGS "-Wall -Weffc++ -Wextra -Wpedantic -Werror")

add_executable(compute-circle compute-circle.cpp) 



