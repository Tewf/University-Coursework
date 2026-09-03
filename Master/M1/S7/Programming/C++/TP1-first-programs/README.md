# C++ TP1: First programs, CMake and tests

Compiling and running with CMake, the course's warning flags, Boost, and Google Test.

## State

Not started. [steps/](steps/index.html) lists the steps this practical asks
for, ready to be filled in as the work happens.

## Steps

The handout's questions, abridged. The wording that counts is the handout's own.

| # | Asked |
|---|-------|
| 1 | What are the main similarities and differences you notice between Programming TP1 - Your first C++ programs You may have noticed that the syntax of the printing function std::cout E. Foussard quences of bytes, better known as streams |
| 2 | Complete the provided skeleton code in compute-circle.cpp, by using π = 3.14, then compile and run your program using CMake |
| 3 | Modify your program accordingly, then compile and run it again |
| 4 | skeleton code provided in the file circle.cpp |
| 5 | Complete the implementation of the gcd in utils.cpp according to their declarations in utils.hpp |
| 6 | Create a new file compute-lcm.cpp in the src folder that will • -Weffc++ : |
| 7 | Add new test cases to verify the correctness of your gcd and lcm functions |
| 8 | Modify the CMakeLists.txt file to create a new executable tions in utils.cpp |
| 9 | Add your lcm function to the calculator program |

## What the handout provides

Unpacked and set up in place, so this folder reads as a working project
rather than an archive next to a drop zone. The archive itself stays for
reference; the `provided-files/` wrapper it unpacked into does not.

From `provided-files.zip`:

- `calculator`
- `compute-circle`
- `hello-world`
- `other-files`

## Running it

```bash
cmake -S . -B build          # add -DBUILD_TESTS=ON for the tests
cmake --build build
./build/main
```

## Where the explanation lives

This folder holds code. The concept note for it is in the M1AI vault, under
`S7/Programming/TP - C++/TP1 - First Programs, CMake and Tests.md`. The map of all of them is
`obsidian-note.local.md` at the course root, which is gitignored because it
names local paths.

## Source material

The handout is by E. Foussard (UGA) and is **not redistributed here**: see
[NOTICE](../../../../../../NOTICE). It sits in `handout/`, the PDF beside the `.txt`
extraction that makes it greppable, and `.gitignore` keeps that whole directory
out of the repository. The code the handout provides is listed above and is
credited in NOTICE.
