# REPORT-mp: Lemma D.1 (`parts/d1.tex`) and the quantifier section (`parts/quantifiers.tex`)

Drafter: mp (council of `ugjs/PLAN.md`). Drafted 31 October and 2 November 2026.
- Read this session:
  - BRIEF-AB.md; `ugjs/PLAN.md` (all 1004 lines); `memo-mp.md`; `r1b-attack-cqft.md`;
    `r1c-orchestrator-rulings.md`; §3 and the MINOR items of `r3-verifier-report.md`;
    `audits/V3-appendixC-report.md` (§§0–2 and 5–12).
  - `part_i/main.tex`: §§2.1–2.6, 3, 4, 5, 6, 7, 8.1–8.2, Lemma 10.2 and Appendix C. Its state of
    2 Nov 15:34: label numbers and pages re-checked against `main.aux` and identical to `labels-main.txt`;
    lines of Appendix C shifted by +2.
  - GJS on the page images pp. 593, 594, 595 (`gjs74/p-10, p-11, p-12`), and p. 594 at 300 dpi
    rendered from `refs/`.
  - The other drafters' parts as they stood between 15:46 and 16:10: `notation.tex`, `d2.tex`, `d3.tex`,
    `d4.tex`, `consequences.tex`.
- Not read: Simon's book, `constants.tex`, `gates.tex`.

## 1. What I drafted
- **`parts/d1.tex`** (§3; 3460 words of source; pp. 17–24 of my master-copy build, about 7.5 pp).
  Numbers below are those of that build.
  - N.22, Lemma `aux:d1-wick`: moments of products of Wick powers of jointly Gaussian variables,
    by generating functions. It includes Wick orthogonality and isometry.
  - N.23, Lemma `aux:d1-cov`: the free covariance.
    - The heat-kernel formula for G.
    - The kernel of (2μ)⁻¹ is C(x) = G(0,x), derived here.
    - Positivity, monotonicity and G ≤ g₀ + (2π)⁻¹log₊(1/|ζ|).
    - A κ-uniform log majorant M₁ of the regularized covariances.
    - Local integrability of every power of M₁.
  - N.24, Definition `aux:d1-obs`: localized monomials of type (1.1.5) (equal or distinct times)
    and (1.1.6), defined as L²-limits of their regularizations with the record's mollifier.
  - N.25, Remark `aux:d1-def`: provenance of that definition.
  - N.26, Lemma `aux:d1-moments`:
    - (a) the limits exist;
    - (b) E[Q^{2j}] ≤ ‖Π_{Q,j}‖_{L²(K^{2j})}‖w‖₂^{2j}, hence every F in the class lies in L^q for all q < ∞;
    - (c) a product kernel gives the product of the Wick powers;
    - (d) Wick orthogonality and isometry for the limits.
  - **Lemma D.1** (`lem:D1`), with a proof in Steps 0–6. Every Hölder exponent is written: (2,4,4)
    and (2,2), or (p₀, 2p₀′, 2p₀′) for any F ∈ L^{p₀}, p₀ > 1.
  - N.27, Remark: what the proof uses and what it does not.
  - N.28, Remark: a one-variable check of signs and normalization.
- **`parts/quantifiers.tex`** (§7; 2933 words of source; pp. 41–46, about 5 pp).
  - 7.1 The fixed data, F1–F3, with the dependence of C₇, m₁, K₁, K₂, n̄, c_U, S₂, Σ₃ₓ₅, V_* and 9^{p′}.
  - 7.2 The order of quantifiers and the dependence and uniformity of every constant, for each of:
    - D.1, D.2 (form (a)), D.3 and D.4;
    - Lemma 4.3(ii), Lemmas 7.1, 7.2, 7.3 and 7.6;
    - Theorem 7.7 (half-width s₀ := min_j (2kK_{e_j})⁻¹), Proposition 7.5 and Theorem 7.8;
    - Theorem 5.1 with M := M_B, and Corollary 5.2 (the ξ⁴ instance);
    - Lemma 10.2, and the transport by Remark 3.3.
  - 7.3 Eleven boundary cases, each written out (§3 below).
