#!/usr/bin/env python3
"""V0 numeric falsification checkpoint for gate (II.11) — thermal two-torus route.

Scoping reference: gate_II11_scoping.tex, Sec. 5.2 and phase table Sec. 6.
Model conventions: lamport_part_ii_model_sheet.tex (torus T_L = R/2LZ, 2r_N sites,
eps_N = L/r_N, [Phi(x),Pi(y)] = i eps^{-1} delta, W(eps q + ip) = e^{i(Phi(q)+Pi(p))},
free vacuum functional (3.3), Wick constant c_{N,L} (3.4)).

Checks (falsification criteria in the scoping note):
  1. A2/A3: CCR phase and Weyl relation; exact diagonalization of the free 2-site
     model vs the closed thermal formula (coth weights); t->infty vacuum limit;
     mode-sum formula vs independent position-space matrix-function evaluation.
  2. A3(b): thermal fixed-coarse rate exponent at t in {1,2,4} vs vacuum (t=inf):
     slopes must be t-independent and at least the envelope bound theta.
  3. Interchange mechanism (Lemmas 3.1/3.2 in vivo): two-site and four-site
     anharmonic toys: spectral tail bound |F(t)-omega| <= 2 D(t), exponential rate
     = gap, truncation stability, N-drift record.
  4. A4b dictionary: delta_N = c_{N,L} - c^{ct}_{L,N} -> log(4/pi)/(2 pi).

The script asserts; it proves nothing. Analytic statements live in the scoping note.
"""

import numpy as np

rng = np.random.default_rng(20260812)
FAIL = []


def check(name, ok, detail=""):
    tag = "PASS" if ok else "FAIL"
    print(f"  [{tag}] {name}  {detail}")
    if not ok:
        FAIL.append(name)


# ----------------------------------------------------------------------
# Lattice kinematics (model sheet)
# ----------------------------------------------------------------------

def lattice(L, rN):
    eps = L / rN
    n = np.arange(-rN, rN)                      # site indices
    x = eps * n                                 # positions
    j = np.arange(-rN, rN)                      # momentum indices
    k = np.pi * j / L                           # momenta Gamma_N
    return eps, x, k


def gamma_lat(k, eps, m):
    return np.sqrt(m**2 + 4.0 * eps**-2 * np.sin(eps * k / 2.0) ** 2)


def fhat(f, x, k, eps):
    """hat f(k) = eps^{1/2} sum_x f(x) e^{-ikx}  (model-sheet normalization)."""
    return np.sqrt(eps) * (np.exp(-1j * np.outer(k, x)) @ f)


def Q_thermal_mode(q, p, L, rN, m, t):
    """A3 mode formula: Q^(t)_N(xi) = (2 rN)^{-1} sum_k coth(t gam/2)(gam^{-1}|qh|^2+gam|ph|^2)."""
    eps, x, k = lattice(L, rN)
    gam = gamma_lat(k, eps, m)
    w = 1.0 / np.tanh(t * gam / 2.0) if np.isfinite(t) else np.ones_like(gam)
    qh, ph = fhat(q, x, k, eps), fhat(p, x, k, eps)
    return (w * (np.abs(qh) ** 2 / gam + gam * np.abs(ph) ** 2)).sum() / (2 * rN)


def Q_thermal_pos(q, p, L, rN, m, t):
    """Independent position-space evaluation: exp(-eps/4 [q^T Om^{-1}coth q + p^T Om coth p])
    with Om = sqrt(M), M the periodic nearest-neighbour coupling matrix (numerical eigh —
    no Fourier bookkeeping used)."""
    eps, x, k = lattice(L, rN)
    ns = 2 * rN
    M = (m**2) * np.eye(ns) + eps**-2 * (2 * np.eye(ns)
        - np.roll(np.eye(ns), 1, axis=1) - np.roll(np.eye(ns), -1, axis=1))
    ev, U = np.linalg.eigh(M)
    om = np.sqrt(ev)
    cth = 1.0 / np.tanh(t * om / 2.0) if np.isfinite(t) else np.ones_like(om)
    Qq = q @ (U * (cth / om)) @ U.T @ q
    Qp = p @ (U * (cth * om)) @ U.T @ p
    return eps * (Qq + Qp)


