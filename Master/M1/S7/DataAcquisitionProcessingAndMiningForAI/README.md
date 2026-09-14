# Data Acquisition, Processing and Mining for AI

> [Lire en français](README.fr.md)

**Course:** Data Acquisition, Processing and Mining for AI, M1 Artificial Intelligence, Semester 7, Université Grenoble Alpes

One pipeline, built twice. The weekly labs teach each stage on a dataset the
staff supply; the paired project then runs the same stages end to end on a live
API of our own choosing — pull the data, clean it, and finish on a mining result
somebody can read.

## The labs

| Folder | Problem | Solved with | Provided |
|---|---|---|---|
| [Lab1-pandas-taxi-data/](Lab1-pandas-taxi-data/) | 200 000 New York taxi trips: load the Parquet, mask out the impossible rows, derive duration and pickup hour, group and plot | pandas, NumPy, matplotlib | subject notebook, the Parquet sample |

Later weeks are added as they are taught.

## The project

Done in a fixed pair, marked out of 20, and described in `Project/handout/`. Four
Moodle submissions carry it:

| Milestone | Due | Holds |
|---|---|---|
| M0 | before the week 3 lab | the pair, the chosen source, and the slice of it we commit to |
| M1 | before the week 4 lab | a log of what was pulled, the code that pulled it, and the dimensions every Parquet file came out at |
| M2 | before the week 6 lab | the one-page data card and the exploratory notebook |
| M3 | defended in the week 8 lab, files a week later | the pipeline notebook, a 3–5 page report, the final data card |

Eight sources are on offer — Crossref, GitHub, Hacker News, Open-Meteo, TMDB,
MediaWiki, data.gouv.fr and Twitch. Four constraints hold whichever one is
picked: query the API rather than scrape it, keep bulk pulls out of class hours,
read every credential from the environment instead of a notebook cell, and say
in the report what personal data was collected and what was dropped.

**No collected data is committed here.** The raw Parquet stays on disk; what the
repository carries is the code that produced it and the writing about it.

## Setting up

The course ships one conda environment, `datacq`, pinned in an `environment.yml`
that comes in the Moodle setup bundle. It is the staff's file and is not
redistributed here (see [NOTICE](../../../../NOTICE)); it sits in
`Setup/handout/` with the rest of the pre-course bundle, and it pins Python 3.12
with pandas, NumPy, DuckDB, pyarrow, requests, BeautifulSoup, matplotlib,
seaborn, scikit-learn, mlxtend and Jupyter.

```bash
conda env create -f Setup/handout/environment.yml
conda activate datacq
python Setup/handout/verify_setup.py   # prints SETUP OK when every import resolves
```

## Folder structure

Every unit keeps its own `handout/`: whatever the staff shipped for that piece
of work sits beside the work itself, rather than in one pile at the course root.
`.publishignore` withholds all of them, so what a folder shows is my work — a README
saying what it asks in my own words, and the completed notebook once there is one.

```
DataAcquisitionProcessingAndMiningForAI/
|-- Setup/
|   |-- handout/               <- setup guide, environment.yml, verify_setup.py
|-- Lab1-pandas-taxi-data/
|   |-- handout/               <- the subject notebook, the bundle as downloaded
|   |-- data/raw/              <- the Parquet sample the notebook reads
|   |-- README.md steps.json steps/
|-- Project/
|   |-- handout/               <- the project handout, the data card template
|   |-- README.md
```

## Where the explanations live

Not here. Parquet and columnar storage, API pagination and rate limits, tidy
data, the cleaning decisions worth recording, association rules and clustering —
each is a note in a separate Obsidian vault, beside the slides it comes from. A
comment here that starts teaching theory belongs in that note instead.

## Source material

The project handout, the data card template, the setup guide, `environment.yml`,
`verify_setup.py`, the lab notebooks and the datasets they read are **not
redistributed here**: see [NOTICE](../../../../NOTICE). Each stays on disk in
the `handout/` of the unit it belongs to, and `.publishignore` keeps every one of
those out of the public repository. What is committed is written against them.
