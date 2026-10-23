# Memo R1 — `editor` (handling editor)

## A. Must know

1. **Theorem 12.2 is proved, conditional on U_GJS and on the imports A1–A8. For 0 ≤ λ/m₀² < ε_P, the full plateau net (ω_g)_{g∈𝒢} converges in norm on every 𝔄(O), with ‖(ω_g − ω_∞)|𝔄(O)‖ ≤ Ψ_{m₁}(d) whenever g ≡ 1 on O_d. The limit is locally normal, translation invariant and, for even 𝒫, ℤ₂ invariant, and it is a ground state of (𝔄, α) in the spectral sense.** Thm 12.2, p. 30; eq. (31), p. 28; Def 2.1, p. 6.
2. **U_GJS is one constant C₈ with |∫Q(x⁰) dq_{h_{T,g}}| ≤ C₈‖Q(x⁰)‖_GJS for all T > 0 and g ∈ 𝒞_H. It is the cutoff-uniform form of GJS Thm 1.1.8 on the slab family, imported at the scope at which the source states it (p. 629) and uses it (pp. 594–597). It is not a quantifier strengthened beyond the source. It remains a named hypothesis, because it is assembled from four pages and the cluster expansion is not re-derived.** A8(vi), eq. (U_GJS), and A8(vii′), p. 10; Scope paragraph, p. 11; App C, p. 35. It is consumed only in Thm 5.1 and Lemmas 7.1–7.3 (Prop C.7, p. 38).
3. **The proof has two layers, joined by two cutoff-uniform estimates. The Euclidean layer yields the moment (M₂) and the gap (G). The Hamiltonian layer turns these into a Cauchy estimate in every local dual 𝔄(O)\*, so no compactness argument selects the limit.** Thm 5.1, p. 16; Thm 7.8, p. 21; Prop 10.4, eq. (27), p. 27; Thm 11.1, p. 28.
4. **The Cauchy estimate rests on two exact ingredients: the inverse-energy filter, which turns the gap into decay in time, and the speed-one light cone, which turns time into distance. They meet in the two-regime bound. The rate decays faster than every inverse power and, by this method, not exponentially.** Lemma 9.1, eq. (18), p. 24; Prop 2.7, p. 12; Lemma 10.3, eq. (26), p. 27; Lemma 10.5, eq. (30), p. 28; §1.4, p. 5.
5. **Three things are not claimed: uniqueness of ω_∞ among locally normal ground states, a sharp (exponential) rate, and anything outside weak coupling. The dichotomy, Thm 13.2, is conditional on Hyp 13.1.** Abstract, p. 2; §1.3, p. 4; §14, pp. 32–33; Thm 13.2, p. 31.

## B. Should know

1. The net is indexed by plateau cutoffs, ordered by inclusion of plateau interiors. The rate depends on O only through d(g, O). Def 2.1, p. 6; Thm 11.1, p. 28.
2. The gap is an output. The slab vacuum ψ̂_s → Ω_g uses only simplicity of the ground state, so the transfer is not circular. A1 (Scope), p. 7; Lemma 4.4, p. 16.
3. (G) comes from printed CE2, through semigroup decay of centred polynomial vectors, which are total by a density theorem. U_GJS enters through the slab moments. Lemma 7.4, p. 19; Prop 7.5, p. 20; Thm 7.7 and Thm 7.8, p. 21.
4. (M₂) bounds the vector V(h)Ω_g, not the operator V(h). Only perturbation cells evaluated in the ground state enter the estimate. Thm 5.1, p. 16; Lemma 10.2, eq. (25), p. 26.
5. Clustering with one unbounded local argument: boundary functions with spectra in [γ, ∞) and (−∞, −γ] coincide on |t| < R by locality, and a Gaussian separator gives 2‖XΩ‖‖A‖e^{−γR/2}. Lemma 9.2, eq. (19); Lemma 9.3, eq. (23); p. 25.
6. At each cutoff, for |t| < d(g, O), the ground-state property is an exact identity, obtained from the patching (P). Local norm convergence passes it to the limit. Prop 12.1, p. 29; A6, eq. (P), p. 9.
7. The limit is canonical, not unique. Every w\* limit point of the Glimm–Jaffe states, averaged or unaveraged, agrees with ω_∞ on each 𝔄(O). Cor 12.3, p. 31.
8. "Explicit rate" means explicit in terms of existential GJS constants (m₁, C₈, K₁, K₂, and ε_P through M_*, λ_*) and of one filter χ. No number is computed. §2.6, p. 13; eq. (M₂), p. 16; eq. (29), p. 28; App A, p. 33.

