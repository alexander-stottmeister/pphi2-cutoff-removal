# DISPOSITION-cqft2 (rounds V1 and V2), 3 November 2026

One line per finding that concerns `parts/notation.tex` or `parts/constants.tex`. Locations name labels
(numbers move); "N.x" are the numbers of `build-cqft2/fullstub` of 3 Nov 12:2x.

## V1, attack (`audits/V1-cqft-report.md`)
- cqft-1 (MAJOR) | fixed | new Lemma N.22 `aux:notation-sharpid`: X_κ → J_t W_n(f) in L²(dμ₀), by the three inner products and a κ-uniform log majorant; uses new N.19(v) (`aux:notation-kernel`: G(ζ) = C(|ζ|), ∫G = m₀⁻²). New Remark N.23 `aux:notation-sharpidrem` (a): N.24(b) objects = J_t-objects; (b): Q_V pieces, Q_V = Y²; (c): degree 1. Also a closing sentence of N.21, the A.D4 base term (`aux:constants-D4`), and A.6 (C7). **For aqft:** cite `aux:notation-sharpid` and `aux:notation-sharpidrem`(b) in D.4 Steps 2/4 and §8.6; no second computation is needed.
- cqft-2 | fixed | Remark N.2(iv) (`aux:notation-gjslattice`): the identification with GJS's monomials is named as a reading. It quotes p. 589's "(1.8) … Wick order with respect to the measure dΦ, as in [9], [1]", cites C5 item 10 and A8 Scope (d) (record p. 13), and notes mollifier independence at sharp time by N.22.
- cqft-3 | not in my files | d1.tex and gates.tex (mp, orchestrator). My §2 introduction already maps Lemma C.2 to R8 alone and Lemma C.4/Theorem C.5 to R1–R10.
- cqft-4 | partly fixed | gapnote after N.20 now states where the GAP enters: only the record's Theorem 5.1 Step 1 and the transfer of §8.6. With V_* for the constructed V(h′) (N.20(iv)) and N.22, the Euclidean D.4 needs no GAP. Naming the GAP at Lemma 4.3(ii) and Thm 5.1 Step 1 is aqft's (consequences.tex). The optional V_* via N.26(d) is not needed.
- cqft-5 | not in my files | consequences.tex §8.1 and the master.
- cqft-6 | fixed (my part) | constants.tex A.5 (D1) records the split: CRITICAL for Prop. 6.2, MAJOR for the displayed bounds of Lemmas 7.1/7.6, MINOR for Thms 7.7, 7.8, 12.2. §8.9 and N.35 are aqft's.
- cqft-7 | not a defect in my files | no "reached by the printed proof" claim in notation.tex or constants.tex (grep "reach": none). The master and N.37 belong to others.
- cqft-8 | fixed (my part) | constants.tex A.4: legend "F-T", and marks on the M_B and M_B(φ⁴) rows. The §8.7 and Cor. 5.2 clauses are aqft's.
- cqft-9, 10, 13, 14, 15 | not in my files | consequences, d2, master, quantifiers, record/gates.
- cqft-11 | fixed (my parts) | §2 introduction names where Lemma C.4 is used: N.5(iv), N.13(iii)–(iv), N.18(iii)–(iv), hence N.15(iii). A new "Inputs of this section" paragraph lists A2, A3, A4 (abstract form), A8(i)–(iv), Remark 2.5, §2.6, Remark 3.3, Lemma 6.1/Prop. 6.2 proofs, App. C regularization, C.4, C.5 and the comparison step. constants.tex intro lists its inputs, Lemma C.4 included. The master §1 is the orchestrator's.
- cqft-12 | fixed | Lemma N.18(iii) (`aux:notation-cU`), statement and proof: a₀ as a coefficient of the interaction enters only through Z (C.2) and S₂; as a coefficient of the observable it enters V_* and 𝔔; not c_U.

