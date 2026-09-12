# APP1 deliverable — LaTeX source

Random maze generation by recursive division, and shortest-path search to the
exit: the APP1 deliverable, stated and solved as a graph problem.

## Building it

```bash
make          # -> main.pdf
make clean
```

`latexmk` and `pdflatex` come from the TinyTeX install; the packages beyond a
base TeX Live are `algorithm2e`, `import` and `pgfplots`.

## Layout

`main.tex` is a skeleton and holds no prose: it sets the title and pulls in one
folder per section with `\subimport`, in reading order. A section folder holds
its `section.tex` and the figures only that section cites, so a figure is
`\input` by bare name from the file that uses it and moving a section moves its
pictures with it. Shared setup — packages, colours, TikZ styles, notation
macros — lives once in `preamble.tex`; sections declare none of their own.

```
main.tex  preamble.tex  references.bib  Makefile
sections/01-problem-formulation/                  section.tex + 2 figures
         02-maze-generation-into-graph/           section.tex + 4 figures
         03-unit-edge-weights/
         04-shortest-path-with-distance-heuristic/
         05-cpp-implementation-and-testing/
         06-complexity-and-result-analysis/
region-tree-search/       a note of its own, its own Makefile and PDF
branching-point-tree/     likewise
```

## The notes beside it

Two standalone documents, each with its own `Makefile` and PDF. They are not
part of `main.pdf`: the report stands without them, and they follow a question
further than a deliverable should.

| Folder | Question it answers |
|---|---|
| [region-tree-search/](region-tree-search/) | Does the search have to touch every cell? No — the region tree locates the route in `Theta(n^0.68)` visits against Dijkstra's `Theta(n)`, and `O(log n)` memory against `Theta(n)`. |
| [branching-point-tree/](branching-point-tree/) | Can the tree be walked greedily by parent/child/sibling, choosing the nearest to the exit? No — that is greedy best-first and it stops at a local minimum 199 runs in 200. Navigating by address instead is optimal and `Theta(log n)`. |

Both borrow `preamble.tex`, so the three documents share one set of styles.

## State

All six sections are written, and the checklist at the end of Section 1 tracks
the specification's requirements against them. The measurements in Sections 5
and 6 come from [../implementation/](../implementation/).

## Source material

The subject is by Nguyen Kim Thang and Enikő Kevi (UGA) and is **not
redistributed here**: see [NOTICE](../../../../../../NOTICE). It stays in
`../handout/`, outside version control.
