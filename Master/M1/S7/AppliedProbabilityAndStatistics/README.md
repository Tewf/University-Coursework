# Applied Probability and Statistics

> [Lire en français](README.fr.md)

**Course:** Applied Probability and Statistics, M1 Artificial Intelligence, Semester 7, Université Grenoble Alpes (shared with the M1 Applied Mathematics)

Four practical sessions in R, from a first hour with the language to a
Gaussian-vector forecast of temperatures over France. Three come as R Markdown
notebooks to complete, one as a PDF alone; each has a folder here. The exercise
sheets, the short tests and the training exam are worked on paper and are not
here.

## The labs

| Folder | Problem | Solved with | Provided |
|---|---|---|---|
| [Lab0-first-manipulations-with-r/](Lab0-first-manipulations-with-r/) | An R warm-up: object classes, vectorised code instead of loops, first random draws | base R, `sample()`, `runif()` | `.Rmd`, `saison_2022.csv`, `BreastCancer.csv` |
| [Lab1-real-random-variables/](Lab1-real-random-variables/) | Distribution functions, densities, medians and the inversion method, by hand then by simulation | `rexp`, `runif`, `ecdf`, `curve` | `.Rmd` |
| [Lab2-estimators-exponential-model/](Lab2-estimators-exponential-model/) | The law of large numbers and the central limit theorem by simulation, then estimators in the exponential model | simulation, method of moments, likelihood | PDF |
| [Lab3-kriging/](Lab3-kriging/) | Simulate a Gaussian vector from a square root of its covariance, then forecast temperatures over France by kriging | Gaussian vectors, conditioning | PDF, `.Rmd`, official `Lab-Solutions.r`, three `.Rdata` |

Two things to know before opening one:

- **Lab 0's `BreastCancer.csv` is read by no code.** The notebook takes that
  dataset from the `mlbench` package. The file shipped with the lab anyway and
  is kept beside it for that reason alone.
- **`Lab-Solutions.r` runs from the lab root.** It `load()`s the three `.Rdata`
  files by bare name, so run it from `Lab3-kriging/`, not from `handout/`.

## Setting up

One conda environment, declared in [environment.yml](environment.yml):

```bash
conda env create -f environment.yml
conda activate m1ai-applied-stats
```

Start a lab by copying its notebook out of `handout/` and knitting the copy:

```bash
cd Lab3-kriging
cp handout/Lab3-kriging.Rmd .
Rscript -e 'rmarkdown::render("Lab3-kriging.Rmd")'
```

That copy is the file that gets committed. The one in `handout/` never changes.

## Folder Structure

Each lab keeps what the staff handed out in `handout/` (the `.Rmd` or PDF
subject, a `.txt` extraction of any PDF so it greps, and the official solution
when one exists). Datasets sit at the lab root, where the code `load()`s them.
`.gitignore` excludes all of it, so what a folder shows on GitHub is the
completed notebook and nothing else, and a lab not started yet shows nothing.

```
AppliedProbabilityAndStatistics/
|-- environment.yml              <- the one conda environment
|-- Lab0-first-manipulations-with-r/
|   |-- handout/                 <- the .Rmd subject
|   |-- saison_2022.csv BreastCancer.csv
|-- Lab1-real-random-variables/
|-- Lab2-estimators-exponential-model/
|   |-- handout/                 <- the PDF subject and its .txt
|-- Lab3-kriging/
|   |-- handout/                 <- PDF + .txt, the .Rmd, Lab-Solutions.r
|   |-- data_temperatures.Rdata frontieres_france.Rdata grille_france.Rdata
```

## Where the explanations live

Not here. The concepts each lab needs — probability spaces, real random
variables, simulation of random variables, random vectors and conditional
expectation, parameter estimation, the law of large numbers and the central
limit theorem — are written up in a separate Obsidian vault, one note per
concept, alongside the lecture slides they come from, the exercise sheets, the
tests and the textbooks. Each lab there maps its questions to the concepts they
need. A comment here that starts teaching theory belongs in that note instead.

## Source material

The subjects, the official solution and the datasets are **not redistributed
here**: see [NOTICE](../../../../NOTICE). They stay on disk in each lab folder
and `.gitignore` keeps them out of the repository. What is committed is the
work written against them.
