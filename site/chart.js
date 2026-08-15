/* SVG charts, drawn by hand. No library, no build step, no CDN.
   Colours are read as CSS custom properties so the charts follow the
   light/dark theme without a second palette living in JavaScript. */

const NS = 'http://www.w3.org/2000/svg';

export function parseCsv(text) {
  const [head, ...lines] = text.trim().split(/\r?\n/);
  const keys = head.split(',');
  return lines.filter(Boolean).map(line => {
    const cells = line.split(',');
    const row = {};
    keys.forEach((k, i) => {
      const raw = cells[i];
      const n = Number(raw);
      row[k] = raw !== '' && !Number.isNaN(n) ? n : raw;
    });
    return row;
  });
}

function svg(tag, attrs = {}) {
  const n = document.createElementNS(NS, tag);
  for (const [k, v] of Object.entries(attrs)) n.setAttribute(k, v);
  return n;
}

function frame(width, height) {
  const s = svg('svg', {
    viewBox: `0 0 ${width} ${height}`,
    role: 'img',
    preserveAspectRatio: 'xMidYMid meet'
  });
  return s;
}

/** Six-step ramp defined in style.css, so dark mode is handled once. */
export function rampColour(t) {
  const step = Math.max(0, Math.min(5, Math.round(t * 5)));
  return `var(--ramp-${step})`;
}

/**
 * Horizontal bars with optional standard-error whiskers.
 * rows: [{ label, value, err? }]
 */
export function barChart(host, { rows, format = v => v, max = null, alt = null, axisLabel = '' }) {
  const rowH = 34, padT = 8, padB = axisLabel ? 30 : 12;
  const gutter = 108, right = 76, width = 640;
  const height = padT + rows.length * rowH + padB;
  const top = max ?? Math.max(...rows.map(r => r.value + (r.err || 0)));
  const plot = width - gutter - right;
  const x = v => gutter + (v / top) * plot;

  const s = frame(width, height);
  s.append(svg('line', {
    x1: gutter, x2: gutter, y1: padT, y2: padT + rows.length * rowH, class: 'grid-line'
  }));

  rows.forEach((r, i) => {
    const cy = padT + i * rowH + rowH / 2;
    const label = svg('text', { x: gutter - 10, y: cy + 4, 'text-anchor': 'end' });
    label.textContent = r.label;
    s.append(label);

    const bar = svg('rect', {
      x: gutter, y: cy - 9, width: Math.max(1, x(r.value) - gutter), height: 18, rx: 2,
      class: alt && alt(r) ? 'bar alt' : 'bar'
    });
    s.append(bar);

    if (r.err) {
      const a = x(r.value - r.err), b = x(r.value + r.err);
      s.append(svg('line', { x1: a, x2: b, y1: cy, y2: cy, class: 'err' }));
      s.append(svg('line', { x1: a, x2: a, y1: cy - 5, y2: cy + 5, class: 'err' }));
      s.append(svg('line', { x1: b, x2: b, y1: cy - 5, y2: cy + 5, class: 'err' }));
    }

    const val = svg('text', { x: x(r.value + (r.err || 0)) + 8, y: cy + 4, class: 'val' });
    val.textContent = format(r.value);
    s.append(val);
  });

  if (axisLabel) {
    const t = svg('text', { x: gutter, y: height - 8 });
    t.textContent = axisLabel;
    s.append(t);
  }

  host.replaceChildren(s);
  return s;
}

/**
 * Square matrix heatmap with row and column labels.
 * get(rowLabel, colLabel) returns a number, or null for the diagonal.
 */
