# APP1 deliverable — LaTeX source

Random maze generation by recursive division, returning two structures, and a
way out of each: Dijkstra on the graph, a common-ancestor descent on the tree.

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
sections/01-problem-analysis-and-formulation/   the problem, as a graph problem
         02-maze-generation-two-outputs/        the generator, and both outputs
         03-dijkstra-on-the-graph/              solving the first output
         04-common-ancestor-on-the-tree/        solving the second output
         05-c-implementation/                   what was built and checked
         06-time-analysis-and-comparison/       costs, measurements, literature
```

## Where the numbers come from

Every measurement is produced by [../implementation/](../implementation/) —
`make benchmark && ./benchmark 200` — and every claim it makes about
correctness by `make test`.

## Source material

The subject is by Nguyen Kim Thang and Enikő Kevi (UGA) and is **not
redistributed here**: see [NOTICE](../../../../../../NOTICE). It stays in
`../handout/`, outside version control.
