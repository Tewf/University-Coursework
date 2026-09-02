# site/

The shared chrome for the GitHub Pages site. Pages hold their own content; this
folder holds everything they would otherwise repeat.

| File | Is |
|---|---|
| [manifest.json](manifest.json) | the list of pages, and the only source of the breadcrumb |
| [nav.js](nav.js) | builds the header, breadcrumb and footer from that list |
| [style.css](style.css) | the whole visual design |
| [chart.js](chart.js) | draws results from the data files that produced them |
| [replay.js](replay.js) | replays a recorded Battleship game |
| favicon.svg · og.png | the tab icon and the social preview |

## Adding a page

Three edits, and the page is broken in a quiet way if any is missed.

**1. Write `index.html` with the right `data-base`.** It is the number of
`../` needed to climb back to the repository root, and every link to `site/`
goes through it:

```html
<body data-base="../../../../">          <!-- Master/M1/S7/Programming/ -->
<link rel="stylesheet" href="../../../../site/style.css">
```

`nav.js` uses it instead of guessing from the URL, so the site still works
served from a different prefix.

**2. Add the page to [manifest.json](manifest.json).**

```json
{ "path": "Master/M1/S7/Programming/", "title": "Programming: Python and C++", "short": "Programming" }
```

`path` is relative to the root and ends with `/`. `short` is the breadcrumb
label. The breadcrumb is every manifest entry whose `path` is a prefix of the
current one, shortest first, so a page missing from the list does not merely
lose its own crumb — **it renders its parent as the current page**, and points
"Source on GitHub" at the parent's folder. Directories with no page of their
own are simply absent, which is why `Bachelor/L3/` and `Master/M1/` never
appear.

**3. Add the page to [.gitattributes](../.gitattributes).**

```
Master/M1/*/*/index.html                         linguist-documentation=true
```

Without it the page counts as HTML in GitHub's language bar. That bar once read
99% HTML because the Quarto renders drowned out the code that produced them;
every page here is excluded so it measures the coursework instead.

## Checking it

Serve the repository root and open the page, rather than opening the file
directly — `nav.js` fetches the manifest, which `file://` refuses:

```bash
python3 -m http.server 8000
```

The header should end on the page you are looking at, and "Source on GitHub"
should point at that page's own folder.
