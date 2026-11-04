#!/usr/bin/env python3
"""aqft_checks.py -- corroborating checks for parts d2.tex, d3.tex, d4.tex, consequences.tex
(aqft, 2 November 2026).  Status of every output: NUMERICAL (or exact integer arithmetic where
stated); nothing in the note is deduced from it.  Standard library only.

Checks
 1. Ring count around the 3x5 box (Lemma aux:notation-rings(ii)): #{m(Delta)=M} = 8M+4, brute force.
 2. Strip assignment (Step 3 of the proof of Theorem D.4): the assigned strip separates, width m-1;
    for rows -1,0,1 no horizontal strip of positive width separates; the widest strip
    (grid over directions) is >= m-1.
 3. Closed forms: sum_{k>=1}(8k+12)x^k = 4x(5-3x)/(1-x)^2 and 2*sum_{j>=1} x^j = 2x/(1-x).
 4. Exact integers: (4n-1)!! = (4n)!/(2^{2n}(2n)!) and (4n-1)!! <= 4^n ((2n)!)^2, n=1..40.
 5. Corollary 5.2 arithmetic: 9*8! = 362880, 24*362880 = 8709120.
 6. The cell-count counterexample (Remark aux:d3-cells): I=(0.4,0.6); cells [j,j+1) vs columns
    [k-1/2,k+1/2); column-decomposition norm of Phi(s,f)^2 (K1=K2=1) for a bump even about 1/2.
"""
import math, fractions, sys, platform

TOL = 1e-9
print("interpreter:", sys.executable, platform.python_version())
print("tolerance for float comparisons:", TOL)

# ---------- 1. ring count ----------
def cdist(k, ka):  # column distance from {ka, ka+1, ka+2}
    return max(ka - k, k - ka - 2, 0)

ka = 0
for M in range(1, 11):
    cnt = sum(1 for l in range(-M - 2, M + 3) for k in range(ka - M - 3, ka + M + 6)
              if max(abs(l), cdist(k, ka)) == M)
    assert cnt == 8 * M + 4, (M, cnt)
print("1. ring count 8M+4 verified for M=1..10 (exact)")
ring1 = [(l, k) for l in range(-4, 5) for k in range(ka - 5, ka + 8) if max(abs(l), cdist(k, ka)) == 2]
P = [(l, k) for (l, k) in ring1 if abs(l) >= cdist(k, ka)]
T = [(l, k) for (l, k) in ring1 if cdist(k, ka) > abs(l)]
print("   ring 1:", len(ring1), "squares;", len(P), "of class (P),", len(T), "of class (T)")
assert (len(ring1), len(P), len(T)) == (20, 14, 6)

# ---------- 2. strips ----------
def corners(l, k):  # closed square [l-1/2,l+1/2]x[k-1/2,k+1/2], points (x0,x1)
    return [(l + a, k + b) for a in (-0.5, 0.5) for b in (-0.5, 0.5)]

R = [c for k in (ka, ka + 1, ka + 2) for c in corners(0, k)]

def width(nu, X, Y):  # widest strip with normal nu, X below, Y above (support functions)
    a = max(nu[0] * x[0] + nu[1] * x[1] for x in X)
    b = min(nu[0] * y[0] + nu[1] * y[1] for y in Y)
    return b - a

def widest(X, Y, n=7200):
    best = -1e9
    for i in range(n):
        th = 2 * math.pi * i / n
        nu = (math.cos(th), math.sin(th))
        best = max(best, width(nu, X, Y))
    return best

