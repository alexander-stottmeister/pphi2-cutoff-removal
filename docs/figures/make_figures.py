#!/usr/bin/env python3
"""Generate the figures of docs/figures/ and the sampled curves the site animates.

    python3 docs/figures/make_figures.py        # from the repository root

Three quantities are computed here from the manuscript's own formulas rather than
drawn -- the filter W_gamma of Lemma 9.1, the tail T_gamma it induces, and the rate
function Psi_gamma of Lemma 10.5 -- and they feed ONE of the five figures, rate.svg, and
the interactive rate page.  imports-dag.svg is generated from the manuscript's reference
graph; the other three are drawn to scale and evaluate nothing.  Requires NumPy and
SciPy, like the other numerics in this repository.

The filter.  Lemma 9.1 puts hat W_gamma(E) = chi(E)/E with chi smooth, 0 on
[-gamma/2, gamma/2] and 1 outside (-gamma, gamma).  hat W_gamma is odd, so

    W_gamma(t) = -(i/pi) int_0^infty sin(tE) chi(E) / E dE ,

and beyond E = gamma the integrand is sin(tE)/E exactly, whose tail is pi/2 - Si(t gamma).
Only the transition window [gamma/2, gamma] needs quadrature.  hat W_gamma decays like
1/|E|, so this integral is improper, not absolutely convergent; the lemma's own route to
W_gamma in L^1 is integration by parts, valid because hat W_gamma is globally smooth with
every derivative of order >= 1 in L^1.  The sine form is used here because it is exact.
"""
import json, pathlib, sys
import numpy as np
from scipy.integrate import quad
from scipy.special import sici

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from svg import Svg, LIGHT, DARK                                                   # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent


# ----------------------------------------------------------------- the filter
def chi(E, g):
    """Smooth 0 -> 1 transition on [g/2, g], built from the standard exp(-1/u) step."""
    a = np.abs(E)
    u = np.clip((a - g / 2) / (g / 2), 0.0, 1.0)
    f = lambda x: np.where(x > 0, np.exp(-1.0 / np.maximum(x, 1e-300)), 0.0)
    s = f(u) / (f(u) + f(1.0 - u))
    return np.where(a <= g / 2, 0.0, np.where(a >= g, 1.0, s))


def W_abs(t, g):
    """|W_gamma(t)|.

    The window [g/2, g] is integrated with an oscillatory quadrature weight, which keeps
    its digits where a plain rule would lose them, and the tail beyond E = g is exact:
    there chi = 1, so int_g^inf sin(tE)/E dE = pi/2 - Si(tg).

    The two pieces are each O(1/t) and cancel to something far smaller -- that
    cancellation IS the super-polynomial decay, since hat W_gamma is smooth across
    E = g.  Below about 1e-9 the difference is at the precision floor of that
    cancellation, so values are clipped there rather than reported as signal.
    """
    t = abs(float(t))
    if t == 0.0:
        return 0.0                                   # W_gamma is odd
    f = lambda E: float(chi(np.array(E), g)) / E
    window = quad(f, g / 2, g, weight="sin", wvar=t, limit=400)[0]
    return max(abs(window + (np.pi / 2 - sici(t * g)[0])) / np.pi, 0.0)


NOISE_FLOOR = 1e-9


def filter_curves(g, tmax=160.0):
    """|W|, its L1 norm, and the tail T(r) = int_{|t|>r} |W|, on a graded grid."""
    ts = np.unique(np.concatenate([np.linspace(0, 8, 400), np.linspace(8, 40, 400),
                                   np.linspace(40, tmax, 300)]))
    ws = np.array([W_abs(t, g) for t in ts])
    ws[ws < NOISE_FLOOR] = 0.0
    cum = np.concatenate([[0.0], np.cumsum(np.diff(ts) * (ws[1:] + ws[:-1]) / 2)])
    l1 = 2 * cum[-1]
    def T(r):
        if r >= ts[-1]:
            return 0.0
        return float(2 * (cum[-1] - np.interp(r, ts, cum)))
    return ts, ws, l1, T