## C. Pointer table: what the companion does not make the reader read

| item | why it is routine or bookkeeping | where |
|---|---|---|
| A1–A7 | standard construction inputs, literal pinpoint quotations | pp. 7–9 |
| A8(i)–(iii), (vii′); Source Facts 2.2–2.4 | verbatim transcriptions of the source; §4 paraphrases (vii′) | pp. 9–11 |
| Remark 2.5 | consistency of Wick orderings | p. 12 |
| Prop 2.6 | two lines from A5 | p. 12 |
| Lemma 2.8 | covariance and parity bookkeeping for item (4) | p. 12 |
| Lemma 3.1 | memberships of the cutoff classes; stability of affine paths | p. 13 |
| Prop 3.2, Remark 3.3 | dilation to the printed condition; one sentence suffices | pp. 13–14 |
| Lemmas 4.1–4.3 | FKN extended from bounded to unbounded arguments | p. 15 |
| Cor 5.2 | φ⁴ arithmetic | p. 17 |
| Lemma 6.1, Prop 6.2, Remark 6.3 | counting cells; GJS norms of monomials | pp. 17–18 |
| Lemmas 7.1–7.3 | slab limits of moments, by weak-graph arguments | pp. 18–19 |
| Lemma 7.6; proof of Thm 7.7 | the density machinery; state the result only | pp. 20–21 |
| Prop 8.1; proof of Prop 8.2 | path regularity; keep eq. (15) only | pp. 22–23 |
| proof of Lemma 9.2 | optimising the separator; keep the idea | p. 25 |
| Lemma 10.2 | partition of unity; keep ‖V_jΩ_s‖ ≤ M | p. 26 |
| Prop 10.4 Steps 3–4; proof of Lemma 10.5 | count of shells, integration in s, sums of tails | pp. 27–28 |
| §13 | conditional dichotomy; one paragraph | pp. 31–32 |
| App A, App B | table of constants; provenance register | pp. 33–34 |
| App C (C.1–C.6) | source-mechanism audit and h-uniform stability: context for U_GJS, not proof steps; keep Prop C.7's one line | pp. 35–38 |

## D. The longest chain

From the printed GJS estimates to Theorem 12.2(1):

1. Scaling to the source's hypotheses. Prop 3.2, p. 13.
2. Slab FKN at fixed g, extended to unbounded arguments. Lemmas 4.1–4.3, p. 15.
3. ψ̂_s → Ω_g, by simplicity only. Lemma 4.4, p. 16.
4. V(h)² as a single GJS observable; U_GJS; weak-graph passage. Thm 5.1, eqs. (4)–(6), pp. 16–17.
5. GJS norms of cylinder monomials. Prop 6.2, p. 18.
6. Moment transfer; one- and two-point slab limits. Lemmas 7.1–7.3, pp. 18–19.
7. CE2 across a strip. Lemma 7.4, p. 19.
8. Semigroup decay of centred vectors. Prop 7.5, p. 20.
9. Exponential moments, then density. Lemma 7.6, Thm 7.7, pp. 20–21.
10. Uniform gap. Thm 7.8, p. 21.
11. Path regularity and Ω̇_s = −H_s⁻¹Q_sV(v)Ω_s. Props 8.1–8.2, eq. (15), pp. 22–23.
12. Exact filter. Lemma 9.1, eq. (18), p. 24.
13. The state derivative as a time integral. Lemma 10.1, eq. (24), p. 26.
14. Exact light cone. Prop 2.7, p. 12.
15. Separation, hence clustering with one unbounded argument. Lemmas 9.2–9.3, eqs. (19) and (23), p. 25.
16. Each cell bounded by M. Lemma 10.2, eq. (25), p. 26.
17. Two-regime bound. Lemma 10.3, eq. (26), p. 27.
18. One-path estimate, at most eight cells per shell. Prop 10.4, eq. (27), p. 27.
19. Super-polynomial rate. Lemma 10.5, eqs. (29)–(30), p. 28.
20. Cauchy in each 𝔄(O)\*; a state; the rate passes to the limit. Thm 11.1, eqs. (31)–(32), p. 28.
21. Assembly. Thm 12.2, p. 30.

