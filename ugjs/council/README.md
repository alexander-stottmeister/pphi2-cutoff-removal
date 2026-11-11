# The council that planned the removal of U_GJS

This folder is the record of a council of agents convened on 28 October 2026 (resumed on
30 October after a usage-limit cutoff) to plan the removal of the hypothesis U_GJS
(Assumption A8(vi) of `part_i/main.tex`) from Theorem 12.2. The plan itself is
`../PLAN.md`. Nothing here is mathematics of the record: every route named in these files
is `conjectured` until it is written out and audited, and Theorem 12.2 remains
"proved, conditional on U_GJS" as of the council's dates; on 31 October 2026 the plan's
Phases 0′ and 0 were executed (gate record: `../../part_i/README.md`, section "Re-sourcing of A8(vi) and documentation repairs (2026-10-31)", and `../../strategy.md`; `../PLAN.md` itself is unchanged, and its "Nothing in it has been executed" describes the state before that date).

## Files

| file | round | what it is |
|---|---|---|
| `BRIEF.md` | R0 | the orchestrator's brief: the hypothesis with its consumers, the page-image corpora, the orchestrator's conjectures O1-O5, the memo format, the role cards (corrected 28 October after the knowledge-base review of the Erice reference node; two corrections are marked in place) |
| `memo-mp.md` | R1 | the mathematical physicist (functional analysis, quantifiers, imports): O1 by an L^2 -> L^4 semigroup bound, O3 refuted by a localized comparison ("Route M") |
| `memo-aqft.md` | R1 | the algebraic quantum field theorist (what the proof consumes): the trace of the constant M, the tolerated and fatal weakenings, O3 refuted by the same comparison ("Route L", L.1-L.4) |
| `memo-cqft.md` | R1 | the reader of the printed expansion: the 21-row map of the printed proof of Theorem 1.1.8, the stability input (2.4.34) that Appendix C's audit missed (finding F1, MAJOR), the costs of the expansion routes E1-E3 |
| `memo-cqft2.md` | R1 | the modern constructive toolkit: the same comparison found a third time, the transverse-strip catch for the sharp-time observable, why no non-expansion method fits [0,1]-valued cutoffs, the forest-formula route M1 |
| `memo-editor.md` | R1 | the handling editor: acceptance criteria under two standards, proportionality, the deliverable form and the map of edits, the plan skeleton |
| `r1b-attack-cqft.md` | R1b | the expansion reader's adversarial check of the comparison route: REPAIRABLE GAP, not fatal; the earlier O3 verdict withdrawn |
| `r1c-orchestrator-rulings.md` | R1c | the page facts the orchestrator verified on the images (GJS pp. 593-597), the convergence of the memos, rulings R1-R8 for the plan |
| `r3-verifier-brief.md` | R3 | the brief of the fresh agent that verified the plan |
| `r3-verifier-report.md` | R3 | its report |

Page images of the sources were rendered into the session scratchpad only; none is in
the repository (publication boundary, `../../README.md`).

## Rounds

1. **R0 (28 October).** The orchestrator read the record's A8, sections 4, 5, 7, Appendix C,
   the knowledge-base nodes on U_GJS, and the two Erice lectures of Glimm, Jaffe and Spencer
   on page images; recorded the latter as `common:reference/glimm-jaffe-spencer-erice-1973`
   (reviewed and amended the same day); wrote the brief with five conjectures to test.
2. **R1 (28-30 October).** Five members wrote independent memos; no member saw another's.
   Three of them (mp, aqft, cqft2) refuted conjecture O3 by the same construction: compare
   the slab cutoff with its restriction to a fixed box around the observable, bound every
   square outside the box by the printed clustering theorem, and the base term by the
   record's own Lemma C.2 and Theorem C.5. Two (cqft, editor) found that Appendix C's
   mechanism audit misstates the source at one point (GJS p. 624, (2.4.34)). One (cqft2)
   found the catch: for the sharp-time observable the comparison uses the printed theorem
   across strips transverse to the time-zero line, a case its printed proof does not reach.
3. **R1b (30 October).** The expansion reader, who had confirmed O3, attacked the comparison
   route with the two sketches in hand and withdrew its verdict: no error in the route,
   one repairable gap (the transverse case).
4. **R1c (30 October).** The orchestrator verified the decisive pages (GJS pp. 593-597) on the
   images and issued the rulings the plan follows.
5. **R2 (30 October).** The editor synthesized all memos into `../PLAN.md`.
6. **R3 (30 October).** A fresh agent verified the plan against the record and the sources
   (`r3-verifier-report.md`: "not yet"; 1 CRITICAL, 4 MAJOR, 20 MINOR). Its two decisive
   findings: a two-standards framework that was inconsistent, and a literal re-sourcing of
   U_GJS inside the Annals paper (Theorem 1.1.11 is printed "uniformly in h", and GJS's own
   proof of Theorem 1.1.8 on p. 600 is its specialization B = I, T = 0). The orchestrator
   re-read pp. 596 and 600 on the images and issued rulings R9-R13
   (`r1c-orchestrator-rulings.md`, section 5).
7. **R2b (30 October).** The editor revised the plan under those rulings (one import
   standard; Phase 0', the re-sourcing; the verifier's MINOR items applied).
8. **R3b (30 October).** The same verifier re-checked the revised parts (section R3b of
   `r3-verifier-report.md`: verdict "After the listed fixes."; 0 CRITICAL,
   2 MAJOR, 14 MINOR). The two MAJOR items were text fixes: the literal basis of Phase 0'
   must be stated at 0 < T < 1, inside the printed hypothesis T > 0 (GJS's own T = 0 on
   p. 600 gives the same bound), and one gate's list of surviving lines was incomplete.
