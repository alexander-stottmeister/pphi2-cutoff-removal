# Memo `qi`: quantum-information theorist, round R1 (23 October 2026)

Numbers from `labels.md`; pages are printed pages (= PDF index of `part_i/main.pdf`, checked with `pdftotext`).

## A. Must know

1. **What is proved.** Theorem 12.2 (p. 30) is proved, conditional on U_GJS (A8(vi), display (U_GJS), p. 10). At weak coupling the full plateau net converges in norm on every A(O), with ‖(ω_g − ω_∞)|A(O)‖ ≤ Ψ_{m₁}(d) whenever g ≡ 1 on O_d (Thm 11.1, eq. (31), p. 28).
2. **The engine is LPPL in derivative form, not a spectral flow.** Along g_s = (1−s)g + sg′ the ground vector moves by Ω̇_s = −H_s⁻¹Q_sV(v)Ω_s (Prop 8.2, eq. (15), p. 23). The exact filter rewrites H_s⁻¹Q_s as filtered real-time evolution (Lemma 9.1(ii), eq. (18), p. 24; Lemma 10.1, eq. (24), p. 26), and integrating the resulting bound over s gives the one-path estimate (Prop 10.4, eq. (27), p. 27).
3. **Two cutoff-uniform numbers carry the model.** Besides the construction inputs A1–A6 (among them the exact light cone, Prop 2.7, p. 12), the engine consumes exactly two estimates: the gap γ = m₁ of (G) (Thm 7.8, p. 21) and the ground-state moment M of (M₂) (Thm 5.1, p. 16). Both come from the GJS cluster expansion, and they are the only places where U_GJS enters §§8–11.
4. **The ground state absorbs the unboundedness.** V(g′) − V(g) has infinite norm (§1.4, p. 4), but the perturbation only ever acts on the ground vector. The clustering bound needs ‖XΩ‖, not ‖X‖ (Lemma 9.3, eq. (23), p. 25), and ‖V_jΩ_s‖ ≤ M holds cell by cell (Lemma 10.2, eq. (25), p. 26).
5. **Faster than every power, not exponential, and only an upper bound.** Ψ_γ(d) ≤ C_{N,γ,M}(1+d)^{−N} for every N (Lemma 10.5, eq. (30), p. 28). The filter kernel W_γ cannot have exponential tails (strip analyticity, §1.4, p. 5). A sharp rate would need a resolvent or Combes–Thomas input that the record does not supply (§14, p. 33).

## B. Should know

1. **The gap is an output.** A1 (p. 7) imports simplicity and explicitly not isolation. The slab vacuum converges by simplicity alone (Lemma 4.4, p. 16). Euclidean clustering (Source Fact 2.2, p. 10) gives semigroup decay (Prop 7.5, p. 20) and, with density (Thm 7.7), the gap (Thm 7.8, p. 21). QI readers expect gap ⇒ clustering; here clustering ⇒ gap comes first, then gap ⇒ clustering in real time (Lemma 9.3).
2. **Why uniform in the cutoff.** Ψ_γ depends on γ and M (Lemma 10.5). The Cauchy step (Thm 11.1, eq. (32), p. 28) needs one bound for all g, g′ ≽ g₀ and for every g_s between them, so it needs one γ and one M for all of C_H.
3. **§§8–10 are proved for an abstract γ** under the standing hypothesis (G_γ) (p. 22). γ is set to m₁ only in §11 (p. 28). Prop 8.2, Lemma 9.3 and Lemma 10.1 are "independent of A8" in labels.md only as implications from (G_γ).
4. **How the clustering works** (Lemma 9.3 via Lemma 9.2, eq. (19), p. 25). F(t) = ⟨XΩ,(e^{itH} − P₀)AΩ⟩ and its mirror G have spectral supports in [γ,∞) and (−∞,−γ], and the exact light cone makes them agree for |t| < R. A Gaussian separator then gives |F(0)| ≤ 2𝔪e^{−γR/2}. The 1/2 is the method's; sharpness is not claimed.
5. **What the filter lemma is credited with** (Lemma 9.1, p. 24): W_γ ∈ L¹ with all moments finite, hence T_γ(r) ≤ C_{q,γ}(1+r)^{−q}. χ is free, and every constant depends on it.
6. **Two regimes** (Lemma 10.3, eq. (26), p. 27). For |t| ≤ r_j/2 the evolved observable stays at distance ≥ r_j/2 from the cell B_j, and clustering gives 2Me^{−γr_j/4}. Beyond that the lemma uses only 2M, weighted by the filter tail T_γ(r_j/2).
7. **Shells** (Prop 10.4, Steps 1 and 3, p. 27). Every cell lies at distance ≥ d ≥ d₀ = 4 + 2/γ, and each unit-distance shell contains at most eight cells (four per side). Ψ_γ is therefore a tail sum over n ≥ ⌊d⌋ and depends on d alone, not on the size of {g ≠ g′}.
8. **An exact light cone, so no Lieb–Robinson bound** (Prop 2.7, p. 12). Speed ≤ 1 for every cutoff dynamics, uniformly in g, from free speed one, a speed-zero interaction and Trotter (A6(i)).