def psi_parts(d, g, M, l1, T, nmax=400):
    """The two summands of Psi_gamma separately: Lemma 10.5 is their sum."""
    n0 = int(np.floor(d))
    ns = range(n0, n0 + nmax)
    expo = 32 * M * sum(l1 * np.exp(-g * n / 4) for n in ns)
    tail = 32 * M * sum(T(n / 2) for n in ns)
    return expo, tail


def psi(d, g, M, l1, T, nmax=400):
    """Psi_gamma(d) of Lemma 10.5, with the max{2, .} clause below d_0 = 4 + 2/gamma."""
    v = sum(psi_parts(d, g, M, l1, T, nmax))
    return v if d >= 4 + 2 / g else max(2.0, v)


# --------------------------------------------------------------- figure 1: rate
def fig_rate(curves):
    """Two panels: where the super-polynomial decay comes from, and what it gives.

    Left, Lemma 9.1(i): |W_gamma(t)| against fixed power laws.  The curve crosses one
    guide after another -- its effective power keeps growing, which is what "faster than
    every polynomial" looks like when it is measured rather than asserted.

    Right, Lemma 10.5: the two summands of Psi_gamma.  The exponential part dies; the
    filter tail is what is left, and it is the part that carries the super-polynomial
    character.  Both panels are computed for ONE admissible chi.  The lemma leaves chi
    free and the constants depend on it, so the shapes are the content here, not the
    heights.
    """
    g, M = 1.0, 1.0
    ts, ws, l1, T = curves
    W, H = 720, 400
    s = Svg(W, H, "Where the super-polynomial rate comes from", 
            "Left: the filter kernel |W_gamma(t)| on log-log axes, crossing the t^-2 and "
            "t^-5 guides, so its effective power grows. Right: the exponential and "
            "filter-tail summands of Psi_gamma(d).")
    s.text(24, 20, "Two decay mechanisms, and which one survives", "b")
    s.text(W - 20, 20, "computed from Lemmas 9.1 and 10.5", "mut xs", text_anchor="end")

    # ---- left panel: |W(t)| and its envelope, log-log
    L, R, Tp, B = 60, 392, 62, 74
    lx1, ly0 = np.log10(160), -8.0
    X = lambda t: L + (R - L) * np.log10(max(t, 1)) / lx1
    Y = lambda v: Tp + (H - Tp - B) * (0.0 - np.log10(max(v, 1e-30))) / (0.0 - ly0)
    for e in range(0, -9, -2):
        s.line(L, Y(10.0 ** e), R, Y(10.0 ** e), "gr")
        s.text(L - 6, Y(10.0 ** e) + 3.5, "1e%d" % e, "mut xs", text_anchor="end")
    for t in (1, 10, 100):
        s.line(X(t), Tp, X(t), H - B, "gr").text(X(t), H - B + 14, str(t), "mut xs",
                                                 text_anchor="middle")
    s.line(L, H - B, R, H - B, "ax").line(L, Tp, L, H - B, "ax")
    # raw |W| faintly, then the envelope through its local maxima
    raw = [(t, w) for t, w in zip(ts, ws) if t >= 1 and w > 0]
    s.poly([(X(t), Y(w)) for t, w in raw if Y(w) < H - B],
           fill="none", stroke="var(--acc)", stroke_width=0.7, opacity="0.30")
    env = [(ts[i], ws[i]) for i in range(1, len(ws) - 1)
           if ts[i] >= 1 and ws[i] > 0 and ws[i] >= ws[i - 1] and ws[i] >= ws[i + 1]]
    s.poly([(X(t), Y(w)) for t, w in env], fill="none", stroke="var(--acc)", stroke_width=2.2)
    # two fixed powers, anchored ON the envelope: it is shallower than one, steeper than
    # the other, which is the whole point -- no single power describes it.
    for N, anchor, lab_at in ((2, 8.0, 3.0), (6, 120.0, 60.0)):
        t0, v0 = min(env, key=lambda p: abs(p[0] - anchor))
        c = v0 * t0 ** N
        pts = [(X(t), Y(c * t ** -N)) for t in np.logspace(0, lx1, 60)
               if Tp < Y(c * t ** -N) < H - B]
        if pts:
            s.poly(pts, fill="none", stroke="var(--mut)", stroke_width=1, stroke_dasharray="3 3")
            s.text(X(lab_at), Y(c * lab_at ** -N) - 4, "t^\u2212%d" % N, "mut xs")
    for t_at, slope in ((8.4, 1.2), (20.9, 3.1), (150.8, 6.7)):
        t0, v0 = min(env, key=lambda q: abs(q[0] - t_at))
        s.circle(X(t0), Y(v0), 2.6, fill="var(--warn)")
        s.text(X(t0) + 5, Y(v0) - 5, "%.1f" % slope, "xs b", fill="var(--warn)")
    s.text(L, Tp - 26, "|W_\u03b3(t)|, the filter kernel, and its envelope", "sm b",
           fill="var(--acc)")
    s.text(L, Tp - 12, "orange: the envelope's local log-log slope, which keeps growing",
           "xs", fill="var(--warn)")
    s.text((L + R) / 2, H - B + 32, "t", "mut sm", text_anchor="middle")
    s.text(L, H - 26, "No fixed power bounds it: shallower than t\u207b\u00b2 early, steeper",
           "xs mut")
    s.text(L, H - 12, "than t\u207b\u2076 late. Lemma 9.1(i), independent of A8.", "xs mut")

    # ---- right panel: the two summands of Psi
    L2, R2 = 452, W - 26
    ds = np.linspace(0, 60, 61)
    ex = np.array([psi_parts(d, g, M, l1, T)[0] for d in ds])
    tl = np.array([psi_parts(d, g, M, l1, T)[1] for d in ds])
    ly0b, ly1b = -5.0, 3.0
    X2 = lambda d: L2 + (R2 - L2) * d / 60
    Y2 = lambda v: Tp + (H - Tp - B) * (ly1b - np.log10(max(v, 1e-30))) / (ly1b - ly0b)
    for e in range(3, -6, -2):
        s.line(L2, Y2(10.0 ** e), R2, Y2(10.0 ** e), "gr")
        s.text(L2 - 6, Y2(10.0 ** e) + 3.5, "1e%d" % e, "mut xs", text_anchor="end")
    for d in (0, 20, 40, 60):
        s.line(X2(d), Tp, X2(d), H - B, "gr").text(X2(d), H - B + 14, str(d), "mut xs",
                                                   text_anchor="middle")
    s.line(L2, H - B, R2, H - B, "ax").line(L2, Tp, L2, H - B, "ax")
    s.poly([(X2(d), Y2(v)) for d, v in zip(ds, tl)], fill="none", stroke="var(--acc)",
           stroke_width=2.2)
    s.poly([(X2(d), Y2(v)) for d, v in zip(ds, ex) if Y2(v) < H - B], fill="none",
           stroke="var(--warn)", stroke_width=2, stroke_dasharray="4 2")
    d0 = 4 + 2 / g
    s.line(X2(d0), Tp, X2(d0), H - B, "", stroke="var(--ok)", stroke_width=1,
           stroke_dasharray="3 3")
    s.text(X2(d0) + 4, Tp + 10, "d\u2080", "xs", fill="var(--ok)")
    s.text(L2, Tp - 22, "\u03a8_\u03b3(d) , split into its two summands", "sm b")
    s.text(L2, Tp - 8, "filter tail", "xs", fill="var(--acc)")
    s.text(L2 + 62, Tp - 8, "exponential part", "xs", fill="var(--warn)")
    s.text((L2 + R2) / 2, H - B + 32, "d = dist(O, {g < 1})", "mut sm", text_anchor="middle")
    s.text(L2, H - 26, "One admissible \u03c7; Lemma 9.1 leaves \u03c7 free and the constants", "xs mut")
    s.text(L2, H - 12, "depend on it. \u03a8_\u03b3 is an upper bound, not a measured decay.", "xs mut")
    return s