export function matrixChart(host, { labels, colLabels = labels, get, format = v => v, note = '' }) {
  const cell = 62, gutter = 96, padT = 30, width = gutter + labels.length * cell + 8;
  const height = padT + labels.length * cell + (note ? 26 : 8);
  const s = frame(width, height);
  // this viewBox is much narrower than the bar charts', so left to stretch to
  // the column width it would magnify the labels until they collide
  s.setAttribute('class', 'matrix');

  const values = [];
  labels.forEach(r => labels.forEach(c => {
    const v = get(r, c);
    if (v !== null && v !== undefined) values.push(v);
  }));
  const top = Math.max(...values, 1);

  colLabels.forEach((c, j) => {
    const t = svg('text', { x: gutter + j * cell + cell / 2, y: padT - 10, 'text-anchor': 'middle' });
    t.textContent = c;
    s.append(t);
  });

  labels.forEach((r, i) => {
    const t = svg('text', { x: gutter - 10, y: padT + i * cell + cell / 2 + 4, 'text-anchor': 'end' });
    t.textContent = r;
    s.append(t);

    labels.forEach((c, j) => {
      const v = get(r, c);
      const x = gutter + j * cell, y = padT + i * cell;
      if (v === null || v === undefined) {
        s.append(svg('rect', { x: x + 1, y: y + 1, width: cell - 2, height: cell - 2, rx: 2, fill: 'var(--sunken)' }));
        return;
      }
      s.append(svg('rect', {
        x: x + 1, y: y + 1, width: cell - 2, height: cell - 2, rx: 2, fill: rampColour(v / top)
      }));
      const t2 = svg('text', {
        x: x + cell / 2, y: y + cell / 2 + 4, 'text-anchor': 'middle', class: 'val',
        fill: v / top > 0.62 ? 'var(--paper)' : 'var(--ink)'
      });
      t2.textContent = format(v);
      s.append(t2);
    });
  });

  if (note) {
    const t = svg('text', { x: 0, y: height - 8 });
    t.textContent = note;
    s.append(t);
  }

  host.replaceChildren(s);
  return s;
}

/**
 * Grouped bars: one cluster per entity, one bar per metric.
 * rows: [{ label, values: {metric: number} }]
 */
export function groupedBars(host, { rows, metrics, format = v => v.toFixed(3), domain = [0, 1] }) {
  const clusterW = 132, barGap = 3, padT = 12, padB = 46, axis = 40, width = axis + rows.length * clusterW + 10;
  const height = 220;
  const barW = (clusterW - 22) / metrics.length - barGap;
  const [lo, hi] = domain;
  const y = v => padT + (1 - (v - lo) / (hi - lo)) * (height - padT - padB);

  const s = frame(width, height);

  for (let g = 0; g <= 4; g++) {
    const v = lo + (hi - lo) * g / 4;
    s.append(svg('line', { x1: axis, x2: width - 6, y1: y(v), y2: y(v), class: 'grid-line' }));
    const t = svg('text', { x: axis - 8, y: y(v) + 4, 'text-anchor': 'end' });
    t.textContent = v.toFixed(2);
    s.append(t);
  }

  rows.forEach((row, i) => {
    const x0 = axis + i * clusterW + 11;
    metrics.forEach((m, j) => {
      const v = row.values[m.key];
      if (v === undefined) return;
      const x = x0 + j * (barW + barGap);
      const rect = svg('rect', {
        x, y: y(v), width: barW, height: Math.max(1, y(lo) - y(v)), rx: 2,
        fill: rampColour(0.25 + 0.7 * (j / Math.max(1, metrics.length - 1)))
      });
      const title = svg('title');
      title.textContent = `${row.label} · ${m.label}: ${format(v)}`;
      rect.append(title);
      s.append(rect);
    });
    const t = svg('text', { x: x0 + (clusterW - 22) / 2, y: height - padB + 18, 'text-anchor': 'middle', class: 'val' });
    t.textContent = row.label;
    s.append(t);
  });

  metrics.forEach((m, j) => {
    const x = axis + 4 + j * 96;
    s.append(svg('rect', { x, y: height - 18, width: 10, height: 10, rx: 2,
      fill: rampColour(0.25 + 0.7 * (j / Math.max(1, metrics.length - 1))) }));
    const t = svg('text', { x: x + 15, y: height - 9 });
    t.textContent = m.label;
    s.append(t);
  });

  host.replaceChildren(s);
  return s;
}
