# V1 audit, role mp (quantifiers): §§4–6 and §8 of the frozen comparison note

Auditor: mp, council of `ugjs/PLAN.md`. I drafted §3 and §7 of the note and did not audit them here.
Written 2–3 November 2026.
- **Object:** `WORK/frozen-v1/`: `comparison.pdf`, 59 pp., sha256 7e393b9a440fe6a2…, built 2 Nov 2026 16:38.
  Hashes re-checked on 3 Nov and unchanged. The parts `d2.tex`, `d3.tex`, `d4.tex` and `consequences.tex`.
- **Definitions consulted:** `notation.tex` and `constants.tex` (Appendix A); `gates.tex` and
  `comparison.tex` §1 for the status sentences.
- **Record:** `part_i/main.tex`, mtime 2 Nov 15:35, 3181 lines; the record's statements are quoted from it.
- **Locators:** "N.k" and page numbers are those of the frozen build (`WORK/comparison.aux`, which belongs to
  the same build: identical PDF hash). Line numbers are those of the part files.

## Verdict
From the side of quantifiers and constants nothing blocks. The quantifiers are in the right order in
D.2, D.3, D.4 and in the statements §8 replaces. Every constant depends on what the text says it
depends on, and is uniform where the text says it is:
- M_B in h, and hence in T and g;
- A in T and s;
- B′ in I.

So D.2–D.4 and the replaced proofs of §8 can be `proved` as written, conditional on four things:
- Lemma D.1;
- the V3 repairs: R8 for Lemma C.2; R1–R10 for Theorem C.5, S₂ and the shape-only property;
- for D.4, Theorem 5.1 and Corollary 5.2, the GAP of §2;
- the transverse case of Theorem 1.1.7 at the printed statement's scope (F-T).

No finding is CRITICAL or MAJOR. Fourteen MINOR findings follow (F13 concerns my own §7 and is
recorded, not judged). Most concern conditions that are not stated at the place of use, inconsistent
status descriptions, two boundary cases, one unquantified threshold, and one unproved sentence inside a
replaced statement.

## Findings

**F1 (MINOR). The statements of D.2–D.4 carry no status conditions.**
- *Locators:* §4 Lemma D.2 (`d2.tex` ll. 104–130, p. 26); §5 Theorem D.3 (`d3.tex` ll. 191–210, p. 31);
  §6 Theorem D.4 (`d4.tex` ll. 102–120, p. 35).
- *Text:*
  - D.3: "In working coordinates (Remark 3.3 of the record), the constant $A$ depends only on
    $(\lambda,\mathscr P,m_0)$ and on $N_B$, through the unevaluated constant $S_2$; … Both are independent
    of $T$ and $s$".
  - D.4: "with $S_2(B_{3\times5})$ the value of Definition N.14 at any box of 3 rows and 5 columns".
- *Why:*
  - The independence of A from s, and the phrase "at any box", rest on Proposition N.15(iii), which
    §2 proves conditional on R1–R10 (translation covariance through Lemma C.4).
  - D.3 and D.4 use Lemma C.2 (R8), and D.2–D.4 use D.1.
  - V_* and 9^{p′} in M_B rest on the GAP after Lemma N.20 and on R8 (Lemma N.21).
  - These conditions are given in Remark N.32 (`aux:d3-V3`), Remark N.44 (`aux:d4-not`) and some proof
    steps, but not in the statements. Read alone, or after integration into the record, the statements
    look unconditional. The brief asks for the conditions at each use.
- *Repair:* a status line after each statement.
  - D.2: "proved, conditional on Lemma D.1" (see F3).
  - D.3: "proved, conditional on Lemma D.1, Lemma C.2 (repair R8) and Theorem C.5 with Proposition N.15
    (repairs R1–R10)".
  - D.4: the same, plus "the GAP after Lemma N.20 and repair R8 (Lemma N.21)", plus F-T.

**F2 (MINOR). D.4, Step 2 does not name the GAP where it is used.**
- *Locator:* `d4.tex` ll. 135–137, p. 35.
- *Text:* "Lemma N.21(ii), applied to $Y:=V(h')(0)$, gives
  $\|Q_V\|_{L^2(\dmu)}=\|Y^2\|_{L^2(\dmu)}\le9^{p'}V_*$. (Lemma C.2, Theorem C.5 through $S_2$, and the
  comparison are used as in Remark N.32.)"
