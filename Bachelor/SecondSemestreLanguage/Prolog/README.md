# Prolog — Logic Programming

> [Lire en francais](README.fr.md)

**Course:** Logic Programming — Licence MIASHS, Universite Grenoble Alpes

An introduction to logic programming with Prolog. Instead of writing step-by-step instructions, you declare **facts** and **rules**, then ask questions — and the Prolog engine finds the answers.

## What You'll Learn

- Defining facts and rules to represent knowledge
- Querying relationships and performing logical reasoning
- Recursive definitions and backtracking mechanisms
- Unification and pattern matching
- Search and problem-solving with declarative logic

## Files

| File | Topic |
|------|-------|
| `TD5.pl`, `TD6.pl` | Directed exercises: facts, rules, queries |
| `TP.pl` | Basic predicates and relationships |
| `TP2.pl` | Recursive definitions |
| `TP3.pl` | List processing in Prolog |
| `TP5.pl` | Advanced backtracking |
| `TP6.pl` | Problem-solving with logic |

## Running the Code

Install [SWI-Prolog](https://www.swi-prolog.org/), then:

```sh
swipl -s TP.pl
```

Use queries at the `?-` prompt to test predicates. Each file includes comments with expected predicates and sample queries.

## Prerequisites

- No prior logic programming experience needed
- Helpful to understand basic propositional logic (AND, OR, implications)