**Cut.** Each piece has at most three steps and ends at a checkpoint displayed from the record.

| piece | steps | checkpoint |
|---|---|---|
| I | 1–3 | ψ̂_s → Ω_g, no gap used (Lemma 4.4) |
| II | 4–5 | (M₂) |
| III | 6–8 | ⟨ψ_Q, e^{−tH(g)}ψ_Q⟩ ≤ Ĉ_Q e^{−m₁t} (Prop 7.5) |
| IV | 9–10 | (G) |
| V | 11–13 | eq. (24) |
| VI | 14–16 | eq. (23) applied to V_j, with ‖V_jΩ_s‖ ≤ M |
| VII | 17–18 | eq. (27) |
| VIII | 19–21 | eqs. (30) and (31), then Thm 12.2(1) |

The identification branch has two steps: Prop 12.1 gives item (3), and Lemma 2.8 with eq. (T) gives item (4). Pieces I–IV form companion §5, V–VII form §6, and VIII with the identification forms §7.

## E. Figures

**Own proposal E1: "Two affine paths, one quantifier".**
- *Purpose:* make the source-scope reading of U_GJS visible; it is the sceptic's first stop.
- *Drawn:* two panels in the (x⁰, x¹) plane.
  - Left: GJS's path h₁ + α(h₂ − h₁) between two arbitrary cutoffs of the p. 589 class, labelled "Thm 1.1.7 at every cutoff, one constant (pp. 594–595)".
  - Right, in #8250df: the record's slab path h_{T,g_s} = (1−s)h_{T,g} + s·h_{T,g′}. It marks where U_GJS is consumed (Thm 5.1, Lemmas 7.1–7.3) and where CE2 is consumed (Lemma 7.4).
- *Computed:* nothing.
- *Must not suggest* that the uniformity is re-derived, that GJS state U_GJS in one theorem, or that the picture is evidence. The caption repeats "named hypothesis; C5 open".

No further proposals: the budget goes to five figures.

**Verdicts on F1–F7.**
- **F1: keep, change.**
  - Draw two layers with the interface (G_γ) + (M₂) between them.
  - CE2 solid; U_GJS dashed in #8250df.
  - Colour exactly the nodes downstream of U_GJS: Thms 5.1, 7.8, 11.1 and 12.2; Prop 10.4; Lemma 10.5; Prop 11.2; Cor 12.3.
  - Leave uncoloured, with labels: Prop 8.2 and Lemma 9.3, "holds under (G_γ) alone"; Lemma 9.1, "operator theory, independent of A8"; Prop 12.1, "holds for any norm limit".
  - Add the identification branch: (P) → Prop 12.1 → item (3), and (T) → item (4).
  - It must not suggest that the record proves the GJS boxes, or that the five items share one provenance.
- **F2: change.** Merge with F4 into one figure with two panels.
  - Left: g, g′, g_s, and v = g′ − g vanishing on O_d.
  - Right: the cone and the two regimes.
  - Formulas (15) and (24) go in the caption.
  - It must not suggest that V(v) is small or bounded, or any approximate (Lieb–Robinson-type) locality: the cone is exact.
