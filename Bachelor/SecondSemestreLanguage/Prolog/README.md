# Prolog: Logic Programming

> [Lire en francais](README.fr.md) · [Open on the site ↗](https://tewf.github.io/University-Coursework/Bachelor/SecondSemestreLanguage/Prolog/)

**Course:** Logic Programming, Licence MIASHS, Universite Grenoble Alpes

An introduction to logic programming with Prolog. Instead of writing step-by-step instructions, you declare **facts** and **rules**, then ask questions, and the Prolog engine finds the answers.

## The project

**[Strategy tournament](StrategyTournament/)**. Two strategies derived on paper, written as Prolog agents, and entered against thirteen other students'. They finished **7th and 8th of 16**, and reading the 636-page log match by match shows the ranking measuring something other than winning: the champion won 6 of its 15 matches, the agent that won 13 finished 14th, and both entrants beat the champion head to head.

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
