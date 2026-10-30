# Memo `mp` (R1): functional analysis, quantifiers, imports

28 October 2026. Read this session: `docs/status.md`, `docs/imports.md`, `companion/council/labels.md`, `part_i/main.tex` (ll. 1-300, 380-1621, 1625-2400, 2495-2944), `m4/r1-check.tex`, `m4/h6.tex`, `m4/m2-audit.tex`, `part_i/C5_reading_record.md`, `part_i/README.md`, the KB nodes named in the brief, and **page images** of GJS pp. 593-597 (`gjs74/p-10..14`) and of Simon's book pp. 155-159 (PDF 177-181, rendered to `<scratch>/simon/`). Every route below is `conjectured` until written out and audited.

## A. Verdict on O1-O5

**O1: confirmed in substance, modified in its instruments.**
1. *What §7 consumes.* Lemmas 7.2-7.3 (ll. 1353-1425) take T → ∞ at fixed s, t, so every vector ψ_a that occurs has a ≥ T−|s| (resp. T−t/2). With t_* := 1/m_0, restricting to T ≥ |s|+t_* (resp. t/2+t_*) loses nothing, so **the small-T range is never consumed**. Square moments at time s reduce to time zero: by Lemma 4.3(i) and Cauchy-Schwarz, ∫Q(s)² dq_{h_{T,g}} ≤ ‖Qψ_{T−s}‖‖Qψ_{T+s}‖/‖ψ_T‖². So §7 needs exactly sup_{a≥t_*}‖Qψ̂_a‖ < ∞ and Ω_g ∈ D(Q), at fixed g.
2. *One L²→L⁴ bound suffices* (Lemma L, §B). The printed source, read on the image, is in Simon's book. The theorem is printed as "THEOREM V.10" (p. 156, PDF 178); its statement (iii) reads "P(t) is bounded from L²(Q_F) to L^s(Q_F) so long as s < s(t) ≡ 1+e^{2mt}. For any such s and t there is an r so that ‖P(t)‖_{2,s} ≤ ‖F_{(0,t)}‖_r for all interaction polynomials and all g's". It is proved as item (iv) on p. 158. P(t) = exp(−tH(g)) is Theorem V.12(c), (V.43), p. 159. The standing hypotheses of §V.3 (p. 155) are g ∈ L^{1+ε}(ℝ) ∩ L¹(ℝ) and g ≥ 0. In the book's own cross-references this theorem is called "Theorem V.11 (iv)" (e.g. step 5 of the proof of Thm V.17, p. 167, PDF 189, read on the image); Proposition V.10 on p. 155 carries the same number. **No new import is needed**, though: the p. 158 proof is five lines from A2 and A4, i.e. the record's own pairing computation (Prop. 8.1 Step 1, eq:pairing, l. 1686) with exponent r = 11/10.
3. Rosen's higher-order estimates (Expositions Thm 3.1.3, p. 32, per `common:reference/glimm-jaffe-expositions`) are **not needed**. They would not give the n-growth of Lemma 7.6 either.
4. Ω_g ∈ L⁴(dφ_0) needs only Lemma L and A1. With it, Lemma 7.6 holds **for every s ≥ 0** (Gaussian exponential moments and Hölder). The radius 1/K' is an artefact of the GJS-norm route.
5. Proposition 7.5 needs only Ĉ_Q < ∞. The gap value is CE2's m_1 (Lemma 7.4). I grepped ll. 1623-2553: only γ = m_1 (via (G_γ), l. 1627) and M (Lemma 10.2) cross out of §§5 and 7. K', Ĉ_Q, 𝔫(Q) and C_8 outside M never appear in §§8-14.
6. "Theorem 7.8 conditional on CE2 only" should read: it rests on A1-A4 and A8(i)-(iv), (viii), all literal (but see G1).

