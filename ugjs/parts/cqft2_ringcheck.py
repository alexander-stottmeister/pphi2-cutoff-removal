#!/usr/bin/env python3
"""cqft2_ringcheck.py -- NUMERICAL checks for parts/notation.tex and parts/constants.tex
(comparison note, Phases A/B of ugjs/PLAN.md).  Drafter: cqft2, 2 November 2026.
Nothing in the note is deduced from this script; it corroborates hand computations only.

Checks:
 1. ring count |L_j| = 8j+12 around B_3x5(a), strip widths >= j, orientation facts;
 2. columns meeting [a,a+2]: exactly 3 set-theoretically, 2 or 3 in positive measure;
 3. closed form sum_{j>=1}(8j+12)x^j = 4x(5-3x)/(1-x)^2: power-series coefficients (exact integers)
    and partial sums (exact rationals);
 4. N_I (cells [j,j+1)) versus N_I^sq (columns [k-1/2,k+1/2)) on two intervals;
 5. kernel C(u) = (4 pi)^{-1} int_0^inf t^{-1} exp(-t m0^2 - u^2/(4t)) dt: compare with
    K_0(m0|u|)/(2 pi) and with the bound (4 pi)^{-1}(b0 + 2|log|u||), b0 = log4 + 1/e + m0^{-2};
 6. I_n = int_{-2}^{2} (2-|u|) C(u)^n du against the bound of Lemma aux:notation-kernel(iv);
 7. ((4n-1)!!)^{1/2} <= 2^n (2n)! (exact integers, squared form), n = 0..40;
 8. Theorem 7.7 polystrip: nothing numerical (pure algebra); skipped.
"""
import math, sys
from fractions import Fraction

def floor_half(a):  # k_a = floor(a + 1/2), exact for Fractions
    return math.floor(a + Fraction(1, 2))

ok = True
def check(cond, msg):
    global ok
    if not cond:
        ok = False
        print("FAIL:", msg)

# ---------- 1. rings ----------
def ring_data(a, jmax=12):
    ka = floor_half(a)
    S = [(0, k) for k in range(ka, ka + 3)]          # S_a, row 0, columns ka..ka+2
    W = jmax + 6
    for j in range(1, jmax + 1):
        ring = []
        for l in range(-W, W + 1):
            for k in range(ka - W, ka + W + 1):
                delta = max(abs(l) - 1, ka - 1 - k, k - ka - 3)
                if delta == j:
                    ring.append((l, k))
        check(len(ring) == 8 * j + 12, f"a={a} j={j}: |L_j|={len(ring)} != {8*j+12}")
        for (l, k) in ring:
            rho_t = abs(l)                            # rows l1=l2=0
            rho_x = max(ka - k, 0, k - (ka + 2))
            m = max(rho_t, rho_x)
            check(m - 1 >= j, f"a={a} j={j} square {(l,k)}: m-1={m-1} < j")
            par_width = rho_t - 1                     # widest parallel strip vs row-0 squares
            if abs(l) <= 1:
                check(par_width <= 0, f"rows -1,0,1 square {(l,k)} has parallel width {par_width}>0")
            if abs(l) <= j:                           # side squares: parallel width <= j-1
                check(par_width <= j - 1, f"side square {(l,k)} parallel width {par_width} > j-1")
                check(k in (ka - 1 - j, ka + 3 + j), f"side square {(l,k)} not in a side column")
        if j == 1:
            listed = sorted(ring)
            expect = sorted([(2, k) for k in range(ka - 2, ka + 5)] + [(-2, k) for k in range(ka - 2, ka + 5)]
                            + [(l, ka - 2) for l in (-1, 0, 1)] + [(l, ka + 4) for l in (-1, 0, 1)])
            check(listed == expect, f"a={a}: ring 1 list differs")
    return True

test_a = [Fraction(0), Fraction(1, 2), Fraction(-1, 2), Fraction(7, 3), Fraction(-13, 10),
          Fraction(3, 2), Fraction(100, 7), Fraction(-5, 2)]
for a in test_a:
    ring_data(a)
print("1. ring count and strip widths: checked for a in", [str(a) for a in test_a], "j=1..12")

# ---------- 2. columns meeting [a, a+2] ----------
for a in test_a:
    ka = floor_half(a)
    meet = [k for k in range(ka - 5, ka + 8)
            if (Fraction(2*k - 1, 2) <= a + 2) and (Fraction(2*k + 1, 2) > a)]
    pos = [k for k in range(ka - 5, ka + 8)
           if min(a + 2, Fraction(2*k + 1, 2)) - max(a, Fraction(2*k - 1, 2)) > 0]
    check(meet == [ka, ka + 1, ka + 2], f"a={a}: columns meeting [a,a+2] = {meet}")
    check(set(pos) <= set(meet) and len(pos) in (2, 3), f"a={a}: positive-measure columns = {pos}")
    print(f"2. a={str(a):>6}: k_a={ka}, meeting={meet}, positive measure={pos}")

# ---------- 3. closed form ----------
# coefficients of 4x(5-3x)/(1-x)^2 = (20x - 12x^2) * sum_{i>=0} (i+1) x^i
N = 60
coef = [0] * (N + 3)
for i in range(N + 1):
    coef[i + 1] += 20 * (i + 1)
    coef[i + 2] += -12 * (i + 1)
