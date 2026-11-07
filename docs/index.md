---
title: Overview
---

# Removal of the spatial cutoff for weakly coupled P(φ)₂

Documentation for a Hamiltonian proof that the net of spatially cutoff P(φ)₂ ground
states converges in norm on every local algebra. This is a research record, not a
published paper.

> **Read this first.** Theorem 12.2 is an implication from the eight printed imports A1–A8
> of §2.4, with one GJS theorem imported since 7 November 2026: Theorem 1.1.7, which is also
> used across strips transverse to the time-zero line, a case its printed proof does not reach
> (A8(iv)-T). The uniform local moment is a theorem of the record (Appendix D); the former
> moment input U_GJS is retired.
> Nothing here has been refereed; audit item C5 is open; the work is AI-assisted and
> human verification of it is ongoing. Treat every statement as a claim under active
> verification. See [status](status.md).

## The result

For the spatially cutoff P(φ)₂ Hamiltonian H(g) with ground state Ω_g, and ω_g the
induced state on the time-zero quasi-local algebra A, in the Glimm–Jaffe–Spencer
weak-coupling region 0 ≤ λ/m₀² < ε_P the **full net** (ω_g) — no subnets, no space
averaging — converges in norm on every local algebra A(O),

```latex
\lim_{g\in\mathcal G}\ \bigl\|(\omega_g-\omega_\infty)|_{\mathfrak A(O)}\bigr\| = 0 ,
```

with a super-polynomial rate in dist(O, {g < 1}), explicit up to the finite constant of Theorem C.5. The limit is locally normal,
translation invariant, ℤ₂ invariant for even P, and a ground state of the Glimm–Jaffe
dynamics in the spectral sense.

## Where to go

| | |
|---|---|
| [Status](status.md) | what is proved, what is conditional, what is open, and the gate record |
| [Results](results.md) | every numbered statement, with dependencies — generated from the manuscript |
| [Imports](imports.md) | A1–A8, their sources, A8(iv)-T, and what U_GJS was |
| [Definitions](definitions.md) | the model, the three cutoff classes, the plateau net |
| [Notation](notation.md) | the frozen notation table |
| [Provenance](provenance.md) | gates, corrections history, the citation dossiers |
| [Figures](interactive/index.html) | eight interactive illustrations of the main results |

The manuscript itself is [`part_i/main.pdf`](https://github.com/alexander-stottmeister/pphi2-cutoff-removal/blob/main/part_i/main.pdf) (110 pp, document of
record).

## The shape of the proof

The route is Hamiltonian rather than Euclidean. Two uniform inputs are established over
the cutoff class — a local interaction moment (M₂, Theorem 5.1, from Theorem D.4) and a gap
(G, Theorem 7.8, from Theorem D.3) — and then a *local perturbations perturb locally* estimate is run along an affine
path of cutoffs. The LPPL step rests on two exact ingredients rather than approximate
ones: an exact inverse-energy filter (Lemma 9.1) that converts the gap into a
super-polynomially decaying time kernel, and the exact light cone of the cutoff dynamics
(Proposition 2.7), which confines a time-evolved local observable. Their combination is
the two-regime bound (Lemma 10.3), and summing it over cells gives the rate function
Ψ_γ (Lemma 10.5), which decays faster than every polynomial.
