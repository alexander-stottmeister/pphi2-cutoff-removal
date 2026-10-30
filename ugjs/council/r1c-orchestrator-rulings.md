# R1c: the orchestrator's verified facts and rulings for R2

30 October 2026. Written after the five R1 memos (`memo-cqft.md`, `memo-cqft2.md`,
`memo-mp.md`, `memo-aqft.md`, `memo-editor.md`) and the R1b attack memo
(`r1b-attack-cqft.md`, appended below when delivered). Everything here that is not a
report of a page read on an image is `conjectured`.

## 1. Facts the orchestrator verified on the page images (cite with these locators)

GJS, Ann. of Math. 100 (1974); images `<scratch>/gjs74/p-NN.png`, printed page = NN + 583.

- p. 593: "(1.1.5) Q(x_0) = int dx-vec w(x) prod_{i=1}^r :Phi(x_i)^{n_i}:" and "(1.1.6) Q =
  int dx_0 Q(x_0)". "Q is said to be localized if w(x) is supported in a product
  Delta_{j_1} x ... x Delta_{j_n} in R^{2r} where Delta_{j_i} is the unit lattice square in
  R^2 centered at the lattice side [sic] j_i in Z^2. We assume a bound on the n_i in (1.1.5),
  n_i < n-bar." "For a localized monomial Q or Q(x_0), let N(Delta) be the local degree".
  So "localized" is defined for both forms, and (1.1.6) monomials carry space-time kernels.
- p. 594: norms (1.1.7) for Q and (1.1.8) for Q(x_0); (1.1.9) sums over localized pieces.
  "For two localized monomials Q_1 and Q_2, with disjoint localization squares ..., let d be
  the width of the widest strip bounded by two parallel lines, and separating" them.
  "THEOREM 1.1.7. Let m_0, K_2 and K_1 be sufficiently large and let lambda be sufficiently
  small. There are constants 0 < m_1 and O(1) independent of h, Q_1 and Q_2 such that
  (1.1.10) | int Q_1 Q_2 dq_h - int Q_1 dq_h int Q_2 dq_h | <= O(1) e^{-m_1 d} ||Q_1|| ||Q_2||."
  No orientation of the strip is prescribed.
- pp. 594-595, proof of Theorem 1.1.1: "for cutoff functions h_1 and h_2", g = h_2 - h_1,
  g_i = g chi_{Delta_i}; (1.1.12) writes <Q>_{h_2} - <Q>_{h_1} as -int_0^1 d alpha
  sum_{i in Z^2} [<Q V(g_i)>_{h_1+alpha g} - <Q>_{h_1+alpha g} <V(g_i)>_{h_1+alpha g}], "We
  apply Theorem 1.1.7 to each term in the sum", and the sum over i in Z^2 cap supp g of
  O(1) e^{-m_1 dist(O, Delta_i)} is bounded by O(1) e^{-m_1 d/2}. This is the source's own
  use of Theorem 1.1.7 for pairs (Q, V(g_i)) with V(g_i) the interaction integrated over one
  square, i.e. a sum of (1.1.6) monomials, with the sum over squares taken over the plane.
- p. 596: "We let A and B denote monomials of type (1.1.5) of degree |A| and |B| and with
  kernels w_A and w_B respectively. We assume that A is localized at times x_{i0} <= 0, and
  that B is localized at times x_{i0} >= 0. Let B_T denote the translate of B at time T > 0".
  Theorem 1.1.11 chooses "n-th degree polynomials Q_n(t_j) of the form (1.1.5) with r = 1" and
  gives "(1.1.16) | int (A - Q) B_T dq_h | <= O(1) ||A|| ||B|| e^{-gamma T}, uniformly in h".
- p. 597: "Proof of Theorem 1.1.7, assuming Theorems 1.1.8 and 1.1.11. Take n = 0 in Theorem
  1.1.11. Then Q is a polynomial of degree zero, i.e., a constant. From the choice B = I, it
  follows that Q = int A dq_h + O(1) ||A|| e^{-m_0(1-epsilon)T}. After rotating and
  translating the strip separating Q_1 and Q_2 in Theorem 1.1.7, and after choosing A = Q_1,
  B_T = Q_2 in Theorem 1.1.11, the proof follows from Theorem 1.1.8, (1.1.16) and the above
  determination of Q."