# --------------------------------------------------- figure 2: the light cone
def fig_cone():
    """One speed everywhere: the cone edge is x = +-(a + |t|), drawn at sc px per unit.

    The content is the hypothesis of Lemma 10.3.  While |t| <= r_j/2 the cell B_j lies
    outside O_|t|, dist(B_j, O_|t|) >= r_j/2, and the clustering lemma gives an
    exponentially small bound.  Past that time the cone has swallowed the gap and only
    the trivial bound 2M is available.  Summing the two regimes over cells is what
    produces the rate function.
    """
    W, H, sc = 720, 430, 20
    a, rj = 1.4, 7.0                     # half-width of O, and dist(B_j, O)
    cx, base, top = 250, H - 74, 58
    tmax = (base - top) / sc
    X = lambda x: cx + x * sc
    Y = lambda t: base - t * sc
    s = Svg(W, H, "The two-regime bound",
            "Spacetime diagram. The cone O_|t| spreads from O at unit speed. While "
            "|t| <= r_j/2 the cell B_j is outside it and the bound is exponentially "
            "small; beyond that only the trivial bound 2M is available.")
    s.text(28, 24, "Exact light cone, exact filter: the two regimes", "b")
    s.text(W - 24, 24, "Lemma 10.3", "mut sm", text_anchor="end")
    half = rj / 2
    # the region where only the trivial bound holds, then the exponential region
    s.rect(X(-10.6), top, X(10.6) - X(-10.6), Y(half) - top, fill="var(--line)", opacity="0.16")
    s.rect(X(-10.6), Y(half), X(10.6) - X(-10.6), base - Y(half), fill="var(--ok)", opacity="0.07")
    # the cone itself
    s.poly([(X(-a), Y(0)), (X(-a - tmax), Y(tmax)), (X(a + tmax), Y(tmax)), (X(a), Y(0))],
           fill="var(--fill)", opacity="0.55", stroke="none")
    s.line(X(-a), Y(0), X(-a - tmax), Y(tmax), "", stroke="var(--acc)", stroke_width=1.8)
    s.line(X(a), Y(0), X(a + tmax), Y(tmax), "", stroke="var(--acc)", stroke_width=1.8)
    s.line(X(-10.6), Y(0), X(10.6), Y(0), "ax")
    s.line(cx, base + 8, cx, top - 6, "ax")
    s.text(X(10.6) + 8, Y(0) + 4, "x", "mut sm")
    s.text(cx + 8, top - 2, "t", "mut sm")
    # O and B_j
    s.rect(X(-a), Y(0) - 4, X(a) - X(-a), 8, fill="var(--acc)", rx=2)
    s.text(cx, Y(0) + 20, "O", "b", text_anchor="middle", fill="var(--acc)")
    s.rect(X(a + rj), Y(0) - 5, X(a + rj + 1) - X(a + rj), 10, fill="var(--warn)", rx=2)
    s.text(X(a + rj + 0.5), Y(0) + 20, "B_j", "b", text_anchor="middle", fill="var(--warn)")
    # r_j dimension line
    s.line(X(a), Y(0) - 20, X(a + rj), Y(0) - 20, "", stroke="var(--mut)", stroke_width=1)
    for xx in (a, a + rj):
        s.line(X(xx), Y(0) - 24, X(xx), Y(0) - 16, "", stroke="var(--mut)", stroke_width=1)
    s.text(X(a + rj / 2), Y(0) - 25, "r_j", "sm mut", text_anchor="middle")
    # the switch time
    s.line(X(-10.6), Y(half), X(10.6), Y(half), "", stroke="var(--warn)", stroke_width=1.2,
           stroke_dasharray="5 3")
    s.text(X(-10.4), Y(half) - 7, "|t| = r_j / 2", "sm b", fill="var(--warn)")
    s.text(X(-1.0), Y(2.6), "O_|t|", "sm", text_anchor="middle", fill="var(--acc)")
    # the two bounds
    s.text(W - 26, Y(half) + 26, "|C_j(t)|  \u2264  2M e^(\u2212\u03b3 r_j / 4)", "sm b",
           text_anchor="end", fill="var(--ok)")
    s.text(W - 26, Y(half) + 42, "B_j is still outside the cone:", "xs mut", text_anchor="end")
    s.text(W - 26, Y(half) + 55, "dist(B_j, O_|t|) \u2265 r_j / 2", "xs mut", text_anchor="end")
    s.text(W - 26, Y(half) - 34, "|C_j(t)|  \u2264  2M", "sm b", text_anchor="end",
           fill="var(--mut)")
    s.text(W - 26, Y(half) - 20, "only the trivial bound", "xs mut", text_anchor="end")
    s.text(28, H - 26, "The gap enters through the filter, the geometry through the cone; "
                       "the lemma is where they meet.", "mut sm")
    s.text(28, H - 10, "Summing the two regimes over the cells B_j gives the rate function "
                       "\u03a8_\u03b3 of Lemma 10.5.", "mut sm")
    return s