**O2: modified.**
1. *What is consumed.* Lemma 10.2 (ll. 1992-2013) consumes: for g, g' ∈ 𝒢 with a common plateau, s ∈ [0,1], and h_j = η_j v ∈ C_c^∞ real with |h_j| ≤ 1 and supp h_j ⊂ [j−1, j+1], Ω_{g_s} ∈ D(V(h_j)) and ‖V(h_j)Ω_{g_s}‖ ≤ M. Lemmas 9.3 and 10.3 use it only through ‖XΩ‖ (the total variation 𝔪) and Cauchy-Schwarz. Theorem 12.2(5) states it for all of 𝒞_H and measurable h. Theorem 5.1 Step 6 needs the Euclidean bound only along T_k → ∞, so "sup_{T>0}" can become "T ≥ t_*".
2. *"Equivalently" is false.* The Euclidean bound implies the Hamiltonian one (Steps 5-6), but not conversely at finite T, since ψ̂_T ≠ Ω_g.
3. *Cell dependence (the role-card check).* The orchestrator's belief is **refuted for polynomial growth**. Suppose ‖V_jΩ_s‖ ≤ F(r_j) with F nondecreasing and polynomially bounded. Then Prop. 10.4 Steps 2-4 give Ψ(d) = 32 Σ_{n≥⌊d⌋} F(n+1)(‖W_γ‖_1 e^{−γn/4} + T_γ(n/2)), still O((1+d)^{−N}) for every N, because T_γ(r) ≤ C_{q,γ}(1+r)^{−q} for every q (Lemma 9.1(i)). Theorem 11.1 Step 1 then runs verbatim. Two things are fatal. The first is dependence on g not controlled by d(g,O), e.g. on |supp g|: the cutoffs g, g' ≽ g_0 have arbitrary tails (Thm 11.1 Step 1). The second is growth exponential in r_j, because T_γ is not exponentially small (§1.4, ll. 300-305).
4. The core is not irreducible: see O3.

**O3: refuted** (an estimate, `conjectured` until written and audited). The regress is real only if the reference cutoff differs from g near supp h. Take supp h ⊂ [c−1, c+1], N := (c−4, c+4), g_0 := g·1_N ∈ 𝒞_H, g_1 := g − g_0, and h_α := h_{T, g_0+αg_1} ∈ 𝒞_E^slab. The mechanism of GJS (1.1.12) (p. 595, read), re-proved like Prop. 8.1 Steps 2-3, gives

  ⟨Q_V⟩_{h_{T,g}} = ⟨Q_V⟩_{h_{T,g_0}} − ∫_0^1 dα Σ_Δ Σ_{n≥1} Cov_{h_α}(Q_V, U_{Δ,n}),  U_{Δ,n} := λ a_n ∫_Δ h_{T,g_1}(z) :Φ(z)^n: dz.

Here Δ runs over GJS squares, "the unit lattice square in R² centered at the lattice side [sic] j_i ∈ Z²" (p. 593). Each such Δ has spatial centre k with |k−c| > 7/2. The localization squares of Q_V lie in [−½, ½] × (c−2, c+2). An axis-parallel strip of width ≥ max(1+j, |l|−1) separates the two, where j is the spatial shell index and l the row of Δ. Theorem 1.1.7 ("constants … independent of h, Q_1 and Q_2", p. 594), applied at every h_α, bounds the far part by C_7 S_* u_* ‖Q_V‖_GJS, uniformly in T and g. The near part is ⟨Q_V⟩_{h_{T,g_0}} = ‖V(h)ψ̂_T(g_0)‖². By Lemma L(iii) it is bounded uniformly over all g_0 with supp g_0 ⊂ N̄: the "fixed-g bounds" of O3 become uniform over cutoffs of bounded support through the record's own Theorem C.5, and E(g_0) cancels exactly. This is GJS's own proof of (1.1.11) with Q = V(h)², h_1 = h_{T,g_0}, h_2 = h_{T,g}. Where GJS bound the reference term by Theorem 1.1.8, the record bounds it by Lemma L. If "two localized monomials" (p. 594) is read as sharp-time only, slice U_{Δ,n} = ∫dx⁰ U_{Δ,n}(x⁰) and apply CE2 to sharp-time pairs, the reading Lemma 7.4 already uses. The bound is unchanged.

