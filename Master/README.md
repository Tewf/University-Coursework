# Master: Artificial Intelligence

> [Lire en français](README.fr.md) · [Open on the site ↗](https://tewf.github.io/University-Coursework/Master/)

[Master of Artificial Intelligence](https://m-ai.imag.fr/), Université Grenoble
Alpes, jointly delivered by UFR IM²AG and Ensimag (Grenoble INP).

M1 is under way and [`M1/`](M1/README.md) fills as the coursework is produced. The Licence
work is under [`Bachelor/`](../Bachelor/README.md).

## Where things are

Semester by semester, mirroring the Licence layout:

| Year | Semester | Course | Folder |
|------|----------|--------|--------|
| M1 | S7 | Programming — Python, C++, pybind11, a TSP solver | [M1/S7/Programming/](M1/S7/Programming/README.md) |

The full M1 curriculum is in [`M1/README.md`](M1/README.md).

## Working here

Each course declares its own dependencies rather than sharing one environment,
so a course can be picked up years later without resolving against the others.
For the Programming course:

```bash
conda env create -f M1/S7/Programming/environment.yml
conda activate m1ai-programming
```

## Handouts

TP subjects and provided code belong to their authors and are **not
redistributed** here; see [NOTICE](../NOTICE). They stay on disk beside each TP,
with a `.txt` extraction next to them so they can be searched, and `.gitignore`
keeps both out of the repository. What is committed is my own work.
