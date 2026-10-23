# Memo R1: cqft (constructive quantum field theory)

23 October 2026. Read in this session: the brief; `README.md`; `docs/status.md`, `imports.md`, `index.md`, `PLAN.md`; `labels.md`; `part_i/main.tex` in full (lines 1-3027); `docs/results.json`, `docs/extract.py`; `part_i/README.md`; `part_i/C5_reading_record.md`; `part_ii/README.md`; `part_ii/gate_II11_scoping.tex` (abstract, section 1); `strategy.md` (scope amendment of 5 September, the GATE STATUS paragraphs); `docs/figures/make_figures.py`, `rate.svg`. From `refs/`, GJS (Ann. of Math. 100): text layer of pp. 588-597, 626, 628-629; pp. 590, 593, 594, 595, 596, 628, 629 rendered and read as images. Numbers come from `labels.md`; pages are printed pages of `main.pdf`.

## A. Must know

**A1.** Theorem 12.2 is proved, conditional on U_GJS (A8(vi)) and the literal imports A1-A7: for 0 ≤ λ/m₀² < ε_P the full plateau net (ω_g)_{g∈𝒢} converges in every local dual 𝔄(O)*, with ‖(ω_g − ω_∞)|_{𝔄(O)}‖ ≤ Ψ_{m₁}(d) when g ≡ 1 on O_d, to a locally normal, translation-invariant (for even P, ℤ₂-invariant) spectral ground state, and every H(g), g ∈ 𝒞_H, has gap ≥ m₁ and local moment ≤ M. *Thm 12.2, p. 30; (U_GJS), p. 10; §2.4, p. 7; (31), p. 28.*

**A2.** U_GJS is the statement that one constant C₈ gives |∫Q(x⁰)dq_{h_{T,g}}| ≤ C₈‖Q(x⁰)‖_GJS on the whole slab family h_{T,g} = 1_{[−T,T]}⊗g (T > 0, g ∈ 𝒞_H); the source states this quantifier (p. 629) and uses it (pp. 594-597), but Theorem 1.1.8 as printed says only "uniformly as h → 1". The record imports it at the source's scope and does not re-derive the cluster expansion. *(U_GJS), SF 2.3-2.4, p. 10; A8(vii′), pp. 10-11; A8 Scope, p. 11; Prop. C.1, p. 36.*

**A3.** The Euclidean estimates reach the Hamiltonian only through slab FKN identities at fixed g, and ψ̂_T = e^{−TH(g)}Ω₀/‖·‖ → Ω_g by simplicity alone, so no gap is presupposed: the gap is an output, and there is no circularity. *(2)-(3), Lemma 4.1, p. 15; Lemma 4.4, p. 16; A1 Scope, p. 7.*

**A4.** The Cauchy estimate consumes exactly two nonstandard inputs, (M₂) and (G), both uniform over 𝒞_H; after §7 no further GJS input enters, only the literal imports A1-A7 and the exact light cone. *Thm 5.1, p. 16; Thm 7.8, p. 21; §1.4, p. 4; Prop. 2.7, p. 12.*

**A5.** Not claimed: uniqueness among locally normal ground states (Corollary 12.3 says only that ω_∞ is canonical for the cutoff family), a sharp exponential rate (the filter cannot give one), anything outside the weak-coupling region; C5 (a second human reading of the GJS page images) is open. *§1.3, p. 4; Cor. 12.3, p. 31; Lemma 9.1, p. 24; §14, p. 32.*

## B. Should know

**B1.** The region is the source's own dimensionless hypothesis: ε_P := λ_*/M_*² for a fixed pair such that the GJS expansion is valid at mass M_* for every coupling below λ_*, and the GJS dilation (s = m₀/M_*) carries λ/m₀² < ε_P into the printed region. All constants are working-coordinate constants, which Remark 3.3 transports back (rate Ψ_{m₁,*}(sd), gap s·m₁,*). ε_P, m₁, C₇, C₈, K₁ and K₂ are not quantified, so "explicit rate" means explicit in terms of them and of a free χ. *§2.6, Prop. 3.2, p. 13; A8(viii), p. 11; Rem. 3.3, p. 14.*