- **F3: change.** Merge with F6 into one computed figure with three panels: Ŵ_γ with its notch; |W_γ| on log-log axes with its envelope; the two summands of Ψ_γ. The caption states:
  - γ = 1, M = 1, one χ, `docs/figures/make_figures.py`, and a grid to t = 160 with values below 10⁻⁹ set to zero;
  - Lemma 9.1(i) proves only W_γ ∈ L¹ with finite moments;
  - the shape "t⁻² early, t⁻⁶ late" belongs to this χ;
  - Ψ is an upper bound, never a measured decay.

  It must suggest no decay law and no meaningful heights.
- **F4: keep**, as the right panel of F2+F4, with both branches of eq. (26) labelled.
- **F5: keep, simplify.** Show the slab [−T, T] × supp g, the sharp-time line, ψ_T = e^{−TH(g)}Ω₀ → Ω_g "simplicity only", and "gap: an output (Thm 7.8)". It must not suggest a gap input, or a T-limit uniform in g (the limits are taken at fixed g).
- **F6: merge into F3.**
- **F7: drop as a figure.**
  - A 61-node map is bookkeeping, which is the opposite of the weighting the companion exists for.
  - Its "24" comes from a `\ref`-graph heuristic that misclassifies Lemma 7.4 (G1).
  - Replace it with F1's colouring, a hand-checked column in the pointer appendix ("uses U_GJS / uses CE2 / neither"), and the Part II status table printed as a table.

## F. Traps

1. "Proved", or "unconditional", for Thm 12.2 → "proved, conditional on U_GJS (and the imports A1–A8)". The same holds for Thms 5.1, 7.8, 11.1 and 13.2, Prop 11.2 and Cor 12.3, whose statements do not repeat the condition (G3).
2. "GJS prove U_GJS", or "U_GJS strengthens GJS" → the brief's §3 wording, verbatim.
3. "The unique vacuum", or "the P(φ)₂ vacuum" → "the limit of this cutoff family; GJ3's construction does not depend on subsequences or averaging (Cor 12.3)". Uniqueness is not claimed, nor identification with GJS's Euclidean theory (no reverse OS reconstruction is used).
4. "The limit has mass gap m₁" → item (5) is a gap of the cutoff Hamiltonians H(g), g ∈ 𝒞_H. No gap is claimed for the limit theory.
5. "Converges in norm" → "in norm on every 𝔄(O)", not on 𝔄. The states converge; the vectors Ω_g are not claimed to.
6. "Exponential convergence" → "faster than every inverse power; not exponential by this method". The quadratic model's poly(d)e^{−2m₁d} comes from the note `m2/`, which is outside the document of record.
7. "Explicit constants" → formula (29) is explicit, but in existential GJS constants and one χ.
8. Lemma 9.1(i) → it gives only W_γ ∈ L¹ with finite moments of every order, hence T_γ(r) ≤ C_{q,γ}(1+r)^{−q}. The computed shape of the kernel is a numerical observation about one χ. Ψ_γ is an upper bound, never a measured decay of any state.
9. "Compactness-free" → "no compactness argument selects the limit state". Weak compactness in ℋ is used in Thm 5.1 and Lemmas 7.1–7.3 (G4).
10. "Thm 13.2 excludes phase transitions" → "(B1)–(B4) cannot hold together at weak coupling; all four are load-bearing; GJS75/76 do not supply (B4)" (Remark 13.3).
11. "Solves GRS Problems 1–2", or "first proof" → "a Hamiltonian counterpart of Problem 2; Problem 1 is neither established nor needed; no such theorem was identified in the references reviewed" (§1.1, §14).
12. "Independently verified" → "internal gates G0–G6, plus adversarial passes that the README says the assistant ran; not refereed; C5 open; human verification ongoing".
13. "C5 decides U_GJS" → "C5 checks transcription; closing it does not change the status of U_GJS".
14. "Cannot be made unconditional" → "the Hamiltonian bypass for (M₂) is recorded as dead, a verdict on the printed record and not a no-go theorem; Level 2 (an h-trace of GJS pp. 598–629) is the only proportionate route and is not scheduled".
15. "24 of 61 are conditional" → print the number only with its definition and the caveat about Lemma 7.4 (G1), or not at all.
16. "Part II closed" → "open at gate (II.11)" (root README), plus one sentence on the record's inconsistency.

