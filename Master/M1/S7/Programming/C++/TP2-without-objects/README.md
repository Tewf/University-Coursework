# C++ TP2: C++ without objects

A 2D vector written as free functions: parameters, references, const, operator overloading, file streams and exceptions.

## State

Not started. [steps/](steps/index.html) lists the steps this practical asks
for, ready to be filled in as the work happens.

## Steps

The handout's questions, abridged. The wording that counts is the handout's own.

| # | Asked |
|---|-------|
| 1 | Vector2D and initializes its fields x and y with the given values |
| 2 | Implement the function print_vector that prints a Vector2D to the standard output in the format (x, y) |
| 3 | Implement the function add that takes two Vector2D as parame- Programming |
| 4 | Implement the function add_to that takes two Vector2D as TP2 - C++ without objects E. Foussard to Vector2D as parameters (indicated by the & symbol) |
| 5 | Remove the & from the parameters of the add_to function and try to compile and run the tests |
| 6 | Add the keyword const to each parameter of each function you have implemented so far |
| 7 | Complete the implementation of the functions subtract, scale, and dot_product in the vector2D.cpp file |
| 8 | Overload the operators +, -, *, and == for the basic arithmetic int my_function(int a); float my_function(float a); int my_function(int a, int b); 1.3 Automatically generated documentation with Doxygen C++ also allows you to redefine most existing operators (such as +, -, *, &, ==, [], etc.) |
| 9 | Generate the documentation for your project using Doxygen |
| 10 | Write a function that takes a file name as input, reads the content of the file, and prints it to the standard output |
| 11 | Write a function that takes a file name and a string as input, and appends the string to the end of the file |
| 12 | Write a function that takes a file name as input, and counts the number of lines and words in the file |
| 13 | Write a function that takes a file name and a word (as a File streams in C++ In C++, file manipulation is done using streams from the <fstream> header |
| 14 | Modify the functions you have implemented so far to throw exceptions in case of errors (e.g., file not found, inaccessible file, etc.) instead of printing error messages to the standard error output |

## What the handout provides

Unpacked and set up in place, so this folder reads as a working project
rather than an archive next to a drop zone. The archive itself stays for
reference; the `provided-files/` wrapper it unpacked into does not.

From `provided-files.zip`:

- `CMakeLists.txt`
- `include`
- `src`
- `tests`

## Running it

```bash
cmake -S . -B build          # add -DBUILD_TESTS=ON for the tests
cmake --build build
./build/main
```

## Where the explanation lives

This folder holds code. The concept note for it is in the M1AI vault, under
`S7/Programming/TP - C++/TP2 - C++ Without Objects.md`. The map of all of them is
`obsidian-note.local.md` at the course root, which is gitignored because it
names local paths.

## Source material

The handout is by E. Foussard (UGA) and is **not redistributed here**: see
[NOTICE](../../../../../../NOTICE). It sits in `handout/`, the PDF beside the `.txt`
extraction that makes it greppable, and `.gitignore` keeps that whole directory
out of the repository. The code the handout provides is listed above and is
credited in NOTICE.