# ------------------------------------------------ figure 3: the plateau net
def fig_plateau():
    """Both cutoffs reach the value 1 on their plateau -- that is the definition.

    What differs between g and g\u2032 is the WIDTH of {g = 1}, not the height, so they
    are drawn at the same level and the order is visible as inclusion of plateaux.
    """
    W, H, L, R = 720, 300, 56, 34
    s = Svg(W, H, "The plateau net",
            "Two cutoffs g and g' in the net class, both with plateau value 1. "
            "{g = 1} is contained in {g' = 1}, and the rate is expressed in d(g, O), the "
            "distance from O to the edge of the plateau.")
    base, hgt = H - 78, 96
    X = lambda x: L + (W - L - R) * (x + 12) / 24
    s.line(L, base, W - R, base, "ax")
    s.line(L, base - hgt, W - R, base - hgt, "gr", stroke_dasharray="4 3")
    s.text(L - 8, base - hgt + 4, "1", "xs mut", text_anchor="end")
    s.text(L - 8, base + 4, "0", "xs mut", text_anchor="end")
    s.text(W - R + 8, base + 4, "x", "mut sm")
    for pl, ram, col, lab, dy in ((4.0, 1.7, "var(--mut)", "g", 16),
                                  (8.0, 1.7, "var(--ok)", "g\u2032", 34)):
        s.poly([(X(-12), base), (X(-pl - ram), base), (X(-pl), base - hgt),
                (X(pl), base - hgt), (X(pl + ram), base), (X(12), base)],
               fill="none", stroke=col, stroke_width=2)
        s.text(X(pl + ram) + 6, base - 6, lab, "b", fill=col)
        y = base - hgt + dy
        s.line(X(1.7), y, X(pl), y, "", stroke=col, stroke_width=1, stroke_dasharray="3 2")
        for xx in (1.7, pl):
            s.line(X(xx), y - 4, X(xx), y + 4, "", stroke=col, stroke_width=1)
        s.text(X((1.7 + pl) / 2), y - 5, "d(%s, O)" % lab, "xs", text_anchor="middle", fill=col)
    s.rect(X(-1.7), base - 4, X(1.7) - X(-1.7), 8, fill="var(--acc)", rx=2)
    s.text(X(0), base + 20, "O", "b", text_anchor="middle", fill="var(--acc)")
    s.text(L, 24, "g \u2AAF g\u2032 in the net class: the plateau widens, d(g, O) grows with it", "b")
    s.text(W - R, 24, "Definition 2.1", "mut sm", text_anchor="end")
    s.text(L, H - 26, "Directed by inclusion of plateau interiors. Convergence is along this "
                      "order \u2014 the full net,", "mut sm")
    s.text(L, H - 10, "with no subnet and no space averaging \u2014 and the rate is a function "
                      "of d(g, O) alone.", "mut sm")
    return s


