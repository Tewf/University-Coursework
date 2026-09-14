# C++ TP1: First programs, CMake and tests

Compiling and running with CMake, the course's warning flags, Boost, and Google Test.

## State

Not started.

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

This folder holds code. The concept note for it is in the Notes vault, under
`S7/Programming/TP - C++/TP1 - First Programs, CMake and Tests.md`.

## Source material

The handout is by E. Foussard (UGA) and is **not redistributed here**: see
[NOTICE](../../../../../../NOTICE). It sits in `handout/`, the PDF beside the `.txt`
extraction that makes it greppable, and `.publishignore` keeps that whole directory
out of this copy. The code the handout provides is listed above and is
credited in NOTICE.