check(all(coef[j] == 8 * j + 12 for j in range(1, N + 1)), "series coefficients differ from 8j+12")
for x in (Fraction(1, 2), Fraction(1, 3), Fraction(2, 7), Fraction(9, 10)):
    closed = 4 * x * (5 - 3 * x) / (1 - x) ** 2
    partial = sum((8 * j + 12) * x ** j for j in range(1, 400))
    tail_ok = partial <= closed and closed - partial < Fraction(1, 10**6)
    check(tail_ok, f"x={x}: partial sum {float(partial)} vs closed {float(closed)}")
    print(f"3. x={x}: closed form {closed} = {float(closed):.10f}; partial sum to j=399 differs by {float(closed - partial):.3e}")
print("3. series coefficients of the closed form equal 8j+12 for j=1..60 (exact)")

# ---------- 4. N_I vs N_I^sq ----------
def counts(lo, hi):
    lo, hi = Fraction(lo), Fraction(hi)
    cells = [j for j in range(-10, 10) if min(hi, j + 1) - max(lo, j) > 0]
    cols = [k for k in range(-10, 10) if min(hi, Fraction(2*k + 1, 2)) - max(lo, Fraction(2*k - 1, 2)) > 0]
    return len(cells), len(cols)
for (lo, hi) in ((Fraction(-1, 10), Fraction(1, 10)), (Fraction(4, 10), Fraction(6, 10))):
    nI, nsq = counts(lo, hi)
    print(f"4. I=({float(lo)},{float(hi)}): N_I={nI}, N_I^sq={nsq}")

# ---------- 5. kernel C and its bound ----------
try:
    import numpy as np
    from scipy import integrate, special
    def C_int(u, m0):
        f = lambda t: math.exp(-t * m0 * m0 - u * u / (4 * t)) / t
        # relative tolerances only (default epsabs=1.49e-8 is useless for tiny values);
        # split at the maximum of t*f(t), t* = |u|/(2 m0), and at decades around it
        tstar = abs(u) / (2 * m0)
        cuts = sorted({0.0, tstar / 100, tstar / 10, tstar, 10 * tstar, 100 * tstar})
        tot = 0.0
        for lo, hi in zip(cuts[:-1], cuts[1:]):
            v, _ = integrate.quad(f, lo, hi, epsabs=0, epsrel=1e-11, limit=500)
            tot += v
        v, _ = integrate.quad(f, cuts[-1], np.inf, epsabs=0, epsrel=1e-11, limit=500)
        return (tot + v) / (4 * math.pi)
    worst = 0.0
    for m0 in (0.5, 1.0, 2.0):
        b0 = math.log(4) + math.exp(-1) + m0 ** -2
        for u in (1e-4, 1e-2, 0.1, 0.5, 0.99, 1.0, 1.5, 3.0, 10.0):
            c1 = C_int(u, m0)
            c2 = special.k0(m0 * u) / (2 * math.pi)
            bound = (b0 + 2 * abs(math.log(u))) / (4 * math.pi)
            worst = max(worst, abs(c1 - c2) / c2)
            print(f"   m0={m0} u={u}: t-integral {c1:.12e}  K0/(2pi) {c2:.12e}  bound {bound:.6e}")
            check(c1 <= bound, f"C({u}) = {c1} > bound {bound} at m0={m0}")
    print(f"5. kernel: max relative difference between the t-integral and K0/(2pi): {worst:.2e}; bound holds on the grid")
    # ---------- 6. I_n ----------
    for m0 in (0.5, 1.0, 2.0):
        b0 = math.log(4) + math.exp(-1) + m0 ** -2
        for n in range(1, 5):
            g = lambda u: (2 - u) * (special.k0(m0 * u) / (2 * math.pi)) ** n
            val, err = integrate.quad(g, 0, 2, limit=400, points=[1e-8, 1e-4, 1e-2])
            In = 2 * val
            bnd = (4 * math.pi) ** (-n) * 2 ** (n + 1) * (2 * b0 ** n + 2 ** n * (math.factorial(n) + math.log(2) ** n))
            check(In <= bnd, f"I_{n}(m0={m0}) = {In} > bound {bnd}")
            print(f"6. m0={m0}, n={n}: I_n = {In:.6f} (quad err {err:.1e}), bound {bnd:.6f}")
    print("   versions:", sys.executable, sys.version.split()[0], "numpy", np.__version__, "scipy",
          __import__('scipy').__version__)
except ImportError as e:
    print("5./6. skipped:", e)

# ---------- 7. ((4n-1)!!)^{1/2} <= 2^n (2n)!  <=>  (4n-1)!! <= 4^n ((2n)!)^2 ----------
def dfact(k):
    r = 1
    while k > 1:
        r *= k; k -= 2
    return r
for n in range(0, 41):
    check(dfact(4 * n - 1) <= 4 ** n * math.factorial(2 * n) ** 2, f"moment inequality fails at n={n}")
    check(dfact(4 * n - 1) <= 4 ** n * math.factorial(2 * n), f"sharper form (4n-1)!! <= 4^n (2n)! fails at n={n}")
print("7. (4n-1)!! <= 4^n (2n)! <= 4^n ((2n)!)^2 for n = 0..40 (exact integers)")

print("ALL CHECKS PASSED" if ok else "SOME CHECK FAILED")
