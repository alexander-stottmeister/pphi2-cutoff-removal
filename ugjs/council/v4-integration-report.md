# Round V4 and its re-check: consistency of the integration (7 November 2026)

One agent (general-purpose, model claude-opus-5-5) that had written none of the audited text. It checked the integration of Appendix D against the comparison note and the record's status sentences, and re-checked the orchestrator's fixes once. Two reports, in the order returned.

Returned by the agent as a message, not as a file. Saved here on 11 November 2026 by the orchestrator from the session transcript. The text is verbatim except that paths under the home directory and under the session's temporary folder are replaced: `<scratch>/` is that temporary folder, which was emptied on 10 November 2026, and paths inside this repository are written relative to its root.

---

## V4, integration (returned 2026-11-07 21:25 UTC)

## (1) Verdict

I found no CRITICAL and no MAJOR finding. As far as I checked, the integration is sound in its mathematics.
- **(a) Replaced proofs.** Every replaced proof in §§4–7 matches its `BEGIN-REPLACEMENT` block in `ugjs/parts/consequences.tex`, up to `\ref` conversions. Each deviation is listed below; all are correct except two small slips (M13, M14).
- **New Step 1 of Theorem 5.1.** It is valid with what the file now contains:
  - `Q_V:=(J_0V(h))^2`, with `V(h)` the object of §2.1 / A1(d);
  - Lemma N.23′(iii) gives `W_n(h)=:φ0^n(h):_C`, so `V(h)` is the constructed `λΣa_nW_n(h)`;
  - `J_0` is the isometry of N.21(i), and it is multiplicative (stated in the proof of N.22);
  - Lemma N.43(i) gives the a.e. decomposition into the pieces `Q_{n,n',k,k'}`.
- **Repaired Appendix C.** I re-derived the repaired Lemmas C.2–C.5 step by step and every step holds:
  - Lemma C.3: Young's inequality, `C(P)`, `C_{p'}`, `b(P)`, `c_1`;
  - (C.a), (C.b), (C.c) with `C_*`;
  - Lemma C.4: J1–J3, `A_n`, `B_n(R)`, `c_2`;
  - Theorem C.5: thresholds `b_0'`, `b_1`, `b_2(p)`, and the layer-cake bound `(1+e^{pb_*})^{1/p}`.
- **New Lemma N.23′.** It holds, apart from two one-line omissions (M8).
- **Discharged conditions.** Every condition the note attached ("R8", "R1–R10", "the GAP") is discharged by the A1/A3 Wick paragraphs, the repaired Appendix C and N.23′.
- **Mechanical checks.** All pass: build clean, 125 labels unmoved, N.k numbering as claimed.
- **What remains.** 26 MINOR findings: stale or false sentences, citation slips, overclaims and disclosure gaps. Two of them make the text say something about verification that is not true today, and should be fixed (or made true) before commit: B1 and B2.

## (2) Findings (all MINOR by AGENTS §2; ranked by importance)

**Blocking for commit**
- **B1.** Title page l.135–136: "the gate record of the integration is `part_i/README.md`". Appendix D l.3768: "the integration gate is recorded in `part_i/README.md`".
  - Why it fails: README.md (working copy, mtime 21:54) has no integration gate record; only the dossier rows of ll.491–494 were added. This is trap 28 of the plan.
  - Repair: write the GI record before committing, or reword.
- **B2.** Appendix A l.2986–2988: "each row was re-verified against its defining display at gates G3a/G3b".
  - Why it fails: this is false for the 13 rows added on 7 November (`c_U`, `S_2`, `Σ̄`, `V_*`, `M_B`, the φ⁴ value of `M_B`, `A`/`B′`, `K_f`/`A_f`, `s_0`, `b_0…b_*`).
  - Repair: "rows of 2 Nov re-verified at G3a/G3b; rows added 7 Nov recomputed in §D.g (N.48–N.55)", or re-run G3.
