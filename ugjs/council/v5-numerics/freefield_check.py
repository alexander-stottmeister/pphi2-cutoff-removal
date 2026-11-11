# Free-field appendix (Appendix E of part_i/main.tex), numerical corroboration only
# (AGENTS 3.9 / 6.1): nothing is deduced from these numbers, and no proof step uses them.
# Notation of Proposition E.5(D): masses m and m' with m = s m', s > 0;
#   (d_s f)(x) = s^{-1} f(x/s),  (e_s h)(x) = h(x/s),  mu_m(k) = (k^2 + m^2)^{1/2},  C_m = (2 mu_m)^{-1}.
# Checked:
#  (K)  C_{m'}(s z) = C_m(z), with C_m(z) = (1/4pi) int_0^oo t^{-1} exp(-t m^2 - z^2/(4t)) dt
#       (the kernel formula of Lemma N.19), and against the closed form K_0(m|z|)/(2 pi);
#  (I)  ||d_s f||_{m'} = ||f||_m for the norm ||f||_m^2 = int |fhat(k)|^2 / mu_m(k) dk
#       (unitary Fourier transform; (d_s f)^(k) = fhat(s k));
#  (M)  <e_s h, mu_{m'} e_s h> = <h, mu_m h>, with (e_s h)^(k) = s hhat(s k).
# Test function for (I) and (M): f(x) = exp(-x^2/2)(1 + 0.3 x), fhat(k) = exp(-k^2/2)(1 - 0.3 i k).
# Run: python3 freefield_check.py     (11 November 2026: /usr/local/bin/python3, versions printed below)
import sys
import numpy as np, scipy
from scipy import integrate, special

print("python", sys.version.split()[0], "numpy", np.__version__, "scipy", scipy.__version__)
TOL = 1e-8
print("tolerance for every comparison (absolute):", TOL, "| quadrature: scipy.integrate.quad, default tolerances, limit=400")


def C(m, z):
    val, _ = integrate.quad(lambda t: np.exp(-t * m * m - z * z / (4 * t)) / t, 0, np.inf, limit=400)
    return val / (4 * np.pi)


def fhat(k):
    return np.exp(-k * k / 2) * (1 - 0.3j * k)


worst = 0.0
for (m, s) in [(1.3, 0.7), (2.0, 3.1), (0.4, 1.0)]:
    mp_ = m / s                                   # m'
    for z in [0.2, 1.0, 2.7]:
        a, b = C(mp_, s * z), C(m, z)
        k0 = special.k0(m * abs(z)) / (2 * np.pi)
        worst = max(worst, abs(a - b), abs(b - k0))
print("(K) max |C_m'(sz) - C_m(z)|, |C_m(z) - K_0(m|z|)/(2pi)| over 9 cases (m,s) in {(1.3,0.7),(2.0,3.1),(0.4,1.0)}, z in {0.2,1.0,2.7}:",
      worst, "pass" if worst < TOL else "FAIL")

worst = 0.0
for (m, s) in [(1.3, 0.7), (2.0, 3.1)]:
    mp_ = m / s
    lhs, _ = integrate.quad(lambda k: abs(fhat(s * k)) ** 2 / np.sqrt(k * k + mp_ * mp_), -np.inf, np.inf, limit=400)
    rhs, _ = integrate.quad(lambda k: abs(fhat(k)) ** 2 / np.sqrt(k * k + m * m), -np.inf, np.inf, limit=400)
    worst = max(worst, abs(lhs - rhs))
print("(I) max | ||d_s f||_m'^2 - ||f||_m^2 | over 2 cases (m,s) in {(1.3,0.7),(2.0,3.1)}:", worst, "pass" if worst < TOL else "FAIL")

worst = 0.0
for (m, s) in [(1.3, 0.7), (2.0, 3.1)]:
    mp_ = m / s
    lhs, _ = integrate.quad(lambda k: np.sqrt(k * k + mp_ * mp_) * abs(s * fhat(s * k)) ** 2, -np.inf, np.inf, limit=400)
    rhs, _ = integrate.quad(lambda k: np.sqrt(k * k + m * m) * abs(fhat(k)) ** 2, -np.inf, np.inf, limit=400)
    worst = max(worst, abs(lhs - rhs))
print("(M) max | <e_s h, mu_m' e_s h> - <h, mu_m h> | over 2 cases (m,s) in {(1.3,0.7),(2.0,3.1)}:", worst, "pass" if worst < TOL else "FAIL")
