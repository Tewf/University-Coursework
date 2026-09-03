# C++ TP3: The same vector, now a class

The same vector as a class: attributes, constructors, destructor, copy semantics, resizing and smart pointers.

## State

Not started. [steps/](steps/index.html) lists the steps this practical asks
for, ready to be filled in as the work happens.

## Steps

The handout's questions, abridged. The wording that counts is the handout's own.

| # | Asked |
|---|-------|
| 1 | Create a new C++ project |
| 2 | Create the class Vector with the following private attributes: |
| 3 | Implement the default constructor for the class Vector |
| 4 | Create two public methods that allow to access the elements of the array |
| 5 | (Optional) Overload the subscription operator [] to support the int value = myVector[k]; // get the k-th element // default constructor myVector[k] = value; // set the k-th element // parameterized constructor To do this, the operator must return a reference to the element in the vector |
| 6 | Create a method size that returns the size of the vector |
| 7 | Write a small main program that creates a vector with 10 elements Attributes in the initializer list should be initialized in the |
| 8 | Implement the destructor ∼Vector for your vector class |
| 9 | Create a copy of your implementation of the vector and modify it to use std::unique_ptr instead of raw pointers |
| 10 | Implement a private method resize function that moves the array to a new array of twice the size |
| 11 | Implement the following methods that respectively add an operations would be invalid |
| 12 | Implement methods that allow to insert or remove an element at any position in the vector |
| 13 | In your main program, call the default copy constructor of At this point, our Vector class is basically a wrapper that encapsulates a C array |
| 14 | Override the default copy constructor to fix the issue |

## Running it

```bash
cmake -S . -B build          # add -DBUILD_TESTS=ON for the tests
cmake --build build
./build/main
```

## Where the explanation lives

This folder holds code. The concept note for it is in the M1AI vault, under
`S7/Programming/TP - C++/TP3 - Custom Vector Class.md`. The map of all of them is
`obsidian-note.local.md` at the course root, which is gitignored because it
names local paths.

## Source material

The handout is by E. Foussard (UGA) and is **not redistributed here**: see
[NOTICE](../../../../../../NOTICE). It sits in `handout/`, the PDF beside the `.txt`
extraction that makes it greppable, and `.gitignore` keeps that whole directory
out of the repository. The code the handout provides is listed above and is
credited in NOTICE.