# ----------------------------------------------------------------------
# Exact diagonalization in truncated oscillator bases
# ----------------------------------------------------------------------

def site_ops(nmax, eps, sigma):
    """Per-site Phi, Pi with [Phi,Pi] = i/eps, via standard ladder ops and scale sigma."""
    a = np.diag(np.sqrt(np.arange(1, nmax)), 1)
    ad = a.T.conj()
    Phi = (a + ad) / np.sqrt(2 * eps * sigma)
    Pi = 1j * (ad - a) * np.sqrt(sigma / (2 * eps))
    return Phi, Pi


def kron_ops(op_list_per_site, nmax, nsites):
    """Embed single-site operators into the chain tensor product."""
    eye = np.eye(nmax)
    out = []
    for s, op in op_list_per_site:
        mats = [eye] * nsites
        mats[s] = op
        acc = mats[0]
        for mm in mats[1:]:
            acc = np.kron(acc, mm)
        out.append(acc)
    return out


def build_chain(L, rN, m, nmax, lam=0.0, sigma=None):
    """H = eps/2 sum [Pi^2 + m^2 Phi^2 + eps^{-2}(Phi(x+eps)-Phi(x))^2]
         + lam * eps * sum :Phi^4:_c   (c = model-sheet Wick constant),
    plus the site operator lists for building Weyl generators."""
    eps, x, k = lattice(L, rN)
    ns = 2 * rN
    sigma = sigma or np.sqrt(m**2 + 2 * eps**-2)   # truncation-friendly scale
    Phi1, Pi1 = site_ops(nmax, eps, sigma)
    Phis = kron_ops([(s, Phi1) for s in range(ns)], nmax, ns)
    Pis = kron_ops([(s, Pi1) for s in range(ns)], nmax, ns)
    H = np.zeros((nmax**ns, nmax**ns), dtype=complex)
    gam = gamma_lat(k, eps, m)
    cN = (1.0 / (2 * rN)) * (1.0 / (2 * eps * gam)).sum()      # c_{N,L}, (3.4)
    for s in range(ns):
        dPhi = Phis[(s + 1) % ns] - Phis[s]
        H += (eps / 2) * (Pis[s] @ Pis[s] + m**2 * Phis[s] @ Phis[s]
                          + eps**-2 * dPhi @ dPhi)
        if lam:
            P2 = Phis[s] @ Phis[s]
            H += lam * eps * (P2 @ P2 - 6 * cN * P2 + 3 * cN**2 * np.eye(nmax**ns))
    return H, Phis, Pis, eps, cN


def weyl_op(Phis, Pis, eps, q, p):
    G = sum(eps * q[s] * Phis[s] for s in range(len(q))) \
        + sum(eps * p[s] * Pis[s] for s in range(len(p)))
    ev, U = np.linalg.eigh(G)
    return (U * np.exp(1j * ev)) @ U.T.conj()


def thermal_ev(H, W, t):
    ev, U = np.linalg.eigh((H + H.T.conj()) / 2)
    ev = ev - ev[0]
    w = np.exp(-t * ev)
    Wd = U.T.conj() @ W @ U
    return (w * np.diag(Wd)).sum() / w.sum(), ev


# ----------------------------------------------------------------------
# D4 mask and refinements
# ----------------------------------------------------------------------

S3 = np.sqrt(3.0)
Hmask = np.array([(1 + S3), (3 + S3), (3 - S3), (1 - S3)]) / (4 * np.sqrt(2))


def m0(tt):
    n = np.arange(4)
    return (Hmask @ np.exp(-1j * np.outer(n, np.atleast_1d(tt)))) / np.sqrt(2)