Consequence, read off these pages (the orchestrator agrees with `memo-cqft2.md`, section A,
O3): the printed proof of Theorem 1.1.7 reduces a pair to time-separated monomials of type
(1.1.5) by rotating the strip into the time direction. A monomial that is sharp in time
before the rotation is sharp in space after it, and is not of type (1.1.5) in the rotated
frame. The printed statement covers every orientation; the printed proof, as written,
reaches sharp-time monomials only for strips parallel to the time-zero line (the case the
record uses in Lemma 7.4). Space-time-smeared monomials of type (1.1.6) are reached in any
orientation after slicing into sharp-time pieces, which is how the source's own application
on p. 595 is covered.

Erice lectures (LNP 25, 1973), images `<scratch>/erice1/`, `<scratch>/erice2/`: as recorded
in `common:reference/glimm-jaffe-spencer-erice-1973` (reviewed and amended 28 October 2026):
Part I (2.2.7) "int A dq_h <= ||A|| uniformly in h" in a bracketed remark, norm (2.2.5)
without K_2, class of h unspecified, proof referred to the Annals paper and Part II; Part II
footnote 5 asserts that a nonnegative L_infinity cutoff h "does not affect the subsequent
discussion"; Part II Theorems 2.1-2.2 are for regions Lambda and Schwartz kernels.

## 2. What the memos agree on, and where they differ

- Appendix C of the record (`cqft` F1, `editor` F1, both MAJOR): three sentences of the
  mechanism audit (M3 l. 2699, M4 ll. 2708-2709, M5 ll. 2725-2727) say no stability estimate
  enters any constant of the printed proof; GJS p. 624, (2.4.34), cited to Dimock-Glimm, is
  a stability bound under the interpolated measures that fixes K_2 >= K_3^2 and hence every
  downstream constant. Proposition C.1 survives only by its own limitation clause. This is a
  finding about the record, to be repaired in Phase 0 whatever route is taken.
- O1 (section 7 at fixed g): confirmed by all; the instruments differ (`mp`: an L^2 -> L^4
  semigroup bound, Simon Thm V.10 p. 156 or in-house from A2 and A4, plus a Jensen step;
  `aqft`, `cqft2`: the box comparison with time-direction strips, which needs nothing beyond
  CE2 as printed and Appendix C; `editor`: Simon V.10(iii)). Ruling: the plan's Phase A uses
  the box comparison with time-direction strips (no new import; the case the printed proof
  reaches), and records `mp`'s Lemma L as the alternative.
- O3 (comparison trick): `mp`, `aqft` and `cqft2` refute it independently by the same
  construction (reference cutoff = the restriction of h_{T,g} to a fixed box of GJS squares
  around the observable; CE2 as printed for every square outside the box; Lemma C.2 and
  Theorem C.5 for the base term). `cqft` and `editor` confirmed O3 for paths between two
  general cutoffs, which is a different statement. `cqft2` identifies the catch: for the
  sharp-time observable V(h)^2 the squares in its own time row need strips transverse to the
  time-zero line, where the printed statement of Theorem 1.1.7 applies but its printed proof
  does not reach. The orchestrator verified the pages (section 1).
- Level 2 (`cqft`, `editor`): a "verified citation" of the printed proof of Theorem 1.1.8 is
  impossible as defined, because the n = 0, B = I branch is left to "bounded similarly"
  (pp. 621, 627) and because of (2.4.34); the honest end state of an expansion route is a
  theorem of the record (31-46 pp, `cqft`'s Route E1; or an isotropic forest-formula expansion,
  45-70 pp, `cqft2`'s M1), which would also close the transverse case.
- Non-expansion methods (`cqft2`): none fits [0,1]-valued measurable cutoffs; not routes.
- Re-sourcing to Erice (O4): corroboration, never a change of status (all).

## 3. Rulings for the plan (R2)

- R1. The plan's core is the box comparison, in two phases: **Phase A** (section 7 at fixed
  g, time-direction strips only; removes U_GJS from Lemma 4.3, Lemmas 7.1-7.3, 7.6,
  Proposition 7.5, Theorems 7.7-7.8; makes the gap clause of Theorem 12.2(5) rest on CE2 as
  printed, in the case its printed proof reaches) and **Phase B** ((M_2) for every g in C_H
  by the same comparison with transverse strips). Both are written as one note with two
  theorems, audited twice, then integrated.
