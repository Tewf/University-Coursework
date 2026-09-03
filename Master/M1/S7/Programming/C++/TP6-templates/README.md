# C++ TP6: Templates

Function templates, specialisation, class templates with non-type parameters, and variadic templates.

## State

Not started. [steps/](steps/index.html) lists the steps this practical asks
for, ready to be filled in as the work happens.

## Steps

The handout's questions, abridged. The wording that counts is the handout's own.

| # | Asked |
|---|-------|
| 1 | Create a new C++ project and copy the provided max imple- Programming int, float, char |
| 2 | Implement a generic function add<T> that returns the sum of the M1 AI, UGA It is possible to define a different implementation of a template func- tion for a specific type |
| 3 | Currently, our function add would fail for std::vector<int>, as size std::vector<int> |
| 4 | Implement a generic average<T> function that computes the arithmetic average of a vector |
| 5 | Implement a map<T> function that takes a function pointer and return y; a vector as a parameter, and applies the function to every element of a copy of } the vector |
| 6 | Implement a Pair<T1, T2> data structure, similar to std::pair, that wraps two elements of possibly different types which can accessed through the getters first and second |
| 7 | Import your previous implementation of custom integer vectors 1 In this first part of the TP, we will see and practice the basic use cases of the C++ templates |
| 8 | Define a class Matrix<Rows, Cols> that represents a matrix with a 2D float array of size Rows × Cols |
| 9 | Implement a variadic max function, that takes any number of pa- Templates wizardry (optional) type Start with a version for integers, then generalize it to any type |
| 10 | Implement a variadic print function, similar to print in Python |

## Running it

```bash
cmake -S . -B build          # add -DBUILD_TESTS=ON for the tests
cmake --build build
./build/main
```

## Where the explanation lives

This folder holds code. The concept note for it is in the M1AI vault, under
`S7/Programming/TP - C++/TP6 - Templates.md`. The map of all of them is
`obsidian-note.local.md` at the course root, which is gitignored because it
names local paths.

## Source material

The handout is by E. Foussard (UGA) and is **not redistributed here**: see
[NOTICE](../../../../../../NOTICE). It sits in `handout/`, the PDF beside the `.txt`
extraction that makes it greppable, and `.gitignore` keeps that whole directory
out of the repository. The code the handout provides is listed above and is
credited in NOTICE.