## G. Findings about the record itself

*Basis.* I read all of `part_i/main.tex` in this session: the abstract; §1; §2 with A8, its Scope paragraph and (vii′); every statement; the proofs of §§3–12 in full; §§13–14; Appendices A–C. I also read `docs/extract.py`, the README, the status pages, `part_i/README.md`, the C5 record, the Part II items, and the strategy entries. I rendered GJ3 pp. 210 and 250 from `refs/`. In the proofs I read, I found no step that fails. Every finding below is MINOR.

- **G1 (MINOR; blocks F7 as specified).**
  - *Where:* README, "What Theorem 12.2 rests on": "A statement is marked conditional exactly when its proof chain reaches A8 … Twenty-four of the sixty-one numbered statements are." `docs/status.md` has the same claim, "computed, not asserted".
  - *Why it fails:* `docs/extract.py` computes reachability of the label `A:gjs` only. Source Facts 2.2–2.4 (`sf:CE2`, `sf:CE1`, `sf:printed`) are A8's items (iv), (v) and (vii), but they have no edge to `A:gjs`. So Lemma 7.4 (p. 19), whose proof applies Source Fact 2.2 (GJS Thm 1.1.7 = A8(iv)), is shown as "independent of A8". Cor 5.2, the φ⁴ instance of (M₂), has no `\ref` at all and is shown as independent too.
  - Conversely, forward references count as dependencies:
    - Prop 3.2 "cites U_GJS" only through Remark 3.3's pointer to Thm 12.2;
    - Lemma 4.3's statement is hypothesis-guarded, and its proof only names where U_GJS later supplies the hypothesis.
  - *Recount:* with the Source Facts treated as A8, the same closure gives 26: the original 24, which include A8 itself, plus Lemma 7.4 and Remark C.6. Counting the three Source Facts gives 29.
  - *Repair:* map the `sf:*` labels to A8, separate "consumes (U_GJS)" from "refers to", and regenerate.
- **G2 (MINOR).** Proof of Lemma 7.1, p. 18, source line 1349: `\|Q\widehat\psi_{T_\alpha}\|le` prints "‖Qψ̂_{T_α}‖le C₈^{1/2}…". *Repair:* `\le`.
- **G3 (MINOR).** The statements of Thm 5.1 (p. 16), Thm 7.8 (p. 21), Thm 11.1 (p. 28), Prop 11.2 (p. 29), Cor 12.3 (p. 31) and Thm 13.2 (p. 31) do not say "Assume U_GJS", although their proofs consume it; only Thm 12.2 and Prop C.7 do. The standing-import convention of §2.4 covers this formally, but a reader who quotes Thm 7.8 or Thm 13.2 on its own presents it as unconditional. *Repair:* add the clause.
- **G4 (MINOR).**
  - *Where:* §1.2, p. 3, "deliberately Hamiltonian and compactness-free"; §1.4, p. 4, "the net converges (Theorem 11.1) — no compactness anywhere".
  - *Why it fails:* Thm 5.1, Step 6 ("choose T_k → ∞ with V(h)ψ̂_{T_k} ⇀ y weakly") and Lemmas 7.1–7.3 (weakly convergent subnets) use weak compactness in ℋ.
  - *Repair:* "no compactness argument selects the limit state".
- **G5 (MINOR).**
  - *Where:* §1.4, Pillar 2(i), p. 5: "a transform analytic in a strip, which cannot vanish on a real neighbourhood of 0 — as Ŵ_γ must — without vanishing identically".
  - *Why it fails:* for the record's Ŵ_γ = χ/E the vanishing holds by construction, so the argument covers every χ of Lemma 9.1. But eq. (18) requires only Ŵ = 1/E on [γ, ∞) together with boundedness, so "must" is not forced. The claim "intrinsic to the method" needs the one-line variant: a function analytic in a strip and equal to 1/E on [γ, ∞) equals 1/E throughout the strip, so it cannot be bounded at 0.
  - *Repair:* "as Ŵ_γ does by construction", and add the variant.