def Pr(ell, r):
    out = np.ones_like(np.atleast_1d(ell), dtype=complex)
    for jj in range(1, r + 1):
        out = out * m0(ell / 2.0**jj)
    return out


def Pinf(ell, jmax=60):
    return Pr(ell, jmax)


def refine_pos(f, L, rM):
    """One-step position-space D4 refinement (model sheet (2.6)) with periodization."""
    rN = 2 * rM
    out = np.zeros(2 * rN)
    for i in range(2 * rM):          # coarse site index (0..2rM-1 corresponds n=-rM..rM-1)
        for nn in range(4):
            out[(2 * i + nn) % (2 * rN)] += np.sqrt(2) * Hmask[nn] * f[i]
    return out


# ======================================================================
print("=" * 72)
print("V0 checkpoint — gate (II.11) thermal two-torus route      2026-08-12")
print("=" * 72)

# ----------------------------------------------------------------------
print("\n[1] A2/A3: algebra checks and exact diagonalization (free)")
# ----------------------------------------------------------------------
L, rN, m = 1.0, 1, 1.0                      # 2-site model
nmax = 28
H, Phis, Pis, eps, _ = build_chain(L, rN, m, nmax, lam=0.0)
q = np.array([0.45, -0.30]); p = np.array([0.25, 0.35])

# Operator identities are tested on the low-occupation corner: truncated Phi, Pi
# violate CCR only at the occupation boundary (verified: corner error 2e-15 at
# K<=16 vs 0.58 at the edge), and separately exponentiated truncated operators
# carry boundary artifacts that thermal traces never see.
n1 = np.arange(nmax)
occ = (n1[:, None] + n1[None, :]).ravel()      # total occupation, 2 sites
corner = occ <= nmax // 2

def corner_err(A):
    return np.abs(A[np.ix_(corner, corner)]).max()

# CCR phase: W(eps q + ip) = e^{i Phi(q)} e^{i Pi(p)} e^{(i/2) eps sum q p}
Wfull = weyl_op(Phis, Pis, eps, q, p)
Wq = weyl_op(Phis, Pis, eps, q, 0 * p)
Wp = weyl_op(Phis, Pis, eps, 0 * q, p)
phase = np.exp(0.5j * eps * (q * p).sum())
err = corner_err(Wfull - Wq @ Wp * phase)
check("CCR phase  W = e^{iPhi(q)} e^{iPi(p)} e^{(i/2) eps q.p}  [corner]",
      err < 1e-10, f"err={err:.2e}")

# Weyl relation W(xi)W(eta) = e^{-i sigma/2} W(xi+eta),  sigma = eps sum(q p' - p q')
q2 = np.array([-0.2, 0.5]); p2 = np.array([0.4, -0.1])
W2 = weyl_op(Phis, Pis, eps, q2, p2)
W12 = weyl_op(Phis, Pis, eps, q + q2, p + p2)
sig = eps * ((q * p2).sum() - (p * q2).sum())
err = corner_err(Wfull @ W2 - np.exp(-0.5j * sig) * W12)
check("Weyl relation with sigma = eps sum(qp'-pq')  [corner]",
      err < 1e-9, f"err={err:.2e}")

# thermal trace vs closed formula, several t and xi
for t in (1.0, 2.0):
    val, ev = thermal_ev(H, Wfull, t)
    ref = np.exp(-0.25 * Q_thermal_mode(q, p, L, rN, m, t))
    check(f"ED thermal trace vs coth formula, t={t}",
          abs(val - ref) < 5e-7, f"|ED-formula|={abs(val - ref):.2e}")
# vacuum limit
val, ev = thermal_ev(H, Wfull, 60.0)
ref = np.exp(-0.25 * Q_thermal_mode(q, p, L, rN, m, np.inf))
check("t->inf reproduces vacuum functional (model sheet (3.3))",
      abs(val - ref) < 5e-7, f"|ED-vac|={abs(val - ref):.2e}")