- *Why:* Remark N.32 does not mention the GAP. Both V_* (Lemma N.20) and N.21(i), which gives
  "$\|Y\|_{L^2(\dmu)}=\|V(h')\|_{L^2(\dphi)}$", identify the record's V(h′) with the constructed limit,
  which is the GAP. The GAP is named in §6.1 (ll. 44–47, p. 33) and in Remark N.44 (ll. 261–262, p. 37),
  but not at this step.
- *Repair:* add "and on the GAP recorded after Lemma N.20".

**F3 (MINOR). D.2's dependence on Lemma C.4 has an unspecified condition, three descriptions of D.2's
status disagree, and the dependence can be avoided.**
- *Locator:* `d2.tex` ll. 154–156, p. 27.
- *Text:* "(Lemma N.18(iv) rests on Lemma N.5(iv), which uses Lemma C.4 of the record; that dependence is
  conditional on the V3 repairs, as in Remark N.32)".
- *Why:*
  - Remark N.32 lists Lemma C.2 (R8), Theorem C.5 (R1–R10) and the Wick structure (R8). It does not list
    Lemma C.4, which §2's introduction places under R1–R10.
  - The three descriptions of D.2's status are: this sentence ("the V3 repairs"); aqft's report
    (`REPORTS-drafters.md`, "D.2 proved conditional on Lemma D.1 … and on V3 repair R8"); and the gate
    record (`gates.tex` ll. 8–10, D.2 "proved conditional on Lemma D.1 and on Lemma C.2 and Theorem C.5").
    Yet D.2 uses neither Lemma C.2 nor Theorem C.5.
  - The decomposition 𝒰_{h−h^B} = Σ_{Δ∈𝒟}(U_{Δ,0}+U_Δ) needs no Lemma C.4. Step 1 of the proof of D.1
    (`d1.tex`, p. 23) shows that λ∫w:𝒫(Φ_κ):dz converges in L² for every bounded measurable w of compact
    support and either sign (by N.26(a)), and that the limit is linear in w. With w = h1_Δ, and with
    N.26(b) for the uncharged squares (‖w‖₂ = 0), this gives the decomposition. It uses only the record's
    identification of 𝒰_h, which D.2 already carries through D.1.
- *Repair:* cite D.1, Step 1 for the decomposition; D.2 is then conditional on D.1 alone. Otherwise
  write "R1–R10 (Lemma C.4)". Make aqft's report line and the gate record agree.

**F4 (MINOR). §8's introduction misstates the inputs of the replaced Lemma 4.3(ii).**
- *Locator:* `consequences.tex` l. 27, p. 43.
- *Text:* "The replaced proof of Lemma 4.3(ii) uses Assumption A3 only."
- *Why:*
  - The replacement (ll. 75–92, p. 44) also uses "Gaussian moments of the free field, Appendix D, §3" and
    A5(i). The Check paragraph (ll. 95–98) lists these correctly.
  - The replacement names "$|V(h)|$ in §5" among the observables with $F(\Phi(s,\cdot))\in L^4(d\mu_0)$.
    For V(h) this rests on the GAP.
  - The GAP is avoidable here. The record applies Lemma 4.3 to |V(h)| in §5 only through part (i)
    (Theorem 5.1, Step 5, main.tex l. 1319 ff.), and the membership ψ_a ∈ D(V(h)) "also follows
    independently from Assumption A5(i)", as the replacement keeps.
- *Repair:* replace the sentence by the Check's list. In the replacement, restrict the L⁴ clause to the
  cylinder monomials of §7 and keep A5(i) for |V(h)|, or else name the GAP.

**F5 (MINOR). The replaced Lemma 7.1 cites Theorem D.3 outside its hypothesis in a boundary case.**
- *Locators:* `consequences.tex` ll. 117–120, p. 45; D.3 at `d3.tex` ll. 192–193.
- *Text:* "Let $A$ and $B'$ be the constants of Theorem D.3 for the cutoff $g$, the interval $I$ of §6 and
  the time $s=0$."
