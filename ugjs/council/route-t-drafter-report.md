# Route T: drafter's report (drafter "route-t", 23 November 2026)

## 1. Outcome

I wrote the Route T note (`route_t.tex`, 25 pages, about 16,100 words) with complete proofs. It proves that items (1)–(4) of Theorem 12.2 and Corollary 12.3 hold without Theorem 5.1, Theorem D.4 or A8(iv)-T, with the same state and a new super-polynomial rate function. Every new application of GJS Theorem 1.1.7 pairs two time-integrated monomials, in both orientations. The printed proof reaches these pairs only on reading R1 of p. 596 (multi-time A in Theorem 1.1.11), the reading GJS's own p. 595 use also needs. So Route T trades A8(iv)-T for reading R1; it does not make items (1)–(4) independent of readings. The finding N3 on Remark N.39 is confirmed.

## 2. Claims, with status and locator

Locators are labels and numbers from `route_t.aux` (note) and `part_i/main.aux` (record, commit 49f2d23 = FROZEN).

| # | claim | status | locator |
|---|---|---|---|
| 1 | Resolvent transforms: F̃(t) = ⟨u, e^{itH}QAΩ⟩, measures supported in [γ,∞) and (−∞,−γ], total variation ≤ 𝔪̃ = ‖(λ₀−iH)⁻¹QXΩ‖‖A‖ | proved | Lemma T.3 (`lem:transforms`, p. 4) |
| 2 | Locality discrepancy: F = G on (−R,R) ⇒ F̃ − G̃ = c e^{−λ₀t} there, \|c\| ≤ 2𝔪̃e^{−λ₀R} | proved | Lemma T.4 (`lem:discrepancy`, p. 6) |
| 3 | Separation with exponential discrepancy, the principal-value term computed exactly: \|F̃(0)\| ≤ 𝔪̃(1+2/(πγR′))e^{−γR′/2} + \|c\|(1/2 + sinh(λ₀R′)/π) | proved | Lemma T.5 (`lem:sep`, p. 6), eq. (t4), (t5) |
| 4 | Resolvent-weighted clustering (replaces Lemma 9.3 in the chain; no γR ≥ 1 needed): bound 𝔪̃ Ξ(R), Ξ(R) = (1+4/(πγR))e^{−γR/4} + (1+1/π)e^{−λ₀R/2} | proved, from Step 2 of the record's Lemma 9.3, Prop. 2.7, (G_γ) | Lemma T.6 (`lem:cluster`, p. 7) |
| 5 | Identity (b): ⟨V_jΩ, H⁻¹QAΩ⟩ = iF̃_j(0) + λ₀∫W_γF̃_j; all operators on QAΩ bounded by the gap; only V_jΩ needs a domain (Prop. 2.6) | proved | Lemma T.7 (`lem:deriv`, p. 8) |
| 6 | Two-regime bound with M̃ (replaces Lemma 10.3) | proved | Lemma T.8 (`lem:tworegime`, p. 8) |
| 7 | One-path estimate with M̃, threshold d ≥ 1, constant 12M′ (replaces Prop. 10.4; at most 3 indices per shell side, not 4) | proved | Prop. T.9 (`prop:onepath`, p. 9) |
| 8 | Rate function Ψ̃ super-polynomial (replaces Lemma 10.5) | proved | Lemma T.10 (`lem:rate`, p. 9) |
| 9 | (λ₀²+E²)⁻¹ ≤ c_k k(E), c_k = 2/(1+e^{−2}), λ₀ ≥ 1, E ≥ 0, k(E) = 2(E−1+e^{−E})/E² | proved | Lemma T.11 (`lem:ineq`, p. 10) |
| 10 | Time slicing: a one-square (1.1.6) monomial is the L²-Bochner integral of its one-time (1.1.5) slices; ∫‖Q(t)‖_GJS dt ≤ ‖Q‖_GJS | proved, from Def. N.26, Lemmas N.24, N.25, N.28(a), Fubini, Pettis | Lemma T.12 (`lem:slice`, p. 10) |
| 11 | V̄(h′) = ∫_{−1/2}^{1/2} J_τV(h′)dτ; ‖V̄‖₂ ≤ ‖V(h′)‖₂ ≤ V_*^{1/2}; ‖V̄²‖₂ ≤ 9^{p′}V_*; V̄² = Σ of (1.1.6) r = 2 pieces with the same GJS-norm bound as Q_V | proved, from N.20(iv), N.21(ii) (its argument), N.23(b), N.23′(ii)–(iii), N.28(c), N.28(f)(2) | Lemma T.13 (`lem:Vbar`, p. 11) |
| 12 | Time-integrated copy of D.4: ∫V̄(h′)² dq_h ≤ M_B² for all h ∈ C_E — the same box, rings and constant as D.4 | proved, conditional on A8(iv) at its printed scope in cases P3–P4 and on the reading of A8 Scope (d) | Theorem T.14 (`thm:TD4`, p. 12); step table §3.1 |
| 13 | lim_{T→∞} ∫V̄(h)² dq_{h_{T,g}} = ⟨XΩ_g, k(H)XΩ_g⟩, X = V(h) | proved, conditional on Simon Thm. V.15 + Remark p. 164 (source of A2; read on the page images), at asymmetric times | Lemma T.15 (`lem:fkn`, p. 14) |
| 14 | M̃(λ₀) ≤ c_k^{1/2} M_B for every λ₀ ≥ 1 (no gap used) | proved (conditional as claims 12–13) | Theorem T.16 (`thm:Mt`, p. 15) |
| 15 | Items (1)–(4) of Thm 12.2 and Cor. 12.3 hold with Ψ̃_{m₁} (same ω_∞); no use of Thm 5.1, D.4, A8(iv)-T | proved, conditional on A1–A8 (A8(iv) only in P1–P4), the declared readings (A1, A3, A6 Scope; A8 Scope (d); C5 items), Simon V.15 + Remark | Theorem T.2 (`thm:routeT`, p. 4), proof §4 |
| 16 | Printed proof of Thm 1.1.7 reaches: P1 (Lemma 7.4) and P2 (D.3) on R1 and R2; P3–P4 (Route T) on R1 only; D.4 class (T) (A8(iv)-T) on neither | proved, as a statement about the source's printed proof | Prop. T.17 (`prop:reach`, p. 19) |
| 17 | On R2 no route via a quadratic observable and the Lemma D.2 comparison around a fixed-shape box is reached (exact step where the stronger claim fails) | proved | Remark T.18 (`rem:obstruction`, p. 20) |
| 18 | GJS's own application on p. 595 (∏Φ(f_i) with ≥ 2 fields against V(g_i), all orientations) is reached by their printed proof only on R1 | proved, as an observation about the source's logic | note §5.3 |
| 19 | N.39: the D.3 parallel pairs are reached after slicing U_{Δ,n} (Fubini), on R1 and R2; no multi-time reading | proved | Prop. T.19 (`prop:N39`, p. 21) |
| 20 | The sketch's steps (a)–(d) and constants | confirmed: (a) also gives the sketch's (1+λ₀R/π) form; (b), (c) (c_k ≤ 2), (d) as stated, with the GJS-norm *bound* (not the norm) unchanged | note pp. 8, 16 |
| 21 | After Route T, items (1)–(4) rest on: P1, P2 (reached on both readings) and P3, P4 (reached on R1 only); the gap clause of (5) on P1, P2 only; the moment clause of (5), Thm 5.1, Cor. 5.2 still on A8(iv)-T | proved (as a dependency analysis), with claims 15–16 | note §5.5, §7.2 |

