# Memo `aqft`: council round R1, 23 October 2026

Read this session: the brief's reading list; `part_i/main.tex` with every proof of §§2, 4, 5, 7–13; outside the record (context and G only), GJ3 printed pp. 210, 211, 250, rendered as images. Numbers from labels.md; pages are main.pdf's printed pages.

## A. Must know

A1. **The theorem.** For 0 ≤ λ/m₀² < ε_P, the cutoff ground states ω_g on the free time-zero quasi-local algebra 𝔄, indexed by the whole plateau class 𝒢, converge in the norm of every local dual 𝔄(O)\*. The rate is ‖(ω_g−ω_∞)|𝔄(O)‖ ≤ Ψ_{m₁}(d) whenever g ≡ 1 on O_d, where Ψ_{m₁} decays super-polynomially and depends on O only through d. *Locators:* Thm 12.2(1) (p. 30); eqs (31), (30) (p. 28); Def 2.1 (p. 6). *Status:* proved, conditional on U_GJS (A8(vi), eq. (U_GJS), p. 10) and on A1–A7.

A2. **The news is convergence, not the topology and not normality.** Context: in GJ3 Thm 2.3 (printed p. 211) the averaged states already lie in a norm-compact subset of each local dual, with normal limit points, and GJ3 Thm 2.1 gives those limit points positive energy. The record proves that the unaveraged full net has a single limit, with a rate, so every w\* limit point of GJ3's construction equals ω_∞: *canonical*, not *unique*. *Locators:* Cor 12.3 (p. 31); §1.1 (p. 3).