- **B3.** Appendix B l.3136–3137: "The page images of Simon's book … are listed in the dossier."
  - Why it fails: the dossier index `audit_2026/citation_screenshot_dossier.tex` (mtime 22 Sep) does not list them, and the Dossier lines of A1/A3/A4 (ll.611–613, 718, 752) were not updated. The images do exist in `audit_2026/evidence/` (git-ignored, created 21:54).
  - Repair: add the image ids to the three Dossier lines, or point to the README table.

**Mathematical text**
- **M1.** Remark N.16, l.4427–4430: "The proof of Theorem C.5 ends ``with a bound depending only on (p,λ,P,Λ)'' and produces no number, … M_B … is not explicit".
  - Why it fails: the repaired proof (ll.3582–3654) contains no such phrase and does produce the bound `(1+e^{pb_*})^{1/p}`. That bound is used at l.4405 and l.3025, so the remark contradicts the text around it.
  - Repair: say that S_2 is not evaluated and is bounded by the explicit but crude `(1+e^{2b_*})^{1/2}`.
- **M2.** N.15(i) proof, l.4398–4399, quotes Theorem C.5 as "…\sup{…}<∞".
  - Why it fails: the statement now reads "≤(1+e^{pb_*})^{1/p}<∞", so the quotation is stale.
  - Repair: quote the current statement.
- **M3.** Remark N.3(iii), l.3926–3933: "…uses the cells only through the decomposition f_i=Σ_k f_i1_{[k-½,k+½)} … over the N_I columns; with the former cells [j,j+1) it would run the same way and gives (N.a)".
  - Why it fails: the mechanical edit made this false. Run with the former cells, the proof gives the bounds with `N^cell_I`, not (N.a). The note said the opposite: with the columns in place of the cells it runs verbatim and gives (N.a).
  - Repair: "decomposes over the columns, applies Cauchy–Schwarz over N_I=N^□_I columns, and gives (N.a)".
- **M4.** §D.g, l.7544: "In \S\ref{app:D-constants} the rows that change are, as §§4–7 lists them: K_1,…,C_8 …".
  - Why it fails: wrong substitution; the note said "the record's Appendix A … as §8 lists them".
  - Repair: replace with `Appendix~\ref{app:constants}` and "changed on 7 November 2026".
- **M5.** Appendix C notation paragraph, l.3340: "c_κ … does not depend on z (Lemma N.13(iii))".
  - Why it fails: the proof of N.13(iii) uses Lemma C.4 (l.4363). This creates an apparent cycle: notation paragraph → N.13(iii) → C.4 → notation paragraph.
  - Repair: cite Lemma N.25(iii) (l.5238), which proves the fact directly.
- **M6.** Appendix C intro, l.3151–3153: "every input they use is derived here or imported in A1, A3 and A4".
  - Why it fails: Lemmas C.2–C.5 also use N.19(v), N.25(iii), N.23′(i) and N.13 from Appendix D.
  - Repair: name Appendix D as well.
- **M7.** §2.1 l.451–454 ("Lemma N.23′ proves that :φ0^n(h):_C is the L²-limit … so that V(h) is also an explicit limit"), and the A1 Scope at ll.598–601.
  - Why it fails: both are stated for every real h∈L¹∩L² with compact support. N.23′ covers only bounded kernels; (iii) covers ‖h′‖_∞≤1 with support in [a,a+2].
  - Repair: restrict the claim to bounded h.
- **M8.** A1(d) ll.565–576 and A3 ll.661–672 attribute to Simon (V.3) the characterization for g∈L^{1+ε}.
  - Simon prints (V.3) for g∈𝒮; I read pp.135–136 on the image. The L^{1+ε} object is the extension.
  - Two one-line steps are missing, also in N.23′(ii), l.5069–5071:
    - the extension satisfies (V.3) by continuity, from (V.6) and continuity of the pairing in g;
    - Wick monomials with f_j∈𝒮 span the same closed Γ_n(H), by density of 𝒮 in H.
  - Repair: add the two lines.
- **M9.** A8(iv-T), l.891–892: "the one case of the printed statement that its printed proof does not reach".
  - Why it fails: Remark N.39 (l.6391–6396) says the appendix "does not need to decide" whether the printed proof reaches the parallel case with a time-integrated partner. The plan (Part 7) says "one case".
  - Repair: "a case …".