- *Why:* D.3 requires "$I\subset\R$ … a bounded interval of positive length". The record's §6
  (main.tex ll. 1353–1354: "all supported in an interval $I$ of length $L$") does not require L > 0.
  If L = 0, every f_i ∈ C_c^∞ supported in I vanishes, Q = 0 and the lemma is trivial, but D.3 does not
  apply as cited. Lemma 7.6 is unaffected: f ≠ 0 forces L > 0.
- *Repair:* add "(if $L=0$, then $Q=0$ and there is nothing to prove)".

**F6 (MINOR). The replaced statement of Lemma 7.6 contains an unproved claim.**
- *Locator:* `consequences.tex` l. 230, p. 47.
- *Text:* "The radius $1/K_f$ is an artefact of the route through the GJS norm." This sentence is inside
  the replacement statement.
- *Why:* "Artefact" asserts that the radius is not a property of μ_g. Neither the note nor the record
  shows exponential moments beyond 1/K_f.
  - The record's own last sentence is a fact about the formula: "The factor $C_8K_1$ affects only the
    prefactor, not the radius $1/K'$" (main.tex l. 1617).
  - Trap 25 corrects the opposite wording ("intrinsic"); the correction belongs in a remark, not in the
    statement of a lemma.
- *Repair:* move it to a remark after the lemma, for instance "The radius comes from the route through the
  GJS norm; whether $\E_{\mu_g}e^{s|X_f|}<\infty$ for larger $s$ is not decided here (trap 25)".

**F7 (MINOR). An unquantified threshold in the radius paragraph for Theorem 7.7, and an empty minimum.**
- *Locator:* `consequences.tex` ll. 258 and 271–272, p. 47.
- *Text:* "Differentiation under the integral is justified, as in the record, by the exponential dominator on
  a slightly smaller polystrip"; and $s_0:=\min_{1\le j\le k,\ e_j\ne0}(2kK_{e_j})^{-1}$.
- *Why:* AGENTS 3.3 requires thresholds as inequalities, and "slightly smaller" is not one. If all
  e_j = 0, the minimum is over the empty set. Appendix A (Remark N.52, `constants.tex` l. 268) says "(any
  $s_0>0$ if all $e_j=0$)"; §8 does not.
- *Repair:* "on every polystrip $\{|\mathrm{Re}\,z_j|\le s_1\}$ with $0<s_1<s_0$, where $2k|\mathrm{Re}\,z_j|\le2ks_1<1/K_{e_j}$"; and add Appendix A's convention for all e_j = 0.

**F8 (MINOR). The check after Lemma 7.6 states the dependence of K_f wrongly.**
- *Locator:* `consequences.tex` ll. 249–250, p. 47.
- *Text:* "$A_f$ and $K_f$ are independent of $n$ …; they depend on $g$ and on $f$ (through $I$, $N_B$,
  $N_I$, $\|f\|_2$ and $\sigma_f$)."
- *Why:* K_f = max{K′, √2σ_f} depends on neither g nor N_B; only A_f does. Appendix A (table row K_f,
  `constants.tex` ll. 349–350, p. 55: "uniform in $n$, $g$"), Remark N.52 ("$s_0$ … not on $g$") and §7
  say so, and the g-independence of s₀ uses it.
- *Repair:* "A_f depends on g and on I (through N_B); K_f depends on f (through ‖f‖₂, σ_f and N_I), on K₂
  and on m₀, and not on g."

**F9 (MINOR). In Remark N.39, "N_g = 0 (g = 0 a.e.)" holds in one direction only.**
- *Locator:* `d3.tex` l. 312, p. 33.
- *Text:* "$N_g=0$ ($g=0$ a.e.): $h_{T,g}=0$ a.e., $B'=0$, and the bound is the base term."
- *Why:* supp g is the closure of {g ≠ 0} (Definition N.4). So N_g = 0 implies g = 0 a.e., but not
  conversely. Counterexample: g := 1_{ℚ∩[0,1]} ∈ 𝒞_H vanishes a.e., while supp g = [0,1] meets columns 0
  and 1 in positive measure, so N_g = 2. The bound remains true, since no square is charged and B′ merely
  overestimates.
