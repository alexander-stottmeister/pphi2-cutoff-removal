# The council

A reader's companion to the document of record (`../companion.tex`, built as
`../companion.pdf`) was planned, drafted, edited and verified by a council of AI agents
with distinct briefs, orchestrated by the author's Claude Code session on 23 and 24 October 2026.
This folder is the council's record. Everything in it is working material: a memo or a
report states what one member read and judged, not a claim of the record, and nothing here
has been refereed.

| file | what it is |
|---|---|
| `BRIEF.md` | the brief every member received: audience, reading list, the facts of the record they build on, the non-negotiables, the memo format, the candidate figures, the four role cards |
| `labels.md` | every number a companion may cite, generated from `docs/results.json` and `part_i/main.aux` by `make_labels.py`; nothing in it is typed in |
| `make_labels.py` | the generator of `labels.md` |
| `memo-aqft.md` | round R1, the algebraic quantum field theorist |
| `memo-qi.md` | round R1, the quantum-information theorist |
| `memo-cqft.md` | round R1, the constructive quantum field theorist, with the Part II page as section P |
| `memo-editor.md` | round R1, the handling editor: outline, rules, abstract, the referee's questions |
| `../PLAN.md` | round R2, the editor's synthesis of the four memos: tiering, outline, figures, rulings, assignments, findings register, verification checklist; Part 9 records the author's Checkpoint 1 decisions, Part 7.1 the findings added after R3 |
| `r3-return-aqft.md`, `r3-return-qi.md`, `r3-return-cqft.md` | round R3, each drafter's return: the sources it read, every locator and quotation it used, and what it reports to the editor |
| `r4-editor-report.md` | round R4, the editor's report: build and measurements, changes by section, the decisions B(i)–(viii), the banned-word grep, the locator and quotation lists after the edit |
| `r5-verifier-report.md` | round R5, the adversarial verifier's report: every checklist item with its output, the findings, and what was not checked |

## The rounds

1. **R1, independent reads.** Each member read the record (`part_i/main.tex` and its
   documentation) and wrote its memo without seeing the others'. The four ran in
   parallel on Claude Opus; the model's reasoning effort was the harness default,
   since the per-role agent definitions with `effort: max` were created in the same
   session and are only loaded at session start.
2. **R2, synthesis.** The editor read the three other memos and wrote `../PLAN.md`,
   which the author approved before any drafting (Checkpoint 1, `../PLAN.md` Part 9).
3. **R3, drafting.** The three domain members drafted the sections the plan assigns
   them (`../sections/`); the orchestrator drew the six figures in TikZ and pgfplots
   (`../figures/`), assembled the front matter and generated the bibliography
   (`../make_bib.py`), and re-checked at the source the findings the drafters reported.
4. **R4, editing.** The editor rewrote the twelve fragments in one voice under the
   plan's rules and cut the document to the 20-page ceiling.
5. **R5, adversarial verification.** A fresh agent that had drafted nothing ran the
   checklist of `../PLAN.md` Part 8: every number against `part_i/main.aux`, every
   quotation against `part_i/main.tex`, the GJ3 pages against the rendered PDF, every
   status word, every caption, the figure data, the page budget. It found one CRITICAL item (an arrow label in Fig. 1 that
   attributed the identity (P) to the proof of Proposition 2.7, which uses A6(i)), one
   MAJOR item (an arrow whose hidden origin made it read as coming from Appendix C) and
   eighteen MINOR items, mostly overlaps in the figures, notation and page budgets; the
   numbers, quotations, GJ3 facts, status words, the Part II table and the Appendix A
   column all passed. What was done with each finding is recorded in `../PLAN.md`,
   Part 10.
6. **R6, record.** The companion's PDF is tracked beside its source, built with the
   timestamp pinned (`../companion.tex`, first lines); README row, `strategy.md` entry,
   knowledge-base nodes, commit (24 October 2026).
7. **Checkpoint 2.** The author reads the built PDF; open at the time of writing
   (`../PLAN.md`, Part 10.5).

Reports of rounds R4 and R5 were handed back as text, because the agent harness refuses
report files written by subagents; the orchestrator saved each under the name above,
unchanged apart from the note at its head.

## Findings about the record

Section G of each memo, the drafters' returns and the editor's report list what their
authors believe is wrong or unclear in the record itself. None of it was written into the
companion: `../PLAN.md` consolidates the items into a register for the author (Parts 7
and 7.1), marking which the orchestrator re-checked at the source, and the editor's
report adds five more (its section 7). All are MINOR; none changes a theorem. The
documentation items (README, site texts, `docs/extract.py`) were fixed on 23 October 2026
in the commit that precedes the companion's; the items in `part_i/main.tex` are left to
the author.

## Revised edition (7 November 2026)

