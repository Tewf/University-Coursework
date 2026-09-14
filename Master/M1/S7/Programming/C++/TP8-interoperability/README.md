# C++ TP8: Binding C++ to Python

pybind11: exposing constants, functions, a class with operator overloads, and an iterator.

## State

Not started. Each question's reasoning, what was rejected and the reference
that settled it are in [steps/](steps/index.html), where the abridged
questions are listed too.

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

This folder holds code. The concept note for it is in the Notes vault, under
`S7/Programming/TP - C++/TP8 - Binding C++ to Python.md`. The map of all of them is
`obsidian-note.local.md` at the course root, which is gitignored because it
names local paths.

## Source material

The handout is by E. Foussard (UGA) and is **not redistributed here**: see
[NOTICE](../../../../../../NOTICE). It sits in `handout/`, the PDF beside the `.txt`
extraction that makes it greppable, and `.publishignore` keeps that whole directory
out of the public repository. The code the handout provides is listed above and is
credited in NOTICE.
