# Python TP1: Environments and packages

Virtual environments with venv and pip, then uv, then notebooks running against each. Built around a weather API.

## State

Not started. [steps/](steps/index.html) lists the steps this practical asks
for, ready to be filled in as the work happens.

## Steps

The handout's questions, abridged. The wording that counts is the handout's own.

| # | Asked |
|---|-------|
| 1 | Run the file meteo.py and observe the output |
| 2 | Implement the function plot_temperature that takes as input the JSON response from the API and plots the temperature data using matplotlib |
| 3 | Generate the requirements file for your virtual environment |
| 4 | Create a new directory for the weather map application, and initialize a new uv environment in it by running the following command: |
| 5 | Go to https://open-meteo.com/en/docs and generate the API pip install -r requirements.txt location |
| 6 | Using tkinter canvas, create a simple GUI that displays a map of a region of your choice (e.g., France, Europe, etc.) and displays the weather data for multiple locations on the map |
| 7 | Create a new Jupyter Notebook in your uv environment and For more details on using Jupyter with uv, refer to the official documentation: |
| 8 | Create a new Jupyter Notebook in your venv environment and verify that you can import the installed packages (e.g., requests) |

## What the handout provides

Unpacked and set up in place, so this folder reads as a working project
rather than an archive next to a drop zone. The archive itself stays for
reference; the `provided-files/` wrapper it unpacked into does not.

From `provided-files.zip`:

- `meteo.py`

## Running it

```bash
conda activate m1ai-programming
```

## Where the explanation lives

This folder holds code. The concept note for it is in the M1AI vault, under
`S7/Programming/TP - Python/TP1 - Environments and Packages.md`. The map of all of them is
`obsidian-note.local.md` at the course root, which is gitignored because it
names local paths.

## Source material

The handout is by E. Foussard (UGA) and is **not redistributed here**: see
[NOTICE](../../../../../../NOTICE). It sits in `handout/`, the PDF beside the `.txt`
extraction that makes it greppable, and `.gitignore` keeps that whole directory
out of the repository. The code the handout provides is listed above and is
credited in NOTICE.
