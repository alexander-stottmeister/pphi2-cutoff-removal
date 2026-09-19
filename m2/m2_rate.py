#!/usr/bin/env python3
"""
M2 -- falsifiable checkpoint for the removal-of-the-spatial-cutoff strategy.

Model: the exactly solvable quadratic case P(xi) = xi^2 (Rosen 1972),

    H(g) = H_0 + lambda * (1/2) int g(x) :phi(x)^2: dx ,

whose ground state omega_g is the quasi-free state with one-particle operator

    mu_g = ( -Delta + m0^2 + lambda*g )^{1/2} ,      mu_1 = ( -Delta + m1^2 )^{1/2},
    m1^2 = m0^2 + lambda .

omega_g and omega_infty are Gaussian, hence completely determined by the covariances
    <phi phi> = (2 mu)^{-1},     <pi pi> = mu/2 .
So the local distance of the STATES is governed by the local size of

    Delta_phi = mu_g^{-1} - mu_1^{-1},        Delta_pi = mu_g - mu_1 .

QUESTION UNDER TEST.  With O a neighbourhood of the origin and d = dist(O, {g<1}),
which exponent governs the decay in d?

    candidates:   m0,   2*m0,   m1,   2*m1

PREDICTION of the strategy note (m2.tex, Prop. 4.1): the exact resolvent identity

    mu_g^{-1} - mu_1^{-1} = (lambda/pi) int_0^infty s^{-1/2}
                              P_O (A+s)^{-1} (1-g) (B+s)^{-1} P_O ds

forces a *round trip* O -> supp(1-g) -> O through the region {g=1}, where the local
mass is m1.  Hence the exponent is 2*m1 (NOT m0, and NOT m1), with prefactor
d^{-1/2} for Delta_phi and d^{-3/2} for Delta_pi.

This script discriminates the four candidates numerically.
"""

import numpy as np

# ----------------------------------------------------------------------------- setup
M0, LAM = 1.0, 3.0
M1 = np.sqrt(M0**2 + LAM)          # = 2.0 exactly, so the four candidates are
                                   # m0=1, 2m0=2, m1=2, 2m1=4  -> well separated
                                   # (2m0 and m1 coincide by design; the test still
                                   #  separates {1}, {2}, {4})


def operators(L, h, ell):
    """Discretised A = -Delta + m0^2 + lam*g and B = -Delta + m1^2 on [-L,L]."""
    x = np.arange(-L, L + h / 2, h)
    n = x.size
    lap = (np.diag(np.full(n, -2.0)) + np.diag(np.ones(n - 1), 1)
           + np.diag(np.ones(n - 1), -1)) / h**2
    g = (np.abs(x) <= ell).astype(float)          # sharp cutoff: g = 1_{[-ell,ell]}
    A = -lap + np.diag(M0**2 + LAM * g)
    B = -lap + np.diag(np.full(n, M1**2))
    return x, A, B


def diag_powers(S, i0, powers):
    """(S^p)_{i0 i0} for each p, from a single eigendecomposition of S."""
    w, V = np.linalg.eigh(S)
    assert w.min() > 0, f"non-positive eigenvalue {w.min()}"
    v2 = V[i0, :] ** 2                       # row i0 squared
    return {p: float(v2 @ (w ** p)) for p in powers}


def kernels_at_centre(L, h, ell, Bcache={}):
    """Return (Delta_phi, Delta_pi) kernel values at x=y=0.

    B does not depend on ell, so its eigendecomposition is cached: this leaves
    exactly one eigh per value of ell.
    """
    x, A, B = operators(L, h, ell)
    i0 = int(np.argmin(np.abs(x)))
    key = (L, h)
    if key not in Bcache:
        Bcache[key] = diag_powers(B, i0, (-0.5, 0.5))
    b = Bcache[key]
    a = diag_powers(A, i0, (-0.5, 0.5))
    # matrix element -> continuum kernel: divide by h (constant, irrelevant for slopes)
    return (a[-0.5] - b[-0.5]) / h, (a[0.5] - b[0.5]) / h


def fit_slope(d, y, prefactor_power):
    """Least-squares slope of log|y| + prefactor_power*log(d) against d."""
    z = np.log(np.abs(y)) + prefactor_power * np.log(d)
    Amat = np.vstack([d, np.ones_like(d)]).T
    slope, intercept = np.linalg.lstsq(Amat, z, rcond=None)[0]
    resid = z - (slope * d + intercept)
    return slope, intercept, np.max(np.abs(resid))


def run(L=25.0, h=0.025, ells=None):
    if ells is None:
        ells = np.arange(1.0, 4.01, 0.25)
    print(f"  grid: L={L}, h={h}, n={int(2*L/h)+1};  m0={M0}, lambda={LAM}, m1={M1}")
    print(f"  {'d':>6} {'Delta_phi(0,0)':>18} {'Delta_pi(0,0)':>18}")
    rows = []
    for ell in ells:
        dphi, dpi = kernels_at_centre(L, h, ell)
        rows.append((ell, dphi, dpi))
        print(f"  {ell:6.2f} {dphi:18.6e} {dpi:18.6e}")
    d = np.array([r[0] for r in rows])
    yphi = np.array([r[1] for r in rows])
    ypi = np.array([r[2] for r in rows])
    return d, yphi, ypi


