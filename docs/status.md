---
title: Status
---

# Status

What is proved, what is conditional, and what is open. Nothing on this page is a
summary of intent: each line names the statement or the gate it comes from.

## Part I — conditional, and the condition is named

**Theorem 12.2 (Main Theorem)** is proved as an *implication* from the imports A1–A8
enumerated in §2.4. It is not a proof of those imports. Seven of the eight are literal
quotations of printed theorems. The eighth is not:

> **A8(vi), written U_GJS** — the cutoff-uniform form of the Glimm–Jaffe–Spencer moment
> estimate (Ann. of Math. **100** (1974), Thm. 1.1.8) on the slab family used here.

Since the scope amendment of 5 September 2026, U_GJS is documented as imported *at the
scope at which the source itself states and uses it*, with the passages on pp. 594–597
and 629 quoted verbatim in A8(vii′), rather than as a quantifier strengthened beyond the
source. It remains a **named hypothesis** of Theorem 12.2. The manuscript does not
re-derive the cluster expansion: Appendix C audits the source mechanism and proves two
analytic prerequisites only. See [imports](imports.md).

Of the 61 numbered statements, **24 reach A8 through their own proof chain** and
therefore inherit this conditionality; the rest do not. Which are which is computed, not
asserted — see the `imports A8` column of the [result inventory](results.md). The
inverse-energy filter (Lemma 9.1), for instance, is independent of A8 entirely.

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
[`part_i/C5_reading_record.md`](https://github.com/alexander-stottmeister/pphi2-cutoff-removal/blob/main/part_i/C5_reading_record.md); all nine verdict fields
are blank. Items 8–9 were added on 5 September 2026 for the affine-path application of
Theorem 1.1.7 on p. 595 and the derivation of Theorem 1.1.7 from Theorem 1.1.8 on
pp. 596–597.

Closing C5 does not change the status of U_GJS. It is a check of transcription fidelity,
not of the mathematics.

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