# truncation stability
H2, Phis2, Pis2, _, _ = build_chain(L, rN, m, nmax - 6, lam=0.0)
v2, _ = thermal_ev(H2, weyl_op(Phis2, Pis2, eps, q, p), 1.0)
v1, _ = thermal_ev(H, Wfull, 1.0)
check("free ED truncation stability (nmax vs nmax-6)", abs(v1 - v2) < 1e-6,
      f"drift={abs(v1 - v2):.2e}")   # thermal-trace accuracy itself certified above

# mode formula vs independent position-space matrix functions, larger lattices
for rr in (8, 64):
    Lb = 4.0
    qb = rng.normal(size=2 * rr) * 0.3
    pb = rng.normal(size=2 * rr) * 0.3
    for t in (1.0, 2.0, 4.0, np.inf):
        a1 = Q_thermal_mode(qb, pb, Lb, rr, m, t)
        a2 = Q_thermal_pos(qb, pb, Lb, rr, m, t)
        ok = abs(a1 - a2) < 1e-9 * max(1, abs(a1))
        if not ok:
            check(f"mode vs position-space Q, rN={rr}, t={t}", ok,
                  f"{a1:.12f} vs {a2:.12f}")
            break
    else:
        check(f"mode vs position-space Q, rN={rr}, all t", True, "")

# ----------------------------------------------------------------------
print("\n[2] A3(b): thermal fixed-coarse rate, t in {1,2,4} vs vacuum")
# ----------------------------------------------------------------------
# Q_{r,M}(xi) via free-rate Lemma 1.1 (momentum space) *and* via position-space
# refinement + generic Q — both computed, compared, then the rate measured.
Lb, rM, m2 = 1.0, 4, 1.0
epsM = Lb / rM
qc = np.zeros(2 * rM); pc = np.zeros(2 * rM)
qc[3] = 1.0; qc[6] = -0.7; pc[1] = 0.8; pc[4] = 0.5          # generic coarse symbol

theta_env = 2 * (2 - np.log2(3.0)) / (5 + (2 - np.log2(3.0)))  # envelope exponent

