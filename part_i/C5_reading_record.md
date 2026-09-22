# C5 reading record — second human reader, GJS 1974 page images

**Purpose.** Audit closure item C5 (Part I, Appendix B "External residue"; `strategy.md` §5)
is the one residue of the Part I manuscript that is not closable by the machine record:
a second human reader confirms, on the page images in `audit_2026/evidence/`, that the
source passages transcribed into `part_i/main.tex` say what the manuscript says they say.
Every item below is a **verbatim comparison**, not a mathematical judgement.

**Source.** J. Glimm, A. Jaffe, T. Spencer, *The Wightman axioms and particle structure in
the P(φ)₂ quantum field model*, Ann. of Math. **100** (1974) 585–632 (`[GJS]` in main.tex).
Printed page = PDF page + 583 in the JSTOR scan.

**Verdict vocabulary.** For each item enter one of
`MATCHES` (the page image says exactly what the manuscript quotes/uses),
`DIFFERS` (state the difference verbatim),
`AMBIGUOUS` (state what is illegible or open to a second reading).
Leave the mathematics alone: the question is only "does the page say this".

| field | entry |
|---|---|
| Reader | _________________________ |
| Date read | _________________________ |
| Copy used | JSTOR scan (`gjs74.pdf`) / journal print / other: __________ |
| Overall verdict | _________________________ |

Manuscript build the record refers to: `part_i/main.tex`, Scope amendment of
5 September 2026 (title-page quote), Assumption A8 items (i)–(viii) with (vii′).

---

## Items 1–7 (original checklist, 16 August 2026)

### 1. Cutoff class and the measure `dq_h` — p. 589 (PDF 6)
- Image: `gjs-p589-06.png` (also `gjs-source-05/06.png`).
- To confirm: (a) the class is "Let h be a function with compact support in R², and let
  0 ≤ h ≤ 1"; (b) `dq_h` is the normalized interacting measure with cutoff h; (c) the
  phrase describing the limit is "h → 1 through rectangular cutoffs" (or record the exact
  wording); (d) footnote 5: "The construction [17] of the measure dq assumes Theorem 1.1.7,
  and consequently the n = 0 case of Theorem 1.1.11."
- Manuscript sites: A8(i) (class `\mathcal C_E`, `lem:classes`), A8(vi) (slab family
  `\mathcal C_E^{slab}` ⊂ `\mathcal C_E`), Scope paragraph step (a).
- Verdict: ________  Notes: ______________________________________________

### 2. Localized monomials, localization squares, N(Δ) — p. 593 (PDF 10)
- Image: `gjs-theorems-10.png`.
- To confirm: (1.1.5)–(1.1.6); the localization squares are unit lattice squares centred at
  lattice sites (record the exact convention printed); N(Δ) counts fields localized in Δ;
  the degree restriction n_i < n̄; footnote 9 wording.
- Manuscript sites: A8(ii), Remark 6.3 (`rem:row`), Lemma 7.4 (`lem:ce2strip`).
- Verdict: ________  Notes: ______________________________________________

### 3. The norms (1.1.7)–(1.1.9) — p. 594 (PDF 11)
- Image: `gjs-theorems-11.png`.
- To confirm, character by character: ‖Q‖ = K₁[∏_Δ K₂^{2N(Δ)} N(Δ)!] ‖w‖₂ and the same for
  ‖Q(x₀)‖ with ‖w(x₀,·)‖₂; **one** overall K₁ (first power); local weight K₂^{2N(Δ)}
  (exponent 2N(Δ), not N(Δ)); N(Δ)! (not (2N)!); (1.1.9) ‖Q‖ = Σ_i ‖Q_i‖ for sums of
  localized monomials.
- Manuscript sites: `eq:printednorm`, every explicit constant (e.g. the (M₂) constant
  M² = 9 C₈ K₁ K₂^{8p′} (4p′)! λ² (Σ|a_n|)² in §5), gate R2 note in the Scope paragraph.