**O4: confirmed, and moot.** Route M needs no re-sourcing. I did not read the Erice pages. Per brief §3 and `common:reference/glimm-jaffe-spencer-erice-1973`, (2.2.7) has another norm and no class of h, so it cannot replace a proof. It should not be a phase.

**O5: modified.** Neither Level 2 nor Level 3 is needed to remove U_GJS if Route M survives audit. Level 2 remains a fallback only, and an optional project for checking the printed proof of CE2 itself, which goes beyond the A1-A7 standard. Level 3 should never be used for this purpose.

## B. The statements to prove

Notation: t_* := 1/m_0. For a bounded open interval N, Z_N := sup{‖e^{−𝒰_h}‖_{L^{11}(dμ_0)} : h ∈ 𝒞_E, supp h ⊂ [0,t_*]×N̄} and A_N := e^{t_*λ|a_0||N|} Z_N.

**Lemma L** (new Lemma 4.5, at the end of §4, with unnumbered displays; nothing is renumbered).
- (i) For every g ∈ 𝒞_H, ‖e^{−t_*K(g)}‖_{L²(dφ_0)→L⁴(dφ_0)} ≤ ‖e^{−𝒰_{1_{[0,t_*]}⊗g}}‖_{L^{11}(dμ_0)}.
- (ii) Z_N < ∞, and Z_N depends on N only through |N|.
- (iii) Let g ∈ 𝒞_H with supp g ⊂ N̄. For every T ≥ t_* and every real time-zero F ∈ L⁴(dφ_0), ‖Fψ̂_T‖ ≤ A_N‖F‖_{L⁴(dφ_0)}. Moreover ‖Ω_g‖_{L⁴(dφ_0)} ≤ A_N.

*Proof sketch.*
- (i) For bounded f, h, A2 gives ⟨f, e^{−t_*K}h⟩ = ∫ \overline{J_{t_*}f} (J_0h) F dμ_0. Apply Hölder with exponents 11/10 and 11. Then ‖(J_{t_*}f)(J_0h)‖_{11/10}^{11/10} = ⟨|f|^{11/10}, 𝖯_{t_*}|h|^{11/10}⟩ ≤ ‖f‖_{4/3}^{11/10} ‖h‖_2^{11/10}, by Hölder (40/33, 40/7) and A4, because (40/7 − 1)/(20/11 − 1) = 121/21 < e² (exact). Conclude by duality and density.
- (ii) Theorem C.5 with p = 11 and Λ = [0,t_*]×N̄, together with translation invariance of μ_0.
- (iii) Put φ := ψ_{T−t_*}. Then ‖Fψ_T‖ ≤ ‖F‖_4 e^{t_*E}‖e^{−t_*K}φ‖_4 ≤ ‖F‖_4 e^{t_*E} Z_N ‖φ‖. Jensen for the spectral measure of φ̂ gives ‖ψ_T‖ ≥ ‖φ‖ e^{−t_*⟨φ̂,Hφ̂⟩}. Chebyshev's association inequality gives ⟨ψ̂_s, Hψ̂_s⟩ ≤ ⟨Ω_0, HΩ_0⟩ = λa_0∫g − E(g), using Ω_0 ∈ D(H_0) ∩ D(V(g)). Here E(g) cancels. For Ω_g, use Lemma 4.4 and Fatou.
- A numerical test of the Jensen-Chebyshev step gave min LHS/RHS = 1.0000005 over 2000 random H ≥ 0 (`numerical`; `<scratch>/mp/check.py`, Python 3.14, numpy 2.5.2, seed 12345).

