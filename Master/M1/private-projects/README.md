# private-projects/

Some of this work tree belongs in a private repository as well as in this
public one. Rather than keeping two copies, a folder here is the **work tree of
two repositories at once**: plain `git` is this repository, `private-git NAME`
is the private one, and `projects.tsv` is the only place a pairing is declared
— name, folder, remote.

| NAME | Folder | Private repository | What it is for |
|---|---|---|---|
| `Vault` | `.`, the whole tree | `Tewf/University-Coursework-private` | keeping what NOTICE removed: subjects, polycopiés, provided code, datasets, the exam folders and the courses left unpublished |
| `TSP` | the TSP project | `Tewf/TSP` | sharing the project with a partner, who sees all of it |
| `ProjetDatamining` | the data-mining project | `Tewf/ProjetDatamining` | the same, with the other partner |

The private git directory lives in `.git/private/NAME.git` of this clone,
outside the tree, so this repository never sees it and it costs the history
nothing.

## Once per clone

```bash
Master/M1/private-projects/private-git setup Vault
Master/M1/private-projects/private-git list
```

`setup` clones the private remote bare, points it at the folder and leaves the
folder's files untouched, so `private-git NAME status` then shows what differs
between the two sides. Put the script on your PATH, or alias it.

## Daily

```bash
private-git Vault save                        # stage everything, ignored files included
private-git Vault commit && private-git Vault push
```

and for a project, where a partner pushes too:

```bash
private-git TSP pull                          # the partner's work lands in the folder
private-git TSP save && private-git TSP commit && private-git TSP push
git status                                    # what of it the allowlist lets through
git add Master/M1/S7/Programming/Project-TSPSolver && git commit
```

Plain `git` inside a folder is always this repository; a private one is never
reached by accident, only by name.

## Why `save`, and not `add -A`

`git add` obeys `.gitignore` even when a path is named, and for the vault that
`.gitignore` is this repository's — it hides precisely what the vault exists to
keep, and `git status` hides it too, so a missing file never announces itself.
`save` therefore does not consult it: it lists the folder with `ls-files`,
reading **`never-track.ignore`** and no other exclude source, then adds with
`--force`. It prints what it staged, which is the only honest signal here.

`never-track.ignore` is short on purpose. A pattern in it loses the file from
the private side as well, so it names only what a documented command rebuilds:
virtualenvs, caches, build and render trees, LaTeX intermediates, `.env`.

## What the public side publishes from a project folder

A project folder is ignored wholesale, then named kinds are let back in:
`README.md`, `steps.json`, `steps/`, `src/`, `include/`, `tests/`,
`notebooks/`, `CMakeLists.txt`, `environment.yml`, `pyproject.toml`, and `.py`
files at the folder root. A partner's data file, report or handout stays
private until a rule names it. `handout/`, `data/` and `.dat` files are denied
again inside the allowed folders, so nothing the staff distributed can reach
the public side through them. Rules: the project blocks in `.gitignore`.