checked = 0
for l in range(-5, 6):
    for k in range(ka - 6, ka + 9):
        m = max(abs(l), cdist(k, ka))
        if m < 2:
            continue
        D = corners(l, k)
        if abs(l) >= cdist(k, ka):  # (P): horizontal strip
            nu = (1.0, 0.0) if l > 0 else (-1.0, 0.0)
            w = width(nu, R, D)
        else:                        # (T): vertical strip
            nu = (0.0, 1.0) if k > ka + 2 else (0.0, -1.0)
            w = width(nu, R, D)
        assert abs(w - (m - 1)) < TOL, (l, k, w, m)
        if abs(l) <= 1:  # no horizontal strip of positive width
            assert max(width((1.0, 0.0), R, D), width((-1.0, 0.0), R, D)) <= TOL
        assert widest(R, D) >= (m - 1) - TOL
        checked += 1
print("2. strip assignment: width m-1 and separation verified for", checked,
      "squares (|l|<=5, window of 15 columns); widest strip >= m-1 (7200 directions)")

# ---------- 3. closed forms ----------
for x in (0.05, 0.3, 0.5, 0.9):
    s1 = sum((8 * k + 12) * x ** k for k in range(1, 4000))
    c1 = 4 * x * (5 - 3 * x) / (1 - x) ** 2
    s2 = 2 * sum(x ** j for j in range(1, 4000))
    c2 = 2 * x / (1 - x)
    print("3. x=%.2f  ring sum %.12g  closed %.12g  |diff| %.1e ;  D.3 sum %.12g closed %.12g"
          % (x, s1, c1, abs(s1 - c1), s2, c2))
    assert abs(s1 - c1) < TOL * max(1, c1) and abs(s2 - c2) < TOL * max(1, c2)

# ---------- 4. exact integers ----------
def dfact(n):
    r = 1
    while n > 1:
        r *= n
        n -= 2
    return r

for n in range(1, 41):
    d = dfact(4 * n - 1)
    assert d * 2 ** (2 * n) * math.factorial(2 * n) == math.factorial(4 * n)
    assert d <= 4 ** n * math.factorial(2 * n) ** 2
print("4. (4n-1)!! identity and (4n-1)!! <= 4^n((2n)!)^2 verified for n=1..40 (exact integers);",
      "n=1: 3 <= 16, n=2: 105 <= 2304")

# ---------- 5. Corollary 5.2 arithmetic ----------
assert 9 * math.factorial(8) == 362880 and 24 * 362880 == 8709120
print("5. 9*8! = 362880 and 24*362880 = 8709120 (exact)")

# ---------- 6. cell count counterexample ----------
I = (0.4, 0.6)
cells = [j for j in range(-3, 4) if min(I[1], j + 1) - max(I[0], j) > 0]
cols = [k for k in range(-3, 4) if min(I[1], k + 0.5) - max(I[0], k - 0.5) > 0]
print("6. I=(0.4,0.6): cells", cells, "-> N_I =", len(cells), "; columns", cols, "-> N_I^col =", len(cols))
assert len(cells) == 1 and len(cols) == 2

def bump(x):  # even about 1/2, supported in (0.4, 0.6)
    u = (x - 0.5) / 0.1
    return math.exp(-1.0 / (1 - u * u)) if abs(u) < 1 else 0.0

N = 200000
h = 0.2 / N
xs = [0.4 + (i + 0.5) * h for i in range(N)]
m0 = sum(bump(x) ** 2 for x in xs if x < 0.5) * h
m1 = sum(bump(x) ** 2 for x in xs if x >= 0.5) * h
tot = m0 + m1
f0, f1 = math.sqrt(m0 / tot), math.sqrt(m1 / tot)  # ||f 1_col||_2 after normalising ||f||_2 = 1
norm = 2 * f0 * f0 + 2 * f1 * f1 + 2 * f0 * f1      # K1=K2=1: (0,0),(1,1) weight 2!; (0,1),(1,0) weight 1
print("   column masses %.9f %.9f ; column-decomposition norm of Phi(f)^2 = %.9f ; record's n(Q)^2 = %d"
      % (f0 ** 2, f1 ** 2, norm, 2 * len(cells)))
assert abs(norm - 3) < 1e-6
print("all checks passed")
