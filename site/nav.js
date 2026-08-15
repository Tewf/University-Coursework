/* Header, breadcrumb and footer, built from site/manifest.json so no page
   repeats them. Each page declares its depth with <body data-base="../../">;
   guessing it from the URL would break the moment the repo is served from a
   different prefix. Content links live in the pages themselves, so the site
   still reads with JavaScript off. */

const base = document.body.dataset.base || './';
const rootUrl = new URL(base, location.href);

/** Path of the current page relative to the repo root, e.g. "Bachelor/Java/". */
function currentPath() {
  let rel = location.href.slice(rootUrl.href.length);
  rel = decodeURIComponent(rel.split('#')[0].split('?')[0]);
  return rel.replace(/index\.html$/, '');
}

function el(tag, attrs = {}, ...kids) {
  const n = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (k === 'class') n.className = v;
    else n.setAttribute(k, v);
  }
  for (const kid of kids) n.append(kid);
  return n;
}

/** Every manifest page that is an ancestor of `path`, shortest first. */
function trail(pages, path) {
  return pages
    .filter(p => path === p.path || path.startsWith(p.path))
    .sort((a, b) => a.path.length - b.path.length);
}

function render(manifest) {
  const path = currentPath();
  const crumbs = trail(manifest.pages, path);
  const here = crumbs[crumbs.length - 1];

  const nav = el('nav', { class: 'crumbs', 'aria-label': 'Breadcrumb' });
  crumbs.forEach((p, i) => {
    const last = i === crumbs.length - 1;
    const href = base + p.path;
    if (i > 0) nav.append(el('span', { class: 'sep' }, '/'));
    if (last) {
      nav.append(el('span', { 'aria-current': 'page' }, p.short));
    } else {
      nav.append(el('a', { href }, p.short));
    }
  });

  const head = el('header', { class: 'site-head' },
    el('div', { class: 'wrap' },
      el('a', { class: 'brand', href: base }, manifest.brand),
      nav,
      el('div', { class: 'spacer' }),
      el('a', { class: 'repo', href: manifest.repo + (here && here.path ? '/tree/main/' + here.path : '') },
        'Source on GitHub')
    )
  );

  const foot = el('footer', { class: 'site-foot' },
    el('div', { class: 'wrap' },
      el('p', {},
        'Code and writing are MIT. ',
        el('a', { href: base + 'NOTICE' }, 'NOTICE'),
        ' matters here: practical subjects, handouts and published papers belong to their authors and are cited, not redistributed.'
      )
    )
  );

  document.body.prepend(head);
  document.body.append(foot);
}

fetch(base + 'site/manifest.json')
  .then(r => r.json())
  .then(render)
  .catch(() => { /* no chrome is better than a broken page */ });
