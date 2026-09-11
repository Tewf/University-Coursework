# Project: acquire, clean, mine

The course's graded work, done in a fixed pair and marked out of 20. One
pipeline that pulls a chosen slice of a live API, cleans and explores it, and
ends on a mining result that can be explained to someone who has not seen the
data.

## State

Not started. No source registered, no pair fixed. M0 is the first thing due.

## The four submissions

| Milestone | Due | Holds | Marked |
|---|---|---|---|
| M0 | before the week 3 lab | both names, the source, the scope in a sentence, and confirmation of the accounts it needs | pass/fail |
| M1 | before the week 4 lab | a log of what was pulled, the code that pulled it, and the dimensions every Parquet file came out at — not the rows themselves | pass/fail |
| M2 | before the week 6 lab | the one-page data card and the exploratory notebook | pass/fail |
| M3 | defended in the week 8 lab, files a week later | pipeline notebook, a 3–5 page report, the updated data card | out of 20 |

Missing any of the first three costs a point off the final mark. The scope
registered at M0 may be revised once, at M1, with a sentence in the log saying
what the first real pull showed; after that it is fixed.

## Choosing a source

Eight are on offer: Crossref, GitHub, Hacker News, Open-Meteo, TMDB, MediaWiki,
data.gouv.fr and Twitch. All but TMDB and Twitch answer an unauthenticated
browser request, so each can be inspected before it is committed to — which is
the point of looking first: how many fields come back populated, and how much
one request actually returns.

Two pairs may share a source but not a scope, so the entities, the time window
and the filters have to be pinned down precisely at M0.

## Rules that hold whichever source is picked

- **Query the API, not the page.** Scraping is demonstrated in the course, not
  used here.
- **Bulk pulls happen outside class hours.** The lab is for testing the script.
- **Credentials come from the environment**, never from a notebook cell, and
  never from a submitted file.
- **The final notebook runs top to bottom on a fresh kernel**, reading the
  cached raw Parquet rather than re-pulling.
- **Personal data is accounted for**: the report and the data card say what was
  collected, what was dropped, and why what remains is justified.

## What lives here, and what does not

The code and the writing. Not the data: the raw Parquet and the cleaned dataset
stay on disk and `.gitignore` keeps them out, which is also what the course
asks — the milestones take the shapes of the files, not the files.

## Source material

The project handout and the data card template are the course staff's and are
not redistributed here: see [NOTICE](../../../../../NOTICE). Both sit in this
folder's own `handout/`, which `.gitignore` excludes.
