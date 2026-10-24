# PLAN — reader's companion to the cutoff-removal theorem (round R2, editor)

23 October 2026. Synthesis of the four R1 memos: `companion/council/memo-{aqft,qi,cqft,editor}.md`. For the author's approval before drafting (R3).

Binding: `companion/council/BRIEF.md` (§4 non-negotiables; §3 U_GJS wording) and `companion/council/labels.md` (every number). Locators have the form *number, printed page of `part_i/main.pdf`*; printed page = PDF index, checked.

**Frozen U_GJS sentence**, used verbatim wherever U_GJS is first described in a section:

> U_GJS (A8(vi)) is the cutoff-uniform form of GJS Thm 1.1.8 on the slab family h_{T,g}; since 5 September 2026 it is imported at the scope at which the source states it (p. 629) and uses it (pp. 594–597: the affine path and the derivation of Thm 1.1.7 from 1.1.8); it is not a quantifier strengthened beyond the source; it is still a named hypothesis, because it is assembled from four pages and the cluster expansion is not re-derived (Appendix C audits the mechanism and proves two analytic prerequisites only).

---

## 1. Tiering

**Tier 1** goes on pages 1–2 (§1 and the front matter) and is repeated wherever it is used. **Tier 2** consists of the ideas, each with about one page and one figure (§§3–7). **Tier 3** is the pointer appendix (App A).

### Tier 1: what the reader must keep

| # | item | locators |
|---|---|---|
| T1.1 | **The theorem.** For 0 ≤ λ/m₀² < ε_P, the full plateau net (ω_g)_{g∈𝒢} (no subnet, no averaging) converges in norm on every local algebra 𝔄(O). The rate is ‖(ω_g−ω_∞)\|𝔄(O)‖ ≤ Ψ_{m₁}(d) whenever g ≡ 1 on O_d, faster than every inverse power, and depends on O only through d. The limit is locally normal, translation invariant, ℤ₂-invariant for even 𝒫, and a ground state of (𝔄, α) *in the spectral sense*. Item (5) gives the gap and the moment for the cutoff Hamiltonians H(g), g ∈ 𝒞_H. | Thm 12.2, p. 30; eq. (31), p. 28; Def 2.1, p. 6; Lemma 10.5, eq. (30), p. 28 |
| T1.2 | **Status.** Proved, conditional on U_GJS and on the imports A1–A8; this holds equally for Thms 5.1, 7.8, 11.1, 13.2, Prop 11.2 and Cor 12.3, although their statements do not say so. The record is AI-assisted and not refereed; C5 (a second human reading of the source page images, a transcription check) is open; human verification is ongoing. | A8(vi), eq. (U_GJS), p. 10; Scope paragraph, p. 11; App B, p. 34 |
| T1.3 | **What is new: convergence, not the topology.** The record proves that the unaveraged full net has one limit, with a rate; hence every w\* limit point of Glimm–Jaffe's construction equals ω_∞ (canonical, not unique). *Context:* GJ3 Thm 2.3 already places GJ3's averaged states in a norm-compact subset of each local dual, with normal limit points, and GJ3 Thm 2.1 gives the limit points positive energy (GJ3 pp. 210–211; R5 re-checks before quoting). | Cor 12.3, p. 31; §1.1, p. 3 |
| T1.4 | **The engine.** The proof has two layers, joined by two cutoff-uniform numbers. The Euclidean layer gives the moment M (Thm 5.1) and the gap m₁ (Thm 7.8). The Hamiltonian layer bounds the derivative of the state along an affine path of cutoffs, by an exact inverse-energy filter, the exact light cone and clustering with one unbounded argument; no automorphism or spectral flow is constructed. §§8–11 use the GJS package only through m₁ and M. | Thm 5.1, p. 16; Thm 7.8, p. 21; Prop 8.2, eq. (15), p. 23; Lemma 9.1, eq. (18), p. 24; Prop 2.7, p. 12; Lemma 9.3, eq. (23), p. 25; Prop 10.4, eq. (27), p. 27 |
| T1.5 | **Not claimed.** The record does not claim uniqueness of ω_∞ among locally normal ground states, a sharp (exponential) rate, or anything outside the weak-coupling region; the dichotomy Thm 13.2 is conditional on Hyp 13.1. Nor does it claim a gap for a GNS Hamiltonian of ω_∞, identification with the Euclidean (Wightman) theory of GJS, or Lorentz covariance (which the record does not discuss). | abstract, p. 2; §1.3, p. 4; §14, pp. 32–33; Thm 13.2, p. 31; Thm 12.2(5), p. 30 |

### Tier 2: the ideas (one page and one figure each)

| # | idea | home | figure | locators |
|---|---|---|---|---|
| T2.0 | Architecture: two layers, five steps, and the checkpoints (M₂), (G), (27), (31) | §3 | Fig. 1 (F1) | §1.2 table, p. 3; Thms 5.1, 7.8, 11.1, 12.2 |
| T2.1 | U_GJS is the source's quantifier, assembled from four pages; that is why the theorem is conditional | §4 | Fig. 2 (E1) | A8(vi)–(vii′), pp. 10–11; SF 2.2–2.4, p. 10; Prop C.7, p. 38; App C, p. 35 |
| T2.2 | The gap is an output: slab FKN at fixed g, with simplicity as the only spectral input, then CE2 → decay → density → (G); (M₂) from V(h)² as one GJS observable | §5 | Fig. 3 (F5) | Lemma 4.1, eq. (2), p. 15; Lemma 4.4, p. 16; Thm 5.1, p. 16; Lemma 7.4, p. 19; Prop 7.5, p. 20; Thms 7.7–7.8, p. 21 |
| T2.3 | Local perturbations perturb locally: the derivative (15) → filter (18) → cone and clustering (23) → two regimes (26) → one path (27) | §6 | Fig. 4 (F2+F4) | Prop 8.2, p. 23; Lemma 10.1, p. 26; Lemma 10.2, p. 26; Lemma 10.3, p. 27; Prop 10.4, p. 27 |
| T2.4 | Why faster than every power and not exponential: what Lemma 9.1(i) proves, and the two summands of Ψ | §6 | Fig. 5 (F3+F6) | Lemma 9.1, p. 24; Lemma 10.5, eqs. (29)–(30), p. 28; §1.4, p. 5 |
| T2.5 | The ground-state property costs an identity, not an estimate (window \|t\| < d(g,O), patching (P)); canonical, not unique | §7 | Fig. 6 (W) | Prop 12.1, p. 29; A6 eq. (P), p. 9; Thm 11.1, p. 28; Prop 11.2, p. 29; Cor 12.3, p. 31 |

### Tier 3: the pointer appendix (App A; one line each, never read in the body)

The body uses the statement or display of an item marked †. Tier 3 holds its proof and bookkeeping only.

| item | why routine or bookkeeping | where |
|---|---|---|
| A1–A7 | literal pinpoint quotations of construction results; §4 gives one table row each, quoting only A1's simplicity and A6's (P) | pp. 7–9 |
| A8(i)–(iii), (vii′); SF 2.2–2.4 | verbatim transcriptions of the source; §4 paraphrases (vii′) in three steps | pp. 9–11 |
| Rem 2.5 | sharp-time Euclidean Wick order equals C-order | p. 12 |
| Prop 2.6 | Ω_g ∈ Ran e^{−tK(g)} ⊆ D(V(h)), in two lines | p. 12 |
| proof of Prop 2.7† | Trotter product plus a speed-zero interaction | p. 12 |
| Lemma 2.8† (proof) | simplicity plus positivity give (T) and parity | p. 12 |
| Lemma 3.1 | class memberships; affine paths stay in 𝒢 | p. 13 |
| Prop 3.2, Rem 3.3 | dilation into the printed region; one sentence on working coordinates | pp. 13–14 |
| Lemmas 4.1†–4.3 | slab FKN: bounded, then signed, then unbounded, by truncation | p. 15 |
| Thm 5.1† Steps 2–4; Cor 5.2 | cell count (3 cells, 9 pairs); φ⁴ arithmetic (9·8! = 362 880) | pp. 16–17 |
| Lemma 6.1, Prop 6.2, Rem 6.3 | cell counting; GJS norms of cylinder monomials | pp. 17–18 |
| Lemmas 7.1–7.3 | slab limits of moments at fixed g; weak compactness plus closed graph | pp. 18–19 |
| proof of Lemma 7.4† | localisation decomposition; strip of width t−2 | p. 19 |
| Lemma 7.6; proof of Thm 7.7† | exponential moments; analytic characteristic functionals, Fourier uniqueness, martingales | pp. 20–21 |
| Prop 8.1; proof of Prop 8.2† | hypercontractive Hölder bookkeeping; Riesz projection with s-uniform separation | pp. 22–23 |
| proofs of Lemmas 9.1†, 9.2† | integration by parts and Dirichlet's test; Gaussian separator with a = R/γ | pp. 24–25 |
| proof of Lemma 10.1†; Lemma 10.2† | insert the filter; partition of unity plus (M₂) | p. 26 |
| Prop 10.4† Steps 3–4; proof of Lemma 10.5† | eight cells per shell, s-integration, hermitian-functional norm; tail sums | pp. 27–28 |
| proof of Thm 11.1† Step 2; proof of Prop 11.2† | compatible limit functionals extend to a state; the 2δ argument | pp. 28–29 |
| proof of Cor 12.3† | averaging bookkeeping | p. 31 |
| Hyp 13.1†, Rem 13.3 | the four hypotheses; literature scope | pp. 31–32 |
| the record's App A, App B | constants table; provenance and corrections register | pp. 33–34 |
| App C (C.1–C.6); Prop C.7† | source-mechanism audit; h-uniform normalisation and stability, not consumed by Thm 12.2; Prop C.7 lists where CE1 and CE2 are used | pp. 35–38 |

The App A table has one more column, *depends on*, filled by hand from the proofs: **U** (consumes U_GJS through (M₂) or (G), or directly), **G_γ** (an implication under the standing hypothesis (G_γ)), **P** (uses only printed A8 items: CE2, the printed norms or the dilation), **–** (independent of A8).

---

## 2. Outline and page budget

Units: one page ≈ 450 words of prose; a figure with its caption ≈ 0.4 pp, except Fig. 1 (0.5 pp), Fig. 4 (0.6 pp) and Fig. 6 (0.3 pp). Word budgets are for prose including boxed displays; tables are budgeted in pages. The **15-minute path** is p. 1 plus §§1, 3 and 8. The **45-minute path** is everything except App A.

| part | title | sentence to retain (italic, opens the section) | figure | pages | prose words |
|---|---|---|---|---|---|
| front | title, notice, abstract, how to read | — | — | 1.0 | notice ≤ 80, abstract ≤ 150, how-to-read ≤ 60 |
| §1 | What is proved, and under what | *Theorem 12.2 is proved conditional on one imported estimate, U_GJS; the news is that the full net converges, with a rate.* | — | 2.0 | 900 (incl. the two boxes) |
| §2 | Why it was open | *Compactness gave Glimm and Jaffe a vacuum; it did not give convergence.* | table, 0.3 pp | 1.25 | 430 |
| §3 | The architecture | *Two cutoff-uniform numbers, the gap m₁ and the moment M, make the net Cauchy.* | Fig. 1 | 1.5 | 450 |
| §4 | The one import that is not a quotation | *U_GJS is the source's own quantifier, assembled from four pages and not re-derived; that is why the theorem is conditional.* | Fig. 2; A1–A7 table, 0.25 pp | 2.0 | 600 |
| §5 | Euclidean layer: the moment and the gap | *The gap is an output: simplicity of the ground state is the only spectral input.* | Fig. 3 | 1.75 | 600 |
| §6 | Hamiltonian layer: local perturbations perturb locally | *An exact filter turns the gap into decay in time; an exact light cone turns time into distance.* | Figs. 4, 5 | 3.0 | 880 |
| §7 | From Cauchy to the theorem | *The ground-state property costs an identity, not an estimate.* | Fig. 6 | 1.25 | 430 |
| §8 | Boundaries, and Part II | *Not unique, not sharp, not beyond weak coupling; and Part II is a different question.* | Part II table, 0.35 pp | 1.25 | 250 + 180 |
| §9 | The record and how to check it | *Every import is pinned to a page of its source; nothing here has been refereed.* | — | 0.75 | 340 |
| App A | Pointer table (Tier 3) | — | table | 1.5 | — |
| App B | Notation | — | table, ≤ 25 symbols | 0.3 | — |
| refs | References | — | — | 0.4 | — |
| **total** | | | 6 figures ≈ 2.6 pp | **18.0** | slack 2.0 pp |

Every section closes with one line, *In the record:* followed by the numbers and pages it explained.