**Phase 1 (§7 at fixed g).** Let N_g be a bounded open interval containing supp g.
- **Lemma 7.1′.** For every g ∈ 𝒞_H, every cylinder monomial Q and every T ≥ t_*: ‖Qψ̂_T‖ ≤ A_{N_g}‖Q‖_{L⁴(dφ_0)}, Ω_g ∈ D(Q), and ‖QΩ_g‖ ≤ A_{N_g}‖Q‖_4.
- **Lemmas 7.2, 7.3:** statements unchanged. Their proofs use T ≥ |s|+t_* and T ≥ t/2+t_*.
- **Lemma 7.6′.** For every s ≥ 0, E_{μ_g} e^{s|X_f|} ≤ √2 exp(s²⟨f, Cf⟩) A_{N_g}².
- **Proposition 7.5 and Theorems 7.7, 7.8:** statements unchanged. The proof of Lemma 4.3(ii) cites Lemma 7.1′ in place of (U_GJS).
- *Status change.* Lemma 4.3, Lemmas 7.1-7.3 and 7.6, Prop. 7.5 and Thms 7.7-7.8 go from "proved, conditional on U_GJS" to **proved**, on the literal imports A1-A4 and A8(i)-(iv), (viii). Theorem 12.2 stays "proved, conditional on U_GJS", now through its moment clause only.

**Phase 2: Theorem 5.1′.** Let 0 ≤ λ/m_0² < ε_𝒫. For every g ∈ 𝒞_H, every c ∈ ℝ, every real measurable h with ‖h‖_∞ ≤ 1 and supp h ⊂ [c−1, c+1], and every T ≥ t_*:

  ∫V(h)² dq_{h_{T,g}} ≤ M_♯²; hence Ω_g ∈ D(V(h)) and ‖V(h)Ω_g‖ ≤ M_♯, with
  M_♯² := 9^{p'} A_8² v_2² + 9 C_7 S_* u_* 𝔎(p') λ² (Σ_n|a_n|)².

