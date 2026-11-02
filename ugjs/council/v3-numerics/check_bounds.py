# V3 audit, numerical corroboration only (AGENTS 3.9 / 6.1): nothing is deduced from these numbers.
# Checks the hand-derived bounds used in the V3 report:
#  (B0) G(r) = (1/2pi) K0(m r) equals the heat-kernel integral int_0^oo e^{-m^2 s} (4 pi s)^{-1} e^{-r^2/(4s)} ds
#  (B1) K0(x) <= (1+log4)(1+|log x|) e^{-x};  K0(x) <= (log(1/x))_+ + 1 + log 4;  K0(x) <= e^{-x}(log(4/x)+e^{-1}) for x<1
#  (B2) K1(x) <= (1+1/x) e^{-x}, and K1 = -K0'
#  (Cs) c_kappa <= (1/2pi) log kappa + C_* for the normalised disc indicator delta = 1_{|z|<=1}/pi (bounded; enough for the variance bound)
#  (AMGM) Lemma C.3 constant b(P) from the explicit Young-inequality constants, for sample polynomials
#  (HC) ||Y||_4 <= 3^{p'} ||Y||_2 on a one-dimensional Gaussian chaos of degree <= 2p' (sample Y)
import mpmath as mp, itertools, math, random, sys
mp.mp.dps = 30
print("python", sys.version.split()[0], "mpmath", mp.__version__, "dps", mp.mp.dps)
TOL = mp.mpf('1e-20'); print("tolerance for <= checks:", TOL)

# (B0)
for m, r in [(1, mp.mpf('0.01')), (1, mp.mpf('0.5')), (2, mp.mpf('1.3')), (mp.mpf('0.3'), mp.mpf('4'))]:
    hk = mp.quad(lambda s: mp.e**(-m**2*s) / (4*mp.pi*s) * mp.e**(-r**2/(4*s)), [0, r**2, 1, mp.inf])
    print("B0 m=%s r=%s heat-kernel=%s  K0/(2pi)=%s  diff=%s" % (m, r, mp.nstr(hk, 15), mp.nstr(mp.besselk(0, m*r)/(2*mp.pi), 15), mp.nstr(hk - mp.besselk(0, m*r)/(2*mp.pi), 3)))

# (B1),(B2) on a log grid
xs = [mp.mpf(10)**(k/mp.mpf(20)) for k in range(-200, 36)]  # 1e-10 .. ~63
worst = {"B1a": -mp.inf, "B1b": -mp.inf, "B1c": -mp.inf, "B2": -mp.inf, "deriv": mp.mpf(0)}
for x in xs:
    K0, K1 = mp.besselk(0, x), mp.besselk(1, x)
    worst["B1a"] = max(worst["B1a"], K0 - (1+mp.log(4))*(1+abs(mp.log(x)))*mp.e**(-x))
    worst["B1b"] = max(worst["B1b"], K0 - (max(mp.log(1/x), 0) + 1 + mp.log(4)))
    if x < 1: worst["B1c"] = max(worst["B1c"], K0 - mp.e**(-x)*(mp.log(4/x) + mp.e**(-1)))
    worst["B2"] = max(worst["B2"], K1 - (1+1/x)*mp.e**(-x))
    if x > mp.mpf('1e-6'): worst["deriv"] = max(worst["deriv"], abs(mp.diff(lambda y: mp.besselk(0, y), x) + K1))
for k, v in worst.items():
    print("%-6s max(lhs-rhs) over %d grid points = %s  -> %s" % (k, len(xs), mp.nstr(v, 6), "OK" if (v <= TOL if k != "deriv" else v < mp.mpf('1e-15')) else "FAIL"))

# (Cs) disc delta: hat(delta)(k) = 2 J1(|k|)/|k| (normalised so hat(delta)(0)=1); c_kappa = (1/2pi) int_0^oo hat(k/kappa)^2 k/(k^2+m^2) dk
def ckappa(kap, m):
    f = lambda k: (2*mp.besselj(1, k/kap)/(k/kap))**2 * k/(k**2+m**2) if k != 0 else 0
    return mp.quad(f, mp.linspace(0, 200*kap, 401) + [mp.inf]) / (2*mp.pi)
