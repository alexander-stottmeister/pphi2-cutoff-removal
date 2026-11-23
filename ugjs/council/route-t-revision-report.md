# Route T note: revision after the two audits (drafter "route-t", 23 November 2026)

## 1. Outcome

I revised `route_t.tex` for every finding of both audits; all were MINOR, and every one was applied. The most important change removes Simon's Remark on p. 164 from Lemma T.15(ii) by a written truncation argument, which uses only A2 for bounded functions and the record's Lemmas N.32, 3.1(ii) and 4.3(ii), and A5(i). Route T therefore adds no input to the record's imports. The rebuilt note has 30 pages, builds cleanly, and its check script passes (23 PASS). The statement numbering T.1–T.19 is unchanged; there are no new statements, only two new displayed equations, (t7) and (t8), inside the proof of T.15.

## 2. What items (1)–(4) rest on after Route T (the final answer)

If the note were integrated, items (1)–(4) of Theorem 12.2 and Corollary 12.3 would carry the rate Ψ̃_{m₁}. In the original coordinates that rate is d ↦ Ψ̃_{m₁,*,λ₀}(s d), with s = m₀/M_*, by Remark 3.3(1). The items would be **proved, conditional on**:
1. **A1–A8 of the record.**
   - A8(iv) is used only in the cases P1–P4; A8(iv)-T is not used.
   - A2 is used with two times placed asymmetrically in a slab, as formula (3) of Lemma 4.1 uses one time. This is within A2's words "the analogous multi-time formulas on finite slabs", stated for bounded functions.
   - Simon's Remark on p. 164 is not used.
2. **The readings the record declares:** the Scope paragraphs of A1, A3 and A6, and A8 Scope (d), together with the open items of `part_i/C5_reading_record.md`.
3. **The record's statements, used as the record states them:** those listed in the note's §4(c) and §7.1.

**Under the standard "only cases the printed proof reaches"** the items are conditional in addition on:
- reading R1 of GJS p. 596, for P3 and P4;
- for P4 only, the rotation presupposition: that the rotation by π/2 the printed proof performs carries dq_h to dq_{h∘ϱ⁻¹} and the constructed monomials to those with rotated kernels. Neither the record nor the note proves it.

The question of the constant, which the printed proof takes from Theorem 1.1.8 at the same h, is common to every case, as in the record.

**On reading R2:**
- the pieces of P3 and P4 with both degrees n, n′ ≥ 1 are not reached;
- the record's A8(iv)-T is not reached on either reading.

R1 is the reading under which GJS's own proofs are complete: p. 595, and pp. 600 and 629. No printed sentence states it in words.

**What stays as in the record:**
- The gap clause of item (5) rests only on P1 and P2, which are reached on either reading.
- The moment clause of item (5), Theorem 5.1 and Corollary 5.2 still rest on A8(iv)-T.

**Section 13.** Theorem 13.2 uses Lemma 9.3 with the bounded X = B, Theorem 7.8, and items (1), (3), (4) of Theorem 12.2 only through local-norm convergence, the ground-state property and translation invariance. It uses neither M nor Ψ_{m₁}. After Route T it rests on what those items rest on. I verified this by reading `main.tex` ll. 3170–3274 at 49f2d23.

## 3. Disposition of every finding

"Before" gives the locator in the audited draft, as the audits cite it. "After" gives the lines of the revised `route_t.tex` (1812 lines).

### 3.1 Audit of the analysis (`route-t-audit-analysis.md`)

**A-F1 (MINOR): Simon's Remark on p. 164 in T.15(ii). Applied.**

The finding was re-checked at its source:
- A2, `main.tex` ll. 825–838, is stated "For all bounded time-zero functions" and adds "the analogous multi-time formulas on finite slabs".
- Formula (3) of Lemma 4.1 (ll. 1725–1735) already places one time s anywhere in [−T, T].
- Simon's Theorem V.15 is printed for arbitrary t_j > 0 with "s₀ arbitrary" (pp. 163–164, read).