- **G6 (MINOR).**
  - *Where:* Cor 12.3, p. 31. The proof fixes "g ∈ 𝒢 with g ≡ 1 on [−3,3]", which requires 0 ≤ g ≤ 1. GJ3 p. 210, eq. (2.3), as rendered, takes "g(x) to be a nonnegative C₀^∞ function equal to one on the interval [−3, 3]", with no upper bound.
  - *Why it matters:* GJ3's own Thm 5.1 (p. 250: "Let 0 ≤ g(x) ≤ 1 …") supports the restriction, but the record does not say so.
  - *Repair:* one clause in the statement or the proof.
- **G7 (MINOR).** The one-sentence summary of §1.4 (p. 5), "the cluster expansion of [GJS] supplies the gap and one local moment uniformly in the cutoff", drops the condition in the sentence most likely to be quoted. *Repair:* "…supplies, granted U_GJS, …".
- **G8 (MINOR).** §1.4, p. 4 contains two unsupported phrases: "the strongest locally uniform statement available" is an unsupported comparative, and "ergodicity-type arguments give extremality of limit points, not uniqueness" has no citation. *Repair:* cut both, or mark them as context.
- **G9 (MINOR for Part I; already known).** The status of Part II is inconsistent across the record:
  - the root README says "open at gate (II.11)";
  - `part_ii/README.md` says "Phase closure: NOT yet reached", "gate (II.11) closed … the cofinal-subnet cluster statement is superseded", and lists "full-sequence … identification … open";
  - `docs/status.md` lists the cofinal-subnet state as "proved unconditionally" and the identification as "open";
  - main.tex §14 (p. 33) says the identified theorem "remains open".

  The companion must not adjudicate.

## H. My reader's first question

The journal's reader asks: *is this a theorem or a reduction, and who has checked it?*

It is an implication, A1–A8 ⇒ Theorem 12.2, with exactly one non-literal import, U_GJS. The record reads U_GJS as the source's own scope but does not re-derive it; hence "proved, conditional on U_GJS". The parts independent of A8 (filter, separation, clustering, path regularity, spectral passage) can be checked without the source. Checking so far consists of internal gates G0–G6, AI-assisted adversarial passes and a page-image dossier; the record is not refereed, and C5 is open.

The companion says this on page 1, in full in §§4 and 9, and repeats the negative scope in §8.

## I. Outline and page budget

Budget: 18.5 pp including five figures (about 2.2 pp of figures), leaving 1.5 pp of slack. A 15-minute path is p. 1 plus §§1, 3 and 8; the 45-minute path is everything except App A.

