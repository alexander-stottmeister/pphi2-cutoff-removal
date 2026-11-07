---
title: Status
---

# Status

What is proved, what is conditional, and what is open. Nothing on this page is a
summary of intent: each line names the statement or the gate it comes from.

## Part I — an implication from printed imports; one GJS theorem imported since 7 November 2026

**Theorem 12.2 (Main Theorem).** Theorem 12.2 is proved from printed statements only, with one GJS theorem imported: Theorem 1.1.7, which is also used for sharp-time observables across strips transverse to the time-zero line, a case its printed statement covers and its printed proof does not reach (listed separately as A8(iv)-T). The uniform local moment is a theorem of the record (Appendix D). The human page readings of audit item C5 (items 1–4 and 10–12, with item 9(c)) are open. It is an *implication* from the imports A1–A8 enumerated in §2.4; the record is not a proof of those imports, and it does not re-derive the cluster expansion.

How the record got here:

- **16 August – 30 October 2026.** The cutoff-uniform moment estimate U_GJS, A8(vi), was a named hypothesis of Theorem 12.2 ("assembled from four pages" of the source).
- **31 October 2026 (re-sourcing).** A8(vi) was read off one printed theorem, GJS Theorem 1.1.11, (1.1.16), at B = I, n = 0 (p. 596; p. 600; p. 629). A re-sourcing, not a proof: the same mathematics with different bookkeeping.
- **7 November 2026 (integration of Appendix D).** The moment bounds that §§5 and 7 consume are derived from the printed clustering theorem, GJS Theorem 1.1.7, by comparing a cutoff with its restriction to a box of the source's lattice squares (Lemmas D.1–D.2, Theorems D.3–D.4), with the normalization, ultraviolet and stability results of Appendix C. A8(vi) is retired; GJS Theorem 1.1.11 is no longer used. The uniform gap (Theorem 7.8) rests on the parallel case of Theorem 1.1.7 alone; the uniform local moment (Theorem 5.1), and through its constant M everything from Lemma 10.2 on, uses the transverse case A8(iv)-T as well. M now contains the finite, unevaluated constant of Theorem C.5, so the rate of Theorem 12.2(1) is explicit up to that constant.

In the same pass three defects of the record were repaired (Appendix B, corrections history): Appendix C's analytic lemmas rested on three inputs that were neither proved nor imported (found by the independent audit V3 of 2 November 2026; now derived or imported, every constant explicit); §6 counted spatial cells shifted by half a unit against the source's squares, which made the displayed norm bounds (7)–(8) false as stated (now counted on the source's columns; no theorem was affected); and the record wrote the interaction V(h) and its Euclidean counterpart as formal integrals with no construction of their Wick powers (now constructed in Assumptions A1 and A3, with Lemma N.23′ identifying them with the limits used in Appendix D). The record is 110 pages.

The plan, the council that wrote Appendix D and its four audit rounds are in [`ugjs/`](https://github.com/alexander-stottmeister/pphi2-cutoff-removal/blob/main/ugjs/PLAN.md). See [imports](imports.md).

Of the numbered statements, the [result inventory](results.md) marks which reach A8 through their own `\ref` chain. Since 31 October 2026 that index records dependence on the GJS package, every item of which is a printed statement, and not a conditional status. The index is mechanical: it counts forward references and misses a dependence stated in prose only (the standing hypothesis (G_γ) of §§8–10, which Theorem 7.8 supplies), so it is not a verdict on any single proof.

### Negative scope, stated by the manuscript itself

No uniqueness of ω_∞ among all locally normal ground states. No sharp exponential rate.
No claim outside the weak-coupling region.

### Gate record (Part I)

| gate | requirement | status |
|---|---|---|
| G0 | compiles; every cite/ref resolves; every assumption has a "Used in" line | passed 10 Aug 2026 |
| G1 / G2 | every ⟨i⟩⟨j⟩ step of the Lamport sources maps to a unique environment or display; no unmapped step, no orphan | passed 10 Aug 2026 |
| G3a / G3b | constants recomputed **by hand**; forbidden-string check | passed 10 Aug 2026 |
| G4 | citation ↔ dossier bijection; regression greps | passed 10 Aug 2026 |
| G5 | 3 × pdflatex, zero unresolved; every page rendered and inspected | passed 10 Aug 2026 |
| G6 | adversarial pass; zero confirmed findings, or all fixed and re-verified | passed 10 Aug 2026 |

The full records, including the findings G6 raised and their dispositions, are in
[`part_i/README.md`](https://github.com/alexander-stottmeister/pphi2-cutoff-removal/blob/main/part_i/README.md).

## Open audit item C5

**No second human reader has yet checked the source page images against the
transcriptions in §2.** The itemized checklist is
[`part_i/C5_reading_record.md`](https://github.com/alexander-stottmeister/pphi2-cutoff-removal/blob/main/part_i/C5_reading_record.md); all thirteen verdict fields
are blank.

C5 is a check of transcription fidelity, not of the mathematics. Since 7 November 2026, items 1–4 carry the imports of A8 (Theorem 1.1.7 is the one GJS theorem imported; item 1(e) the reading of GJS's definition (1.8) of V(h)); items 10–11, with items 9(c) and 12(a),(c), carry the readings behind A8(iv)-T and the identification of the source's monomials with the objects Appendix D constructs; the rest of items 5–9 and 12, and item 13 (Theorems 1.1.8 and 1.1.11, the pages behind the retired A8(vi)), are corroboration.

**Open beyond C5.** The transverse case A8(iv)-T is used at the printed statement's scope and is not proved in the record; closing it is Phase C of the plan (optional, not scheduled). The constant of Theorem C.5 is finite and not evaluated.

## Part II — open at gate (II.11)

Nothing in Part I depends on Part II. The preparatory scoping pass is
[`part_ii/gate_II11_scoping.pdf`](https://github.com/alexander-stottmeister/pphi2-cutoff-removal/blob/main/part_ii/gate_II11_scoping.pdf); phases V0–V4 are
recorded in `strategy.md`.

| claim | status |
|---|---|
| finest-scale diagonal norm convergence | **disproved** |
| exact finite-torus interacting model and ground state | **constructed** |
| interacting fixed-coarse projective cluster state along a cofinal subnet | **proved unconditionally** |
| MMST free fixed-coarse / projective convergence | proved in the source, **strengthened here** to an explicit D4 power rate |
| exact free gap, group-velocity bound, Wick logarithm | **proved** in the Lamport note |
| Battle–Federbush as a source for OAR-uniform CE1/CE2 | **not available** — the cited note treats different phase-cell variables |
| full-sequence interacting convergence and identification with the continuum P(φ)₂ state | **open**, exactly at the coarse Weyl characteristic-functional limit |
| interacting scale-uniform gap, local second moment, Lieb–Robinson | **open** |
| the cited Nachtergaele–Raz–Schlein–Sims theorem | **inapplicable** to the Wick quartic: it assumes V′ ∈ L¹(ℝ) |
| the former path (1−s)H_N + sH | **undefined** without a common Hilbert-space/form realization; removed from the corrected program |

## The record itself

This is an AI-assisted research record and an experiment in open science. Nothing in it
has been refereed. The author's own line-by-line check of the machine-assisted material
is still in progress. Every phase, gate and adversarial round is published in
`strategy.md`, including the rounds that found errors in earlier rounds' repairs.
