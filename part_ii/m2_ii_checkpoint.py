#!/usr/bin/env python3
"""Exact quadratic checkpoint for Part II of the OAR programme.

The proof in ``lamport_part_ii_quadratic_obstruction.tex`` is analytic.  This
script evaluates the finite-torus quantities which occur in that proof; it is
not used as a substitute for any limiting argument.

For a lattice spacing ``eps`` and physical mass ``m``, the dimensionless
nearest-neighbour lattice dispersion is

    a_delta(theta) = sqrt(delta**2 + 4*sin(theta/2)**2),
    delta = m*eps.

If an orthonormal scaling function is used to embed the lattice Weyl algebra
in the continuum Weyl algebra, the continuum momentum covariance has symbol

    b_delta(theta) = sum_l sqrt(delta**2 + (theta+2*pi*l)**2)
                           * |phi_hat(theta+2*pi*l)|**2.

Orthonormality of the integer translates gives

    sum_l |phi_hat(theta+2*pi*l)|**2 = 1,

and hence the wavelet-independent lower bound

    b_delta(theta) >= h_delta(theta)
                   := sqrt(delta**2 + dist(theta, 2*pi*Z)**2).

The localized carrier used below has lattice frequency theta_0 = 3*pi/4.
Its lattice quadratic form tends to a_0(theta_0), whereas its continuum
quadratic form is bounded below by h_0(theta_0)=theta_0.  The strict inequality

    2*sin(theta_0/2) < theta_0

is the free-field obstruction to diagonal local state-norm convergence.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
from scipy.integrate import quad


MASS = 1.0
HALF_LENGTH = 8.0
THETA_0 = 3.0 * math.pi / 4.0


@dataclass(frozen=True)
class Row:
    level: int
    sites: int
    epsilon: float
    q_lattice: float
    q_continuum_lower: float
    state_difference_lower: float
    max_group_velocity: float
    wick_constant: float
    wick_asymptotic_error: float


def smooth_bump(x: np.ndarray, radius: float = 2.0) -> np.ndarray:
    """A real C-infinity function supported in (-radius, radius)."""

    y = x / radius
    out = np.zeros_like(y, dtype=np.float64)
    inside = np.abs(y) < 1.0
    out[inside] = np.exp(-1.0 / (1.0 - y[inside] ** 2))
    return out


def principal_angles(number_of_sites: int) -> np.ndarray:
    """Angles in [-pi, pi) in the ordering used by numpy's unitary DFT."""

    return 2.0 * math.pi * np.fft.fftfreq(number_of_sites)


def carrier(number_of_sites: int, epsilon: float) -> np.ndarray:
    """Return the exactly normalized localized carrier p_N.

    The factor cos(3*pi*n/4) has period eight.  All lattices used below have a
    number of sites divisible by eight, so it is a well-defined torus carrier.
    """

    half_sites = number_of_sites // 2
    n = np.arange(-half_sites, half_sites, dtype=np.int64)
    x = epsilon * n
    raw = math.sqrt(2.0 * epsilon) * smooth_bump(x) * np.cos(THETA_0 * n)
    norm = np.linalg.norm(raw)
    if not norm > 0.0:
        raise RuntimeError("the localized carrier vanished")
    return raw / norm


def quadratic_form_from_symbol(vector: np.ndarray, symbol: np.ndarray) -> float:
    """Evaluate <vector, symbol(D) vector> using the unitary DFT."""

    transformed = np.fft.fft(vector, norm="ortho")
    value = np.sum(np.abs(transformed) ** 2 * symbol)
    return float(np.real_if_close(value))


def wick_constant(delta: float) -> float:
    r"""Infinite-lattice equal-site field covariance.

    c(delta) = (4*pi)^(-1) int_{-pi}^{pi}
               (delta^2 + 4 sin^2(theta/2))^(-1/2) d theta.
    """

    integrand = lambda theta: 1.0 / math.sqrt(
        delta * delta + 4.0 * math.sin(theta / 2.0) ** 2
    )
    positive_half, _ = quad(
        integrand,
        0.0,
        math.pi,
        epsabs=2.0e-13,
        epsrel=2.0e-13,
        limit=500,
    )
    return positive_half / (2.0 * math.pi)