| § | title | sentence to retain | content (record locators) | fig | pp |
|---|---|---|---|---|---|
| — | front | — | title; notice (L); abstract (L); how to read | — | 1.0 |
| 1 | What is proved, under what | "Theorem 12.2 is proved conditional on one imported estimate, U_GJS." | setting in ten lines (𝔄(O); the classes 𝒞_E, 𝒞_H and 𝒢 ⊂ 𝒞_H; d(g,O)); Thm 12.2 displayed verbatim; claims-ledger box (proved conditional / independent of A8 / not claimed / open) | — | 2.0 |
| 2 | Why it was open | "Compactness gave a vacuum; it did not give convergence." | GJ3's limit point; Expositions "has not been proved"; GRS Problems 1–2 with Newman's note (§1.1); why convergence of Schwinger functions, (1.1.11) as quoted in A8(vii′), does not control norms on 𝔄(O)\*; why the lattice machinery does not start (context: [Hastings], [BMNS]) | — | 1.5 |
| 3 | The architecture | "Two cutoff-uniform estimates, (G) and (M₂), make the net Cauchy." | the two layers; the table in §1.2; checkpoints (G), (M₂), (27), (31) | F1 | 1.5 |
| 4 | The one import that is not a quotation | "U_GJS is the source's quantifier, assembled from four pages and not re-derived; hence the condition." | display (U_GJS); the reading in three steps (a)–(c) with GJS pages; consumers (Prop C.7); what App C is not; C5; Level 2; dead Hamiltonian bypass; A1–A7 as a 7-row table | E1 | 1.5 |
| 5 | Euclidean layer | "The gap is an output: simplicity is the only spectral input." | pieces I–IV | F5 | 2.0 |
| 6 | Hamiltonian layer: local perturbations perturb locally | "An exact filter turns the gap into time decay; an exact light cone turns time into distance." | pieces V–VII; why not exponential | F2+F4, F3+F6 | 3.0 |
| 7 | From Cauchy to the theorem | "The ground-state property costs an identity, not an estimate." | piece VIII; normality; Prop 12.1; invariances; Cor 12.3 (canonical ≠ unique) | — | 1.5 |
| 8 | Boundaries | "Not unique, not sharp, not beyond weak coupling." | the three negatives, with the record's reasons (§1.3, §14); Thm 13.2 in one paragraph; Part II in ≤ ½ page (README wording, one sentence on the inconsistency, the table from docs/status.md) | — | 1.0 |
| 9 | The record | "Every import is pinned to a page; nothing here is refereed." | AI-assisted method; G0–G6, one line each; corrections that changed statements (P1 → Hyp 13.1; R2 constants; 5 Sep scope; 25 Sep wording of the README); C5; how to check (`% src:`, dossier, labels) | — | 1.0 |
| A | Pointer appendix | — | section C, with a hand-checked conditionality column | — | 1.5 |
| B | Notation | — | at most 25 symbols | — | 0.5 |
| — | References | — | the `\bibitem`s of main.tex, plus record files | — | 0.5 |

Arbitration principles I will apply in R2:
- Order by the sceptic's questions: status and import, then mechanism, then limits, then provenance.
- Anything that does not change what the reader believes is true goes to Appendix A.
- Part II ≤ ½ page; App C ≤ 3 body lines; §13 ≤ one paragraph.
- Each contextual remark from AQFT or QI ≤ 3 lines, marked as context.

## J. Editorial rules I will enforce in R4

1. No paragraph with more than three inferential steps without a displayed checkpoint. A checkpoint is a display transcribed from main.tex with its number and page.
2. Every section opens with its sentence to retain (italic, ≤ 30 words) and closes with a one-line "In the record:" pointer.
3. One figure per Tier-2 idea; five figures in all. Each caption says what is drawn and what is computed, and by which script, and ends "Illustration, not evidence." #8250df is used only for what is conditional on U_GJS.
4. Forward references go only to numbered statements of the record. The companion numbers nothing of its own except sections, figures and displays.
5. Status words only from proved / partial / conjectured / numerical / refuted. In each section, the first mention of a statement that depends on U_GJS carries "conditional on U_GJS".
6. The wording of U_GJS is frozen to the brief's §3.
7. No new mathematics. Contextual remarks begin "Context." and cite only the `\bibitem`s of main.tex.
8. Numbers come only from `labels.md`; pages are printed pages of main.pdf, which equal the PDF index (checked).
9. Banned unless quoted with correction: unique vacuum, mass gap of the limit, exponential rate, unconditional, verified, first, solves, strongest, compactness-free, clearly, obviously.
10. Page budgets are hard. Overruns are cut from §§5–6, never from §§1, 4 or 8.
11. The notation freeze of main.tex §2.3 applies, with ≤ 25 symbols, each defined before first use.
12. Statements about a source are phrased as the record's quotations ("GJS p. 629, as quoted in A8(vii)"). The companion does not vouch for transcriptions (C5).
13. Disagreements with the record go to the R5 list, never into the text.

## K. The referee's first three questions

