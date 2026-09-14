# cmake/

One file per concern, included by the root `CMakeLists.txt`:

| File | Role | Included |
|---|---|---|
| `targets.cmake` | the standard, the build type, the library from `src/` and one executable per file in `apps/` | always |
| `compiler-options.cmake` | the `project_warnings` target: the warning set, `-Weffc++` and the sanitizers as options | always |
| `googletest.cmake` | the `tests` executable and its CTest registration | `BUILD_TESTS=ON` |
| `base-presets.json` | the `debug`, `asan` and `release` presets; the root `CMakePresets.json` only includes it, so a template laid over this one can add presets without a second copy | always |

## Options

| Option | Default | Effect |
|---|---|---|
| `CMAKE_BUILD_TYPE` | `Release` | `Debug` is `-g`, `Release` is `-O3 -DNDEBUG`: CMake's own defaults |
| `BUILD_TESTS` | `OFF`; every preset sets `ON` | builds `tests` and registers each `TEST()` with CTest |
| `ENABLE_SANITIZERS` | `OFF`; the `asan` preset sets `ON` | AddressSanitizer and UBSan on the project's own targets |
| `WARN_EFFCXX` | `OFF` | adds `-Weffc++`, the handout's fifth flag |

## Decisions, and the trail behind each

- **Flags on an INTERFACE target, not in `CMAKE_CXX_FLAGS`.** The course skeleton sets
  the flags globally, so fetched googletest compiles under `-Werror` too and a compiler
  upgrade can break the build inside code that is not ours. Linking `project_warnings`
  PRIVATE is the target-based form Modern CMake recommends (Craig Scott, *Professional
  CMake*, "Compiler and linker essentials"; cmake-init and cpp-best-practices do the same).
- **The warning set is the course's four flags.** `-Wall -Wextra -Wpedantic -Werror`, from
  TP1's handout (p. 3). `-Weffc++`, which the same page lists and the TP8 skeleton uses, is
  opt-in: the GCC manual itself notes that the standard headers do not follow all of its
  guidelines. Rejected: cpp-best-practices' longer list (`-Wshadow -Wconversion ...`),
  worth adding per project, not in a template that must build every handout's stub.
- **`file(GLOB ... CONFIGURE_DEPENDS)`.** The skeleton's plain `file(GLOB)` never sees a
  file added after configure (observed 2026-09-09, vault note *Makefile*, À revoir), which
  CMake's `file(GLOB)` documentation warns about and answers with a hand-written list.
  `CONFIGURE_DEPENDS` keeps the drop-a-file workflow the practicals rely on; it re-globs at
  every build with the Makefile and Ninja generators, the only two used here.
- **`apps/` for executables.** The skeleton removes `main.cpp` from the library by name and
  TP1 asks for a second executable, so each one means editing that list. A folder where every
  file is an executable needs no list. Same split as the Pitchfork Layout (vector-of-bool,
  *The Pitchfork Layout*, `src/` against `tests/` and top-level executables) and
  ModernCppStarter's `standalone/`.
- **Google Test: the system package first, then fetch.** The handout's `find_package(GTest)`
  (p. 4) and the skeleton's `FetchContent` of v1.17.0 are both right; `FIND_PACKAGE_ARGS`
  (CMake 3.24) does the first and falls back to the second. `gtest_discover_tests`, from
  CMake's `GoogleTest` module, replaces `add_test(NAME tests ...)` so CTest reports each test.
- **Presets over `.vscode/settings.json`.** The skeleton passes `-DBUILD_TESTS=ON
  -DCMAKE_EXPORT_COMPILE_COMMANDS=ON` through editor settings, gitignored here.
  `CMakePresets.json` (CMake 3.19) is read by the command line and by CMake Tools alike, and
  one build directory per preset means switching Debug and Release rebuilds nothing.
- **`-DNDEBUG` in Release.** The skeleton overrides `CMAKE_CXX_FLAGS_RELEASE` to `-O3` alone,
  which keeps `assert` active in Release; CMake's default is kept. A check that must survive
  Release is a thrown exception, as `mean` shows.
- **Baselines compared.** Pitchfork Layout; friendlyanon/cmake-init (2.5k stars);
  TheLartians/ModernCppStarter (5.4k); cpp-best-practices/cmake_template. All three carry CI,
  packaging and install rules a practical never needs; this stops at what the eight
  practicals and the project use.