- Verdict: ________  Notes: ______________________________________________

### 4. Theorem 1.1.7 (CE2) and the dilation — p. 594 (PDF 11) and p. 590 (PDF 7)
- Images: `gjs-theorems-11.png`, `gjs-scaling-07.png`.
- To confirm: Theorem 1.1.7 reads "Let m₀, K₂ and K₁ be sufficiently large and let λ be
  sufficiently small. There are constants 0 < m₁ and O(1) independent of h, Q₁ and Q₂ such
  that (1.1.10) |∫Q₁Q₂dq_h − ∫Q₁dq_h ∫Q₂dq_h| ≤ O(1) e^{−m₁d} ‖Q₁‖ ‖Q₂‖"; d is "the width of
  the widest strip bounded by two parallel lines, and separating the {Δ⁽¹⁾} from the
  {Δ⁽²⁾}" (any orientation); p. 590: the dilation sends (m₀, λ) ↦ (s⁻¹m₀, s⁻²λ).
- Manuscript sites: Source Fact 2.2 (`sf:CE2`), Lemma 7.4, Proposition 3.2 (`prop:scaling`).
- Verdict: ________  Notes: ______________________________________________

### 5. Theorem 1.1.8 (CE1) verbatim — p. 595 (PDF 12)
- Image: `gjs-theorems-12.png`.
- To confirm: "THEOREM 1.1.8. For Q(x₀) of the form (1.1.5), |∫Q(x₀)dq_h| ≤ O(1)‖Q(x₀)‖,
  uniformly as h → 1."; the Feynman–Kac identity ∫Q(x₀)dq = ⟨Ω, θ⟩ with θ from (1.1.13);
  the Remark's n-point bound |S_h(f₁⊗…⊗f_n)| ≤ n! ∏`|f_i|_{\mathcal S}` with the norm "independent of h".
- Manuscript sites: Source Fact 2.3 (`sf:CE1`). The one-sentence statement is a
  limit-uniformity statement; the scope actually used is fixed by items 6, 8, 9.
- Verdict: ________  Notes: ______________________________________________

### 6. The uniformity sentence and the special-case identification — p. 629 (PDF 46)
- Images: `gjs-uniform-46.png`, `gjs-uniformity-46.png`.
- To confirm: (a) "It is important to work with a translation invariant Hamiltonian, in
  order that time translation preserve subspaces of bounded momentum. The estimates of
  Theorems 1.1.8, 1.1.11, 3.1 and 4.1 are uniform in the space cutoff h, and the path space
  integrals converge as h → 1. Thus these theorems hold in the infinite volume limit, and we
  proceed to work in the limit h = 1."; (b) earlier on the same page: "Theorem 1.1.11 follows
  from this inequality, while Theorem 1.1.8 is the special case B = I, n = 0."; (c) the h of
  (a) is the dq_h cutoff of p. 589 (no other cutoff has been introduced under that name).
- Manuscript sites: Source Fact 2.4 (`sf:printed`), (vii′)(c), Scope paragraph step (c),
  Appendix C intro.
- Verdict: ________  Notes: ______________________________________________

### 7. Hamiltonian cutoff class and ground state — p. 588 (PDF 5)
- Image: `gjs-source-05.png`.
- To confirm: (1.6) and the class of spatial cutoffs for H(g); essential self-adjointness;
  the ground eigenvalue is simple (record the exact statement and any citation the source
  gives for it).
- Manuscript sites: A8(i), A1 cross-reference.
- Verdict: ________  Notes: ______________________________________________

---

## Items 8–9 (added 5 September 2026 — scope of U_GJS)