- **M10.** A8(iv)-T is defined for strips "bounded by two lines of constant x¹" (l.888–892). Appendix D attaches the label to every *transverse* use, which by Definition N.6 includes tilted strips: D.2(a) l.5868–5871, D.2(b) l.5879–5882, N.48 l.7186–7189, N.33(2) l.6033–6038.
  - Effect: Theorem D.4 uses only constant-x¹ strips, so it is covered; the general statements are mislabelled.
  - Repair: define A8(iv)-T for any non-parallel strip, constant-x¹ in every use by Theorem D.4.
- **M11.** A8 Scope (d), l.1121–1127: "item 10 … asks a human reader to confirm the printed text these readings rest on".
  - Why it fails: one of those readings is "GJS's V(h) of (1.8), p.589 is U_h". C5 item 10 covers pp.593 and 595 only, and neither item 1 nor item 10 lists (1.8) or the p.589 sentence "Wick order with respect to the measure dΦ".
  - Repair: add that text to a C5 item, or narrow the sentence.
- **M12.** External residue l.3128–3134, title page l.133–134, and the status lines of D.3/D.4 (l.6320, l.6616) classify C5 items 9 and 12 as "corroboration".
  - Why it fails:
    - Scope (b)/(c) and the "printed proof does not reach" half of A8(iv)-T rest on p.597's rotation sentence and on p.596's "monomials of type (1.1.5)" (items 9(c), 12(a),(c)).
    - Item 12's own "What this carries" names Scope (b).
    - §D.e.4 (l.6728–6733) quotes exactly these sentences.
    - Plan gate GB2 asked for items 10–13 to be named open.
  - Repair: name item 12 (and 9(c)) as open in D.4's status line and in the External residue.
- **M13.** Corollary 5.2, l.1615–1626.
  - Why it fails: the replacement block ends with the transverse disclosure ("rests on the transverse case … F-T"); the integrated text drops it.
  - Repair: add "(through Theorem D.4 it rests on A8(iv)-T)".
- **M14.** Lemma 7.6, l.1924–1925: "K_f on f, K_2 and m_0".
  - Why it fails: K_f also depends on I through N_I. §D.f.2 (l.6943) and the A.4 table (l.7515) say so.
  - Repair: add I.
- **M15.** Theorem 5.1 Step 1, l.1525–1527: "a multiplicative isometry (A2; Lemma N.21(i))".
  - Why it fails: multiplicativity is stated in the proof of N.22 (l.4864), not in N.21(i).
  - Repair: cite N.22's proof.
- **M16.** §1.2, l.249–250: "The dependency graph, as established by the independent audit of the predecessor manuscript".
  - Why it fails: the display now contains items of Appendices C and D added on 7 November, which that audit did not establish (the src comment says "transcribed").
  - Repair: add "updated 7 Nov 2026".
- **M17.** The §1.4 Provenance paragraph (ll.409–421) and Appendix B's "Frozen sources" table (ll.3035–3053) omit `ugjs/comparison.tex`, the source of Appendix D.
  - Repair: add it.
- **M18.** Title page l.124–126: "The uniform local moment is a theorem of the record (… Theorems D.3 and D.4 …)".
  - Why it fails: Theorem D.3 is the fixed-g bound used for the gap, not the uniform local moment.
  - Repair: separate the two theorems.
- **M19.** A8(v) l.912–913 ("proved from item (iv)") and A8(vi) l.936–937 ("from item (iv) alone").
  - Why it fails: Theorems D.3–D.4 also use Appendix C, A2–A4 and A8(i)–(iii).
  - Repair: name these inputs.
- **M20.** Appendix B l.3116–3117: "A8(vii′)(a) transcribes (1.1.11) with ``O(1)'' where p.594 prints ``0(1)''".
  - Why it fails: the present tense describes the old state; l.1025 now transcribes "0(1)" with [sic].
  - The [sic] itself is correct: I checked `gjs-theorems-11.png`. The (1.1.11) prefactor is an upright 0(1); (1.1.10) has an italic O(1).
  - Repair: past tense.
