# Targets only. Compiler flags live in cmake/compiler-options.cmake, each
# optional dependency in its own cmake/*.cmake; cmake/README.md explains both.
cmake_minimum_required(VERSION 3.24)  # FetchContent's FIND_PACKAGE_ARGS
project(change_me LANGUAGES CXX)      # new-project.sh renames this

option(BUILD_TESTS "Build the Google Test executable from tests/" OFF)
option(BUILD_PYTHON_LIB "Build one pybind11 module per file in bindings/" OFF)
option(ENABLE_SANITIZERS "Compile with AddressSanitizer and UBSan" OFF)
option(WARN_EFFCXX "Add -Weffc++ to the warning set" OFF)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)  # build/<preset>/compile_commands.json for clangd
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

include(cmake/compiler-options.cmake)  # defines the project_warnings target
find_package(Threads REQUIRED)

# --- The library: every .cpp under src/, every header under include/ ---
# CONFIGURE_DEPENDS makes a build re-glob, so a file added to src/ is picked up
# without re-running the configure step by hand.
file(GLOB_RECURSE LIBRARY_SOURCES CONFIGURE_DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp")
if(LIBRARY_SOURCES)
  add_library(${PROJECT_NAME} STATIC ${LIBRARY_SOURCES})
  set(library_scope PUBLIC)
  target_link_libraries(${PROJECT_NAME} PRIVATE project_warnings)
  # Position-independent objects, so the same archive links into a Python .so
  set_target_properties(${PROJECT_NAME} PROPERTIES POSITION_INDEPENDENT_CODE ON)
else()
  add_library(${PROJECT_NAME} INTERFACE)  # header-only project: src/ is empty
  set(library_scope INTERFACE)
endif()
target_include_directories(${PROJECT_NAME} ${library_scope} "${CMAKE_CURRENT_SOURCE_DIR}/include")
target_link_libraries(${PROJECT_NAME} ${library_scope} Threads::Threads)

# --- Executables: one per .cpp in apps/, named after the file ---
file(GLOB APP_SOURCES CONFIGURE_DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/apps/*.cpp")
foreach(app_source IN LISTS APP_SOURCES)
  get_filename_component(app_name "${app_source}" NAME_WE)
  add_executable(${app_name} "${app_source}")
  target_link_libraries(${app_name} PRIVATE ${PROJECT_NAME} project_warnings)
endforeach()

if(BUILD_TESTS)
  include(cmake/googletest.cmake)
endif()
if(BUILD_PYTHON_LIB)
  include(cmake/pybind11.cmake)
endif()
