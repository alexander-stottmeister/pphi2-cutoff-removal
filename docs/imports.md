---
title: Imports
---

# The standing imports A1–A8

Theorem 12.2 is an implication from these eight assumptions (§2.4, pp. 7–9). Their exact
statements are in the [result inventory](results.md); this page records what each one is
for, and what its status is.

| | assumption | what it supplies |
|---|---|---|
| A1 | cutoff construction | existence and normalization of the ground state Ω_g of H(g) |
| A2 | Feynman–Kac–Nelson transfer | the slab objects h_{T,g}, ψ_s, c_g and the Euclidean ↔ Hamiltonian passage |
| A3 | finite-volume stability | U_h in every L^p and e^{−ϱU_h} integrable, so 0 < Z(h) < ∞ and the interacting measures dq_h are well defined |
| A4 | free hypercontractivity | the L^p smoothing used in the moment estimates |
| A5 | domain smoothing; common core | Ω_g ∈ D(V_j), and a core on which the algebra acts |
| A6 | free propagation; patching; the dynamics α | the **exact light cone** and the patched limit dynamics |
| A7 | covariance data | translation covariance and parity |
| A8 | the GJS package | the cluster-expansion estimates: CE1, CE2, the printed norms, and **U_GJS** |

A1–A7 are literal quotations of printed theorems, cited to the page. A8 is a package of
several printed items, and one of them is not literal.

## U_GJS: what it is, and what it is not

**It is** A8(vi): the cutoff-uniform form of the Glimm–Jaffe–Spencer moment estimate
(Ann. of Math. **100** (1974), Thm. 1.1.8), on the slab family used here. In the
manuscript's own display,

```latex
\text{one constant for the whole slab family }\mathcal C^{\rm slab},
\qquad\text{uniformly in the cutoff }h .
```

**It is not** a quantifier strengthened beyond the source. Since the scope amendment of
5 September 2026 the reading is this: the quantifier is the one GJS themselves state on
p. 629 and consume in their printed proofs of Theorems 1.1.7 and 1.1.1 on pp. 594–597.
A8(vii′) quotes those passages verbatim, in three steps:

1. the source proves Theorem 1.1.1 along the affine path h₁ + α(h₂ − h₁), α ∈ [0,1], for
   *arbitrary* cutoff functions h₁, h₂ of its class, and applies Theorem 1.1.7 at every
   cutoff of that path with one h-independent constant;
2. the printed proof of Theorem 1.1.7 obtains its h-independent constant from Theorems
   1.1.8 and 1.1.11 and the estimate (1.1.16), which is stated "uniformly in h";
3. p. 629 states that the estimates of Theorems 1.1.8, 1.1.11, 3.1 and 4.1 are uniform
   in the space cutoff h.

**It is still a hypothesis.** The manuscript does not re-derive the cluster expansion.
Appendix C is a *source-mechanism audit* plus proofs of two analytic prerequisites — it
is not a reconstruction. Theorem 12.2 therefore remains conditional, and any citation of
it should say so.

## What would discharge it

The only proportionate route to an unconditional Theorem 12.2 is a display-by-display
trace of the h-dependence through the printed expansion on GJS pp. 598–629, completing
Proposition C.1, so that U_GJS becomes derived rather than imported. This is recorded
as an open problem and is **not scheduled**: it is judged disproportionate for a record
whose imports are named and whose scope is stated.

Separately, a Hamiltonian bypass was investigated and found closed — g-uniform local
moments were explicitly open in the 1970–71 literature, and the available substitutes
cover only translation-averaged states or carry constants that are not uniform in the
needed sense. That is a verdict on the printed record, not a no-go theorem.

## Reading the sources yourself

Every transcribed display in the manuscript carries a `% src:` comment naming its
origin, and each citation is matched to a page image in the dossiers. The page images
are third-party copyrighted material and are not redistributed here; see
[provenance](provenance.md) for how to regenerate them from your own copies.
