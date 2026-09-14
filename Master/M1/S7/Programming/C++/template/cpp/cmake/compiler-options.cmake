# One INTERFACE target carries every flag the project's own code compiles with.
# A target opts in by linking project_warnings PRIVATE. Fetched dependencies
# never link it, so a new compiler's warnings inside googletest or pybind11
# cannot stop the build under -Werror. Debug (-g) and Release (-O3 -DNDEBUG)
# flags are CMake's defaults and are not set here.
#
# Usage:
#   another warning for every build: append it to the first target_compile_options.
#   a flag for one configuration only: a generator expression,
#     e.g. $<$<CONFIG:Debug>:-Og>, in the same call.
#   silence one warning while a stub is unfinished: -Wno-<warning> here, and
#     take it out again; the course's grade assumes the four flags below.
add_library(project_warnings INTERFACE)

if(CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang")
  # The course's set: every warning, and every warning is an error.
  target_compile_options(project_warnings INTERFACE -Wall -Wextra -Wpedantic -Werror)
  if(WARN_EFFCXX)
    target_compile_options(project_warnings INTERFACE -Weffc++)
  endif()
  if(ENABLE_SANITIZERS)
    # Not compatible with Valgrind: run one or the other on a given build.
    target_compile_options(project_warnings INTERFACE
      -fsanitize=address,undefined -fno-omit-frame-pointer)
    target_link_options(project_warnings INTERFACE -fsanitize=address,undefined)
  endif()
elseif(MSVC)
  target_compile_options(project_warnings INTERFACE /W4 /WX)
endif()