### §1 What is proved, and under what (Tier 1)
1. **Setting** (≤ 12 lines).
   - Q-space ℋ over the time-zero free field of mass m₀. 𝔄(O) is generated by Weyl operators W(f,h) with f, h ∈ C_c^∞(O); 𝔄 is the norm closure. The local algebras are the free ones; the interaction sits in the states and in α (§2.1, p. 6; A6, p. 9).
   - V(h), K(g), E(g), H(g) = K(g) − E(g), Ω_g, ω_g, β^g_t (§2.1, p. 6).
   - 𝒞_E on ℝ², 𝒞_H on ℝ, and 𝒢 ⊂ 𝒞_H, the plateau class, directed by inclusion of plateau interiors; O_r; d(g,O) (Def 2.1, p. 6).
   - The region 0 ≤ λ/m₀² < ε_P := λ_*/M_*², with M_*, λ_* source-admissible (§2.6, p. 13).
2. **Theorem 12.2 verbatim in a `recordbox`**: the clause "Assume U_GJS, namely Assumption A8(vi)" and items (1)–(5). The closing imports paragraph may be cut to its last sentence.
3. **The frozen U_GJS sentence.**
4. **"What is new" (T1.3):** convergence of the full unaveraged net, with a rate; canonical, not unique (Cor 12.3). The context sentence on GJ3 Thms 2.1 and 2.3 (GJ3 p. 211) is marked `context` and depends on the R5 re-check.
5. **Claims-ledger box**, four rows:
   - *Proved, conditional on U_GJS:* Thms 5.1, 7.8, 11.1, 12.2, 13.2; Lemmas 10.2, 10.3, 10.5; Props 10.4, 11.2; Cor 12.3.
   - *Proved, independent of A8:* Prop 2.7, Lemma 2.8, Lemma 4.4, Prop 8.1, Lemmas 9.1, 9.2.
   - *Implications under a stated hypothesis:* Prop 8.2, Lemma 9.3, Lemma 10.1 (under (G_γ), p. 22, which for P(φ)₂ only Thm 7.8 supplies); Prop 12.1 (for any sequence (g_n) in 𝒢 with d(g_n,O) → ∞ whose states converge in norm on every 𝔄(O)).
   - *Not claimed:* T1.5. *Open:* C5; Level 2 (not scheduled); Part II gate (II.11).
6. **One line on status words:** proved / partial / conjectured / numerical / refuted.

### §2 Why it was open
1. GJ3's construction: cutoffs g_n = g(·/n) with g ≡ 1 on [−3,3]; space-averaged states; a w\* limit point by compactness (record §1.1, p. 3; §1.4, p. 4; GJ3 (2.3)–(2.5), p. 210 as context).
2. The Expositions sentence that the g → 1 limit "has not been proved", quoted as the record quotes it (§1.1, p. 3). GRS Problems 1–2 and Newman's note (§1.1, p. 3; §14, p. 32).
3. **Table "GJ3 (context) vs the record"**, rows:
   - states: averaged ω_n vs unaveraged ω_g, g ∈ 𝒢;
   - limit: w\* limit point along a subsequence vs limit of the full net in every 𝔄(O)\*;
   - local norm: norm-compact in each local dual (GJ3 Thm 2.3) vs Cauchy, with rate Ψ_{m₁}(d) (Thm 11.1);
   - normality: limit points normal (GJ3 Thm 2.3) vs Prop 11.2;
   - energy: spectrum of H in [0,∞) (GJ3 Thm 2.1) vs ground state in the spectral sense (Prop 12.1);
   - selection: none vs every limit point equals ω_∞ (Cor 12.3; weak coupling; conditional on U_GJS).

   The GJ3 cells carry only what R5 confirms on GJ3 pp. 210–211; an unconfirmed cell is deleted, not reworded.
4. **Moments do not control norms.** GJS's own affine-path argument gives convergence of the cutoff Schwinger functions, with O(1)e^{−m₁d/2} for products of smeared fields ((1.1.11), as quoted in A8(vii′)(a), p. 10). The record states that "there is no soft passage from moments to norms on local von Neumann algebras" (§1.4, p. 4); quote it as the record's statement.
5. **Context, citing [Hastings], [BMNS] only as the record does:** the lattice machinery does not start, because V(g′) − V(g) has infinite norm (§1.4, p. 4).
6. AHZ and BDW (Euclidean uniqueness statements) and RZT (finite volume), as the record describes them (§1.1, p. 3). The record identifies no such theorem "in the references reviewed here"; this is not a priority claim.