- **`parts/check_d1.py`**: the checks of §3 below.
- **Fallback Lemma L, not drafted; what it would need.**
  - It replaces Lemma 7.1 by a bound for T ≥ t_* := 1/m₀ only, with constant A_N depending on |supp g|
    and the L⁴(dφ₀)-norm in place of the GJS norm.
  - (i) The L²→L⁴ bound ‖e^{−t_*K(g)}‖_{2→4} ≤ ‖e^{−𝒰_{1_{[0,t_*]}⊗g}}‖_{L¹¹(dμ₀)}. It follows from
    A2 and A4 by the record's pairing argument (Prop. 8.1, Step 1) with Hölder exponents 11/10, 11,
    40/33 and 40/7. Only the exact check (40/7−1)/(20/11−1) = 121/21 < e² has been verified so far.
    Alternatively import Simon Thm V.10(iii), p. 156 (trap 24); that would be a new import.
  - (ii) Z_N < ∞: Theorem C.5 at p = 11, conditional on the V3 repairs, plus translation invariance.
  - (iii) Two elementary steps that my memo tested only numerically. Both now have short proofs:
    - the spectral Jensen inequality ‖e^{−tH}φ‖ ≥ ‖φ‖e^{−t⟨φ̂,Hφ̂⟩};
    - Chebyshev's association inequality for the spectral measure of Ω₀ (E increasing, e^{−2sE}
      decreasing), which gives ⟨ψ̂_s,Hψ̂_s⟩ ≤ ⟨Ω₀,HΩ₀⟩ = λa₀∫g − E(g), using Ω₀ ∈ D(H₀) ∩ D(V(g)).
    - These must be written out and audited.
  - E(g) cancels. Lemma 7.6 then holds for every s ≥ 0. Lemma L needs no CE2, but it changes the
    statement of Lemma 7.1.

## 2. Status, in the brief's sense
- **Lemma D.1: proved** from the named inputs, with no GAP and no `gapnote`. The inputs are:
  - A2 (μ₀ Gaussian with covariance (−Δ+m₀²)⁻¹);
  - A3 as the record states it, quoted in Step 2;
  - the record's identification of 𝒰_h (h ∈ 𝒞_E) with the L²-limit of 𝒰_{h,κ} (Appendix C, notation
    paragraph, p. 39). The record gives no other construction of 𝒰_h (V3 finding M-3). If that
    identification is not accepted as the definition of 𝒰_h, D.1 is "proved, conditional on it". It is
    used only for linearity in Step 1, where the existence of the limits is proved here (N.26(a)).
  - elementary analysis: Hölder, dominated convergence, Fatou, Fubini, and the fundamental theorem of
    calculus.
