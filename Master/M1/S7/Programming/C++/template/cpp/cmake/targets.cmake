# The targets every project of this layout has: the library from src/ and
# include/, one executable per file in apps/. Included once by the root
# CMakeLists.txt after the options are declared.
#
# Usage:
#   a new .cpp in src/ or apps/ is found at the next build: nothing to edit.
#   a library the whole project uses (Boost, GMP, ...): the "External
#     dependencies" block at the end, PUBLIC so programs and tests get it too.
#   a library one program alone uses: target_link_libraries(<program> PRIVATE ...)
#     after the loop, guarded by if(TARGET <program>).
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)  # build/<preset>/compile_commands.json for clangd
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release)
endif()

include(${CMAKE_CURRENT_LIST_DIR}/compiler-options.cmake)  # defines project_warnings
find_package(Threads REQUIRED)

# --- The library: every .cpp under src/, every header under include/ ---
# The target is project_library, the archive lib<project>.a: a fixed target
# name lets an executable in apps/ carry the project's own name.
# CONFIGURE_DEPENDS makes a build re-glob, so a file added to src/ is picked up
# without re-running the configure step by hand.
file(GLOB_RECURSE LIBRARY_SOURCES CONFIGURE_DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp")
if(LIBRARY_SOURCES)
  add_library(project_library STATIC ${LIBRARY_SOURCES})
  set(library_scope PUBLIC)
  target_link_libraries(project_library PRIVATE project_warnings)
  # Position-independent objects, so the same archive links into a shared library
  set_target_properties(project_library PROPERTIES
    OUTPUT_NAME ${PROJECT_NAME} POSITION_INDEPENDENT_CODE ON)
else()
  add_library(project_library INTERFACE)  # header-only project: src/ is empty
  set(library_scope INTERFACE)
endif()
target_include_directories(project_library ${library_scope} "${CMAKE_CURRENT_SOURCE_DIR}/include")
target_link_libraries(project_library ${library_scope} Threads::Threads)

# --- Executables: one per .cpp in apps/, named after the file ---
file(GLOB APP_SOURCES CONFIGURE_DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/apps/*.cpp")
foreach(app_source IN LISTS APP_SOURCES)
  get_filename_component(app_name "${app_source}" NAME_WE)
  add_executable(${app_name} "${app_source}")
  target_link_libraries(${app_name} PRIVATE project_library project_warnings)
endforeach()

# --- External dependencies ---
# find_package locates a library installed on the system; the imported
# target it provides carries the include paths and the link line. Uncomment
# and adapt; the Boost pair is what TP1's calculator needs.
# find_package(Boost REQUIRED COMPONENTS program_options)
# target_link_libraries(project_library ${library_scope} Boost::program_options)