- **M21.** Appendix B entry, ll.3092–3096.
  - The list of replaced texts omits the rewrite of Theorem 5.1 Step 1 and the changed statements of Lemmas 7.1 and 7.6 and of Theorem 5.1.
  - Dates disagree: "2–4 November" there, "31 October–4 November" in Appendix D (l.3760).
  - Repair: complete the list and align the dates.
- **M22.** Appendix D intro: ll.3762–3764 and ll.3770–3771 say the same thing twice (the N.k numbering is kept so the audit reports apply). Delete one.
- **M23.** Prop. C.7, l.3676–3677: "every use of clustering in this manuscript is Source Fact 2.2".
  - Why it fails: §9 uses Hamiltonian clustering (lem:cluster).
  - Repair: "every use of Euclidean clustering (CE2)".
- **M24.** Incomplete "Used in" lists:
  - A8 Used in (ll.1132–1135) omits §5 (Step 1 uses (ii), Steps 3–4 use (iii)).
  - A1's Used in (ll.606–609) and A2's (l.639) omit Appendix D and §5 Step 1.
  - Remark 3.3 (ll.1359–1361) omits Appendix D among the working-coordinate constants.
- **M25.** Plan gate GB1, by its letter: the notation table (l.508) and Appendix A (l.2997, l.3027) still contain C_8. All three are history parentheticals, but GB1 required these places not to hit.
- **M26 (optional).**
  - The headings "A.1–A.4" inside §D.g (ll.7170, 7216, 7359, 7462) are easily confused with Appendix A.
  - The constants A, B′ share letters with the observables A, B of §§9–12.
  - Γ is overloaded: second quantization, chaoses, Γ_{κ,κ′} (l.4877), and a kernel (l.5390).

**Deviations from the replacement blocks (all correct unless listed above)**
- Lemma 7.2 gains the box-translation justification for A(s)=A(0) (B_s is B_0 shifted by whole rows; N.15(iii)). Correct.
- Lemma 7.6 gains a dependence sentence (see M14) and the remark on the radius. Lemma 7.6's "≤(√2σ_f)^{2n}(2n)!" bound is correct (N.52).
- Theorem 7.7's radius `s_0=min(2kK_{e_j})^{-1}` is written inline, together with the differentiation bound `|x|^ℓe^{s_1|x|}≤ℓ!(s_2−s_1)^{-ℓ}e^{s_2|x|}`. Correct.
- Theorem 5.1's statement adds "finite, not evaluated" and the dependence clause (trap 10). Step 5 adds `=∫Q_V dq` and drops the parenthetical about the GAP, which is now closed.
- Corollary 5.2 adds its derivation; the arithmetic checks (9·8!=362 880, 24·362 880=8 709 120, 81·24=1944).
- §6 edits are verbatim, plus the counterexample note. Checked: I=(0.4,0.6) meets two columns, and the column decomposition gives ‖Q‖=√2K_1K_2²‖f‖_2.

## (3) Mechanical checks

- **Build.** Copy in `<scratch>/audit-integ/build/`, three runs of pdflatex, each exit 0. `grep -cE '^!'` = 0; Overfull = 0; `grep -icE undefined` = 0. Underfull = 19 (5 in the committed build). There are 23 hyperref "Token not allowed" warnings, which are benign. 109 pages. The pdftotext grep for `??|TODO|Hmm|wait,` gives 0.
- **Labels.**
  - The committed aux (identical to a fresh build of HEAD in `buildHEAD/`) has 125 `\newlabel` entries.
  - `labels-main-2026-11-02.txt` lists 119 of them; the 6 tag labels eq:G, eq:Ggamma, eq:M2, eq:P, eq:T, eq:UGJS are not in it.
  - Result: 0 txt mismatches against the old aux; 0 old labels missing from the new aux; 0 numbers changed; 125 identical; 105 new labels.