**B2.** In §7, U_GJS is used at one fixed g and uniformly in the slab half-width T only, and the gap's independence of g is CE2's printed h-independent m₁. The uniformity of U_GJS across g is what makes M independent of g, and Lemma 10.2 uses that along the path g_s. `strategy.md` (5 September) records this split and judges a Hamiltonian bypass for (M₂) dead (see H). *Lemmas 7.1-7.4, pp. 18-19; Prop. 7.5, Lemma 7.6, p. 20; Thm 5.1 Step 5, p. 17; Lemma 10.2, p. 26.*

**B3.** (M₂): V(h)² is itself a GJS observable (individually Wick-ordered factors at equal times), and a support of length 2 meets at most 3 cells, which gives M² = 9C₈K₁K₂^{8p′}(4p′)!λ²(Σ|aₙ|)². U_GJS at time 0 then bounds ‖V(h)ψ̂_T‖ ≤ M for all T, and the closed graph of V(h) passes the bound to Ω_g. *A8(ii), p. 9; (M₂), p. 16; (5)-(6), p. 17.*

**B4.** (G): moment transfer and two limits in T turn CE2 across a horizontal strip of width t − 2 into ⟨ψ_Q, e^{−tH(g)}ψ_Q⟩ ≤ Ĉ_Q e^{−m₁t} on centred polynomial vectors. These vectors are total because sharp-time fields have exponential moments in Ω_g, which needs the source's licence of unbounded total degree with bounded individual Wick degree. *Lemmas 7.1-7.4, pp. 18-19; Prop. 7.5, Lemma 7.6, p. 20; Thms 7.7-7.8, p. 21; A8(ii), p. 9.*

**B5.** The record's consistency argument: the printed proof of Theorem 1.1.7 takes its h-independent constant from 1.1.8 at the same h, and Lemma 7.4 uses 1.1.7 as printed at h_{T,g}; whoever doubts U_GJS must doubt printed CE2 at slab cutoffs equally. *A8 Scope (b) and A8(vii′)(b), p. 11.*

**B6.** Appendix C supports the scope reading but carries no step of the proof: Prop. C.1 concerns five audited source mechanisms, and Lemma C.2 to Thm C.5 re-prove normalisation and stability uniformly in h, whereas Thm 12.2 needs only the per-h statements it imports as A3. *Prop. C.1, p. 36; pp. 37-38; A3, p. 8.*

**B7.** Ψ_γ(d) = 32M Σ_{n≥⌊d⌋}(‖W_γ‖₁e^{−γn/4} + T_γ(n/2)), for d ≥ d₀ = 4 + 2/γ, is at most C_{N,γ,M}(1+d)^{−N} for every N. It bounds a norm difference, measures no decay, and depends on the free χ. *(29)-(30), Lemma 10.5, p. 28.*

**B8.** The record names an h-trace of GJS pp. 598-629 completing Proposition C.1 as the only proportionate route to an unconditional theorem; it is not scheduled. Closing C5 would not change the status of U_GJS. *`docs/imports.md`; `docs/status.md`.*

## C. Pointer table

