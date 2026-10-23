# The council

A reader's companion to the document of record (`../companion.tex`) was planned and
drafted by a council of four AI agents with distinct briefs, orchestrated by the
author's Claude Code session on 23 October 2026. This folder is the council's record.
Everything in it is working material: a memo states what one member read and judged,
not a claim of the record, and nothing here has been refereed.

| file | what it is |
|---|---|
| `BRIEF.md` | the brief every member received: audience, reading list, the facts of the record they build on, the non-negotiables, the memo format, the candidate figures, the four role cards |
| `labels.md` | every number a companion may cite, generated from `docs/results.json` and `part_i/main.aux` by `make_labels.py`; nothing in it is typed in |
| `make_labels.py` | the generator of `labels.md` |
| `memo-aqft.md` | round 1, the algebraic quantum field theorist |
| `memo-qi.md` | round 1, the quantum-information theorist |
| `memo-cqft.md` | round 1, the constructive quantum field theorist, with the Part II page as section P |
| `memo-editor.md` | round 1, the handling editor: outline, rules, abstract, the referee's questions |
| `../PLAN.md` | round 2, the editor's synthesis of the four memos: tiering, outline, figures, rulings, assignments, findings register, verification checklist |

## The rounds

1. **R1, independent reads.** Each member read the record (`part_i/main.tex` and its
   documentation) and wrote its memo without seeing the others'. The four ran in
   parallel on Claude Opus; the model's reasoning effort was the harness default,
   since the per-role agent definitions with `effort: max` were created in the same
   session and are only loaded at session start.
2. **R2, synthesis.** The editor read the three other memos and wrote `../PLAN.md`,
   which the author approved before any drafting.
3. **R3, drafting.** The three domain members drafted the sections the plan assigns
   them; the orchestrator built the figures.
4. **R4, editing.** The editor rewrote the draft in one voice under its own rules.
5. **R5, adversarial verification.** A fresh agent checked every number against
   `part_i/main.aux`, every quotation against `part_i/main.tex`, every status word,
   and the plan's checklist; findings were fixed and the document rebuilt.
6. **R6, record.** Ignore rules, README row, `strategy.md` entry, knowledge-base
   nodes, commit.

## Findings about the record

Section G of each memo lists what its author believes is wrong or unclear in the
record itself. These were never written into the companion: `../PLAN.md` consolidates
them into a register for the author, marking which the orchestrator re-checked at the
source. All were MINOR; none changes a theorem.
