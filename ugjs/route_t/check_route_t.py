#!/usr/bin/env python3
"""Numerical corroboration of the elementary identities and inequalities of the
Route T note (ugjs/route_t/route_t.tex).  NUMERICAL ONLY: nothing in the note is deduced
from this script; every statement it touches is proved in the note by hand.

Run:  python3 check_route_t.py   (system python3; run of 23 November 2026: Python 3.14.7)
Every tolerance used is printed.  Seeds are fixed and printed.
"""
import sys
import math
import numpy as np
import scipy
from scipy import integrate, special
import mpmath as mp

mp.mp.dps = 40
SEED = 20261123
rng = np.random.default_rng(SEED)

print("python", sys.version.split()[0], "| numpy", np.__version__,
      "| scipy", scipy.__version__, "| mpmath", mp.__version__)
print("seed", SEED)
fails = []


def report(name, ok, detail):
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)
    if not ok:
        fails.append(name)


# ---------------------------------------------------------------------------
# 1. k(E) = int int_{[-1/2,1/2]^2} e^{-|t-t'|E} = 2(E-1+e^{-E})/E^2   (Lemma T.9)
TOL1 = 1e-12
worst = 0.0
for E in [1e-6, 1e-3, 0.1, 0.5, 1.0, 2.0, 5.0, 20.0, 100.0]:
    E = mp.mpf(E)  # all arithmetic in 40-digit precision (a float E - 1 cancels catastrophically)
    num = mp.quad(lambda u: 2 * (1 - u) * mp.e ** (-u * E), [0, 1])  # = int_{-1}^1 (1-|u|) e^{-|u|E}
    # iterated integral over the square, inner integral split at the kink s = t
    dbl = mp.quad(lambda t: mp.quad(lambda s: mp.e ** (-abs(s - t) * E), [-0.5, t, 0.5]), [-0.5, 0.5])
    closed = 2 * (E - 1 + mp.e ** (-E)) / E ** 2
    worst = max(worst, float(abs(num - closed) / closed), float(abs(dbl - closed) / closed))
report("k(E) closed form", worst < TOL1, "max rel. error %.2e (tolerance %.0e)" % (worst, TOL1))

# ---------------------------------------------------------------------------
# 2. (lambda0^2+E^2)^{-1} <= c_k k(E), lambda0 >= 1, E >= 0; k nonincreasing (Lemma T.9)
c_k = 2 / (1 + math.exp(-2))
Es = np.concatenate([np.linspace(0, 10, 200001), np.linspace(10, 1e4, 200001)])
Esafe = np.where(Es == 0, 1.0, Es)
kE = np.where(Es < 1e-4, 1 - Es / 3 + Es ** 2 / 12,
              2 * (Esafe - 1 + np.exp(-Esafe)) / Esafe ** 2)
minmargin = np.inf
for lam0 in [1.0, 1.0001, 1.5, 3.0, 10.0]:
    lhs = 1 / (lam0 ** 2 + Es ** 2)
    minmargin = min(minmargin, np.min(c_k * kE - lhs))
mono = np.all(np.diff(kE) <= 1e-15)
report("inequality (T.9)", minmargin >= 0,
       "c_k=%.12f, min over grid of c_k k(E)-(lam0^2+E^2)^-1 = %.3e (must be >= 0)" % (c_k, minmargin))
report("k nonincreasing on grid", bool(mono), "max increment %.2e (tolerance 1e-15)" % np.max(np.diff(kE)))
print("     k(2) =", 2 * (2 - 1 + math.exp(-2)) / 4, " 1/c_k =", 1 / c_k)

# ---------------------------------------------------------------------------
# 3. transform of f_{a,eps}(t) = (2 pi i)^{-1} e^{-t^2/(2a)}/(t - i eps)       (Lemma T.3)
TOL3 = 1e-9
worst = 0.0
for (a, eps, E) in [(1.0, 0.3, 0.7), (2.0, 0.05, -0.4), (0.5, 1.0, 2.0), (3.0, 0.2, 0.0)]:
    def re_int(t):
        z = mp.e ** (-t ** 2 / (2 * a)) / (t - 1j * eps) / (2j * mp.pi) * mp.e ** (1j * t * E)
        return z
    num = mp.quad(re_int, [-mp.inf, -1, 0, 1, mp.inf])
    closed = mp.sqrt(a / (2 * mp.pi)) * mp.quad(lambda Ep: mp.e ** (-a * (E - Ep) ** 2 / 2 - eps * Ep), [0, mp.inf])
    worst = max(worst, float(abs(num - closed)))