## V1, quantifiers (`audits/V1-mp-report.md`)
- mp-F1, F2, F4–F12 | not in my files | d2, d3, d4, consequences, master. For F2: with N.22 the GAP is not used at D.4 Step 2 (see cqft-4).
- mp-F3 | partly addressed | N.5(iv) proof (`aux:notation-cutoffs`) now records the alternative route: Step 1 of D.1's proof, from Lemma N.26(a), without Lemma C.4, for 𝒰_h read as the δ_κ-limit. Which route D.2 cites is aqft's choice.
- mp-F13 | not in my files | §7 (mp). Note: after N.22, V_*, 9^{p′} and M_B rest on the GAP only at the transfer, not as constants.
- mp-F14 | fixed, refined | constants.tex A.4 legend now says where the GAP enters ("GAP for Thm 5.1" and "GAP for Cor. 5.2" on the M_B rows). V_* (row names the constructed V(h′) of N.20(iv)) and 9^{p′} need no GAP after N.22.

## V2 (`audits/V2-report.md`)
- V2-1 (MAJOR) | fixed | as cqft-1 (N.22, N.23, A.D4, A.6 (C7)).
- V2-11 | fixed | constants.tex A.4 closing paragraph now lists the rows exactly as §8.7 does: changed K₁…m₁, N_I, M², M²(φ⁴), K′, Ψ_γ rows; unchanged ε_𝒫, 𝔎, Ĉ_Q, 𝔪, d₀, shell count; new c_U, S₂, A, B′, A_f, K_f, s₀, V_*, Σ̄₃ₓ₅, M_B. A.6 (C6) corrected: A.1 and D.2(a) both use assigned strips of positive width.
- V2-12 | wording supplied (gate record is the orchestrator's) | Proposed text: "GA3 (Appendix A, cqft2, recomputed independently of aqft's text): every constant agrees with §§5–6 and §8; the deviations from PLAN Part 1 are listed in A.5, (D1)–(D4) and (D9)". New A.5 (D9) records that M_B uses Σ̄₃ₓ₅ ≥ the plan's Σ₃ₓ₅.
- V2-13 | fixed (my parts) | as cqft-11. The master §1 is the orchestrator's.
- V2-15 | fixed | as cqft-12.
- V2-18 | fixed | Remark N.12(c) (`aux:notation-ringrem`) records the run: 3 Nov 2026 12:08 CET, /usr/local/bin/python3 (3.14.7, numpy 2.5.2, scipy 1.18.1), output `build-cqft2/ringcheck-output.txt`, "ALL CHECKS PASSED", labelled numerical. A.3 refers to it. Copying the output into the frozen bundle is the orchestrator's.
- V2-19 | fixed | notation.tex introduction cites `ugjs/council/v3-appendix-c-report.md` (the only V3 path in my files). The gapnote follows its errata header (Simon chapters I and V).
- V2-20 (my locator) | fixed | chaos paragraph: Prop. 3.2's generating-function sentence is at record p. 16 (checked on main.pdf). The other slips of V2-20 are in the master.
- V2-21 | fixed | chaos paragraph and N.21(i) (`aux:notation-hyper`): the note's degree-n objects are L²-limits of integrals of Wick monomials, so they lie in Simon's Γ_n, on which R8 imports Γ's action.
- V2-2…V2-10, V2-14, V2-16, V2-17, V2-22 | not in my files | d1, d2, d3, d4, quantifiers, consequences, gates, master, record.