def Q_fine_of_refined(qc, pc, r, t):
    qf, pf = qc.copy(), pc.copy()
    for _ in range(r):
        qf, pf = refine_pos(qf, Lb, len(qf) // 2), refine_pos(pf, Lb, len(pf) // 2)
    return Q_thermal_mode(qf, pf, Lb, rM * 2**r, m2, t)

def Q_cont(qc, pc, t, Jmax):
    jj = np.arange(-Jmax, Jmax + 1)
    k = np.pi * jj / Lb
    gam = np.sqrt(m2**2 + k**2)
    w = 1.0 / np.tanh(t * gam / 2.0) if np.isfinite(t) else np.ones_like(gam)
    _, xM, kM = lattice(Lb, rM)
    # periodic extension of the coarse hats:
    qh = np.sqrt(epsM) * (np.exp(-1j * np.outer(k, xM)) @ qc)
    ph = np.sqrt(epsM) * (np.exp(-1j * np.outer(k, xM)) @ pc)
    env = np.abs(Pinf(epsM * k)) ** 2
    return (epsM / (2 * Lb)) * (env * w *
            (np.abs(qh) ** 2 / gam + gam * np.abs(ph) ** 2)).sum()

# implementation cross-check: momentum-space refinement equals position-space one
def Q_fine_momspace(qc, pc, r, t):
    rNf = rM * 2**r
    _, xf, kf = lattice(Lb, rNf)
    gam = gamma_lat(kf, Lb / rNf, m2)
    w = 1.0 / np.tanh(t * gam / 2.0) if np.isfinite(t) else np.ones_like(gam)
    _, xM, _ = lattice(Lb, rM)
    qh = np.sqrt(epsM) * (np.exp(-1j * np.outer(kf, xM)) @ qc)
    ph = np.sqrt(epsM) * (np.exp(-1j * np.outer(kf, xM)) @ pc)
    pr = np.abs(Pr(epsM * kf, r)) ** 2
    return (epsM / (2 * Lb)) * (pr * w *
            (np.abs(qh) ** 2 / gam + gam * np.abs(ph) ** 2)).sum()

a_pos = Q_fine_of_refined(qc, pc, 3, 2.0)
a_mom = Q_fine_momspace(qc, pc, 3, 2.0)
check("refinement: position-space (2.6) == momentum-space (free-rate (1.5))",
      abs(a_pos - a_mom) < 1e-9, f"diff={abs(a_pos - a_mom):.2e}")

Jmax = rM * 2**15
slopes = {}
print("      r : " + "  ".join(f"t={t}" for t in (1.0, 2.0, 4.0, np.inf)))
diffs_by_t = {}
for t in (1.0, 2.0, 4.0, np.inf):
    Qc = Q_cont(qc, pc, t, Jmax)
    diffs = []
    for r in range(1, 11):
        diffs.append(abs(Q_fine_momspace(qc, pc, r, t) - Qc))
    diffs_by_t[t] = np.array(diffs)
for r in range(1, 11):
    print(f"     {r:2d} : " + "  ".join(f"{diffs_by_t[t][r-1]:.3e}" for t in (1.0, 2.0, 4.0, np.inf)))
for t in (1.0, 2.0, 4.0, np.inf):
    d = np.log2(diffs_by_t[t])
    slope = np.polyfit(np.arange(7, 11), d[6:10], 1)[0]
    slopes[t] = slope
print("      LSQ slopes (r=7..10):",
      {(str(t) if np.isfinite(t) else "inf"): f"{s:.4f}" for t, s in slopes.items()})
drift = max(abs(slopes[t] - slopes[np.inf]) for t in (1.0, 2.0, 4.0))
check("thermal slopes t-independent (drift < 0.05)", drift < 0.05, f"drift={drift:.4f}")
check(f"decay at least the envelope bound (slope <= -theta={theta_env:.4f})",
      slopes[np.inf] <= -theta_env + 0.02, f"slope(inf)={slopes[np.inf]:.4f}")

# ----------------------------------------------------------------------
print("\n[3] Interchange mechanism in vivo (anharmonic toys)")
# ----------------------------------------------------------------------
lam = 0.4
# two-site toy (M = 0 level): full ED
H2s, Ph2, Pi2, eps0, c0 = build_chain(1.0, 1, 1.0, 26, lam=lam)
q0 = np.array([0.4, -0.25]); p0 = np.array([0.3, 0.2])
W0 = weyl_op(Ph2, Pi2, eps0, q0, p0)
vals = {}
ev0 = None
for t in (1.0, 2.0, 3.0, 4.0, 6.0, 8.0):
    vals[t], ev0 = thermal_ev(H2s, W0, t)
omega0 = np.linalg.eigh((H2s + H2s.T.conj()) / 2)[1][:, 0]
w_gs = omega0.conj() @ (W0 @ omega0)
gap0 = ev0[1] - ev0[0]
okD, rate_pts = True, []
for t in (2.0, 3.0, 4.0, 6.0, 8.0):
    D = np.exp(-t * (ev0[1:] - ev0[0])).sum()
    lhs = abs(vals[t] - w_gs)
    okD = okD and (lhs <= 2 * D + 1e-12)
    if lhs > 1e-14:
        rate_pts.append((t, np.log(lhs)))
check("two-site: |F(t) - omega(W)| <= 2 D(t) on t-grid", okD, "")
if len(rate_pts) >= 3:
    ts, ls = np.array(rate_pts).T
    fitted = -np.polyfit(ts, ls, 1)[0]
    check("two-site: exponential rate ~ gap (within 20%)",
          abs(fitted - gap0) < 0.2 * gap0, f"fit={fitted:.4f}, gap={gap0:.4f}")
# truncation stability (interacting)
H2b, Ph2b, Pi2b, _, _ = build_chain(1.0, 1, 1.0, 20, lam=lam)
e0a = np.linalg.eigvalsh((H2s + H2s.T.conj()) / 2)[0]
e0b = np.linalg.eigvalsh((H2b + H2b.T.conj()) / 2)[0]
check("two-site interacting truncation stability (nmax 26 vs 20)",
      abs(e0a - e0b) < 1e-6 * max(1, abs(e0a)), f"dE0={abs(e0a - e0b):.2e}")

# four-site toy (N = 1 level): mode-doubling drift + tail bound
H4, Ph4, Pi4, eps1, c1 = build_chain(1.0, 2, 1.0, 7, lam=lam)
q1, p1 = refine_pos(q0, 1.0, 1), refine_pos(p0, 1.0, 1)
W1 = weyl_op(Ph4, Pi4, eps1, q1, p1)
ev1 = None
okD4 = True
vals4 = {}
for t in (2.0, 4.0, 6.0):
    vals4[t], ev1 = thermal_ev(H4, W1, t)
gs4 = np.linalg.eigh((H4 + H4.T.conj()) / 2)[1][:, 0]
w_gs4 = gs4.conj() @ (W1 @ gs4)
for t in (2.0, 4.0, 6.0):
    D = np.exp(-t * (ev1[1:] - ev1[0])).sum()
    okD4 = okD4 and (abs(vals4[t] - w_gs4) <= 2 * D + 1e-12)
check("four-site: |F(t) - omega(W)| <= 2 D(t) on t-grid", okD4, "")
gap1 = ev1[1] - ev1[0]
e0_4 = np.linalg.eigvalsh((H4 + H4.T.conj()) / 2)[0]
print(f"      mode-doubling record: E0: {e0a:+.6f} -> {e0_4:+.6f}, "
      f"gap: {gap0:.6f} -> {gap1:.6f}, omega(W): {w_gs.real:+.6f} -> {w_gs4.real:+.6f}")
print(f"      (drifts are the N=0 -> N=1 approximation step; recorded, not asserted)")
# Laplace-lemma illustration: partition functions close at two t's vs gap closeness
Z_ratio = lambda ev, t: np.exp(-t * (ev - ev[0])).sum()
print(f"      Z-tail(t=2): {Z_ratio(ev0,2.0):.6f} (2-site) vs {Z_ratio(ev1,2.0):.6f} (4-site)")

# ----------------------------------------------------------------------
print("\n[4] A4b dictionary: delta_N -> log(4/pi)/(2 pi)")
# ----------------------------------------------------------------------
delta_pred = np.log(4 / np.pi) / (2 * np.pi)
print(f"      analytic prediction: {delta_pred:.10f}")
Ld, md = 1.0, 1.0
prev = None
ok_dec = True
for Nexp in range(4, 15):
    rr = 2**Nexp
    epsn, xx, kk = lattice(Ld, rr)
    gN = gamma_lat(kk, epsn, md)
    gC = np.sqrt(md**2 + kk**2)
    cN = (1.0 / (2 * Ld)) * (1.0 / (2 * gN)).sum()
    cC = (1.0 / (2 * Ld)) * (1.0 / (2 * gC)).sum()
    dN = cN - cC
    if Nexp in (4, 8, 12, 14):
        print(f"      N={Nexp:2d}  r_N={rr:6d}   delta_N = {dN:.10f}   "
              f"|delta_N - pred| = {abs(dN - delta_pred):.3e}")
    if prev is not None:
        ok_dec = ok_dec and (abs(dN - delta_pred) <= abs(prev - delta_pred) + 1e-12)
    prev = dN
check("delta_N converges to log(4/pi)/(2 pi), monotone approach",
      ok_dec and abs(prev - delta_pred) < 2e-4,
      f"final |delta - pred| = {abs(prev - delta_pred):.3e}")

# ----------------------------------------------------------------------
print("\n" + "=" * 72)
if FAIL:
    print(f"V0 RESULT: {len(FAIL)} FAILURE(S): " + ", ".join(FAIL))
    raise SystemExit(1)
print("V0 RESULT: ALL CHECKS PASSED")