## C. Pointer table (not read in the companion)

| item | why routine | where |
|---|---|---|
| Prop 8.1 | FKN, hypercontractivity, Vitali: s ↦ e^{−TK_s} is norm-C¹; used only to differentiate | p. 22 |
| Prop 8.2(i) | Riesz projection with an s-uniform relative separation | p. 23 |
| proof of Lemma 9.1 | integration by parts; Dirichlet's test | p. 24 |
| proof of Lemma 9.2 | Gaussian separator; choice a = R/γ | p. 25 |
| Lemma 10.2 | partition of unity; one call to Thm 5.1 | p. 26 |
| Prop 10.4, Steps 3–4 | integer count per shell; endpoint limit; hermitian-functional norm | p. 27 |
| proof of Lemma 10.5 | geometric series; integral comparison; ⌊d⌋ ≥ (3/5)(1+d) | p. 28 |
| Prop 11.2 | one inequality for a monotone net | p. 29 |
| Prop 2.6, Lemma 2.8, Lemma 3.1 | domains, covariance, class memberships; one-liners | pp. 12–13 |
| Remark 2.5, Cor 5.2, Lemma 6.1, Prop 6.2, Remark 6.3 | conventions, cell counts, norm bookkeeping | pp. 12, 17–18 |
| Appendix A | constants table: cite, do not reproduce | p. 33 |

## D. The longest chain

Computed from `results.json` (uses ∪ proof_uses between numbered statements; the cycle-forming forward pointers 3.2→3.3, 4.3→5.1, 4.3→7.1 dropped): 12 steps, A3 → 3.1 → 4.1 → 4.2 → 4.3 → 5.1 → 10.2 → 10.3 → 10.4 → 10.5 → 11.1 → 11.2 → 12.2. With the one prose edge the reader follows, (G_γ) supplied by Thm 7.8 (p. 22): 15 steps, A3 → 3.1 → 4.1 → 4.2 → 4.3 → 7.1 → 7.2 → 7.5 → 7.8 → 8.2 → 10.1 → 10.4 → 10.5 → 11.1 → 11.2 → 12.2.

As experienced, with the parallel branches:
1. A8(iv)–(vi), pp. 9–10.
2. Slab FKN, Lemmas 4.1–4.3, p. 15.
3. Slab vacuum, Lemma 4.4, p. 16.
4. (M₂), Thm 5.1, p. 16.
5. Transfer and slab limits, Lemmas 7.1–7.3, pp. 18–19.
6. CE2 strip, Lemma 7.4, p. 19.
7. Semigroup decay, Prop 7.5, p. 20.
8. Density, Lemma 7.6, Thm 7.7, pp. 20–21.
9. Gap, Thm 7.8, p. 21.
10. Derivative formula, Props 8.1–8.2, pp. 22–23.
11. Filter, Lemma 9.1, p. 24.
12. State derivative, Lemma 10.1, p. 26.
13. Clustering, Lemmas 9.2–9.3 with Prop 2.7, p. 25.
14. Cell moments, Lemma 10.2, p. 26.
15. Two regimes, Lemma 10.3, p. 27.
16. Shells and s-integration, Prop 10.4, p. 27.
17. Rate, Lemma 10.5, p. 28.
18. Cauchy and limit, Thm 11.1, p. 28.
19. Normality, spectral passage, assembly, Prop 11.2, Prop 12.1, Thm 12.2, pp. 29–30.

Cut (≤ 3 steps per piece, each ending at a displayed checkpoint):

| piece | steps | checkpoint |
|---|---|---|
| I | 2–4 | (M₂): ‖V(h)Ω_g‖ ≤ M for all g ∈ C_H |
| II | 5–7 | Prop 7.5: ⟨ψ_Q, e^{−tH(g)}ψ_Q⟩ ≤ Ĉ_Q e^{−m₁t} |
| III | 8–9 | (G): spec H(g) ⊆ {0} ∪ [m₁,∞) |
| IV | 10 | (15) |
| V | 11–12 | (24) |
| VI | 13 | (23) |
| VII | 14–15 | (26) |
| VIII | 16–17 | (27), (30) |
| IX | 18–19 | (31); Thm 12.2(1)–(3) |