| statement (point to it; do not reproduce) | why routine or bookkeeping | where |
|---|---|---|
| Rem. 2.5 | sharp-time Euclidean Wick order = C-order (one Gaussian integral) | p. 12 |
| Prop. 2.6 | two lines from A5(i) | p. 12 |
| Lemma 2.8 | simplicity + positivity give (T) and parity | p. 12 |
| Lemma 3.1 | class memberships; affine paths stay in 𝒢 | p. 13 |
| Rem. 3.3 | scaling dictionary; one sentence | p. 14 |
| Lemmas 4.1-4.3 | slab FKN, bounded → signed → unbounded by truncation; quote (2)-(3) only | p. 15 |
| Thm 5.1 Steps 2-4; Cor. 5.2 | cell count, arithmetic (9 pairs; 9·8! = 362 880) | pp. 16-17 |
| Lemma 6.1; Prop. 6.2; Rem. 6.3 | counting, Cauchy-Schwarz over cells | pp. 17-18 |
| Lemmas 7.1-7.3 | weak compactness, closed graph | pp. 18-19 |
| Lemma 7.6; proof of Thm 7.7 | series bound; analytic characteristic functionals, Fourier uniqueness, martingales | pp. 20-21 |
| Prop. 8.1 | hypercontractive Hölder bookkeeping | p. 22 |
| Prop. 8.2 except (15) | Riesz projection; keep Ω̇_s = −H_s⁻¹Q_sV(v)Ω_s | p. 23 |
| proof of Lemma 9.2 | Gaussian separator, a = R/γ | p. 25 |
| Lemmas 10.1-10.2 | insert the filter; partition of unity + (M₂) | p. 26 |
| Prop. 10.4 Steps 3-4; proof of Lemma 10.5 | eight cells per shell; tail sum | pp. 27-28 |
| Prop. 11.2 | 2δ argument | p. 29 |
| proof of Cor. 12.3 | averaging bookkeeping | p. 31 |
| Rem. 13.3 | literature scope | p. 32 |
| App. A, B | constants, provenance | pp. 33-34 |
| Lemma C.2 to Rem. C.6; Prop. C.7 | h-uniform stability, not consumed by Thm 12.2; coverage | pp. 37-38 |
| A1-A7, full text | one table; quote only A1's simplicity and A6's (P) | pp. 7-9 |

Read in full (my area): A8(iii)-(vii′) with Scope; Lemma 4.4; Thm 5.1 Steps 1, 5, 6; Lemma 7.4 to Thm 7.8.

## D. The longest chain

The `\ref` graph's longest chain (12 steps, via Thm 5.1, Lemmas 4.3-4.1, Lemma 3.1, A3) avoids the gap, which §§8-10 assume as (G_γ) and §11's opening sentence instantiates. The reader experiences the longer route through the gap:

1. Slab measures dq_{h_{T,g}} exist (A2, A3, Lemma 3.1(ii); pp. 8, 13).
2. Slab FKN (2)-(3), bounded then unbounded (Lemmas 4.1-4.3, p. 15).
3. ψ̂_T → Ω_g by simplicity only (Lemma 4.4, p. 16).
4. ‖QΩ_g‖² ≤ C₈𝔫(Q)² from U_GJS at fixed g (Lemma 7.1, p. 18).
5. One- and two-point limits T → ∞ (Lemmas 7.2-7.3, pp. 18-19).
6. CE2 across a strip of width t − 2, hence decay e^{−m₁t} on centred vectors (Lemma 7.4, p. 19; Prop. 7.5, p. 20).
7. Exponential moments under |Ω_g|²dφ₀ (Lemma 7.6, p. 20).
8. Polynomial vectors are total (Thm 7.7, p. 21).
9. Gap (G) (Thm 7.8, p. 21).
10. Path regularity and (15) (Props 8.1-8.2, pp. 22-23).
11. Exact filter (18) (Lemma 9.1, p. 24).
12. State derivative (24) (Lemma 10.1, p. 26).
13. Clustering with one unbounded argument (23) (Lemmas 9.2-9.3, p. 25).
14. Localisation with ‖V_jΩ_s‖ ≤ M (Lemma 10.2, p. 26; joins the (M₂) branch).
15. Two-regime bound (26) (Lemma 10.3, p. 27).
16. One-path estimate (27) (Prop. 10.4, p. 27).
17. Ψ_γ super-polynomial (30) (Lemma 10.5, p. 28).
18. Cauchy net, limit state, rate (31) (Thm 11.1, p. 28).
19. Normality, exact spectral passage, invariances (Prop. 11.2, Prop. 12.1, Thm 12.2; pp. 29-30).

Cut, each piece ending at a displayed checkpoint:

- **I** (1-3): ∫F₁(Φ(−t/2))F₂(Φ(t/2)) dq_{h_{T,g}} = ⟨F₁ψ_{T−t/2}, e^{−tH(g)}F₂ψ_{T−t/2}⟩/‖ψ_T‖², and ψ̂_T → Ω_g with no gap used.
- **II** (Thm 5.1 Steps 1, 5, 6; a parallel branch): (M₂).
- **III** (4-6): ⟨ψ_Q, e^{−tH(g)}ψ_Q⟩ ≤ Ĉ_Q e^{−m₁t}, with m₁ independent of g.
- **IV** (7-9): (G).
- **V** (10-12): (24).
- **VI** (13-15): (26).
- **VII** (16-18): (31).
- **VIII** (19): Theorem 12.2 (1)-(5).

## E. Figures

Own proposals:

- **E-a. Where each uniformity comes from** (the annotation layer of F1). Purpose: B2. Drawn: boxes for printed CE2, U_GJS, (G) and (M₂), with arrows labelled "m₁ independent of h" (CE2 → (G)), "fixed g, uniform in T" (U_GJS → (G)) and "uniform in g and T" (U_GJS → (M₂) → Lemma 10.2). Computed: nothing. Must not suggest that (G) is free of U_GJS or that CE2 is independent of 1.1.8 in the source (dotted arrow: "1.1.7's printed proof uses 1.1.8 at the same h").
- **E-b. U_GJS at the source's scope.** Purpose: A2, B5. Drawn: four boxes holding only the record's own quotations from A8(vii′) and Source Fact 2.4 (the affine path, pp. 594-595; (1.1.16) "uniformly in h"; 1.1.7 derived from 1.1.8, p. 597; p. 629), with implication arrows into a dashed #8250df box for U_GJS. Computed: nothing; no page images. Must not suggest a proof: the caption says the source states and uses the quantifier but displays no proof for the slab family, and C5 is unread.
- **E-c. The Euclidean picture of the gap** (replaces F5). Purpose: A3, B4. Drawn: the (x⁰, x¹) plane with the slab [−T, T] × supp g, sharp-time rows at ±t/2 and the separating strip of width t − 2; the labels "T → ∞ at fixed g" and "e^{−TH(g)}Ω₀/‖·‖ → Ω_g (simplicity)"; the bound of Prop. 7.5. Computed: nothing. Must not suggest an assumed gap, an infinite-volume measure, or physical lengths (these are working coordinates).

Verdicts:

- **F1: keep, change.** Put E-a's labels on the GJS arrows and colour everything downstream of U_GJS (the whole spine) #8250df; Lemma 9.1 and Prop. 2.7, if drawn, stay neutral. No Appendix C arrow may close the dashed edge.
- **F2: keep.** Note that only V(v)Ω_s enters, and it is finite by (M₂).
- **F3: keep, change.** Caption: "one admissible χ, γ = 1; Lemma 9.1(i) proves finite moments of every order". No slope numbers, and not the `<desc>` text of `rate.svg` (G4). F6 becomes the right panel.
- **F4: keep.**
- **F5: replace with E-c.**
- **F6: merge into F3.** Mark M = 1 and γ = 1 as illustrative; the true M depends on the unquantified C₈, K₁, K₂.
- **F7: change.** Do not draw 61 nodes. Either colour the roughly 20 spine statements by what their proofs consume (literal import; U_GJS via (M₂) or (G); analysis under (G_γ)), or caption the computed count exactly (G3). Part II stays out of this figure (see section P).

## F. Traps

