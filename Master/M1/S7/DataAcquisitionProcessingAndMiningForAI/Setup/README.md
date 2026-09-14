# Setup: the course environment

The pre-course setup: one conda environment, `datacq`, declared by the
course's `environment.yml`, and a checker script that confirms Python, the
pinned packages and Jupyter answer as expected. Nothing is written here; the
folder exists so the environment can be rebuilt from what the course shipped.

## Running it

```bash
conda env create -f handout/environment.yml
conda activate datacq
python handout/verify_setup.py
```

The checker prints one line per requirement and exits non-zero when one is
missing. The same environment serves every lab and the project of the course.

## Source material

The setup guide, `environment.yml` and `verify_setup.py` are the course
staff's and are not redistributed here: see [NOTICE](../../../../../NOTICE).
They stay with the work on the private side, in `handout/`, and
`.publishignore` keeps them out of this copy.
