# V6 repairs check: independent re-check of the edits to `part_i/main.tex` (23 November 2026)

Auditor "repairs-check" of the working council of 23 November 2026. I was read-only on the
repository and wrote none of the text checked.

- Object: `part_i/main.tex` of the working tree, sha256
  `3da0640725bcf851c2d8acd37dec515adbb2cbfb5c732f151a91e92c5d74bbf7`, 8858 lines. It was
  unchanged from the start of this check to its end (hash, line count and modification time
  compared at both points).
- Reference: public HEAD 49f2d23, 8744 lines.
- Diff checked: the council's `repairs-main.diff` (584 lines, 38 hunks). It is byte-identical to
  `git diff -- part_i/main.tex` and contains both of the editor's passes (`wording-main.md`,
  `repairs-main.md`). The instructions behind pass 2 are the council's `PASS2.md`; the findings
  it repairs are in `ugjs/council/v6-chain-audit.md` (F-A to F-K) and
  `ugjs/council/v6-appendix-e-audit.md` (F1 to F3, O4).
- Conventions: "FROZEN l." is a line of 49f2d23, "new l." a line of the checked file. Numbers
  and pages come from the two `main.aux` files; a page is the new page unless stated otherwise.

## 1. Outcome

All 38 hunks hold. Each amended statement follows from its proof, each new quotation is what the
cited page prints, and no edit breaks the text around it. I found no CRITICAL or MAJOR point,
four MINOR findings (F1 to F4, on wording and sourcing) and nine observations. The build is
clean: 127 pages, byte-identical to `part_i/main.pdf`, no label renumbered, and exactly the
thirteen reported statement environments changed.

## 2. Claims, with status words and locators