for m in [mp.mpf('0.5'), mp.mpf(1), mp.mpf(3)]:
    Cstar = (mp.pi/2*(1/mp.pi) + max(mp.log(1/m), 0) + 1 + mp.log(4)) / (2*mp.pi)
    for kap in [1, 2, 10, 100, 1000]:
        c = ckappa(mp.mpf(kap), m)
        print("Cs m=%s kappa=%5d c_kappa=%s  (1/2pi)log kappa + C_*=%s  %s" % (mp.nstr(m,3), kap, mp.nstr(c, 8), mp.nstr(mp.log(kap)/(2*mp.pi)+Cstar, 8), "OK" if c <= mp.log(kap)/(2*mp.pi)+Cstar else "FAIL"))

# (AMGM) Lemma C.3: b(P) := C_{p'} * sum_{m<2p'} C(P)^{2p'/(2p'-m)} * A^{-m/(2p'-m)},
#   C_{p'} := max(1, max_{1<=m<2p'} ((2p'-m)/(2p')) (2m)^{m/(2p'-m)}),  C(P) := sum_n |a_n| * max_{j} n!/(j!(n-2j)!2^j)
def hermite_coeffs(n):  # c^{n/2} He_n(x/sqrt c) = sum_j (-1)^j n!/(j!(n-2j)!2^j) c^j x^{n-2j}
    return [((-1)**j * math.factorial(n)//(math.factorial(j)*math.factorial(n-2*j)*2**j), j) for j in range(n//2+1)]
def wickpoly(a, c):  # coefficients beta_m of :P:_c
    beta = [mp.mpf(0)]*len(a)
    for n, an in enumerate(a):
        for coef, j in hermite_coeffs(n): beta[n-2*j] += an*coef*mp.mpf(c)**j
    return beta
random.seed(7); print("AMGM seed 7")
for trial in range(6):
    pp = 1 + trial % 3; deg = 2*pp
    a = [mp.mpf(random.uniform(-3, 3)) for _ in range(deg)] + [mp.mpf(random.uniform(0.2, 2))]
    A = a[-1]
    CP = sum(abs(an)*max(abs(cf) for cf, j in hermite_coeffs(n)) for n, an in enumerate(a))
    Cp = max([mp.mpf(1)] + [mp.mpf(2*pp-m)/(2*pp) * mp.mpf(2*m)**(mp.mpf(m)/(2*pp-m)) for m in range(1, 2*pp)])
    b = Cp*sum(CP**(mp.mpf(2*pp)/(2*pp-m)) * A**(-mp.mpf(m)/(2*pp-m)) for m in range(2*pp))
    worst = mp.inf
    for c in [0, mp.mpf('0.1'), 1, 5, 50, 1000]:
        beta = wickpoly(a, c)
        # minimum over x of the polynomial: check critical points and a grid
        crit = mp.polyroots([k*beta[k] for k in range(len(beta)-1, 0, -1)], maxsteps=200, extraprec=200)
        vals = [sum(beta[k]*mp.re(x)**k for k in range(len(beta))) for x in crit if abs(mp.im(x)) < mp.mpf('1e-12')]
        mn = min(vals) if vals else sum(beta[k]*0**k for k in range(len(beta)))
        worst = min(worst, (mn + b*(1+c)**pp))
    print("AMGM p'=%d  b(P)=%s  min over c of [min_x :P:_c + b(1+c)^p'] = %s  %s" % (pp, mp.nstr(b, 6), mp.nstr(worst, 6), "OK" if worst >= 0 else "FAIL"))

# (HC) one Gaussian variable X ~ N(0,1): Y = sum_{r<=2p'} y_r He_r(X); ||Y||_q via Gauss-Hermite quadrature (probabilists')
import numpy as np
from numpy.polynomial.hermite_e import hermegauss, hermeval
xg, wg = hermegauss(200); wg = wg/np.sqrt(2*np.pi)
rng = np.random.default_rng(11); worstratio = 0.0
for pp in [1, 2, 3]:
    for _ in range(200):
        coef = rng.normal(size=2*pp+1)
        Y = hermeval(xg, coef)
        n2 = np.sqrt(np.sum(wg*Y**2)); n4 = np.sum(wg*Y**4)**0.25
        worstratio = max(worstratio, n4/(3**pp*n2))
    print("HC p'=%d: max over 200 random Y of ||Y||_4/(3^p' ||Y||_2) = %.4f (<= 1 expected)" % (pp, worstratio)); worstratio = 0.0
print("numpy", np.__version__)
