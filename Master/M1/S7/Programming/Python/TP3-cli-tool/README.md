# Python TP3: A command-line duplicate finder

A click command-line tool: walking a directory, hashing files, handling duplicates and corrupt images, resizing, and reporting.

## State

Not started. [steps/](steps/index.html) lists the steps this practical asks
for, ready to be filled in as the work happens.

## Steps

The handout's questions, abridged. The wording that counts is the handout's own.

| # | Asked |
|---|-------|
| 1 | Using the click library, create a CLI tool whose help message to process the images and organize them into the target directory |
| 2 | Create a function that finds all .jpg files in a folder and its J. Perier-Camby, E. Foussard in the os and os.path libraries |
| 3 | Create a function that detects all duplicate files in a list of file paths, and organizes them into groups with a dictionnary |
| 4 | Modify your main program to produce the following output: |
| 5 | Create a function that checks if an image file is corrupted |
| 6 | Create a function that verifies if the target directory exists, and creates it if it does not |
| 7 | Options: and non-corrupted images to the target directory, with a clean file name -H, --height INTEGER Target image height. e.g |
| 8 | Modify your main program to resize all images to the target size (height and width) specified in the command line arguments |
| 9 | Add a progress bar to your main program, to show the progress of the image processing |
| 10 | To finalize your program, create a json file in the target di- rectory, containing the correspondance between original file paths and new file paths |

## Running it

```bash
conda activate m1ai-programming
```

## Where the explanation lives

This folder holds code. The concept note for it is in the M1AI vault, under
`S7/Programming/TP - Python/TP3 - Command-Line Duplicate Finder.md`. The map of all of them is
`obsidian-note.local.md` at the course root, which is gitignored because it
names local paths.

## Source material

The handout is by E. Foussard and J. Perier-Camby (UGA) and is **not redistributed here**: see
[NOTICE](../../../../../../NOTICE). It sits in `handout/`, the PDF beside the `.txt`
extraction that makes it greppable, and `.gitignore` keeps that whole directory
out of the repository. The code the handout provides is listed above and is
credited in NOTICE.
