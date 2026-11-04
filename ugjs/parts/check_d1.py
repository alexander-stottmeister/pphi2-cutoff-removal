"""mp, 2 November 2026. Checks for parts/d1.tex (labelled `numerical'; nothing is deduced from them).
(1) Lemma aux:d1-wick: E[prod_a :X_a^{m_a}:_{c_a}] = P_m(gamma), exact rational arithmetic,
    left side by Isserlis' theorem after expanding the Wick powers with eq. (d1-hermite).
(2) Lemma aux:d1-cov(ii): G(z) = (2 pi)^{-1} K_0(m0 |z|) <= M0(|z|) = g0 + (2 pi)^{-1} log_+(1/|z|),
    g0 = (4 + m0^{-2})/(4 pi); and the heat-kernel formula of (i), floating point.
(3) Remark aux:d1-check: the one-variable model, by quadrature.
"""
import itertools, math, random, sys
from fractions import Fraction as Fr
from functools import lru_cache

def hermite_coeffs(n, c):
    # :X^n:_c = sum_j n!/(j!(n-2j)!) (-c/2)^j X^{n-2j}
    return {n-2*j: Fr(math.factorial(n), math.factorial(j)*math.factorial(n-2*j))*(Fr(-c,2)**j)
            for j in range(n//2+1)}

def isserlis(idx, cov):
    # E[X_{i1}...X_{ik}] for centred jointly Gaussian X, idx a tuple of variable labels
    idx = list(idx)
    if len(idx) % 2: return Fr(0)
    @lru_cache(maxsize=None)
    def rec(t):
        if not t: return Fr(1)
        a, rest = t[0], t[1:]
        s = Fr(0)
        for k in range(len(rest)):
            s += cov[a][rest[k]]*rec(rest[:k]+rest[k+1:])
        return s
    return rec(tuple(idx))

def lhs(m, cov):
    l = len(m)
    expans = [hermite_coeffs(m[a], cov[a][a]) for a in range(l)]
    total = Fr(0)
    for choice in itertools.product(*[list(e.items()) for e in expans]):
        coef = Fr(1); idx = []
        for a, (power, cf) in enumerate(choice):
            coef *= cf; idx += [a]*power
        if coef: total += coef*isserlis(tuple(idx), cov)
    return total

def rhs(m, cov):
    l = len(m); pairs = [(a, b) for a in range(l) for b in range(a+1, l)]
    total = Fr(0)
    def families(i, rem):
        if i == len(pairs):
            if all(r == 0 for r in rem): yield {}
            return
        a, b = pairs[i]
        for k in range(min(rem[a], rem[b])+1):
            rem2 = list(rem); rem2[a] -= k; rem2[b] -= k
            for f in families(i+1, rem2):
                f2 = dict(f); f2[(a, b)] = k; yield f2
    for f in families(0, list(m)):
        term = Fr(1)
        for a in range(l): term *= math.factorial(m[a])
        for (a, b), k in f.items(): term *= cov[a][b]**k / math.factorial(k)
        total += term
    return total

random.seed(20261102)
cases = [(2,2), (3,3), (2,3), (2,2,2), (1,1,2), (3,1,2), (4,2,2), (1,1,1,1), (2,1,1), (2,2,1,1), (0,2,2), (3,3,2)]
ok = True
for m in cases:
    l = len(m)
    A = [[Fr(random.randint(-3, 3)) for _ in range(l+1)] for _ in range(l)]
    cov = [[sum(A[i][k]*A[j][k] for k in range(l+1)) for j in range(l)] for i in range(l)]
    L, R = lhs(m, cov), rhs(m, cov)
    ok &= (L == R)
    print(f"(1) m={m}: LHS={L}  RHS={R}  equal={L==R}")
print("(1) all equal:", ok)

import numpy as np, scipy
from scipy.special import k0
from scipy.integrate import quad
print("python", sys.version.split()[0], "numpy", np.__version__, "scipy", scipy.__version__)
worst = []
for m0 in [0.05, 0.1, 0.5, 1.0, 2.0, 10.0]:
    g0 = (4 + m0**-2)/(4*math.pi)
    r = np.logspace(-10, 3, 4001)
    G = k0(m0*r)/(2*math.pi)
    M0 = g0 + np.maximum(np.log(1/r), 0)/(2*math.pi)
    worst.append((m0, float(np.min(M0 - G))))
print("(2) min over the grid of M0 - G, per m0 (must be >= 0):", worst)
for m0, z in [(1.0, 0.3), (0.5, 2.0), (2.0, 0.01)]:
    val, err = quad(lambda s: math.exp(-z*z/(4*s) - m0*m0*s)/(4*math.pi*s), 0, np.inf, limit=200)
    print(f"(2) heat-kernel integral at m0={m0}, |z|={z}: {val:.12g} vs K0/(2pi) = {k0(m0*z)/(2*math.pi):.12g} (quad err {err:.1e})")
vals = []
for h in [0.0, 0.5, 1.0]:
    Z = quad(lambda x: math.exp(-(1+h)*x*x/2), -np.inf, np.inf)[0]
    E2 = quad(lambda x: x*x*math.exp(-(1+h)*x*x/2), -np.inf, np.inf)[0]/Z
    E4 = quad(lambda x: x**4*math.exp(-(1+h)*x*x/2), -np.inf, np.inf)[0]/Z
    vals.append((h, E2, 0.5*(E4 - E2*E2), (1+h)**-2))
print("(3) h, <X^2>_h, Cov_h(X^2, X^2/2), (1+h)^-2:", vals)
I = quad(lambda a: (1+a)**-2, 0, 1)[0]
print("(3) -int_0^1 (1+a)^-2 da =", -I, "; <F>_{h2}-<F>_{h1} =", vals[2][1]-vals[0][1])

# (4) quantifiers.tex, boundary case (8): rings around a 3x4 box (rows -1..1, columns 0..3);
#     ring j = squares at sup-index distance exactly j from the box; claim: 8j+10 squares, and an
#     axis-parallel strip of width >= j separates each from R, the row-0 squares of the two
#     middle columns 1..2 (the case a in 1/2+Z: R in two columns, box = R's columns +-1)
#     (integer arithmetic; strip widths as in Lemma aux:notation-strip: rho-1).
ok4 = True
for j in range(1, 13):
    ring = [(l, k) for l in range(-1-j, 2+j) for k in range(-j, 4+j)
            if max(max(abs(l)-1, 0), max(-k, 0, k-3)) == j]
    widths = []
    for (l, k) in ring:
        rho_t = abs(l)                          # row distance to row 0 (the row of R)
        rho_x = max(1 - k, 0, k - 2)            # column distance to columns 1..2 (the columns of R)
        widths.append(max(rho_t, rho_x) - 1)
    good = (len(ring) == 8*j + 10) and min(widths) >= j
    if not good: print("   j", j, "count", len(ring), "min width", min(widths))
    ok4 &= good
print("(4) 3x4-box rings: counts 8j+10 and widths >= j for j=1..12:", ok4)

# (5) quantifiers.tex, boundary case (1): rows l charged by [-T,T] (positive-measure overlap
#     with [l-1/2, l+1/2)) are exactly |l| < T + 1/2; exact rationals.
ok5 = True
for T in [Fr(1,10), Fr(1,2), Fr(3,4), Fr(1), Fr(3,2), Fr(17,10), Fr(5,2)]:
    rows = [l for l in range(-10, 11) if min(Fr(l)+Fr(1,2), T) - max(Fr(l)-Fr(1,2), -T) > 0]
    ok5 &= rows == [l for l in range(-10, 11) if abs(l) < T + Fr(1,2)]
print("(5) charged rows of the slab = {|l| < T+1/2} for 7 values of T:", ok5)