def report(d, yphi, ypi):
    cands = {"m0": M0, "2*m0": 2 * M0, "m1": M1, "2*m1": 2 * M1}
    print("\n  === decay exponents (fitted -slope) ===")
    for name, y, ppow, ppred in (("Delta_phi", yphi, 0.5, "d^{-1/2}"),
                                 ("Delta_pi", ypi, 1.5, "d^{-3/2}")):
        s_raw, _, r_raw = fit_slope(d, y, 0.0)
        s_pre, _, r_pre = fit_slope(d, y, ppow)
        print(f"\n  {name}:")
        print(f"    raw fit  log|y| ~ c - k d          :  k = {-s_raw:8.4f}   maxresid {r_raw:.2e}")
        print(f"    with {ppred} prefactor divided out :  k = {-s_pre:8.4f}   maxresid {r_pre:.2e}")
        best = min(cands, key=lambda c: abs(cands[c] - (-s_pre)))
        print("    candidate exponents: " +
              ", ".join(f"{c}={v:.3f}" for c, v in cands.items()))
        print(f"    --> closest candidate: {best} = {cands[best]:.3f} "
              f"(|err| = {abs(cands[best] + s_pre):.4f})")


def prefactor_test(d, y, k):
    """Given the exponent k, fit log|y| + k d = c - p log d and return p."""
    z = np.log(np.abs(y)) + k * d
    Amat = np.vstack([-np.log(d), np.ones_like(d)]).T
    p, c = np.linalg.lstsq(Amat, z, rcond=None)[0]
    return p


def joint_fit(d, y):
    """Fit log|y| = c - k d - p log d for (c,k,p) simultaneously.

    Over a finite d-range the exponent k and the prefactor power p are partly
    degenerate, so fitting them together is the honest test.
    """
    z = np.log(np.abs(y))
    Amat = np.vstack([-d, -np.log(d), np.ones_like(d)]).T
    (k, p, c), *_ = np.linalg.lstsq(Amat, z, rcond=None)
    resid = z - Amat @ np.array([k, p, c])
    return k, p, np.max(np.abs(resid))


def local_slopes(d, y):
    """Successive-difference slopes k(d) = -dlog|y|/dd.

    For log|y| = c - k d - p log d one has k(d) = k + p/d, so the local slope
    decreases monotonically to the true exponent k.  This is prefactor-free
    evidence for the asymptotic exponent.
    """
    ly = np.log(np.abs(y))
    kk = -(ly[1:] - ly[:-1]) / (d[1:] - d[:-1])
    dm = 0.5 * (d[1:] + d[:-1])
    return dm, kk


if __name__ == "__main__":
    print("=" * 78)
    print("M2: which mass sets the rate at which omega_g -> omega_infty ?")
    print("=" * 78)

    d, yphi, ypi = run()
    report(d, yphi, ypi)

    print("\n  === prefactor powers (fitting |y| ~ d^{-p} e^{-2 m1 d}) ===")
    for name, y, ppred in (("Delta_phi", yphi, 0.5), ("Delta_pi", ypi, 1.5)):
        p = prefactor_test(d, y, 2 * M1)
        print(f"    {name}: p = {p:6.3f}   (predicted {ppred})")

    print("\n  === joint fit  log|y| = c - k d - p log d  (k and p together) ===")
    for name, y, ppred in (("Delta_phi", yphi, 0.5), ("Delta_pi", ypi, 1.5)):
        k, p, r = joint_fit(d, y)
        print(f"    {name}: k = {k:7.4f}  (2*m1 = {2*M1:.4f}),   "
              f"p = {p:6.3f}  (predicted {ppred}),   maxresid {r:.2e}")

    print("\n  === local slopes k(d) = -dlog|y|/dd  ->  should decrease to 2*m1 ===")
    for name, y in (("Delta_phi", yphi), ("Delta_pi", ypi)):
        dm, kk = local_slopes(d, y)
        print(f"    {name}:")
        print("      d    " + "".join(f"{v:8.2f}" for v in dm))
        print("      k(d) " + "".join(f"{v:8.3f}" for v in kk))
        print(f"      last k(d) = {kk[-1]:.3f};  extrapolated k(d)-p/d with p from joint "
              f"fit = {kk[-1] - joint_fit(d, y)[1]/dm[-1]:.3f}")

    print("\n  === discretisation check: refine h ===")
    d2, yphi2, ypi2 = run(L=25.0, h=0.0166, ells=np.arange(1.0, 3.51, 0.5))
    s2, _, _ = fit_slope(d2, yphi2, 0.5)
    print(f"\n    Delta_phi exponent at h=0.0125 : {-s2:.4f}   (2*m1 = {2*M1:.4f})")

    print("\n  === sign check (mu_g <= mu_1 forces Delta_phi>=0, Delta_pi<=0) ===")
    print(f"    Delta_phi all >= 0 : {bool(np.all(yphi >= 0))}")
    print(f"    Delta_pi  all <= 0 : {bool(np.all(ypi <= 0))}")
