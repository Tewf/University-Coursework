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
main.tex  preamble.tex  Makefile
sections/01-problem-formulation/          section.tex + 2 figures
         02-maze-generation-into-graph/   section.tex + 3 figures
         03-unit-edge-weights/            \
         04-shortest-path-with-distance-heuristic/  > headings only, so far
         05-python-implementation-and-testing/       >
         06-complexity-and-result-analysis/         /
```

## State

Sections 1 and 2 are written. Sections 3 to 6 are headings with a comment
saying what belongs in them; the checklist at the end of Section 1 tracks the
specification's requirements against them.

## Source material

The subject is by Nguyen Kim Thang and Enikő Kevi (UGA) and is **not
redistributed here**: see [NOTICE](../../../../../../NOTICE). It stays in
`../handout/`, outside version control.
