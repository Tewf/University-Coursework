# Object‑Oriented Programming Exercises

This directory contains coursework for my object‑oriented programming course. The assignments are organised in the `TD` and `TM` subdirectories.

## Structure

- `TD` – Travaux Dirigés (directed exercises) that introduced basic OOP concepts such as classes, inheritance, interfaces, generics, exceptions, and file I/O.
- `TM` – Travaux Mise en pratique / mini‑projects that allowed me to apply OOP principles to more substantial problems.

## Running the exercises

Each subdirectory follows a simple structure with `src` for source files and `bin` for compiled classes. You can compile exercises using `javac`:

```sh
javac -d bin $(find src -name '*.java')
```

Run individual classes using `java -cp bin package.ClassName`. Some exercises include unit tests; run them with `java -cp ...` or a testing framework.

## What I learned

These exercises deepened my understanding of Java and object‑oriented thinking. They complement my AI project by reinforcing design patterns and modular programming.
