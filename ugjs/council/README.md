# The council that planned the removal of U_GJS

This folder is the record of a council of agents convened on 28 October 2026 (resumed on
30 October after a usage-limit cutoff) to plan the removal of the hypothesis U_GJS
(Assumption A8(vi) of `part_i/main.tex`) from Theorem 12.2. The plan itself is
`../PLAN.md`. Nothing here is mathematics of the record: every route named in these files
is `conjectured` until it is written out and audited, and Theorem 12.2 remains
"proved, conditional on U_GJS" (see `../../docs/status.md`).

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
   `r3-verifier-report.md`: "can go to the author after the listed fixes"; 0 CRITICAL,
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