- R2. The plan states the transverse case as what it is: after Phase B, Theorem 12.2 rests on
  printed statements only, and one of them (A8(iv), Theorem 1.1.7) is used in a case that its
  printed proof does not reach. The record's text, the companion and `docs/` say so in one
  frozen sentence. The author decides at Checkpoint 1 whether "proved from literal imports"
  may then be used (statement scope, the standard of A1-A7) or whether the transverse case
  must first be closed (Phase C). The plan carries both status tables.
- R3. **Phase C** (close the transverse case) is the hard, optional phase: an isotropic
  clustering theorem of the record for sharp-time pairs (`cqft2` M1, or `cqft` E1/E3 adapted;
  45-70 pp estimated), or a cheaper argument if one is found. It is also the only route that
  lifts the record above the A1-A7 standard. The plan prices it and does not schedule it
  before Checkpoint 2. Any research idea for a cheaper closure (for instance an
  energy-weighted moment obtained from the concavity of the ground-state energy and a
  g-uniform local energy-shift bound, which the orchestrator raises as a conjecture and
  nobody has checked) is listed as a scouting memo, not as a phase.
- R4. **Phase 0** (documentation, before any mathematics): repair Appendix C's three sentences
  and Proposition C.1's description (F1), widen A8(ii) to name (1.1.6) monomials and the
  square convention, add the transverse-case remark to A8(iv)'s Scope, correct "the only
  proportionate route" wherever it appears (`docs/imports.md`, the KB nodes
  `problem/level2-h-trace` and `result/hamiltonian-bypass-dead`, companion section 4), and
  correct the page range "598-629" to "600-631". None of this changes a proof.
- R5. Gates follow `part_i/README.md` G0-G6 and the editor's H-K; every phase has a written
  statement, an owner, a page estimate labelled as such, a fallback and a status table. The
  deliverable form is the editor's J (a note in `ugjs/`, integrated into `part_i/main.tex`
  as an appendix or in place so that no existing label moves; the editor decides and says
  why).