| # | claim | status | locator |
|---|---|---|---|
| C1 | Corollary 12.3 as restricted (𝒫(ξ) = ξ⁴; the cutoff of [GJ3, (2.3)] chosen in G) follows from its proof. Every hypothesis of Theorem 12.2(1) is met. Each τ_{−εnu}g_n lies in G. For O ⊆ [−R, R] and \|u\| ≤ 1, d(τ_{−εnu}g_n, O) ≥ 2n − R, and d(g, O) ≥ d implies g ≡ 1 on O_d. So the rate gives Ψ_{m_1}(2n − R) → 0 for the averaged states, and Ψ_{m_1}(3n − R) → 0 for the unaveraged g_n. The weak-coupling hypothesis is standing (§2.6, "Throughout, 0 ≤ λ/m_0² < ε_𝒫"). | proved, conditional on Theorem 12.2(1), (T) of Lemma 2.8 and Proposition E.5(T), and on two identifications with GJ3: its ground states are the Ω_{g_n} (the A1-Scope reading, named after the corollary), and its σ_α is τ_α (F3) | `cor:canonical` 12.3, p. 43; new ll. 3172–3219 |
| C2 | GJ3 p. 205 prints "(1.10) H(g) = H_0 + λ∫:φ⁴(x): g(x)dx − E_g = H_0 + H_{I,g} − E_g". It also prints "the spatial cutoff g(x) is a smooth, positive function that equals one on some bounded set and that vanishes off some larger bounded set". | verified | GJ3 copy in `refs/` (Acta Math. 125, 65 PDF pages), PDF page 3, rendered at 150 dpi |
| C3 | GJ3 p. 210 prints "we take g(x) to be a nonnegative C_0^∞ function equal to one on the interval [−3, 3]", (2.3) g_n(x) = g(x/n), and (2.4) ω_n(A) = (1/n)∫(Ω_{g_n}, σ_α(A)Ω_{g_n})h(α/n)dα. It also prints "where σ_α is the space translation automorphism (see II, sections 3.6 and 4)", "The function h(·) ≥ 0 is C^∞, has support in [−1, 1]", and (2.5). There is no bound g ≤ 1. | verified | `audit_2026/evidence/gjiii-08.png` (= GJ3 PDF page 8, also rendered) |
| C4 | GJ2 p. 400 prints "σ_a(A) = U(−α)e^{itH(g)}Ae^{−itH(g)}U(+α)" for a space-time translation (α, t) = a. With Lemma E.7(a)(4), 𝔇U(−a)𝔇⁻¹ = U_a, this gives σ_α = τ_α at t = 0, that is ε = +1, which lies inside the proof's ε ∈ {±1}. | verified (quotation); consequence proved, conditional on GJ3 using GJ2's objects | `audit_2026/evidence/gj2-local-algebra-40.png`; `lem:ff-sources` E.7, p. 124 |
| C5 | A cutoff admitted by GJ3 lies in G exactly when g ≤ 1. G is {g ∈ C_c^∞(ℝ): 0 ≤ g ≤ 1, g ≡ 1 on a nonempty open interval}, and g ≡ 1 on [−3, 3] supplies the interval. | proved | `def:classes` 2.1, p. 10 |
| C6 | a ↦ U_a is a strongly continuous one-parameter unitary group. The proof's cited items give exactly what is used: E.1(ii) gives j^C τ_a^C = e^{−ia·} j^C, with j^C unitary by E.1(i), and multiplication by e^{−iak} is strongly continuous by dominated convergence (dominant 4\|θ\|²). E.2(iv) is stated for "a strongly continuous one-parameter unitary group on 𝔥". U_a = DΓ(τ_a^C)D⁻¹ is E.4's definition U_T = D_2Γ(T^C)D_1⁻¹ with D_1 = D_2 = D, and conjugation by the fixed unitary D keeps strong continuity. | proved | `prop:ff-symmetries` E.5, p. 121; new ll. 8462–8463, 8508–8512 |
| C7 | In the proof of Corollary 12.3, b ↦ ω_{g_n}(τ_bA) = ⟨U_{−b}Ω_{g_n}, AU_{−b}Ω_{g_n}⟩ is continuous. By (T), ω_{τ_a g} = ω_g∘τ_{−a}, so the norm integrand is sup_A \|ω_{g_n}(τ_{εnu}A) − ω_∞(A)\| over the unit ball of 𝔄(O). A supremum of continuous functions is lower semicontinuous, hence Borel. | proved | new ll. 3203–3205, 3213–3218 |
| C8 | Theorem 13.2 holds as stated with Hypothesis 13.1 amended; I re-derived Steps 1 to 4. (B2) is used nowhere. Step 3 applies (B4) to ω_∞, a ground state in the spectral sense by Theorem 12.2(3), and θ-invariant by 12.2(4). O is a bounded open interval, since 𝔄(O) is defined only for those, and it is nonempty, since 𝔄(∅) = ℂ1 would force ω_+(B) = ω_−(B). R_a = max(0, \|a\| − \|O\|), so every a with \|a\| ≥ \|O\| + 1/m_1 has R_a ≥ 1/m_1 > 0, and such a exist because m_1 > 0. The bound of Step 2 then holds for all large \|a\|, as the limit \|a\| → ∞ requires. | proved, conditional on Theorem 12.2(1), (3), (4), Theorem 7.8, Lemma 9.3, A6(iii) and E.5(T) | `thm:dichotomy` 13.2, p. 44; new ll. 3253–3322 |
| C9 | The amended hypotheses of Proposition 12.1 (ω a state on 𝔄; bounded open intervals) and of Lemma 9.3 (bounded open interval) are met at every use. In Theorem 12.2(3), ω_∞ is "a state on 𝔄" by the statement of 12.2. In Lemma 10.3, β_t(A) ∈ 𝔄(O_{\|t\|}), an open interval. In Theorem 13.2 Step 1, τ_a(B) ∈ 𝔄(O + a). | verified (each use read) | `prop:spectral` 12.1, p. 41; `lem:cluster` 9.3, p. 38; new ll. 3152–3156, 2847, 3271–3279 |
| C10 | At λ = 0, V_* = 0 and both terms of M² vanish, so M = 0 and Ψ_{m_1}(d) = 0 for d ≥ d_0. For λ > 0, V_* ≥ λ²a_{2p′}²(2p′)! I_{2p′} > 0 and S_2 ≥ 1, so M > 0. Ψ_{m_1}(d) ≥ 32M·T_γ(⌊d⌋/2), and an exponentially small T_γ would make Ŵ_γ analytic in a strip, which the argument of §1.4 excludes. So for λ > 0, Ψ_{m_1} is not O(e^{−cd}) for any c > 0. | proved | `thm:M2` 5.1, new ll. 1897–1900; `aux:notation-wick` N.20(iv); `aux:notation-S2` N.15(i); `eq:Psidef` (`lem:rate` 10.5); §1.4, new ll. 407–414 |
| C11 | V_* = V̄_* = λ²Σ_n a_n² n! I_n. The function h′ = 1_{[a,a+2]} is admissible in N.20, and N.20(iv)'s displayed identity is an equality for it. | proved here; not stated in the record (F1) | `aux:notation-wick` N.20, p. 73 |
| C12 | `m2/m2.tex` treats 𝒫(ξ) = ξ² with (λ/2)∫g:φ_0²: and m_1² := m_0² + λ (l. 67), the mass of that model (Lemma `lem:freeeq`). Proposition `prop:rate` (l. 172) has a "Proof sketch" (l. 185), and "Moreover the exponent is sharp" (l. 179) is asserted, not proved. The numerics give k = 4.03 ± 0.05, with the prefactor powers "not sharply confirmed" (ll. 237–240). | verified (file read) | `m2/m2.tex` ll. 61–68, 86–99, 172–197, 237–241 |
| C13 | `part_ii/v3_continuum_package.tex` imports (d) "Part I Appendix C: the Γ(e^{−τ}) sum-of-chaoses moment comparison and the layer-cake assembly (proof of thm:stability)". No proof in `part_i/main.tex` cites `part_ii/`. | verified | ll. 231–233 of that file; grep of `part_i/main.tex` |
| C14 | GJS p. 588 prints "Fock space 𝓕 = L_2(S′(R¹), dφ) is defined by the Gaussian measure dφ with mean zero and covariance μ⁻¹ = (−d²/dx_1² + m_0²)^{−1/2}, see [1]. Also : : denotes Wick ordering with respect to dφ". GJS p. 589 prints "Φ(0, x⃗) = φ_0(x⃗)" and "dΦ is the Gaussian measure with mean zero and covariance (−Δ + m_0²)⁻¹". With C = (2μ)⁻¹ one has μ⁻¹ = 2C, and the sharp-time covariance ∫dk_0(2π)⁻¹(k_0² + μ²)⁻¹ = (2μ)⁻¹ = C. GJS's [1] is not in the record's bibliography (19 entries; Dimock appears only at new l. 3758). | verified (quotations); proved (calculations) | `audit_2026/evidence/gjs-source-05.png`, `gjs-p589-06.png`; `rem:conv` 2.5, p. 22 |
| C15 | GJ71 p. 255 prints "In the representation of Fock space for which the operators H_I(κ) are all diagonal, exp(−tH_{0,V}) is an integral operator with a positive kernel". Rosen70 p. 158 prints "The boson Fock space 𝓕 is the direct sum 𝓕 = Σ⊕𝓕^n". | verified | `refs/`: GJ71 PDF page 3, Rosen70 PDF page 2, both rendered |
| C16 | Simon p. 158 prints Theorem V.12(a) as A5 quotes it. p. 146 prints (V.15) "H(g) = H_0 + H_I(g)" with "Define H_I(g) = ∫ g(x) :P(φ_F(x)): dx", and asks for essential self-adjointness "on D(H_0) ∩ D(H_I)". p. 141 prints "Henceforth the symbol P will denote a semibounded polynomial". p. 140 prints "We will call P semibounded if and only if inf_{x∈R} P(x) > −∞ i.e., if and only if P(X) = a_{2n}X^{2n}+…+a_0 with a_{2n} > 0". | verified | `simon-transfer-180.png`, `simon-hg-168.png`, `simon-semibounded-163.png`; Simon PDF page 162 rendered |
| C17 | A5(ii) follows from Theorem V.12(a) applied at each g_s. First, 0 ≤ g_s ∈ C_c^∞ ⊂ L¹ ∩ L^{1+ε}. The closure of H(g_s)↾C^∞(H_0) is self-adjoint and contained in the self-adjoint K(g_s), hence equal to it. Taking s = 0 and s = 1 gives ξ ∈ D(V(g)) ∩ D(V(g′)), so ξ ∈ D(V(g′ − g)), and the identity follows by linearity. | proved, conditional on the φ_F reading of A1's Scope and on "essentially self-adjoint on C^∞(H_0)" in its usual sense, which includes C^∞(H_0) ⊆ D(H(g)); for λ = 0 see O2 | `A:domain` A5, p. 15; new ll. 1020–1031 |
| C18 | Simon p. 31 prints "Let D_n(A) ⊂ Γ_n(H) be D(A)⊗…⊗D(A) (incomplete tensor product) and D(dΓ(A)) = +_{n=0}^∞ D_n(A) (incomplete direct sum)". Under the reading now declared in E.7(b), D⁻¹H_0D ⊇ dΓ(μ). This uses D(μ) ⊆ D(μ^C), the linearity of D⁻¹H_0D, and the fact that the operator of (I.40) commutes with S_n. | verified (quotation); proved (inclusion) | `simon-dgamma-053.png`; `lem:ff-sources` E.7(b), new ll. 8759–8762 |
| C19 | GJS p. 595 prints Theorem 1.1.8 "uniformly as h → 1". p. 597 prints "the proof follows from Theorem 1.1.8, (1.1.16) and the above determination of Q". p. 629 prints "The estimates of Theorems 1.1.8, 1.1.11, 3.1 and 4.1 are uniform in the space cutoff h" (= Source Fact 2.4). Remark N.39 says the parallel pairs with a time-integrated partner are reached by the printed proof "only after slicing", and it leaves open whether the printed proof reaches them. | verified | `gjs-theorems-12.png`, `gjs-proof-14.png`, `gjs-uniform-46.png`; `sf:printed` 2.4, p. 20; `aux:d3-orient` N.39, p. 98 |
| C20 | GJS p. 594 prints "Let m_0, K_2 and K_1 be sufficiently large and let λ be sufficiently small. There are constants 0 < m_1 and O(1) independent of h, Q_1 and Q_2 such that". | verified | `gjs-theorems-11.png` |
| C21 | `audit_2026/evidence/` holds 97 images. 54 of them are named in `audit_2026/citation_screenshot_dossier.tex`, which was last modified on 22 September 2026. | verified (script) | — |
| C22 | [MMST]: the title, the four authors and arXiv:2010.11121 match the copy in `refs/part_ii/` (v2, 26 Oct 2021). The entry now gives "Comm. Math. Phys. 387 (2021) 299--360; arXiv:2010.11121", as the orchestrator verified. | verified (title, authors, identifier); journal data not verified by me | new ll. 8848–8850 |
| C23 | In Theorems 12.2 and D.4, and in Remark N.46, the only change is the attribution "of Definition N.14, finite by Theorem C.5". Items (1) to (5) of 12.2 and the bound of D.4 are unchanged word for word. | verified (word diff) | `thm:MAIN` 12.2, p. 42; `thm:D4` D.4, p. 101; `aux:d4-not` N.46, p. 104 |