My conclusion: A2 as stated covers the asymmetric two-time formula for bounded functions. The note says so plainly, with these three reasons (l. 972 ff.).

What changed:
- **The proof of T.15(ii)** was rewritten (before: ll. 940–965; after: ll. 972–1027).
  - Step 1 applies A2 to bounded functions at −T < τ < τ′ < T, giving equations (t7) and (t8), with the energy shift and the reality argument.
  - Step 2 truncates with X^{[ℓ]} = (−ℓ)∨(X∧ℓ). It proves J_τ(X^{[ℓ]}) = (J_τX)^{[ℓ]}, using that clipping is 1-Lipschitz, that cylinder functions are dense, and that J_τ is an isometry.
  - On the path side, dominated convergence uses the majorant |J_τX||J_τ′X|. That majorant is integrable because J_τX ∈ L⁴(dμ₀), Lemma N.32 at h_{T,g} ∈ C_E (Lemma 3.1(ii)) gives J_τX ∈ L²(dq), and Cauchy–Schwarz applies.
  - On the Hilbert side, ψ_b ∈ D(X) by A5(i), and dominated convergence with the dominator |X|²|ψ_b|² gives the limit, as in the computation of Lemma 4.3(ii).
  - I checked both dominated-convergence steps myself, not only as the auditor described them.
- **The conditions were updated:**
  - the Summary (l. 90 ff.);
  - the status of T.2 (ll. 262–270);
  - the paragraph on the role of the cutoff (l. 1064 ff.);
  - §7.1, rows T.2, T.15 and T.16;
  - §7.2.
- **One sentence was kept** saying that Simon's Remark would give (ii) directly but is not used (l. 1025).

**A-F2 (MINOR): strict inequalities in T.9, Step 3. Applied.** The text now reads y ≤ a_O − d and y′ ≥ b_O + d, so y′ − y ≥ b_O − a_O + 2d > 2 (before: ll. 582–583; after: ll. 612–615).

**A-F3 (MINOR): the reason given in Definition T.1. Applied.** It now reads "because H(g) is self-adjoint and |λ₀ − iE| ≥ λ₀ for real E" (before: ll. 149–150; after: l. 171).

**A-F4 (MINOR): coordinates, and the integration list. Applied.**
- I verified Remark 3.3, `main.tex` ll. 1610–1708, and added a "Coordinates" paragraph after T.2 (l. 255).
- The §7.3 integration list was extended (l. 1729 ff.), together with S-F7.

**§13 result (§5 of the analysis report). Verified and added to §7.2** (l. 1711).

### 3.2 Audit of the sources and dependencies (`route-t-audit-sources.md`)

**S-F1 (MINOR): the evidence for R1. Applied.**

I rendered and read the pages myself on 23 November 2026:
- p. 590 (PDF page 7);
- p. 600 (PDF page 17);
- p. 628 (PDF page 45, the top of the page at 200 dpi);
- p. 597 and p. 629, which I had rendered earlier.