1. *"Is U_GJS a theorem of GJS? If it is, why is the result conditional; if it is not, what is missing?"* → §4 and E1: the display, the reading in three steps, the four consumers (Prop C.7), what App C is not, C5, and Level 2.
2. *"GJS already prove convergence of the cutoff Schwinger functions at rate e^{−m₁d/2} ((1.1.11), as quoted in A8(vii′)(a)). What does norm convergence on 𝔄(O)\* add, and why is your rate only super-polynomial?"* → §2 (moments do not control norms on local von Neumann algebras; GJ3 has only a limit point; Cor 12.3), §6 (the filter obstruction) and §8 (the quadratic model; §14's remark that a sharp rate would need resolvent or Combes–Thomas input).
3. *"V(g′) − V(g) has infinite norm, and continuum bosons have no Lieb–Robinson bound. How is the derivative along the path controlled, domains included?"* → §6, with F2+F4: Prop 2.6 (domains), eq. (15), eq. (18), Prop 2.7, eq. (23) with X unbounded, (M₂) via eq. (25), and eqs. (26)–(27).

Runner-up: "In what sense is ω_∞ a ground state, and is α imported?" → §7: Prop 12.1; α is imported in A6(ii).

## L. Draft abstract and page-1 notice

**Abstract (draft).** A reading guide to a 40-page research record on the spatially cutoff P(φ)₂ model; it proves nothing new. The record's Theorem 12.2 states that, for 0 ≤ λ/m₀² < ε_P, the full net of cutoff ground states ω_g (plateau order, no subnets, no averaging) converges in norm on every local algebra 𝔄(O). The rate is faster than every inverse power of the distance from O to the plateau edge. The limit is locally normal, translation and (for even P) ℤ₂ invariant, and a ground state of the Glimm–Jaffe dynamics in a spectral sense. The theorem is proved conditional on U_GJS, a cutoff-uniform Glimm–Jaffe–Spencer moment estimate. The record imports it at the scope at which the source states and uses it, and does not re-derive it. We explain why the question was open, how a uniform gap and an exact light cone replace compactness, and what is not claimed.

**Page-1 notice (draft).** *Read this first.* This companion explains a research record and proves nothing new. The record is AI-assisted and has not been refereed; human verification is ongoing. Its main result, Theorem 12.2, is proved conditional on the imported hypothesis U_GJS (Assumption A8(vi)), which is not re-derived. Audit item C5, a second human reading of the source page images, is open. Statement numbers refer to part_i/main.tex; figures are illustrations, not evidence.

## M. Section 1.4 of main.tex: what is right, what must change

§1.4 (pp. 4–5) is a sound first draft of companion §§3, 5, 6 and 7, and its order should be kept. Its fault is density: six paragraphs, each with four to seven inferential steps and no display. The eight checkpoints of section D must go in, and the scope parentheticals must move to §4.

1. **Topology.** *Right:* limit point versus convergence; norm on local duals; Cor 12.3; normality via Prop 11.2. *Change:* drop "the strongest locally uniform statement available" (G8).
2. **Why standard tools fail.** *Right:* the infinite norm of V(g′) − V(g); moments versus norms; Cauchy rather than compactness. *Change:* "no compactness anywhere" becomes "no compactness selects the limit" (G4). Cut the uncited ergodicity clause, or mark it as context (G8).
3. **Pillar 1.** *Right:* the two inputs; the slab FKN device; "simplicity only", so no circularity; density is needed. *Change:*
   - split it into two chains of at most three steps: slab → (M₂), and CE2 → decay → density → (G);
   - move the list of the density proof's five techniques to Appendix A;
   - replace the scope parenthetical with "consumed in Thm 5.1 and Lemmas 7.1–7.3 (Prop C.7)".
4. **Pillar 2.** *Right:* eq. (15); the three moves; "the operator-algebraic softening of the unboundedness" (this is §6's best sentence). *Change:*
   - fix the filter-obstruction parenthetical (G5);
   - the closing sentence assembles three steps (partition, two-regime split, eight cells) without a checkpoint, so display eqs. (26) and (27);
   - mark the "quantitative substitute for strip-analyticity arguments" as context.
5. **Assembly and identification.** *Right as written.* §7 can follow it almost verbatim, and "costs an identity, not an estimate" is §7's sentence to retain.
6. **Boundaries and the one-sentence summary.** *Right* on the three negatives and the conditional dichotomy. *Change:* the summary must carry "granted U_GJS" (G7). The companion's version must also mention C5 and the AI-assisted status, which §1.4 never does.
