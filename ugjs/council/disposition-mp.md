# Disposition by mp of the V1 (cqft) and V2 findings on d1.tex and quantifiers.tex

mp, 3 November 2026. The files are the live `WORK/parts/d1.tex` and `WORK/parts/quantifiers.tex`; backups are `WORK/build-mp/*-before-*.tex`. Line numbers refer to the live files as of 4 Nov 2026, after the V2b edits. quantifiers.tex locators past l. 98 have been moved to match. Statement numbers come from `WORK/build-mp/master-copy.aux`, the full build of the live parts, and shift whenever another part changes. Labels used below:
- Remark N.27 = `aux:d1-def`; Lemma N.28 = `aux:d1-moments`; Lemma D.1 = `lem:D1`; Remarks N.29 = `aux:d1-uses` and N.30 = `aux:d1-check`;
- Lemma N.22 = `aux:notation-sharpid` and Remark N.23 = `aux:notation-sharpidrem` (both cqft2's);
- Lemma N.43 = `aux:d4-QV` (the d4 drafter's). The d4 drafter's identification lemma `aux:d4-ident` was removed at 12:22; d4.tex now cites N.22 and N.23.

## V1 report (cqft)
- cqft-1 (MAJOR: two constructions in D.4): **fixed for my objects.**
  - Lemma N.28(f), statement d1.tex ll. 274-294. (1) The degree-1 monomial at time t is Phi(t,f), for every kernel in L^2 with bounded support; it is proved at ll. 405-412.
  - (2) is now only a citation of cqft2's Lemma N.22 with Remark N.23(a): a one-factor monomial with a bounded kernel at time t equals J_t W_n(f) a.e., and products follow (ll. 281-289; proof l. 414: "not proved again here"). The 42-line proof of (2) was cut on the coordinator's instruction (backup `WORK/build-mp/d1-before-f2-cut.tex`).
  - One sentence (ll. 290-293) says what N.22 does not cover for my objects and why (1) is kept: N.22 needs a bounded kernel and names the degree-1 limit J_t W_1(f). For n >= 2 with an unbounded kernel, Section 2 has no W_n(f) to compare with.
  - Section 7 now cites N.22 and N.23(b) for the identification (quantifiers.tex ll. 198-206, 252-254).
  - D.4's steps, N.21 and Section 8.6: **deferred**, not my files. As of 12:22, d4.tex cites N.22 and N.23(b).
  - The identity is now proved once, in N.22. Remark N.23(c) states the degree-1 case for C_c^infty kernels; (1) covers it for every L^2 kernel with bounded support.
- cqft-2 (MINOR: reading not named; mollifier independence): **fixed.**
  - Remark N.27, d1.tex ll. 238-245, names both readings: the limits as GJS's monomials, with "Wick order with respect to the measure dPhi, as in [9], [1]" from p. 589; and the record's U_h as GJS's V(h), which V3 §12 leaves unchecked.
  - Mollifier independence is the new Lemma N.28(e): statement l. 270, proof ll. 391-403.
  - D.2, Step 4 (d2.tex): not mine.
- cqft-3(a) (MINOR: D.1 labelled plainly "proved"): **fixed.**
  - Status paragraph right after D.1, d1.tex ll. 452-469: "Proved, conditional on repair R8 of the V3 audit"; on the Step-1 route, conditional on Lemma C.4 (R1-R10).
  - Also changed: Step 1, ll. 500-502; Remark N.29(b), ll. 594-597; the input list, ll. 14-18; the Section 7 status line, quantifiers.tex ll. 76-79.
  - gates.tex ll. 6-8: **deferred** to the orchestrator (not my file).
- cqft-3(b) (MINOR: D.2 label in gates.tex): **deferred** to the orchestrator (gates.tex). Section 7's D.2 paragraph names Lemma C.4 as D.2's condition (quantifiers.tex ll. 99-107; see V2b-1 below).
- cqft-3(c) (MINOR: Lemma C.2 "R1-R10"): **fixed**; now "conditional on repair R8", d1.tex l. 562 (formerly l. 481).
- cqft-4 (MINOR: GAP at Lemma 4.3(ii) and at Theorem 5.1, Step 1): **fixed in Section 7.**
  - The GAP is placed at Theorem 5.1, Step 1 (quantifiers.tex ll. 248-254) and at Corollary 5.2 (ll. 262-264).
  - V_* is taken for the constructed object (ll. 53-58), as cqft suggested.
  - consequences.tex l. 27 and the lemma-4.3-ii block: **deferred** to their owner.
- cqft-5 (N_I edit map): **not mine** (consequences.tex, master, record l. 448). Deferred to the consequences drafter and the orchestrator.
- cqft-6 (severity of E1): **not mine** (consequences.tex §8.9; d3.tex). Deferred to the owners.
- cqft-7 (D.3 "parallel case"): **not mine** (comparison.tex l. 53; d3.tex). Section 7 does not use the phrase.
- cqft-8 (MINOR: F-T not carried to D.4's consumers): **fixed in Section 7.**
  - Theorem 5.1, Corollary 5.2, Lemma 10.2, Theorem 11.1 and Theorem 12.2 (1),(5) rest on F-T (quantifiers.tex ll. 245-248); Corollary 5.2 also at ll. 262-264.
  - Section 8.7, the Corollary 5.2 block and the constants.tex rows: **deferred** to their owners.
- cqft-9 (l. 1449 vs 1448): **not mine** (consequences.tex ll. 111-112).
- cqft-10 (D.2(b) "positive width"): **not mine** (d2.tex, gates.tex).
- cqft-11 (MINOR: input lists omit Lemma C.4): **fixed in my parts.**
  - d1.tex: the input list (ll. 14-18) and the status paragraph (ll. 460-462).
  - quantifiers.tex: S_2 "whose proof uses Lemma C.4" (l. 40); D.2 (ll. 99-107); the D.3 order (ll. 117-119); D.4's uniformity in a (ll. 209-210).
  - Master ll. 26-28 and 65-69, and the d3.tex remark: **deferred** to their owners.
- cqft-12 (N.18(iii) on a_0): **not mine** (notation.tex). Section 7's boundary case (9) already listed V_* and the GJS norm of Q_V. Its "only through" sentence is now split into a_0's role in the interaction and its role in the observable (quantifiers.tex ll. 366-372).
- cqft-13 (F-T not verbatim): **not mine** (comparison.tex ll. 47-53).
- cqft-14 (MINOR: two slips in Section 7): **fixed.**
  - N^col_I is removed; l. 135 reads "the column count N^square_I of Remark aux:notation-counts".
  - s_0 is now min over j<=k with e_j != 0 of (2kK_{e_j})^{-1}. If all e_j = 0, then F(z) = E_{mu_g}[conj zeta] is constant and s_0 := +infinity (ll. 166-177).
  - The constants.tex occurrence of N^col_I was cqft2's to fix; as of 12:26, constants.tex contains no N^col_I.
- cqft-15 (0(1) misprint; gates.tex): **not mine** (the record, PLAN, gates.tex). Deferred to the orchestrator.

## My own V1 finding
- F13 (Section 7 omits the GAP from M_B and 9^{p'}): **fixed, in the scope the coordinator set on 3 Nov after cqft2's N.22.**
  - V_*, 9^{p'}, M_B and the Euclidean D.4 need no GAP, because they concern the constructed objects (N.22, N.23(b)). The GAP enters only at Theorem 5.1, Step 1 and at Corollary 5.2.
  - Locations: quantifiers.tex ll. 52-58, 62-64, 198-206, 216-218, 248-254, 262-264.
  - The D.3 order is now the stronger one ("g and I; then A and B'; then s, F and T"), ll. 117-119.

## V2 report
- V2-2 (D.1 status; Remark (b)): **fixed**, as cqft-3(a), following V2-2's repair.
  - New sentence, d1.tex ll. 462-469. Step 1 proves convergence and linearity of the regularized limit from N.28(a) alone. The condition is what identifies that limit with the U_h of Assumption A3, which A3 imports with "[Thm. V.7]" of Simon's book as its source (record main.tex l. 535). The "so that" at ll. 2919-2920 asserts the convergence; it is not a definition.
  - This also reconciles d1.tex with the last paragraph of the proof of N.5(iv), notation.tex ll. 271-281 (cqft2's). As of 12:26 that paragraph labels its route "a reading the record itself does not make" and points to the D.1 status paragraph, so the two parts now agree.
- V2-3 (Lemma C.2: R1-R10 vs R8): **fixed**, d1.tex l. 562.
- V2-4 (two status words): **not a defect in my parts.** `grep -i conjectur` finds nothing in d1.tex or quantifiers.tex, and each statement there carries only the conditional claim. The instances V2 names (comparison.tex, notation.tex, constants.tex) belong to their owners.
- V2-9 (N^col_I undefined): **fixed in Section 7** (quantifiers.tex l. 135). The constants.tex occurrence was cqft2's; none remains as of 12:26.
- V2-10 (s_0 without e_j != 0): **fixed**, quantifiers.tex ll. 166-177, including the all-zero case.
- V2-18 (no run record of check_d1.py): **fixed.**
  - New file `WORK/parts/check_d1.out`. Run 2026-11-03 12:06 CET with /usr/local/bin/python3 3.14.7, numpy 2.5.2 and scipy 1.18.1; script sha256 prefix 0f1e2374d79c0563; seed 20261102. Checks (1)-(5) all pass. These results are numerical only.
  - Referenced in Remark N.30 (d1.tex ll. 623-632) and in Section 7.3 (8) (quantifiers.tex ll. 360-362).
  - The frozen bundle should include parts/check_d1.out.
- V2-21 (N.21(ii) applies R8's action on Gamma_r to the note's H_r): **deferred to cqft2.** notation.tex N.21 is not my part. V2's sentence: "J_0 W_{r,kappa} is a Bochner integral of the Wick monomials :Phi(0,rho_kappa(x-.))^r:, with all r test functions equal, so J_0 W_r lies in Gamma_r directly."

## V2b re-check (appended to V2-report.md, 4 Nov 2026)
- V2b-1 (MINOR: the R8 alternative for D.2-D.4 is not backed by the text): **fixed in Section 7.**
  - quantifiers.tex ll. 99-107 now say that D.2 is conditional on Lemma C.4 of the record (R1-R10). These repairs include R8 and so cover D.1's condition.
  - The clause "under repair R8, gives the same decomposition" is deleted. In its place: R8 alone makes h -> U_h linear but does not give the identification as the note is written.
  - The D.3 line (ll. 130-131) and the D.4 lines (ll. 203-205, 219-220) now read "conditional on Lemma C.4 (R1-R10) through Lemma D.2".
  - The status lines in d2.tex, d3.tex and d4.tex belong to their owners; as of 18:19 they already name Lemma C.4.
- V2b-2 (MINOR: Section 7 describes D.2's old route): **fixed**, quantifiers.tex ll. 101-107, following d2.tex's Step 3.
  - Step 1 of D.1's proof and Lemma N.28(a) give the convergence of the regularizations U^(kappa)_w, w = h - h^B, and of their pieces U^(kappa)_{Delta,n}.
  - Lemma N.5(iii) splits w into the squares.
  - Lemma C.4 identifies the limit with U_h - U_{h^B}.
  - N.18(iv) and N.5(iv) are no longer cited there.

## Further changes in my parts this round
- The Fubini check that this round added to the proof of N.28(f)(2) was removed with that proof; N.22's proof checks its own Fubini step.
- Section 7 cites N.22 and N.23 wherever it mentions the identification (quantifiers.tex ll. 201-202, 252-253).

## Builds (pdflatex twice)
- 4 Nov 2026, after the V2b edits:
  - Stub (`WORK/build-mp/stub.tex`: preamble, d1, quantifiers): 0 errors, 0 Overfull, 16 pp. Its 26 distinct undefined references all point into other parts; none is a label of d1.tex or quantifiers.tex.
  - Full build: `WORK/build-mp/master-copy.tex`, refreshed from the changed `WORK/comparison.tex`, on the live parts. 0 errors, 0 undefined, no ??/TODO in the PDF, 71 pp.
  - One Overfull box, 95.8pt, in gates.tex at the paragraph of ll. 107-115: a long \texttt path, in the orchestrator's file, edited 4 Nov 18:17. My parts have none.
- 3 Nov 2026 (12:27, after the cut of N.28(f)(2)): stub 0/0, 16 pp; full build 0 errors, 0 Overfull, 0 undefined, 67 pp.