- *Repair:* "$N_g=0$ (which implies $g=0$ a.e.)". Add: "if $g=0$ a.e., no square is charged and the
  comparison term vanishes, whatever $N_g$".

**F10 (MINOR). In Remark N.39, the case "T < 1" treats only T ≤ ½.**
- *Locator:* `d3.tex` ll. 299–304, p. 33.
- *Text:* "$T<1$. … for $T\le\frac12$ only row $0$ does. If moreover $|l_s|\le1$, then
  $\mathcal D(h_{T,g},B)=\varnothing$ …; if $|l_s|\ge2$, then $h_{T,g}^B=0$".
- *Why:* For ½ < T < 1 the rows −1, 0, 1 are charged. Then 𝒟 = ∅ only for l_s = 0, and "|l_s| ≥ 2 ⇒
  h^B = 0" fails: for l_s = 2, row 1 lies in B. Read with "moreover" as restricting to T ≤ ½, the text is
  correct, but the range ½ < T < 1 is not covered.
- *Repair:* add the case, as §7.3(1) does: for ½ < T < 1, 𝒟 = ∅ iff l_s = 0; otherwise the charged squares
  outside B are at row distance ≥ 2 and the general parallel case applies.

**F11 (MINOR; could matter at integration). Theorem 12.2's imports paragraph.**
- *Locator:* `consequences.tex` ll. 357–362, p. 49.
- *Text:* "Its statement keeps its text except the imports paragraph (ll. 2415–2424), whose rewrite at
  integration is listed in the plan (Part 6) and is not drafted here".
- *Why:* The record's paragraph ends "The theorem is an implication from exactly this list of printed
  statements; no other external input is used" (main.tex ll. 2423–2424).
  - From Phase A on, the gap clause of (5) rests on Theorem D.3, hence on Lemma C.2 and Theorem C.5 under
    the V3 repairs. R8 imports Simon's definitional facts on Wick powers.
  - From Phase B on, item (5) rests on Theorem D.4, hence on the GAP; so does item (1), through M = M_B.
  - PLAN Part 6 predates both the V3 report and the GAP, so the deferred rewrite would not list them.
  - The note's §1 sentence "No new import is made" (`comparison.tex` l. 69) has the same issue once R8 is
    adopted.
- *Repair:* in §8.7, record that the rewritten paragraph must name the construction of the Wick powers
  (R8, and its time-zero companion closing the GAP), or that items (1) and (5) stay "proved, conditional
  on …" until it is supplied.

**F12 (MINOR; cross-check with the master §1). Theorem 7.7's radius.**
- *Locators:* `comparison.tex` ll. 56–59, p. 2; against §8.5, `consequences.tex` l. 253, p. 47.
- *Text:* §1 says the note "changes no statement except through the value of the constants that contained
  $C_8$ (… the constants of Lemmas 7.1 and 7.6 and the radius of Theorem 7.7 …)". §8.5 says "The
  statement of Theorem 7.7 (ll. 1637–1642) is unchanged and so is the text of its proof".
- *Why:* The record's statement of Theorem 7.7 contains no radius: "Cylinder polynomials are dense in
  $L^2(d\mu_g)$. Equivalently, …", main.tex ll. 1639–1641. The polystrip is in its proof (ll. 1652–1653). §8 is
  right and §1 is not.
- *Repair:* in §1, "and the radius in the proof of Theorem 7.7".

**F13 (recorded for the orchestrator; my own §7, not audited by me).** §7 omits the GAP from the dependence
of M_B and of 9^{p′}.
- The text in `quantifiers.tex`, D.4 bullets and F3: "the unevaluated constant $S_2(B_{3\times5})$ of
  Theorem C.5 (conditional on R1–R10) and the finite $V_*$", and, for 9^{p′}, "it rests on the chaos
  structure … (its M-3, repair R8)".
- Repair, in §7: add "and, through $V_*$ and Lemma N.21, on the GAP recorded after Lemma N.20".
- §7's order for D.3 ("$g$, $I$, $s$; then $A$, $B'$") is valid. It is weaker than Remark N.38's ("for
  every $g$ and every bounded interval $I$ … the constants $A$ … and $B'$ … are fixed; then the bound holds
  for every $s\in\R$"), which is also correct and could replace it.