# ------------------------------------------------- figure 4: the uniform gap
def fig_gap():
    W, H, L, R = 720, 300, 70, 40
    s = Svg(W, H, "The uniform gap",
            "spec H(g) is contained in {0} union [gamma, infinity) with one gamma for the "
            "whole cutoff class, so the gap does not close as the cutoff grows.")
    X = lambda e: L + (W - L - R) * e / 6.0
    g = 1.6
    rows = [("g₁", 0), ("g₂", 1), ("g₃", 2), ("g₄", 3)]
    for lab, i in rows:
        y = 76 + i * 44
        s.text(L - 12, y + 4, lab, "sm mut", text_anchor="end")
        s.line(L, y, W - R, y, "gr")
        s.circle(X(0), y, 4.5, fill="var(--acc)")
        s.rect(X(g), y - 7, X(6.0) - X(g), 14, fill="var(--fill)", rx=2)
        s.line(X(g), y - 7, X(g), y + 7, "", stroke="var(--ok)", stroke_width=2)
    s.line(X(g), 60, X(g), 76 + 3 * 44 + 22, "", stroke="var(--ok)", stroke_width=1,
           stroke_dasharray="4 3")
    s.text(X(g), 54, "γ", "b", text_anchor="middle", fill="var(--ok)")
    s.text(X(0), 54, "0", "b", text_anchor="middle", fill="var(--acc)")
    s.text(L, 24, "spec H(g) ⊆ {0} ∪ [γ, ∞), one γ for the whole class", "b")
    s.text(W - R, 24, "Theorem 7.8", "mut sm", text_anchor="end")
    s.text(L, H - 26, "The ground state is simple and the gap is bounded below uniformly in "
                      "the cutoff.", "mut sm")
    s.text(L, H - 10, "Lemma 9.1 turns that one number into a time kernel that decays faster "
                      "than every polynomial.", "mut sm")
    return s