report("transform of f_{a,eps}", worst < TOL3, "max abs. error %.2e (tolerance %.0e)" % (worst, TOL3))

# ---------------------------------------------------------------------------
# 4. principal-value limit:  int_{-R'}^{R'} f_{a,eps}(t) e^{-lam0 t} dt -> 1/2 + (i/pi) J,
#    J = int_0^{R'} e^{-t^2/(2a)} sinh(lam0 t)/t dt                              (Lemma T.3)
for (a, lam0, Rp) in [(2.0, 1.0, 3.0), (5.0, 1.0, 5.0), (1.0, 2.0, 1.5)]:
    J = mp.quad(lambda t: mp.e ** (-t ** 2 / (2 * a)) * mp.sinh(lam0 * t) / t, [0, Rp])
    target = mp.mpf(1) / 2 + 1j * J / mp.pi
    errs = []
    for eps in [1e-2, 1e-3, 1e-4]:
        val = mp.quad(lambda t: mp.e ** (-t ** 2 / (2 * a)) * mp.e ** (-lam0 * t) / (t - 1j * eps) / (2j * mp.pi),
                      [-Rp, -10 * eps, 0, 10 * eps, Rp])
        errs.append(float(abs(val - target)))
    ok = errs[-1] < 2e-3 and errs[0] > errs[1] > errs[2]
    report("PV limit (a=%g, lam0=%g, R'=%g)" % (a, lam0, Rp), ok,
           "|I_eps - (1/2 + iJ/pi)| for eps=1e-2,1e-3,1e-4: %s (require decreasing, last < 2e-3)"
           % ", ".join("%.2e" % e for e in errs))
    # the bound J <= sinh(lam0 R') and J <= lam0 R' cosh(lam0 R')
    report("J bounds", float(J) <= math.sinh(lam0 * Rp) and float(J) <= lam0 * Rp * math.cosh(lam0 * Rp),
           "J=%.6g sinh=%.6g x cosh x=%.6g" % (float(J), math.sinh(lam0 * Rp), lam0 * Rp * math.cosh(lam0 * Rp)))

# ---------------------------------------------------------------------------
# 5. Gaussian tail 1 - Phi(x) <= exp(-x^2/2)/2 for x >= 0                       (Lemma T.3)
xs = np.linspace(0, 40, 400001)
tail = 0.5 * special.erfc(xs / math.sqrt(2))
margin = np.min(0.5 * np.exp(-xs ** 2 / 2) - tail)
report("Gaussian tail", margin >= -1e-300, "min of e^{-x^2/2}/2 - (1-Phi(x)) on [0,40] = %.3e" % margin)

# 6. int_0^x sinh(u)/u du <= sinh(x)                                              (Lemma T.3)
worst = -np.inf
for x in [1e-3, 0.1, 1, 3, 10, 30]:
    lhs = float(mp.quad(lambda u: mp.sinh(u) / u, [0, x]))
    worst = max(worst, lhs - math.sinh(x))
report("int sinh(u)/u <= sinh", worst <= 0, "max of lhs - sinh(x) = %.3e" % worst)

# ---------------------------------------------------------------------------
# 7. resolvent transform and identity (b) for random discrete measures         (Lemmas T.1, T.5)
gamma = 0.7
lam0 = 1.3
TOL7 = 1e-10
Ek = gamma + rng.exponential(2.0, size=12)
wk = rng.normal(size=12) + 1j * rng.normal(size=12)
F = lambda s: np.sum(wk * np.exp(1j * s * Ek))
Ft_closed = lambda t: np.sum(wk / (lam0 + 1j * Ek) * np.exp(1j * t * Ek))
worst = 0.0
for t in [-1.0, 0.0, 0.8, 2.5]:
    re = integrate.quad(lambda s: math.exp(-lam0 * (t - s)) * F(s).real, -np.inf, t, limit=400, epsabs=1e-13, epsrel=1e-13)[0]
    im = integrate.quad(lambda s: math.exp(-lam0 * (t - s)) * F(s).imag, -np.inf, t, limit=400, epsabs=1e-13, epsrel=1e-13)[0]
    worst = max(worst, abs(re + 1j * im - Ft_closed(t)))
