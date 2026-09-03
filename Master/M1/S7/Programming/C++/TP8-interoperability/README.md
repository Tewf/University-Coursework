# C++ TP8: Binding C++ to Python

pybind11: exposing constants, functions, a class with operator overloads, and an iterator.

## State

Not started. [steps/](steps/index.html) lists the steps this practical asks
for, ready to be filled in as the work happens.

## Steps

The handout's questions, abridged. The wording that counts is the handout's own.

| # | Asked |
|---|-------|
| 1 | Open the file module.cpp and examine its contents |
| 2 | Compile the module. This will produce a shared library file named my_math.<extension>, where the extension depends on your |
| 3 | Complete the file module.cpp to expose any remaining constants and functions to the shared library |
| 4 | Open the file fractions.cpp and examine its contents |
| 5 | Complete the file fractions.cpp to add the missing constructors, methods and operator overloads to the module |
| 6 | Open the file CMakeLists.txt and have a look at its contents |
| 7 | Clone pybind11 into the active directory |
| 8 | Create a copy of your implementation of the subset iterator |
| 9 | Write the code to port the class Subset, and verify that you can successfully use it in your Python Shell |
| 10 | Copy the code below to implement the iterator on the elements |
| 11 | Implement SubsetIterator, test it in your Python shell |

## What the handout provides

Unpacked and set up in place, so this folder reads as a working project
rather than an archive next to a drop zone. The archive itself stays for
reference; the `provided-files/` wrapper it unpacked into does not.

From `provided-files.zip`:

- `fractions.cpp`
- `module.cpp`
- `pybind_cmake_project.zip`

## Running it

```bash
cmake -S . -B build          # add -DBUILD_TESTS=ON for the tests
cmake --build build
./build/main
```

## Where the explanation lives

This folder holds code. The concept note for it is in the M1AI vault, under
`S7/Programming/TP - C++/TP8 - Binding C++ to Python.md`. The map of all of them is
`obsidian-note.local.md` at the course root, which is gitignored because it
names local paths.

## Source material

The handout is by E. Foussard (UGA) and is **not redistributed here**: see
[NOTICE](../../../../../../NOTICE). It sits in `handout/`, the PDF beside the `.txt`
extraction that makes it greppable, and `.gitignore` keeps that whole directory
out of the repository. The code the handout provides is listed above and is
credited in NOTICE.