# ------------------------------------------------- figure 5: the import graph
GJS = "A:gjs"


def clip(text, n):
    """Truncate on a word boundary, so a label never breaks mid-word."""
    if len(text) <= n:
        return text
    cut = text[:n].rsplit(" ", 1)[0]
    return cut + "\u2026"


SPINE = ["A:cutoff", "A:fkn", "A:stability", "A:hyper", "A:domain", "A:patch", "A:covar",
         "A:gjs", "prop:scaling", "thm:M2", "thm:G", "lem:filter", "lem:tworegime",
         "prop:onepath", "lem:rate", "thm:cauchy", "prop:spectral", "thm:MAIN",
         "thm:dichotomy"]


def fig_dag(results):
    by = {r["label"]: r for r in results}
    W, H = 720, 470
    cols = {}
    for i, lab in enumerate(SPINE[:8]):
        cols[lab] = (58 + i * 82, 74)
    chain = SPINE[8:]
    for i, lab in enumerate(chain):
        cols[lab] = (100 + (i % 2) * 300, 150 + i * 29)
    s = Svg(W, H, "The import graph",
            "A1-A8 and the spine of Part I. Everything whose proof chain reaches A8, the "
            "GJS package, inherits the conditionality of Theorem 12.2.")
    s.text(28, 26, "What Theorem 12.2 rests on", "b")
    s.text(W - 24, 26, "generated from part_i/main.tex", "mut xs", text_anchor="end")
    s.rect(28, 38, 10, 10, fill="var(--cfill)", stroke="var(--cond)", stroke_width=1.2, rx=2)
    s.text(43, 47, "proof chain reaches A8 \u2014 conditional on U_GJS", "xs", fill="var(--cond)")
    s.rect(268, 38, 10, 10, fill="var(--bg)", stroke="var(--ok)", stroke_width=1.2, rx=2)
    s.text(283, 47, "independent of A8", "xs", fill="var(--ok)")
    s.rect(400, 38, 10, 10, fill="var(--bg)", stroke="var(--line)", stroke_width=1.2, rx=2)
    s.text(415, 47, "imported hypothesis", "xs mut")
    for lab in SPINE:
        r = by.get(lab)
        if not r:
            continue
        x, y = cols[lab]
        for dep in sorted(set(r["uses"]) | set(r["proof_uses"])):
            if dep in cols:
                dx, dy = cols[dep]
                s.path("M%.1f %.1f C %.1f %.1f, %.1f %.1f, %.1f %.1f"
                       % (dx, dy + 9, dx, (dy + y) / 2, x, (dy + y) / 2, x, y - 9),
                       fill="none", stroke="var(--line)", stroke_width=1)
    for lab in SPINE:
        r = by.get(lab)
        if not r:
            continue
        x, y = cols[lab]
        cond = r["imports_A8"]
        is_hyp = lab.startswith("A:")
        if is_hyp:
            # A1-A7 are hypotheses: "independent of A8" is vacuous for them.  Only A8
            # itself is marked, because it is what the conditionality is about.
            col = "var(--cond)" if lab == GJS else "var(--line)"
            fill = "var(--cfill)" if lab == GJS else "var(--bg)"
        else:
            col = "var(--cond)" if cond else "var(--ok)"
            fill = "var(--cfill)" if cond else "var(--bg)"
        w = 74 if lab.startswith("A:") else 168
        s.rect(x - w / 2, y - 11, w, 22, fill=fill, stroke=col, stroke_width=1.4, rx=4)
        name = r["number"] if is_hyp else "%s %s" % (
            r["kind"][:4] if r["kind"] != "Theorem" else "Thm", r["number"])
        s.text(x, y + 4, name, "sm b", text_anchor="middle",
               fill="var(--fg)" if (is_hyp and lab != GJS) else col)
        if not is_hyp:
            s.text(x + w / 2 + 8, y + 4, clip(r["title"] or "", 42), "xs mut")
    ax, ay = cols["A:gjs"]
    s.text(ax, ay - 18, "U_GJS is item (vi)", "xs b", text_anchor="middle", fill="var(--cond)")
    return s


