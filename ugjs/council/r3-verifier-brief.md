# R3: adversarial verification of `ugjs/PLAN.md`

Round R3, 30 October 2026. The verifier is a fresh agent that wrote none of the memos and
none of the plan. Repository root: `glimm_jaffe/` (public; make no git changes). The
scratchpad is `<scratch> = /private/tmp/claude-501/-Users-alex-Documents-Uni-Hannover-claude-glimm-jaffe/8bac9e45-6e21-41a1-bdb8-e018c3356462/scratchpad`;
page images: `<scratch>/gjs74/p-NN.png` (printed page = NN + 583), `<scratch>/erice1/p-NN.png`
(printed = NN + 131), `<scratch>/erice2/p-NN.png` (printed = NN + 198). Render further pages
only into `<scratch>`.

## What the plan is

`ugjs/PLAN.md` is the council's plan to remove the hypothesis U_GJS (Assumption A8(vi) of
`part_i/main.tex`) from Theorem 12.2. Its core is a comparison argument that rests on the
printed clustering theorem (GJS Theorem 1.1.7, imported as A8(iv)) and on the record's own
Lemma C.2 and Theorem C.5; its open point is that, for the sharp-time observable of
Theorem 5.1, the comparison uses Theorem 1.1.7 across strips transverse to the time-zero
line, a case the printed statement covers and the printed proof does not reach. The author
will approve or amend the plan on the strength of this verification.

## Working rules (the workspace's AGENTS.md binds you)

1. Never state a fact about a file you have not read in this session; never invent a
   number, page, quotation or author. Render the page before asserting what a display says.
2. Read-only on everything except your report file. No `git` command that changes state;
   the only `kb` command allowed is `python3 <KB>/kb.py show <id>`; no edits to any other
   file; no build; do not spawn agents.
3. Treat every sentence of the plan as possibly wrong until the source says otherwise.

## Checks, in this order

A. **Locators of the record.** Every theorem, lemma, equation and line number the plan
   attributes to `part_i/main.tex` exists and says what the plan says: check numbers against
   `companion/council/labels.md`, lines against the file (`sed -n`). List every mismatch.
B. **Page facts.** Every statement about GJS pp. 589-631 and about the Erice lectures is
   checked on the image (or against the verified claims of the KB reference nodes
   `common:reference/glimm-jaffe-spencer-1974`, `common:reference/glimm-jaffe-spencer-erice-1973`,
   which you may trust only for the claims they list as verified). In particular re-read, on
   the images: p. 593 (the two forms (1.1.5)-(1.1.6), "localized", the square convention,
   n_i < n-bar), p. 594 (Theorem 1.1.7 and the strip definition), p. 595 ((1.1.12) and the
   application of Theorem 1.1.7 to pairs with V(g_i)), p. 596 (type (1.1.5) in Theorem 1.1.11,
   (1.1.16)), p. 597 (the rotation sentence), p. 622 and p. 624 ((2.4.34)-(2.4.35) and the
   citation to [1]). Decide for yourself whether the plan's description of the transverse
   case is right: does the printed proof of Theorem 1.1.7 reach a sharp-time monomial across
   a strip transverse to the time-zero line, or not?
C. **The statements to prove (Part 1).** For each statement: are the quantifiers complete;
   is the dependence of every constant stated; does it match exactly what the record
   consumes (Lemma 4.3(ii) ll. 1085-1121; Theorem 5.1 Steps 5-6 ll. 1218-1250; Lemmas
   7.1-7.3 ll. 1329-1425; Lemma 7.6 ll. 1504-1536; Lemma 10.2 ll. 1992-2013; Theorem 12.2(5)
   ll. 2311-2317)? Is anything consumed that the statement does not deliver (for example
   T > 0 versus T >= t_*, C_H versus G, the centred versus the full moment, sharp-time
   versus smeared)?
D. **The argument itself (an attack).** Re-derive the comparison route independently from
   the plan's description and try to break each step: (1) the differentiation identity along
   the affine path and its integrability (A3 ll. 516-535; Lemma C.2 ll. 2771-2784; Theorem C.5
   ll. 2859-2912); (2) the box on GJS squares, the strip widths, the convergence of the sum
   over squares outside the box uniformly in T and in the cutoff; (3) the admissibility of
   the pair (sharp-time product monomial, one-square (1.1.6) interaction piece) under the
   printed statement, and the norm of the interaction piece; (4) the base term via
   Cauchy-Schwarz, Lemma C.2 and Theorem C.5, including translation invariance; (5) the
   passage to Omega_g (Theorem 5.1 Steps 5-6) and to Lemmas 7.1-7.3, 7.6; (6) the hypotheses
   of Theorem 1.1.7 versus the standing assumption ll. 884-899. Name the weakest step.
E. **Status words and the two tables (Parts 0, 7).** Under each standard, is each status word
   justified by the plan's own definitions? Does the plan anywhere call a route proved, or
   Theorem 12.2 anything other than "proved, conditional on U_GJS" as of today?
F. **Phases and gates (Part 3).** Is every gate checkable (a command, a count, a document, a
   named reviewer)? Does every phase have a fallback? Are the page estimates labelled as
   estimates? Is anything scheduled before an author checkpoint that the checkpoint is
   supposed to decide?
G. **The findings register (Part 9).** Open each locator; confirm or refute each finding you
   can reach; say which you did not check.
H. **Internal consistency.** Parts that contradict each other; a constant named differently in
   two places; a phase number used inconsistently; a frozen sentence that differs between
   Parts 0 and 8.
I. **What the plan omits.** Anything a sceptical referee or the author would ask that the plan
   does not answer.

## Report

Write `ugjs/council/r3-verifier-report.md`: (1) a verdict in one line (the plan can go to the
author as is / after the listed fixes / not yet); (2) findings, each with locator in the
plan (Part and line), the exact sentence, what is wrong, the repair, and a severity
(CRITICAL: the plan's core argument or a status claim is wrong; MAJOR: a gate, a statement
or a locator is wrong in a way that would mislead the author; MINOR: wording); (3) the list
of what you checked at the source, page by page and line by line; (4) what you could not
check. Report back to the orchestrator in your final message: the verdict, the counts by
severity, and the CRITICAL and MAJOR items in one line each. Do not paste the report.