- **What D.1 does not use:** Lemma C.2 (cited in Step 4 only as an aside, marked "proved conditional on
  the repairs R1–R8 of the V3 audit"), Theorem C.5, A4, the chaos decomposition, hypercontractivity and
  the record's Wick isometry for 𝒰_h. It is therefore untouched by V3's M-1, M-2 and M-3, except
  through the identification just named.
- **N.22, N.23 and N.26: proved** from A2 and elementary analysis. N.24 is a definition.
- **§7:** restates D.2–D.4 and the consequences with their quantifiers. Its own small claims are proved
  inline: s₀ = min_j (2kK_{e_j})⁻¹; the 3×4 ring count 8j+10; the example g = 1_{[0,1/10]} + 1_{{3}};
  the edge cases. Its statements carry the status of D.2–D.4.
- **The note as a whole:** conjectured until audited.
- **GAPs in my parts:** none.

## 3. Boundary cases and checks
- **Boundary cases written out** (§7.3):
  1. T < 1;
  2. T not an integer, including T ∈ ½+ℤ;
  3. s on a lattice line;
  4. N_g = 1 and N_g = 0, with the charged-squares point below;
  5. I meeting one column only;
  6. p′ = 1;
  7. ring k = 1;
  8. [a,a+2] meeting three columns, under both readings, with the 3×4-box alternative;
  9. the n = 0 term of 𝒫;
  10. λ = 0;
  11. D.1 at h₁ = h₂, at constant F and at the endpoints.
- **Charged squares (case 4).** With PLAN's index set {Δ ⊄ B : Δ ∩ supp h ≠ ∅}, D.3's "parallel only"
  claim and its count 2N_g fail. Example: g = 1_{[0,1/10]} + 1_{{3}} ∈ 𝒞_H has N_g = 1, yet column 3
  meets supp g. Form (a) of D.2 (charged squares 𝒟(h,B)), which aqft uses, is needed.
- **None of the eleven fails** with the conventions of §§2–4: half-open squares, l_s = ⌊s+½⌋, and
  form (a) of D.2.
- **By hand:**
  - D.1 in the model N(0,1), 𝒰_h = hX²/2, F = X²: both sides equal −½ (Remark N.28).
  - E[:X²::Y²::Z²:] = 8γ₁₂γ₁₃γ₂₃.
  - The ring-1 list, 20 = 14 + 6.
  - c_U for p′ = 1, and 216K₁K₂⁸.
- **`numerical`**, script `parts/check_d1.py`, run with `/usr/local/bin/python3` 3.14.7, numpy 2.5.2,
  scipy 1.18.1. No project venv exists, and nothing is deduced from these checks.
  1. Lemma N.22 against Isserlis's theorem, in exact rational arithmetic, for 12 degree patterns
     (seed 20261102): all equal.
  2. M₀ − G ≥ 0.319 on 4001 log-spaced points |ζ| ∈ [1e−10, 1e3], for m₀ ∈ {0.05, 0.1, 0.5, 1, 2, 10}.
     The heat-kernel integral equals K₀/(2π) to 12 digits at 3 points.
  3. The one-variable D.1 model, by quadrature: −0.5 on both sides.
  4. Rings of the 3×4 box: counts 8j+10 and strip widths ≥ j for j ≤ 12, in integer arithmetic.
     The first run failed because my script put R in the wrong columns. Fixed, it passes; the claim was
     not at fault.
  5. The rows charged by [−T,T] are exactly |l| < T+½, for 7 rational values of T: exact, passes.

## 4. Deviations from PLAN Part 1 (each a finding for the audit)
1. **D.1's class is made precise.** Localized monomials are defined as L²-limits of their
   regularizations, because the record gives no construction. The proof uses only F ∈ L^{p₀},
   p₀ > 1, so D.1 holds for every such F.
2. **Gaussian moments by explicit diagram bounds and Fatou**, not by A4 and the chaos decomposition.
   This avoids the record's unimported chaos facts (V3 M-3). The brief's "say which": explicit moments.
3. **GA2's input list** (A3, C.2, C.5, Gaussian moments, Hölder, dominated convergence) omits two things
   D.1 uses: the linearity of h ↦ 𝒰_h (Step 1), and Fatou and Fubini.
   - D.1 uses neither C.2 (optional) nor C.5.
4. **D.2's index set.** The charged squares are needed (§3 above). PLAN Part 1's form is aqft's form (b),
   which D.3 and D.4 do not use.
5. **Theorem 7.7's radius.** It is min_j (2kK_{e_j})⁻¹, not 1/K_f. aqft found the same.

## 5. Not done, and what the auditors should attack first
- **Not done.** Simon's book was not read: the comparison ‖Y‖₄ ≤ 3^{p′}‖Y‖₂ is credited to Simon
  Thm I.22 only through the V3 report, and §7 says so. Lemma L was not drafted, as instructed.
- **Attack first:**
  1. **N.26's majorant argument.** Check that every factor of Π_{Q,j} pairs two distinct integration
     variables. Check N.23(iii)'s κ-uniform majorant: the ball-rearrangement step and g₁, b₁. Check the
     pathwise and Fubini steps in N.24 and N.26(b).
  2. **Step 1 of D.1.** It identifies the record's 𝒰_h with lim 𝒰_{h,κ}. This is the one place D.1
     touches the record's undefined object (V3 M-3). The V3 report §12 also leaves open whether this 𝒰_h
     is GJS's interaction in dq_h.
  3. **D.4's Gaussian constants.** `aux:d4-hyper`'s 9^{p′} rests on the chaos structure, conditional on
     V3's R8. V_* now cites my N.26(d). An unconditional alternative exists, with a different constant:
     the explicit fourth-moment bound N.26(b) at j = 2.
  - Also worth checking: aqft's statement of D.4 and its Remark omit trap 10's rider "in working
    coordinates (Remark 3.3)".
- **Traps checked against aqft's drafts** (d2 15:46/16:03, d3 ~16:00, d4 16:04, consequences 16:04):
  - 8 (d3 Remark `aux:d3-not`), 9 and 17 (d4 Remark), 20 (d2 Remark (1)), 25 (consequences, Lemma 7.6
    replacement): respected.
  - 10: respected in the consequences, but the rider is missing in D.4 (MINOR).
  - 11: no prohibited wording; Lemma 10.2 is cited by name with value M_B.

## 6. Errors found
- **E1, master §1 (MINOR).** `comparison.tex` (orchestrator) says the note "does not change the
  statement of any numbered result of the record". This is false: the statements of Lemmas 7.1 and 7.6,
  Theorem 5.1 (M := M_B) and Corollary 5.2 change their constants. aqft found the same.
- **E2, PLAN Part 1, Lemma D.2 (MINOR).** The index set "Δ ⊄ B, Δ ∩ supp h ≠ ∅" makes the D.3 count wrong;
  see §3 for the example. Use the charged squares.
- **E3, PLAN Part 1 (MINOR).** "Theorem 7.7 then has s₀ = 1/K_f": the polystrip half-width for k
  functions is min_j (2kK_{e_j})⁻¹.
- **E4, PLAN Part 3, GA2 and Part 1, D.1 inputs (MINOR).** They omit the linearity of h ↦ 𝒰_h. After V3,
  "Gaussian moments" should not mean the chaos route.
- **E5, record main.tex l. 814 (MINOR, AGENTS 4.6).** A8(vii′)(a), printed p. 12, transcribes GJS
  (1.1.11) as "≤ O(1)e^{−m_1d/2}". GJS p. 594 prints "≦ 0(1)e^{−m₁d/2}" with an upright digit zero; the
  italic "O(1)" of (1.1.10) on the same page differs (300 dpi crop, `build-mp/gjs594-1111b.png` against
  `gjs594-1110b.png`). A silent correction; add the misprint to PLAN Part 9b.
- **E6, GJS p. 595 (source misprint, not used).** "One version of the Feyman-Kac formula": "Feyman" [sic].
- **Repair material for V3 M-2 and M-1.**
  - N.23(iii)'s proof gives, for κ ≥ 2, c_κ ≤ ‖δ‖_∞(4πg₀ + 1 + 2 log κ), with g₀ = (4 + m₀⁻²)/(4π), an
    explicit alternative to the undefined C_* of l. 2917.
  - N.23(ii) derives G ≤ g₀ + (2π)⁻¹log₊(1/|ζ|) from the heat kernel. This covers the log part of the
    "Bessel facts" of Lemma C.4, but not their exponential decay or the gradient bound.

## 7. Test build
- **`build-mp/stub.tex`** (preamble, a dummy §2 label, `d1.tex`, `quantifiers.tex`), pdflatex ×2:
  0 errors, 0 Overfull, 13 pp. The 52 undefined-reference lines point only to labels in other drafters'
  parts or the master, as the brief expects.
- **`build-mp/master-copy.tex`** (a copy of `comparison.tex`; `parts` symlinked; the master itself not
  modified), pdflatex ×2 at 16:12: 0 errors, 0 Overfull, 0 undefined references, 60 pp.;
  `pdftotext | grep -E '\?\?|TODO|Hmm|wait,'` prints nothing.
- **Earlier in the session.** One Overfull box in aqft's `d4.tex` (3.5 pt), since gone. My own Overfull
  boxes were fixed.
- **Other checks.** `\newcommand`/`\def` in my parts: none. Control-sequence scan: only standard macros
  and the preamble's.

## Addendum, 2 November 2026: harmonization at the coordinator's request
- **`quantifiers.tex`**, re-read after the coordinator's edit of 16:31 (repointing to
  `aux:notation-hyper`).
  - **Σ̄₃ₓ₅.** M_B, its dependence, Corollary 5.2 and ring k = 1 now use Σ̄₃ₓ₅ :=
    Σ_{j≥1}(8j+12)e^{−m₁j} = 4x(5−3x)/(1−x)², aqft's `\overline\Sigma_{3\times5}`. (F3) says it bounds
    both the R-dependent Σ₃ₓ₅ of §2 and the sum over the charged squares outside B₃ₓ₅ with the widths of
    the assigned strips. Boundary case (8) says it still bounds the 3×4-box ring sum.
  - **Statuses.** Lemma C.2 is "conditional on repair R8" (D.3's A; D.4's e^{15λ|a₀|}; boundary case 9).
    Theorem C.5 and S₂ are "conditional on R1–R10", pointing to Remark `aux:d3-V3`.
  - **Other edits.** V_* now cites `aux:notation-wick`(iv). §7.1 notes that D.2–D.4 state the
    working-coordinates rider. Boundary case (4) notes that `aux:d2-uses`(3) records the example g.
  - **Checked against the merged wording:** `aux:d2-uses`(3), `aux:d3-cyl`(v), `aux:notation-hyper`,
    D.2(a) (charged squares, strips of positive width), and D.3 (A, B′, I of positive length, rider).
    No further mismatch found.
- **Builds.** `build-mp/stub.tex`: 0 errors, 0 Overfull, 14 pp. `build-mp/master-copy.tex` (a copy of
  the master with the current parts): 0 errors, 0 Overfull, 0 undefined, 58 pp., no `??`.
- The previous `quantifiers.tex` is saved as `build-mp/quantifiers-before-harmonization.tex`.
- `d1.tex` was not touched in this round. It was modified at 16:27 by someone other than me, and I have
  not re-read that version.
