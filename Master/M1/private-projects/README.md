# private-projects/

Two course projects are done with a partner in a private repository of their
own, where nothing is ignored, and are also published here, where the ignore
rules decide what is public. Rather than two copies, each project's folder in
this repository is the **work tree of both repositories at once**:

| In the folder | Repository | Ignore rules | Pushes to |
|---|---|---|---|
| `git ...` | this one | `.gitignore` here: an allowlist for the folder | `Tewf/University-Coursework`, public |
| `private-git NAME ...` | the project's own | none: handouts, data, everything | the private remote in `projects.tsv` |

The private repository's git directory lives in `.git/private/NAME.git` of this
clone, outside the tree, so this repository never sees it and it costs the
history nothing. `projects.tsv` is the only place a project is declared:
name, folder, remote.

## Once per clone

```bash
Master/M1/private-projects/private-git setup TSP
Master/M1/private-projects/private-git list
```

`setup` clones the private remote bare, points it at the folder, and leaves the
folder's files untouched: `private-git TSP status` then shows what differs
between the two sides. Put the script on your PATH, or alias it.

## Daily

```bash
private-git TSP pull                 # the partner's work lands in the folder
private-git TSP add -A && private-git TSP commit && private-git TSP push
git status                           # what of it the allowlist lets through
git add Master/M1/S7/Programming/Project-TSPSolver && git commit
```

Plain `git` inside the folder is always this repository; the private one is
never reached by accident, only by name.

## What the allowlist publishes

The folder is ignored wholesale, then named kinds are let back in: `README.md`,
`steps.json`, `steps/`, `src/`, `include/`, `tests/`, `notebooks/`,
`CMakeLists.txt`, `environment.yml`, `pyproject.toml`, and `.py` files at the
folder root. A partner's data file, report or handout stays private until a
rule names it. `handout/`, `data/` and `.dat` files are denied again inside the
allowed folders, so nothing the staff distributed can reach the public side
through them. Rules: the project blocks in `.gitignore` at the repository root.