report("F~(t) = int_{-inf}^t e^{-lam0(t-s)}F(s) ds", worst < 1e-7, "max abs. error %.2e (tolerance 1e-7; quad epsabs=epsrel=1e-13)" % worst)
lhs = np.sum(wk / Ek)
rhs = 1j * np.sum(wk / (lam0 + 1j * Ek)) + lam0 * np.sum(wk / (lam0 + 1j * Ek) / Ek)
report("identity (b): int E^-1 drho = i F~(0) + lam0 int E^-1 drho~", abs(lhs - rhs) < TOL7,
       "abs. error %.2e (tolerance %.0e)" % (abs(lhs - rhs), TOL7))

# ---------------------------------------------------------------------------
# 8. locality discrepancy: F = G on (-R,R) => F~ - G~ = c e^{-lam0 t} on (-R,R), |c| <= 2 m e^{-lam0 R}
R = 2.0
lam0 = 1.0
Dfun = lambda s: (math.cos(3 * s) + 0.5 * math.sin(s)) * (1 if abs(s) >= R else 0) * math.exp(-0.1 * abs(s))
Gfun = lambda s: math.sin(2 * s) / (1 + s * s)
Ffun = lambda s: Gfun(s) + Dfun(s)
def tilde(fun, t):
    pts = [p for p in (-R, R) if p < t]
    return integrate.quad(lambda s: math.exp(-lam0 * (t - s)) * fun(s), -60, t, points=pts or None, limit=800,
                          epsabs=1e-12, epsrel=1e-12)[0]
c = integrate.quad(lambda s: math.exp(lam0 * s) * Dfun(s), -60, -R, limit=800, epsabs=1e-13, epsrel=1e-13)[0]
worst = 0.0
for t in np.linspace(-R + 0.05, R - 0.05, 9):
    worst = max(worst, abs(tilde(Ffun, t) - tilde(Gfun, t) - c * math.exp(-lam0 * t)))
ts = np.linspace(-40, 40, 4001)
mbound = max(max(abs(tilde(Ffun, t)) for t in ts[::50]), max(abs(tilde(Gfun, t)) for t in ts[::50]))
report("discrepancy c e^{-lam0 t}", worst < 1e-8, "max abs. error %.2e (tolerance 1e-8)" % worst)
report("|c| <= 2 m~ e^{-lam0 R}", abs(c) <= 2 * mbound * math.exp(-lam0 * R),
       "|c|=%.4e, 2 m~ e^{-lam0 R}=%.4e (m~ estimated on a grid of 81 points)" % (abs(c), 2 * mbound * math.exp(-lam0 * R)))

# ---------------------------------------------------------------------------
# 9. tail of the separator: int_{|t|>=R'} |f_{a,eps}| <= (a/(pi R'^2)) e^{-R'^2/(2a)}
worst = -np.inf
for (a, eps, Rp) in [(1.0, 0.1, 1.0), (2.0, 1e-3, 3.0), (0.3, 0.5, 0.5)]:
    val = 2 * integrate.quad(lambda t: math.exp(-t * t / (2 * a)) / abs(t - 1j * eps) / (2 * math.pi), Rp, np.inf)[0]
    bound = a / (math.pi * Rp ** 2) * math.exp(-Rp ** 2 / (2 * a))
    worst = max(worst, val - bound)
report("separator tail", worst <= 0, "max of value - bound = %.3e" % worst)

# ---------------------------------------------------------------------------
# 10. shell count: #{j in Z : j in [b+n-1, b+n+2)} <= 3
worst = 0
for _ in range(100000):
    x = rng.uniform(-50, 50)
    cnt = sum(1 for j in range(math.floor(x) - 3, math.floor(x) + 5) if x - 1 <= j < x + 2)
    worst = max(worst, cnt)
