---
title: Imports
---

# The standing imports A1–A8

Theorem 12.2 is proved from printed statements only, with one GJS theorem imported: Theorem 1.1.7, which is also used for sharp-time observables across strips transverse to the time-zero line, a case its printed statement covers and its printed proof does not reach (listed separately as A8(iv)-T). The uniform local moment is a theorem of the record (Appendix D). The human page readings of audit item C5 (items 1–4 and 10–12, with item 9(c)) are open. The statements are in the [result inventory](results.md); this page records what each import is for, and what its status is.

| | assumption | what it supplies |
|---|---|---|
| A1 | cutoff construction | existence and normalization of the ground state Ω_g of H(g); since 7 November 2026 also the construction of the Wick powers in V(h) (Simon, pp. 10–12, 15–17, 134–138) |
| A2 | Feynman–Kac–Nelson transfer | the slab objects h_{T,g}, ψ_s, c_g and the Euclidean ↔ Hamiltonian passage |
| A3 | finite-volume stability | U_h in every L^p and e^{−ϱU_h} integrable, so 0 < Z(h) < ∞ and the interacting measures dq_h are well defined; since 7 November 2026 also the construction of U_h from Simon's Wick powers (V.3) |
| A4 | free hypercontractivity | the L^p smoothing used in the moment estimates, and the moment comparison on the chaoses (Simon, Theorem I.22) |
| A5 | domain smoothing; common core | Ω_g ∈ D(V_j), and a core on which the algebra acts |
| A6 | free propagation; patching; the dynamics α | free propagation at speed one, the Trotter formula, and the patched limit dynamics α; since 7 November 2026 also the locality of the time-zero net, item (iii) (GJ2 p. 397), which the record used before without listing it; the cutoff light cone itself is derived (Proposition 2.7) |
| A7 | covariance data | translation covariance and parity |
| A8 | the GJS package | the cutoff class, the observables and the printed norms of GJS, and CE2 (Theorem 1.1.7), including its transverse case **A8(iv)-T**; CE1 and **U_GJS** (A8(v)–(vi)) are kept as provenance and are used by no proof since 7 November 2026 |

A1–A7 are literal quotations of printed statements, cited to the page (A6(iii), the locality of the net, is a sentence printed inside the proof of Theorem 3.5.1 of GJ2, p. 397). A8 is a package of
several printed items; since 31 October 2026 every item is read off a printed statement, and
since 7 November 2026 the one GJS theorem among them that a proof uses is Theorem 1.1.7.

## A8(iv)-T: the transverse case of Theorem 1.1.7

GJS Theorem 1.1.7 is printed for localized monomials separated by a strip of any orientation (p. 594). Its printed proof rotates the strip into the time direction (p. 597) and so reaches sharp-time monomials only across strips parallel to the time-zero line. Lemma 7.4 uses only that case; Appendix D also uses the transverse case, listed separately as A8(iv)-T. It is the printed statement at its printed scope, the standard under which A1–A8 are all imported, and it is named separately for transparency. It is not a narrower form of U_GJS: U_GJS was a moment bound and states no clustering, and neither statement is known to imply the other. The uniform gap (Theorem 7.8) does not use it; the uniform local moment (Theorem 5.1), and through its constant everything from Lemma 10.2 on, does.

## U_GJS: what it was

From 16 August to 30 October 2026, A8(vi) — the cutoff-uniform Glimm–Jaffe–Spencer moment estimate on the slab family — was a named hypothesis of Theorem 12.2, documented on 5 September 2026 as the quantifier GJS state on p. 629 and consume in their printed proofs on pp. 594–597, "assembled from four pages". On 31 October 2026 it was read off one printed theorem, GJS Theorem 1.1.11, (1.1.16), at B = I, n = 0 (p. 596; GJS's own specialization on p. 600, named on p. 629): a re-sourcing, not a proof — the same mathematics with different bookkeeping.

Since 7 November 2026 it is **retired**. Appendix D derives what §§5 and 7 need from Theorem 1.1.7 and Appendix C: Theorem D.3 bounds sharp-time cylinder observables at fixed spatial cutoff, across strips parallel to the time-zero line only; Theorem D.4 bounds the square of the local interaction uniformly in the cutoff, using transverse strips as well. Its constant M_B contains the finite, unevaluated constant of Theorem C.5. A8(v)–(vii′) are kept in the record as provenance; no proof uses them.

What the record does not do: it does not re-derive the cluster expansion behind Theorem 1.1.7 (whose printed proof takes its constant from Theorem 1.1.8 at the same h, p. 597, and uses the stability input (2.4.34) of p. 624 that Appendix C's item M6 records), and it does not prove A8(iv)-T. Closing A8(iv)-T is Phase C of the plan `ugjs/PLAN.md` (optional, not scheduled).

Separately, a Hamiltonian bypass was investigated and found closed — g-uniform local moments were explicitly open in the 1970–71 literature, and the available substitutes cover only translation-averaged states or carry constants that are not uniform in the needed sense. That is a verdict on the printed record, not a no-go theorem.

## Reading the sources yourself

Every transcribed display in the manuscript carries a `% src:` comment naming its
origin, and each citation is matched to a page image in the dossiers. The page images
are third-party copyrighted material and are not redistributed here; see
[provenance](provenance.md) for how to regenerate them from your own copies.