## 3. Every hunk of the diff

| # | locus (FROZEN l. → new l.; label, number, page) | what changed | verdict |
|---|---|---|---|
| 1 | `\date` and its comment, ll. 76–81 → 76–82 | `\date{23 November 2026}`; the comment names the corrections of 23 November; epoch 1795392000 | holds: the epoch is 2026-11-23 00:00 UTC, and the PDF built with it is byte-identical |
| 2 | title-page notice, new ll. 159–178 (p. 2) | new paragraph "Audit of 23 November 2026; corrections." | holds; see O3, O4. Its sentence on the re-check is discussed in §5 and in the final line |
| 3 | abstract, ll. 174–175 → 195–196 (p. 2) | the rate is "explicit in the imported theorem's unevaluated constants and one stability constant" | holds as mathematics; gap, MINOR (F1) |
| 4 | abstract, ll. 188–189 → 209–211 | "Wick powers and the free field" added to the list of imports | holds: these are A1(a)–(d) and A1(e)–(g) |
| 5 | §1.2, l. 236 → 258 | "explicit in unevaluated constants (Appendix A)" | holds |
| 6 | §1.3 (b), (c), ll. 317–323 → 339–347 | m2/ "gives, with a proof sketch and numerics", poly(d)e^{−2md}, m the mass of that model; Ψ_{m_1} "for λ > 0, not exponential" (§1.4); "a cutoff-uniform gap together with the uniform local moment" | holds (C10, C12) |
| 7 | §1.4, ll. 340–341 → 364–365 | the summary of the corollary restricted to "a cutoff 0 ≤ g ≤ 1" | holds |
| 8 | §1.4 "Boundaries", ll. 419–423 → 443–448 | m2/ wording; "a cutoff-uniform gap together with the uniform local moment" | holds; this is the chain audit's locus "§1.4, ll. 422–424" |
| 9 | §1 provenance paragraph, ll. 446–447 → 470–472 | the corollary also quotes [GJ3, (1.10)] | holds |
| 10 | §2.4, l. 633 → 658 | "partly indexed in" | holds (C21) |
| 11 | A1 Scope (`A:cutoff` A1, p. 11; text on p. 13), ll. 797–801 → 822–834 | GJS works in Q-space; μ⁻¹ is read as 2⟨f, Cg⟩, a declared reading; GJ2, GJ71 and Rosen70 work in Fock space; the dictionary 𝔇 is claimed for GJ2 only, and for GJ71 and Rosen70 it is a reading | holds (C14, C15); see O1 |
| 12 | A5 (`A:domain` A5, p. 15; text on p. 16), ll. 987–997 → 1020–1037 | Theorem V.12(a) quoted with (V.15) and "semibounded"; the Scope derives the common core C^∞(H_0); the Dossier line names two more images | holds (C16, C17); see O2, O8 |
| 13 | A8 Scope (`A:gjs` A8, p. 17; text on p. 21), ll. 1346–1350 → 1386–1392 | "only" removed and p. 629 added; "A stricter standard … is not adopted: it would exclude A8(iv)-T (point (b)), and Theorems D.3, D.4 would need the slicing of Remark N.39" | holds (C19). Consistent with Scope (b), whose transverse case would be excluded; with Remark N.39 and §D.e.4, whose class (P) "reaches after slicing"; and with Scope (c) |
| 14 | Lemma 9.1 (`lem:filter` 9.1, p. 36), ll. 2551–2552 → 2593–2596 | χ is fixed once for each γ; the objects that depend on it are listed | holds. Remark 3.3 uses Ψ at the single gap m_{1,*} and says the original-coordinate rate "is not the function Ψ_γ formed with the gap γ = s m_{1,*}", so no compatibility between γ's is needed |
| 15 | Lemma 9.3 (`lem:cluster` 9.3, p. 38), l. 2677 → 2721 | "bounded open interval" | holds; its uses match (C9) |
| 16 | Proposition 12.1 (`prop:spectral` 12.1, p. 41), ll. 2994–2995 → 3038–3040 | "open"; "ω is a state on 𝔄" | holds (C9) |
| 17 | proof of Proposition 12.1, l. 3007 → 3052 | "open" | holds |
| 18 | Theorem 12.2 (`thm:MAIN` 12.2, p. 42), l. 3099 → 3144–3145 | "S_2(B_{3×5}) of Definition N.14, finite by Theorem C.5" | holds; an attribution only (C23) |
| 19 | Corollary 12.3 (`cor:canonical` 12.3, p. 43), ll. 3126–3131 → 3172–3186 | statement restricted to 𝒫(ξ) = ξ⁴ and g ∈ G; the sentence after it quotes [GJ3, (1.10)] and names the A1 reading | holds (C1–C5); gap, MINOR (F3) |
| 20 | proof of Corollary 12.3, l. 3149 → 3203–3205 | the integrands are continuous, by the strong continuity of U | holds (C7); gap, MINOR (F2) |
| 21 | proof of Corollary 12.3, ll. 3157–3159 → 3213–3218; §13 introduction (`sec:dichotomy` 13, p. 44), ll. 3165–3169 → 3224–3230 | the norm integrand is measurable; §13 now says "together with the uniform local moment … through Theorem 12.2", "its proof uses (B1), (B3) and (B4)", and that (B2) "is not used" | holds (C7, C8) |
| 22 | Hypothesis 13.1 (`hyp:broken` 13.1, p. 44), after l. 3186 → 3249–3250 | "In (B1) and (B4), 'ground state' is meant in the spectral sense of Proposition 12.1." | holds (C8) |
| 23 | proof of Theorem 13.2, ll. 3201–3204 → 3264–3269 | "In Steps 1 and 2, a ∈ ℝ is any number with …"; every a with \|a\| ≥ \|O\| + 1/m_1 qualifies | holds (C8) |
| 24 | Remark 13.3 (`rem:gjs7576` 13.3, p. 45), l. 3269 → 3333 | "and the uniform local moment" | holds |
| 25 | §14 "Sharpness", ll. 3288–3293 → 3352–3358; §14 "Uniqueness", ll. 3295–3296 → 3360–3362 (p. 45) | the m2/ rate; "for λ > 0, not exponential"; "does not obtain an exponential rate"; the corollary summary restricted | holds, except the sentence of F4 (gap, MINOR) |
| 26 | §14 "Beyond weak coupling", l. 3305 → 3371; §14 "Part II", ll. 3311–3312 → 3377–3379 | "and a uniform local moment"; "Part I does not depend on Part II, and Part II re-uses one argument of Appendix C" | holds (C13). §14's "which remains open" (chain F-H) is unchanged, by the orchestrator's decision |
| 27 | Appendix A paragraph (`app:constants` A, p. 46; text on p. 47), ll. 3378–3380 → 3445–3452 | S_2 belongs to Definition N.14 and is bounded through Theorem C.5; the first two rows are unevaluated (p. 594); the rest is "explicit in these, in V_* (explicitly bounded, Lemma N.20) and, for Ψ_γ, in the filter of Lemma 9.1" | holds (C20); checked row by row against the table, new ll. 3418–3440 |
| 28 | Appendix B table, l. 3398 → 3470 | "(the .tex index covers only part of them)" | holds (C21) |
| 29 | Appendix B free-field entry, ll. 3506–3507 → 3578–3580 | the dilation unitary is excepted from the objects identified with the sources | holds; see O6 |
| 30 | Appendix B, new entry, new ll. 3593–3621 (p. 50) | corrections history, items (i) to (vii) | holds. Every hunk of this diff falls under one of its items, the provenance paragraph under (i) |
| 31 | Appendix D introduction, ll. 4163–4164 → 4265–4267 | the attribution of S_2(B) | holds |
| 32 | Theorem D.4 (`thm:D4` D.4, p. 101), ll. 7024–7025 → 7127–7129 | the attribution of S_2(B_{3×5}) | holds; an attribution only (C23) |
| 33 | Remark N.46 (`aux:d4-not`, p. 104), l. 7199 → 7303–7305 | the attribution of S_2(B_{3×5}) | holds |
| 34 | §D.f.1 (`sec:quant-fixed`, p. 105), ll. 7391–7392 → 7497–7499 | the attribution of S_2(B_{3×5}) | holds |
| 35 | Proposition E.5(T) (`prop:ff-symmetries` E.5, p. 121), l. 8356 → 8462–8463 | "a ↦ U_a is a strongly continuous one-parameter unitary group" | holds (C6) |
| 36 | proof of E.5(T), after l. 8401 → 8508–8512 | the one-line proof | holds (C6) |
| 37 | proof of Lemma E.7(b) (`lem:ff-sources` E.7, p. 124), before l. 8648 → 8759–8762 | the declared reading of the domain in (I.40) | holds (C18) |
| 38 | `\bibitem{MMST}`, ll. 8734–8736 → 8848–8850 | pages 299–360; arXiv:2010.11121 added | holds (C22) |