report("at most 3 integers in a half-open interval of length 3", worst <= 3, "max count %d over 1e5 random left ends" % worst)

# ---------------------------------------------------------------------------
# 11. Xi(R) nonincreasing, Xi(R) = (1+4/(pi g R)) e^{-g R/4} + (1+1/pi) e^{-lam0 R/2}
def Xi(Rr, g, l0):
    return (1 + 4 / (math.pi * g * Rr)) * math.exp(-g * Rr / 4) + (1 + 1 / math.pi) * math.exp(-l0 * Rr / 2)
ok = True
for g in [0.05, 0.5, 2.0, 10.0]:
    for l0 in [1.0, 3.0]:
        vals = [Xi(r, g, l0) for r in np.linspace(0.01, 200, 20001)]
        ok = ok and all(vals[i + 1] <= vals[i] + 1e-15 for i in range(len(vals) - 1))
report("Xi nonincreasing", ok, "grid R in [0.01,200], gamma in {0.05,0.5,2,10}, lam0 in {1,3}")

# ---------------------------------------------------------------------------
# 12. slicing norm inequality: int ||w(t,.)||_2 dt <= ||w||_{L^2} on a unit time interval
worst = -np.inf
for _ in range(200):
    W = rng.normal(size=(40, 40)) * (rng.uniform(size=(40, 40)) < 0.5)
    dt = dx = 1 / 40
    lhs = np.sum(np.sqrt(np.sum(W ** 2, axis=1) * dx)) * dt
    rhs = math.sqrt(np.sum(W ** 2) * dt * dx)
    worst = max(worst, lhs - rhs)
report("int ||w(t,.)|| dt <= ||w||", worst <= 1e-12, "max of lhs - rhs = %.3e over 200 random step kernels" % worst)

# ---------------------------------------------------------------------------
# 13. free-field check, degree 1: E[Vbar^2] <= E[V^2]  (V = phi_0(h), Vbar = int_{-1/2}^{1/2} J_tau V)
#     E[Vbar^2] = int dk/(2pi) |h^(k)|^2 k(mu(k))/(2 mu(k)),  E[V^2] = int dk/(2pi) |h^(k)|^2/(2 mu(k))
m0 = 1.0
def hhat(kk):  # h = indicator of [0,2]
    return 2.0 if abs(kk) < 1e-12 else (1 - np.exp(-2j * kk)) / (1j * kk)
def kfun(E):
    return 1 - E / 3 + E * E / 12 if E < 1e-4 else 2 * (E - 1 + math.exp(-E)) / E ** 2
mu = lambda kk: math.sqrt(kk * kk + m0 * m0)
Ebar = integrate.quad(lambda kk: abs(hhat(kk)) ** 2 * kfun(mu(kk)) / (2 * mu(kk)) / (2 * math.pi), -np.inf, np.inf, limit=2000)[0]
Efull = integrate.quad(lambda kk: abs(hhat(kk)) ** 2 / (2 * mu(kk)) / (2 * math.pi), -np.inf, np.inf, limit=2000)[0]
report("free field, n=1: E[Vbar^2] <= E[V^2]", Ebar <= Efull, "E[Vbar^2]=%.6f, E[V^2]=%.6f (m0=1, h=1_[0,2])" % (Ebar, Efull))

# ---------------------------------------------------------------------------
# 14. (added in the revision) the truncation limit of Lemma T.15(ii), Step 2, in a Gaussian toy:
#     Y1, Y2 standard normal with correlation rho; X_i = Y_i^2 - 1 (a Wick square);
#     E[c_l(X1) c_l(X2)] -> E[X1 X2] = 2 rho^2 as l -> infinity, c_l = clipping at +-l.
#     Computed with the Mehler expansion E[f(Y1)f(Y2)] = sum_n rho^n (E[f(Y) h_n(Y)])^2, with the
#     normalized Hermite polynomials h_n = He_n/sqrt(n!) (stable three-term recurrence), and
#     Gauss-Legendre quadrature (400 nodes per piece) between the kinks of the clipping.
NMEHLER = 120
TOL14 = 1e-6
def mehler_value(fun, kinks, rho):
    pts = sorted(set([-14.0, 0.0, 14.0] + [k for k in kinks if -14 < k < 14]))
    xg, wg = np.polynomial.legendre.leggauss(400)
    ys, ws = [], []
    for a_, b_ in zip(pts[:-1], pts[1:]):
        ys.append(0.5 * (b_ - a_) * xg + 0.5 * (b_ + a_))
        ws.append(0.5 * (b_ - a_) * wg)
    y = np.concatenate(ys)
    w = np.concatenate(ws) * np.exp(-y * y / 2) / math.sqrt(2 * math.pi)
    fy = np.array([fun(t) for t in y])
    h_prev = np.zeros_like(y)
    h = np.ones_like(y)
    total = 0.0
    for n in range(NMEHLER + 1):
        cn = float(np.sum(w * fy * h))
        total += rho ** n * cn * cn
        h_next = (y * h - math.sqrt(n) * h_prev) / math.sqrt(n + 1)
        h_prev, h = h, h_next
    return total
