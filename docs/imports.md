---
title: Imports
---

# The standing imports A1–A8

Theorem 12.2 is proved from the literal imports A1–A8. Its moment input A8(vi) is GJS Theorem 1.1.11, (1.1.16), at B = I, n = 0 and any 0 < T < 1 (p. 596), the case GJS name on p. 629 and specialize to T = 0 in their proof of Theorem 1.1.8 (p. 600); the record does not re-derive the cluster expansion. The human page readings of audit item C5 (items 1–4 and 9–13) are open. It is an implication from these eight assumptions (§2.4, pp. 8–13). Their exact
statements are in the [result inventory](results.md); this page records what each one is
for, and what its status is.

| | assumption | what it supplies |
|---|---|---|
| A1 | cutoff construction | existence and normalization of the ground state Ω_g of H(g) |
| A2 | Feynman–Kac–Nelson transfer | the slab objects h_{T,g}, ψ_s, c_g and the Euclidean ↔ Hamiltonian passage |
| A3 | finite-volume stability | U_h in every L^p and e^{−ϱU_h} integrable, so 0 < Z(h) < ∞ and the interacting measures dq_h are well defined |
| A4 | free hypercontractivity | the L^p smoothing used in the moment estimates |
| A5 | domain smoothing; common core | Ω_g ∈ D(V_j), and a core on which the algebra acts |
| A6 | free propagation; patching; the dynamics α | free propagation at speed one, the Trotter formula, and the patched limit dynamics α; the cutoff light cone itself is derived (Proposition 2.7) |
| A7 | covariance data | translation covariance and parity |
| A8 | the GJS package | the cluster-expansion estimates: CE1, CE2, the printed norms, and **U_GJS** (since 31 October 2026 read off the printed Theorem 1.1.11) |

A1–A7 are literal quotations of printed theorems, cited to the page. A8 is a package of
several printed items; since 31 October 2026 every item is read off a printed statement.

## U_GJS: what it is, and what it is not

**It is** A8(vi): the cutoff-uniform Glimm–Jaffe–Spencer moment estimate on the slab
family used here. Theorem 12.2 is proved from the literal imports A1–A8. Its moment input A8(vi) is GJS Theorem 1.1.11, (1.1.16), at B = I, n = 0 and any 0 < T < 1 (p. 596), the case GJS name on p. 629 and specialize to T = 0 in their proof of Theorem 1.1.8 (p. 600); the record does not re-derive the cluster expansion. The human page readings of audit item C5 (items 1–4 and
9–13) are open. In the
manuscript's own display,

```latex
\text{one constant for the whole slab family }\mathcal C^{\rm slab},
\qquad\text{uniformly in the cutoff }h .
```

**It is not** a proof: the record trusts GJS's printed argument exactly as before, and
does not re-derive the cluster expansion. **It is not** a quantifier strengthened beyond
the source either. From 5 September to 30 October 2026 the reading was this: the
quantifier is the one GJS themselves state on p. 629 and consume in their printed proofs
of Theorems 1.1.7 and 1.1.1 on pp. 594–597, "assembled from four pages". A8(vii′) still
quotes those passages verbatim, now as corroboration, in three steps:

1. the source proves Theorem 1.1.1 along the affine path h₁ + α(h₂ − h₁), α ∈ [0,1], for
   *arbitrary* cutoff functions h₁, h₂ of its class, and applies Theorem 1.1.7 at every
   cutoff of that path with one h-independent constant;
2. the printed proof of Theorem 1.1.7 obtains its h-independent constant from Theorems
   1.1.8 and 1.1.11 and the estimate (1.1.16), which is stated "uniformly in h";
3. p. 629 states that the estimates of Theorems 1.1.8, 1.1.11, 3.1 and 4.1 are uniform
   in the space cutoff h.

**It is no longer a separate hypothesis of Theorem 12.2.** Since 31 October 2026 it is an
import like A1–A7: the same mathematics with different bookkeeping. Appendix C is a
*source-mechanism audit* plus proofs of two analytic prerequisites — not a reconstruction;
its item M6 (added the same day) records the stability input (2.4.34) of GJS p. 624 that
the audit had wrongly declared absent. Any citation of Theorem 12.2 should name the open
human page readings (audit item C5).

## What remains, and the plan

The council record `ugjs/PLAN.md` (28–30 October 2026) found that a display-by-display
trace of the printed expansion (GJS pp. 600–631) cannot be completed as a verified
citation and is not the route; the derivation that remains to be written is the box
comparison of its Phases A and B, which is planned to prove (conjectured until written and
audited) the uniform local moment from the printed
clustering theorem (GJS Theorem 1.1.7) and the record's own Lemma C.2 and Theorem C.5,
so that only one GJS theorem is imported. That derivation uses Theorem 1.1.7 for
sharp-time observables across strips transverse to the time-zero line, a case its printed
statement covers and its printed proof does not reach (the record's A8 Scope paragraph,
point (b)); closing that case is the plan's optional Phase C.

Separately, a Hamiltonian bypass was investigated and found closed — g-uniform local
moments were explicitly open in the 1970–71 literature, and the available substitutes
cover only translation-averaged states or carry constants that are not uniform in the
needed sense. That is a verdict on the printed record, not a no-go theorem.

## Reading the sources yourself

Every transcribed display in the manuscript carries a `% src:` comment naming its
origin, and each citation is matched to a page image in the dossiers. The page images
are third-party copyrighted material and are not redistributed here; see
[provenance](provenance.md) for how to regenerate them from your own copies.