- **N.k numbering.** N.1–N.46 and N.48–N.55 are identical to `ugjs/comparison.aux`. N.47 (aux:consequences-moment) is absent, skipped by `\stepcounter` at l.7152. aux:notation-ident is N.23′. Lemma D.1–D.2 and Theorems D.3–D.4 keep their numbers. Subsections are numbered D.a–D.g.
- **Other greps.** `grep -c 'Assume $U_{\rm GJS}'` = 0. The plan's `assum…U_GJS` grep finds nothing. GA5: no non-comment hit of eq:UGJS or C_8 in §§4–7. The replacement-block grep in consequences.tex gives 0.
- **GB1 grep** (39 hits); none is used in a proof:

| lines | classification |
|---|---|
| 63 | macro `\UGJS` (used only at 6765) |
| 90, 94, 98, 103 | superseded title-page notices |
| 508 | notation table, history parenthetical |
| 906 | A8(v), provenance |
| 917, 926, 929, 931, 935, 980, 982, 985 | A8(vi), retired item |
| 1014 | A8(vii′) |
| 1081 | Scope (a), history |
| 1501, 1566, 1614, 1718, 1909 | `%` comments, not typeset |
| 2997, 3027 | Appendix A, history |
| 3075, 3081 | Appendix B, history |
| 3246 | mechanism audit M6 (audit record) |
| 5090, 6442, 6579, 6765–6766, 6927, 6938, 6995, 7024–7025, 7354, 7545 | Appendix D provenance or negative statements |

  `\eqref{eq:UGJS}` occurs only at 935, 980, 1014 and 1081, all inside A8 (vi), (vii′) and Scope (a).
- **Appendix D against the note.** A token-level diff of main.tex ll.3774–7554 against the note's notation, d1–d4, quantifiers and constants parts (up to A.5) gives 659 hunks; I read every one. Apart from the items above, all are mechanical: refs, "note"→"appendix", F-T→A8(iv)-T, removal of record citations. The substantive changes are N.23′, the closure paragraph replacing the GAP, the rewritten status lines, the explicit bound in N.15(i), and M1–M4.
- **Source images read this session.**
  - GJS p.594 (`gjs-theorems-11.png`) for the "0(1)" [sic].
  - Simon pp.12, 135, 136, 137, 138, 152 and 38 (`simon-wickprod-034`, `simon-wickdef-157/158`, `simon-wickthm-159/160`, `simon-exp-174`, `simon-thm122-060`). The quotes in A1, A3 and A4 from these pages are verbatim; M8 is the one scope difference.

## (4) Not checked

- Simon pp.10, 11, 17, 25 and 34; GJS pages other than p.594.
- The note's own quotes and the proofs of Appendix D statements that the integration did not change. I compared these against the audited note, not re-proved them. Re-derived: C.2–C.5, (C.a)–(C.c), N.19, N.20(ii), N.23′, the N.43 counting, D.4's constants, and the arithmetic of Lemma 7.6 and Corollary 5.2.
- §§8–14, which the integration did not change.
- The PDF pages visually.
- The numerical scripts.
- docs/, the root README, CITATION.cff, KB, companion; `ugjs/comparison.tex`'s new notice.
- The re-run of gates G0–G6/GI, the step maps, `labels.md`.
- `part_i/README.md` and `C5_reading_record.md` were being edited while I worked (mtimes 21:53–21:54). B1, B3, M11 and M12 describe their working copies at about 22:10.
- `main.tex` itself did not change during the audit: SHA1 `44e2fce7…` at the start and at the end.

Scratch files are in `<scratch>/audit-integ/`: `build/`, `buildHEAD/`, `appD_diff.txt`, `cmp_appD.py`, `parse_aux.py`, `gb1.txt`, `newlabels.txt`, `cmp_O1*.png`.

---

## Re-check of the fixes (21:39 UTC)

## Round V4b: re-check of the fixes in `part_i/main.tex`

I checked the edited file (SHA1 `0d87448f…`, mtime 22:31:32; it did not change while I checked) against my first-round findings B1–B3 and M1–M26.