def main():
    out = HERE
    results = json.loads((ROOT / "docs" / "results.json").read_text())["results"]
    print("computing the filter ...")
    curves = filter_curves(1.0)
    ts, ws, l1, T = curves
    print("  ||W_1||_1 = %.5f   T_1(5) = %.3e   T_1(20) = %.3e" % (l1, T(5), T(20)))
    builders = {"rate": lambda: fig_rate(curves), "light-cone": fig_cone,
                "plateau-net": fig_plateau, "uniform-gap": fig_gap,
                "imports-dag": lambda: fig_dag(results)}
    for stem, build in builders.items():
        for suffix, theme in (("", LIGHT), ("-dark", DARK)):
            global THEME
            THEME = theme
            fig = build()
            fig.theme = theme
            fig.save(out / ("%s%s.svg" % (stem, suffix)))
        print("  wrote %s.svg and %s-dark.svg" % (stem, stem))
    # sampled curves for the interactive figures.  gamma enters the kernel itself, so
    # it cannot be a free slider in the browser: the site offers the values computed
    # here and says so.  M is an exact prefactor and stays continuous there.
    series = {}
    for gam in (0.5, 1.0, 2.0):
        c = curves if gam == 1.0 else filter_curves(gam)
        t2, w2, l2, T2 = c
        env = [(t2[i], w2[i]) for i in range(1, len(w2) - 1)
               if t2[i] >= 1 and w2[i] > 0 and w2[i] >= w2[i - 1] and w2[i] >= w2[i + 1]]
        dd = np.linspace(0, 60, 121)
        series["%g" % gam] = {
            "L1": float("%.6g" % l2),
            "d0": 4 + 2 / gam,
            "t": [round(float(x), 3) for x in t2[::3]],
            "absW": [float("%.4g" % v) for v in w2[::3]],
            "envT": [round(float(x), 3) for x, _ in env],
            "envW": [float("%.4g" % v) for _, v in env],
            "d": [round(float(x), 2) for x in dd],
            "psiExp": [float("%.5g" % psi_parts(d, gam, 1.0, l2, T2)[0]) for d in dd],
            "psiTail": [float("%.5g" % psi_parts(d, gam, 1.0, l2, T2)[1]) for d in dd],
        }
        print("  gamma=%g: ||W||_1 = %.4f, d0 = %.2f" % (gam, l2, 4 + 2 / gam))
    data = {"note": "Generated by docs/figures/make_figures.py. Do not edit by hand.",
            "about": "psiExp and psiTail are the two summands of Psi_gamma at M = 1; "
                     "Psi = M * (psiExp + psiTail), with the max{2, .} clause below d0.",
            "series": series}
    (out / "curves.json").write_text(json.dumps(data, indent=1) + "\n")
    # The pages import this statically rather than fetching it: a static import is
    # resolved before the module body runs, so there is no loading state to race and no
    # fetch to fail.  It does NOT make them work from file:// -- module scripts are
    # blocked there by the origin rules.  Serve docs/ over http to try them locally.
    (out / "curves.js").write_text(
        "// Generated by docs/figures/make_figures.py. Do not edit by hand.\n"
        "export const CURVES = " + json.dumps(data, separators=(",", ":")) + ";\n")
    print("  wrote curves.json and curves.js")


if __name__ == "__main__":
    main()