A3. **Two inputs, one implication.** Props 8.1–12.1 reach the GJS package A8, and hence U_GJS, only through (M₂) (Thm 5.1, p. 16) and (G) (Thm 7.8, p. 21). With those two edges cut, none of them reaches A8 (computed here from results.json with extract.py's own closure rule). The rest of the argument uses A1–A7 and operator theory, which agrees with "exactly two nonstandard inputs" (§1.4, p. 4).

A4. **Locality meets the gap through three exact tools:**
- the exact light cone of every cutoff dynamics (Prop 2.7, p. 12);
- the exact inverse-energy filter (Lemma 9.1, eq. (18), p. 24);
- clustering with one unbounded local argument (Lemma 9.3, eq. (23), p. 25).

They combine in the two-regime bound (Lemma 10.3, eq. (26), p. 27), which Prop 10.4 sums over cells (eq. (27), p. 27).

A5. **"Ground state" means the spectral sense of Prop 12.1 (p. 29), and it costs an identity, not an estimate.** The dynamics α is Glimm–Jaffe's patched dynamics, imported in A6(ii) (p. 9) as a one-parameter automorphism group of 𝔄 with property (P); no continuity of α is imported or used. For |t| < d(g,O), (P) makes ω_g(Aα_t(B)) the Fourier–Stieltjes transform of a measure on [0,∞), and local norm convergence carries this to ω_∞.

## B. Should know

B1. **The plateau net.** 𝒢 consists of g ∈ C_c^∞ with 0 ≤ g ≤ 1 and a plateau, directed by inclusion of plateau interiors. "Full net" means no subnet and no averaging; the bound sees g only through which O_d its plateau contains. *Locators:* Def 2.1 (p. 6); eq. (31); Thm 11.1 Step 3 (p. 28).

B2. **Simplicity, not a gap, drives the Euclidean transfer.** ψ̂_T → Ω_g by simplicity alone; isolation of E(g) is not imported and the gap is an output, so there is no circularity. Simplicity returns in the rank-one Riesz projection behind eq. (15) and in covariance and parity. *Locators:* Lemma 4.4 (p. 16); A1 Scope (p. 7); Prop 8.2, eq. (15) (p. 23); Lemma 2.8 (p. 12).

B3. **Local normality.** It means ω_∞|𝔄(O) is normal on the Fock-space von Neumann algebra 𝔄(O) (the local Fock folium). It is free given (1): norm limits of the normal vector states ω_g stay normal. *Locator:* Prop 11.2 (p. 29).

B4. **How the unbounded perturbation is handled.** V(g′)−V(g) has infinite norm, but the state derivative sees only the vector V(v)Ω_s, cut into unit cells with ‖V_jΩ_s‖ ≤ M uniformly along the path. No automorphism or spectral flow is constructed. *Locators:* Lemma 10.1, eq. (24) (p. 26); Lemma 10.2, eq. (25) (p. 26).

B5. **What norm (rather than w\*) convergence buys.** In Prop 12.1, {Aα_t(B): |t| ≤ T} is bounded in 𝔄(O_T), so the two-point functions converge uniformly on |t| ≤ T, giving the continuity the definition needs. In Thm 11.1 the rate is uniform over the unit ball of 𝔄(O). *Locators:* Prop 12.1 (p. 29); Thm 11.1 (p. 28).

B6. **Translation invariance needs no averaging.** g ↦ τ_a g is an order isomorphism of 𝒢, so (T) plus (1) give ω_∞∘τ_a = ω_∞. Parity follows the same way for even P. *Locators:* Lemma 2.8, eq. (T) (p. 12); proof of Thm 12.2 (p. 30).

B7. **Constants are in working coordinates (m₀ = M_\*).** In the original coordinates the rate is Ψ_{m₁,\*}(s·d), with m₁ := s·m₁,\*. *Locators:* §2.6 (p. 13); Rem 3.3 (p. 14).

B8. **What the local algebras are.** They are the free time-zero von Neumann algebras 𝔄(O) on Fock space, O a bounded interval; the interaction sits in the states and in α. Item (5) of Thm 12.2 concerns the cutoff H(g), not a GNS Hamiltonian of ω_∞. *Locators:* §2.1 (p. 6); Thm 12.2(5).

## C. Pointer table

| statement | why the companion skips it | where |
|---|---|---|
| Rem 2.5 | conventions lock | p. 12 |
| Prop 2.6 | one line: Ω_g ∈ Ran e^{−tK(g)} ⊆ D(V(h)) | p. 12 |
| proof of Prop 2.7 | Trotter + speed-zero interaction; keep the statement | p. 12 |
| proof of Lemma 2.8 | simplicity + positivity; keep display (T) | p. 12 |
| Lemma 3.1 | class membership, affine stability | p. 13 |
| Prop 3.2, Rem 3.3 | dilation into the printed regime; one sentence (B7) | pp. 13–14 |
| Lemmas 4.1–4.3 | FKN for bounded, signed, unbounded arguments | p. 15 |
| Cor 5.2 | φ⁴ constant | p. 17 |
| Lemma 6.1, Prop 6.2, Rem 6.3 | cell counts, GJS norms | pp. 17–18 |
| Lemmas 7.1–7.4 | slab limits at fixed g; CE2 across a strip | pp. 18–19 |
| Lemma 7.6, proof of Thm 7.7 | density tools; keep "centered polynomial vectors are total" | pp. 20–21 |
| Prop 8.1 | norm-C¹ of e^{−TK_s} (hypercontractive pairing) | p. 22 |
| proof of Prop 8.2 | Riesz projection; keep eq. (15) | p. 23 |
| Lemma 9.2 | optimized Gaussian separator; one sentence | p. 25 |
| proof of Lemma 10.5; Thm 11.1 Step 2 | summation; limit functionals extend to a state | p. 28 |
| Source Facts 2.2–2.4, A8(vii′) | the evidence for U_GJS belongs in a status box | p. 10 |
| App. A, B, C | constants, provenance, source audit | pp. 33–35 |
| Hyp 13.1, Thm 13.2, Rem 13.3 | one paragraph under "not claimed" | pp. 31–32 |

## D. The longest chain

**D1. Computed.** The longest chain of proof references runs through 14 statements (13 links). It is computed from results.json `proof_uses`, with equation labels mapped to their statements and three forward pointers dropped (3.2→3.3, 4.3→5.1, 4.3→7.1):

A3 → Lemma 3.1 → 4.1 → 4.2 → 4.3 → Thm 5.1 → Lemma 10.2 → 10.3 → Prop 10.4 → Lemma 10.5 → Thm 11.1 → Prop 11.2 → Thm 12.2 → Cor 12.3 (or Thm 13.2).

**D2. The chain as the reader experiences it** (the gap branch, the longer one):
1. A8: CE1 via U_GJS, CE2, norms (p. 10)
2. slab FKN, eqs (2)–(3) (p. 15)
3. Lemma 4.4
4. (M₂) (Thm 5.1); Lemma 7.1
5. Lemmas 7.2–7.3
6. Lemma 7.4
7. Prop 7.5
8. Lemma 7.6, Thm 7.7
9. (G) (Thm 7.8)
10. eq. (15) (Props 8.1–8.2)
11. eq. (18) (Lemma 9.1)
12. eq. (24) (Lemma 10.1)
13. Prop 2.7, Lemmas 9.2–9.3
14. Lemma 10.2
15. Lemma 10.3
16. Prop 10.4
17. Lemma 10.5
18. Thm 11.1
19. Prop 11.2
20. Prop 12.1
21. Lemma 2.8, Thm 12.2
22. Cor 12.3

**D3. Cut into pieces, each ending at a displayed checkpoint:**

| piece | steps | checkpoint |
|---|---|---|
| P1 | 1–3 | eq. (2), and ψ̂_T → Ω_g without a gap |
| P2 | 4 | (M₂) and Lemma 7.1's bound |
| P3 | 5–7 | ⟨ψ_Q,e^{−tH(g)}ψ_Q⟩ ≤ Ĉ_Q e^{−m₁t} |
| P4 | 8–9 | (G) |
| P5 | 10–12 | eq. (24) |
| P6 | 13–15 | eq. (26) |
| P7 | 16–17 | ‖(ω_g−ω_{g′})|𝔄(O)‖ ≤ Ψ_γ(d) ≤ C_N(1+d)^{−N} |
| P8 | 18–19 | eq. (31) and normality |
| P9 | 20–22 | Thm 12.2(1)–(5) and Cor 12.3 |

P1–P4, P5–P7 and P8–P9 are the companion's three parts. They follow rows (i)–(v) of the table in §1.2 (p. 3).

**D4. §1.4 (pp. 4–5) judged as a first draft.**
- *The topology.* Right. Drop "the strongest locally uniform statement available", add A2's GJ3 sentence, gloss "local Fock folia" as in B3.
- *Why standard tools fail.* Drop "ergodicity-type arguments give extremality…" (no reference, no body counterpart); mark "no soft passage" as context; replace "no compactness anywhere" (G2).
- *Pillar 1.* About eight steps in one paragraph: split it at P1–P4 and move the U_GJS scope parenthetical to the status box.
- *Pillar 2.* Central and correct: split it at P5/P6. The strip-analyticity parenthetical goes to "sharpness" (for qi: "as Ŵ_γ must" describes the chosen χ, not a requirement of eq. (18)).
- *Assembly and identification.* Keep it nearly verbatim, adding the spectral definition as a display and A6(ii) as the source of α.
- *Boundaries.* Change "records the expected mechanism" to "states, conditional on Hyp 13.1". Its closing sentence ends the companion.

## E. Figures

**Own proposals.**

- **E1. Identity window (Prop 12.1).**
  - *Purpose:* why the ground-state property costs an identity.
  - *Drawn:* the (x,t)-plane with the plateau on t = 0 and O inside it; the band |t| < d(g,O) is labelled "α_t = β^g_t on 𝔄(O)". Inset: ω_g(Aα_t(B)) = ∫_{[0,∞)}e^{itE}dρ_g(E) on (−d,d).
  - *Computed:* nothing.
  - *Must not suggest:* that ω_g is α-invariant, that an estimate is involved, or that the record constructs α.
  - Best as the right panel of F4.
- **E2. What each item of Thm 12.2 costs** (drawn inside F1).
  - *Drawn:* edges labelled by cost: (1) estimate (Thm 11.1); (2) normal limits (Prop 11.2); (3) the identity (P) (Prop 12.1); (4) the order isomorphism plus (T); (5) restated inputs (Thms 7.8, 5.1).
  - *Computed:* the conditional colouring, from results.json.
  - *Must not suggest:* that items (2)–(4) are unconditional. Only the arrows are free of A8.
- **E3. Limit point versus limit.**
  - *Drawn:* two columns. GJ3 (context): averaged states, a subsequence, a normal positive-energy limit point. The record: the full net over 𝒢, Cauchy in each 𝔄(O)\*, one limit, Cor 12.3.
  - *Must not suggest:* that GJ3 lacked the norm topology or normality, that distinct GJ3 limit points were known, or uniqueness among ground states.

**Verdicts on F1–F7.**
- **F1: keep, change.** Carry E2. Add A6 (α, (P), the cone) feeding Prop 2.7 and Prop 12.1, and A1 (simplicity) feeding Lemma 4.4 and Prop 8.2. Compute the colouring, so that Lemmas 9.1–9.3, 10.1, Props 8.1–8.2, 12.1 and Lemma 2.8 stay neutral.
- **F2: keep.** Label V(v) (infinite norm) against V(v)Ω_s (a vector). Note g_s ∈ 𝒢 (Lemma 3.1(iii)). Show no automorphism between the endpoints.
- **F3: keep.** Merge it with F6 into one two-panel figure, captioned as the 25 September corrections require.
- **F4: keep, change.** Pair it with E1. Label the cone "exact, speed ≤ 1 for every g ∈ 𝒞_H". The switch at |t| = r_j/2 is a switch of the bound, not of the correlation.
- **F5: keep.** Label it "simplicity only; the gap is an output".
- **F6: merge into F3** as its right panel. The x-axis is the plateau distance; mark d₀ and the trivial bound 2. It shows an upper bound, for one χ.
- **F7: keep, change.** Add the cut view of A3. Part II goes in its own panel, with the wording of docs/status.md verbatim.

## F. Traps

| tempting wording | correct wording |
|---|---|
| "unique vacuum" | canonical for the cutoff family (Cor 12.3); uniqueness among locally normal ground states is not claimed (§1.3(a), p. 4; §14, p. 32) |
| "the GJS / Wightman vacuum" | the limit of the Hamiltonian cutoff net, equal to GJ3's limit points; no reverse Osterwalder–Schrader reconstruction is used (abstract) |
| "mass gap", "the gapped limit", "exponential clustering of ω_∞" | (G) holds for H(g), uniformly in g ∈ 𝒞_H; nothing is stated about a GNS Hamiltonian of ω_∞; eq. (34) is one bound inside the proof of Thm 13.2 |
| "ground state" without qualifier | ground state of (𝔄,α) in the spectral sense, with α imported (A6(ii)); not a Haag–Kastler vacuum: no Lorentz covariance appears in the record |
| "norm convergence and local normality are the news" | convergence of the full unaveraged net, with a rate (A2) |
| "compactness-free" | no compactness argument selects the limit state (G2) |
| "the ground-state vectors converge" | only the states converge, on each 𝔄(O) |
| "for every spatial cutoff" | items (1)–(4) along 𝒢; item (5) on 𝒞_H; 𝟙_{[−L,L]} is in 𝒞_H but not in 𝒢 |
| "automorphic equivalence" or "spectral flow" | a bound on d/ds ω_{g_s}(A) for A ∈ 𝔄(O) |
| "converges in norm" | converges in the norm of each 𝔄(O)\* |
| "excludes symmetry breaking" | at weak coupling, (B1)–(B4) cannot hold together; all four are load-bearing; the proof also uses Thm 12.2(1), (3), (4) |
| "closing C5 removes the condition" | C5 is a transcription check of the GJS pages (A8 only); closing it leaves U_GJS a hypothesis |
| "proved" | proved, conditional on U_GJS |

## G. Findings

**G1 (MINOR, attribution).**
- *Where:* §1.4 first paragraph (p. 4, lines 251–260); §1.1 (p. 3, lines 132–134).
- *The record says:* "produced a vacuum as a w\* limit point … Theorem 12.2 asserts convergence … in the norm of every local dual — the strongest locally uniform statement available … Norm convergence on local duals also transports normality".
- *Why it fails:* neither passage says what GJ3 Thm 2.3 (printed p. 211, rendered) states: "the sequence ω_n↾𝔄(B) ∈ 𝔄(B)\* … lies in a norm compact subset of 𝔄(B)\*. Any limit point ω↾𝔄(B) is normal." §1.1 cites Thms 2.1–2.3 only for "locally Fock". Thm 2.1 on the same page also states: "The spectrum of the generator H of time translations is contained in the interval [0, ∞)". A reader can therefore credit the topology and the normality to the new theorem.
- *Repair:* one sentence of context, and drop "strongest … available".

**G2 (MINOR, exposition).**
- *Where:* §1.2 (p. 3, line 166) "compactness-free"; §1.4 (p. 4, line 271) "no compactness anywhere".
- *Why it fails:* Thm 5.1 Step 6 (line 1233), Lemma 7.1 (line 1343) and Lemma 7.3 (line 1416) extract weakly convergent subnets of bounded families in ℋ. The limits are identified uniquely by graph closedness, so nothing is selected, but the sentences are literally false.
- *Repair:* "no compactness argument selects the limit state".

**G3 (MINOR, definitions).**
- *Where:* Hyp 13.1 (B1) and (B4) (p. 31), §1.3(a) and §14 use "ground state of (𝔄,α)" without qualifier.
- *Why it fails:* the only definition is the spectral one inside Prop 12.1. Step 3 of Thm 13.2's proof applies (B4) to ω_∞, which is known to be a ground state only in that sense; under a GNS definition, a bridging argument would be missing.
- *Repair:* define the term once, or append "(in the spectral sense of Proposition 12.1)".

**G4 (MINOR, statement versus proof).**
- *Where:* Cor 12.3 (p. 31) claims "every w\* limit point … constructed in [GJ3, §2]", while its proof fixes g ∈ 𝒢, i.e. g ≤ 1.
- *Why it matters:* GJ3 (2.3) (p. 210, rendered) takes "g(x) to be a nonnegative C₀^∞ function equal to one on the interval [−3, 3]", with no upper bound. This is harmless, because GJ3 Thm 5.1 (p. 250, rendered) assumes "0 ≤ g(x) ≤ 1" and is applied to the g_n of (2.3).
- *Repair:* add "(with g ∈ 𝒢)" to the statement.

**G5 (MINOR, typo).** Lemma 7.1 proof (p. 18, line 1349): `\|le` renders as "∥Qψ̂_{T_α}∥le C₈^{1/2}" (checked in main.pdf). It should read `\le`.

**No CRITICAL or MAJOR finding in my area.** I checked the following step by step and found them sound: the Lemma 9.2 constants; the locality identity and P₀ terms of Lemma 9.3; the parallel gauge of Prop 8.2; the shell count of Prop 10.4; the reduction of the hermitian-functional norm to self-adjoint contractions; Thm 11.1 Steps 1–3; the sign conventions and the n→∞, T→∞ limits of Prop 12.1; the averaging identity and uniform plateau bound of Cor 12.3; and Prop 2.7 and Lemma 2.8.

## H. My reader's first question

My community will ask first: *"Is ω_∞ a new state, or the Glimm–Jaffe vacuum with a new proof? And in what sense is it a ground state?"*

Answer: it is the Glimm–Jaffe vacuum: by Cor 12.3, every w\* limit point of GJ3's averaged construction equals ω_∞. GJ3 had already shown such limit points to be locally Fock and of positive energy, with the averaged states norm-compact on each local algebra; that is context (GJ3 Thms 2.1–2.3, in the record's own bibliography).

What the record adds, at weak coupling and conditional on U_GJS, is that there is nothing left to select. The unaveraged net over all plateau cutoffs converges in every local norm, with a rate that depends only on the plateau distance. So the vacuum is canonical, and translation invariant without averaging.

"Ground state" means the following. ω_∞ is invariant under α, Glimm–Jaffe's patched dynamics (imported, A6(ii)). Its two-point functions t ↦ ω_∞(Aα_t(B)) are continuous, and ∫f(t)ω_∞(Aα_t(B))dt = 0 whenever ∫f(t)e^{itE}dt vanishes on [0,∞). The limit inherits this through the identity (P) on |t| < d(g,O).

Not claimed:
- uniqueness among locally normal ground states;
- identification with the Euclidean vacuum;
- any spectral property of a GNS Hamiltonian of ω_∞;
- Lorentz covariance.