## (1) Verdict

- **Closed: 26 of 29.**
- **B1, pending by design.** `part_i/README.md` (mtime 21:54:27) still has no integration gate record. The two sentences that point to it are otherwise accurate: title page l.135–136 and Appendix D l.3851. That README already holds the earlier gate records, including the G3a/G3b record that Appendix A cites.
- **B3, not closed.** The External residue (l.3212–3216) says the Simon images for pp.15–17 and 134 are in `audit_2026/evidence/`. Three of the ids named in the Dossier lines do not exist there; at 22:37:45 they were still missing:
  - `simon-gaussproc-037` (p.15, A1, l.668);
  - `simon-gamman-038` (p.16, A1, l.668);
  - `simon-wickdef-156` (p.134, A1 l.669 and A3 l.778).
  The A1 and A3 rows of the dossier table in `part_i/README.md` (ll.491–494) omit them too. The pages themselves are in `refs/Simon - The P(\Phi)_2 … .pdf` (PDF pp.37, 38, 156).
  - Repair: render the three images into `audit_2026/evidence/` and add them to the README table, or drop pp.15, 16 and 134 from the claim.
- **M26, partly closed.** The A.k headings in §D.g are renamed. The overloading of A, B′ and Γ is left, as you decided.

New text since my report, checked and correct:
- **The Locality paragraph (l.461–484).** I checked each step:
  - for κ > 1/dist(supp h, ℝ∖U), the support of ρ_κ(x−·) lies in U;
  - the Bochner integral of Σ_U-measurable variables stays in the closed subspace L²(Σ_U), and so does its limit;
  - unbounded h by truncation, using (V.6b) at p=2, ε=1 and ‖h−h_N‖₂→0. This case rests on the V.2(b) reading, which the paragraph discloses;
  - M_U contains every bounded Σ_U-measurable multiplication (joint functional calculus, then a monotone class);
  - the spectral projections lie in M_U, which gives the affiliation.
- **The ½ normalisation of H_C and H_G.**
  - The quotes match the pages, which I rendered from the PDF in refs/: p.15 (Definition (c) and Thm I.6), p.16 ("the closed subspaces generated by"), p.134 ((V.1)), p.11 (the proof of Thm I.3 uses ⟨:exp(αf+βg):⟩ = 1).
  - E[φ0(f)φ0(g)] = ½·2⟨f,Cg⟩ ✓, and 2⟨f,Cf⟩ ≤ ‖f‖²/m0 ✓.
- **The p-range in A4's Scope.** In §8 Step 1, p_T = 1+e^{−m0T} and p_T′ = 1+e^{m0T}; Appendices C and D use p=2.

## (2) Per-finding status (line numbers of the edited file)

- **B2** closed, l.3054–3058.
- **M1** closed, l.4513–4516.
- **M2** closed, l.4483–4485 (the quote stops before "where b_* …", which is acceptable).
- **M3** closed, l.4009–4013.
- **M4** closed, l.7633; see residual R3.
- **M5** closed, l.3420. A trivial mismatch remains: N.25(iii) assumes κ ≥ 2, but c_κ is defined for κ ≥ 1. Only κ ≥ 2 is ever used.
- **M6** closed, l.3231–3233. N.19, N.23′(i) and N.25 indeed do not use Appendix C.
- **M7** closed, l.453–459 and l.649–652.
- **M8** closed: A1(d) l.620–629, A3 l.728–729, N.23′(ii) l.5157–5159. The extension argument holds: Π ∈ L¹∩L^∞ makes the pairing continuous on L^{1+ε}, and (V.6b) at p=2 makes the extension continuous.
- **M9** closed in A8(iv-T), l.954–955; residuals R1 and R2.
- **M10** closed, l.951–957.
- **M11** closed, l.1192–1194, together with C5 item 1(e).
- **M12** closed: l.134, l.3205–3210, l.3834, l.6704–6705, and the headers of the C5 record, the root README and docs/status.md.
- **M13** closed, l.1693–1694.
- **M14** closed, l.1993.
- **M15** closed, l.1594.
- **M16** closed, l.248–250.
- **M17** closed, l.416–417 and l.3119.
- **M18** closed, l.125–127.
- **M19** closed, l.978–980 and l.1003.
- **M20** closed, l.3191–3192.
- **M21** closed, l.3160–3167.
- **M22** closed, l.3847.
- **M23** closed, l.3760–3762.
- **M24** closed: A1 l.657–662, A2 l.695–696, A8 l.1199–1200, Remark 3.3 l.1427–1428.
- **M25** closed: l.540, l.3067, l.3096–3098.

