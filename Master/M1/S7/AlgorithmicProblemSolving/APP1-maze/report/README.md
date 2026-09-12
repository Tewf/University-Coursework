# APP1 deliverable — LaTeX source

Random maze generation by recursive division, returning two structures, and a
way out of each: A* on the graph, a lowest-common-ancestor descent on the tree.
Seven pages.

## Building it

```bash
make          # -> main.pdf
make clean
```

`latexmk` and `pdflatex` come from the TinyTeX install; the packages beyond a
base TeX Live are `algorithm2e`, `import`, `pgfplots` and `tcolorbox`.

## Layout

`main.tex` is a skeleton and holds no prose: it sets the title and pulls in one
folder per section with `\subimport`, in reading order. A section folder holds
its `section.tex` and the figures only that section cites, so a figure is
`\input` by bare name from the file that uses it and moving a section moves its
pictures with it. Shared setup — packages, colours, TikZ styles, emphasis
macros — lives once in `preamble.tex`.

```
main.tex  preamble.tex  references.bib  Makefile
sections/01-problem/        the problem, as a graph problem, and the plan
         02-generation/     recursive division, filling the graph and the tree
         03-graph-astar/    A* on the graph output
         04-tree-lca/       lowest common ancestor on the tree output
         05-comparison/     both solvers measured side by side
         06-conclusion/
```

## Where the numbers come from

Every measurement is produced by [../implementation/](../implementation/) —
`make benchmark && ./benchmark 200` — and every claim it makes about
correctness by `make test`.

## Source material

The subject is by Nguyen Kim Thang and Enikő Kevi (UGA) and is **not
redistributed here**: see [NOTICE](../../../../../../NOTICE). It stays in
`../handout/`, outside version control.