def evaluate(level: int) -> Row:
    number_of_sites = 2 ** level
    epsilon = 2.0 * HALF_LENGTH / number_of_sites
    delta = MASS * epsilon
    theta = principal_angles(number_of_sites)
    p = carrier(number_of_sites, epsilon)

    lattice_symbol = np.sqrt(delta**2 + 4.0 * np.sin(theta / 2.0) ** 2)
    distance_to_alias_lattice = np.abs(theta)
    continuum_lower_symbol = np.sqrt(delta**2 + distance_to_alias_lattice**2)

    q_lattice = quadratic_form_from_symbol(p, lattice_symbol)
    q_continuum_lower = quadratic_form_from_symbol(p, continuum_lower_symbol)
    state_difference_lower = (
        math.exp(-q_lattice / 4.0)
        - math.exp(-q_continuum_lower / 4.0)
    )

    # d[eps^{-1} a_delta(eps*k)]/dk = sin(theta)/a_delta(theta).
    velocity = np.divide(
        np.abs(np.sin(theta)),
        lattice_symbol,
        out=np.zeros_like(theta),
        where=lattice_symbol > 0.0,
    )
    max_group_velocity = float(np.max(velocity))

    c_delta = wick_constant(delta)
    c_asymptotic = math.log(8.0 / delta) / (2.0 * math.pi)

    return Row(
        level=level,
        sites=number_of_sites,
        epsilon=epsilon,
        q_lattice=q_lattice,
        q_continuum_lower=q_continuum_lower,
        state_difference_lower=state_difference_lower,
        max_group_velocity=max_group_velocity,
        wick_constant=c_delta,
        wick_asymptotic_error=c_delta - c_asymptotic,
    )


def run_checks(rows: list[Row]) -> None:
    """Fail loudly if the reproducible finite-scale calculation is inconsistent."""

    lattice_limit = 2.0 * math.sin(THETA_0 / 2.0)
    continuum_lower_limit = THETA_0
    state_lower_limit = (
        math.exp(-lattice_limit / 4.0)
        - math.exp(-continuum_lower_limit / 4.0)
    )
    last = rows[-1]

    assert all(row.max_group_velocity <= 1.0 + 5.0e-14 for row in rows)
    assert abs(last.q_lattice - lattice_limit) < 2.0e-3
    assert abs(last.q_continuum_lower - continuum_lower_limit) < 2.0e-3
    assert abs(last.state_difference_lower - state_lower_limit) < 1.0e-3
    assert abs(last.wick_asymptotic_error) < 2.0e-3
    assert state_lower_limit > 0.0


def main() -> None:
    rows = [evaluate(level) for level in range(7, 15)]
    run_checks(rows)

    lattice_limit = 2.0 * math.sin(THETA_0 / 2.0)
    state_lower_limit = (
        math.exp(-lattice_limit / 4.0) - math.exp(-THETA_0 / 4.0)
    )

    print("M2-II exact quadratic checkpoint")
    print(f"mass={MASS:.6g}, torus half-length={HALF_LENGTH:.6g}")
    print(f"theta_0={THETA_0:.12f}")
    print(f"predicted lattice limit={lattice_limit:.12f}")
    print(f"universal continuum lower limit={THETA_0:.12f}")
    print(f"rigorous state-norm liminf constant={state_lower_limit:.12f}")
    print()
    print(
        "level sites       epsilon       Q_lattice    Q_cont_lower "
        " state_lower     max|v|       c_delta       c-log(8/d)/(2pi)"
    )
    for row in rows:
        print(
            f"{row.level:5d} {row.sites:5d} "
            f"{row.epsilon:13.6e} {row.q_lattice:13.9f} "
            f"{row.q_continuum_lower:13.9f} "
            f"{row.state_difference_lower:13.9f} "
            f"{row.max_group_velocity:11.9f} "
            f"{row.wick_constant:13.9f} "
            f"{row.wick_asymptotic_error:18.9e}"
        )
    print()
    print("all analytic-consistency checks passed")


if __name__ == "__main__":
    main()