What changed:
- **§5.1 gained the printed sentences** of p. 590 (Theorem 1.1.1), p. 597 (θ_A), p. 600 (with the record's [sic] at ll. 1236–1238), p. 628 (Q_n(y₀)) and p. 629 (ll. 1150–1199).
- **§5.3 was rewritten** (before: ll. 1151–1157; after: ll. 1241–1286):
  - points (a)–(d) in favour of R1;
  - the old R2 argument withdrawn, because p. 628 builds Q_n(y₀) with up to n factors at one time;
  - "no printed sentence states R1 in words" kept, in the narrow sense;
  - R1 named as the reading under which GJS's own proofs are complete.

**S-F2 (MINOR): a new import missing from the Summary. Resolved by A-F1.** The Remark is no longer used. The Summary now says that Route T adds no input. The phrases "A2 imports this theorem" and "the instance of A2" were removed.

**S-F3 (MINOR): T.17(c) on R1, and the P4 presupposition. Applied.**
- **The P3 integration is written out** in four steps (ll. 1365–1430):
  1. an L⁴-Bochner representation of the slices and the double integral of the two-factor piece;
  2. the covariance as a bounded functional, used twice;
  3. one triple of slices;
  4. the integration.
- **For P4 on R1** the statement is now conditional on the rotation presupposition (l. 1431). The presupposition is defined in §5.4 (l. 1324) and carried into §5.5 (ll. 1505 ff., 1534 ff.), §7.2 and the Summary.
- **I did not write the x¹-sliced analogue** of T.12, which the auditor offered as an alternative.
- **The status of T.17 was changed.** Proved: (a), (b), (d), P3 on R1, and everything on R2. Proved, conditional on the rotation presupposition: P4 on R1.

**S-F4 (MINOR): degree-0 pieces. Applied.**
- T.17(c) now reads: the pieces with n, n′ ≥ 1 are not reached on R2; the degree-0 pieces are reached.
- The proof's paragraph "On R2" (l. 1443) gives the argument: λa₀∫h′_k is a constant, and the remaining factor is a time-integrated monomial with r = 1.
- T.18 now says "r ≥ 2 factors of positive degree".
- The Summary was qualified to match.

**S-F5 (MINOR): T.18 claimed more generally than proved. Applied.**
- T.18 is retitled "an argued observation" (l. 1467) and restricted to boxes of fixed shape.
- Lemma N.7(iv) is now cited as holding for every rectangle of squares.
- The note says that a box growing with supp h escapes the argument, Theorem D.3 being of that kind.
- In §7.1 the two ingredients are marked proved and the conclusion an argued observation.
- The Summary's qualifier "around a box of fixed shape" is restored.

**S-F6 (MINOR): translations, and the rotation by π. Applied.**
- I verified Remark N.2(ii) (l. 4289) and Lemma N.13(ii),(iv).
- §5.4 now has a "Translations" item (l. 1310). For two-time slices it adds that splitting a local degree does not increase the norm, since n!n′! ≤ (n+n′)!.
- "Rotation by π" is replaced by relabelling Q₁ ↔ Q₂, which (1.1.10) permits because it is symmetric, in three places: the definition of "reached", the proof of T.17(a), and the proof of T.19(iv).

**S-F7 (MINOR): where Theorem 5.1 enters, and the integration list. Applied.**
- §4(c) now quotes `main.tex` ll. 3104–3106. That passage routes (M₂) into items (1)–(2) through Theorem 11.1, and into item (5) directly (l. 1123 ff.).
- The §7.3 list (l. 1729 ff.) now has every site of both auditors' lists. I checked each line in the frozen `main.tex`:

  | lines | content |
  |---|---|
  | 120–124 | the "Integration of Appendix D" paragraph |
  | 237–241, 351 | the rate in the introduction |
  | 251, 257 | the strategy table |
  | 280 | the dependency display |
  | 356–368 | Pillar 1 |
  | 613, 618, 619 | notation rows M, Ψ_γ, d₀ |
  | 1166–1169, 1369–1377 | A8 (iv-T) "Used in", A8 Scope (b) |
  | 1656–1657, 1698–1701 | Remark 3.3 |
  | 2921 | head of §11 |
  | 3083–3099 | imports paragraph of Theorem 12.2 |
  | 3291 | the Discussion |
  | 3369–3372, 3378 | Appendix A rows |
  | 4087–4101 | Proposition C.7 |

**S-F8 (MINOR): two readings presented as printed. Applied.**
- Corollary 1.1.9's "Apply the theorem to" is now quoted, and its identification with Theorem 1.1.8 is marked as a reading (l. 1180).
- Theorem 1.1.1 is quoted from p. 590 (l. 1150), and the p. 595 step is named as "the cutoff Schwinger functions converge" (l. 1283).

**S-F9 (MINOR): the undefined "(iii)". Applied.** §5.5, item "The category" (l. 1505), now spells out the three categories of the commission.

**S-F10 (MINOR): provenance of R1. Applied.** A "Provenance" paragraph (l. 1267) cites:
- Remark N.39 (l. 6816);
- Definition N.26(b) (l. 5750);
- Remark N.27 (l. 5783);
- `ugjs/PLAN.md` Part 2, ll. 312–315.

I read each in the frozen copy.

**S-F11 (MINOR): a path and undated sentences. Applied.**
- The path is now `ugjs/route_t/route_t.tex` (l. 1637).
- "This session" became "on 23 November 2026" (l. 137). The §7.1 row that used the phrase was rewritten.
- A grep finds no "in this session" left.

**S-F12 (MINOR): the status of T.19. Applied.** It is now aligned with T.14 (l. 1591, and the §7.1 row): (i)–(iii) are proved, conditional on A8(iv) for one-time parallel pairs, A3, and the reading of A8 Scope (d); (iv) is a statement about the printed proof.

### 3.3 The coordinator's item 5: the first page. Applied (ll. 63–72)

The first page now states:
- the date;
- that the note was written by an AI agent (Claude) under the author's supervision, for Phase C3;
- that two independent agents audited it, with the report paths and the appended re-check;
- that no human has yet read it;
- that it is not integrated, and Theorem 12.2 is unchanged;
- that it cites the record at 49f2d23, and that the record of 23 November 2026 has the same numbers and different pages.

I checked the last sentence against the repository's `part_i/main.aux`, built at 13:50 on 23 November: it has 238 labels, no statement number differs from 49f2d23, and 190 labels are on different pages. For example, `thm:MAIN` 12.2 is on p. 41 at 49f2d23 and on p. 42 there.

### 3.4 Not applied

None. One alternative was not taken, as explained under S-F3: the x¹-sliced analogue of T.12 was not written; the P4 claim is stated conditionally instead.

## 4. New statements

None; T.1–T.19 keep their numbers (`route_t.aux`). The new material is:
- equations (t7) and (t8), in the proof of T.15(ii);
- proof steps within T.15(ii), T.17(c) and T.19(iv);
- the rewritten Remark T.18;
- §5.3, §5.4, §5.5, §7.2, §7.3, §7.4 and the Appendix, rewritten or extended.

## 5. Checks actually run

- **Build.** Three passes of `/Library/TeX/texbin/pdflatex -interaction=nonstopmode route_t.tex`.
  - `^!`: 0; Overfull: 0 (two intermediate overfull boxes were fixed); undefined: 0.
  - The forbidden-string grep on the PDF text gives no output (exit 1).
  - `pdfinfo`: 30 pages. `pdftotext | wc -w`: 19,388 words.
  - No machine paths in the note, the script or the diff (a grep for machine-path prefixes).
- **Labels.** `route_t.aux` lists T.1–T.19 at pp. 3–26 and (t1)–(t8).
- **`check_route_t.py`.** Two checks were added and the script rerun: 23 PASS, "ALL CHECKS PASSED". Run with the system python3: Python 3.14.7, numpy 2.5.2, scipy 1.18.1, mpmath 1.4.1; seed 20261123.
  - **Check 14:** the truncation limit of T.15(ii), Step 2, in a Gaussian toy, using the Mehler expansion with 120 terms. The errors |E[c_ℓ(X₁)c_ℓ(X₂)] − 2ρ²| for ℓ = 0.5, 2, 8, 32, 64 are:

    | ρ | ℓ = 0.5 | ℓ = 2 | ℓ = 8 | ℓ = 32 | ℓ = 64 |
    |---|---|---|---|---|---|
    | 0.9 | 1.47 | 0.894 | 8.39e-2 | 1.03e-6 | 2.11e-13 |
    | 0.3 | 1.40e-1 | 9.21e-2 | 1.03e-2 | 1.16e-7 | 2.36e-14 |

    The sanity check on the unclipped Wick square has error 1.5e-13.

    **The first run printed FAIL.** That run stopped at ℓ = 32 with an a priori tolerance of 1e-6, and the true truncation error at ρ = 0.9, ℓ = 32 is 1.03e-6. I then added ℓ = 64. The failing output is kept as `work/route-t/check_route_t.output.revision-run1.txt`, and the note's Appendix records it.
  - **Check 15:** the free two-time formula of T.15(ii) at λ = 0, position space against momentum space, for u = 0.3, 1, 2.5. The relative difference is 1.7e-15 (tolerance 1e-8).
  - These checks are numerical only; nothing in the note is deduced from them.
- **Sources rendered and read:**
  - GJS p. 590 (PDF page 7), p. 600 (PDF page 17), and the top of p. 628 at 200 dpi (PDF page 45);
  - GJS pp. 593–597 and 628–629 from earlier;
  - Simon pp. 163–164.
- **Record passages read in the frozen copy:**
  - A2 (ll. 825–838); Lemmas 4.1 and 4.3;
  - Remark 3.3 (ll. 1610–1708);
  - §13 (ll. 3163–3274);
  - Proposition C.7 (ll. 4087–4120);
  - the Discussion (ll. 3285–3295);
  - every line in the S-F7 / A-F4 lists (§3.2 above);
  - Remark N.2(ii), Lemma N.13, Definition N.26(b), Remark N.27, Remark N.39 (l. 6816);
  - `ugjs/PLAN.md` ll. 301–320.
- **Diff.** `reports/route-t-revision.diff` is a unified diff of `route_t.tex` against the audited draft: 954 lines, 517 added and 211 removed. The audited draft was saved before any edit as `work/route-t/route_t.audited-draft.tex` (sha1 4fbb322e…, identical to the audited file).

## 6. Not done, not verified, not run

- **Not done:**
  - integration into `part_i/main.tex`;
  - a proof of the rotation presupposition (the x¹-sliced analogue of T.12);
  - a decision between R1 and R2;
  - a proof of A8(iv)-T;
  - an evaluation of S₂(B_{3×5});
  - any proof of GJS;
  - a re-audit of the record statements the note cites.
- **Not verified:**
  - the Discussion's "super-polynomial but sub-exponential" (l. 3291), for Ψ_{m₁} and for Ψ̃_{m₁}; the note says so;
  - the auditors' own scratch scripts.
- **Not run:**
  - an independent re-check of this revision (the auditors' appended re-check is pending);
  - no git command; no subagents.

## 7. Files written

All are in the council's scratch directory (`scratchpad/c2/`), outside the repository; nothing was written under REPO.
- `route_t/route_t.tex` (revised, 1812 lines) and `route_t/route_t.pdf` (30 pages), with the build by-products.
- `route_t/check_route_t.py`, with checks 14 and 15 added; `route_t/check_route_t.output.txt`.
- `work/route-t/route_t.audited-draft.tex` and `work/route-t/check_route_t.output.revision-run1.txt`.
- `work/route-t/new_sec54_55.tex` and `work/route-t/new_sec7.tex`: edit fragments.
- `work/route-t/gjs-p7-07.png` and `work/route-t/gjs-p45top-45.png`: renders.
- `reports/route-t-revision.diff` and `reports/route-t-revision.md` (this report).

## Second round (after the re-checks)

I re-checked each point at its source and applied all of them. Nothing is left undone. The statement numbering T.1–T.19 and the equation numbering (t1)–(t8) are unchanged (`route_t.aux`). Before editing I saved the version the re-checks read as `work/route-t/route_t.rechecked.tex` (sha1 86742cce…). `reports/route-t-revision2.diff` is the diff against it: 362 lines, 164 added and 62 removed. Line numbers below are those of the new `route_t.tex`, which has 1916 lines.

**1. Analysis R1: the printed basis of (t7) for functions not of finitely many fields. Applied.**
- **Re-checked at the source.**
  - Simon's Theorem V.15 (p. 163, rendered at 220 dpi) is printed for "measurable functions on R^k with |G_j(x)| ≤ C(1+|x|^N)" of φ_F(f_1), …, φ_F(f_k), with "f_1, …, f_k ∈ F".
  - Its proof on p. 164 treats the bounded case first ("Suppose first that G_0, …, G_n are bounded … This proves (V.47) in case are bounded").
  - GRS's Theorem II.16 (image `grs-fkn-40.png`) likewise has G_i of finitely many fields at the interior times.
  - A2 (ll. 825–838) is stated "For all bounded time-zero functions".
- **The new Step 1 of T.15(ii)** (ll. 996–1062) writes out the auditor's argument in five items.
  1. Bounded cylinder approximants F_i^{(m)} = c_C∘P_{i,m}, with |F_i^{(m)}| ≤ C and F_i^{(m)} → F_i in L². The polynomials are dense by A1(c), using the density of S(R) in H_C; this is the density by which N.22 extends J_τ.
  2. (t7) for the approximants, by the bounded case of V.15 as printed, with every hypothesis checked: n = 3, t_j > 0, G_0 = G_3 = 1, bounded G_j (N = 0), g ∈ L¹∩L^{1+ε}, the dictionary of A2, and the complex conjugate for A2's ordering.
  3. The Hilbert side converges: dominated convergence along subsequences, then the boundedness of the semigroup.
  4. The path side converges: J_τ is an isometry, |J_sF| ≤ C, and e^{−U} ∈ L² by A3.
  5. The conclusion; Z(h_{T,g}) is obtained the same way.
- **The clipping identity** J_τ(c_ℓ∘F) = c_ℓ∘J_τF moved into a new Step 0 (l. 987). It gives |J_τF| ≤ C as well, and Step 2 refers back to it.
- **The class of the f_j.** Simon's symbol F ("Let f_1, …, f_k ∈ F") is not restated on pp. 163–164, and I did not find its definition elsewhere in the book's text layer. The note therefore says that real Schwartz functions belonging to F is the reading under which A2 cites V.15 for the record's time-zero fields (item (2), ll. 1026 and 1036).
- **The Remark.** The sentence on Simon's Remark now says that the proof "uses it nowhere, neither for V(h) nor for the bounded truncations" (l. 1096).
- **For the record (§7.3, l. 1851).** One sentence says the same remark applies to the record's own Lemma 4.1. Its printed basis for bounded functions not of finitely many fields is Simon's Remark or this approximation. This is a point for the record, not for this note.

**2. Analysis R2 and sources F17: the inventories. Applied.**
- §7.1, row T.2: the statements are those "listed in §4(c) and in the rows of this table" (l. 1747).
- §7.1, row T.15 (l. 1765 ff.) adds A1(c), A1(d) and Lemma N.22 (the definition of J_τ, its density extension and its isometry). It also names the derivation from V.15's bounded case.
- §4(c) adds the inputs of Lemma T.15 (l. 1192): Lemmas 3.1(ii), 4.4, N.22 and N.32; the computation of Lemma 4.3(ii); and A1(c), A1(d), A2 (with V.15 as printed behind it), A3 and A5(i).
- **Analysis R3:** the header comment (l. 3) now reads "Audited by two independent agents and re-checked on 23 November 2026; revised for their findings. Not integrated into the record."

**3. Sources F13, F14, F15, F18. Applied.**
- **F13.** I verified A2's parenthetical (ll. 835–838) and its "Used in" line (l. 848). Both are now on the §7.3 integration list (l. 1831).
- **F14.** The status line of T.17 (l. 1440) and its §7.1 row now except the reach of P4's degree-0 pieces from the unconditional R2 assertions. That reach is proved conditional on the rotation presupposition.
- **F15.** The "Translations" item (l. 1381 ff.) now says "raise no question in P1–P3; in P4 … at most a bounded factor".
  - The one-line identity Φ_κ(z)∘T_a = Φ_κ(z+a) is added. It is taken from the proof of N.13(iii) and uses c_κ independent of z, so a constructed monomial composed with T_a is the one with the translated kernel. The limits agree because F ↦ F∘T_a is an L² isometry (N.13(i)).
  - P3 cannot merge factors: both start in row 0.
  - For P4 with k ≠ k′, a non-integer translation can merge the two factors and raise the weight by (n+n′)!/(n!n′!) ≤ 2^{n+n′} ≤ 2^{4p′}. Integer translations avoid this at the price of at most one unit of T in (1.1.16), a factor at most e^γ. Either way this is a bounded factor, of the same kind as the constant question, and no verdict changes.
  - §5.5, item 3 (l. 1642) is adjusted to match.
- **F18, first part.** The degree-0 cross-reference (l. 1542) now reads: both partners are time-integrated with one factor, and both are sliced, so Steps 1–4 apply with one-factor slices. For P4 this is granted the rotation presupposition.
- **F18, second part.** "The commission" is now defined in §1.1 (l. 150) as "the author's commission of 23 November 2026 for this note (Phase C3 of ugjs/PLAN.md)", which asked for items (a)–(d) and for the three categories of §5. The four uses refer to it.

**4. Sources F16: the first page. Applied.**
- **Title block.** It now reads "Written by an AI agent (Claude), commissioned by the author and supervised by the council's orchestrator (an AI agent) … revised after two independent audits and their re-checks".
- **Status paragraph** (ll. 65–81), now itemized:
  - authorship (commissioned and supervised as above);
  - two audits and one re-check each on 23 November 2026, with the report paths `ugjs/council/route-t-audit-analysis.md` and `ugjs/council/route-t-audit-sources.md`, none CRITICAL or MAJOR;
  - the last round of MINOR points applied after the re-checks;
  - "Nothing in it has yet been read by a human";
  - "This note changes nothing in the record: it is not integrated, and Theorem 12.2 of part_i/main.tex is stated and proved there as before";
  - the record at 49f2d23, and "The record of 23 November 2026 (127 pages) has the same statement numbers as 49f2d23, and different pages".
- **What I verified.**
  - REPO's `part_i/main.pdf` (23:21) has 127 pages.
  - REPO's `part_i/main.aux` (23:21) has the same 238 labels as 49f2d23, none renumbered and 199 on different pages.
- **What I could not verify.**
  - The report paths under `ugjs/council/` exist only once the orchestrator archives the reports there.
  - I cannot check "not read by a human".
- **Also adjusted.** The Summary's account of A2 (l. 102) now cites formulas (2) and (3) of Lemma 4.1 as precedent, as the sources auditor suggested, and says that the formula is derived from V.15's bounded case.

**Checks run.**
- **Build.** Three passes of `/Library/TeX/texbin/pdflatex -interaction=nonstopmode route_t.tex`.
  - `^!`: 0. Overfull: 0. Undefined: 0.
  - `pdftotext route_t.pdf - | grep -nE '\?\?|TODO|Hmm|wait,'` printed nothing (exit 1).
  - `pdfinfo`: 33 pages. 20,822 words.
  - No machine paths in the note, the script or the second diff.
- **Script.** `check_route_t.py` was rerun unchanged: 23 PASS, 0 FAIL, "ALL CHECKS PASSED". The output is identical to the previous run apart from the version line. No new identity was introduced: the approximation is a limit argument, and check 14 already tests the truncation limit in the Gaussian toy.

**Not done, not verified, not run.**
- **Not done:** none of the requested points.
- **Not verified:**
  - Simon's class F, whose definition I could not find (this is now stated in the note);
  - the archived paths of the audit reports;
  - "not read by a human".
- **Not run:** any check of this second round by another agent; no git command; no subagents.

**Files written in this round** (scratch, outside the repository):
- `route_t/route_t.tex` (1916 lines) and `route_t/route_t.pdf` (33 pages), with the build by-products;
- `route_t/check_route_t.output.txt` (rerun);
- `work/route-t/route_t.rechecked.tex` and `work/route-t/check_route_t.output.revision1-final.txt`;
- `work/route-t/simon-p163full-185.png` and `work/route-t/simon-p163-bottom.png`; `work/route-t/simon_all.txt` (the text layer of Simon's book, used to search for F);
- `reports/route-t-revision2.diff`, and this section, appended to `reports/route-t-revision.md`.
