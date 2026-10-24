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
