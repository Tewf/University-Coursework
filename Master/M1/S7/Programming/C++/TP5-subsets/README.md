# C++ TP5: Subsets and iterators

A Subset class and its iterators, written to the STL's iterator contract.

## State

Not started. [steps/](steps/index.html) lists the steps this practical asks
for, ready to be filled in as the work happens.

## Steps

The handout's questions, abridged. The wording that counts is the handout's own.

| # | Asked |
|---|-------|
| 1 | Set up a new C++ project |
| 2 | Create the constructor Subset(size_t k, size_t n), which create the subset S ′ = {0..k} of the set S = {0..n} |
| 3 | Overload the « operator to print your subset |
| 4 | Implement the following methods: |
| 5 | Overload your methods to handle subsets as parameters: |
| 6 | Create the class ElementsIterator inside the namespace subset |
| 7 | Implement the methods begin() and end() in the Subset class |
| 8 | Overload the * operator in the ElementsIterator class to return the current element of the subset |
| 9 | Overload the ++ operator in the ElementsIterator class to move to the next element of the subset |
| 10 | Overload the != operator in the ElementsIterator class to compare two iterators |
| 11 | Create the class SubsetIterator inside the namespace subset |
| 12 | Implement the ++ operator in the SubsetIterator class using 3 Iterating on all subsets of fixed size Your SubsetIterator class should now be fully functional |
| 13 | Add the required type definitions to your SubsetIterator class to make it STL-compatible |
| 14 | Implement any missing methods in your SubsetIterator class to make it STL-compatible |

## Running it

```bash
cmake -S . -B build          # add -DBUILD_TESTS=ON for the tests
cmake --build build
./build/main
```

## Where the explanation lives

This folder holds code. The concept note for it is in the M1AI vault, under
`S7/Programming/TP - C++/TP5 - Subsets and Iterators.md`. The map of all of them is
`obsidian-note.local.md` at the course root, which is gitignored because it
names local paths.

## Source material

The handout is by E. Foussard (UGA) and is **not redistributed here**: see
[NOTICE](../../../../../../NOTICE). It sits in `handout/`, the PDF beside the `.txt`
extraction that makes it greppable, and `.gitignore` keeps that whole directory
out of the repository. The code the handout provides is listed above and is
credited in NOTICE.
