# Audit brief V1: the comparison note (Phases A and B of `ugjs/PLAN.md`), first audit

Object: the note `WORK/comparison.tex` (built PDF `WORK/comparison.pdf`; parts in `WORK/parts/`), where
`WORK/` = `/private/tmp/claude-501/-Users-alex-Documents-Uni-Hannover-claude-glimm-jaffe/8bac9e45-6e21-41a1-bdb8-e018c3356462/scratchpad/phaseAB/`.
Drafters: aqft (§§4–6, §8), mp (§3 Lemma D.1, §7), cqft2 (§2, Appendix A). The drafters' own reports
are in `WORK/REPORTS-drafters.md`. Record: `/Users/alex/Documents/Uni/Hannover/claude/glimm_jaffe/part_i/main.tex`
(42 pp; labels and pages in `WORK/labels-main.txt`). Plan: `ugjs/PLAN.md` (Part 1 statements, Part 3 gates GA/GB,
Part 8 traps). GJS 1974: `glimm_jaffe/refs/Glimm et al. - 1974 - The Wightman Axioms…pdf` (PDF page = printed − 583);
render pages you need with pdftoppm into your own folder `WORK/audits/v1-<name>/`. V3 audit of Lemmas C.2–C.5:
`glimm_jaffe/ugjs/council/v3-appendix-c-report.md` (its repairs R1–R8 are the condition under which the note cites
Lemma C.2 and Theorem C.5). Standard: AGENTS.md §§1–5 (`/Users/alex/Documents/Uni/Hannover/claude/AGENTS.md`).

## Roles
- **cqft (attacker).** Refute. Every application of GJS Theorem 1.1.7 ((1.1.10), p. 594) in §§4–6: are the two
  objects "localized monomials" in GJS's sense (p. 593: types (1.1.5)/(1.1.6), n_i < n̄, kernels, squares), are the
  squares disjoint, is the strip as claimed (orientation, width d), is the cutoff in the class of p. 589, is the
  covariance taken under dq_h at that cutoff, is the constant C₇ c_U ‖piece‖_GJS e^{−m₁d} what (1.1.10) gives? Every
  transverse use flagged (F-T)? The base terms: Cauchy–Schwarz, Lemma C.2, Theorem C.5 with hypotheses checked;
  the 3^{p′} comparison; the Wick/chaos facts used (V3's M-3 and the note's GAP in §2). Lemma D.1's chain (mp's):
  integrability, dominated convergence, the derivative. The replaced proofs in §8 against the record's statements
  (quote the record). The N_I repair (§8.1): is the counterexample right, is the repair complete, does any other
  use of the cell count survive? Boundary cases (T < 1, s on a lattice line, N_g = 1, p′ = 1, ring k = 1, |Λ| = 0). Two source
  claims by drafters to confirm on the page images: GJS (1.1.11) on p. 594/595 prints "0(1)" with a digit zero
  (mp, 300 dpi crop) where the record's l. 814 transcribes "O(1)"; and p. 594's strip-definition sentence has no
  closing period (aqft, cqft2). The V3 repairs are R1–R10 (ten), R8 alone for Lemma C.2.
- **mp (quantifiers).** Audit §§4–6 and §8 (not §3 and §7, which you drafted): the order of quantifiers in each
  statement; for every constant what it depends on and what it is uniform in, against the note's §7 table and
  Appendix A; thresholds as inequalities; every "for all"/"there exists" in the right order; the uniformity in h of
  M_B, in T and s of A, the position of I for B′; the radius s₀ (min over j with e_j ≠ 0); traps 8–11, 17, 20, 25.

## Output
Each auditor writes one report, `WORK/audits/V1-<name>-report.md` (if the harness refuses the write, return it as
your final message): numbered findings, each with locator (section, statement label, line of the part file, PDF
page), the exact sentence or display, why it fails, the repair, and the severity (CRITICAL / MAJOR / MINOR per
AGENTS.md §2); then "holds" items you checked; then "not checked". Verdict sentence first: can D.1–D.4 be `proved`
(conditional on the V3 repairs) as written, or what blocks. Read-only everywhere except your report and your
folder; no git, no kb, no edits to the note or the record. Nothing you did not read is reported.