**Remaining inconsistencies, all MINOR.**
- **R1.** Prop. C.7, l.3764–3765, says of Lemma 7.4 and Theorem D.3: "the strips are parallel …, the case the printed proof reaches".
  - Why it fails: for D.3 this is the overclaim that M9 removed from A8(iv-T). Remark N.39 says the time-integrated partner is reached "only after slicing" (a reading GJS do not print) and that the appendix "does not need to decide".
  - Also at l.3760–3762: after the new parenthetical, "whose constants are independent of h" reads as if it referred to Lemma 9.x.
  - Repair: "the parallel case (for Lemma 7.4, the case the printed proof reaches)", and move the parenthetical.
- **R2.** The heading in `docs/imports.md` reads "A8(iv)-T: the one case used beyond the printed proof". Same issue as R1. Its A1 row says "Simon, pp. 10–17, 135–138", while the manuscript says pp.10–12, 15–17, 134–138.
- **R3.** §D.g's closing list of "New rows" (l.7633ff.) omits Appendix A's row "b_0, C_*, c_1, c_2, b_*".
- **R4.** Outside main.tex: in `C5_reading_record.md`, the "What this carries" lines of items 9 and 12 still describe the 31 October state ("literal basis of A8(vi)"). The new header supersedes them.

## (3) Mechanical checks

- **Build.** `<scratch>/audit-integ/v4b/build`, three pdflatex runs, each exit 0.
  - Errors 0, Overfull 0, undefined 0. Underfull 18. No multiply-defined labels and no rerun warnings.
  - 110 pages. The pdftotext grep for `??|TODO|Hmm|wait,` finds 0.
- **Labels.**
  - Against a fresh build of HEAD (125 labels): 0 missing, 0 changed, 125 identical, 105 added. The repository's `part_i/main.aux` has since been rebuilt with 230 labels, so I compared against my HEAD build instead.
  - `labels-main-2026-11-02.txt` (119 entries): all match.
  - All 230 numbers are identical to my first-round build.
  - N.k numbering: N.1–N.46 and N.48–N.55 equal the note, N.47 is absent, and aux:notation-ident is N.23′.
- **GB1 grep: 36 hits; the notation table and Appendix A no longer hit.**

| lines | classification |
|---|---|
| 63 | macro definition |
| 90, 94, 98, 103 | superseded title-page notices |
| 971 | A8(v) |
| 983, 992, 995, 997, 1001, 1046, 1048, 1051 | A8(vi), retired |
| 1080 | A8(vii′) |
| 1147 | Scope (a) |
| 1568, 1633, 1681, 1786, 1977 | `%` comments |
| 3145, 3151 | Appendix B history |
| 3326 | M6 audit record |
| 5179, 6531, 6668, 6854–6855, 7016, 7027, 7084, 7113–7114, 7443, 7633 | Appendix D provenance or negative statements |

  - `Assume $U_{\rm GJS}` count 0; the `assum…U_GJS` grep finds 0.
  - `\eqref{eq:UGJS}` occurs only at l.1001, 1046, 1080 and 1147.

## (4) Not checked

- docs/results.*, the figures and CITATION.cff beyond the grep; the KB; the new notice in `ugjs/comparison.tex`.
- Further concurrent edits to `part_i/README.md`, the C5 record and docs after 22:37.

Scratch files are in `<scratch>/audit-integ/v4b/`: the build, `v4_vs_v3.diff`, `gb1_v4.txt`, and the page renders in `simon/`.
