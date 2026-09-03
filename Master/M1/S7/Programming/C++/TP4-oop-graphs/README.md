# C++ TP4: Object-oriented programming and graphs

A graph library: abstract base classes, inheritance, weighted and complete graphs, multiple inheritance, and path finding.

## State

Not started. [steps/](steps/index.html) lists the steps this practical asks
for, ready to be filled in as the work happens.

## Steps

The handout's questions, abridged. The wording that counts is the handout's own.

| # | Asked |
|---|-------|
| 1 | List the shared and differing properties and behaviors of graphs E. Foussard sign of your graph library, and how you would structure the classes and their relationships |
| 2 | Implement a class AdjacenceMatrixGraph that represents a graph using an adjacence matrix |
| 3 | Write a small program that creates an instance of user |
| 4 | What features of AdjacenceMatrixGraph are common to all graph representations? How would you design a base class Graph that defines Inheritance and abstract classes in C++ as a distinct construct |
| 5 | Implement the base class Graph as an abstract class in C++ |
| 6 | Design an abstract base class WeightedGraph that inherits from the Graph class and adds methods for handling weighted edges |
| 7 | Implement a class AdjacenceMatrixWeightedGraph that inherits from WeightedGraph and represents a weighted graph using an adjacence matrix |
| 8 | AdjacenceMatrixWeightedGraph representing a small tram network, and tests the methods implemented in the class |
| 9 | Define an abstract base class CompleteGraph that inherits from the Graph class and adds methods specific to complete graphs |
| 10 | Implement a class CoordinatesGraph that inherits from both Multiple inheritance and the diamond problem in C++ allows multiple inheritance, meaning that a class can inherit from more than one base class |
| 11 | Mark the inheritance from the Graph class as virtual in both |
| 12 | CoordinatesGraph representing a small geographic map, and tests the meth- ods implemented in the class |
| 13 | Modify the CoordinatesGraph class to allow for different distance metrics (e.g., Manhattan distance) in addition to the Euclidean dis- CoordinatesGraph class upon instantiation using function pointers |
| 14 | Implement a method std::vector<size_t> find_path(size_t class FinalDerived : |
| 15 | Implement a method that returns the total weight of a path derived classes |
| 16 | Use the find_path method to find a path between two nodes in the WeightedGraph and CompleteGraph classes |

## Running it

```bash
cmake -S . -B build          # add -DBUILD_TESTS=ON for the tests
cmake --build build
./build/main
```

## Where the explanation lives

This folder holds code. The concept note for it is in the M1AI vault, under
`S7/Programming/TP - C++/TP4 - OOP and Graphs.md`. The map of all of them is
`obsidian-note.local.md` at the course root, which is gitignored because it
names local paths.

## Source material

The handout is by E. Foussard (UGA) and is **not redistributed here**: see
[NOTICE](../../../../../../NOTICE). It sits in `handout/`, the PDF beside the `.txt`
extraction that makes it greppable, and `.gitignore` keeps that whole directory
out of the repository. The code the handout provides is listed above and is
credited in NOTICE.
