# V3 audit of Appendix C, `part_i/main.tex`: Lemmas C.2, C.3, C.4 and Theorem C.5

> Copied into the council record from the session scratchpad on 2 November 2026 (orchestrator). The numerics
> files named below as `audits/v3-numerics/…` are in `ugjs/council/v3-numerics/` (the output file renamed
> `check_bounds.output.txt`, since `*.out` is git-ignored as a LaTeX artefact); the rendered page images
> (`audits/v3-pages/`, scans of Simon's book and of the record) stay outside the repository.
> Errata noted by the KB reviewer of 2 November 2026 (orchestrator's note, text below unchanged): §9 contains ten
> repairs, R1–R10; the "R1–R8" of the orchestrator's drafting instructions, of the KB node as first written and of
> the commit message of e436654 undercounted them (the report itself never says R1–R8); and of the chaos facts
> cited in M-3, (I.21) p. 11, Γ_n p. 17 and (I.32) p. 25 are in chapter I of Simon's book, not in chapter V.

Round V3 of `ugjs/PLAN.md` Part 5. Auditor: a fresh agent (Claude Opus 5.5) that wrote neither the record nor the
note. Started 31 October 2026, interrupted by a usage limit, resumed and finished 2 November 2026.
Standard: AGENTS.md §§1–5. Verdict words: holds / gap (severity) / false / not checked.

## Verdict

Lemmas C.2–C.4 and Theorem C.5 are true. I re-derived every displayed computation in the four proofs and each one
checks out; I found no false statement and no CRITICAL gap. As written, however, they are not `proved` in the sense of
AGENTS.md §2, so **Lemma C.2 and Theorem C.5 cannot be load-bearing as written**. Each of the following three
load-bearing steps is asserted without a proof and without an imported statement (MAJOR):

- **M-1** (= PLAN F13, upgraded from MINOR). The "classical Bessel facts" and the four kernel bounds of Lemma C.4
  (l. 2989–2993) are neither cited nor derived, and K₀ is never defined (l. 2901).
- **M-2.** The variance bound c_κ ≤ (1/2π) log κ + C_* (l. 2917), which Lemma C.3 consumes, is justified only by
  "(translation invariance)". That shows c_κ does not depend on z; it does not give the bound. C_* is defined nowhere.
- **M-3.** The record never says what 𝒰_h is as an element of L²(dμ₀). A2 and A3 give only the formal expression and
  integrability. Yet Lemma C.2 ("Wick monomials of degree ≥ 1 have mean zero"), Lemma C.4 ("By the Wick isometry",
  including the cross term) and Theorem C.5 ("a sum … of Wick chaoses", Γ(e^{−t})Y_r = e^{−rt}Y_r) all use the
  chaos structure of 𝒰_h. The needed facts are printed in the chapter of Simon's book that A3 already cites. I read them
  this session at the locators in §1, but the record does not import them.

None of the three needs new mathematics. §9 writes out every repair: elementary derivations of all Bessel and
kernel bounds from K₀(x) = ∫₀^∞ e^{−x cosh t} dt with explicit constants, an explicit C_*, an import paragraph for A3,
and explicit thresholds. Add the MINOR bookkeeping of §8 as well. The main items are:

- the thresholds b₀, b₁ and "b large" written as inequalities;
- c₁ > 0;
- the statement of Theorem C.5 recording that its bound depends on Λ only through |Λ| and diam Λ.

With those repairs, Lemmas C.2–C.4 and Theorem C.5 are `proved`. They then rest on these imports: A3 (Lemma C.2 only),
A4, and the Simon definitional facts. All three uses the PLAN makes hold:

1. Z(h) ≥ e^{−λ|a₀||Λ|}.
2. S₂(B) < ∞, from Theorem C.5 at p = 2, with a bound that depends on B only through |B| and diam B.
3. ‖Y‖₄ ≤ 3^{p′}‖Y‖₂. This holds for every Y in the chaoses of degree ≤ 2p′ of any Gaussian L²-space and is verbatim
   Simon Thm I.22. Citing Thm I.22 also covers the note's use under dφ₀, which the proof of C.5, written on L²(dμ₀)
   only, does not literally cover.

## 0. Object, version, locators

- **Object.** `glimm_jaffe/part_i/main.tex`, `\subsection*{The two $h$-sensitive analytic facts, proved}`, l. 2898–3058
  (Remark C.6 to l. 3069). Printed page = PDF page index; I checked the footers of pp. 39–42. Per the current `main.aux`:
  - the notation paragraph: pp. 39–40;
  - Lemma C.2 (`lem:Z`, l. 2922), Lemma C.3 (`lem:wick`, l. 2937), Lemma C.4 (`lem:uv`, l. 2968): p. 40;
  - Theorem C.5 (`thm:stability`, l. 3010): p. 41;
  - inputs: A2 (`A:fkn`, l. 497, p. 8), A3 (`A:stability`, l. 526, p. 8), A4 (`A:hyper`, l. 547, p. 9),
    Remark 2.5 (`rem:conv`, l. 912, p. 14), §2.6 (l. 977, with "Throughout, $0\le\lambda/m_0^2<\varepsilon_{\mathscr P}$"
    at l. 991, p. 14), Definition 2.1 (l. 402, p. 7).
- **Version audited.** `main.tex` with mtime 2 Nov 2026 15:35:23. The audited ranges are saved verbatim in
  `audits/v3-pages/audited-text-snapshot.txt`. SHA-256 prefixes: l. 2898–3069 `52fa91a9d90cd33a`; l. 497–572
  `1577465e371d32bf`. I re-checked both immediately before writing this report; they were unchanged.
- **Line-number drift, for the orchestrator.** `labels-main.txt` (31 Oct) is now stale: by +2 for every Appendix C
  label, and by +1 for `app:provenance`. The coordinator's resume message said a display in M5 had been split and that
  lines after l. 2835 had shifted by one. What I observe is different:
  - The M5 display (l. 2837–2842) is now an `align*` with the same number of lines as before.
  - The shift is +1 between l. 2655 and l. 2687, and +2 from l. 2766 (`app:huniform`) onward. I did not identify
    those edits.
  - `main.tex` was modified twice on 2 Nov while I worked (15:34:16 and 15:35:23). `main.pdf` was rebuilt each time:
    43 pp, then 42 pp.
  - On re-reading, the audited text is identical to the text I read on 31 Oct. A4's "Sources" sentence (l. 560–561)
    was reworded, with no change of content.

  All locators below are current line numbers.

## 1. Sources read this session, and the inputs as the record states them

**Record, A3** (l. 527–533, p. 8), verbatim: "For every $h\in\CE$: $\mathcal U_h\in L^p(d\mu_0)$ for every $p<\infty$,
and $e^{-\varrho\,\mathcal U_h}\in L^1(d\mu_0)$ for every finite $\varrho>0$. In particular
$0<Z(h):=\int e^{-\mathcal U_h}d\mu_0<\infty$, and the interacting measures $dq_h:=Z(h)^{-1}e^{-\mathcal U_h}\,d\mu_0$,
$h\in\CE$, are well-defined probability measures." Source (l. 535): "\cite[Thm.~V.7]{SimonBook} and its chapter
context."

**Record, A4** (l. 548–558, p. 9), verbatim: "The free time-zero Markov semigroup $\mathsf P_T$ satisfies
$\|\mathsf P_TF\|_{q}\le\|F\|_{p}$ whenever $\frac{q-1}{p-1}=e^{2m_0T}$, $1<p\le q<\infty$. More generally (the
abstract form of the same source): for the second quantization $\Gamma(c)$ of a contraction $c$ on the one-particle
space of any Gaussian $L^2$-space, $\|\Gamma(c)F\|_{q}\le\|F\|_{p}$ whenever $\|c\|^2\le(p-1)/(q-1)$; the display is
the case $c=e^{-T\mu}$, and the Mehler case $c=e^{-t}\mathbf 1$ on $L^2(d\mu_0)$ is the form used in
Appendix~\ref{app:huniform}." Source (l. 560): Simon Thm I.17.

**Record, definition of 𝒰_h.** A2 (l. 499–500) reads "for $h\in\CE$, $\mathcal U_h:=\lambda\int h(z){:}\mathscr
P(\Phi(z)){:}\,dz$". No construction is given anywhere in the record. Remark 2.5 (l. 914–918) fixes dμ₀-Wick ordering
for *sharp-time* functionals only. "K_0" occurs once in the file (l. 2901) and is never defined. "Wick isometry" and
"chaos" occur only in Appendix C.

**Simon, *The P(Φ)₂ Euclidean (Quantum) Field Theory*.** Copy: `refs/`. PDF page = printed page + 22.
Read this session on page images unless marked "text layer".

| printed page (PDF page) | what I read |
|---|---|
| p. 11 (33) | Theorem I.3, "(I.21) ⟨:f^n: :g^m:⟩ = δ_{nm} n!⟨fg⟩^n". Remark 2: ":f^n: = H_n(f)" for ⟨f²⟩ = 1, with generating function exp(αx − α²/2). |
| p. 17 (39), text layer | "Γ_n(H) denotes the subspace of Γ(H) spanned by the {:φ(f_1)…φ(f_n):}". |
| p. 25 (47) | "(I.32) Γ(A):φ(f_1)…φ(f_n): = :φ(Af_1)…φ(Af_n):" for a contraction A on a real Hilbert space H. |
| p. 34 (56; dossier image `simon-hyper-056`) | Theorem I.17, "Let H_1 and H_2 be real Hilbert spaces and let A: H_1 → H_2 be a contraction. Let p, q ∈ (1,∞) with p ≤ q so that ‖A‖ ≤ (p−1)^{1/2}/(q−1)^{1/2} (I.42). Then Γ(A) is a contraction from L^p(Q_{H_1},dμ_{0,H_1}) to L^q(Q_{H_2},dμ_{0,H_2})". |
| p. 38 (60) | Theorem I.22, "Γ_F(H) ⊂ ∩_{p<∞} L^p(Q_H, dμ_0); explicitly if ψ ∈ ⊕_{n=0}^m Γ_n(H), then ‖ψ‖_p ≤ (p−1)^{m/2}‖ψ‖_2 (I.47) for all p > 2". Its proof is the record's proof of the comparison, with c = (p−1)^{−1/2}. |
| p. 136 (158) | ":φ^m(g): is then defined as the unique random variable in Γ_m(H) with ⟨:φ(h_1)…φ(h_m):, :φ^m(g):⟩ = m!∫[∏_j h(x_j)S(x_j,y)]g(y)dxdy. (V.3)" Also Proposition V.1 and condition (V.4). |
| p. 137 (159) | "In case (V.4) holds: ‖:φ^m(g):‖²_{Γ(H)} = m!∫g(x)g(y)S(x,y)^m dxdy". Theorem V.2(a): ":φ^n: exists for any n as a random process for L^{1+ε}(R²) for each ε ∈ (0,1]. Moreover, for any such ε and any p ≥ 2, ‖:φ^n(g):‖_p ≤ c(p−1)^{n/2}‖g‖_{1+ε} (V.6a)". |
| p. 138 (160), text layer | Theorem V.2(b), the time-zero analogue (V.6b). |
| p. 152 (174; dossier image `simon-exp-174`) | Theorem V.7(a), "Let P be a fixed semibounded polynomial. … If g ≥ 0, g ∈ L¹ ∩ L^{1+ε}(R²), then exp(−∫g(x):P(φ(x)):d²x) ∈ ∩_{p<∞} L^p(Q_N, dμ_{0,N})". |

**Do A3 and A4 suffice?**

- **A3.** Its second clause is Thm V.7(a): take g = h, which is ≥ 0, bounded and compactly supported, so
  h ∈ L¹ ∩ L^{1+ε}; take P := ϱλ𝒫, which is semibounded for ϱλ ≥ 0. Its first clause is Thm V.2(a) (V.6a), not
  Thm V.7; A3 gives no pinpoint for it (m-9). For Appendix C, A3 supplies 𝒰_h ∈ L¹, which Lemma C.2 needs, and nothing
  else.
- **A4.** Its abstract form is Thm I.17 squared. It drops "p, q ∈ (1,∞), p ≤ q", which the display keeps. Appendix C
  uses p = 2 ≤ q < ∞, inside the printed range. A4 supplies the hypercontractive contraction and nothing else. How
  Γ(c) acts on the chaoses is Simon (I.32), which A4 does not quote (m-7).
- **Neither** import supplies the chaos structure of 𝒰_h (M-3).

## 2. Lemma C.2 (normalisation), l. 2922–2935, p. 40

| # | claim, locator | verdict |
|---|---|---|
| C2.1 | Statement (l. 2924–2927): "For every $h\in\CE$ with $\supp h\subseteq\Lambda$: $Z(h)\ge e^{-\lambda\lvert a_0\rvert\,\lvert\Lambda\rvert}>0$, and $Z(h)<\infty$ by Theorem C.5. Hence $dq_h$ is a well-defined probability measure on the whole class $\CE$." | holds (proof incomplete until M-3 is repaired) |
| C2.2 | 𝒰_h ∈ L¹(dμ₀). | holds: A3, first clause (l. 527). After R8 it also follows from 𝒰_h ∈ L². |
| C2.3 | E[𝒰_h] = λa₀∫h (l. 2931–2932), "since Wick monomials of degree $\ge1$ have mean zero". | holds; **gap MAJOR (M-3)**. The n = 0 term is λa₀∫h. For n ≥ 1, :φ^n(h): lies in Γ_n by definition (Simon (V.3)), and Γ_n ⊥ constants by (I.21) with m = 0. The record states neither the definition nor a source. The sentence is true for the dμ₀-Wick ordering of (V.3), which is the only reading consistent with A3's source. |
| C2.4 | E[𝒰_h] ∈ [−λ\|a₀\|\|Λ\|, λ\|a₀\|\|Λ\|] (l. 2931). | holds. Uses λ ≥ 0 (l. 991) and 0 ≤ ∫h ≤ \|Λ\| (h takes values in [0,1] and vanishes off Λ); \|Λ\| is Lebesgue measure. Both h ≥ 0 and h ≤ 1 are used (m-3). |
| C2.5 | Jensen (l. 2933–2934): Z(h) ≥ e^{−E[𝒰_h]}. | holds. exp is convex, μ₀ is a probability measure, 𝒰_h ∈ L¹. The direction is correct, and the inequality holds even if Z(h) were +∞. |
| C2.6 | "Z(h) < ∞ by Theorem C.5" (l. 2925–2926). | holds. C.5 at p = 1 bounds Z(h) = ‖e^{−𝒰_h}‖₁. There is no circularity: C.5's proof uses Lemmas C.3, C.4 and A4, not Lemma C.2 and not Z(h). A3 gives the same bound independently. It is a forward reference only. |
| C2.7 | "well-defined probability measure on the whole class 𝒞_E". | holds: take Λ := supp h, which is compact. |

After R8, Lemma C.2 is `proved` from A3 and the Simon definitional import.

## 3. Lemma C.3 (Wick lower bound), l. 2937–2966, p. 40

| # | claim, locator | verdict |
|---|---|---|
| C3.1 | Hermite expansion (l. 2951–2953): ":𝒫:_c(x) = Σ_{m=0}^{2p′}β_m x^m with β_{2p′} = a_{2p′} and \|β_m\| ≤ C(𝒫)(1+c)^{(2p′−m)/2} (each power c^j comes with x^{n−2j})". | holds. He_n are the probabilists' Hermite polynomials; the record leaves them undefined (m-2). Expanding, c^{n/2}He_n(x/√c) = Σ_{j≤n/2}(−1)^j n!/(j!(n−2j)!2^j) c^j x^{n−2j}, so β_m = Σ_{n≡m (2), m≤n≤2p′} a_n(−1)^{(n−m)/2} n!/(((n−m)/2)! m! 2^{(n−m)/2}) c^{(n−m)/2}. Since c^{(n−m)/2} ≤ (1+c)^{(2p′−m)/2} for n ≤ 2p′, this gives C(𝒫) := Σ_n\|a_n\| max_j n!/(j!(n−2j)!2^j). This identification of :𝒫:_c with the Wick ordering at variance c agrees with Simon p. 11, Remark 2, together with homogeneity. |
| C3.2 | Weighted AM–GM display (l. 2956–2959). | holds. Young's inequality with explicit C_{p′} (R7). |
| C3.3 | Summing gives min_x :𝒫:_c ≥ −C′_{p′}Σ_m(\|β_m\|^{2p′}/A^m)^{1/(2p′−m)} (l. 2960–2961). | holds. The 2p′ terms with m < 2p′ each cost (A/4p′)x^{2p′}, leaving (A/2)x^{2p′} ≥ 0; C′_{p′} = C_{p′}. |
| C3.4 | The exponent of (1+c) is p′ "uniformly in m" (l. 2962–2963). | holds: (\|β_m\|^{2p′})^{1/(2p′−m)} ≤ C(𝒫)^{2p′/(2p′−m)}(1+c)^{p′} for every m < 2p′. Hence b(𝒫) of R7. |
| C3.5 | :𝒫:_c(x) ≥ −b(1+c)^{p′} for all c ≥ 0 and x ∈ ℝ (l. 2939–2940). | holds for c > 0. At c = 0 the defining formula divides by √c; read it as the polynomial of C3.1, so that :𝒫:_0 = 𝒫 (m-2). |
| C3.6 | c_κ ≤ (1/2π)log κ + C_*, used at l. 2945 (stated at l. 2917). | holds; **gap MAJOR (M-2)**. True, with an explicit C_* in R6, but not derived in the record. |
| C3.7 | First inequality of the display (l. 2944–2945): "from $h\ge0$, $\int h\le\lvert\Lambda\rvert$, and the pointwise bound applied under the integral" (l. 2963–2965). | holds, pathwise. 𝒰_{h,κ}(Φ) = λ∫h(z):𝒫:_{c_κ}(Φ_κ(z))dz is defined for every Φ ∈ 𝒮′(ℝ²), because z ↦ Φ(δ_κ(z−·)) is C^∞. The step uses λ ≥ 0, h ≥ 0, ∫h ≤ \|Λ\| (so h ≤ 1 is used too, m-3), and monotonicity of c ↦ (1+c)^{p′}. |
| C3.8 | Second inequality, κ ≥ 2: ≥ −c₁(λ,𝒫,Λ)(log κ)^{p′}. | holds with c₁ of R7. c₁ depends on (λ, 𝒫, \|Λ\|, m₀, ‖δ‖_∞), and on Λ only through \|Λ\| (m-4). With the natural choice, c₁ = 0 when \|Λ\| = 0 (m-6). |
| C3.9 | Lemma C.3 is pathwise; Lemma C.4 and Theorem C.5 treat 𝒰_{h,κ} as an element of ⊕Γ_n. | holds. The two agree μ₀-a.s. by Fubini: (z,Φ) ↦ :Φ_κ(z)^n: is jointly measurable, with second moment bounded uniformly in z. The record does not say so (m-8). |

## 4. Lemma C.4 (ultraviolet difference), l. 2968–3008, p. 40

| # | claim, locator | verdict |
|---|---|---|
| C4.1 | Statement (l. 2970–2975): ‖𝒰_h − 𝒰_{h,κ}‖²_{L²(dμ₀)} ≤ c₂κ^{−1}(log κ)^{2p′} for all h ∈ 𝒞_E with supp h ⊆ Λ and all κ ≥ 2. | holds; c₂ is explicit in R9. c₂ depends on (λ, 𝒫, m₀, ‖δ‖_∞, \|Λ\|, diam Λ), not only on "(λ, 𝒫, Λ)" (m-4). It is uniform in h. |
| C4.2 | Wick isometry identity (l. 2979–2986), with G^{(1)}_κ := (δ_κ⊗1)*G and G_κ := (δ_κ⊗δ_κ)*G: the displayed sum over n = 1..2p′ with kernel G^n − 2(G^{(1)}_κ)^n + G_κ^n; "(the c_κ-Wick ordering makes the diagonal subtractions match; degree 0 cancels)". | holds given R8; **gap MAJOR (M-3)**. Write f_z := δ_κ(z−·). The n-th chaos components are λa_n:φ^n(h): and λa_n∫h(z):φ(f_z)^n:dz, and components of different n are orthogonal ((I.21)). Then: ‖:φ^n(h):‖² = n!∬hhG^n (Simon p. 137); ⟨:φ(f_z)^n:, :φ^n(h):⟩ = n!∫((δ_κ*G)(z−y))^n h(y)dy by (V.3) with all n test functions equal to f_z; ⟨:φ(f_z)^n:, :φ(f_{z′})^n:⟩ = n!G_κ(z−z′)^n by (I.21). Integrating in z, z′ (Fubini) gives the display. Because δ and G are even, G^{(1)}_κ(ζ) = (δ_κ*G)(ζ) and G_κ = δ_κ*δ_κ*G. The c_κ-Wick power of Φ_κ(z) is the dμ₀-Wick power of the Gaussian variable φ(f_z), whose variance is c_κ, so it lies in Γ_n. Any other Wick constant would add lower-chaos terms and break the identity. The degree-0 terms are λa₀∫h on both sides and cancel. |
| C4.3 | Reduction using \|h\| ≤ 1_Λ (l. 2986–2989): "it suffices to bound ∬_{Λ×Λ}\|G^n − J^n\|". | holds. G^n − 2J₁^n + J₂^n = 2(G^n − J₁^n) − (G^n − J₂^n), so the factor 3 is implicit. Also ∬_{Λ×Λ}\|F(z−z′)\| ≤ \|Λ\|∫_{\|ζ\|≤R}\|F\| with R = diam Λ. h ≥ 0 is not used here. |
| C4.4 | G(ζ) = (1/2π)K₀(m₀\|ζ\|) (l. 2901). "The classical Bessel facts 0 < G(ζ) ≤ C(1+\|log\|ζ\|\|)e^{−m₀\|ζ\|} and \|∇G(ζ)\| ≤ C(\|ζ\|^{−1}+1)e^{−m₀\|ζ\|}" (l. 2989–2991). | holds; **gap MAJOR (M-1, = F13)**. Both facts are true; R1–R3 derive them with C_G, C_∇ explicit. Neither is cited or derived in the record, and K₀ is undefined. |
| C4.5 | "J(ζ) ≤ C(1+log κ) for all ζ, and \|J(ζ) − G(ζ)\| ≤ Cκ^{−1}(\|ζ\|^{−1}+1) for \|ζ\| ≥ 4/κ" (l. 2991–2993). | holds (R4, R5); **part of M-1**. Not derived in the record. The derivation needs G to be radially nonincreasing (K₀′ = −K₁ < 0) and ‖δ_κ*δ_κ‖_∞ ≤ κ²‖δ‖_∞. |
| C4.6 | First region (l. 2995–3000): ∫_{\|ζ\|<4/κ}[G^n+J^n] ≤ … ≤ C′_nκ^{−2}(log κ)^n. | holds (R9). This includes 2 ≤ κ < 4, where 4/κ > 1. |
| C4.7 | Second region (l. 3001–3005): ∫_{4/κ≤\|ζ\|≤R} n max(G,J)^{n−1}\|G−J\| ≤ C_nκ^{−1}∫₀^R(1+\|log r\|)^{n−1}(1+r)dr ≤ C_n(R)κ^{−1}. | holds. The tacit step max(G,J) ≤ C(1+\|log r\|) on 4/κ ≤ r ≤ R follows immediately from the two stated bounds (R5, J3). Polar coordinates turn (r^{−1}+1)·r dr into (1+r)dr. If R < 4/κ the region is empty. |
| C4.8 | Final form c₂κ^{−1}(log κ)^{2p′} (l. 2974, 3006–3007). | holds. The two regions give O(κ^{−2}(log κ)^{2p′}) + O(κ^{−1}) ≤ c₂κ^{−1}(log κ)^{2p′} for κ ≥ 2, using (log κ)^{n−2p′} ≤ (log 2)^{n−2p′}. The logarithmic power is generous, since the proof actually gives O(κ^{−1}); this is harmless. |
| C4.9 | "the single use of the *upper* bound on h" (l. 2987–2988). | holds as a statement about Lemma C.4. As exposition it is inaccurate: Lemmas C.2 and C.3 use h ≤ 1 too (m-3). |

## 5. Theorem C.5 (h-uniform stability), l. 3010–3058, p. 41

| # | claim, locator | verdict |
|---|---|---|
| C5.1 | Statement (l. 3012–3016): for every p < ∞ and compact Λ, sup{‖e^{−𝒰_h}‖_{L^p(dμ₀)} : h ∈ 𝒞_E, supp h ⊆ Λ} < ∞. | holds. The class is {h ∈ 𝒞_E : supp h ⊆ Λ} with Λ any compact set, and the bound is uniform in h. The proof gives more than the statement records: the supremum is ≤ (1+e^{pb_*})^{1/p} with b_* = b_*(p, p′, c₁, c₂) (R10). So the bound depends on Λ only through \|Λ\| and diam Λ, which makes it translation- and rotation-invariant. The statement should say so (m-4), because the note needs a bound that depends on the shape of the box only. |
| C5.2 | λ = 0 is trivial (l. 3020). | holds. |
| C5.3 | "$Y:=\mathcal U_h-\mathcal U_{h,\kappa}$ is a sum $Y=\sum_{r=0}^{2p'}Y_r$ of Wick chaoses" (l. 3021). | holds given R8; **gap MAJOR (M-3)**. 𝒰_h ∈ ⊕_{n≤2p′}Γ_n by (V.3); 𝒰_{h,κ} too (Bochner integral in the closed space Γ_n; C3.9). |
| C5.4 | Comparison ‖Y‖_{L^q} ≤ (q−1)^{p′}‖Y‖_{L²} for q ≥ 2, with its proof (l. 3023–3031). | holds. Checks: (a) A4 applies with p = 2, q = 1+e^{2t}, c = e^{−t}𝟙, since ‖c‖² = e^{−2t} = (p−1)/(q−1) and 2 ≤ q < ∞ is inside Simon's range. (b) Γ(e^{−t})Y_r = e^{−rt}Y_r is Simon (I.32) on Γ_r (p. 25) together with the definition of Γ_r (p. 17); it is not in A4's text (m-7, M-3). (c) ‖Z‖₂² = Σ_r e^{2rt}‖Y_r‖₂² ≤ e^{4p′t}‖Y‖₂², because r ≤ 2p′, t ≥ 0 and the chaoses are orthogonal. (d) e^{2p′t} = (q−1)^{p′}. The statement and proof are verbatim Simon Thm I.22 (I.47) at m = 2p′ (p. 38). |
| C5.5 | The PLAN's ‖Y‖₄ ≤ 3^{p′}‖Y‖₂. | holds: q = 4. The derivation uses only that Y lies in ⊕_{r≤2p′}Γ_r. Scope: the proof is written on L²(dμ₀). For the note's V(h′) on L²(dφ₀), cite Simon Thm I.22, or repeat the derivation with A4's abstract form on the time-zero Gaussian space. V(h′) ∈ ⊕_{n≤2p′}Γ_n of that space by Simon Thm V.2(b) (p. 138, text layer). The sign of h′ plays no role. |
| C5.6 | "For $b\ge b_0(\lambda,\mathscr P,\Lambda)$ choose $\kappa=\kappa(b)$ by $c_1(\log\kappa)^{p'}=b/2$" (l. 3033–3034). | holds after R10. The choice needs c₁ > 0 (m-6). It also needs κ ≥ 2, the hypothesis of Lemmas C.3 and C.4, and 2q ≥ 2, the hypothesis of the comparison at exponent 2q. The record never says that b₀ must secure these (m-5). R10's b₀ := 2c₁(4p′ log 2)^{p′} secures both. |
| C5.7 | {𝒰_h ≤ −b} ⊆ {𝒰_h − 𝒰_{h,κ} ≤ −b/2} (l. 3035–3036). | holds μ₀-a.s.: Lemma C.3 gives 𝒰_{h,κ} ≥ −b/2 everywhere. |
| C5.8 | Chebyshev in L^{2q} plus Lemma C.4 (l. 3037–3043). | holds. μ₀(\|Y\| ≥ b/2) ≤ (2/b)^{2q}‖Y‖_{2q}^{2q} ≤ (2/b)^{2q}(2q)^{2p′q}(c₂e^{−L}L^{2p′})^q, using (2q−1)^{p′} ≤ (2q)^{p′} and κ = e^L. The right-hand equality is algebra. |
| C5.9 | 2q = exp(L/4p′), "the bracket is ≤ (2√c₂/b)L^{p′}e^{−L/4} ≤ e^{−1} for b ≥ b₁" (l. 3044–3046). | holds. (2q)^{p′} = e^{L/4}. The bracket *equals* (2√c₂/b)L^{p′}e^{−L/4} = (√c₂/c₁)e^{−L/4}, because L^{p′} = b/(2c₁). This makes b₁ explicit (R10). |
| C5.10 | Pr[𝒰_h ≤ −b] ≤ exp(−exp((b/2c₁)^{1/p′}/4p′)), "uniformly over the stated class" (l. 3047–3051). | holds: bracket^{2q} ≤ e^{−2q}, and c₁, c₂ do not depend on h. |
| C5.11 | "≥ 2pb for b large" (l. 3052–3053). | holds. A threshold b₂(p) exists (R10) but is not stated (m-5). |
| C5.12 | "$\|e^{-\mathcal U_h}\|_{L^p}^p=\int_0^\infty pe^{pb}\Pr[\mathcal U_h\le-b]\,db+O(e^{pb_1})<\infty$" (l. 3054–3055). | holds as an inequality, ≤ e^{pb_*} + 1 with b_* = max{b₀, b₁, b₂(p)} (R10). Written as an equation with threshold b₁ it is loose (m-5). |
| C5.13 | "Every constant above came from Lemmas C.3–C.4, which used exactly $h\ge0$ and $h\le1$" (l. 3056–3057). | holds: plus the universal hypercontractive constant and the thresholds. |
| C5.14 | Is every constant derived? | no. C, C_*, C_n, C′_n, C_n(R) (inside M-1, M-2) are named but not derived, and so are C(𝒫), C_{p′}, C′_{p′}, b₀, b₁ and "b large" (m-4, m-5). R6–R10 derive all of them. |

## 6. Boundary cases

| case | verdict |
|---|---|
| p′ = 1, 𝒫 = a₂x² + a₁x + a₀ | holds. By hand, :𝒫:_c(x) = a₂x² + a₁x + a₀ − a₂c ≥ −(a₁²/(4a₂) + \|a₀\| + a₂c) ≥ −b(1+c). In Lemma C.4 only n ≤ 2 occur. In Theorem C.5, L = b/(2c₁), 2q = e^{L/4}, the tail is exp(−e^{b/(8c₁)}), and the comparison constant is (q−1)¹. |
| κ = 2 | holds. Lemma C.3: c₁ must absorb (1 + (log 2)/(2π) + C_*)/log 2, and R7 does. Lemma C.4: the first region is \|ζ\| < 2 and the second is 2 ≤ \|ζ\| ≤ R (empty if R < 2). In Theorem C.5, once b ≥ b₀ of R10 we have κ(b) ≥ 2^{4p′} ≥ 16, so κ = 2 is never used there. |
| Λ a single GJS square (closed unit square) | holds: \|Λ\| = 1, diam Λ = √2, all constants finite. |
| h = 1_Λ | holds. 1_Λ ∈ 𝒞_E (measurable, values in {0,1}, compact support). ∫h ≤ \|Λ\| holds with equality, so it is the extreme case of Lemmas C.2 and C.3. |
| h with small support, or h = 0 | holds. The bounds are stated through Λ, not supp h, and are unchanged. |
| \|Λ\| = 0 (e.g. Λ a segment) | Every h in the class vanishes a.e., 𝒰_h = 0, and Theorem C.5 is trivially true. The proof's κ(b) is undefined, though, because the natural c₁ is 0 (m-6). Repair: use any c₁ > 0 not smaller than the R7 value. |
| p ≤ 1 | holds. p = 1 gives Z(h) < ∞. For 0 < p < 1, ‖·‖_p is a quasi-norm and R10's layer-cake bound is unchanged. |
| Dependence on Λ; translation invariance | The constants are c₁ ∝ \|Λ\| and c₂ ∝ \|Λ\|·max_n K_n(diam Λ), with K_n(R) := ∫₀^R(1+\|log r\|)^{n−1}(1+r)dr nondecreasing in R, and b_* = b_*(p, p′, c₁, c₂). So **the proof's bound depends on Λ only through (\|Λ\|, diam Λ), monotonically, and is translation-invariant as written in the proof** (not in the statement; m-4). For a box B this gives S₂(B) ≤ S̄₂(\|B\|, diam B), which depends on B only through its side lengths; \|B̄\| = \|B\|. The stronger claim that the supremum S₂(B) is itself translation-invariant needs 𝒰_{h(·−a)} to have the same law as 𝒰_h under μ₀. That is not in the record, and I did not check it. The note can avoid it by using the bound. |

## 7. Conventions

- **𝒰_h.** The record does not state the Wick ordering of space-time integrals: A2 (l. 500) and A3 (l. 527) write
  :𝒫(Φ(z)): with no subscript, and Remark 2.5 (l. 914–918) covers sharp-time functionals only. The only reading
  consistent with A3's source is Simon's (V.3) with S = G, i.e. dμ₀-Wick ordering. That reading gives
  𝒰_h = λΣ_n a_n:φ^n(h): ∈ ⊕_{n≤2p′}Γ_n. All four proofs presuppose it (M-3).
- **𝒰_{h,κ}.** The c_κ-Wick ordering (l. 2918–2919) orders the Gaussian variable Φ_κ(z) = φ(f_z) at its own μ₀-variance
  c_κ, so it is also dμ₀-Wick ordering, and the n-th component lies in Γ_n. This is consistent with 𝒰_h: the n-th
  components of 𝒰_h and 𝒰_{h,κ} live in the same chaos, which is exactly what makes Lemma C.4's identity exact. No
  mismatch.
- **"(translation invariance)"** at l. 2917 does justify that c_κ(z) does not depend on z. It justifies nothing else
  there (M-2).
- **"so that 𝒰_{h,κ} → 𝒰_h in every L^p(dμ₀)"** (l. 2918–2920) is asserted and proved nowhere in the record. It follows
  from Lemma C.4 and the comparison in C.5's proof: ‖𝒰_h − 𝒰_{h,κ}‖_q ≤ (q−1)^{p′}(c₂κ^{−1}(log κ)^{2p′})^{1/2} → 0 for
  q ≥ 2, and ‖·‖_q ≤ ‖·‖₂ for q ≤ 2. It is not a premise of C.2–C.5 (m-1).

## 8. Findings

### CRITICAL
None.

### MAJOR

**M-1 (PLAN F13, upgraded now that Lemma C.4 is load-bearing).**
- *Locator:* l. 2989–2993 (p. 40), and l. 2901 (p. 39) for $G(\zeta)=\frac1{2\pi}K_0(m_0|\zeta|)$. F13's "l. 2838"
  is an earlier numbering.
- *Text:* "The classical Bessel facts $0<G(\zeta)\le C(1+|\log|\zeta||)e^{-m_0|\zeta|}$ and
  $|\nabla G(\zeta)|\le C(|\zeta|^{-1}+1)e^{-m_0|\zeta|}$ give, for the average $J$ of $G$ over balls of radius
  $\le2/\kappa$: $J(\zeta)\le C(1+\log\kappa)$ for all $\zeta$, and $|J(\zeta)-G(\zeta)|\le C\kappa^{-1}(|\zeta|^{-1}+1)$
  for $|\zeta|\ge4/\kappa$."
- *Why it fails the standard:* the step is load-bearing (C.4 → C.5 → S₂(B)). It is neither cited nor derived; K₀ is
  undefined; the constants C are not derived. This breaks AGENTS 3.1, 3.4, 3.8 and 4.1.
- *Truth:* the facts are true (R1–R5).
- *Repair:* insert R1–R5, about 15 lines, no citation needed.
- *Severity:* MAJOR.

**M-2.**
- *Locator:* l. 2917 (p. 40). It is consumed at l. 2945 (Lemma C.3) and, through c₁, in Theorem C.5.
- *Text:* "$c_\kappa(z)=\E[\Phi_\kappa(z)^2]\le\frac1{2\pi}\log\kappa+C_*$ (translation invariance)".
- *Why it fails the standard:* the parenthetical yields only that c_κ does not depend on z. The bound itself needs the
  logarithmic singularity of G, and C_* is defined nowhere.
- *Truth:* the bound is true for every κ ≥ 1, with C_* := (1/2π)[(π/2)‖δ‖_∞ + (log(1/m₀))₊ + 1 + log 4] (R6).
- *Repair:* R6. Alternatively, replace the bound by c_κ = G_κ(0) ≤ 8πC_G‖δ‖_∞(1+log κ) (R4 at ζ = 0, κ ≥ 2) and adjust
  c₁.
- *Severity:* MAJOR.

**M-3.**
- *Locators and text:*
  - l. 2931–2933 (p. 40): "since Wick monomials of degree $\ge1$ have mean zero";
  - l. 2979–2986 (p. 40): "By the Wick isometry, … (the $c_\kappa$-Wick ordering makes the diagonal subtractions match;
    degree $0$ cancels)";
  - l. 3021 (p. 41): "is a sum $Y=\sum_{r=0}^{2p'}Y_r$ of Wick chaoses";
  - l. 3029 (p. 41): "$\Gamma(e^{-t})Y_r=e^{-rt}Y_r$".
- *Why it fails the standard:* these steps use four facts:
  - that 𝒰_h = λΣa_n:φ^n(h):, with :φ^n(h): the element of Γ_n fixed by its pairings;
  - the isometry ‖:φ^n(h):‖² = n!∬hhG^n;
  - Wick's pairing formula (I.21);
  - Γ(A) acting on Γ_n.

  None is stated or imported. A2 (l. 499–500) and A3 (l. 527) give only the formal expression and integrability. A3's
  source line (l. 535) says "and its chapter context", and A4 imports only the contraction property. A3's Scope
  sentence (l. 538–539) says the bounds are "re-proved" in Appendix C, but the re-proof rests on structure the record
  never states.
- *Truth:* the facts are true and printed in that very chapter (§1): (V.3) and Prop. V.1 on p. 136; the isometry and
  Thm V.2(a) on p. 137; Thm I.3 (I.21) on p. 11; Γ_n on p. 17; (I.32) on p. 25. Thm I.22 (p. 38) is the comparison
  itself.
- *Repair:* one import paragraph (R8), plus the Fubini remark of C3.9.
- *Severity:* MAJOR by the letter of AGENTS §2, since a load-bearing step rests on an unimported fact. I found no
  mathematical risk.

### MINOR

- **m-1** (l. 2918–2920). "so that $\mathcal U_{h,\kappa}\to\mathcal U_h$ in every $L^p(d\mu_0)$" is unproved where it
  stands. It follows from C.4 and the comparison (§7) and is not a premise. Move it after Theorem C.5, or cite those two.
- **m-2** (l. 2940). He_n is undefined, and its normalisation matters: it should be the probabilists' He_n with
  generating function e^{αy−α²/2}, as in Simon p. 11, Remark 2. The defining formula is also undefined at c = 0. Define
  He_n, and define :𝒫:_c by the polynomial of C3.1.
- **m-3** (l. 2964–2965; l. 2987–2988; Remark C.6, l. 3062–3065). The claim "the single use of the *sign* / *upper*
  bound" is exposition, and inaccurate: h ≤ 1 also enters C.2 (l. 2931–2933) and C.3 (∫h ≤ |Λ|, l. 2964).
  Correctness is unaffected.
- **m-4** (l. 2946, l. 2970, l. 3055–3056).
  - The constants are stated as depending on (λ,𝒫,Λ), or (p,λ,𝒫,Λ). They also depend on m₀ and ‖δ‖_∞, and they depend
    on Λ only through |Λ| and diam Λ.
  - The statement of Theorem C.5 should record this, because the note needs a bound that depends on the shape of the
    box only.
  - C(𝒫), C_{p′}, C′_{p′}, C_n, C′_n and C_n(R) are named but not derived (AGENTS 3.4); R7 and R9 derive them.
- **m-5** (l. 3033; l. 3045–3046; l. 3052–3055).
  - The thresholds b₀, b₁ and "for $b$ large" are not given as inequalities (AGENTS 3.3).
  - b₀'s purpose is not stated, i.e. the hypotheses κ ≥ 2 and 2q ≥ 2 are not checked in writing (AGENTS 3.1).
  - "$=\int_0^\infty\cdots+O(e^{pb_1})$" should read ≤ e^{pb_*} + 1 with b_* = max{b₀, b₁, b₂(p)}.
  - Repair: R10.
- **m-6** (l. 3033–3034). The choice c₁(log κ)^{p′} = b/2 needs c₁ > 0, and the natural c₁ ∝ λ|Λ| vanishes when
  |Λ| = 0. Take any c₁ > 0 not smaller than the R7 value.
- **m-7** (l. 554–556, l. 3026–3031).
  - A4's text drops "p, q ∈ (1,∞), p ≤ q" from the abstract form; the display at l. 551 keeps it. The use is inside the
    printed range.
  - A4 does not contain Γ's action on chaoses (Simon (I.32), p. 25).
  - Cite Simon Thm I.22 (p. 38) for the comparison; that also covers the note's L²(dφ₀) use.
- **m-8** (Lemma C.3 vs Lemmas C.4, C.5). The μ₀-a.s. equality of the pathwise and the chaos definitions of 𝒰_{h,κ}
  is not stated (C3.9). It is a two-line Fubini remark.
- **m-9** (l. 527, l. 535). A3's first clause (𝒰_h ∈ L^p) is Simon Thm V.2(a), (V.6a), on p. 137, not Thm V.7 on
  p. 152. The pinpoint is missing; R8 absorbs it.

## 9. Repairs, written out (each is a new claim; it needs its own audit, per AGENTS 3.10)

Notation: m := m₀ > 0; B(ζ,a) is the closed disc; (x)₊ := max(x,0).

**R1 (G as a heat-kernel integral; definition of K₀).**
1. For real f ∈ 𝒮(ℝ²):
   ⟨f,(−Δ+m²)^{−1}f⟩ = (2π)^{−2}∫|f̂(k)|²(k²+m²)^{−1}dk = ∫₀^∞e^{−sm²}[(2π)^{−2}∫|f̂(k)|²e^{−sk²}dk]ds
   = ∫₀^∞e^{−sm²}∬f(x)f(y)p_s(x−y)dxdy ds,
   with p_s(ζ) := (4πs)^{−1}e^{−|ζ|²/(4s)}. The middle step is Tonelli in s; the last is the Fourier transform of a
   Gaussian.
2. Exchanging the integrals is justified because ∫₀^∞e^{−sm²}∬|f(x)||f(y)|p_s(x−y)dxdy ds ≤ ‖f‖_∞‖f‖₁/m².
3. Hence G(ζ) = ∫₀^∞e^{−sm²}p_s(ζ)ds.
4. For ζ ≠ 0, substitute s = (|ζ|/2m)e^t. Then sm² + |ζ|²/(4s) = m|ζ|cosh t and ds/s = dt, so
   G(ζ) = (1/4π)∫_ℝe^{−m|ζ|cosh t}dt = (1/2π)K₀(m|ζ|), where **K₀(x) := ∫₀^∞e^{−x cosh t}dt** (x > 0).
5. This identifies K₀ in l. 2901. That it is the classical Macdonald function is from memory and is not needed.

**R2 (bounds on K₀; first Bessel fact).**
1. K₀ > 0, and K₀′ = −K₁ with K₁(x) := ∫₀^∞cosh t e^{−x cosh t}dt > 0. Differentiating under the integral is
   dominated by cosh t·e^{−x₀cosh t} on x ≥ x₀ > 0. So K₀ is decreasing and G is radially decreasing.
2. (a) Since cosh t − 1 ≥ t²/2: K₀(x) = e^{−x}∫₀^∞e^{−x(cosh t−1)}dt ≤ √(π/2x)·e^{−x} for all x > 0.
3. (b) For 0 < x < 1, let T := log(4/x). Then ∫₀^T(·) ≤ T. For t ≥ T we have e^t ≥ 4/x > 4, so
   cosh t − 1 ≥ e^t/2 − 1 ≥ e^t/4, and ∫_T^∞e^{−xe^t/4}dt = ∫₁^∞e^{−u}u^{−1}du ≤ e^{−1} (substituting u = xe^t/4).
   Hence K₀(x) ≤ e^{−x}(log(4/x) + e^{−1}).
4. (c) Combining (a) and (b):
   - K₀(x) ≤ (1+log 4)(1+|log x|)e^{−x}. For x ≥ 1 use √(π/2) < 1+log 4; for x < 1 use
     log 4 + e^{−1} + log(1/x) ≤ (1+log 4)(1+log(1/x)).
   - K₀(x) ≤ (log(1/x))₊ + 1 + log 4. For x ≥ 1 use √(π/2)e^{−1} < 1.
5. (d) Since 1+|log(mr)| ≤ (1+|log m|)(1+|log r|):
   **0 < G(ζ) ≤ C_G(1+|log|ζ||)e^{−m|ζ|}, with C_G := (1+log 4)(1+|log m|)/(2π).**

**R3 (gradient; second Bessel fact).**
1. Substituting u = sinh t, K₁(x) = e^{−x}∫₀^∞e^{−x(√(1+u²)−1)}du.
2. Since √(1+u²) − 1 ≥ u − 1, this is ≤ e^{−x}(1 + ∫₁^∞e^{−x(u−1)}du) = (1+1/x)e^{−x}.
3. For ζ ≠ 0, ∇G(ζ) = −(m/2π)K₁(m|ζ|)ζ/|ζ|. So
   **|∇G(ζ)| ≤ (1/2π)(m + |ζ|^{−1})e^{−m|ζ|} ≤ C_∇(1+|ζ|^{−1})e^{−m|ζ|}, with C_∇ := max(1,m)/(2π).**

**R4 (J1).**
1. Let ρ ∈ {δ_κ, δ_κ*δ_κ}. Then ρ is a probability density, supp ρ ⊆ B(0,2/κ), and ‖ρ‖_∞ ≤ κ²‖δ‖_∞ (Young's
   inequality). Set J := ρ*G. By evenness, J = G^{(1)}_κ for ρ = δ_κ and J = G_κ for ρ = δ_κ*δ_κ.
2. For G ≥ 0 radially nonincreasing, ∫_{B(ζ,a)}G ≤ ∫_{B(0,a)}G. Reason: the sets B(ζ,a)∖B(0,a) and B(0,a)∖B(ζ,a) have
   equal measure, G ≤ G|_{|·|=a} on the first, and G ≥ G|_{|·|=a} on the second.
3. For κ ≥ 2, so that a := 2/κ ≤ 1:
   J(ζ) ≤ κ²‖δ‖_∞∫_{B(0,a)}G ≤ κ²‖δ‖_∞C_G·2π∫₀^a r(1+log(1/r))dr = κ²‖δ‖_∞C_G·2πa²(3/4 + ½log(1/a)).
4. Hence **J(ζ) ≤ 8πC_G‖δ‖_∞(1+log κ) for all ζ**.

**R5 (J2, J3).**
1. Let |ζ| ≥ 4/κ and |w| ≤ 2/κ. The segment [ζ−w, ζ] lies in {|ξ| ≥ |ζ|/2}, where G is C¹ with
   |∇G(ξ)| ≤ C_∇(1 + 2|ζ|^{−1}).
2. Hence **|J(ζ) − G(ζ)| ≤ (2/κ)C_∇(1+2|ζ|^{−1}) ≤ 4C_∇κ^{−1}(1+|ζ|^{−1})** (J2).
3. On the same set, κ^{−1} ≤ ½ and κ^{−1}|ζ|^{−1} ≤ ¼. So **max(G,J)(ζ) ≤ (C_G + 3C_∇)(1+|log|ζ||)** (J3). This is the
   step used tacitly in C.4's second display.

**R6 (C_*).**
1. c_κ = E[Φ_κ(z)²] = ∫(δ_κ*δ_κ)(w)G(w)dw = ∫ρ̃(v)G(v/κ)dv, with ρ̃ := δ*δ and ‖ρ̃‖_∞ ≤ ‖δ‖_∞.
2. By R2(c), for κ ≥ 1:
   G(v/κ) ≤ (1/2π)[(log(κ/(m|v|)))₊ + 1 + log 4] ≤ (1/2π)[log κ + (log(1/|v|))₊ + (log(1/m))₊ + 1 + log 4].
3. Also ∫ρ̃(v)(log(1/|v|))₊dv ≤ ‖δ‖_∞∫_{|v|≤1}log(1/|v|)dv = (π/2)‖δ‖_∞.
4. Hence **c_κ ≤ (1/2π)log κ + C_* for all κ ≥ 1 and all z, with C_* := (1/2π)[(π/2)‖δ‖_∞ + (log(1/m))₊ + 1 + log 4] ≥ 0.**

**R7 (Lemma C.3 constants).**
1. For 1 ≤ m < 2p′, apply Young's inequality with exponents 2p′/m and 2p′/(2p′−m) to (η|x|^m)(|β_m|/η), where
   η^{2p′/m} := A/(2m). This gives
   |β_m||x|^m ≤ (A/4p′)x^{2p′} + ((2p′−m)/2p′)(2m)^{m/(2p′−m)}(|β_m|^{2p′}/A^m)^{1/(2p′−m)}.
   For m = 0 the same holds with constant 1.
2. So:
   - C_{p′} = C′_{p′} := max{1, max_{1≤m<2p′}((2p′−m)/2p′)(2m)^{m/(2p′−m)}};
   - C(𝒫) := Σ_n|a_n|max_j n!/(j!(n−2j)!2^j);
   - b(𝒫) := C_{p′}Σ_{m=0}^{2p′−1}C(𝒫)^{2p′/(2p′−m)}a_{2p′}^{−m/(2p′−m)};
   - c₁: any number > 0 with c₁ ≥ λb(𝒫)|Λ|(1/2π + (1+C_*)/log 2)^{p′}.
3. The last uses 1 + C_* + (1/2π)log κ ≤ ((1+C_*)/log 2 + 1/2π)log κ for κ ≥ 2.

**R8 (import paragraph for A3; proposed text).**
> *Wick powers.* For g ∈ L^{1+ε}(ℝ²) and n ≥ 0:
> - :Φ^n(g): (formally ∫g:Φ(z)^n:dz) is the element of the n-th chaos Γ_n (the closed span of the Wick monomials
>   :Φ(f₁)⋯Φ(f_n):, [Simon, p. 17]; Simon writes "spanned by", and closedness is implicit in (V.3)'s "unique random
>   variable in Γ_m(H)") fixed by ⟨:Φ(f₁)⋯Φ(f_n):, :Φ^n(g):⟩ = n!∫∏_j[∫f_j(x)G(x−y)dx]g(y)dy
>   ([Simon, (V.3), p. 136]). It exists for g ∈ L^{1+ε} [Simon, Thm V.2(a), p. 137].
> - ‖:Φ^n(g):‖₂² = n!∬g(x)g(y)G(x−y)^ndxdy [Simon, p. 137].
> - For jointly Gaussian centred f, g, ⟨:f^n::g^m:⟩ = δ_{nm}n!⟨fg⟩^n [Simon, Thm I.3, (I.21), p. 11].
> - For a contraction A, Γ(A):Φ(f₁)⋯Φ(f_n): = :Φ(Af₁)⋯Φ(Af_n): [Simon, (I.32), p. 25].
> - 𝒰_h := λΣ_n a_n:Φ^n(h):.

With this, three steps become explicit calculations: C.2's mean zero; C.4's isometry, whose cross term comes from
(V.3) with f₁ = ⋯ = f_n = δ_κ(z−·) plus Fubini; and C.5's chaos decomposition. For the dossier: PDF pp. 33, 39, 47,
158, 159, and p. 60 for Thm I.22.

**R9 (Lemma C.4 constant).**
1. Let I_n := ∫₀¹s(1+log(1/s))^nds and K_n(R) := ∫₀^R(1+|log r|)^{n−1}(1+r)dr.
2. First region, for κ ≥ 2, substituting r = 4s/κ and using |log(4s/κ)| ≤ log κ + log 4 + log(1/s):
   ∫_{|ζ|<4/κ}(G^n+J^n) ≤ A_nκ^{−2}(1+log κ)^n, with A_n := 32πC_G^n(1+log 4)^nI_n + 16π(8πC_G‖δ‖_∞)^n.
3. Second region, by R5: ≤ B_nK_n(R)κ^{−1}, with B_n := 8πnC_∇(C_G+3C_∇)^{n−1}.
4. With (1+log κ)^n ≤ (1+1/log 2)^n(log 2)^{n−2p′}(log κ)^{2p′}, κ^{−2} ≤ κ^{−1}/2 and
   κ^{−1} ≤ (log 2)^{−2p′}κ^{−1}(log κ)^{2p′}:
   **c₂ := 3λ²|Λ|Σ_{n=1}^{2p′}a_n²n![(A_n/2)(1+1/log 2)^n(log 2)^{n−2p′} + B_nK_n(diam Λ)(log 2)^{−2p′}].**

**R10 (Theorem C.5 thresholds and the final bound).** Take λ > 0 and |Λ| > 0 (otherwise the theorem is trivial), c₁ > 0
as in R7, and c₂ as in R9. Set L := (b/2c₁)^{1/p′}, κ := e^L, 2q := e^{L/4p′}.
1. b₀ := 2c₁(4p′log 2)^{p′}. For b ≥ b₀ we get L ≥ 4p′log 2, so κ ≥ 2^{4p′} ≥ 2 (Lemmas C.3, C.4 apply) and 2q ≥ 2
   (the comparison applies at exponent 2q).
2. The bracket equals (√c₂/c₁)e^{−L/4}. Set b₁ := 2c₁(max{0, 4 + 2log(c₂/c₁²)})^{p′}, or b₁ := 0 if c₂ = 0. For
   b ≥ b₁ the bracket is ≤ e^{−1}.
3. Let f(b) := (1/4p′)(b/2c₁)^{1/p′} − log(2pb). Then f′(b) = b^{−1}[(4p′²)^{−1}(b/2c₁)^{1/p′} − 1], so f is
   nondecreasing for b ≥ 2c₁(4p′²)^{p′}, and f → +∞. Set b₂(p) := min{b ≥ 2c₁(4p′²)^{p′} : f(b) ≥ 0}; then f ≥ 0 on
   [b₂(p), ∞).
4. Let b_* := max{b₀, b₁, b₂(p)}. For b ≥ b_*: μ₀(𝒰_h ≤ −b) ≤ exp(−e^{L/4p′}) ≤ e^{−2pb}.
5. **‖e^{−𝒰_h}‖_p^p = ∫_ℝpe^{pb}μ₀(−𝒰_h > b)db ≤ e^{pb_*} + ∫_{b_*}^∞pe^{−pb}db ≤ e^{pb_*} + 1**, uniformly over the
   class.
6. So b_* = b_*(p, p′, c₁, c₂), and S₂ becomes explicit, though crude. PLAN Part 2's "does not supply … an evaluated
   constant" then becomes optional.

## 10. What the PLAN's three uses get

1. **Z(h) ≥ e^{−λ|a₀||Λ|}** (Lemma C.2). Holds for every compact Λ ⊇ supp h; for B̄, |B̄| = |B|. It is `proved` after R8.
2. **S₂(B) := sup{‖e^{−𝒰_{h′}}‖_{L²(dμ₀)} : h′ ∈ 𝒞_E, supp h′ ⊆ B̄} < ∞** (Theorem C.5, p = 2, Λ = B̄). Holds, and is
   `proved` after R1–R10. Moreover:
   - S₂(B) ≤ (1 + e^{2b_*})^{1/2}, with b_* from R10 at p = 2;
   - b_* depends on B only through c₁ ∝ |B| and c₂ (through |B| and diam B), so this is a bound that depends on the
     shape of B only.
   - The stronger claim that the supremum itself is translation-invariant is not checked (§6).
3. **‖Y‖₄ ≤ 3^{p′}‖Y‖₂.** Holds for every Y ∈ ⊕_{r≤2p′}Γ_r of any Gaussian L²-space.
   - Sources: the record's l. 3023–3031 (display at l. 3024), and verbatim Simon Thm I.22 (I.47) at m = 2p′, p = 4.
   - For the note's V(h′) under dφ₀, cite Thm I.22, or repeat the derivation on the time-zero space; the record's
     proof is written for L²(dμ₀).

## 11. Numerical corroboration (numerical; nothing is deduced from it)

- **Files:** script `audits/v3-numerics/check_bounds.py`; output `audits/v3-numerics/check_bounds.out`.
- **Environment:** `/usr/local/bin/python3` 3.14.7, mpmath 1.4.1 at 30 digits, numpy 2.5.2. The tolerance for the ≤
  checks is printed: 1e−20. No seeds except "AMGM seed 7" and numpy default_rng(11).
- **Results:**
  - **R1:** the heat-kernel integral equals K₀/(2π) at 4 points, with |diff| ≤ 2e−33.
  - **R2(a–c):** the three K₀ bounds hold on 236 log-spaced points x ∈ [1e−10, 63].
  - **R3:** K₁ ≤ (1+1/x)e^{−x} holds, and K₀′ = −K₁ holds to 1e−15.
  - **R6:** c_κ ≤ (1/2π)log κ + C_* holds with margin ≥ 0.36, for the disc indicator δ = 1_{|z|≤1}/π, which is bounded
    but not smooth; the bound uses only ‖δ‖_∞, the support and the mass. Tested at m₀ ∈ {0.5, 1, 3} and
    κ ∈ {1, 2, 10, 100, 1000}.
  - **R7:** b(𝒫) is valid for 6 random polynomials (p′ = 1, 2, 3) at c ∈ {0, 0.1, 1, 5, 50, 1000}.
  - **Comparison:** ‖Y‖₄/(3^{p′}‖Y‖₂) ≤ 0.67 for 600 random one-variable chaos expansions (Gauss–Hermite, 200 nodes).

## 12. Not checked

- Whether 𝒰_h, read as Simon's (V.3) construction, is the same object as GJS's Euclidean interaction in the measures
  dq_h of A8(i). This is outside the object; Remark 2.5 covers sharp-time Wick ordering only.
- Simon's *proofs* of Thms I.3, I.17, I.22, V.2 and V.7. I read the statements only. I also did not read the
  realisation of the free Euclidean field as the Gaussian process over its one-particle space; A4's "any Gaussian
  L²-space" imports it.
- Simon's (I.18a) itself (the Wick exponential). The identity :x^n:_c = c^{n/2}He_n(x/√c) rests on p. 11 Remark 2 and
  on the proof of Thm I.3 on p. 11, which uses (I.18a).
- The law of 𝒰_{h(·−a)} versus 𝒰_h under translations of μ₀ (the PLAN's "translation-invariance sentence"). It is not
  needed if the note uses the bound of §10.
- Remark C.6's claim that Lemma C.3 "would fail for $h$ of variable sign". Not load-bearing.
- Proposition C.1, Proposition C.7, M1–M6, and the other uses of Theorem C.5 in the record (M4, l. 2830–2831). Outside
  the object.
- The Fubini identifications in C3.9 and R8 are sketched, not written out line by line.
