/* Helpers shared by the interactive figures.  Vanilla DOM, no build step. */
const SVGNS = "http://www.w3.org/2000/svg";

export function svg(tag, attrs = {}, parent = null) {
  const e = document.createElementNS(SVGNS, tag);
  for (const [k, v] of Object.entries(attrs)) e.setAttribute(k, v);
  if (parent) parent.appendChild(e);
  return e;
}

export function clear(node) { while (node.firstChild) node.removeChild(node.firstChild); }

/** A labelled range control.  Returns an object with .value and .on(fn). */
export function slider(host, { label, min, max, step, value, fmt = (v) => v }) {
  const wrap = document.createElement("div");
  wrap.className = "ctl";
  const lab = document.createElement("label");
  const b = document.createElement("b");
  lab.append(document.createTextNode(label), b);
  const input = document.createElement("input");
  Object.assign(input, { type: "range", min, max, step, value });
  wrap.append(lab, input);
  host.appendChild(wrap);
  const api = {
    get value() { return parseFloat(input.value); },
    set value(v) { input.value = v; b.textContent = fmt(parseFloat(input.value)); },
    on(fn) { input.addEventListener("input", fn); return api; },
  };
  api.value = value;
  return api;
}

/** A labelled checkbox.  Returns an object with .checked and .on(fn). */
export function toggle(host, { label, checked = true }) {
  const wrap = document.createElement("label");
  wrap.className = "toggle";
  const input = document.createElement("input");
  input.type = "checkbox";
  input.checked = checked;
  wrap.append(input, document.createTextNode(label));
  host.appendChild(wrap);
  return {
    get checked() { return input.checked; },
    on(fn) { input.addEventListener("change", fn); return this; },
  };
}

/** The standing honesty banner.  Every figure page carries it; none may omit it. */
export function banner(host) {
  const d = document.createElement("div");
  d.className = "banner";
  d.innerHTML = "<b>This is an illustration, not evidence.</b> Theorem 12.2 is " +
    "conditional on the imported interface U_GJS, audit item C5 is open, the work is " +
    "AI-assisted and human verification of it is ongoing. Figures show bounds and " +
    "structure, never a measured property of any state. " +
    '<a href="../status.html">Status</a>.';
  host.prepend(d);
}

export function crumbs(host, here) {
  const n = document.createElement("nav");
  n.className = "crumbs";
  n.innerHTML = '<a href="../index.html">Overview</a> &rsaquo; ' +
    '<a href="index.html">Figures</a> &rsaquo; ' + here;
  host.prepend(n);
}

export const lerp = (a, b, t) => a + (b - a) * t;
export const clamp = (v, a, b) => Math.min(b, Math.max(a, v));

/** Show failures in the page instead of leaving an empty frame.  A published figure
    that silently renders nothing is worse than one that says what went wrong. */
export function guard(fn, out) {
  try { fn(); } catch (e) {
    if (out) out.textContent = "This figure failed to draw:\n" + (e && e.stack || e);
    console.error(e);
  }
}
window.addEventListener("error", (ev) => {
  const out = document.getElementById("out");
  if (out && !out.dataset.failed) {
    out.dataset.failed = "1";
    out.textContent = "This figure failed to load:\n" + (ev.message || ev.error);
  }
});