## Builds (3 Nov 2026)
- `build-cqft2/stub.tex` (my parts only), pdflatex ×2: 0 errors, 0 Overfull, 27 pp. Undefined references are only to other parts' labels.
- `build-cqft2/fullstub.tex`, regenerated from the current master: 0 errors, 0 undefined, 0 multiply defined, 68 pp, no "??". Its 2 Overfull boxes are in d4.tex (aqft).
- mp-deferred-1 (N^col_I in constants.tex A.6 (C2)) | fixed | (C2) now refers to the record's N_I as redefined in §8.1 (`sub:cons-NI`) and states that it is N^□_I of Remark N.3 (`aux:notation-counts`); no part uses N^col_I any more (grep: none). Rebuilt 3 Nov 12:26: stub 0 errors/0 Overfull/27 pp; full stub 0 errors/0 Overfull/0 undefined/67 pp.
- mp-deferred-2 (reading of 𝒰_h in N.5(iv)) | fixed | last paragraph of the proof of N.5(iv) (`aux:notation-cutoffs`): "𝒰_h read as the L²-limit" is now marked as a reading the record itself does not make (V3 M-3; notation paragraph's unproved assertion, p. 39, V3 m-1; A3 imports 𝒰_h with Simon Thm V.7, main.tex l. 535, p. 8). The identification with the 𝒰_h that A3 imports is the condition §3 states for Step 1; on the reading it moves into A3's import, as in §3.

## V1b (`audits/V1-cqft-report.md`) and V2b (`audits/V2-report.md`), 4 November 2026
Numbers N.x from `build-cqft2/fullstub` of 4 Nov 18:27 (unchanged for my labels).
- V1b-1 = V2b-4 (scope of N.23(c)) | fixed | Remark N.23(c) (`aux:notation-sharpidrem`): (c) now claims only the unsplit factors Φ(s,f_i), f_i ∈ C_c^∞, of D.3's cylinder monomials, and not D.3's pieces f_i1_{[k−½,k+½)}, which are bounded but need not be smooth. It attributes those pieces to N.22 with n = 1 through (a), which identifies them with J_tW_1(g), and to N.28(f)(1), which identifies them with Φ(t,g). N.36(vi) uses the latter, with N.28(c) for the products. No new claim: both are existing, audited statements.
- V1b-4 = V2b-5 (where the reading is named) | fixed | Remark N.2(iv) (`aux:notation-gjslattice`) now reads: "It is named in the status lines of Lemma D.2 and Theorems D.3–D.4 and in Appendix B". Checked at d2.tex l. 151, d3.tex l. 265, d4.tex l. 159 and gates.tex l. 24. C5 item 10 is described as what it is (`part_i/C5_reading_record.md` ll. 153–163): an open item asking a reader to confirm the printed text of (1.1.5)–(1.1.6) and p. 595's multi-time notation. It does not check the reading.
- V2b-6 (A.4 legend against the rows) | fixed | constants.tex A.4: rows C₇c_U and B′ marked "cond.". The legend now assigns R1–R10 also where the comparison bound of Lemma N.48 (`aux:constants-comparison`) is used: Lemma C.4 via N.18(iv) and N.5(iv), and D.1's condition. The §2 introduction's sentence on Appendix A, which named only S₂ (R1–R10) and Z/9^{p′} (R8), has the same correction.
- V2-16 residue (last sentence of N.48 without F-T) | fixed | Lemma N.48 (`aux:constants-comparison`), last sentence: "where a strip so chosen is transverse to the time-zero line and some F_a is of type (1.1.5), this form uses the transverse case of GJS Theorem 1.1.7 at the printed statement's scope (F-T, §1)", worded as in D.2(b).
- V2-18 residue (run record missing from the bundle) | fixed | Remark N.12(c) (`aux:notation-ringrem`) now cites `parts/cqft2_ringcheck.output.txt`. It is byte-identical to `build-cqft2/ringcheck-output.txt` (`cmp`; sha256 b2a4a347…).
- Builds (4 Nov 18:27), pdflatex ×2 each:
  - stub: 0 errors, 0 Overfull, 27 pp. The only undefined references are to other parts' labels.
  - full stub, regenerated from the master of 4 Nov 18:19: 0 errors, 0 Overfull, 0 undefined, 0 multiply defined, 72 pp. The `pdftotext` marker grep finds nothing.
