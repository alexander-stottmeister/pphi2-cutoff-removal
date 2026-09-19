#!/usr/bin/env python3
"""Finite-sample diagnostics for the analytic D4 fixed-coarse rate proof.

The Lamport proof is analytic.  This script only catches normalization, sign,
and arithmetic regressions in the displayed identities.
"""

from __future__ import annotations

import math

import numpy as np


SQRT3 = math.sqrt(3.0)
H = np.array(
    [
        (1.0 + SQRT3) / (4.0 * math.sqrt(2.0)),
        (3.0 + SQRT3) / (4.0 * math.sqrt(2.0)),
        (3.0 - SQRT3) / (4.0 * math.sqrt(2.0)),
        (1.0 - SQRT3) / (4.0 * math.sqrt(2.0)),
    ]
)
ETA = 2.0 * (1.0 - math.log(SQRT3, 2.0))
THETA = 2.0 * ETA / (5.0 + ETA)
C_D = 48.0 * math.pi**4 * math.exp(1.0 / 6.0)


def m0(t: np.ndarray | float) -> np.ndarray:
    t_array = np.asarray(t)
    phases = np.exp(-1j * np.expand_dims(t_array, axis=-1) * np.arange(4))
    return (phases @ H) / math.sqrt(2.0)


def product(r: int, ell: np.ndarray) -> np.ndarray:
    answer = np.ones_like(ell, dtype=np.complex128)
    for j in range(1, r + 1):
        answer *= m0((2.0**-j) * ell)
    return answer


def check_qmf() -> float:
    grid = np.linspace(-math.pi, math.pi, 20001)
    residual = np.abs(np.abs(m0(grid)) ** 2 + np.abs(m0(grid + math.pi)) ** 2 - 1.0)
    error = float(np.max(residual))
    assert error < 2.0e-14
    return error


def check_filter_envelope() -> float:
    worst_ratio = 0.0
    for r in range(0, 13):
        ell = np.linspace(-math.pi * 2**r, math.pi * 2**r, 40001)
        ratio = np.abs(product(r, ell)) ** 2 * (1.0 + np.abs(ell)) ** (2.0 + ETA)
        worst_ratio = max(worst_ratio, float(np.max(ratio)))
    assert worst_ratio <= C_D * (1.0 + 2.0e-12)
    return worst_ratio


def check_filter_tail() -> float:
    worst_scaled_ratio = 0.0
    for r in range(1, 12):
        ell = np.linspace(-2**r, 2**r, 20001)
        finite = np.abs(product(r, ell)) ** 2
        proxy_infinite = np.abs(product(r + 40, ell)) ** 2
        difference = finite - proxy_infinite
        assert float(np.min(difference)) > -2.0e-13
        denominator = (SQRT3 / 12.0) * ell**2 * 4.0**-r
        mask = denominator > 1.0e-20
        ratio = np.zeros_like(denominator)
        ratio[mask] = difference[mask] / denominator[mask]
        worst_scaled_ratio = max(worst_scaled_ratio, float(np.max(ratio)))
    assert worst_scaled_ratio <= 1.0 + 2.0e-10
    return worst_scaled_ratio


def check_dispersion() -> float:
    mass = 1.3
    worst_scaled_ratio = 0.0
    for epsilon in (0.5, 0.25, 0.125, 0.0625):
        k = np.linspace(-math.pi / epsilon, math.pi / epsilon, 30001)
        gamma = np.sqrt(mass**2 + k**2)
        x = epsilon * k / 2.0
        # np.sinc(z) = sin(pi*z)/(pi*z), including the stable value at z=0.
        lattice_k_squared = k**2 * np.sinc(x / math.pi) ** 2
        gamma_n = np.sqrt(mass**2 + lattice_k_squared)
        squared_symbol_error = k**2 - lattice_k_squared
        difference = squared_symbol_error / (gamma + gamma_n)
        bound = epsilon**2 * k**4 / (24.0 * mass)
        # Ratios below this scale are dominated by double-precision cancellation
        # in 1-sinc(x)^2.  The unscaled inequality is checked on the full grid.
        mask = bound > 1.0e-9
        ratio = np.zeros_like(bound)
        ratio[mask] = difference[mask] / bound[mask]
        worst_scaled_ratio = max(worst_scaled_ratio, float(np.max(ratio)))
        assert float(np.min(squared_symbol_error)) > -2.0e-13
        assert float(np.max(difference - bound)) <= 2.0e-13
        assert float(np.max(ratio)) <= 1.0 + 2.0e-7
    return worst_scaled_ratio


def main() -> None:
    print(f"sum(h_n)                  = {np.sum(H):.16f}")
    print(f"sqrt(2)                   = {math.sqrt(2.0):.16f}")
    print(f"eta                        = {ETA:.12f}")
    print(f"theta                      = {THETA:.12f}")
    print(f"C_D                        = {C_D:.12f}")
    print(f"QMF max residual           = {check_qmf():.3e}")
    print(f"max sampled envelope ratio = {check_filter_envelope():.12f}")
    print(f"max sampled tail ratio     = {check_filter_tail():.12f}")
    print(f"max sampled disp. ratio    = {check_dispersion():.12f}")
    print("all diagnostic assertions passed")


if __name__ == "__main__":
    main()