### 8. Affine-path application of Theorem 1.1.7 — pp. 594–595 (PDF 11–12)
- Images: `gjs-theorems-11.png` (foot of p. 594), `gjs-theorems-12.png` (top of p. 595).
- To confirm, against Assumption A8(vii′)(a): (a) "For test functions f_i ∈ C₀^∞(`\mathcal O`) and for
  cutoff functions h₁ and h₂, we assert that (1.1.11) … ≤ O(1)e^{−m₁d/2} where
  d = dist(`\mathcal O`, suppt h₁ − h₂) [sic: "suppt" as printed], and then Theorem 1.1.1 follows."; (b) "let g = h₂ − h₁, and
  define g_i = gχ_{Δ_i}"; (c) (1.1.12): the derivative is taken along h₁ + αg, α ∈ [0, 1],
  and the three displayed lines match the manuscript's transcription (V(g), V(g_i),
  ⟨·⟩_{h₁+αg}); (d) "We apply Theorem 1.1.7 to each term in the sum to obtain
  |⟨Q⟩_{h₂} − ⟨Q⟩_{h₁}| ≤ Σ_{i∈Z²∩supp g} O(1)e^{−m₁ dist(`\mathcal O`,Δ_i)} ≤ O(1)e^{−m₁d/2}."; (e) "As a
  special case, the cutoff Schwinger functions S_h converge as h → 1."
- What this settles: the source applies Theorem 1.1.7 with its h-independent constant at
  every cutoff h₁ + α(h₂ − h₁) of an affine path between **arbitrary** cutoff functions of the
  p. 589 class — not only at rectangular cutoffs and not only in the limit. The manuscript's
  path h_{T,g_s} = (1−s)h_{T,g} + s h_{T,g′} is this family (Scope paragraph step (a)).
- Note that no restriction on h₁, h₂ beyond "cutoff functions" appears between (1.1.11) and
  the end of the proof; if the reader finds one, record it verbatim.
- Verdict: ________  Notes: ______________________________________________

### 9. Derivation of Theorem 1.1.7 from Theorems 1.1.8 and 1.1.11 — pp. 596–597 (PDF 13–14)
- Images: `gjs-proof-14.png` (p. 597); the proof heading is the last line of p. 596
  (PDF 13; the scan's OCR layer reads "Proof of Theorem 1.1.7, assuming Theorems 1.1.8 and
  1.1.11. Take").
- To confirm, against Assumption A8(vii′)(b): (a) heading as above; (b) "n = 0 in Theorem
  1.1.11 Then Q is a polynomial of degree zero, i.e., a constant. From the choice B = I, it
  follows that Q = ∫A dq_h + O(1)‖A‖e^{−m₀(1−ε)T}."; (c) "After rotating and translating the
  strip separating Q₁ and Q₂ in Theorem 1.1.7, and after choosing A = Q₁, B_T = Q₂ in Theorem
  1.1.11, the proof follows from Theorem 1.1.8, (1.1.16) and the above determination of Q.";
  (d) p. 596, (1.1.16): "|∫(A − Q)B_T dq_h| ≤ O(1)‖A‖‖B‖e^{−γT} uniformly in h. We shall
  choose t_j = j, j ∈ Z."
- What this settles: the h-independent constant of Theorem 1.1.7 is obtained from Theorem
  1.1.8 **at the same h**. Since the manuscript uses Theorem 1.1.7 as printed at the
  non-rectangular slab cutoffs h_{T,g} (Lemma 7.4, Proposition C.7), the constant of Theorem
  1.1.8 must be uniform on the same class — which is exactly U_GJS (Scope paragraph step (b)).
- Verdict: ________  Notes: ______________________________________________

---

## What a completed record closes

- All nine `MATCHES`: C5 is closed; Appendix B "External residue" and `strategy.md` §5 can be
  updated to "closed on <date> by <reader>". The status of U_GJS does not change (it remains
  an import at source scope, by design), but its transcription is then independently
  confirmed.
- Any `DIFFERS`: quote the difference here, then check whether a constant or a quantifier
  in `main.tex` depends on it (items 3, 4 → §§5–7 constants; items 6, 8, 9 → A8(vi) scope).
- Any `AMBIGUOUS`: consult a second copy of the source (journal print or a higher-resolution
  scan) before recording a verdict.
