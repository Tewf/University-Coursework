# The targets every project of this layout has: a library from src/ and
# include/, and one executable per file in apps/. Included once by the root
# CMakeLists.txt after the options are declared.
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
# CONFIGURE_DEPENDS makes a build re-glob, so a file added to src/ is picked up
# without re-running the configure step by hand.
file(GLOB_RECURSE LIBRARY_SOURCES CONFIGURE_DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/src/*.cpp")
if(LIBRARY_SOURCES)
  add_library(${PROJECT_NAME} STATIC ${LIBRARY_SOURCES})
  set(library_scope PUBLIC)
  target_link_libraries(${PROJECT_NAME} PRIVATE project_warnings)
  # Position-independent objects, so the same archive links into a shared library
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
