---
title: Status
---

# Status

What is proved, what is conditional, and what is open. Nothing on this page is a
summary of intent: each line names the statement or the gate it comes from.

## The free-field layer: found on 9 November 2026, repaired on 11 November, published on 21 November

A fresh audit on 9 November 2026 (round V4f; report
[`ugjs/council/v4f-free-field-report.md`](https://github.com/alexander-stottmeister/pphi2-cutoff-removal/blob/main/ugjs/council/v4f-free-field-report.md))
found that `part_i/main.tex` used four standard properties of the free field that it neither
defined, derived nor imported:

1. the time-zero momentum field π₀ and the free Hamiltonian H₀ on Q-space, which were named
   and never defined;
2. the space translations as automorphisms of the algebra, which Theorem 12.2(4),
   Corollary 12.3 and Theorem 13.2 use, and their action on the net, τ_a(A(O)) = A(O + a),
   used in the proofs of Theorem 12.2(4) and Theorem 13.2;
3. the parity relation Θπ₀(h)Θ = −π₀(h), used in the proof of Theorem 12.2(4) and through it
   in Theorem 13.2;
4. the dilation unitary of Remark 3.3, on which the reduction to the source's mass rests.

No step was found to be false, and all four gaps were older than the integration of
7 November. From 11 to 21 November the public pages carried a notice that Theorem 12.2
was proved conditional on these four items (commit d2b106c). The record now has an Appendix E.
It defines the objects through the unitary between Fock space and Q-space of Simon's
Theorem I.11, proves how translations, parity and dilations act on the fields, on the local
algebras, on H₀ and on the interaction V(g), and identifies the objects with those of the
Fock-space sources. The printed statements it uses are listed in Assumption A1, whose items
(e)–(g) are new. Two fresh agents audited the repair on 11 November (round V5: one the
mathematics, one the sources and the integration). They found no critical error and three
major points: Remark 3.3 stated how the dynamics transports under the dilation without
deriving it, and two statements of the record about itself were inaccurate. These and the
minor points were repaired, and each repair to the manuscript was re-checked by the auditor who
had raised the finding (rounds V5b to V5d; reports
[`v5-math-report.md`](https://github.com/alexander-stottmeister/pphi2-cutoff-removal/blob/main/ugjs/council/v5-math-report.md) and
[`v5-sources-report.md`](https://github.com/alexander-stottmeister/pphi2-cutoff-removal/blob/main/ugjs/council/v5-sources-report.md)). The repair was committed on
11 November (73bbb76) and published on 21 November, after a third agent had checked its
documentation on 12 November and that check's three major and eight minor points had been
applied. All of them concern the documentation; two of the minor ones concern the title-page
notice of the manuscript, which was rebuilt (no statement, label or page number changed)
([`docs-check-2026-11-12-report.md`](https://github.com/alexander-stottmeister/pphi2-cutoff-removal/blob/main/ugjs/council/docs-check-2026-11-12-report.md);
gate record in [`part_i/README.md`](https://github.com/alexander-stottmeister/pphi2-cutoff-removal/blob/main/part_i/README.md), "Free-field appendix (2026-11-11)"). The notice is withdrawn: the status sentence stands as on
7 November, with the free-field layer now written out. The record has 125 pages. No numbered
statement changed its number, and no statement of a theorem, proposition, lemma or corollary
changed; Assumptions A1, A6 and A7 and Remark 3.3 did.

## Part I — an implication from printed imports; one GJS theorem imported since 7 November 2026

**Theorem 12.2 (Main Theorem).** Theorem 12.2 is proved from printed statements only, with one GJS theorem imported: Theorem 1.1.7, which is also used for sharp-time observables across strips transverse to the time-zero line, a case its printed statement covers and its printed proof does not reach (listed separately as A8(iv)-T). The uniform local moment is a theorem of the record (Appendix D). The human page readings of audit item C5 (items 1–4 and 10–12, with item 9(c)) are open. It is an *implication* from the imports A1–A8 enumerated in §2.4; the record is not a proof of those imports, and it does not re-derive the cluster expansion.

How the record got here:

- **16 August – 30 October 2026.** The cutoff-uniform moment estimate U_GJS, A8(vi), was a named hypothesis of Theorem 12.2 ("assembled from four pages" of the source).
- **31 October 2026 (re-sourcing).** A8(vi) was read off one printed theorem, GJS Theorem 1.1.11, (1.1.16), at B = I, n = 0 (p. 596; p. 600; p. 629). A re-sourcing, not a proof: the same mathematics with different bookkeeping.
- **7 November 2026 (integration of Appendix D).** The moment bounds that §§5 and 7 consume are derived from the printed clustering theorem, GJS Theorem 1.1.7, by comparing a cutoff with its restriction to a box of the source's lattice squares (Lemmas D.1–D.2, Theorems D.3–D.4), with the normalization, ultraviolet and stability results of Appendix C. A8(vi) is retired; GJS Theorem 1.1.11 is no longer used. The uniform gap (Theorem 7.8) rests on the parallel case of Theorem 1.1.7 alone; the uniform local moment (Theorem 5.1), and through its constant M everything from Lemma 10.2 on, uses the transverse case A8(iv)-T as well. M now contains the finite, unevaluated constant of Theorem C.5, so the rate of Theorem 12.2(1) is explicit up to that constant.
- **11 November 2026 (free-field appendix; published 21 November).** Appendix E defines the momentum field π₀, the free Hamiltonian H₀ and the unitaries of translation, parity and dilation on Q-space and proves how they act; until then the record had used them without stating them (section above). Theorem 12.2 and its proof are unchanged apart from the references to that appendix; Remark 3.3, which reduces a general pair (m₀, λ) to the source's mass, is rewritten and transports each conclusion of Theorem 12.2 explicitly.

In the pass of 7 November three defects of the record were repaired (Appendix B, corrections history): Appendix C's analytic lemmas rested on three inputs that were neither proved nor imported (found by the independent audit V3 of 2 November 2026; now derived or imported, every constant explicit); §6 counted spatial cells shifted by half a unit against the source's squares, which made the displayed norm bounds (7)–(8) false as stated (now counted on the source's columns; no theorem was affected); and the record wrote the interaction V(h) and its Euclidean counterpart as formal integrals with no construction of their Wick powers (now constructed in Assumptions A1 and A3, with Lemma N.23′ identifying them with the limits used in Appendix D). The record of that date has 110 pages; since 11 November 2026 it has 125.

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
| GI | integration of Appendix D: G0 re-run on the 110 pages; the 125 earlier labels keep their numbers; step map of the replaced proofs; constants re-derived by hand; audit rounds V4 and V4b, with the re-checks V4c–V4e | passed 7 Nov 2026, without G4 and G5 |
| GF | free-field appendix E: G0 re-run on the 125 pages; all 230 earlier labels keep their numbers; no statement of a theorem, proposition, lemma or corollary changed; the scaling identities re-derived by hand by the auditor; audit rounds V5 to V5d; its documentation checked by a third agent on 12 Nov | passed 11 Nov 2026, without G4 and G5; published 21 Nov 2026 |

G0–G6 are the gates of the manuscript of 10 August 2026. For the build of 7 November 2026 the
corresponding record is gate GI. Two of its parts were **not run**: the dossier index was not
extended to the new page images (G4), and the 110 pages were not each inspected (G5). The
audit of 9 November 2026 (round V4f, above) came after GI and is not a gate; the repair it led
to has its own record, gate GF, with the same two parts **not run** for the 125 pages.

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