## 4. Findings

**F1 (MINOR). The two short descriptions of the rate's constants omit V_* and the filter, and
calling V_* explicit rests on an equality that the record does not state.**

- *Locator:* abstract, new ll. 195–196 (p. 2); title-page notice, new ll. 171–174 (p. 2).
- *Text:* abstract, "with a super-polynomial rate in $\dist(O,\{g<1\})$, explicit in the imported
  theorem's unevaluated constants and one stability constant"; notice, "the rate and $M$ are
  explicit in $S_2$ and the unevaluated GJS constants".
- *Why it fails:*
  - M² = e^{15λ\|a_0\|} S_2(B_{3×5}) 9^{p′} V_* + 9 C_7 c_U Σ̄_{3×5} 𝔎(p′) λ²(Σ\|a_n\|)²
    (Theorem 5.1, new ll. 1897–1900) contains V_* := sup_{h′}‖V(h′)‖².
  - The record only bounds V_*: "V_* ≤ V̄_* < ∞" (N.20(iv)).
  - Appendix A accordingly says the other constants are explicit "in these, in V_* (explicitly
    bounded, Lemma N.20) and, for Ψ_γ, in the filter of Lemma 9.1" (new ll. 3450–3452). The
    rate also depends on the filter χ, as Lemma 9.1 now says.
  - Both summary sentences are true mathematically: V_* = V̄_* (C11), and χ is a fixed
    explicit choice. But the equality V_* = V̄_* appears nowhere in the record, and the two
    summaries do not match Appendix A.