**F14 (MINOR; Appendix A, cross-check). The "cond." legend omits the GAP.**
- *Locator:* `constants.tex` ll. 303–306, p. 55.
- *Text:* "'Cond.' marks a constant whose finiteness or bound uses Lemma C.2, Lemma C.4, Theorem C.5 or the
  comparison step in the proof of Theorem C.5, hence is proved conditional on repairs of the V3 audit".
- *Why:* The rows for V_*, 9^{p′}, M_B and M_B (φ⁴) also rest on the GAP: V_* through the identification of
  the record's V(h′), and 9^{p′} through Lemma N.21(i). cqft2's own report lists N.54 (M_B) as
  "conditional on D.1, V3 and the GAP". The table does not show this.
- *Repair:* extend the legend, and mark these four rows.

## Holds (checked)
- **H1. Order of quantifiers.**
  - D.2: F, R, B, h, then (a) any assignment of strips over 𝒟(h,B); (b) a hypothesis on all squares outside
    B meeting supp h. The constants are fixed before h, B, R and F.
  - D.3: g, I and s, then A and B′, then F and T. Remark N.38 has the stronger order g, I, then A and B′,
    then s, F and T, which holds because A is independent of s.
  - D.4: M_B, then h, a and h′ (Remark N.42).
  - No "there exists" is chosen after a variable it must be uniform in.
- **H2. M_B is uniform in h, factor by factor:**
  - C₇ and m₁: "constants … independent of $h$, $Q_1$ and $Q_2$" (Theorem 1.1.7, p. 594, which I read on the
    image this session), read over 𝒞_E (main.tex ll. 887–889);
  - c_U, through ‖h1_Δ‖₂ ≤ 1;
  - Σ̄₃ₓ₅, which contains no h;
  - S₂(B₃ₓ₅), a supremum over all h′ ∈ 𝒞_E with supp in the box;
  - Z(h^B) ≥ e^{−15λ|a₀|};
  - V_* and the bound on ‖Q_V‖_GJS, which contain no h.
  - Uniformity in a holds through Proposition N.15(iii), conditionally (F1).
- **H3.** A is uniform in T (there is no T in it) and in s. B_s(g,I) moves by whole rows, N_B = k₊ − k₋ + 1
  does not involve s, and S₂ is shape-only (conditional, F1).
- **H4.** B′ contains no I and is uniform in the position and length of I. It depends on g only through N_g.
- **H5. Charged squares.**
  - D.3 and D.4 use form (a) of D.2 over 𝒟(h,B).
  - D.3: Lemma N.36(i) gives k ∈ K_g and |l − l_s| ≥ 2 for charged squares outside B. Each j ≥ 1 occurs for
    exactly two rows, hence the count 2N_g.
  - D.4, Step 3: Δ ∈ ℒ_j with |l| = 1+j is class (P), width j. With |l| ≤ j it lies in a side column
    k_a−1−j or k_a+3+j and is class (T), width j. Corners go to (P). The sum is at most Σ̄₃ₓ₅.
  - The example in N.31(3) (g = 1_{[0,1/10]} + 1_{{3}}, T ≥ |l_s| + 2) is correct as written.
- **H6. The radius s₀.** s₀ = min_{j: e_j≠0}(2kK_{e_j})⁻¹ appears both in §8.5 and in Appendix A, Remark N.52.
  The Cauchy–Schwarz step, and Hölder with k exponents k, were re-derived. s₀ does not depend on g.
- **H7. Traps.**
  - 8: Remark N.40.
  - 9: N.44, "the converse is not claimed".
  - 10: the rider in the statement of D.4 and in N.44; §8.6–8.7 give "value $M_B$". The sentence "After
    Phase A alone, $M$ is unchanged" (§8.8) is true and is not the trap's wording.
  - 11: §8.7 cites Lemma 10.2 by name with value M_B, and claims nothing about g-uniformity being needed.
  - 17: N.44.
  - 20: N.31(1).
  - 25: the wording in §8.5 follows the trap; see F6 for where it stands.
