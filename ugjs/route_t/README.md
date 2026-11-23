# Route T: a note for Phase C3 of `../PLAN.md`

`route_t.tex` (33 pages) was commissioned by the author on 23 November 2026, after the status
council of 22 November proposed "Route T" as the content of Phase C3. It was written by an AI
agent (Claude Opus), audited the same day by two other agents that had written none of it, revised,
re-checked by both, revised once more for the re-checks' MINOR points, and confirmed by one of
the two on 24 November. **Nothing in it has been read by a human, and it is not integrated into
the record: `../../part_i/main.tex` and its Theorem 12.2 are unchanged by it.**

## What it shows

Its Theorem T.2 is "proved, conditional on" the imports A1–A8 of the record (A8(iv) used only in
the cases P1–P4, A8(iv)-T not used, A2 used at two times placed asymmetrically in a slab), the
readings the record declares (Scope paragraphs of A1, A3, A6 and A8, with the open items of
`../../part_i/C5_reading_record.md`) and the record's statements the note lists, used as the
record states them, by the two audits: items (1)–(4) of Theorem 12.2 hold with the same limit
state and a different rate function, which still decays faster than every inverse power, and so
does Corollary 12.3 in its restricted form of 23 November (𝒫(ξ) = ξ⁴, cutoffs 0 ≤ g ≤ 1; it
rests in addition on the reading of A1's Scope applied to GJ3, which the record names after it),
without Theorem 5.1, Theorem D.4 and the transverse sharp-time case A8(iv)-T of GJS Theorem
1.1.7. The note's Theorem T.2(b) repeats the statement of 49f2d23, which covered every cutoff of
GJ3 and which the record's audit of 23 November found to go beyond its proof (see the note's
first page). The moment M of the record is replaced by
a resolvent-weighted quantity, bounded through a time-integrated copy of Theorem D.4. No input
beyond the record's imports is added.

What it does not show. Every application of Theorem 1.1.7 that it adds pairs two time-integrated
monomials (its cases P3, parallel, and P4, transverse). These lie within the printed statement of
the theorem. The printed proof reaches them only if GJS p. 596 is read as allowing the monomial
A of Theorem 1.1.11 to have factors at different times (reading R1 of the note). That is the
reading under which GJS's own proofs are complete (pp. 595, 600, 629), and no printed sentence
states it; for P4 the note also presupposes that rotating the setting is covariant. ("Reached" is
the note's term for the scope of the printed proof, not its correctness. One question remains for
every application alike, in the record as here: the printed proof takes its constant from
Theorem 1.1.8 at the same h, p. 597.) So Route T
exchanges a case that no reading of the printed proof reaches for cases reached on that reading.
The moment clause of item (5) of Theorem 12.2, Theorem 5.1 and Corollary 5.2 still rest on
A8(iv)-T. The note's Proposition T.19 also settles the question that Remark N.39 of the record
leaves open: the parallel pairs behind the uniform gap are reached by the printed proof after
slicing in time, on either reading, subject to that common question.

## Files

| file | what it is |
|---|---|
| `route_t.tex`, `route_t.pdf` | the note; it refers to the record at commit 49f2d23 (statement numbers are those of the record at 9733263 as well; pages differ, and so does the statement of Corollary 12.3) |
| `check_route_t.py`, `check_route_t.output.txt` | numerical corroboration of its elementary identities and inequalities (23 checks pass); nothing in the note is deduced from it |
| `../council/route-t-drafter-report.md`, `../council/route-t-revision-report.md` | the drafter's reports on the draft and on the two revisions |
| `../council/route-t-audit-analysis.md` | audit of the analysis (T.1–T.16 and the proof of T.2), its re-check and its confirmation of the last round |
| `../council/route-t-audit-sources.md` | audit of the note's claims about the sources and about what rests on what, and its re-check |
| `../council/route-t-docs-check.md` | check of this file, of the note's first page and of the public sentences about the note, before the commit: 1 MAJOR and 8 smaller points, applied |

Findings: no CRITICAL or MAJOR point in either audit. All MINOR points of the audits and of the
re-checks were applied. Of the three points of the last confirmation (two MINOR, one cosmetic), the second
(on the record of 23 November) is taken up on the note's first page; the other two are open and
named there. The first-page sentences about the last confirmation and about Corollary 12.3 were
written by the orchestrating agent after that confirmation; only the documentation check of
24 November (`../council/route-t-docs-check.md`) read them, and they were corrected for its
findings. The corrections were not checked again.

A point for the record that the audit raised: Assumption A2 is stated for all bounded time-zero
functions, while the multi-time theorems it cites (Simon's Theorem V.15, GRS Theorem II.16) print
the interior functions as functions of finitely many fields; for other bounded functions the
printed basis is the Remark after Theorem V.15, which the source does not prove. The record's
Lemma 4.1 relies on this. Step 1 of the proof of Lemma T.15(ii) of the note derives the two-time case it
uses from the bounded case of Theorem V.15 by approximation; by the auditor's remark the same
argument would serve the record's Lemma 4.1. It is not yet in the record.

## Build

```sh
SOURCE_DATE_EPOCH=1795392000 FORCE_SOURCE_DATE=1 pdflatex route_t.tex   # x3
```

Three passes reproduce the committed PDF under pdfTeX 1.40.29 (TeX Live 2026): 33 pages, no
errors, no overfull boxes, no undefined references.