Record locators used: `thm:MAIN` 12.2 p. 41 (ll. 3057–3124); `lem:separation` 9.2 p. 36 (ll. 2608–2670); `lem:cluster` 9.3 p. 37 (ll. 2672–2715); `lem:statederiv` 10.1, `lem:localize` 10.2, `lem:tworegime` 10.3, `prop:onepath` 10.4 p. 38 (ll. 2723–2872); `lem:rate` 10.5 p. 39; `thm:M2` 5.1 p. 27 (ll. 1843–1954); `thm:D4` D.4 p. 100 (ll. 7009–7125); `lem:D2` D.2 p. 88 (ll. 6276–6449); `thm:D3` D.3 p. 95; `aux:d3-orient` N.39 p. 96 (ll. 6804–6825); A8 item (iv-T) ll. 1151–1169.

## 3. Findings

**F1 (MINOR). Remark N.39** (`aux:d3-orient`, N.39, p. 96, `part_i/main.tex` ll. 6814–6818).
- Text: "The partner U_{Δ,n} is of type (1.1.6); the printed proof reaches the pair only after U_{Δ,n} is sliced in time and the bound is integrated over the slices, the multi-time reading of (1.1.5) that the plan records (Part 2) and GJS do not print."
- Why it is inaccurate: U_{Δ,n} has r = 1 (Definition N.17), so its time slices are one-time monomials, and the sharp-time pieces have all their factors at one time. Every pair of slices is therefore admissible on either reading of p. 596; no multi-time reading is involved. What GJS do not print is the Fubini step. Proposition T.19 writes it out: the Bochner representation (Lemma T.12), the covariance as a bounded functional, and ∫‖U(t)‖_GJS dt ≤ ‖U‖_GJS.
- Repair (proposed wording, note p. 22): "… the printed proof reaches the pair after U_{Δ,n} is sliced in time and the bound is integrated over the slices, a Fubini step that GJS do not print (ugjs/route_t.tex, Proposition T.19); every pair of slices consists of two monomials of type (1.1.5), each with all its factors at one time, so the pair is reached on either reading of the equal-times sentence of p. 596, and no multi-time reading is needed."
- Severity: MINOR. This confirms the finding N3 of 22 November. Consequence: the uniform gap rests only on applications the printed proof reaches.