- *Repair:* in N.20(iv) add "with equality for h′ = 1_{[a,a+2]}, so V_* = V̄_*", and in
  Appendix A replace "explicitly bounded" by "explicit". Alternatively, name V_* and the filter
  in the two summaries.
- *Severity:* MINOR.

**F2 (MINOR). "The integrands are continuous" relies on a property of GJ3's weight that the
record does not list.**

- *Locator:* proof of `cor:canonical`, new ll. 3194–3195 and 3203–3205 (p. 43).
- *Text:* "let $\bar h\ge0$, $\supp\bar h\subseteq[-1,1]$, $\int\bar h=1$, be the averaging
  weight", and later "the integrands are continuous, as $b\mapsto\omega_{g_n}(\tau_bA)$ … is".
- *Why it fails:*
  - The integrands contain h̄, and continuity is not among the three properties listed for h̄.
  - GJ3 p. 210 prints "h(·) ≥ 0 is C^∞", so the sentence is true of the weight GJ3 uses.
  - Only measurability is needed, and that holds in any case.
- *Repair:* add "C^∞" to the list, as GJ3 prints it. Alternatively, write "the integrands are
  measurable (h̄ times continuous functions)".
- *Severity:* MINOR.

**F3 (MINOR). The proof identifies GJ3's translation automorphisms without a source, and the new
sentence after the corollary names a reading for the ground states only.**

- *Locator:* proof of `cor:canonical`, new ll. 3191–3194; the sentence after the corollary,
  new ll. 3183–3186 (p. 43).
- *Text:* "let $\sigma_{a'}$ denote the space-translation automorphisms used there (our
  $\tau_{\epsilon a'}=\mathrm{Ad}\,U_{\epsilon a'}$ of Proposition~\ref{prop:ff-symmetries}(T),
  with $\epsilon\in\{\pm1\}$ the direction convention)"; and "that these are the $\Om_{g_n}$ of
  this manuscript rests on the reading recorded in the Scope of Assumption~\ref{A:cutoff},
  applied to \cite{GJ3}".
- *Why it fails:*
  - GJ3 p. 210 defines σ_α by pointing to "II, sections 3.6 and 4".
  - GJ2 p. 400 prints "σ_a(A) = U(−α)e^{itH(g)}Ae^{−itH(g)}U(+α)".
  - Lemma E.7(a)(4) gives 𝔇U(−a)𝔇⁻¹ = U_a.
  - So σ_α = τ_α (ε = +1) holds under the same reading, namely that GJ3 uses GJ2's objects. But
    the record cites none of these steps. That GJ3's algebra 𝔄 is the 𝔄 of §2.1 is the reading
    recorded there and in A6's Scope.
  - Correctness is unaffected: the proof covers both signs of ε, and GJ3's weight h matches the
    proof's h̄ (C3).
- *Repair:* extend the sentence after the corollary with "…, and that its σ_α is τ_α (GJ2,
  p. 400, with Lemma E.7(a)(4); so ε = +1)".
- *Severity:* MINOR.

**F4 (MINOR). In §14 "Sharpness", the last sentence fails at λ = 0, the case that the sentence
before it now excludes.**

- *Locator:* `sec:discussion` §14, new ll. 3356–3358 (p. 45).
- *Text:* "The present filter argument does not obtain an exponential rate; a proof of such a rate
  would require an additional resolvent or Combes--Thomas input not supplied here."
- *Why it fails:*
  - The standing region contains λ = 0 (§2.6: "Throughout, 0 ≤ λ/m_0² < ε_𝒫").
  - At λ = 0, M = 0 and Ψ_{m_1}(d) = 0 for d ≥ d_0 (C10). There the filter argument does give an
    exponential bound.
  - FROZEN read "does not obtain the sharp exponential rate"; changing it to "an exponential
    rate" made the sentence sweeping.
  - This is the defect of the chain audit's F-G, one sentence later.
- *Repair:* "For $\lambda>0$ the present filter argument does not obtain an exponential rate; …".
- *Severity:* MINOR.

**Observations (not findings).**

- **O1.** A1 Scope:
  - GJ71's cited page, p. 255, works "In the representation of Fock space for which the operators
    H_I(κ) are all diagonal", which is a Q-space realisation. "Work in Fock space" is GJ71's own
    framing, and the new clause "that [GJ71, Rosen70] use the same objects is a reading of those
    sources" covers it.
  - The A1 change adds no reading. Before it, the reading "𝔇 carries their V(g) to V(g)" was
    declared collectively for all sources, GJS included. Now GJS's reading is stated correctly,
    as a covariance reading.
- **O2.** A5 at λ = 0:
  - P = λ𝒫 = 0 satisfies Simon's defining condition inf P > −∞ (p. 140). It does not satisfy his
    gloss "a_{2n} > 0".
  - Either way, A5(ii) is immediate at λ = 0: K(g_s) = H_0 for every s, C^∞(H_0) is a core of the
    self-adjoint H_0, and the identity reads 0 = 0.
  - One clause would make this boundary case explicit.
- **O3.** The notice lists the chain audit's objects as "the Locality paragraph of §2.1, Lemma
  2.8, Proposition 12.1, Corollary 12.3, Theorem 13.2 and §14". That audit also covered
  Proposition 2.7, Lemma 9.3, Theorem 12.2 (2), (3), (5), Hypothesis 13.1 and Remark 13.3 (its
  §2.1). The list is incomplete, not false.
- **O4.** "Theorem 12.2 and every other theorem are unchanged in substance" is true of the nine
  theorem environments; 12.2 and D.4 change in attribution only. Theorem 13.2's content is made
  precise through Hypothesis 13.1, which the same sentence discloses. Corollary 12.3 and
  Proposition E.5(T) are named as changed.
- **O5.** The symbol m now means "the mass of that model" in §1.3(b), §1.4 and §14. It also
  denotes (B3)'s order-parameter value in §13 and the mass parameter of Appendix E. Each is
  defined where it is used.
- **O6.** Appendix B, "except for the dilation unitary, which has no counterpart in the sources":
  GJS p. 590 (`gjs-scaling-07.png`) prints "a unitary scaling transformation on
  L_2(S′(R²), dΦ)", which is Euclidean. The clause is accurate in the record's own sense; the
  same entry says that A8(viii) "imports a Euclidean scaling only".