- R6. Two author checkpoints: Checkpoint 1 before any mathematics (the standard question of
  R2; Phase 0 fixes; whether Phase A and Phase B are written together); Checkpoint 2 after
  the Phase A/B audits (integrate; whether to start Phase C; the companion's notice).
- R7. Findings about the record from all memos go into one register in the plan with
  severity and who confirmed each at the source; none is applied by the council.
- R8. Status words: Theorem 12.2 is "proved, conditional on U_GJS" until Phase B's gate
  passes and the author's standard allows the change. Every route is `conjectured` until
  written and audited. Costs are estimates.

## 4. The attack memo (R1b)

Delivered 30 October 2026 as `r1b-attack-cqft.md` (1495 words). Verdict of the expansion
reader, who had confirmed O3 in R1 and withdraws that verdict: REPAIRABLE GAP, not fatal.
No error found in the steps of the comparison route; it is the source's own device from the
proof of (1.1.11), p. 595. The gap is the transverse case for the sharp-time observable:
the printed statement of Theorem 1.1.7 covers it (no orientation is prescribed, p. 594), the
printed proof does not reach it (the rotation on p. 597 takes a sharp-time monomial outside
(1.1.5)-(1.1.6)), and neither GJS nor Lemma 7.4 ever uses it. The repair the reader names is
a paragraph declaring this in the import note and a rewording of A8's Scope (b); the
orchestrator's ruling R2 goes further and makes the author's standard the decision of
Checkpoint 1. Smaller repairs named: a written translation-invariance sentence for Theorem
C.5 in the base bound; Theorem C.5 becomes load-bearing and needs its own audit; the box must
be built on GJS squares; the exponent in each term is the strip width, not the distance.
If the route passes its audit, the reader's Route E1 becomes an optional upgrade, and as
scoped it would be the wrong one, since a trace would then have to target Theorem 1.1.7
itself (its transverse case) rather than Theorem 1.1.8.

## 5. Rulings after the R3 verification (30 October 2026)

The verifier's report (`r3-verifier-report.md`: verdict "not yet"; 1 CRITICAL, 4 MAJOR,
20 MINOR) is accepted in full. The orchestrator re-read GJS p. 596 (Theorem 1.1.11 and
(1.1.16), printed "uniformly in h"; "We shall choose t_j = j, j in Z") and p. 600 ("Proof
of Theorem 1.1.8, assuming Theorem 1.1.10 [sic]. Choose T = 0 and B = I in Theorem 1.1.11.
Then Q = 0, so Theorem 1.1.8 is a special case of Theorem 1.1.10 [sic]") on the images.
Earlier the same day the orchestrator also read pp. 622 and 624 on the images (`gjs74/p-39`,
`gjs74/p-41`): Lemma 2.4.6 with "K_2 = K_2(m_0, K_3)", and (2.4.34)-(2.4.35) with "a
constant K_3, independent of C, m_0 and lambda", "These are standard estimates for such
integrals (see [1])" and "which yields (2.4.28), for K_2 >= K_3^2"; this is the reading the
plan's finding F1 attributes to the orchestrator.

- R9 (C1: one standard). The record has one import standard, that of A1-A7: a printed
  statement, used at the scope at which it is printed. A "proof-reached scope" is not a
  standard the record can apply, because under it A8(iv) itself (Theorem 1.1.7) would not
  be reached at any cutoff other than h -> 1: its printed proof obtains its constant from
  Theorem 1.1.8 at the same h (p. 597), and the record rejected that asymmetry on
  5 September 2026. The plan therefore carries ONE status table. The transverse case of
  Theorem 1.1.7 remains a disclosure (sentence F-T), not a second standard; the plan may
  offer the author the option of naming it as a hypothesis "A8(iv)-T" for transparency, but
  must say that this is not a different standard and that A8(iv)-T and U_GJS are different
  statements, neither known to imply the other (M4; wording per the R3b verifier's n7).
- R10 (M1: the literal re-sourcing, adopted as Phase 0'). Under the record's standard, the
  content of U_GJS is a printed statement: Theorem 1.1.11, (1.1.16), "uniformly in h", at
  B = I, n = 0, T = 0, which is exactly the specialization GJS print as their proof of
  Theorem 1.1.8 on p. 600 (and name on p. 629). After an integer time translation, which
  preserves the lattice, the norms and the class of h, it covers every sharp-time (1.1.5)
  monomial at every h in the p. 589 class, hence the slab family, with C_8 = O(1) ||I||, where
  O(1) is the constant of Theorem 1.1.11 at n = 0 and ||I|| = K_1 by (1.1.7). The plan adds
  Phase 0': re-base A8(vi) on Theorem 1.1.11 with the p. 600 specialization; status of
  A8(vi) literal; Theorem 12.2 "proved from the literal imports A1-A8" at documentation
  cost; the constant M keeps its form. Phase 0' is a status change, not a proof, and the
  plan says so; it does not reduce what the record trusts in GJS beyond what it trusts
  today. C5 item 9 already covers (1.1.16); a new item covers p. 600. The plan records why
  the 5 September 2026 reading stopped short of this (it treated (1.1.16) and p. 629 as
  evidence for a reading of Theorem 1.1.8 rather than as the import itself) and says that
  the two readings are the same mathematics with different bookkeeping.
- R11 (what Phases A and B then buy). After Phase 0', Phases A and B are not needed for the
  status of Theorem 12.2 under the record's standard. They are the mathematical content of
  the removal: the record proves "clustering implies the uniform local moment" (D.1-D.4),
  so that the moment bound is a theorem of the record rather than an import, and the GJS
  statements the record imports shrink from two (Theorems 1.1.7 and 1.1.11) to one (Theorem
  1.1.7), at the cost of using that one in its transverse case for the sharp-time
  observable (disclosed by F-T). The plan presents this trade honestly: fewer imported
  statements and a derivation in the record, against one printed statement used beyond
  what its printed proof reaches. Phase A alone uses only strips in the time direction. The
  plan keeps the status table's row "GJS statements imported" so the author can see the
  trade. The orchestrator's recommendation to the author: Phase 0' now; Phase 0 now; Phases
  A and B as the substantive work, at the author's choice; Phase C priced, not scheduled.
- R12 (M3: human readings). As the record does today for C5, the human page readings stay
  user-level open items named beside every status word; no gate waits for a MATCHES verdict.
  Gates record that the checklist items exist with their pages and the text to confirm. The
  fallback clauses that depended on GB2 are rewritten accordingly.
- R13 (M2 and the MINOR items). The grep of gate GB1 is replaced by patterns that see
  `U_{\rm GJS}`, `UGJS` and `C_8`, with the expected surviving lines written into the gate,
  plus `grep -c 'Assume \$U_{\rm GJS}'` printing 0. Every MINOR item m1-m20 of the report is
  applied as the verifier proposes; where a line locator was off by a few lines (m13) the
  verifier's numbers are used.