9. **R2c (30 October).** The editor applied every R3b item in place; the orchestrator
   spot-checked them and recorded its own reading of GJS pp. 622 and 624 in the rulings file.
10. **Checkpoint (open).** The author reads the plan and decides the questions of its Part 11.

## Harness notes

Custom agent types (`council-*`) load only at session start; the second constructive member
ran as a general-purpose agent on Opus with a role card in its prompt. Three members were
cut off by a session usage limit on 28 October and resumed from their transcripts on
30 October. The Annals paper's text layer is garbled on the expansion pages; every page
fact in these files was read on a rendered image.

## Phases A and B: the comparison note (2–4 November 2026)

After the author's "start with the plan" (31 October 2026) and the execution of Phases 0′ and 0
(gate record in `../../part_i/README.md`; commit 4166883), the council drafted the comparison
note `../comparison.tex` (`../preamble.tex`, `../parts/`): aqft wrote §§4–6 and §8 (Lemma D.2,
Theorems D.3–D.4, the replaced proofs), mp §3 (Lemma D.1) and §7 (quantifiers), cqft2 §2
(notation, geometry, the identification Lemma N.22) and Appendix A (constants, recomputed
independently); the orchestrator wrote §1 and Appendix B (gate record). Files here:
`ab-drafting-brief.md` (the drafting brief; the paths in it were the session scratchpad),
`reports-drafters.md` and `report-mp.md` (the drafters' reports), `v1-brief.md` and
`v2-brief.md` (audit briefs), `v1-cqft-report.md` (cqft as attacker; with its re-check V1b and
closing pass V1c), `v1-mp-report.md` (quantifiers), `v2-report.md` (a fresh agent; with its
re-check V2b), `disposition-aqft.md`, `disposition-mp.md`, `disposition-cqft2.md` (one line
per finding), `labels-main-2026-11-02.txt` (the record's statement numbers and pages used for
citations), and `v3-appendix-c-report.md` with `v3-numerics/` (round V3, the audit of
Lemmas C.2–C.5). Rounds: drafting 2 November; V1 and V2 on the frozen version of 2 November
(59 pp): no false statement, one MAJOR, 49 MINOR; dispositions and the repair (Lemma N.22)
3 November; V1b and V2b on the frozen version of 3 November (70 pp): the repair holds, status
wording corrected; V1c on the frozen version of 4 November (72 pp): every item closed. Three
usage-limit interruptions (31 October, 2 and 3 November); every agent resumed from its
transcript. The harness refused the drafters' report and disposition files; those were returned
as messages and saved by the orchestrator. Integration waits for Checkpoint 2 (PLAN Part 11).

## Integration as Appendix D (7 November 2026)

At Checkpoint 2 the author decided to integrate the note as Appendix D of `part_i/main.tex`, as a dated amendment, to name the transverse case A8(iv)-T, to revise the companion now, to update the records with the integration, and to apply the repairs. The orchestrator integrated the note (auxiliary numbering kept; N.47 omitted; new Lemma N.23′, which closes the note's GAP after the construction of the Wick powers was added to Assumptions A1 and A3), applied the replaced proofs of §8, the V3 repairs of Appendix C, the counting on GJS columns and the "0(1)" [sic]. Two fresh Opus agents audited the integration (round V4: mathematics; integration consistency); their reports were returned as messages. Findings: no CRITICAL; one MAJOR, inherited (the affiliation of V(h) with A(U) asserted without argument in §2.1, now proved there); 36 MINOR; all fixed the same day; re-check V4b by the same two agents (ten new or residual MINOR items, all fixed the same evening) and V4c of the last fixes by the mathematics auditor. Gate GI: `part_i/README.md`. The note itself carries a dated notice and is otherwise unchanged.

## Reports of the integration audits, archived (11 November 2026)

The reports of round V4 and of its re-checks were returned as messages and were kept in a temporary folder of the session, which was emptied on 10 November 2026. On 11 November the orchestrator recovered them from the session transcripts and saved them here, verbatim except for machine paths: `v4-math-report.md` (V4, V4b, V4c, V4d, V4e; one agent), `v4-integration-report.md` (V4 and its re-check; one agent). Each report ends with its own list of what it did not check; `part_i/README.md`, "Status review (2026-11-09 to 2026-11-11)", collects those lists.

## Round V4f: the free-field layer (9 November 2026)

Two edits that the orchestrator made on 7 November after round V4e (the sentence of §2.1 that introduces π₀; the parenthesis on the Weyl relations in the Scope of A6) had not been audited, and V4e had named three items it had not checked (the rest of Remark 3.3, the parity relation for π₀, the translation covariance of the net). A fresh Opus agent audited them read-only on 9 November: `v4f-free-field-report.md`, 4 MAJOR and 6 MINOR findings. The record uses π₀, H₀, the translation unitaries and a dilation unitary, and the action of translations, parity and dilations on the fields, without defining these objects or deriving or importing those actions. The orchestrator re-read the findings at the source; the gate record (`part_i/README.md`, "Status review (2026-11-09 to 2026-11-11)") lists them and says which were re-read in full. The repair is not written yet.

## Check of the documentation unit (11 November 2026)

Before the commit that repaired the site, corrected the stale public text and added the notice of 11 November, a fresh Opus agent that had written none of it checked the working tree: `docs-check-2026-11-11-report.md` (findings F-a to F-p: 5 MAJOR, 11 MINOR; all applied; its line numbers refer to the tree as it was when it ran).