After the integration of Appendix D into the record on 7 November 2026 (Theorems D.3–D.4
derive the uniform local moment from GJS Theorem 1.1.7 and Appendix C; A8(vi) retired; the
transverse case listed as A8(iv)-T), the author decided to revise the companion at once
(answer 9 to Checkpoint 2 of `ugjs/PLAN.md`, recorded in `part_i/README.md`). The revision
was made by one editor agent on 7 November 2026, not by the council: the edition of
24 October 2026 was rewritten in place to describe the 110-page record of that date, with
`labels.md` regenerated from it (65 numbered statements). No memo or report of this
revision is kept in this folder; what changed, the rules that replace the U_GJS rules of
the first edition, and the checks run are `../PLAN.md`, Part 11. The revised edition has
not yet had an adversarial verification round like R5, and the author's reading of it is
open.

*8 November 2026, round R7.* The orchestrator's adversarial verification of the revised
edition (round R7) reported 0 CRITICAL, 2 MAJOR and 12 MINOR items, which the editor fixed
in place; the findings, the fixes, the space recovered and the checks run are
`../PLAN.md`, Part 11.1. This supersedes the last sentence above as far as the verification
round goes: the fixes have not been re-verified by an agent that did not write them, and
the author's reading of the revised edition is open.

*8 November 2026, round R7b.* The verifier's re-check of the R7 fixes found all fourteen
fixed and two new MINOR items caused by them (an edge of Fig. 1 drawn into Proposition 12.1,
and the definition of class P in Appendix A); the editor fixed both the same day
(`../PLAN.md`, Part 11.1, "R7b"), and those fixes have not been re-verified.

*11 November 2026, reports archived.* The sentence above that no report of the revision is
kept here is superseded. The editor's three reports (the revision, the fixes of R7, the
fixes of R7b) and the verifier's two (R7, R7b) had been returned as messages; they were
recovered from the session transcripts and saved as `revised-edition-editor-reports.md`
and `r7-verifier-report.md`, verbatim except for machine paths.

*11 November 2026, status.* An audit of the record on 9 November 2026 (round V4f,
`../../ugjs/council/v4f-free-field-report.md`) found four standard free-field facts that
the record used without stating or importing them, so that the companion's sentences
calling Theorem 12.2 "proved from printed statements" (abstract, §1 and §4) overstated.
The record was repaired on 11 November (its new Appendix E, audited in rounds V5 to V5d;
published on 21 November),
and those sentences hold of the repaired record (125 pages), not of the record of
7 November that the companion describes. The companion's text was not changed for the
repair: it is the edition of
7 November 2026 and describes the record of that date (110 pages, commit f213cc8). From
11 to 23 November the record had 125 pages; no statement changed its number, but the page
numbers in the companion's locators are those of the 7 November build, `labels.md` is the
label table of that build, and the companion's body does not mention Appendix E.

*23 November 2026, dated notice.* A notice of 23 November 2026 (161 words, nine lines) was
added to the box on the companion's first page, below the unchanged "Read this first"
paragraph, and rewritten the same day after the record's second pass of 23 November. It says
that the audit of 9 November found the record described here (commit f213cc8) using its
free-field layer without stating it, that Appendix E has supplied it since 11 November, and
that the status sentence quoted in §§1 and 4 stands; that the current record (23 November,
127 pages) restricts Corollary 12.3, which the companion states without restriction in §§1,
2 and 7 and in Fig. 1, to 𝒫(ξ) = ξ⁴ and to cutoffs 0 ≤ g ≤ 1 of GJ3, (2.3), and that
Theorem 12.2 is unchanged in substance; that statement numbers are unchanged and the cited
pages are up to seven pages too early (the 230 labels of `labels.md` moved by 0 to 7 pages
against the record of 23 November, none earlier); that §4's table and Fig. 1 predate items
(e)–(g) of A1, their "literal imports" to be read with the readings declared in A1, A3, A6
and A8, and A7's row as the covariance of K(g) and the parity of H₀ and, for even 𝒫, of
V(g); that §1's rate and gap are in working coordinates (Remark 3.3 of the record); and that
a third edition waits for the author's decision on Phase C of `../../ugjs/PLAN.md`. The
bibliography was regenerated by `../make_bib.py` from the record of 23 November; only the
entry MMST changed (pages 299–360 for 1299–1367, and its arXiv number). Nothing else in the
companion's text changed. Any notice on page 1, even one line, pushed the references onto a 21st
page, so its space was taken from page 1 alone: the box is set in footnote size, the title
block has tighter skips, and three kerns narrow the gaps around the box and before "How to
read". Pages 2–19 are the pages of 7 November (same text; same rendering at 72 dpi), and
page 20 differs only in the last line of the MMST entry. The edition, its date and its build
epoch (1794009600) are unchanged, and reference [R] is unchanged, because adding the commit
to it lengthens it by one line. The notice was written by one editor agent of the working
council of 23 November 2026 and checked by the documentation checker of that council
(`../../ugjs/council/v6-docs-check.md`, rows 27–30). The companion also repeats three sentences
of the record of 7 November that the record of 23 November corrects, and the notice does not
say so: "(B1)–(B4) are all load-bearing" (§8.1; (B2) is not used), "no mathematical dependence
in either direction" (§8.2; Part II re-uses an argument of Appendix C) and "not exponential"
(§§6, 8.1; for λ > 0 only).
