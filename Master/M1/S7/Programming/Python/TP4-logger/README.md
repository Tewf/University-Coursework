# Python TP4: Logging, then a logger of your own

The standard logging module, then a logger class of your own: levels, file output, decorators, a static class and a singleton.

## State

Not started. [steps/](steps/index.html) lists the steps this practical asks
for, ready to be filled in as the work happens.

## Steps

The handout's questions, abridged. The wording that counts is the handout's own.

| # | Asked |
|---|-------|
| 1 | Open your previous TP code (TP3) on the CLI tool, and add logging statements to track the execution of the program in the console |
| 2 | Configure the logger to write log messages to a file instead of the console |
| 3 | Create a new Python project for your logger library |
| 4 | Let’s enhance our logger by adding log levels: |
| 5 | Let’s now redefine the specific log level methods (debug, info, warning, error, critical) to use the generic log method internally |
| 6 | Finally, add the ability to log messages to a file instead of the Implementing our own logger specified files if a file path is set, otherwise log to the console |
| 7 | Test your logger class on the CLI tool from TP3, replacing the built-in logging module with your own logger |
| 8 | Implement a decorator method that logs the function name and its arguments each time a decorated function is called |
| 9 | (Optional) For the more advanced: |
| 10 | Create a new static class StaticLogger and move all the features of the logger in this new class |
| 11 | Implement the singleton pattern for your logger class, ensuring that only one instance of the logger can be created |

## Running it

```bash
conda activate m1ai-programming
```

## Where the explanation lives

This folder holds code. The concept note for it is in the M1AI vault, under
`S7/Programming/TP - Python/TP4 - Logging.md`. The map of all of them is
`obsidian-note.local.md` at the course root, which is gitignored because it
names local paths.

## Source material

The handout is by E. Foussard (UGA) and is **not redistributed here**: see
[NOTICE](../../../../../../NOTICE). It sits in `handout/`, the PDF beside the `.txt`
extraction that makes it greppable, and `.gitignore` keeps that whole directory
out of the repository. The code the handout provides is listed above and is
credited in NOTICE.