### §3 The architecture (Tier 2, Fig. 1)
1. The two layers and the five steps of the §1.2 table (p. 3).
2. The four checkpoints: (M₂) (Thm 5.1, p. 16), (G) (Thm 7.8, p. 21), eq. (27) (Prop 10.4, p. 27) and eq. (31) (Thm 11.1, p. 28).
3. **Where each uniformity comes from** (from the record's proofs; locators required):
   - the g-independence of m₁ is CE2's printed h-independence (SF 2.2, p. 10; Lemma 7.4, p. 19);
   - in §7, U_GJS is used at one fixed g, uniformly in T (preamble of §7, p. 18; Lemmas 7.1–7.3);
   - U_GJS across g makes M independent of g, which Lemma 10.2 uses along g_s (p. 26).
4. §§8–11 use the GJS package only through m₁ and M: γ is instantiated as m₁ in §11 (p. 28), and Lemma 10.2 calls Thm 5.1.

### §4 The one import that is not a quotation (Tier 2, Fig. 2)
1. Display (U_GJS) verbatim (A8(vi), p. 10), then the frozen sentence.
2. **Why it is not literal.** Thm 1.1.8 is "stated uniformly as the source cutoff tends to one" (SF 2.3, p. 10; use this paraphrase, not the Scope paragraph's glyph). The proof needs T → ∞ at fixed g and moments uniform in g, and the slab cutoffs h_{T,g} do not tend to 1.
3. **The reading in three steps** (Scope paragraph (a)–(c), p. 11; (vii′), p. 10), each with its GJS pages, phrased as the record's reading.
4. **Consumers.** CE1 via U_GJS: Thm 5.1 and Lemmas 7.1–7.3. CE2: Lemma 7.4 only (Prop C.7, p. 38).
5. **App C.** It audits five source mechanisms (Prop C.1, p. 36, limited to them) and proves h-uniform normalisation and stability (Lemma C.2; Thm C.5, p. 38). It re-derives neither the expansion nor U_GJS, and Thm 12.2 does not consume it.
6. **C5 and the routes out.**
   - C5: nine items, all verdicts blank; a transcription check, so closing it leaves U_GJS a hypothesis (App B, p. 34).
   - Level 2 is the only proportionate route: an h-trace of the printed expansion on GJS pp. 598–629, completing Prop C.1. It is not scheduled (docs/imports.md).
   - The Hamiltonian bypass for (M₂) is recorded as dead: a verdict on the printed record, not a no-go theorem.
7. **Table A1–A7**, one row each: name, what it supplies (docs/imports.md table) and the source pinpoint (main.tex A1–A7, pp. 7–9).

### §5 Euclidean layer (Tier 2, Fig. 3)
Four pieces, described in full below, each ending at a `checkpoint` box:
- **I.** Slab FKN, eq. (2) (Lemma 4.1, p. 15); ψ̂_s → Ω_g by simplicity only (Lemma 4.4, p. 16). Isolation of E(g) is not imported (A1 Scope, p. 7).
- **II.** V(h)² is one GJS observable (A8(ii), p. 9). Support of length 2 gives 3 cells and 9 pairs, hence eq. (5). U_GJS at time 0 gives eq. (6); the closed graph passes the bound to Ω_g. Checkpoint: (M₂).
- **III.** Slab limits at fixed g (Lemmas 7.1–7.3); CE2 across a strip of width t − 2 (Lemma 7.4); checkpoint: Prop 7.5's bound.
- **IV.** Exponential moments, then density (Lemma 7.6, Thm 7.7), then the spectral theorem. Checkpoint: (G).
- One sentence: the slab limits use weak compactness in ℋ, and each limit is identified by a closed graph, so nothing is selected.

### §6 Hamiltonian layer (Tier 2, Figs. 4 and 5)
1. **Opening checkpoint (the contract):** the last sentence of Lemma 10.5 (p. 28), displayed verbatim: ‖(ω_g − ω_{g′})|𝔄(O)‖ ≤ Ψ_γ(d) whenever g ≡ g′ ≡ 1 on O_d, d ≥ 0. One sentence before it, in prose and without quotation marks, says that §§8–10 prove this for g, g′ ∈ 𝒢, every γ satisfying (G_γ), and M the moment constant of (M₂) (R34).
2. **Piece V.** g_s ∈ 𝒢 (Lemma 3.1(iii), p. 13); eq. (15) (Prop 8.2, p. 23); eq. (18) (Lemma 9.1(ii), p. 24). Checkpoint: eq. (24) (Lemma 10.1, p. 26).
3. **Piece VI.**
   - The exact light cone (Prop 2.7, p. 12): speed ≤ 1, uniform in g, from A6(i).
   - Spectral separation, eq. (19), then clustering with one unbounded argument, eq. (23), which needs ‖XΩ‖ and not ‖X‖ (Lemmas 9.2–9.3, p. 25).
   - Cells with ‖V_jΩ_s‖ ≤ M, eq. (25) (Lemma 10.2, p. 26).
4. **Piece VII.** The two-regime bound, eq. (26), with the wording of ruling R16 (Lemma 10.3, p. 27). The one-path estimate, eq. (27), with d₀ = 4 + 2/γ and at most eight cells per unit shell (Prop 10.4, p. 27).
5. **Rate.**
   - Eq. (29) and eq. (30) (Lemma 10.5, p. 28). Lemma 9.1(i) is credited only with W_γ ∈ L¹ and finite moments of every order, hence T_γ(r) ≤ C_{q,γ}(1+r)^{−q}.
   - The summands, with the wording of ruling R20.
   - "Not exponential" in the form of ruling R25 (§1.4, p. 5, as context). All constants depend on χ.
6. **`context` box (≤ 80 words):** no automorphism or spectral flow is constructed, and the machinery of [Hastings, BMNS] "does not start" (§1.4).

### §7 From Cauchy to the theorem (Tier 2, Fig. 6)
1. **Piece VIII.** Cauchy in each 𝔄(O)\* (Thm 11.1, Step 1, eq. (32)); completeness, compatible limits, a state (Step 2); the rate along a cofinal set. Checkpoint: eq. (31), p. 28.
2. **Normality.** Norm limits of normal vector states are normal (Prop 11.2, p. 29). This is how it is proved, not news (T1.3).
3. **The identity.**
   - α is imported (A6(ii), p. 9): a one-parameter automorphism group of 𝔄, independent of g, with (P). No continuity of α is imported or used.
   - Display: for |t| < d(g,O), ω_g(Aα_t(B)) = ⟨A\*Ω_g, e^{itH(g)}BΩ_g⟩ = ∫_{[0,∞)} e^{itE} dρ_g(E) (proof of Prop 12.1, p. 29).
   - Display the definition "ground state in the spectral sense" from the statement of Prop 12.1.
   - Norm convergence gives uniform convergence for |t| ≤ T.
4. **Invariances.** g ↦ τ_a g is an order isomorphism of 𝒢 with cofinal range; (T) (Lemma 2.8, p. 12); parity likewise (proof of Thm 12.2, p. 30).
5. **Cor 12.3, p. 31:** every w\* limit point of GJ3's averaged or unaveraged states equals ω_∞ on each 𝔄(O), "its proof takes GJ3's cutoff function g in 𝒢". Canonical, not unique.

### §8 Boundaries, and Part II
- **§8.1 (250 words): the record's own reasons.**
  - (a) Uniqueness: §1.3(a), p. 4; §14, p. 33.
  - (b) Sharp rate: §14, p. 33, "an additional resolvent or Combes–Thomas input not supplied here"; the quadratic model in the wording of ruling R21.
  - (c) Beyond weak coupling: Thm 13.2 is conditional on Hyp 13.1, with all four hypotheses load-bearing; the wording of ruling R23; Rem 13.3, p. 32.
  - (d) Not addressed: a gap of a GNS Hamiltonian of ω_∞; identification with the Euclidean (Wightman) theory; Lorentz covariance.
- **§8.2 Part II:** the text given in Part 6.3 (trimmed from cqft's section P), and the docs/status.md table verbatim.

### §9 The record and how to check it
- The AI-assisted method (README, "What this is").
- Gates G0–G6, one line each, from the docs/status.md table.
- The adversarial passes, "which the README says the assistant ran".
- Corrections that changed statements, from App B, p. 34, and the README:
  - audit P1, which led to Hyp 13.1 with (B4);
  - S1–S3 (citation pinpoints);
  - L1–L6;
  - R2 (printed-norm prefactor);
  - the 5 September 2026 scope amendment (status re-based; no proof changed).
- C5 open.
- How to check: `% src:` comments; the citation dossier (page images not redistributed, with a render script); numbers resolved from `main.aux`.

---

## 3. Figures (six; final)

The orchestrator builds all six in TikZ/pgfplots with `companion/preamble.tex`.
- **Colours:** `cond` (#8250df) only for what is conditional on U_GJS; `gline`/`mut` for imports and guides; `acc`/`warn`/`ok` as in the drafts.
- **Captions:** every caption states what is drawn and what is computed, and ends with **"Illustration, not evidence."**
- **Numbering:** companion figures are numbered 1–6, in the order of first reference.

### Fig. 1: the two-layer spine (F1; §3; 0.5 pp)
- **Purpose:** the one picture to retain (T1.4, T2.0): where the import enters, what flows across the interface, and what each item of Thm 12.2 costs.
- **Drawn:**
  - Five bands, top to bottom: inputs; layer E (§§4–7); an interface strip; layer H (§§8–11); identification (§12).
  - **Inputs:** a grey box "A1–A7 (literal imports)"; a grey box "CE2, printed (A8(iv), SF 2.2)"; a dashed `cond` box "U_GJS (A8(vi))".
  - **Layer E:** Lemma 4.4; Thm 5.1 (M₂); Thm 7.8 (G).
  - **Interface:** "(G_γ), γ = m₁" and "M".
  - **Layer H:** Prop 2.7; Prop 8.2; Lemma 9.1; Lemma 9.3; Lemma 10.1; Lemma 10.3; Prop 10.4; Lemma 10.5; Thm 11.1.
  - **Identification:** Prop 11.2; Prop 12.1; Lemma 2.8; Thm 12.2 with items (1)–(5); Cor 12.3.
- **Node classes** (by hand from the proofs, as in the App A column):
  - `cond` fill: Thms 5.1, 7.8, 11.1, 12.2; Lemmas 10.3, 10.5; Props 10.4, 11.2; Cor 12.3.
  - `cond` outline on white, tag "under (G_γ)": Prop 8.2, Lemmas 9.3, 10.1.
  - `cond` outline, tag "any norm limit": Prop 12.1.
  - grey (independent of A8): Prop 2.7, Lemma 2.8, Lemma 4.4, Lemma 9.1.
- **Edge labels** (short):
  - CE2 → Thm 7.8: "m₁ independent of h".
  - U_GJS → Thm 7.8: "fixed g, uniform in T".
  - U_GJS → Thm 5.1: "uniform in g and T".
  - Thm 7.8 → interface: "γ = m₁ (§11)".
  - Thm 5.1 → Lemma 10.3: "M (via Lemma 10.2)".
  - Prop 2.7 → Lemma 9.3: "exact cone".
  - A1 → Lemma 4.4 and Prop 8.2: "simplicity".
  - A6 → Prop 2.7 and Prop 12.1: "(P)".
  - Items of Thm 12.2: (1) "estimate, Thm 11.1"; (2) "normal limits, Prop 11.2"; (3) "identity (P), Prop 12.1"; (4) "order isomorphism + (T)"; (5) "restates Thms 7.8, 5.1".
- **Computed:** nothing.
- **Source:** §1.2 table, p. 3; the proofs named on each node.
- **Caption, mandatory sentences:**
  - "Shading records what each proof consumes, read from the record's proofs: violet fill, conditional on U_GJS; violet outline, an implication under a hypothesis that for P(φ)₂ only a violet node supplies; grey, independent of A8."
  - "No arrow from Appendix C closes the dashed box."
  - "Illustration, not evidence."
- **Must not suggest:** that the record proves CE2 or U_GJS; that grey nodes make any item of Thm 12.2 unconditional; that the five items share one provenance. It shows no count of conditional statements.

### Fig. 2: "two affine paths, one quantifier" (E1, merged with cqft E-b; §4; 0.4 pp)
- **Purpose:** T2.1. What the source says, what the record imports, and what is missing.
- **Drawn, left (geometry):**
  - Top: two arbitrary cutoffs h₁, h₂ in the (x¹, x⁰) plane (compact support, 0 ≤ h ≤ 1) and the path h₁ + α(h₂ − h₁). Label: "GJS pp. 594–595: Thm 1.1.7 applied at every cutoff of the path, one constant (quoted in A8(vii′)(a))".
  - Bottom: the slab cutoffs h_{T,g}, h_{T,g′} and the path h_{T,g_s} = (1−s)h_{T,g} + s·h_{T,g′}. Label: "the same family, h₁ = h_{T,g}, h₂ = h_{T,g′}, α = s (A8 Scope (a), p. 11); CE1 used at every slab cutoff: Thm 5.1, Lemmas 7.1–7.3".
- **Drawn, right (logic):** three grey boxes with arrows into a dashed `cond` box.
  - (a) "pp. 594–595: Thm 1.1.7 at every cutoff of an affine path".
  - (b) "pp. 596–597: 1.1.7's h-independent constant taken from 1.1.8 at the same h; (1.1.16) 'uniformly in h'".
  - (c) "p. 629: Thms 1.1.8, 1.1.11, 3.1, 4.1 'uniform in the space cutoff h'; 1.1.8 is the case B = I, n = 0".
  - The dashed `cond` box: "U_GJS: one C₈ for all h_{T,g}, T > 0, g ∈ 𝒞_H — imported at the source's scope, not re-derived".
  - A grey note under it: "as stated, Thm 1.1.8 holds uniformly as the source cutoff tends to one (SF 2.3)".
  - A grey box "App C: mechanism audit + two prerequisites", with no arrow into the dashed box.
  - Quotation marks only around the two phrases that main.tex itself quotes ((vii′)(b), SF 2.4). All other labels are paraphrases.
- **Computed:** nothing. No page images.
- **Source:** A8(vi), (vii′), Scope paragraph, pp. 10–11; SF 2.3–2.4, p. 10; Prop C.7, p. 38.
- **Caption, mandatory sentences:**
  - "The source states this quantifier (p. 629) and uses it (pp. 594–597); the record imports it at that scope and does not re-derive it, so U_GJS remains a named hypothesis of Theorem 12.2."
  - "Audit item C5, a second human reading of these pages, is open."
  - "Illustration, not evidence."
- **Must not suggest:** a proof; that GJS state U_GJS in a single theorem; that App C closes the gap; that the spacetime cutoff h is the spatial cutoff g; that the Euclidean bound (1.1.11) implies the Hamiltonian one.

### Fig. 3: slab transfer, and the gap as an output (F5, merged with cqft E-c; §5; 0.4 pp)
- **Purpose:** T2.2. The Euclidean–Hamiltonian bridge at fixed g, and why there is no circularity.
- **Drawn:** `companion/figures/fig-slab.tex`, amended in three ways.
  - (i) Move the sharp-time rows to x⁰ = ±t/2 with t/2 = 2, inside half-width T = 3, as Lemma 7.3 needs T ≥ t/2. Shade the strip |x⁰| < t/2 − 1 and label it "CE2 across this strip, width t − 2 (Lemma 7.4)".
  - (ii) Keep the three boxes: Euclidean side; Hamiltonian side, eq. (2), "all limits at fixed g"; and T → ∞, "Lemma 4.4: simplicity only, no gap assumed".
  - (iii) Add a fourth box, `cond` fill (conditional on U_GJS through Lemmas 7.1–7.3): "Prop 7.5: ⟨ψ_Q, e^{−tH(g)}ψ_Q⟩ ≤ Ĉ_Q e^{−m₁t}; with density (Thm 7.7): (G) spec H(g) ⊆ {0} ∪ [m₁,∞) (Thm 7.8) — an output".
- **Computed:** nothing.
- **Source:** Lemma 4.1, eq. (2), p. 15; Lemma 4.4, p. 16; Lemma 7.4, p. 19; Prop 7.5, p. 20; Thm 7.8, p. 21.
- **Caption, mandatory sentences:**
  - "Every limit T → ∞ is taken at fixed g, and no gap is assumed: the gap of Theorem 7.8 is the output of this picture."
  - "Working coordinates; lengths are not physical."
  - "Illustration, not evidence."
- **Must not suggest:** an assumed gap; an infinite-volume measure; a T-limit that is uniform in g.

### Fig. 4: the derivative along the path (F2+F4; §6; 0.6 pp; three panels)
- **Purpose:** T2.3, the engine.
- **Panel (a), top:** `fig-moves.tex`, with one wording fix: in box (2), "speed one" becomes "speed ≤ 1 for every g ∈ 𝒞_H".
- **Panel (b), bottom left:** `fig-path.tex`, amended.
  - Draw each cell as supp(η_jv) = (j−1, j+1) ∩ supp v, i.e. clipped to where v ≠ 0. No bar may enter O_d: in the draft, the bar for j = 6 overlaps O_d. Draw every nonzero cell; the draft omits j = ±12.
  - Add unit-shell ticks at distances d, d+1, d+2, … from O on each side, labelled "≤ 4 cells per shell per side (Prop 10.4, Step 3)".
  - Annotate "V(v): unbounded, not small; only V_jΩ_s enters (Lemma 10.2)" and "plateau of g_s ⊇ {g=1}° ∩ {g′=1}° (Lemma 3.1(iii))".
- **Panel (c), bottom right:** `fig-two-regime.tex`, amended.
  - Mark |t| = r_j, where the cone edge meets B_j.
  - Label the band r_j/2 < |t| < r_j "B_j still outside the cone; the lemma uses 2M here by choice".
  - Replace "only the trivial bound" with "Lemma 10.3 uses only the trivial bound 2M".
  - Label the cone "exact, speed ≤ 1 (Prop 2.7)".
- **Computed:** nothing.
- **Source:** Lemma 10.1, eq. (24), p. 26; Prop 10.4, Step 2, p. 27; Lemma 9.1, p. 24; Prop 2.7, p. 12; Lemmas 9.3 and 10.3, pp. 25–27; Lemma 3.1(iii), p. 13; Lemma 10.2, p. 26.
- **Caption, mandatory sentences:**
  - "The switch at |t| = r_j/2 is a switch of the bound, not of the correlation; the cone reaches B_j only at |t| = r_j."
  - "No automorphism or spectral flow is constructed: the derivative of the state is bounded and integrated along the path."
  - "Illustration, not evidence."
- **Must not suggest:** a small or bounded perturbation; Lieb–Robinson-type approximate locality; s as a physical time; that B_j enters the cone at r_j/2; equal or measured contributions of the cells.

### Fig. 5: filter, tail, rate (F3+F6; §6; 0.4 pp; three computed panels)
- **Purpose:** T2.4. What is proved about the filter, and why the rate is super-polynomial but not exponential.
- **Panel (a):** Ŵ_γ(E) = χ(E)/E from `hatW_g1.dat`. Mark the notch [−γ/2, γ/2]; shade spec H(g) ⊆ {0} ∪ [γ,∞) under the axis; label "Ŵ_γ(E) = 1/E on [γ,∞); the notch on [−γ/2, γ/2] is part of the construction (17)".
- **Panel (b):** T_γ(r) = ∫_{|t|>r}|W_γ(t)|dt at γ = 1, log-y axis, no reference powers. The data is a new table `tail_g1.dat` (columns `r T`), written by `companion/figures/make_tables.py` from `make_figures.filter_curves(1.0)`. That is the site's own function, on its full grid, with the same trapezoid rule as its `T`.
- **Panel (c):** the summands `exp` and `tail` of `psi_g1.dat` (γ = 1, M = 1), log-y, d ∈ [0, 60]. Draw a vertical line at d₀ = 6 and a horizontal line at 2, labelled "trivial bound".
- **Computed:** all three panels, by `docs/figures/make_figures.py` through `companion/figures/make_tables.py`.
- **Source:** Lemma 9.1 (17)–(18), p. 24; Lemma 10.5 (29)–(30), p. 28.
- **Caption, mandatory sentences:**
  1. "Computed by docs/figures/make_figures.py for one admissible χ, γ = 1 and M = 1, on a time grid up to t ≈ 159, with values of |W_γ| below 10⁻⁹ set to zero."
  2. "Lemma 9.1(i) proves only that W_γ ∈ L¹ with finite moments of every order, hence T_γ(r) ≤ C_{q,γ}(1+r)^{−q}; the curves are numerical and claim no decay law."
  3. "Ψ_γ is an upper bound on ‖(ω_g − ω_{g′})|𝔄(O)‖, never a measured decay of any state; M = 1 is a placeholder, not the record's M, which depends on unquantified GJS constants."
  4. "At these values Ψ_γ(d) exceeds the trivial bound 2 at every d shown: the content is the decay in d, not the size at any d." (checked: Ψ_γ(60) ≈ 11.7 in `psi_g1.dat`)
  5. "Both summands decay faster than every inverse power; the exponential summand decays faster, so the filter-tail summand sets the rate."
  6. "Illustration, not evidence."
- **Must not suggest:** a slope or decay law; meaningful heights; the README's "exponential-then-stuck" reading; that the bound is useful at d ≤ 60 for these values.

### Fig. 6: the identity window (aqft E1; §7; 0.3 pp)
- **Purpose:** T2.5. Why the ground-state property costs an identity.
- **Drawn:**
  - The (x, t)-plane with the plateau interior {g=1}° on the axis t = 0, O inside it, and the cone O_{|t|}.
  - The band |t| < d(g,O), shaded, labelled "α_t(A) = β^g_t(A) for A ∈ 𝔄(O) (patching (P), A6)".
  - An inset: ω_g(Aα_t(B)) = ⟨A\*Ω_g, e^{itH(g)}BΩ_g⟩ = ∫_{[0,∞)} e^{itE} dρ_g(E) on that band.
- **Computed:** nothing.
- **Source:** A6, eq. (P), p. 9; proof of Prop 12.1, p. 29.
- **Caption, mandatory sentences:**
  - "Inside the window the spectral condition is an identity at each cutoff; norm convergence on each 𝔄(O_T) carries it to ω_∞ (Proposition 12.1)."
  - "α is Glimm–Jaffe's patched dynamics, imported in A6(ii); the record does not construct it."
  - "Illustration, not evidence."
- **Must not suggest:** that ω_g is α-invariant; an estimate; a GNS Hamiltonian of ω_∞; anything about the window |t| ≤ r_j/2 of Fig. 4 (it is a different window).

**Dropped:**
- **F7 (status map):** see ruling R7. Its content goes to Fig. 1's shading, the App A column, and the §8.2 table.
- **qi Q3 (zoom on where U_GJS enters):** folded into Fig. 1's labels.
- **aqft E3 (limit point versus limit):** becomes the §2 table.
- **The README's five SVGs:** not reused as images. Fig. 1 replaces the import graph, Fig. 4(c) the light cone and Fig. 5 the rate figure. The plateau-net and uniform-gap pictures are not reproduced; Def 2.1 and Thm 7.8 are stated in the text.

---

## 4. Editorial rules (final; enforced in R4)

### Structure and pacing
1. **Three-step rule.** No paragraph may make more than three inferential steps without a displayed checkpoint. A checkpoint is a `checkpoint` or `recordbox` transcribed from main.tex and carrying `\rec{number}{page}`.
2. **Openings and closings.** Every section opens with its sentence to retain (italic, ≤ 30 words, as in Part 2) and closes with one line, *In the record:*, listing the numbers and pages it explained.
3. **Figures.** There are six: Fig. 1 for the architecture, and one for each Tier-2 idea. No other figure, and no table that restates a figure. Captions carry the mandatory sentences of Part 3 verbatim and end "Illustration, not evidence." `cond` violet marks only what is conditional on U_GJS.

### Status and wording
4. **References.** Forward references go only to numbered statements of the record, written `\rec{Theorem~12.2}{30}`. The companion numbers only its own sections, figures, tables and displays.
5. **Status words** come only from proved / partial / conjectured / numerical / refuted.
   - Theorem 12.2 is "proved, conditional on U_GJS", never "proved" bare.
   - In each section, the first mention of any statement of class U in App A carries "conditional on U_GJS". Class U includes Thms 5.1, 7.8, 11.1, 12.2 and 13.2, Props 10.4 and 11.2, Lemma 10.5, Cor 12.3 and Lemmas 7.1–7.3.
   - Prop 8.2, Lemma 9.3 and Lemma 10.1 are described as implications under (G_γ).
6. **U_GJS wording.** The first description of U_GJS in any section is the frozen sentence at the top of this PLAN, verbatim, nothing stronger or weaker. Later mentions may say "U_GJS (A8(vi))".
7. **No new mathematics.** No new proof, constant, strengthening or comparison of rates.
   - Contextual remarks go in the `context` environment and cite only the `\bibitem`s of main.tex, or record files by path.
   - Facts about GJ3 or GJS that main.tex does not itself state appear only in `context`, and only after R5 confirms them at the page.
8. **Numbers.** Theorem, lemma, equation and section numbers and pages come only from `companion/council/labels.md`. Unlabelled places carry the printed pages of Part 1. Quotation marks enclose only verbatim text of main.tex or of the named file.
9. **Fixed phrasings:**
   - "ground state" always comes with "in the spectral sense (Prop 12.1)", also when Hyp 13.1 is described;
   - "converges in norm" always comes with "on every local algebra 𝔄(O)" or "in each 𝔄(O)\*";
   - item (5) always refers to "the cutoff Hamiltonians H(g), g ∈ 𝒞_H";
   - items (1)–(4) are statements along 𝒢 (𝟙_{[−L,L]} lies in 𝒞_H but not in 𝒢);
   - the symbol m₁ denotes only the GJS constant.
10. **Banned words and phrases** (R4 greps for them):
    - unique vacuum; the vacuum (unqualified: write ω_∞); mass gap of the limit; gapped limit; exponential rate; exponential convergence; exponential clustering of ω_∞;
    - unconditional; verified; independently verified; first; solves; settles; strongest;
    - compactness-free; no compactness anywhere; purely Hamiltonian;
    - spectral flow, quasi-adiabatic continuation, automorphic equivalence (allowed only in the §6 `context` box, as what is *not* done);
    - "Lieb–Robinson bound" (allowed only as "no Lieb–Robinson bound is needed");
    - norm-convergent Bochner integral; true rate; exponential-then-stuck; the cone swallows; only the trivial bound survives;
    - clearly; obviously; standard (unless what follows is immediate).

### Weight, notation, sources
11. **Budgets are hard.** An overrun is cut from §§5–6. §§1, 4 and 8 are never cut.
12. **Notation** follows main.tex §2.3 (p. 7). App B lists at most 25 symbols, each defined before its first use.
13. **Sources** are phrased as the record's quotations ("GJS p. 629, as quoted in Source Fact 2.4"). The companion does not vouch for any transcription (C5).
14. **Findings stay out.** Anything wrong or unclear in the record goes to the findings register (Part 7) and never into the companion's text. Where a record sentence is the subject of a finding, the companion paraphrases the record's mathematics, without the faulty phrase and without comment.

---

## 5. Disagreement register (38 rulings)

"ed" is the editor's R1 memo. Each row gives the positions, the ruling and one reason. Items marked *verified* were re-checked at the source by the orchestrator (Part 7).

### Tiering and weighting

| # | point | positions | ruling | reason |
|---|---|---|---|---|
| R1 | Tier 1: what is new | ed M.1 counted "norm on local duals" as news. aqft A2: the news is convergence; GJ3 Thm 2.3 already has norm compactness and normal limit points, and Thm 2.1 positive energy. | T1.3 follows aqft; the GJ3 facts appear as context, after R5. | It keeps the companion from crediting the record with GJ3's results. The editor rendered GJ3 p. 211 in R2, and aqft's quotations match. |
| R2 | Tier 1: the inputs | ed A3 (two layers); qi A3 (two numbers); cqft A4; aqft A3 (cut view) | T1.4 merges them: two layers joined by m₁ and M; §§8–11 use A8 only through them. | The content is the same; "two numbers" is the form a reader keeps. |
| R3 | Tier 1: the engine | ed A4 (two exact ingredients); qi A2 (derivative form, no spectral flow) | T1.4 adds "no automorphism or spectral flow is constructed". | It pre-empts the QI misreading at no cost. |
| R4 | Tier of "costs an identity" | aqft A5: Tier 1. ed B6: should know. | Tier 2 (§7, Fig. 6). The qualifier "in the spectral sense" stays Tier 1 (T1.1). | Tier 1 holds claims; the identity is a mechanism. |
| R5 | weight of Part II | cqft P ≈ 1 p; ed ≤ ½ p | 0.75 p: trimmed P (≤ 180 words) plus the verbatim table. | The table needs 0.35 p, and nothing in Part I depends on Part II. |
| R6 | weight of §4 | ed 1.5 p | 2.0 p | U_GJS is the first question of cqft (H), of the editor (K1) and of the sceptic. |
| R30 | pointer-table membership | aqft sends Lemmas 7.1–7.4 and 9.2 to Tier 3; cqft sends Lemmas 10.1–10.2, Prop 11.2 and the proof of Cor 12.3; qi sends Prop 11.2. | Statements that are checkpoints or carry an import stay in the body (Lemma 7.4, eq. (24), Prop 11.2, Cor 12.3); their proofs go to App A. | The body needs every checkpoint and every place an import enters. |
| R31 | where U_GJS enters (G) | ed: Thm 5.1 and Lemmas 7.1–7.3. cqft B2: in §7 at fixed g, uniformly in T; the g-independence of m₁ comes from CE2; across g, U_GJS is needed only for M. | cqft's refinement is adopted in §3 and in Fig. 1's labels. | It is checkable in main.tex (§7 preamble, p. 18; Lemma 7.4; Lemma 10.2). |
| R34 | how §6 opens | ed: sentence to retain only. qi: open with the "contract". | Both: the sentence to retain, then the contract as the opening checkpoint. | The contract is the best checkpoint for the layer. |
| R36 | abstract and notice | only the editor drafted them | Final wording in Part 6 (O1). The abstract leads with "converges … with a rate" (R1). | No conflict. |

### Figures

| # | point | positions | ruling | reason |
|---|---|---|---|---|
| R7 | F7 status map | aqft keep/change; qi keep/change; cqft change (spine only, or an exact caption); ed drop | Dropped. Its content goes into Fig. 1's classes, the App A column and the §8.2 table. | Three members found artefacts in the computed count (Part 7, F1), and 61 nodes is bookkeeping. |
| R8 | rule for colouring Fig. 1 | aqft: compute from results.json. cqft: whole spine violet, with 9.1 and 2.7 neutral. qi: hatch 8.2, 9.3, 10.1 and 12.1. ed: neutral, with labels. | Three classes by hand (fill / outline with a tag / grey), checked by R5 against main.tex. | The flag in results.json is unreliable. The outline class is true both for P(φ)₂ (qi) and for the implications as stated (aqft). |
| R9 | labels in Fig. 1 | cqft E-a (types of uniformity); qi (what flows); aqft E2 (what each item costs) | All three, on different edges. | Each answers a different reader; they do not conflict. |
| R10 | content of E1 | ed: geometry of the two paths. cqft E-b: the logic of the evidence. qi Q1: old versus new (Schwinger functions versus norms). | Fig. 2 has ed's geometry on the left and cqft's logic on the right; qi's contrast goes into the §2 text. | The figure's job is the scope argument; the old/new contrast is a second idea. |
| R11 | qi Q3 (zoom) | proposed as an inset | Folded into Fig. 1's labels. | Same content, no budget needed. |
| R12 | F2 and F4 | ed: merge. aqft and qi: keep F2, with labels. qi Q2: shells. The orchestrator: the moves panel exists. | Fig. 4 in three panels: moves; path with cells clipped and shells; two regimes. | One Tier-2 idea gets one figure. In the draft, the cell bar for j = 6 crosses O_d. |
| R13 | Fig. 5, panel (b) | ed and site: \|W_γ(t)\| on log-log axes. qi: T_γ(r). | T_γ(r). | It is what Lemma 9.1(i) bounds and what Ψ uses, and it sidesteps the withdrawn claims about the kernel's shape. |
| R14 | reference powers in Fig. 5 | qi: guides labelled "constants arbitrary". cqft: no slope numbers. Site: t⁻² and t⁻⁶ anchored on the envelope. | No guides. | The record withdrew its slope claims (*verified*: the description of rate.svg), and guides invite slope reading. |
| R15 | trivial bound in Fig. 5(c) | aqft: mark d₀ and 2; the others are silent | Draw d₀ and the line 2; add mandatory sentence 4. | At γ = M = 1 the computed Ψ exceeds 2 for every d ≤ 60 (psi_g1.dat: Ψ(60) ≈ 11.7), so the bare panel oversells. |
| R17 | F5 versus cqft E-c | cqft: replace F5. ed: simplify. aqft, qi: keep. | Fig. 3 is fig-slab.tex plus E-c's strip and the "(G) as output" box. | This keeps the drafted bridge and adds where CE2 enters. |
| R18 | identity window (aqft E1) | aqft: as the right panel of F4. ed R1: no figure for §7. | A separate Fig. 6 (0.3 p). | T2.5 needs its own figure; inside F4, the window \|t\| < d(g,O) would blur into \|t\| ≤ r_j/2. |
| R19 | aqft E3 (limit point versus limit) | proposed as a figure | A table in §2. | A comparison of statements is more exact as a table. |
| R37 | Fig. 2 must not equate h and g | qi Q1, "must not suggest" | Adopted. | The spacetime cutoff h is not the spatial cutoff g. |

### Wording

| # | point | positions | ruling | reason |
|---|---|---|---|---|
| R16 | two-regime wording (qi G7) | README and make_figures: "past that time only the trivial bound survives", "the cone has swallowed the gap". qi: the cone reaches B_j only at r_j. | "For \|t\| ≤ r_j/2 the cell stays at distance ≥ r_j/2 from O_{\|t\|}; beyond that, Lemma 10.3 uses only the trivial bound 2M (by choice; the cone reaches B_j at \|t\| = r_j)." | This matches the proof of Lemma 10.3 (p. 27) and Prop 2.7. |
| R20 | Ψ-summand wording (qi G6) | README: the filter tail "makes the rate super-polynomial rather than merely exponential-then-stuck". qi: the roles are reversed. | "Both summands decay faster than every inverse power; the exponential summand decays faster, so the filter-tail summand sets the rate." | The README sentence is wrong (*verified*). Lemma 10.5 bounds both summands. |
| R21 | m₁ clash with m2/ (qi G2) | main.tex §1.3(b) and §14: "true rate poly(d)e^{−2m₁d}". m2/m2.tex: m₁² := m₀² + λ, and the result is a proof sketch. | "The record reports, from its working note m2/ (a proof sketch with numerics, outside the document of record), that in the exactly solvable quadratic model the rate is poly(d)e^{−2md}, with m that model's mass." Never write m₁ for it, never "true rate". | *verified*. It avoids comparing two different masses. |
| R22 | GJ3 Thm 2.3 and normality (aqft G1) | The record (§§1.1, 1.4) leaves topology and normality implicitly to Thm 12.2. aqft: GJ3 Thm 2.3 already has them. | T1.3 and the §2 table state GJ3's results as context. §7 presents normality as how Prop 11.2 is proved, not as news. | The editor rendered GJ3 p. 211: Thm 2.1 and Thm 2.3 read as aqft quotes. R5 re-checks before printing. |
| R23 | §13 depends on Thm 12.2 (cqft G6; the coordinator's message calls it G4) | Record §1.3(c) and the opening of §13: "a cutoff-uniform gap is incompatible with that two-phase structure". cqft: the proof also uses Thm 12.2 (1), (3), (4). | "For even 𝒫 at weak coupling, (B1)–(B4) cannot all hold; the proof uses the uniform gap through Lemma 9.3 and Theorem 12.2 (1), (3), (4), hence also (M₂) and U_GJS." | *verified* at lines 2445–2454. |
| R24 | "uniformly as h → 1" (cqft A2, G1) | The Scope paragraph quotes "h↑1"; the source and C5 item 5 have "h → 1"; the frozen sentence is silent. | §4 may say that Thm 1.1.8 is "stated uniformly as the source cutoff tends to one" (SF 2.3), outside the frozen sentence. | This is why U_GJS is a named hypothesis, and SF 2.3 is glyph-free. |
| R25 | wording of the filter obstruction | Record §1.4: "as Ŵ_γ must … intrinsic to the method". ed G5 and qi G1: "must" is not forced by (18). aqft: move the remark to §8. | In §6: W_γ cannot have exponential tails, because Ŵ_γ vanishes on [−γ/2, γ/2] by construction and a transform analytic in a strip cannot vanish on an interval without vanishing identically. Report "intrinsic to the filter method" as the record's statement, adding no argument. | The restricted statement is fully supported. The general one needs a variant the record lacks. §6 is where the filter is. |
| R26 | "norm-convergent Bochner integral" (qi G4) | Lemma 9.1(ii) says so; qi: the integral is only strongly convergent. | Describe (18) as an integral identity applied to vectors, without "norm-convergent". | The phrase is under a finding, and Lemma 10.1 needs (18) on one vector only. |
| R27 | wording of Level 2 (cqft G7) | docs: "display-by-display trace … pp. 598–629". cqft: p. 628 omits a step. | "An h-trace of the printed expansion on GJS pp. 598–629, completing Prop C.1 (not scheduled)." | It drops the questioned adjective without adjudicating. |
| R28 | GJS p. 590 slab family (cqft G8) | cqft: an optional addition to the record | Not in the companion; it goes to the author. | The companion must not add evidence the record does not use. |
| R29 | longest chain and its cut | aqft: 14 statements, 9 pieces. qi: 12 or 15, 9 pieces. cqft: 12, 8 pieces. ed: 21 steps, 8 pieces. | ed's 8 pieces, plus the identification as a separate two-step branch. | All four cuts end at the same checkpoints. |
| R32 | "ground state" without qualifier (aqft G3) | The record uses it unqualified in Hyp 13.1, §1.3(a) and §14. | Rule 9. | Prop 12.1 holds the record's only definition. |
| R33 | Lorentz covariance; a GNS gap | not in the record's negative list | Listed in §8.1(d) as "not addressed". | A grep of main.tex finds no "Lorentz", "Poincaré" or "Haag"; this prevents the AQFT overreading. |
| R35 | "the proof is Hamiltonian" (cqft trap) | Record abstract: "The proof is Hamiltonian". cqft: only the Cauchy argument is. | "The convergence argument is Hamiltonian; its two inputs come from Euclidean estimates through slab FKN transfer." | This is exact to the table in §1.2. |
| R38 | dependence on χ (qi G9) | The record suppresses χ in C_{q,γ}, C_{N,γ,M} and Ψ_γ. | §6 says once: "these constants, and Ψ_γ itself, depend on the fixed choice of χ". | True by (17) and (29), and not a correction of the record. |

---

## 6. Drafting assignments for R3

### 6.0 Conventions for every drafter
- **Files.**
  - Write only your own files under `companion/sections/`. Each is a LaTeX fragment with no preamble, starting with its `\section{…}` (or `\subsection{…}`, as given), compiled inside `companion/companion.tex` with `companion/preamble.tex`.
  - You may read any file of the repository. You edit nothing else, run no `git` or `kb` command, and build nothing; the orchestrator builds.
- **Macros** (from the preamble):
  - `\rec{Theorem~12.2}{30}` for every locator;
  - `\UGJS` for U_GJS;
  - `\condtext{…}` for the words "conditional on U_GJS" at their first occurrence in a section;
  - the environments `recordbox` (verbatim statements of the record), `checkpoint` (end of a chain) and `context` (contextual remarks);
  - figures as `Fig.~\ref{fig:spine}`, `fig:quantifier`, `fig:slab`, `fig:lppl`, `fig:rate`, `fig:window` (Figs. 1–6 of Part 3).
- **Sources of facts.**
  - Mathematics: only from `part_i/main.tex`, with numbers and pages from `companion/council/labels.md` and, for unlabelled places, the printed pages of Part 2.
  - Status facts about the record: only from the files named in your assignment.
  - GJ3 facts: only the sentences marked "(R5)" below. If R5 does not confirm one, it is deleted.
- **Rules.** Part 4 binds every sentence: the three-step rule, the frozen U_GJS sentence, status words, banned words, and findings that stay out.
- **Budgets.** Word budgets are targets of ±10 % for prose, boxes included. Tables are budgeted in pages. Exceed a budget only by taking the words from your own other section.
- **Return.** Each file, plus a list of every locator used and every verbatim quotation with its main.tex line number. R4 and R5 check these lists.

### 6.1 `aqft`: §1, §2, §7, §8.1 (≈ 2010 words)

**§1 What is proved, and under what.** File `s1-result.tex`; 900 words including two boxes; no figure, one forward pointer to Fig. 1.
- Open with the sentence to retain from Part 2.
- Then the five numbered items of Part 2 §1, in that order:
  - the setting, ≤ 12 lines;
  - Thm 12.2 in a `recordbox` titled "Theorem 12.2 of the record (p. 30)", verbatim from main.tex lines 2291–2326, with the imports paragraph cut to its last sentence;
  - the frozen U_GJS sentence;
  - "What is new", using T1.3 and the (R5) context sentence: *"In GJ3, the averaged states of [GJ3, (2.4)] lie, on each local algebra, in a norm-compact subset of the local dual, and their limit points are normal [GJ3, Thm 2.3, p. 211]; in the representation of any w\* limit point, the generator of time translations has spectrum in [0, ∞) [GJ3, Thm 2.1, p. 211]."*;
  - the claims-ledger box, exactly the four rows of Part 2 §1.5.
- Must include the T1.5 negatives in one sentence, pointing to §8.
- Must not include a count of conditional statements (R7).

**§2 Why it was open.** File `s2-open.tex`; 430 words plus the table (0.3 pp).
- Items 1–6 of Part 2 §2.
- The table has three columns: property; GJ3 (context; every cell (R5)); the record (with locators).
- Use ruling R1. The phrase "no soft passage from moments to norms" is quoted from main.tex lines 266–267.
- Hastings and BMNS are cited only inside `context`.

**§7 From Cauchy to the theorem.** File `s7-identification.tex`; 430 words; Fig. 6.
- Items 1–5 of Part 2 §7. Display the spectral definition from the statement of Prop 12.1, verbatim.
- Display the identity from the proof of Prop 12.1 (p. 29), verbatim except for spacing.
- Cor 12.3 with the clause "its proof takes GJ3's cutoff function g in 𝒢".
- Rulings R4, R22, R32. Normality is "how Prop 11.2 is proved", not news.

**§8.1 What is not claimed.** File `s8a-boundaries.tex` (`\section{Boundaries, and Part II}` plus `\subsection{What is not claimed}`); 250 words.
- Items (a)–(d) of Part 2 §8, with rulings R21 (the quadratic-model wording, verbatim), R23 (the Thm 13.2 wording, verbatim) and R33.
- For (b), quote §14's "an additional resolvent or Combes–Thomas input not supplied here" (main.tex lines 2512–2513).

### 6.2 `qi`: §3, §6, §9 (≈ 1670 words)

**§3 The architecture.** File `s3-architecture.tex`; 450 words; Fig. 1.
- Items 1–4 of Part 2 §3.
- Explain the three node classes of Fig. 1 in two sentences, using the legend wording of Part 3, Fig. 1.
- The uniformity sentences of R31 come with their three locators.
- End at the checkpoint (31) (Thm 11.1, p. 28), quoted as "‖(ω_g − ω_∞)|𝔄(O)‖ ≤ Ψ_{m₁}(d) whenever g ≡ 1 on O_d".

**§6 Hamiltonian layer.** File `s6-lppl.tex`; 880 words; Figs. 4 and 5.
- Items 1–6 of Part 2 §6: the opening checkpoint (the contract, R34), then pieces V, VI and VII, each ending at its checkpoint display (24), (23), (27), transcribed with numbers.
- Then the rate paragraph, with the wording of rulings R20, R25 and R38, and the Lemma 9.1(i) credit sentence verbatim from Part 2 §6.5.
- Then the `context` box, ≤ 80 words, with the R3 wording.
- The two-regime sentence is R16, verbatim. Describe eq. (18) as in R26.
- Must not use a decay law, slope or number read off Fig. 5.

**§9 The record and how to check it.** File `s9-record.tex`; 340 words; no figure. Sources:
- `README.md`, sections "What this is", "Status" and "How this record was produced";
- the gate table of `docs/status.md`;
- App B of main.tex (pp. 34–35);
- `part_i/C5_reading_record.md`.

Content:
- One line per gate G0–G6, with the requirement column paraphrased.
- The adversarial passes, "which the README says the assistant ran".
- The corrections listed in Part 2 §9.
- C5: nine items, verdicts blank.
- How to check: `% src:` comments; the dossier, whose page images are not redistributed (README, "What is deliberately not in this repository"); numbers resolved from `main.aux`.

Never call an audit "independent" without "AI-assisted" beside it.

### 6.3 `cqft`: §4, §5, §8.2, App A, App B (≈ 1380 words plus tables)

**§4 The one import that is not a quotation.** File `s4-import.tex`; 600 words plus the A1–A7 table (0.25 pp); Fig. 2.
- Items 1–7 of Part 2 §4, with rulings R24 and R27.
- The three-step reading (a)–(c) follows the Scope paragraph (p. 11) step by step, each step with its GJS pages, phrased as "the record reads …".
- **A1–A7 table**, three columns:
  - the import (number and name from labels.md);
  - what it supplies (the "what it supplies" column of `docs/imports.md`);
  - the source pinpoint, as each assumption's *Sources* line in main.tex (pp. 7–9) gives it.
- Facts about Level 2 and the dead Hamiltonian bypass: only from `docs/imports.md`, sections "What would discharge it".
- Must not use: GJS p. 590 (R28); "Appendix C establishes"; "display-by-display".

**§5 Euclidean layer.** File `s5-euclidean.tex`; 600 words; Fig. 3.
- Pieces I–IV of Part 2 §5. The checkpoints are displayed verbatim with their numbers: eq. (2); the conclusion of Lemma 4.4; (M₂); the bound of Prop 7.5; (G).
- One sentence on weak compactness (Part 2 §5).
- The sentence of R31 appears in §3 (qi); here, refer to §3 for it.

**§8.2 Part II.** File `s8b-part2.tex` (`\subsection{Part II: open at gate (II.11)}`); the text below, verbatim, plus the Part II table of `docs/status.md` verbatim (all ten rows, bold as in the source). cqft's section P is accepted with these trims (R5): the scoping-pass definition is shortened, and the closing sentence is kept. Change the text only to correct a factual error found at its source, and report any such change.

> Nothing in Part I depends on Part II; §14 of the record states that the two problems have "no mathematical dependence in either direction" (p. 33). Part II asks a different question: uniformity in a lattice or wavelet resolution, in the operator-algebraic renormalisation programme over the wavelet maps of [MMST] (§1.3(d), p. 4; §14, p. 33). Its gate (II.11) asks that the lattice ground states, evaluated on each fixed coarse Weyl generator, converge as the resolution is refined to the vector state of the ground vector of a continuum torus operator constructed in phase V3 (`part_ii/gate_II11_scoping.pdf`, §1); the scoping pass "proves no part of (II.11)". Already for the free model, no finest-scale local-state-norm error of order ε_N^ϑ, ϑ > 0, is possible (§14, p. 33), so the comparison is made at a fixed coarse scale. Status per claim, verbatim from `docs/status.md`: [table]. The record is not consistent about this gate: `strategy.md` and the ledger of phase V4 record (II.11) as closed at the stated import scope, `part_ii/README.md` says that phase closure was not reached, and the repository README says the gate is open; this companion uses the README's wording.

**App A Pointer table.** File `appA-pointers.tex` (`\section*{Appendix A. Where every statement lives}`); 1.5 pp; `\small` longtable.
- One row for each of the 61 numbered statements of labels.md, in order, with five columns:
  - number;
  - title (from labels.md);
  - page;
  - *depends on*: U (consumes U_GJS directly or through a statement of class U, including via (M₂) or (G)); G_γ (assumes (G_γ), nothing of class U); P (uses a printed A8 item — CE2, the norms, or the dilation — and nothing of class U); – (none of these); "import" for A1–A8 and Source Facts 2.2–2.4;
  - where the companion treats it (§ number), or, for Tier 3, a reason of at most eight words taken from Part 1.
- **Proposed column.** cqft checks every entry against the proof, changes any it finds wrong and reports the change; R5 re-checks.
  - **U:** 5.1, 5.2, 7.1, 7.2, 7.3, 7.5, 7.6, 7.7, 7.8, 10.2, 10.3, 10.4, 10.5, 11.1, 11.2, 12.2, 12.3, 13.2, C.7.
  - **G_γ:** 8.2, 9.3, 10.1.
  - **P:** 3.2, 3.3, 6.2, 7.4.
  - **import:** A1–A8, 2.2, 2.3, 2.4.
  - **–:** 2.1, 2.5, 2.6, 2.7, 2.8, 3.1, 4.1, 4.2, 4.3 (its statement carries its own hypotheses; its proof only points to later applications), 4.4, 6.1, 6.3, 8.1, 9.1, 9.2, 12.1 (its hypothesis is supplied by Thm 11.1), 13.1, 13.3, C.1–C.6.
- **Print no count of any class** (R7).

**App B Notation.** File `appB-notation.tex`; at most 25 symbols, two columns: symbol, then meaning with its locator from main.tex §2.1–2.3 (pp. 6–7), Def 2.1 or the defining display.
- Group K(g)/E(g)/H(g), Ω_g/ω_g, and 𝒞_E/𝒞_H/𝒢 as single rows.
- m₁ is "the GJS decay constant (A8(iv)); also the gap of Thm 7.8" and nothing else.

### 6.4 The orchestrator: front matter, figures, bibliography, assembly

**O1. Front matter** (`companion.tex`; the author block of the scaffold).
- **Title:** "A reader's companion to the cutoff-removal theorem for weakly coupled P(φ)₂".
- **`statusnotice`, verbatim:**

  > *Read this first.* This companion explains a research record and proves nothing new. The record is AI-assisted and has not been refereed; human verification is ongoing. Its main result, Theorem 12.2, is proved conditional on the imported hypothesis U_GJS (Assumption A8(vi)), which is not re-derived. Audit item C5, a second human reading of the source page images, is open. Statement numbers refer to `part_i/main.tex`; figures are illustrations, not evidence.

- **Abstract, verbatim:**

  > A reading guide to a 40-page research record on the spatially cutoff P(φ)₂ model; it proves nothing new. The record's Theorem 12.2 states that, for 0 ≤ λ/m₀² < ε_P, the full net of cutoff ground states ω_g (plateau order, no subnets, no averaging) converges in norm on every local algebra 𝔄(O). The rate is faster than every inverse power of the distance from O to the plateau edge. The limit is locally normal, translation and (for even P) ℤ₂ invariant, and a ground state of the Glimm–Jaffe dynamics in a spectral sense. The theorem is proved conditional on U_GJS, a cutoff-uniform Glimm–Jaffe–Spencer moment estimate. The record imports it at the scope at which the source states and uses it, and does not re-derive it. We explain why the question was open, how a uniform gap and an exact light cone replace compactness, and what is not claimed.

- **How to read (≤ 60 words), verbatim:**

  > Fifteen minutes: this page, §1 (what is proved, under what), §3 with Fig. 1 (the architecture) and §8 (what is not claimed). Forty-five minutes: everything except Appendix A, which points into the record for every step not explained here. Every claim carries its locator in the record: statement number and printed page.

**O2. Figures**, per Part 3:

| figure | file | label |
|---|---|---|
| Fig. 1 | `fig-spine.tex` | `fig:spine` |
| Fig. 2 | `fig-quantifier.tex` | `fig:quantifier` |
| Fig. 3 | `fig-slab.tex`, amended | `fig:slab` |
| Fig. 4 | `fig-lppl.tex`, composing the amended `fig-moves.tex`, `fig-path.tex` and `fig-two-regime.tex` | `fig:lppl` |
| Fig. 5 | `fig-rate.tex`, pgfplots | `fig:rate` |
| Fig. 6 | `fig-window.tex` | `fig:window` |

Extend `make_tables.py` with `tail_g1.dat`, the columns `r T` written from `make_figures.filter_curves(1.0)`. Each figure's mandatory caption sentences are copied verbatim from Part 3.

**O3. Bibliography.**
- [R], the record, as in the scaffold.
- Exactly the `\bibitem`s of main.tex (lines 2942–3025) that the drafts cite, copied verbatim.
- A list "Files of the record cited by path": `README.md`, `docs/status.md`, `docs/imports.md`, `part_i/C5_reading_record.md`, `part_ii/README.md`, `part_ii/gate_II11_scoping.pdf`, `strategy.md`, `m2/m2.tex`, `docs/figures/make_figures.py`.

**O4. Assembly and build.**
- `companion.tex` inputs the front matter, then `s1`–`s9` in order (§8 = `s8a` + `s8b`), App A, App B, and the bibliography.
- Build per AGENTS.md §7.1 (pdflatex twice; 0 errors, 0 Overfull, 0 undefined; no "??"/"TODO" in pdftotext).
- Measure each section's pages against Part 2 and send overruns to the editor for R4. Total ≤ 20 pp.

---

## 7. Consolidated findings register (for the author; never in the companion)

Sections G of all four memos, deduplicated, plus one new item from R2 (F15). Every item is MINOR: no member found a CRITICAL or MAJOR finding. Lines are lines of `part_i/main.tex` unless another file is named.

Status codes:
- **V**: verified by the orchestrator at the source.
- **R**: reported by the named member(s), not yet re-checked. "ed-read" means the editor has read the cited text in this session, which is not an orchestrator re-check.

### Main.tex: wording and statements

| ID | locator | finding (one line) | sev. | by | status |
|---|---|---|---|---|---|
| F2 | l. 1349 (Lemma 7.1, p. 18) | `\|le` prints "le" for ≤ | MINOR | all four | **V** |
| F3 | statements of Thms 5.1 (p. 16), 7.8 (p. 21), 11.1 (p. 28), 13.2 (p. 31), Prop 11.2 (p. 29), Cor 12.3 (p. 31) | "Assume U_GJS" is missing although their proofs consume it; only Thm 12.2 and Prop C.7 carry it | MINOR | ed; cqft, qi (traps) | **V** |
| F4 | l. 166 "compactness-free"; l. 271 "no compactness anywhere" | weak compactness in ℋ is used in Thm 5.1 Step 6 (l. 1233) and Lemmas 7.1–7.3; repair: "no compactness argument selects the limit state" | MINOR | ed, aqft, qi | **V** |
| F5 | l. 342 (§1.4 summary, p. 5) | the summary sentence drops "granted U_GJS" | MINOR | ed | **V** |
| F6 | l. 257; l. 264 (§1.4, p. 4) | "the strongest locally uniform statement available" is an unsupported comparative; the ergodicity clause has no citation | MINOR | ed, aqft | **V** |
| F7 | ll. 132–134 (§1.1); ll. 251–260 (§1.4) | GJ3 Thm 2.3 (norm compactness in local duals, normal limit points) and Thm 2.1 (positive energy), GJ3 p. 211, are not credited, so the reader may attribute them to Thm 12.2 | MINOR | aqft | R (ed rendered GJ3 p. 211 and concurs) |
| F8 | Cor 12.3 (p. 31) | the proof takes g ∈ 𝒢 (0 ≤ g ≤ 1); GJ3 (2.3), p. 210, says only "nonnegative"; GJ3 Thm 5.1, p. 250, assumes 0 ≤ g ≤ 1; repair: add "(with g ∈ 𝒢)" | MINOR | ed, aqft | **V** |
| F9 | ll. 300–305 (§1.4, p. 5); `part_i/README.md` l. 118 | "as Ŵ_γ must" is not forced by (18); "intrinsic to the method" needs the variant "analytic in a strip and = 1/E on [γ,∞) ⇒ unbounded at 0" | MINOR | ed, qi, aqft | R (ed-read) |
| F10 | ll. 235–237 (§1.3(b)); ll. 2508–2511 (§14) | "true rate poly(d)e^{−2m₁d}" comes from `m2/m2.tex`, which defines its own m₁² = m₀² + λ and gives a "Proof sketch" | MINOR | qi | **V** |
| F11 | l. 1806 (Lemma 9.1(ii)) | "a norm-convergent Bochner integral": t ↦ e^{itH} is in general only strongly continuous; repair: "strongly convergent" | MINOR | qi | R (ed-read) |
| F16 | Lemma 9.1 (p. 24); Lemma 10.5 (p. 28) | C_{q,γ}, C′_γ, C_{N,γ,M} and Ψ_γ depend on χ, which the notation hides | MINOR | qi | R |
| F17 | Hyp 13.1 (B1), (B4) (p. 31); §1.3(a); §14 | "ground state of (𝔄,α)" is used without qualifier; the only definition is in Prop 12.1, and Thm 13.2 Step 3 applies (B4) to ω_∞ | MINOR | aqft | R |
| F18 | l. 780 (A8 Scope, p. 11) | Thm 1.1.8 is quoted as "uniformly as h↑1"; the source prints "h → 1", as do SF 2.3 and C5 item 5 | MINOR | cqft | R (ed-read: l. 780 and C5 item 5) |
| F19 | §1.3(c) (p. 4); §13 opening (p. 31) | the incompatibility is attributed to the gap alone; Thm 13.2's proof also uses Thm 12.2 (1), (3), (4) (ll. 2445–2454), hence (M₂) and U_GJS | MINOR | cqft | **V** |
| F20 | Thm 5.1 Step 2; Lemma 6.1; Prop 6.2 (pp. 16–18) | GJS p. 593 centres Δ_j at lattice sites, while the record uses cells [j, j+1); every count is offset-invariant | MINOR | cqft | R |

### Documentation and figures

| ID | locator | finding (one line) | sev. | by | status |
|---|---|---|---|---|---|
| F1 | `README.md` ("What Theorem 12.2 rests on"); `docs/status.md`; `docs/results.md`; `docs/extract.py` l. 145 | The "24 of 61" count is `\ref`-reachability of the label `A:gjs`. (a) A8 itself is counted. (b) Source Facts 2.2–2.4 have no edge to A8, so Lemma 7.4 and Rem C.6 are missed. (c) Forward references count as uses (Prop 3.2, Rem 13.3, Lemma 4.3). (d) Prop 6.2 is flagged although it uses only the printed norm. (e) (G_γ), discharged in prose, leaves Prop 8.2, Lemma 9.3 and Lemma 10.1 "independent". (f) Cor 5.2 has no `\ref`. | MINOR | ed, cqft, qi | (b) **V**; (a), (c)–(f) R |
| F12 | `README.md` ll. 96–97 | the roles of the Ψ summands are reversed ("exponential-then-stuck") | MINOR | qi | **V** |
| F13 | `README.md` ll. 109–111; `docs/figures/make_figures.py` l. 203 | "past that time only the trivial bound survives" / "the cone has swallowed the gap": the cone reaches B_j only at \|t\| = r_j; Lemma 10.3 switches at r_j/2 by choice | MINOR | qi | R (ed-read) |
| F14 | `docs/figures/rate.svg`, `rate-dark.svg` `<desc>`; `make_figures.py` ll. 101–106, 117–119 | "crossing the t^-2 and t^-5 guides, so its effective power grows" contradicts the withdrawn slope claim and the drawn t⁻⁶ guide | MINOR | cqft | **V** |
| F15 | README rate figure, right panel; `docs/figures/curves.json` | at γ = M = 1, Ψ_γ(d) > 2 for every plotted d ≤ 60 (Ψ(60) ≈ 11.7 in `companion/figures/psi_g1.dat`), and no line marks the trivial bound 2, so the bound looks informative where it is not | MINOR | ed (R2) | R |
| F21 | `docs/imports.md` ("What would discharge it") | "display-by-display trace … pp. 598–629": GJS p. 628 omits a step ("we do not give the details") | MINOR | cqft | R |
| F23 | root `README.md`; `part_ii/README.md`; `docs/status.md`; main.tex §14 (p. 33); `strategy.md` | the status of Part II is inconsistent: "open" vs "closed at the stated import scope" vs "phase closure NOT yet reached", and the cofinal-subnet statement is "proved unconditionally" vs "superseded" | MINOR (Part II) | ed; BRIEF §3 | known to the orchestrator (BRIEF §3); details R |

### Optional additions to the record

| ID | locator | finding (one line) | sev. | by | status |
|---|---|---|---|---|---|
| F22 | A8(vii′)/(viii); C5 | GJS p. 590 introduces the slab family h_j = g(x)χ_j(t) and the dimensionless coupling; the p. 595 Remark has an n-point bound "independent of h" | MINOR (omission) | cqft | R |

---

## 8. R5 checklist for the adversarial verifier

The verifier did not draft the companion. Work from the built `companion/companion.pdf`, its `.tex` sources, `part_i/main.tex`, `part_i/main.aux` and the files named below. Record every check with its output. A failure goes to the editor with its locator. Nothing is fixed silently.

### Numbers, quotations, words
1. **Numbers against main.aux.**
   - Regenerate `labels.md` with `python3 companion/council/make_labels.py` and diff it against the committed copy.
   - Every `\rec{X}{p}` in the companion must give a number X and page p that agree with labels.md.
   - Every unlabelled page (§1.3, p. 4; §1.4, pp. 4–5; A8(vii′), p. 10; Scope, p. 11; §14, pp. 32–33; abstract, p. 2) must agree with `pdftotext -f p -l p part_i/main.pdf`.
2. **Quotations against main.tex.** Every string in quotation marks and every `recordbox` must occur verbatim in main.tex, up to LaTeX markup, or in the named file. Use the drafters' returned lists (Part 6.0) and add any quotation they missed.
3. **Status words.**
   - grep "proved": no bare "proved" may attach to Thm 12.2 or to any statement in class U of App A;
   - in each section, the first mention of a class-U statement carries "conditional on U_GJS";
   - Prop 8.2, Lemma 9.3 and Lemma 10.1 are described as implications under (G_γ).
4. **U_GJS wording.**
   - The frozen sentence (top of this PLAN) appears verbatim at the first description of U_GJS in each section.
   - Read every other occurrence of U_GJS: none may be stronger ("GJS prove", "a theorem of GJS") or weaker ("a strengthened quantifier", "beyond the source").
5. **Banned words.** grep, case-insensitive, for every item of rule 10 (Part 4). Each hit must be absent or sit in its allowed context. Then check the fixed phrasings of rule 9.

### Sources outside main.tex
6. **GJ3 facts.** Render GJ3, `refs/Glimm und Jaffe - 1970 - The λ(φ4)_2 quantum field theory without cutoffs .pdf`, PDF pages 8, 9 and 48 (printed pp. 210, 211, 250), with `pdftoppm -r 110`, and confirm each of the following:
   - (2.3): g is "a nonnegative C₀^∞ function equal to one on the interval [−3, 3]", and g_n(x) = g(x/n);
   - (2.4)–(2.5): averaging with h ≥ 0 supported in [−1, 1];
   - Thm 2.1: w\* limit points along a subsequence, and the spectrum of the time-translation generator lies in [0, ∞);
   - Thm 2.3: ω_n↾𝔄(B) lies in a norm-compact subset of 𝔄(B)\*, and every limit point is normal;
   - Thm 5.1: "0 ≤ g(x) ≤ 1".

   Delete any companion sentence or §2 table cell that is not confirmed word for word in substance.
7. **Part II.**
   - The §8.2 table equals the Part II table of `docs/status.md` character for character, bold included.
   - "proves no part of (II.11)" occurs in the abstract of `part_ii/gate_II11_scoping.tex`.
   - "no mathematical dependence in either direction" and the ε_N^ϑ sentence agree with main.tex §14 (p. 33).
   - The inconsistency sentence matches BRIEF §3. The status word used is the README's "open".

### Figures, mathematics, pages
8. **Figures.**
   - Each caption contains its mandatory sentences from Part 3 verbatim and ends "Illustration, not evidence."
   - `#8250df` (`cond`) appears only on class-U items, with outline only for G_γ items and Prop 12.1.
   - Fig. 1's node classes agree with App A's column.
   - For Fig. 5: rerun `python3 companion/figures/make_tables.py` and diff the `.dat` files; check that sentence 4 holds for the plotted range (Ψ > 2 at every plotted d); and confirm no reference powers or slopes appear.
   - For Fig. 4(b): no cell bar enters O_d, and the shells are labelled ≤ 4 per side.
   - For Fig. 4(c): the band r_j/2 < |t| < r_j is labelled as in Part 3.
9. **App A classification.**
   - Re-derive from main.tex's proofs, independently, the column for 3.2, 3.3, 4.3, 5.2, 6.2, 7.4, 8.2, 9.3, 10.1, 12.1, 13.3, C.6 and C.7, and spot-check ten further rows.
   - Check that no count of any class is printed.
10. **No new mathematics.** Every mathematical sentence traces to a main.tex locator. Every `context` box cites only `\bibitem`s of main.tex (lines 2942–3025) or record files. The filter-obstruction sentence is the restricted form of R25.
11. **No leakage of findings.** None of F1–F23 appears in the companion as a finding or an implied correction (e.g. "the record says h↑1", "the README is wrong"). The rulings R16, R20, R21, R23 and R26 appear as plain wording.
12. **Front matter.** Count words on the rendered text (pdftotext, then `wc -w`): abstract ≤ 150, notice ≤ 80, how-to-read ≤ 60. The notice states AI-assisted, not refereed, C5 open, human verification ongoing, and "conditional on U_GJS".
13. **Page budget and build.**
    - Total ≤ 20 pp; report the page count.
    - Each section within +10 % of its Part 2 page budget.
    - The build log shows 0 errors, 0 Overfull and 0 undefined, and `pdftotext companion.pdf - | grep -nE '\?\?|TODO'` prints nothing.
14. **Notation.** App B has ≤ 25 rows. Each symbol of App B is defined in the body before its first use; check by grepping first occurrences. m₁ is used only for the GJS constant.

---

## 9. Checkpoint 1 (author, 23 October 2026) and the orchestrator's amendments in R3

The author approved the plan with the orchestrator's recommendations on the five decisions:

1. **Fig. 6** is kept.
2. **GJ3 context** (Thms 2.1, 2.3; (2.3)–(2.5); Thm 5.1 of GJ3) is cited as context only, after the R5 page check (Part 8, item 6); the record's §1.1/§1.4 wording is left to the author.
3. **Fig. 5** shows γ ∈ {1, 2} with M = 1 and draws the trivial bound 2. It has four computed panels: (a) Ŵ_γ(E) = χ(E)/E at γ = 1; (b) T_γ(r) for γ ∈ {1, 2}; (c) the two summands of Ψ_γ at γ = 1; (d) Ψ_γ(d) for γ ∈ {1, 2} with the line at 2 and d₀ = 4 + 2/γ marked. Two new tables, `tail_g1.dat` and `tail_g2.dat` (columns `r T`), are written by `companion/figures/make_tables.py` from `make_figures.filter_curves(γ)`. Caption sentence 1 of Part 3 therefore reads "… for one admissible χ, γ ∈ {1, 2} and M = 1, on a time grid up to t = 160, with values of |W_γ| below 10⁻⁹ set to zero" (the grid of `filter_curves` ends at t = 160; the subsampled `curves.json` ends at 159.197), and sentence 4 reads "At γ = 1, Ψ_γ(d) exceeds the trivial bound 2 at every d shown; at γ = 2 it falls below 2 from d = 35 on: the content is the decay in d, not the size at any d" (`psi_g2.dat`: Ψ(34.5) = 2.0363, Ψ(35) = 1.8573; `psi_g1.dat`: Ψ(60) = 11.7441).
4. **Documentation fixes** (README, site texts, `docs/extract.py`; findings F1, F12, F13, F14, F15) are made in this session in a separate commit. `part_i/main.tex` is not edited: F2–F11 and F16–F20 remain for the author.
5. **Part II**: the companion uses the README's "open"; the record's wording is left to the author.

Orchestrator's amendments to Part 3 while drawing (all content as specified; layout only):
- Fig. 1: the band labels are one word each (inputs, Euclidean, m₁ and M, Hamiltonian, identification), with the section ranges in the caption; the edges A1 → Lemma 4.4, A1 → Prop 8.2, A6 → Prop 2.7 and A6 → Prop 12.1 are drawn as labelled stubs; the items (1)–(5) of Thm 12.2 are listed inside its node, each with its cost; Cor 12.3 is a node "by (1) and averaging"; Appendix C is a grey node without any arrow.
- Fig. 2: the two geometry panels are stacked at the left; the three evidence boxes are in a row above the dashed box.
- Fig. 3: as specified (sharp times at ±2 with T = 3, hatched strip |x⁰| < 1, fourth box in `cond`).
- Fig. 4: three stacked full-width panels; (b) uses d = 6, g = 1 on [−8, 8] (0 outside (−10, 10)), g′ = 1 on [−12, 12] (0 outside (−14, 14)), cells j = ±8, …, ±14 clipped to supp v, shells n = d, …, d + 6; (c) carries the line labels at the right.
- Fig. 6: as specified, with the text in the two pockets left of the cone.

### 7.1 Addendum after R3 (23 October 2026, orchestrator; items reported by the drafters and re-checked at the source)

| ID | locator | finding (one line) | sev. | by | status |
|---|---|---|---|---|---|
| F24 | `README.md`, "What is deliberately not in this repository" | "`render_evidence.sh` regenerates the audit's page-image corpus": the script renders a fixed page list into `fresh_audit_2026_08_16/evidence/` only; `audit_2026/evidence/`, the dossier main.tex §2.4 names, has no render script | MINOR (documentation) | qi | **V**; README reworded in this session |
| F25 | l. 689 (Source Fact 2.3, p. 10) | "uses on pp. 595–597", while ll. 79, 110, 728 and 2656 say pp. 594–597 | MINOR | aqft | **V** |
| F26 | l. 299 (§1.4) vs l. 1803 (Lemma 9.1(ii)) | the filter identity is written with P₀ in §1.4 and with P_{ker H} in the lemma | MINOR | qi | R |
| F27 | ll. 192, 354, 2390, 2598, 2625 | the 9 August 2026 audit is called "independent" although the README says the audit documents were drafted with the assistant | MINOR (wording) | qi | **V** (the five lines) |
| F28 | `docs/status.md`, gate table | six rows carry eight gate names (G1/G2, G3a/G3b share rows), so "seven gates" is not a count the table supports | MINOR (documentation) | qi | **V** |
| F29 | GJ3 p. 210 vs Thm 2.1 (p. 211) | p. 210 says "subnet", Thm 2.1 "subsequence" (context only; the §2 table follows Thm 2.1) | note | aqft | R5 |
| F1 (update) | `docs/extract.py` | item (b) fixed in this session: a statement printed inside an assumption gets the edge to it; the count is now 29 (Source Facts 2.2–2.4, Lemma 7.4, Remark C.6 added); items (a), (c)–(f) remain and are stated as limits of the index in README and `docs/status.md` | — | — | (b) fixed |

Corrections to this PLAN's own locators, found by the drafters and checked against `part_i/main.pdf`: display (1.1.11) of A8(vii′)(a) is printed on p. 11, not p. 10 (T2.1 row, §2 item 4); the paragraph naming C5 in App B is on p. 35, not p. 34 (T1.2 row, §4 item 6).
- Superseded files removed in R3: the R0 drafts `fig-moves.tex`, `fig-path.tex`, `fig-two-regime.tex` (folded into `fig-lppl.tex`) and `fig-two-paths.tex` (folded into `fig-quantifier.tex`), and `make_status.py` with `status_part_i.dat` (the dropped F7).

### 7.2 Addendum after R4 and R5 (24 October 2026; items reported by the editor and the verifier, each marked with who checked it at the source)

| ID | locator | finding (one line) | sev. | by | status |
|---|---|---|---|---|---|
| N1 | `docs/imports.md` l. 16 (A4) | "the L^p smoothing used in the moment estimates", while A4's "Used in" line (main.tex ll. 557–558) names §8 (the pairing bound) and App. C (the tail estimate), not Thm 5.1 | MINOR (documentation) | cqft; ed | ed-read |
| N2 | `docs/imports.md` l. 17 (A5) | "a core on which the algebra acts", while A5(ii) (ll. 571–573) is a common core for all K(g_s) with K(g_s)ξ = K(g_{s₀})ξ + (s−s₀)V(g′−g)ξ | MINOR (documentation) | cqft; ed | ed-read |
| N3 | `part_ii/README.md` ll. 70, 74, 238–240 | l. 70 and ll. 238–240 say "(II.11) closed", l. 74 "Phase closure: NOT yet reached"; ll. 3–4 say the 16 August addendum supersedes earlier closure statements (the F23 family) | MINOR (Part II) | ed | ed-read; R5 read ll. 70, 74, 238 |
| N4 | main.tex App. B l. 2644; `docs/status.md` l. 61 | "on p. 595" for the affine-path application of Thm 1.1.7, where A8(vii′)(a) and C5 item 8 (`C5_reading_record.md` l. 106) say pp. 594–595 (the F25 family) | MINOR | ed | ed-read |
| N5 | abstract ll. 117–118; §1.3(a) ll. 233–234; §14 ll. 2516–2517 | the scope of the uniqueness non-claim is worded three ways ("among all locally normal ground states" / "every locally normal ground state" / "every locally normal translation-invariant ground state"); not a contradiction | MINOR (wording) | aqft; ed | ed-read |
| O1 | `docs/imports.md` l. 18 (A6) | "the exact light cone" credited to A6, while A6's Scope (ll. 603–605) says the cutoff cone is derived (Prop. 2.7) | MINOR (documentation) | R5 | **V**; fixed 24 October (Part 10) |
| O2 | main.tex ll. 1018–1020 (Remark 3.3) | the remark mixes the dilation transport, which §2.6 consumes as an input (ll. 892–897), with a forward claim about Thm 12.2's conclusions, so the mechanical index flags it as A8-dependent | MINOR (presentation) | R5 | R5-read |
| O3 | `README.md` | the github.com repository URL appears only in `CITATION.cff` l. 40, not in the README | note | R5 | R5-read |
| O4 | GJ3 p. 210 vs Thm 2.1 (p. 211) | p. 210 prints "subnet", Thm 2.1 "subsequence" (= F29); confirmed on the page images; the companion's Table 2 follows Thm 2.1 | note | aqft; R5 | **V** by R5 |

## 10. R5 outcome and the corrections of 23–24 October 2026 (orchestrator)

The verifier's report is `council/r5-verifier-report.md`; the editor's R4 report is `council/r4-editor-report.md`. Every finding below names the verifier's ID. "Fixed" means changed in the companion and rebuilt; "recorded" means left as it is, with the reason here. The round-R4 text fixes requested by the editor (its report, section 6) were applied before R5: the Fig. 2 locator (pp. 11–12), the abstract (ε_𝒫, "(for even 𝒫)", "in the spectral sense", "without re-deriving it"; the built abstract supersedes the text of Part 6.4, O1), and the Fig. 1 caption's duplicated clause.

### 10.1 Figures, captions, bibliography (orchestrator)

| ID | severity | disposition |
|---|---|---|
| V1 | CRITICAL | **Fixed.** The stub into Proposition 2.7 in Fig. 1 now reads "A6(i): speed 1, Trotter"; the stub into Proposition 12.1 keeps "(P)". Verified at the source: main.tex ll. 849–858 (the proof of Prop. 2.7 uses A6(i) twice) and ll. 603–605 (A6's Scope: the cutoff propagation bound "is not imported but derived"). Part 3's edge list ("A6 → Prop 2.7 and Prop 12.1: '(P)'") was wrong for Prop. 2.7 and is corrected by this entry. |
| V2 | MAJOR | **Fixed.** The U_GJS → Theorem 7.8 edge now leaves the U_GJS box at its bottom-left corner, runs horizontally beneath Appendix C with its label "fixed g, uniform in T" in the empty slot above Proposition 2.7, and enters (G) at its top-right; the (M₂) edge's label moved to the right of its arrow and reads "uniform in g, T". Appendix C still has no arrow. |
| V3 | MINOR | **Fixed.** `make_bib.py` writes `\bibitem[R]{record}`; the reference list prints the record as [R]. |
| V4 | MINOR | **Fixed.** The Proposition 12.1 node is three lines ("ground state in the spectral sense, via (P)"); the "(31) as hypothesis" edge bends above the node; the "(3)" edge leaves the node's bottom-right so that the tag "any norm limit" is clear. |
| V5 | MINOR | **Fixed.** The input boxes (A1–A7, CE2, Appendix C) have sharp corners and a light fill, the interface nodes (G_γ) and M a neutral outline, and the caption says "The top row (inputs, light fill) and the two interface nodes carry no class." |
| V6 | MINOR | **Fixed.** Top panel: smaller h₁ box, the path label at the top of the dashed box with a white background. Bottom panel: T and −T right of the axis outside the frame, h_{T,g} below the frame; the slab path h_{T,g_s} and its tint in the accent colour (violet reserved for U_GJS); the arrows from (a) and (c) enter the dashed box 5–6 mm inside its corners, clear of Appendix C. |
| V7 | MINOR | **Fixed.** The strip label sits above the x¹ axis; T and −T outside the frame; the caption now says "Nothing is computed." |
| V8 | MINOR | **Fixed.** O is labelled above its segment; both annotation blocks are raised clear of the plateau line. |
| V9 | MINOR | **Fixed.** The spectrum label in Fig. 5(a) is right-aligned inside the axis. |
| V10 | MINOR | **Fixed.** The two pocket texts of Fig. 6 stand at the far left in small type, outside the cone at every line; the plateau label stands at the right end of the plateau, above the axis. |
| V11 | MINOR | **Recorded.** Total 20 pp, the ceiling of Checkpoint 1. The per-section overruns (§3 +17 %, §4 +17 %, §5 +15 %, §6 +22 %, §7 +15 %, App. B +33 %, references +143 %) come from the figures' real heights (Part 2 budgeted 0.4 pp per figure; Figs. 1, 4 and 5 take 0.85, 0.85 and 0.60 pp with their captions) and from the sixteen verbatim bibliography entries; the prose is within budget. Not cut: the three sections that could be cut (§§5–6, App. B) carry the checkpoints and the notation. |
| V19 | MINOR | **Fixed.** The record's entry carries the full title ("… algebra. Part I — unified manuscript"); the URL stays (it is the one in `CITATION.cff` and `docs/status.md`). |
| V20 | MINOR | **Fixed in part.** The label "exact cone" sits on the Proposition 2.7 → Lemma 10.3 edge; the Proposition 2.7 → Lemma 9.3 edge stays unlabelled, since the two boxes are 4 mm apart and no label fits (Part 3's edge list is amended accordingly). The caption now says "its Euclidean layer, §§4–7; … its Hamiltonian layer, §§8–11; the identification, §12", so the numbers read as the record's. |
| N2 | note | **Recorded.** The Fig. 4 caption's "No automorphism or spectral flow is constructed" is a mandatory sentence of Part 3 and states what is not done; rule 10 is read as allowing it there. |
| N3 | note | **Recorded.** The abstract as built (see above) supersedes Part 6.4, O1. |
| O1 | record | **Fixed in the documentation.** `docs/imports.md`, A6 row: "free propagation at speed one, the Trotter formula, and the patched limit dynamics α; the cutoff light cone itself is derived (Proposition 2.7)". The KB import node for A6 is corrected the same way. |
| O2–O4 | record | **Recorded** in Part 7.2 below. |

Besides these, the underfull boxes of Fig. 3 and the label of the trivial bound in Fig. 5(d), which crossed the γ = 2 curve, were fixed on 23 October before R5. The verifier's one deviation (a read-only `git ls-files`, reported by it) changed nothing.

### 10.2 Text (a fresh editor agent, 24 October 2026; its report is `council/r5-fix-editor-report.md`)

| ID | severity | disposition |
|---|---|---|
| V12 | MINOR | **Fixed.** §5 Piece II, §5 Piece IV and §6 Piece VII each make three steps before their checkpoint: Piece II treats Steps 1–4 of the proof of Theorem 5.1 as one step ending in (5), then (2) with U_GJS gives (6), then weak closedness; Piece IV cites Theorem 7.7 as one step ("with Ω_g, they span a dense subspace", which also corrects the draft's "these vectors are total": the centred vectors are orthogonal to Ω_g), then Checkpoint III, then density; Piece VII follows the record's Steps 1–4 of Proposition 10.4. Checked by the orchestrator at main.tex ll. 1538–1543 (Theorem 7.7) and ll. 1212–1215 (eq. (5), ‖Q_V‖_GJS ≤ M²/C₈). |
| V13 | MINOR | **Fixed.** §9: "The scope amendment of 5 September 2026 gave U_GJS (A8(vi)) the status described in §4" (the amendment changed the status, not the inequality: title page, l. 76). |
| V14 | MINOR | **Fixed.** Checkpoint (23) transcribes main.tex ll. 1908–1911 in full, including g ∈ 𝒞_H, "assume (G_γ)" and "for a bounded interval O". |
| V15 | MINOR | **Fixed.** §1 defines φ₀, C = (2μ)⁻¹, λ and the C-Wick order at the first display, glosses α as the g-independent automorphism group of A6(ii), and says that Ψ_γ is an explicit function of the distance stated in §6; the A3 cell names the Euclidean interaction 𝒰_h and the integrability of e^{−ϱ𝒰_h} in words. |
| V16 | MINOR | **Fixed.** Table 1: "d(g_n,O) → ∞ for every bounded interval O". |
| V17 | MINOR | **Fixed.** §8.1(c) carries both locators, Remark 13.3 (p. 32) and §14 *Beyond weak coupling* (p. 33). |
| V18 | MINOR | **Fixed.** Table 2: "converges w* to it". |
| N1 | note | **Fixed.** The §8.2 inconsistency sentence is back to the content of BRIEF §3 (strategy.md and V4's ledger; part_ii/README.md's "not yet reached"; the repository README's "open"); the clause about part_ii/README.md's own contradiction (N3 of 7.2) is out. |
| N4 | note | **Fixed.** The A6 cell reads "(i) speed one, the Trotter formula; (ii) (P): …; the cutoff cone is Proposition 2.7". |

Rule 11 paid for the longer checkpoint and glosses from §§5–6 (three shortenings listed in the editor's report). The editor's own caution stands: the pagination is fragile at three spots (before §7, around Fig. 2, before §6); any later edit of more than two lines needs the figure placements re-checked (Part 8, item 13).

### 10.3 Final build (24 October 2026)

`python3 make_bib.py`, then `SOURCE_DATE_EPOCH=1792800000 FORCE_SOURCE_DATE=1 pdflatex -interaction=nonstopmode companion.tex` three times: 0 errors, 0 Overfull, 0 undefined, 0 Underfull; `pdftotext | grep -nE '\?\?|TODO|Hmm|wait,'` empty; 20 pages; `pdfimages -list`: no embedded image; a second run of the same three passes reproduces the PDF byte for byte. Start pages from `companion.aux`: §1 p. 1, Table 1 p. 3, §2 p. 3, Table 2 p. 4, §3 p. 4, Fig. 1 p. 5, §4 p. 6, Fig. 2 p. 7, §5 p. 8, Fig. 3 p. 9, Fig. 4 and §6 p. 11, Fig. 5 p. 12, §7 p. 14, Fig. 6 p. 15, §8 p. 16, §9 p. 17. Front matter by `pdftotext | wc -w`: notice 69, abstract 149, how-to-read 53. The printed date is 24 October 2026.

### 10.4 Re-verification (24 October 2026)

The same verifier re-checked the rebuilt PDF against V1–V20, N1 and N4 (its second report is appended to `council/r5-verifier-report.md`): every item fixed as 10.1–10.2 record; the locators re-extracted (159, none failing), the quotations unchanged, the colour classes correct, the build reproduced byte for byte. Three new MINOR items, fixed by the orchestrator the same day and rebuilt under the same gates (20 pages; start pages unchanged):

| ID | disposition |
|---|---|
| W1 | **Fixed.** The U_GJS → Theorem 7.8 edge in Fig. 1 now runs between Appendix C and the tops of (G) and (M₂) and enters (G) from its right side, 2.5 mm below its top, so the arrowhead points into (G). |
| W2 | **Fixed.** Fig. 2, bottom panel: T and −T stand left of the x⁰ axis; h_{T,g} is labelled at the top-left corner of its frame and h_{T,g′} at the top-right, so no label pair reads as a formula. |
| W3 | **Fixed.** §3: "for every bounded interval O and ω_{g_n} converging in norm on every local algebra 𝔄(O)" (the V16 wording; main.tex l. 2228). |

The verifier's optional note on the Fig. 1 caption was taken: "The light-filled inputs of the top row and the two interface nodes carry no class." The final PDF is the build after these three fixes; its gates and placements are those of 10.3.