ok14 = True
lines14 = []
for rho in [0.3, 0.7, 0.9]:
    errs = []
    for ell in [0.5, 2.0, 8.0, 32.0, 64.0]:
        clip = lambda t, ell=ell: max(-ell, min(ell, t * t - 1.0))
        r = math.sqrt(1.0 + ell)
        errs.append(abs(mehler_value(clip, [-r, r], rho) - 2 * rho * rho))
    ok14 = ok14 and all(errs[i + 1] <= errs[i] + 1e-12 for i in range(len(errs) - 1)) and errs[-1] < TOL14
    lines14.append("rho=%.1f: %s" % (rho, ", ".join("%.2e" % e for e in errs)))
# sanity check of the expansion on the unclipped Wick square (exact value 2 rho^2)
sanity = max(abs(mehler_value(lambda t: t * t - 1.0, [], rho) - 2 * rho * rho) for rho in [0.3, 0.7, 0.9])
ok14 = ok14 and sanity < 1e-10
report("truncation limit (T.15(ii), Step 2), Gaussian toy", ok14,
       "|E[c_l(X1)c_l(X2)] - 2rho^2| for l = 0.5, 2, 8, 32, 64: " + "; ".join(lines14)
       + " (require nonincreasing in l, last < %.0e; Mehler terms n <= %d; unclipped sanity error %.1e, tolerance 1e-10)"
       % (TOL14, NMEHLER, sanity))

# ---------------------------------------------------------------------------
# 15. (added in the revision) the two-time formula of Lemma T.15(ii) in the free case (lambda = 0):
#     E_mu0[Phi(tau,f) Phi(tau',f)] = int int f(x) f(y) G((u, x-y)) dx dy, G(z) = K_0(m0|z|)/(2 pi),
#     equals <phi_0(f) Omega_0, e^{-u H_0} phi_0(f) Omega_0> = (1/2pi) int |f^(k)|^2 e^{-u mu(k)}/(2 mu(k)) dk,
#     u = tau' - tau > 0, f = indicator of [0,1], m0 = 1.
TOL15 = 1e-8
worst = 0.0
details = []
for u in [0.3, 1.0, 2.5]:
    pos = integrate.quad(lambda v: (1 - abs(v)) * special.k0(m0 * math.sqrt(u * u + v * v)) / (2 * math.pi),
                         -1, 1, points=[0.0], limit=400, epsabs=1e-14, epsrel=1e-12)[0]
    mom = integrate.quad(lambda kk: (1.0 if abs(kk) < 1e-12 else 4 * math.sin(kk / 2) ** 2 / kk ** 2)
                         * math.exp(-u * mu(kk)) / (2 * mu(kk)) / (2 * math.pi), -np.inf, np.inf,
                         limit=2000, epsabs=1e-14, epsrel=1e-12)[0]
    worst = max(worst, abs(pos - mom) / abs(mom))
    details.append("u=%.1f: %.10f vs %.10f" % (u, pos, mom))
report("free two-time formula (T.15(ii) at lambda=0)", worst < TOL15,
       "; ".join(details) + "; max rel. difference %.2e (tolerance %.0e)" % (worst, TOL15))

print()
print("ALL CHECKS PASSED" if not fails else "FAILED: " + ", ".join(fails))