**F2 (MINOR). The sketch of 22 November** (status memo of the constructive-QFT member, §2 "Item 3: Phase C", step (d), and the paragraph after it).
- Text: "But every application of CE2 now pairs two time-integrated monomials. That is the kind of pair GJS themselves treat in all orientations on p. 595" and "One reading remains: the multi-time reading of A in Thm 1.1.11 that p. 595 supports."
- Why it is incomplete: the sentences are correct. They omit that the reading is needed in both orientations, including the parallel class P3. The record's parallel class of D.4 is reached on either reading, so on R2 Route T reaches none of its applications (Prop. T.17(c)). Remark T.18 shows that no route of this type can be reached on R2.
- Repair: state that Route T replaces A8(iv)-T by reading R1 for all of its applications.
- Severity: MINOR.

**Observation (no change needed).** Prop. 10.4, Step 3 (ll. 2850–2856): "j ∈ [b+n−1, b+n+2], an interval containing at most four integers". The true set is the half-open interval [b+n−1, b+n+2), which contains at most three integers. The record's bound is true and weaker. The memo noted the same.

**For the auditor: the steps I am least sure of.**
1. The measure theory of Lemma T.12: joint measurability of (t,x,q) ↦ A_κ(t,x)(q), separability of L²(dμ₀) via a countable dense set in S(R²), and the passage κ → ∞ inside the Bochner integral.
2. Lemma T.15(ii) rests on Simon's Remark on p. 164 ("More generally, the above holds if G_j^F ∈ ∩_{p<∞}L^p(Q_F) …"), a printed sentence without proof. A truncation argument like the record's Lemmas 4.1/4.3 would avoid it; I did not write that variant.
3. The principal-value computation (sign and limit) in Step 3 of Lemma T.5. It was tested numerically at three parameter sets.
4. Prop. T.17(c) and Remark T.18: the claim that, on R2, the two-time slices carry the whole integral, so that no other use of the printed proof reaches P3–P4. Also that any quadratic-observable route needs transverse two-factor applications.
5. The observation that GJS's own p. 595 use needs R1.
6. The notion "reached by the printed proof" (note §5.4). It follows the record's usage. Two questions about the source's proof are left open and affect all cases alike: the constant taken from Theorem 1.1.8 at the same h, and the half-integer translation of the squares. Rotation covariance of the GJS setting is presupposed by "rotating"; I did not prove it, and no proof of the note uses it.

## 4. Checks actually run

- Build: three passes of `/Library/TeX/texbin/pdflatex -interaction=nonstopmode route_t.tex`.
  - `grep -cE '^!' route_t.log` → 0.
  - `grep -c Overfull route_t.log` → 0 (the first build had 14; all were fixed).
  - `grep -icE undefined route_t.log` → 0.
  - `pdftotext route_t.pdf - | grep -nE '\?\?|TODO|Hmm|wait,'` → no output (exit 1).
  - `pdfinfo`: 25 pages. `pdftotext | wc -w`: 16,140 words.