- **O7.** The dated passage of §D.g (new ll. 8079–8080) keeps "the unevaluated finite constant of
  Theorem C.5". It records the changes of 7 November, and the new notice says how that phrase is
  to be read. The editor left it on purpose, and I agree.
- **O8.** The two images newly named in A5's Dossier line, `simon-semibounded-163` and
  `simon-hg-168` (modified 23 Nov 13:32), exist on disk. `audit_2026/evidence/` is git-ignored in
  the public repository (`.gitignore` l. 10), so they reach the record only through the private
  companion.
- **O9.** The pdfTeX warnings "destination with the same identifier" are pre-existing: FROZEN's
  build has the same five anchors (equation.1, .2, .4, .11, .35). Their count rose from 37 to 40
  log lines with the new layout; no anchor is new.

## 5. Dates: the record dated 23 November 2026 and published on 24 November

No sentence of the checked file becomes false if the record is dated 23 November 2026 and
published on 24 November, subject to the three conditions below. A grep for the dates
20–24 November finds these dated sentences:

- **New l. 77 (comment),** "the restriction of Corollary 12.3 and the corrections of 23 November
  2026": true. The edits were made on 23 November: the file was modified on 23 Nov 2026 at 13:49
  CET, and both of the editor's reports are of that day.
- **New l. 81 (comment),** "SOURCE_DATE_EPOCH=1795392000 … (23 November 2026, 00:00 UTC)": true.
  `date -u -r 1795392000` prints 23 Nov 2026 00:00:00 UTC, and the build with that epoch is
  byte-identical to `part_i/main.pdf`.
- **New l. 82,** `\date{23 November 2026}`: true. By the comment above it, the date "tracks the
  last change of the mathematics or of an import's status …, not the build date"; it makes no
  claim about publication.
  - The precedent, from `git log`: FROZEN carries `\date{11 November 2026}`. Commit 73bbb76
    (Appendix E) was made on 2026-11-11 12:05 UTC, and the public HEAD 49f2d23 on 2026-11-21
    13:31 +0100.
- **New l. 161 (notice) and new l. 3593 (Appendix B),** "Audit of 23 November 2026": true. The
  phrase dates the two audits, whose reports are of 23 November.
- **New l. 3174 (comment),** "statement restricted 23 November 2026": true.
- **New ll. 3596 and 3616,** "the status council of 22 November 2026" and "(status council of
  22 November)": true.
- **No other dated sentence.** No sentence says "published", "public since" or "today" of this
  version. The only "before publication" (new l. 156) belongs to the unchanged notice of
  11 November.

Conditions:

1. If a statement or an import's status is changed on 24 November, the comment's rule calls for
   `\date{24 November 2026}` and the epoch of that day. A repair of F1 to F4 that touches a
   statement would be such a change; wording-only edits would not.
2. The notice's "Reports: ugjs/council/ (v6-appendix-e-audit.md, v6-chain-audit.md); gate
   record: part_i/README.md" (new ll. 176–178) and the file names in the Appendix B entry are true
   only if those files are in the published commit. At the time of this check both reports were
   in `ugjs/council/`, untracked, and `part_i/README.md` was modified but uncommitted.
3. "The repairs were re-checked by an agent that wrote none of them" carries no date. It is true
   of the text checked here and of no later edit.

## 6. Checks actually run, with output

Integrity:

- At the start, `shasum -a 256 part_i/main.tex` printed `3da0640725bc…74bbf7`, with 8858 lines,
  equal to my scratch copy. At resumption it printed the same, and `stat` showed the same
  modification time, 23 Nov 13:49:36.
- `git diff -- part_i/main.tex`, saved and `cmp`'d with the council's `repairs-main.diff`:
  IDENTICAL (584 lines each).
- `git show HEAD:part_i/main.tex | cmp - <FROZEN main.tex>`: identical.
- `git log -4`: HEAD is 49f2d23.

Build, in a scratch copy of `part_i/main.tex` outside the repository:

