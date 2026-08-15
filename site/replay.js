/* Plays back games recorded by tools/ReplayRecorder.java.
   Nothing here decides anything: the shots and the heatmap both come out of
   the Java run, so the board shows what the bot did, not an imitation of it.

   Turn i means: i shots have been fired, the heatmap on screen is the one the
   bot computed to choose shot i, and shot i is the cell outlined in gold. */

import { rampColour } from './chart.js';

const MISS = 3;

export async function loadReplays(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`replays: ${res.status}`);
  return res.json();
}

/** Cells occupied by the fleet, as a Set of r*n+c. */
function fleetCells(fleet, n) {
  const set = new Set();
  for (const s of fleet) {
    for (let k = 0; k < s.len; k++) {
      const r = s.v ? s.r + k : s.r;
      const c = s.v ? s.c : s.c + k;
      if (r < n && c < n) set.add(r * n + c);
    }
  }
  return set;
}

function buildBoard(host, n) {
  host.classList.add('board');
  host.style.gridTemplateColumns = `repeat(${n}, 1fr)`;
  const cells = [];
  for (let i = 0; i < n * n; i++) {
    const d = document.createElement('div');
    d.className = 'cell';
    host.append(d);
    cells.push(d);
  }
  return cells;
}

export class Replay {
  constructor(host, { board, showHeat = true }) {
    this.n = board;
    this.cells = buildBoard(host, board);
    this.showHeat = showHeat;
    this.revealFleet = false;
    this.timer = null;
    this.onchange = () => {};
  }

  load(game) {
    this.game = game;
    this.ships = fleetCells(game.fleet, this.n);
    this.turn = 0;
    this.draw();
  }

  get total() { return this.game.shots.length; }

  seek(t) {
    this.turn = Math.max(0, Math.min(this.total, t));
    this.draw();
    this.onchange(this);
  }

  /** loop: rest on the sunk fleet for a moment, then start over. */
  play({ loop = false } = {}) {
    if (this.timer) return;
    if (this.turn >= this.total) this.seek(0);
    let rest = 0;
    this.timer = setInterval(() => {
      if (this.turn >= this.total) {
        if (!loop) return this.pause();
        if (rest++ < 7) return;
        rest = 0;
        return this.seek(0);
      }
      this.seek(this.turn + 1);
    }, 220);
    this.onchange(this);
  }

  pause() {
    clearInterval(this.timer);
    this.timer = null;
    this.onchange(this);
  }

  get playing() { return this.timer !== null; }

  draw() {
    const { game, n } = this;
    const heat = this.showHeat && game.heat ? game.heat[this.turn] : null;
    const top = heat ? Math.max(...heat, 1) : 1;

    for (let i = 0; i < n * n; i++) {
      const cell = this.cells[i];
      cell.className = 'cell';
      cell.style.background = heat ? rampColour(heat[i] / top) : '';
      cell.replaceChildren();
      if (this.revealFleet && this.ships.has(i)) {
        const mark = document.createElement('span');
        mark.className = 's';
        cell.append(mark);
      }
    }

    for (let k = 0; k < this.turn; k++) {
      const s = game.shots[k];
      const cell = this.cells[s.r * n + s.c];
      cell.classList.add(s.res === MISS ? 'miss' : 'hit');
      cell.style.background = '';
    }

    const next = game.shots[this.turn];
    if (next) this.cells[next.r * n + next.c].classList.add('next');
  }

  /** Hits landed so far, out of the 19 cells the fleet occupies. */
  hits() {
    let h = 0;
    for (let k = 0; k < this.turn; k++) if (this.game.shots[k].res !== MISS) h++;
    return h;
  }
}

/** Two boards stepping together on the same fleet. */
export function race(hosts, games, board) {
  const players = hosts.map(h => new Replay(h, { board, showHeat: false }));
  players.forEach((p, i) => p.load(games[i]));
  const longest = Math.max(...games.map(g => g.shots.length));
  return {
    players,
    longest,
    seek(t) { players.forEach(p => p.seek(Math.min(t, p.total))); },
    done(t) { return t >= longest; }
  };
}