Pieces IV–VIII should form one companion section. It opens with the contract "for γ and M uniform in the cutoff, two plateau cutoffs equal to 1 on O_d give states within Ψ_γ(d) on A(O)": the last sentence of Lemma 10.5 (p. 28), read under (G_γ).

## E. Figures

### Own proposals

**Q1. Two affine paths** (purpose: what is old, what is new).
- *Top row:* the GJS Euclidean argument quoted in A8(vii′)(a), p. 11. The path is h₁ + α(h₂ − h₁), the derivative is a covariance (1.1.12), Thm 1.1.7 is applied per cell, and the result is O(1)e^{−m₁d/2} for Schwinger functions.
- *Bottom row:* the record's path g_s. The derivative (15) carries H_s⁻¹; filter, light cone and clustering then give norm convergence on A(O) at rate Ψ_{m₁}(d).
- *Computed vs drawn:* drawn; nothing is computed.
- *Must not suggest:* that the Euclidean bound implies the Hamiltonian one (§1.4: "no soft passage from moments to norms"), comparable rates, h (spacetime) ≡ g (space), or a re-proof of (1.1.11).

**Q2. Cells and shells** (purpose: why Ψ depends on d alone).
- *What is drawn:* a line with O, O_d, the half-lines where v ≠ 0, the cells B_j (length ≤ 2) and the unit shells, at most four cells per side in each. Each cell is tagged with its term of (28).
- *Computed vs drawn:* drawn to scale; nothing is computed.
- *Must not suggest:* equal or measured contributions, or a dependence on |supp v|.
- Could be F4's second panel.

**Q3. Where U_GJS enters the engine** (a zoom of F1 onto §§8–11).
- *What is drawn:* boxes for Prop 2.7, Props 8.1–8.2, Lemmas 9.1–10.5 and Thm 11.1.
- *Computed vs drawn:* edges generated from `proof_uses`. Two plugs in `#8250df`: Thm 7.8 → (G_γ), dashed and labelled "instantiated in §11", and Thm 5.1 → Lemma 10.2.
- *Must not suggest:* that the uncoloured boxes hold for P(φ)₂ without U_GJS. They are implications.

### Verdicts on F1–F7

- **F1: keep, change.** Label the arrows into the LPPL node by what flows along them (γ = m₁; M; the light cone via Prop 2.7). (M₂) enters at Lemma 10.2, (G) at (G_γ). Q3 could serve as an inset.
- **F2: keep, change.** Draw the plateau of g_s as containing {g=1}° ∩ {g′=1}° (Lemma 3.1(iii)), and annotate "V(v) unbounded and not small; only V_jΩ_s enters". It must not suggest a physical time s, a spectral-flow automorphism, or a small perturbation.
- **F3: keep, change.**
  - *Left panel:* Ŵ_γ over E, with spec H(g) shaded underneath. (18) fixes only 1/E on [γ,∞) and the value 0 at E = 0; the notch is a choice.
  - *Right panel:* the computed tail T_γ(r), which is what Lemma 9.1(i) bounds and what Ψ uses, rather than |W_γ(t)|. Add reference powers labelled "constants arbitrary".
  - *Caption:* "moments proved; curve numerical, one χ, γ = 1".
  - *Numerical check (this memo):* the site's |W₁(t)| for t ≤ 160 is unchanged to four digits under a 10⁶-fold tighter quadrature tolerance (Python 3.14.7, NumPy 2.5.2, SciPy 1.18.1).