- Three passes of `SOURCE_DATE_EPOCH=1795392000 FORCE_SOURCE_DATE=1 pdflatex
  -interaction=nonstopmode main.tex` (the brief's pdflatex); each exited 0.
- Engine: pdfTeX 3.141592653-2.6-1.40.29 (TeX Live 2026).
- Results:
  - `grep -cE '^!' main.log`: 0
  - `grep -c Overfull main.log`: 0
  - `grep -icE undefined main.log`: 0
  - `pdftotext main.pdf - | grep -nE '\?\?|TODO|Hmm|wait,'`: no output (exit 1)
  - `pdfinfo`: 127 pages; CreationDate Mon Nov 23 01:00:00 2026 CET
  - `shasum -a 256 main.pdf`:
    `ea42d274d822142edd73008eaaa44a9e43ec1e70088c3c44759cd97e8f2098a1`, equal to that of
    `part_i/main.pdf` (the editor's ea42d274…98a1)
  - The log's only "Rerun" line is the package banner of `rerunfilecheck`.
- Control build of FROZEN (three passes, epoch 1794355200): sha256
  `87084de82564cb1a83881f7bab634300f5d436c7a26b89bd8ba3b84e980fd80e`, equal to FROZEN's
  `main.pdf`, and `main.aux` byte-identical, so the toolchain reproduces. Warnings: 23 hyperref
  "Token not allowed" in both builds; duplicate-destination lines 37 (FROZEN) and 40 (new) (O9).

Labels (script over `\newlabel`, number and page):

- 238 labels in FROZEN and 238 new; none added, none removed, no number changed.
- 199 page changes: 113 by +1 and 86 by +2.

Statement environments (theorem, proposition, lemma, corollary, hypothesis, assumption, remark,
definition, srcfact, srcfactstar, aux*; compared by label, whitespace-normalised):

- 127 labelled and 2 unlabelled, before and after; none added or removed; the 2 unlabelled ones
  unchanged.
- Changed: `A:cutoff`, `A:domain`, `A:gjs`, `lem:filter`, `lem:cluster`, `prop:spectral`,
  `thm:MAIN`, `cor:canonical`, `hyp:broken`, `rem:gjs7576`, `thm:D4`, `aux:d4-not`,
  `prop:ff-symmetries`. These are thirteen, exactly the editor's list.
- Word diffs:
  - `thm:MAIN` and `thm:D4`: "finite, … of Theorem C.5" became "of Definition N.14, finite by
    Theorem C.5", and nothing else.
  - `aux:d4-not`: the same attribution, plus "$S_2(B_{3\times5})$".
  - `lem:cluster`: "open".
  - `prop:spectral`: "open"; "$\omega$ is a state on $\A$ with".
  - `hyp:broken`: the one new sentence.
  - `rem:gjs7576`: "gap." became "gap and the uniform local moment."
  - `lem:filter`: the χ clause.
  - `prop:ff-symmetries`: the strong-continuity clause.

AGENTS.md 3.8 (every symbol defined):

- The added lines contain 61 distinct control sequences. All 61 already occur in FROZEN; the
  non-standard ones (`\G`, `\A`, `\Om`, `\ip`, `\HH`, `\C`, `\R`, `\dist`) are preamble macros,
  ll. 46–58.
- New symbols are defined where they are used:
  - ω_n and g_n by [GJ3, (2.3)–(2.4)] in the corollary;
  - \|O\| as "the length of O", and R_a in a display;
  - m as "the mass of that model";
  - C^∞(H_0) as ⋂_n D(H_0^n);
  - S_n as the symmetrisation of Appendix E.

References:

- The added lines refer to 40 labels. Each resolves in the new `main.aux` to the intended
  statement, among them: A1, A5–A8, Appendices A–E, N.14, N.15, N.20, N.39, 12.1, 12.2, 12.3,
  13, 13.1, 13.2, 14, 1.4, 2.1, 2.4 (Source Fact), 2.5, 2.8, 5.1, 7.8, 9.1, 9.3, 10.5, D.3, D.4,
  E.1, E.2, E.5, E.7, C.5 and (T).
- I read the PDF text (`pdftotext`) of the notice, of the A5 and A8 Scopes, of Corollary 12.3,
  of Hypothesis 13.1 and of Theorem 13.2. "the Scope of~\ref{A:cutoff}" renders as "the Scope of
  A1", and "§§\ref{subsec:strategy} and~\ref{sec:discussion}" as "§§1.4 and 14".

Rendering: I rendered pages 2, 3, 43 and 44 of the new PDF at 80 dpi and looked at pages 2
and 43. The notice and the corollary are set as their own paragraphs, and nothing lies outside
the margins.

Sources:

- Rendered from `refs/`: GJ3 PDF pages 1–9 at 150 dpi (pages 3 and 8 read, printed pp. 205 and
  210); GJ71 PDF pages 1–4 at 130 dpi (pages 1 and 3 read, pp. 253 and 255); Rosen70 PDF page 2
  (p. 158); Simon PDF page 162 (p. 140).
- Page images viewed in `audit_2026/evidence/`: `gjiii-08`, `gj2-local-algebra-40`,
  `gjs-source-05`, `gjs-p589-06`, `gjs-scaling-07`, `gjs-theorems-11`, `gjs-theorems-12`,
  `gjs-proof-14`, `gjs-uniform-46`, `simon-dgamma-053`, `simon-semibounded-163`, `simon-hg-168`,
  `simon-transfer-180`.
- Text search with `pdftotext`, for location only: GJ2 §§3.6 and 4; the first page of the MMST
  arXiv copy.
- Files read: `m2/m2.tex` ll. 40–244; `part_ii/v3_continuum_package.tex` ll. 222–240; grep of
  `part_ii/v2_interaction_comparison.tex`.

Other:

- Image count: 97 files in `audit_2026/evidence/`, of which 54 are named in
  `audit_2026/citation_screenshot_dossier.tex` and 43 are not.
- `git check-ignore`: `audit_2026/evidence/` is ignored by `.gitignore` l. 10; 0 evidence files
  are tracked in the public repository.
- `git log -4` printed: 49f2d23, committed 2026-11-21 13:31:56 +0100; 73bbb76, committed
  2026-11-11 12:05:09 +0000.
- No numerical computation was used. The new identities (R_a, μ⁻¹ = 2C, the sharp-time
  covariance, V_* = V̄_*, M = 0 at λ = 0) were checked by hand.

## 7. Not done, not verified, not run

Not done:

- I did not open the earlier council reports V4, V4f, V5 and D3. The text checked is new, so
  there is no comparison with them.
- I did not check the public texts (`README.md`, `docs/`, `CITATION.cff`, `companion/`) or the
  gate record in `part_i/README.md`.
- I did not re-check chain F-H (§14's "remains open"), which lies outside the diff and was left
  by the orchestrator's decision.
- I did not re-derive Lemma 9.2, Theorems 5.1, 7.8 and 11.1, or Appendices C–E beyond the loci
  cited above; they were used as stated.

Not verified:

- MMST's journal, volume and pages. These are the orchestrator's verification; I read only the
  arXiv copy.
- The declared readings themselves: the A1-Scope readings of the sources' V(g) and of GJS's
  covariance, the normalisation of φ_F, and GJ3 using GJ2's objects.
- Simon's definition of C^∞(H_0), which is not on the pages read.
- GJ2 §3.6 on a page image. It was read through text search only, and its (3.6.2) is used
  through Lemma E.7(a)(4), which I did not re-audit.
- The proof sketch and the numerics of `m2/` (statements only).
- Whether `simon-semibounded-163` and `simon-hg-168` are committed in the private companion.

Not run: any git command that changes state; any `kb` command; `docs/extract.py`; any network
access.

## 8. Files written

- `v6-repairs-check.md` (this report), in the council's reports directory.
- Scratch files, outside the repository and not deliverables: a copy of `part_i/main.tex` with
  its build products, a build of FROZEN, page renders, and two comparison scripts.

**Final line.** The sentence "The repairs were re-checked by an agent that wrote none of them"
stands, for the text checked (`part_i/main.tex`, sha256 3da06407…, 8858 lines); it needs no
further fix to be true. F1 to F4 are optional MINOR repairs. Any edit made after this check,
including a repair of F1 to F4, is a new repair that this check does not cover: it must be
re-checked by an agent that did not write it, or the sentence must be confined to the repairs of
the two passes checked here.

## 9. Re-check of the four last edits (23/24 November 2026)

**Object.** `part_i/main.tex`, sha256
`254f9f0d1af903c08a23fbe95ca8206cc72a13dcc7e2c955a5381afc35709ff9`, 8858 lines. The file's
modification time is 23 Nov 2026, 23:21:29 CET. The orchestrator wrote the four edits; I wrote
none of them. Line numbers in this section are those of this file.

**Integrity.**

- The orchestrator's copy of the text checked in §§1–8 is byte-identical to that text (sha256
  3da06407…). Its `main.aux` is byte-identical to the aux of my build of that text.
- `diff` from the checked text to `part_i/main.tex` is byte-identical to the orchestrator's
  `final-edits.diff` (24 lines). The two files differ by exactly the four edits and nothing else.
- The checked text is HEAD 49f2d23 plus the 38 hunks of `repairs-main.diff` (§6). So the whole
  diff against HEAD is those 38 hunks plus these four edits.

| # | edit | locus | verdict |
|---|---|---|---|
| E1 | Lemma 9.1: "… $C_{N,\gamma,M}$ of Lemma~\ref{lem:rate} depend on this choice" became "… of \S\ref{sec:lppl} depend on this choice" | `lem:filter` 9.1, p. 36, l. 2595 | **holds.** `sec:lppl` is §10, "The one-path LPPL estimate" (p. 38, ll. 2762–2960). It contains Lemma 10.5 (l. 2918), where Ψ_γ is defined by (29) (l. 2929), C_{N,γ,M} appears in the statement (ll. 2931–2934) and C′_γ in the proof (l. 2943). The text renders "of §10". The lemma's mathematics is unchanged. |
| E2 | the paragraph "The states of [GJ3] are built … which is not among the sources listed there." moved from between `\end{corollary}` and `\begin{proof}` to directly after `\end{proof}` | after the proof of `cor:canonical` 12.3, ll. 3216–3219 (p. 43), before §13 | **holds.** The diff deletes and re-inserts the same four lines, so the wording is unchanged. The paragraph is self-contained: "these" refers to "the ground states" in the same sentence. A grep finds no positional reference to it; Appendix B (i), "the reading it rests on is named", does not say where. The proof now follows the statement directly, and the paragraph follows its end mark on the same page. The proof's display uses Ω_{g_n} before the reader reaches the sentence that names the reading, but the two are adjacent, which is acceptable. |
| E3 | my F2: the averaging weight is now "$\bar h\ge0$, $\bar h\in C^\infty$, $\supp\bar h\subseteq[-1,1]$, $\int\bar h=1$" | proof of `cor:canonical` 12.3, l. 3189 (p. 43) | **holds.** GJ3 p. 210 (`audit_2026/evidence/gjiii-08.png`, viewed in this session) prints "The function h(·) ≥ 0 is C^∞, has support in [−1, 1] and". With h̄ continuous, "the integrands are continuous" (ll. 3198–3200) is now justified inside the record. F2 is closed. |
| E4 | my F4: §14 now reads "For $\lambda>0$ the present filter argument does not obtain an exponential rate; …" | §14 "Sharpness", l. 3356 (p. 45) | **holds.** For λ > 0, M > 0 and Ψ_{m_1} is not O(e^{−cd}) (C10). At λ = 0 the sentence now claims nothing. F4 is closed. Appendix B item (v) ("claim the non-exponential decay of Ψ_{m_1} for λ > 0 only") is now literally true of all of §14. |

**The notice and the Appendix B entry, against the whole diff against HEAD: still true.**

- E1 falls under item (vii), "the dependence on the filter (Lemma 9.1)".
- E2 falls under item (i), "the reading it rests on is named"; the item does not state a position.
- E4 falls under item (v).
- E3 is not named literally. It belongs to the measurability argument of item (ii).
  Observation O10: item (ii) could add "and the smoothness of the weight of [GJ3, p. 210]". The
  notice's "smaller corrections are listed in Appendix B" is not made false by this one-word
  precision inside a proof that item (ii) covers in substance.
- "Theorem 12.2 and every other theorem are unchanged in substance; no label was renumbered"
  remains true.
- None of the four edits changes the mathematics of a statement or the status of an import, and
  all four were made on 23 November. The conclusions of §5 (dates) are unchanged.

**Mechanical checks** (scratch copy of the new `part_i/main.tex`; three passes of
`SOURCE_DATE_EPOCH=1795392000 FORCE_SOURCE_DATE=1 pdflatex -interaction=nonstopmode main.tex`):

- Each pass exited 0.
- `grep -cE '^!' main.log`: 0. `grep -c Overfull main.log`: 0. `grep -icE undefined
  main.log`: 0.
- `pdftotext main.pdf - | grep -nE '\?\?|TODO|Hmm|wait,'`: no output (exit 1).
- `pdfinfo`: 127 pages.
- sha256 of `main.tex`: `254f9f0d…709ff9`. sha256 of `main.pdf`:
  `b2bd43f31ce15ad5863ddac7746fff067bc0b51221521bed4e7d3bfd85d17271`, byte-identical to
  `part_i/main.pdf` (`cmp`). These are the orchestrator's figures.
- `main.aux` and `main.toc` are byte-identical to my build of the checked text, so all 238 labels
  keep their numbers and their pages.
- Against FROZEN: no label added, removed or renumbered; 199 page changes (113 by +1, 86 by +2),
  as before.
- Statement environments against FROZEN: the same thirteen (`A:cutoff`, `A:domain`, `A:gjs`,
  `lem:filter`, `lem:cluster`, `prop:spectral`, `thm:MAIN`, `cor:canonical`, `hyp:broken`,
  `rem:gjs7576`, `thm:D4`, `aux:d4-not`, `prop:ff-symmetries`). Against the checked text only
  `lem:filter` changed (E1); E2 to E4 lie outside statement environments.
- Log warnings: 23 hyperref "Token not allowed" and 40 duplicate-destination lines, the same as
  in the build of the checked text.
- I read the rendered text of the four loci with `pdftotext` (pp. 36, 43, 45), and rendered
  p. 43 at 80 dpi and looked at it.

**Status of my findings.** E3 closes F2 and E4 closes F4. F1 and F3 stay open as MINOR points, by
the orchestrator's decision. F3's sentence now stands after the proof (ll. 3216–3219), and its
proposed repair applies there unchanged.

**Final line.** The sentence "The repairs were re-checked by an agent that wrote none of them"
stands for `part_i/main.tex` with sha256 254f9f0d…709ff9. It now covers the 38 hunks of the
editor's two passes and the four edits written by the orchestrator. I checked all of them and
wrote none of them. It covers no later edit.