- Machine paths: a grep for machine-path prefixes → none after one fix (the script's docstring had named the interpreter path).
- Numerical script `check_route_t.py`.
  - Run with the system python3: Python 3.14.7, numpy 2.5.2, scipy 1.18.1, mpmath 1.4.1; seed 20261123.
  - The output file ends "ALL CHECKS PASSED", with 21 PASS lines.
  - k(E) closed form: max rel. error 9.23e-30 (tolerance 1e-12).
  - Inequality T.11: min margin 3.523e-04 ≥ 0 on a 4·10⁵-point grid.
  - f_{a,ε} transform: error 2.87e-42.
  - Principal-value limit, errors for ε = 1e-2, 1e-3, 1e-4:
    - 4.99e-3, 5.01e-4, 5.01e-5;
    - 6.92e-3, 6.94e-4, 6.94e-5;
    - 1.08e-2, 1.09e-3, 1.09e-4.
  - Resolvent identity (b): abs. error 0.00e+00 (tolerance 1e-10).
  - Discrepancy formula: 1.02e-16.
  - Free field, n = 1: E[V̄²] = 0.478114 ≤ E[V²] = 0.708903.
  - The first run printed "FAIL k(E) closed form" (rel. error 1.14e-3). Cause: a defect in the test. `E - 1` was evaluated in double precision before mpmath, which cancels at E = 1e-6. I fixed it (`E = mp.mpf(E)`) and re-ran; the closed form itself was correct. The final run is the one recorded.
  - Numerical only: nothing in the note is deduced from it.
- Record checks.
  - `grep newlabel part_i/main.aux`: full label table; every record number cited in the note was taken from it.
  - §7 (ll. 2055–2389) contains no `thm:M2`, `thm:D4`, `M_B` or "transverse". The cross-references in §7 are D.3 (5), Lemma 7.4 (1), Source Fact 2.2 (1), and others without M.
  - Lines 2389–3165: Theorem 5.1 enters only at l. 2776 (Lemma 10.2), through Lemmas 10.3–10.5, at l. 2921 (§11) and at l. 3104 (proof of 12.2(5)).
- Sources rendered myself (`pdftoppm -r 150`).
  - GJS PDF pages 6, 8–14, 45–46 (printed pp. 589, 591–597, 628–629).
  - Simon PDF page 186 (printed p. 164).
  - Evidence image `simon-fkn-185.png` (p. 163).
  - First pages: GJS = Annals of Mathematics, Vol. 100, No. 3 (Nov. 1974), pp. 585–632; Simon = Princeton University Press, 1974.

## 5. Not done, not verified, not run

- **Not done:**
  - integration into `part_i/main.tex` (the note lists what integration would change, §7.3);
  - §13 of the record (Thm 13.2, Rem. 13.3), not re-examined;
  - no KB node, no `kb` command;
  - no proof of A8(iv)-T, P3 or P4;
  - no decision between R1 and R2;
  - no proof of rotation covariance;
  - S₂ not evaluated;
  - the truncation variant of Lemma T.15(ii) not written.
- **Not verified:**
  - the record statements the note cites (Appendix C; Lemmas D.1, D.2; N.5–N.43; Props 8.1–8.2; Lemma 9.1; Thm 7.8) are used as the record states them, not re-audited;
  - Simon's Theorem I.22 is used only through the record's A4 quotation and the argument of N.21(ii);
  - GJS Chapters 2–4 were not read beyond the rendered pp. 628–629;
  - the KB node `import/a8-iv-t` and the `ugjs/council/` reports were not opened.
- **Not run:**
  - no build of the record;
  - no git command;
  - no independent audit of the note (that is the next step);
  - no subagents.

## 6. Files written

All in the council scratch directory (`scratchpad/c2/`, outside the repository); nothing under REPO.
- `route_t/route_t.tex`: the note, 1,492 lines.
- `route_t/route_t.pdf`: 25 pages. Build by-products: `.aux`, `.log`, `.out`, `.toc`.
- `route_t/check_route_t.py` and `route_t/check_route_t.output.txt`.
- `work/route-t/*.png`: page renders, not for the repository.
- `reports/route-t-drafter.md`: this report.
