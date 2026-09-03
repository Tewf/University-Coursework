# C++ TP7: Concurrent programming

Threads, shared state, mutexes, a producer-consumer buffer with condition variables, and atomics.

## State

Not started. [steps/](steps/index.html) lists the steps this practical asks
for, ready to be filled in as the work happens.

## Steps

The handout's questions, abridged. The wording that counts is the handout's own.

| # | Asked |
|---|-------|
| 1 | Create a new blank C++ project using CMake |
| 2 | Modifiy the provided code to create 10 threads that each print before the program exits |
| 3 | Run the program multiple times |
| 4 | Modify your C++ project to include a shared integer variable Threads Creation and Management In C++, threads can be created using the <thread> library |
| 5 | Modify your previous C++ project to include a mutex lock for the shared variable x |
| 6 | Download the provided Buffer class implementation and include it in your C++ project |
| 7 | Create a main function that initializes a Buffer object with a specified size (e.g., 5) |
| 8 | Modify the Buffer class to include a mutex and two condition variables: |
| 9 | Modify your C++ project to include a performance measurement for the incrementing of the shared variable x from the earlier exercise |
| 10 | Modify your C++ project to use an atomic variable for x instead previous measurements and analyze the performance benefits of |

## Running it

```bash
cmake -S . -B build          # add -DBUILD_TESTS=ON for the tests
cmake --build build
./build/main
```

## Where the explanation lives

This folder holds code. The concept note for it is in the M1AI vault, under
`S7/Programming/TP - C++/TP7 - Concurrency.md`. The map of all of them is
`obsidian-note.local.md` at the course root, which is gitignored because it
names local paths.

## Source material

The handout is by E. Foussard (UGA) and is **not redistributed here**: see
[NOTICE](../../../../../../NOTICE). It sits in `handout/`, the PDF beside the `.txt`
extraction that makes it greppable, and `.gitignore` keeps that whole directory
out of the repository. The code the handout provides is listed above and is
credited in NOTICE.
