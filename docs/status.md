---
title: Status
---

# Status

What is proved, what is conditional, and what is open. Nothing on this page is a
summary of intent: each line names the statement or the gate it comes from.

## Part I — an implication from printed imports; the moment input re-sourced on 31 October 2026

**Theorem 12.2 (Main Theorem).** Theorem 12.2 is proved from the literal imports A1–A8. Its moment input A8(vi) is GJS Theorem 1.1.11, (1.1.16), at B = I, n = 0 and any 0 < T < 1 (p. 596), the case GJS name on p. 629 and specialize to T = 0 in their proof of Theorem 1.1.8 (p. 600); the record does not re-derive the cluster expansion. The human page readings of audit item C5 (items 1–4 and 9–13) are open. It is an *implication* from the imports A1–A8 enumerated in §2.4; the record is not a proof of those imports. Since 31 October 2026 all eight
are printed statements used at the scope at which they are printed; the last to become so
was

> **A8(vi), written U_GJS** — the cutoff-uniform Glimm–Jaffe–Spencer moment estimate on the
> slab family used here. Theorem 12.2 is proved from the literal imports A1–A8. Its moment input A8(vi) is GJS Theorem 1.1.11, (1.1.16), at B = I, n = 0 and any 0 < T < 1 (p. 596), the case GJS name on p. 629 and specialize to T = 0 in their proof of Theorem 1.1.8 (p. 600); the record does not re-derive the cluster expansion.

This is a re-sourcing, not a proof. From 16 August to 30 October 2026 the same estimate was
carried as a named hypothesis of Theorem 12.2, documented on 5 September 2026 as the
quantifier GJS state on p. 629 and consume on pp. 594–597 but "assembled from four pages";
the two readings are the same mathematics with different bookkeeping, and the record still
trusts GJS's printed argument exactly as before. Appendix C audits the source mechanism
(its item M6, added 31 October 2026, records a stability input the audit had missed) and
proves two analytic prerequisites only. The human page readings of audit item C5 (items
1–4 and 9–13) are open and are to be named beside every status word. The plan to derive
the moment bound from the clustering theorem alone, and the one case of GJS Theorem 1.1.7
that its printed proof does not reach, are in
[`ugjs/PLAN.md`](https://github.com/alexander-stottmeister/pphi2-cutoff-removal/blob/main/ugjs/PLAN.md).
See [imports](imports.md).

Of the 61 numbered statements, **29 reach A8 through their own `\ref` chain** (since
23 October 2026 this counts the three Source Facts printed inside A8, and with them
Lemma 7.4 and Remark C.6); since 31 October 2026 this index records dependence on the GJS
package, every item of which is a printed statement, and no longer a conditional status;
the rest do not reach A8. Which are which is computed from the manuscript's reference graph, not
asserted — see the `imports A8` column of the [result inventory](results.md). The index
is mechanical: it counts forward references and misses a dependence stated in prose only
(the standing hypothesis (G_γ) of §§8–10, which Theorem 7.8 supplies), so it is not a
verdict on any single proof. The inverse-energy filter (Lemma 9.1), for instance, is
independent of A8 entirely.

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
are blank. Items 8–9 were added on 5 September 2026 for the affine-path application of
Theorem 1.1.7 on p. 595 and the derivation of Theorem 1.1.7 from Theorem 1.1.8 on
pp. 596–597; items 10–13 on 31 October 2026.

C5 is a check of transcription fidelity, not of the mathematics. Items 1–4, 9, 12 and 13
carry the imports of A8 (items 12–13: Theorem 1.1.11's "monomials of type (1.1.5)",
"B_T … at time T > 0" and the rotation sentence; p. 600's specialization and p. 628's
hypotheses of Theorem 4.1); items 10–11 carry the disclosure of the transverse case in A8's
Scope paragraph (the two forms (1.1.5)–(1.1.6) with p. 595's multi-time notation;
Theorem 1.1.7's strip without orientation); items 5–8 are corroboration.

**Phases A and B of the removal plan (2–4 November 2026).** The comparison note
`ugjs/comparison.tex` (72 pp, built with `pdflatex` from `ugjs/`; master, preamble and
`ugjs/parts/`) derives the uniform local moment of Theorem 5.1 and §7 from the printed
clustering theorem (GJS Theorem 1.1.7) and Appendix C, so that after integration Theorem 1.1.11
would no longer be used. It is audited in four rounds (`ugjs/council/`) and not integrated:
every statement in it is conditional on the repairs R1–R10 of the V3 audit of Appendix C
(three MAJOR gaps in Lemmas C.2–C.5: true statements with unproved inputs) and, for the
sharp-time observable, on the transverse case of Theorem 1.1.7 at the printed statement's
scope, which its printed proof does not reach. Theorem 12.2's status is unchanged. Integration
is Checkpoint 2 of the plan, the author's decision.

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