The constants are:
- A_8 := A_{(−4,4)};
- v_2² := λ² Σ_{n=0}^{2p'} a_n² n! ∫_{−1}^{1}∫_{−1}^{1} C(x−y)^n dx dy, where C > 0 is the kernel of (2μ)^{−1}, and 9^{p'} is Nelson's comparison (q−1)^{p'} at q = 4, as in the proof of Theorem C.5;
- u_* := λ Σ_{n=1}^{2p'} |a_n| K_1 K_2^{2n} n!, the norm (1.1.7) of one square's interaction piece;
- S_* := 2 Σ_{j≥0} Σ_{l∈ℤ} e^{−m_1 max(1+j, |l|−1)} < ∞.

M_♯ depends on (λ, 𝒫, m_0) through the printed C_7, m_1, K_1, K_2 and through the finite, unevaluated constant Z_{(−4,4)} of Theorem C.5. It is uniform in g, c, h and T. Steps 1-4 and 6 of Theorem 5.1 are kept; Step 5 becomes the decomposition of O3.

*Status after Phase 2.* The following become **proved**, on the literal imports A1-A7 and A8(i)-(iv), (viii): Thm 5.1, Cor. 5.2 (with its constant recomputed), Lemmas 10.2-10.3, Prop. 10.4, Lemma 10.5, Thm 11.1, Prop. 11.2, Thm 12.2, Cor. 12.3, Thm 13.2 (still conditional on its stated Hypothesis 13.1) and Rem. 13.3. A8(v)-(vii′), Prop. C.1 and Prop. C.7 as stated are then no longer consumed.

**Appendix A.**
- *After Phase 1:* add rows for t_*, the exponent 11, Z_N and A_N (Lemma 4.5) and for the bound of Lemma 7.1′; delete the K′ row; Lemma 7.6 gets prefactor √2 e^{s²⟨f,Cf⟩}A_{N_g}² and radius ∞; the Ĉ_Q row is unchanged.
- *After Phase 2:* replace the two M² rows by M_♯², with new rows for v_2, u_*, S_* and A_8; drop C_8 from the first row; 𝔎(p′) stays.

## C. Routes

**Route M (recommended): CE2 comparison plus a local hypercontractive bound.**
- *Base:* GJS Thm 1.1.7 (p. 594) and the mechanism of (1.1.12) (p. 595), both read on the images; A2 and A4; the record's Thm C.5, Lemma 4.4, Thm 5.1 Steps 1-4 and 6, Prop. 6.2 and Lemma 7.4.
- *Steps:*
  1. Lemma L.
  2. The §7 replacements.
  3. Differentiability of α ↦ ⟨Q_V⟩_{h_α}, with derivative −Cov, under the Hölder interpolation (eq:wsbound) pattern.
  4. Lattice bookkeeping and the CE2 sum S_*.
  5. Theorem 5.1′.
  6. Constants.
- *Deliverable:* a standalone note `ugjs/route-m.tex`, audited first and then integrated. Lemma L becomes Lemma 4.5; the proofs of 5.1, 7.1-7.3 and 7.6 are replaced in place; the statements of 7.1 and 7.6 change. The numbered statements go from 61 to 62, with every existing number kept; regenerate `labels.md`.
- *Estimate:* 4.5-6 pages of finished proof plus 1-2 pages of edits (mostly deletions in A8, the Scope paragraph and App. C), and 2 verification rounds.
- *Imports:* only literal ones, on disk and read (§E).
- *Risk:* the step most likely to fail is the bookkeeping of step 3 (routine, following the Prop. 8.1 pattern). The exposed point is that **Theorem C.5 becomes load-bearing**. If its audit fails, Phase 2 stalls: U_GJS is then kept, restricted to Theorem 5.1 (the O2 state), and Phase 1 survives, since at fixed g A3 suffices.

**Route O+L2 (fallback).** Phase 1 is as above, and U^{M2} comes from the Level-2 trace (cqft's map). Use it only if Route M's Phase 2 is refuted for a reason other than CE2's statement; a CE2 failure would break Lemma 7.4 as well.

## D. Recommendation

- **Phase 0, before the plan is fixed.** Hand O3's refutation to cqft and to one independent auditor.
  - *Gate Γ0:* a written proof of Lemma L and Theorem 5.1′ (≤ 5 pp). Every step is classified per AGENTS 3.1, with the hypotheses of A2, A4, C.5 and Thm 1.1.7 checked in writing at each use. Two audits with zero open findings.
  - *Fallback:* the orchestrator's plan (Route O+L2).
- **Phase 1 (Lemma L and §7), written jointly with Phase 2 but gated separately.**
  - *Gate Γ1:* a G1/G3a-style step map for every new or changed proof, constants recomputed by hand, zero open audit findings.
  - *Fallback:* none needed; Phase 1 uses no uniformity in g.
- **Phase 2 (Theorem 5.1′).**
  - *Gate Γ2:* Γ1, plus an independent audit of Theorem C.5, plus a human reading of GJS pp. 593-594 recorded as new C5 items 10-11. Item 10: the square convention and (1.1.6). Item 11: the class of pairs in Theorem 1.1.7.
  - *Fallback:* keep U_GJS for Theorem 5.1 only.
- **Phase 3 (integration).**
  - *Gate:* G0, G4, G5 and G6 re-run on `main.tex`. The `.aux` diff shows all 125 labels keeping their numbers, plus the one new label.
- **Never:** Level 3 for this purpose; Erice re-sourcing presented as a "removal".
- **Optional, as a separate project:** a Level-2 check of the printed proof of Thm 1.1.7.

## E. Imports and sources (Route M)

| item | status | used for |
|---|---|---|
| A1 (GJS p. 588; GJ II; GJ71; Rosen70) | literal | Ω_g, e.s.a., Ω_0 ∈ D(K(g)) |
| A2 (Simon III.6, V.14, V.15) | literal | slab FKN, free Markov identity |
| A3 (Simon V.7) | literal | finiteness at fixed g |
| A4 (Simon I.17, III.17) | literal | Lemma L(i); Nelson comparison |
| A8(i)-(iv) (GJS pp. 589, 593-594, read) | literal | measures; class, to be **widened to (1.1.6)** or handled by slicing; norms (1.1.7)-(1.1.9); CE2 |
| A8(viii) (p. 590) | literal | scaling (Prop. 3.2) |
| Lemma C.2, Lemmas C.3-C.4, Thm C.5; Lemmas 4.1-4.4; Prop. 6.2; Lemma 7.4 | record's own, proved | load-bearing |
| Gaussian moments, Wick orthogonality, positivity and local integrability of C^n | elementary | to be written out, ≈ 0.25 p |
| *Optional:* Simon Thm V.10 (p. 156) (iii)/(iv) and V.12(c) (p. 159) | on disk, read | a literal alternative to proving L(i) in-house |

New assumption items: none if L(i) is proved in-house; otherwise one new literal item. A8(v)-(vii′) become unused. A human must still read GJS pp. 593-594 (the new C5 items), and Simon pp. 155-159 if Simon is cited.

## F. Findings

1. **MINOR. main.tex l. 1349** (proof of Lemma 7.1, PDF p. 18): `\|Q\widehat\psi_{T_\alpha}\|le` renders as "‖Qψ̂Tα‖leC8^{1/2}𝔫(Q)", so the relation ≤ is lost. Repair: `\le`.
2. **MINOR. ll. 438, 1188, 1261.** These lines use cells [j, j+1). GJS's localization squares are centred at lattice sites (p. 593; "lattice side" is a typo in the source). Every count used (≤ 3 cells, N_I ≤ ⌊L⌋+2) is invariant under a half-unit shift of the lattice, so no constant changes. Repair: one sentence.
3. **MINOR. ll. 291-292** (§1.4): "proved from the factorial moments of Source Fact 2.3". The moments come from Lemma 7.1, that is, from (U_GJS). Source Fact 2.3 says only "uniformly as h → 1", which does not cover h_{T,g}. Repair: cite Lemma 7.6 and (U_GJS).
4. **MINOR. l. 553** (A4 Scope, "Thms V.10, V.12"). Simon prints both Proposition V.10 (p. 155) and Theorem V.10 (p. 156), and cites the latter as V.11. Repair: "Theorem V.10, p. 156".
5. **MINOR. `docs/imports.md` l. 56:** "The only proportionate route … is a display-by-display trace" is an unsupported negative claim, and Route M is a counter-candidate. The same claim appears in KB `level2-h-trace` and in the Consequence paragraph of `hamiltonian-bypass-dead`. Repair: "One route".

## G. Traps

1. **"Theorem 12.2 no longer depends on the h-uniformity of the GJS expansion."** Say instead: "Theorem 12.2 no longer imports U_GJS. It imports GJS Thm 1.1.7 literally, at its printed scope, whose printed proof obtains h-independence from Thm 1.1.8 at the same h (pp. 596-597); the record does not re-verify it, as for A1-A7."
2. **"U^{M2} ⇔ (M_2)".** Say instead: "the slab bound for T ≥ t_* implies (M_2)".
3. **"sup_{T>0}, one constant for all g" for Lemma 7.1′.** Say instead: "T ≥ t_*, constant A_{N_g}, depending on |supp g|".
4. **"M depends only on (λ, 𝒫, m_0)"** without the rider. Add "through C_7, m_1, K_1, K_2 and the unevaluated constant of Theorem C.5"; no numerical value of M exists.
5. **"Simon Theorem V.11."** Cite "Theorem V.10, p. 156, statement (iii); proof item (iv), p. 158", and record the source's discrepancy: statement ‖F_{(0,t)}‖_r, proof ‖F(0,t)‖_{r′}.
6. **"Lemma 10.2 needs g-uniformity or the net is not Cauchy."** Say instead: "for each cell distance, a bound uniform over the net's cutoffs; polynomial growth in r_j suffices, dependence on |supp g| does not".
7. **"The 1970-71 open problem (Expositions p. 57) is solved."** No: (M_2) is weaker than a g-uniform N^loc ≤ c(H(g)+I), and Route M is Euclidean and uses CE2.
8. **"Appendix C is supporting evidence."** After Phase 2, Theorem C.5 is load-bearing; its Used-in line and the Scope text must say so.
9. **"Phase 2 removes the weak-coupling restriction."** No: Lemma L holds for every λ ≥ 0, but Thm 5.1′ and Thm 7.8 need CE2.
10. **"A Level-2 trace would make Theorem 12.2 unconditional."** After Route M it is already proved at the import standard; Level 2 would verify an import's printed proof instead.
11. **"Lemma 7.6's radius 1/K′ is intrinsic."** It is an artefact of the GJS-norm route; after Phase 1 the moments are finite for every s.