- **F4: keep, change.** Continue the cone until it meets B_j at |t| = r_j, and label r_j/2 < |t| < r_j "clustering available, not used". It must not suggest that B_j enters the cone at r_j/2, as the README does.
- **F5: keep** (cqft's figure). Key arrow for QI readers: "simplicity only (Lemma 4.4)", the no-circularity point.
- **F6: merge into F3**, as `rate.svg` does. Show the two computed summands with M = 1 (a prefactor) and d₀ marked; show (1+d)^{−N} only as reference powers. The caption should say the filter tail is the slower summand, hence the bound is not exponential.
- **F7: keep, change.** Define the shading as "proof chain reaches A8 through numbered statements". Hatch Prop 8.2, Lemma 9.3 and Lemma 10.1 ("assume (G_γ), supplied by Thm 7.8") and Prop 12.1 ("hypothesis from Thm 11.1"). Take the Part II table verbatim from `docs/status.md`.

## F. Traps

| tempting | correct wording |
|---|---|
| "quasi-adiabatic continuation / spectral flow in the continuum" | No automorphism is constructed: the derivative of the cutoff ground state is bounded and integrated along an affine path (Prop 8.2, Lemma 10.1, Prop 10.4). [Hastings, BMNS] are cited only as machinery that "does not start" (§1.4). |
| "P(φ)₂ has no Lieb–Robinson bound" | None is needed: an exact light cone, speed ≤ 1, uniform in g (Prop 2.7). |
| "exponential rate", "e^{−m₁d/4}" | Ψ_{m₁}(d) ≤ C_N(1+d)^{−N} for every N (Lemma 10.5); not exponential. |
| "the filter decays like t^{−6}" (any decay law) | W_γ ∈ L¹, all moments finite, T_γ(r) ≤ C_{q,γ}(1+r)^{−q} (Lemma 9.1(i)). Shapes are numerical, for one χ. |
| "the filter tail makes the rate super-polynomial" (README) | Both summands are; the filter tail is the slower one and keeps Ψ from being exponential. |
| "super-polynomial is the best this method can do" | The record shows only that W_γ cannot have exponential tails (§1.4). |
| "the true rate is poly(d)e^{−2m₁d}" | Context from the working note m2/ (proof sketch, numerics), for the quadratic model, with m₁ that model's physical mass. Not a Part I result. |
| "the limit has a mass gap m₁" / "ω_∞ clusters exponentially" | The gap holds for every cutoff H(g) (Thm 7.8; Thm 12.2(5)). Part I states no gap for the GNS Hamiltonian of ω_∞. Clustering of ω_∞ appears only for the order parameter, inside the proof of Thm 13.2 (eq. (34), p. 32). |
| "perturbative, small perturbation" | v = g′ − g has ‖v‖_∞ ≤ 1 and support of any size; only its distance ≥ d from O is used. |
| Thm 5.1, 7.8 or 11.1 quoted bare | Their statements omit "assume U_GJS"; each is conditional on it through A8(vi). |
| "compactness-free", "no compactness anywhere" | No limit point of states is selected. Weak compactness in Hilbert space is used (Thm 5.1 Step 6, Lemmas 7.1–7.3), with each limit identified uniquely. |
| "exact" read as sharp | "Exact" means an identity with no error term. |

## G. Findings

There is no CRITICAL or MAJOR finding in §§8–11, Prop 2.7 or §14. I re-derived every step of Props 8.1–8.2, Lemmas 9.1–9.3 and 10.1–10.5, Prop 10.4 and Thm 11.1 by hand, including these constants:
- the Hölder exponents of Prop 8.1;
- the optimisation a = R/γ;
- γd₀/2 = 2γ + 1;
- 4M·8 = 32M and the four-integer shell count;
- ⌊d⌋ ≥ (3/5)(1+d) for d ≥ 4.

All findings below are MINOR.

**G1. Wrong reason for "not exponential"** (§1.4, `main.tex` 300–305, p. 5; repeated in `part_i/README.md` 118).
- *Text:* "a kernel with exponential tails has a transform analytic in a strip, which cannot vanish on a real neighbourhood of 0 --- as Ŵ_γ must --- without vanishing identically … it is intrinsic to the method".
- *Why it fails:* (18) only needs Ŵ(0) = 0 and Ŵ = 1/E on [γ,∞). Vanishing on [−γ/2, γ/2] is a design choice in (17), not a requirement. The argument therefore covers the record's χ-family, whereas "intrinsic" claims every exact filter.
- *Repair:* "a transform analytic in a strip that equals 1/E on [γ,∞) equals 1/E on the strip minus 0, so it cannot be finite at E = 0." The conclusion stands.

**G2. "True rate" for the quadratic model** (§1.3(b), `main.tex` 235–237, p. 4; §14, 2508–2511, p. 33).
- *Text:* "the true rate is poly(d)e^{−2m₁d} (companion note m2/); Ψ_{m₁} is super-polynomial …".
- *(a) Two different m₁:* `m2/m2.tex` line 67 sets m₁² := m₀² + λ, the physical mass of H₀ + (λ/2)∫g:φ₀²:. `main.tex` freezes m₁ as the GJS constant (§2.3).
- *(b) "True" is stronger than its support:* m2's `prop:rate` (line 172) has only a "Proof sketch". Its claim that the local state norm is also bounded above by a constant times ‖P_OΔ_φP_O‖ ("as well as above", line 182) has no argument. The numerics fit kernel values at one point (line 214).
- *Repair:* "the working note m2/ reports (proof sketch, numerics) poly(d)e^{−2md}, with m that model's physical mass." Not used in any proof.

**G3. "Compactness-free"** (`main.tex` 166, p. 3; 271, p. 4).
- *Text:* "compactness-free" and "no compactness anywhere".
- *Why it fails:* Thm 5.1 Step 6 (line 1233) and Lemmas 7.1–7.3 (e.g. line 1343) extract weakly convergent subsequences or subnets. This is harmless, because each limit is identified by weak closedness of a graph, but the sentence is literally false.
- *Repair:* "no limit point of states is selected", as p. 5 already puts it.

**G4. "Norm-convergent Bochner integral"** (Lemma 9.1(ii), `main.tex` 1806, p. 24).
- *Why it fails:* t ↦ e^{itH} is in general only strongly continuous. The proof bounds the integrand's norm but does not establish operator-norm measurability.
- *Repair:* "strongly convergent; a Bochner integral on each vector, of norm ≤ ‖W_γ‖₁". Lemma 10.1 uses (18) on one vector only, so nothing downstream changes.

**G5. The "24 of 61" count understates** (documentation: `docs/extract.py` 130–145; `README.md` 82; `docs/status.md` 27).
- *Why it fails:* the closure stops at equation labels. (G_γ) (p. 22), which is discharged by Thm 7.8 only in prose, therefore never reaches A8, so Prop 8.2, Lemma 9.3 and Lemma 10.1 are computed as "independent of A8". The status page's "the rest do not [inherit this conditionality]" then understates: for P(φ)₂ these three statements rest on (G_γ), which only Thm 7.8 supplies. As implications they are classified correctly.
- *Repair:* add the edge eq:Ggamma → thm:G, or introduce a third class "under (G_γ)".

**G6. Summands' roles reversed** (`README.md` 96–97).
- *Text:* "the filter tail … is what makes the rate super-polynomial rather than merely exponential-then-stuck".
- *Why it fails:* the exponential summand decays faster, and the filter tail is the slower one. Nothing in Lemma 10.5 is "exponential-then-stuck".
- *Repair:* "both summands decay faster than every power; the slower filter tail sets the rate, so Ψ is not exponential."

**G7. Where the cone reaches B_j** (`README.md` 109–111; `make_figures.py` 203).
- *Text:* "past that time only the trivial bound survives"; "the cone has swallowed the gap".
- *Why it fails:* O_{|t|} reaches B_j only at |t| = r_j. Lemma 10.3 switches to 2M at r_j/2 by choice, to keep the distance ≥ r_j/2.
- *Repair:* "for |t| ≤ r_j/2 the cell stays at distance ≥ r_j/2 from O_{|t|}; beyond that, Lemma 10.3 uses only the trivial bound 2M."

**G8. Typo in Lemma 7.1** (proof, `main.tex` 1349, p. 18). `\|le` lacks a backslash, and the PDF prints "‖Qψ̂_{T_α}‖leC₈…". Repair: `\le`.

**G9. Hidden dependence on χ.** C_{q,γ} (Lemma 9.1), C′_γ and C_{N,γ,M} (Lemma 10.5) and Ψ_γ itself depend on χ, which the notation suppresses. Repair: in Lemma 9.1, say "fix χ once for each γ".

## H. Your reader's first question

"Isn't this just local-perturbations-perturb-locally, or quasi-adiabatic continuation, in the continuum? What is new, and why does it need a cluster expansion?"

The standard machinery does not start, because V(g′) − V(g) has infinite norm (§1.4, p. 4). The record keeps the shape of the argument but replaces each ingredient:
- **Norms of local terms → ground-state moments.** The record uses ‖V(h)Ω_g‖ ≤ M (Thm 5.1). That is enough because the perturbation only ever acts on the ground vector, both in the derivative formula (Prop 8.2) and in the clustering lemma (Lemma 9.3).
- **Lieb–Robinson bounds → the exact light cone** of every cutoff dynamics (Prop 2.7).
- **A gap along the path → one m₁ for the whole cutoff class** (Thm 7.8), obtained as an output of Euclidean clustering.

No automorphism is constructed. The derivative of the state is bounded through an exact inverse-energy filter (Lemma 9.1) and integrated along the affine path (Prop 10.4).

The cluster expansion is needed because the moment bound and the gap must hold uniformly in the cutoff. The record imports both from Glimm–Jaffe–Spencer through slab FKN transfer, exactly where U_GJS enters. The price of an exact filter is a rate faster than every power but not exponential (Lemma 10.5; §14).