| tempting | correct |
|---|---|
| "Theorem 12.2 proves norm convergence." | Proved, conditional on U_GJS and on the literal imports A1-A7. |
| Thms 5.1, 7.8, 11.1 and 13.2 are unconditional, since only 12.2 says "Assume U_GJS". | All of them consume U_GJS through the standing imports of §2.4. |
| "U_GJS is GJS Theorem 1.1.8." | It is the slab-uniform form of 1.1.8, whose printed statement says "uniformly as h → 1". The quantifier is stated on p. 629 and used on pp. 594-597; it is imported, not re-derived. |
| "Appendix C establishes h-uniformity." | It audits five mechanisms (Prop. C.1 is limited to them) and proves h-uniform normalisation and stability. It re-derives neither the expansion nor U_GJS. |
| "The uniform gap follows from U_GJS." | The gap's independence of g is CE2's h-independent m₁. U_GJS enters (G) only at fixed g; M's independence of g needs it across g. |
| "Explicit rate." | A formula in M, m₁ and a free χ. M, m₁ and ε_P are not quantified, so no number is available. |
| "The state decays super-polynomially"; "the kernel decays like t⁻⁶". | Ψ bounds ‖(ω_g − ω_∞)\|_{𝔄(O)}‖. Lemma 9.1(i) gives W_γ ∈ L¹ with all moments finite; the computed shape belongs to one χ. |
| "Purely Hamiltonian." | Only the Cauchy argument is; its two inputs are Euclidean, via slab FKN. |
| Thm 13.2: "no phase transition at weak coupling", or "broken phases have no uniform gap". | For even P at weak coupling, (B1)-(B4) cannot all hold. The proof uses Thm 12.2 (1), (3), (4), hence (M₂) and U_GJS as well. Nothing is proved at strong coupling. |
| "Cor. 12.3: the vacuum is unique." | Canonical for the cutoff family (it agrees with every w* limit point of [GJ3]'s states, averaged or not); uniqueness is not claimed. |
| "24 of the 61 statements are conditional." | The extractor flags 24 by `\ref`-reachability, A8 itself included (G3). |

## G. Findings

**G1 (MINOR).** `main.tex` l. 780, A8 Scope, p. 11: "the one-sentence statement of Theorem 1.1.8 says ``uniformly as $h\uparrow1$''." The printed Theorem 1.1.8 (GJS p. 595, rendered today) reads "uniformly as h → 1". The quotation changes the glyph, and ↑ suggests monotone convergence, which the source does not state. Source Fact 2.3 (p. 10) paraphrases it correctly, and C5 item 5 quotes "h → 1". Repair: `$h\to1$`.

**G2 (MINOR).** `main.tex` l. 1349, proof of Lemma 7.1, p. 18: `\|Q\widehat\psi_{T_\alpha}\|le C_8^{1/2}\mathfrak n(Q)`. A backslash is missing, and `main.pdf` p. 18 prints "∥Qψ̂_{T_α}∥leC₈^{1/2}𝔫(Q)" (pdftotext). Repair: `\|\le`.

**G3 (MINOR; affects F7 and any count sentence).** `docs/extract.py` l. 145 sets `imports_A8 = "A:gjs" in closure or label == "A:gjs"`, and three documents rest on it. `docs/status.md` says "24 reach A8 through their own proof chain and therefore inherit this conditionality"; `docs/results.md` says "everything marked here inherits the conditionality of Theorem 12.2"; `README.md` says "conditional exactly when its proof chain reaches A8". The flag is `\ref`-reachability of one label, and it fails in four ways:
- (a) the 24 include A8 itself;
- (b) Source Facts 2.2-2.4, which are items (iv), (v) and (vii) of A8, are separate nodes with no edge to A8, so Lemma 7.4 (whose proof uses only Rem. 6.3 and Source Fact 2.2 = CE2) and Rem. C.6 are not flagged;
- (c) mentions and forward references count as uses: Prop. 3.2, a scaling computation, "cites U_GJS" only through its pointer to Rem. 3.3, whose dictionary refers to Thm 12.2 (path 3.2 → 3.3 → 12.2 → 5.1 → (U_GJS)); Rem. 13.3 does so through Thm 13.2; Lemma 4.3 does so through its remark that U_GJS supplies the square moments at later applications, although its statement carries its own hypotheses;
- (d) Prop. 6.2 is flagged although it uses only the printed norm (1), so it does not inherit U_GJS.

Counted today on `results.json`: 24 flagged; 23 reach (U_GJS), A8 included; 29 reach some item of A8. No theorem is affected. Repair: treat A8's sub-labels as A8, report "reaches (U_GJS)" separately from "uses a printed A8 item", or caption the number as a `\ref`-graph count.

**G4 (MINOR).** The `<desc>` of `docs/figures/rate.svg` and `rate-dark.svg`, generated at `make_figures.py` l. 117-119, reads "crossing the t^-2 and t^-5 guides, so its effective power grows." The figure draws t⁻² and t⁻⁶ guides (l. 144), and the growth claim was withdrawn: commit 5d42114 says "stop claiming the slope grows", and the comment at l. 151-154 records non-monotone measured slopes. The `fig_rate` docstring (l. 101-106) repeats the claim. Repair: regenerate the description.

**G5 (MINOR).** GJS p. 593 (rendered today) defines Δ_j as "the unit lattice square in R² centered at the lattice side [sic: site] j ∈ Z²". Theorem 5.1 Step 2, Lemma 6.1 and the proof of Prop. 6.2 use cells [j, j+1), a lattice offset by ½, and call the pieces localized in the sense of (1). Every count used is invariant under the offset: at most 3 cells for support length 2; N_I ≤ ⌊L⌋+2; and a unit square meeting x⁰ = ±t/2 lies within distance 1 of that line, so the strip width t − 2 of Lemma 7.4 stands. No constant changes, but as written the pieces are not localized in the printed sense. The convention is already a C5 item (App. B, p. 34). Repair: one sentence in A8(iii) or §6.

**G6 (MINOR).** Two sentences attribute to the gap alone what the proof of Theorem 13.2 uses:
- §1.3(c), p. 4: "a cutoff-uniform gap is incompatible with that two-phase structure (Theorem 13.2). Thus an extension to such a broken phase would have to abandon the uniform-gap input";
- §13, p. 31: "The uniform gap of Theorem 7.8 is incompatible with a fully classified two-phase structure."

Theorem 13.2 is stated only for 0 ≤ λ/m₀² < ε_P. Its proof uses Thm 12.2(1) in Step 2, and that convergence consumes (M₂); it uses Thm 12.2(3)-(4) in Step 3. Repair: "incompatible with the cutoff-uniform gap and local moment, through Theorem 12.2". §14 is already phrased with care ("a proof based on a cutoff-uniform gap").

**G7 (MINOR).** `docs/imports.md` describes Level 2 as "a display-by-display trace of the h-dependence through the printed expansion on GJS pp. 598–629". On GJS p. 628 (rendered today), the proof of Theorem 4.1 reads "This step is similar to, but easier than the analogous step in the proof of Theorem 4.2 below, so we do not give the details". Theorems 1.1.8 and 1.1.11 are then derived "by Theorem 4.1" (pp. 628-629). A trace of printed displays cannot cover an unprinted step, so Level 2 would have to supply it. Not checked: whether the case n = 0, the only one U_GJS needs, passes through that step.

**G8 (MINOR; an omission whose repair would strengthen the record).** GJS p. 590 (rendered today) introduces exactly the slab family: "Let h_j = g(x⃗)χ_j(t), where χ_j is the characteristic function of the interval [−j, j] … Then the Feynman-Kac formula yields (1.11) W(x̂₁, …, x̂ₙ) = lim_{j→∞} S_{h_j}(x₁, …, xₙ)". It also says "Thus λ/m₀² is a dimensionless coupling constant, and a basic hypothesis of the entire paper is that λ/m₀² is chosen to be small." The record cites p. 590 only for the dilation (A8(viii), Prop. 3.2). The p. 595 Remark (an n-point bound with a Schwartz norm "independent of h") appears in C5 item 5 but not in A8(vii′). Repair: optional additions to A8(vii′)/(viii) and C5.

Not checked: the interior of GJS pp. 598-627; the Hamiltonian-bypass sources named in `strategy.md`; A1-A7 against their sources.

## H. Your reader's first question

A constructive field theorist asks first: *is U_GJS a theorem of Glimm, Jaffe and Spencer, or a new assumption?* The companion should answer on its first page:
- The proof needs Theorem 1.1.8 uniformly over the slab cutoffs h_{T,g}: it lets T → ∞ at fixed g and needs moments uniform in g, and h_{T,g} does not tend to 1.
- The printed theorem says only "uniformly as h → 1".
- GJS nevertheless state the stronger quantifier. p. 629 says the estimates of Theorems 1.1.8 and 1.1.11 "are uniform in the space cutoff h"; Theorem 1.1.11 carries "uniformly in h" in (1.1.16), and 1.1.8 is its case B = I, n = 0; and Theorem 1.1.7, whose constant they derive from 1.1.8 at the same h, is applied at every cutoff of an affine path (pp. 594-597).
- The quantifier is therefore the source's own. What is missing is a displayed proof for this family, which the record does not supply.
- Hence "proved, conditional on U_GJS": a hypothesis the source asserts, the record has not re-derived, and no second human has yet checked in the transcriptions (C5).

To the follow-up, why not prove (M₂) on the Hamiltonian side: g-uniform local moments were open in the 1970-71 literature, and the substitutes cover only translation-averaged states (`docs/imports.md`). That is a verdict on the printed record, not a no-go theorem.

## P. Part II page (draft companion text, about one page)

**Part II: open at gate (II.11).** Nothing in Part I depends on Part II, and §14 of the record states that there is "no mathematical dependence in either direction".

*What it is about.* Part I removes the spatial cutoff g. Part II asks a different question: uniformity in a lattice or wavelet resolution, in the operator-algebraic renormalisation programme over the wavelet maps of Morinelli-Morsella-Stottmeister-Tanimoto [MMST] (§1.3(d), §14). Its setting is a fixed spatial torus 𝕋_L, dyadic lattices of spacing ε_N = 2⁻ᴺε₀ with Daubechies D4 refinement maps, and the nearest-neighbour lattice φ⁴ Hamiltonian.

*The gate.* Statement (II.11) (scoping pass, Definition 1.1) concerns the lattice ground states ω_N. Evaluated on a fixed coarse Weyl generator embedded at resolution N, they should converge as N → ∞ to the vector state of the ground vector of the continuum torus operator K_L constructed in phase V3. Convergence is required pointwise, for every fixed coarse scale M and symbol ξ. The scoping pass "proves no part of (II.11); it fixes what 'proving (II.11)' shall mean, statement by statement."

*Why a fixed coarse scale.* Already for the free model there are local Weyl unitaries with liminf_N ‖ω⁽⁰⁾_N − ω⁽⁰⁾∘β_N‖ ≥ e^{−√(2+√2)/4} − e^{−3π/16} > 0. So no finest-scale local-state-norm error Cε_N^ϑ, ϑ > 0, is possible, and the comparison is made at a fixed coarse scale (§14).

*Status per claim* (`docs/status.md`, verbatim):

| claim | status |
|---|---|
| finest-scale diagonal norm convergence | **disproved** |
| exact finite-torus interacting model and ground state | **constructed** |
| interacting fixed-coarse projective cluster state along a cofinal subnet | **proved unconditionally** |
| MMST free fixed-coarse / projective convergence | proved in the source, **strengthened here** to an explicit D4 power rate |
| exact free gap, group-velocity bound, Wick logarithm | **proved** in the Lamport note |
| Battle–Federbush as a source for OAR-uniform CE1/CE2 | **not available** — the cited note treats different phase-cell variables |
| full-sequence interacting convergence and identification with the continuum P(φ)₂ state | **open**, exactly at the coarse Weyl characteristic-functional limit |
| interacting scale-uniform gap, local second moment, Lieb–Robinson | **open** |
| the cited Nachtergaele–Raz–Schlein–Sims theorem | **inapplicable** to the Wick quartic: it assumes V′ ∈ L¹(ℝ) |
| the former path (1−s)H_N + sH | **undefined** without a common Hilbert-space/form realization; removed from the corrected program |

The record is not consistent about this gate. `strategy.md` and the ledger of phase V4 record (II.11) as closed at the stated import scope, `part_ii/README.md` says that phase closure was not reached, and the repository README says the gate is open; this companion uses the README's wording.
