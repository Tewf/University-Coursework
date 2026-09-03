# A minimal CMake file must contain these three commands

# States the minimum version of cmake required to compile your project
# Here, we say that we need at least cmake 3.5 to compile this project
cmake_minimum_required(VERSION 3.5)

# Define the name of the project
project(my-first-cpp-project)

# Create an executable named hello-world 
add_executable(hello-world hello-world.cpp) 