- **H8. §8's replaced statements keep the record's quantifiers.** The record's statements, quoted from
  main.tex:
  - Theorem 5.1 (ll. 1255–1267): "For every $g\in\CH$ and every real measurable $h$ with $\|h\|_\infty\le1$
    and $\supp h$ contained in an interval of length $2$, $\|V(h)\Om_g\|\le M$". Kept, with M := M_B.
  - Corollary 5.2 (ll. 1342–1347): "For $\mathscr P(\xi)=\xi^4$ ($p'=2$, $\sum_n|a_n|=1$; degrees exactly
    $4+4=8$), $M^2=9\cdot8!\;C_8K_1K_2^{16}\lambda^2$". Kept: the same P, with the new value.
  - §7's standing clause (ll. 1424–1425): "$g\in\CH$ is arbitrary and fixed, and $Q=\prod_{i=1}^r\varphi_0(f_i)$
    is as in §6". Lemma 7.1 (ll. 1428–1432): "$\sup_{T>0}\|Q\hat\psi_T\|^2\le C_8\,\mathfrak n(Q)^2$;
    moreover $\Om_g\in D(Q)$ and $\|Q\Om_g\|^2\le C_8\,\mathfrak n(Q)^2$". Kept, for every fixed g and Q;
    the constants now depend on g and I (a disclosed change), apart from F5.
  - Lemma 7.6 (ll. 1603–1618): "for real $f\in C_c^\infty(\R)$, $f\ne0$, supported in an interval of length
    $L$ … $(n\ge1)$ … $(0\le s<1/K')$". Kept, with A_f, K_f and 0 ≤ s < 1/K_f.
  - Theorem 7.7 (ll. 1637–1642): unchanged.
  - The statements of Lemmas 4.3, 7.2 and 7.3: unchanged.
  - The fixed A and B′ of Lemma 7.1 are what make Lemma 7.6's A_f and K_f independent of n.
- **H9. Appendix A** (table on p. 55; Propositions N.47 and N.48; N.51; N.52) agrees with §§5–6 and §8 on
  what c_U, S₂, A, B′, A_f, K_f, s₀, Σ̄₃ₓ₅, V_*, 9^{p′} and M_B depend on and are uniform in, apart from F8
  and F14.
- **H10. Thresholds are inequalities:** T ≤ ½, |l_s| ≤ 1, |l_s| ≥ 2, T ≥ |l_s| + 2, n ≥ 1, 0 ≤ s < 1/K_f
  and 2k|Re z_j| < 1/K_{e_j}. The exception is F7.
- **H11. GA6 re-run.** The grep of §8.8, run on main.tex on 3 Nov, prints exactly the lines §8.8 lists:
  1731, 1859–1860, 2110, 2252, 2254, 2394, 2417, 2429–2430, 2486 and 2530.
- **H12. Record locators used in §§4–6 and 8, verified:**
  - A8 Scope (d), ll. 887–889;
  - Lemma C.2's notation "Λ compact", l. 2902;
  - Lemma 4.3 with its proof, ll. 1184–1220;
  - Theorem 12.2's imports paragraph, ll. 2415–2424, and its proof from l. 2427;
  - the statements of Theorems 5.1 and 7.7, Corollary 5.2 and Lemmas 7.1 and 7.6 at the cited lines.
- **H13. ξ⁴ arithmetic:** 9·8! = 362 880; 24·362 880 = 8 709 120; 81·24 = 1944. It is consistent between
  §8.6 (Corollary 5.2) and Appendix A.

## Not checked
- §3 and §7 (mine).
- Whether each application of Theorem 1.1.7 is legitimate at the level of GJS, and the transverse case
  (role cqft).
- The GA5 grep, which I did not re-run.
- The V3 repairs themselves, and Lemmas C.2–C.5.
- The proofs in §2 (`notation.tex`) behind the statements I cite (N.5, N.15, N.18, N.20, N.21, N.36). I read
  their statements and the GAP note (`notation.tex` ll. 926–936), not their proofs.
- The proofs in Appendix A beyond Propositions N.47 and N.48 and Remarks N.51 and N.52.
- The record's own Appendix A rows (ll. 2655–2685), which §8.7 lists.
- The numerical scripts (`aqft_checks.py`, `cqft2_ringcheck.py`), not run.
