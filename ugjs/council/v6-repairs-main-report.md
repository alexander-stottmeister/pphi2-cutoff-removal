# Pass 2 on `part_i/main.tex`: repairs from the two audits of 23 November 2026 (editor math-wording)

## 1. Outcome

I applied repairs R1–R13 and additions (a)–(e) of the orchestrator, together with the new notice, the date and epoch, and one merged Appendix B entry for 23 November 2026. Each repair was re-read at its source first. The build is clean: 0 errors, 0 Overfull, 0 undefined, empty grep, 127 pages, no label renumbered. The only statement environments whose text differs from FROZEN are the ten expected ones plus three named in §4 (Remark 13.3, Theorem D.4, Remark N.46). Each of those three changes is an attribution or a sentence of the same finding, not a change of mathematics.

## 2. Claims, with status and locator

Line numbers: "FROZEN" is 49f2d23; "new" is the edited working-tree file (8858 lines). Label numbers and pages are FROZEN / new `main.aux`.

| # | Claim | Status | Locator |
|---|---|---|---|
| 1 | GJ3 p. 210 prints "we take g(x) to be a nonnegative C_0^∞ function equal to one on the interval [−3, 3]" and (2.3)–(2.5), with no bound g ≤ 1. | verified | `audit_2026/evidence/gjiii-08.png` |
| 2 | GJ3 p. 205 prints "(1.10) H(g) = H_0 + λ∫:φ⁴(x): g(x)dx − E_g = H_0 + H_{I,g} − E_g", and "the spatial cutoff g(x) is a smooth, positive function that equals one on some bounded set". So GJ3's model is φ⁴. | verified | GJ3 PDF page 3 of the copy in `refs/`, rendered (130 dpi) |
| 3 | Corollary 12.3, as restricted, holds for g ∈ 𝒢 and 𝒫(ξ) = ξ⁴. The proof is unchanged apart from the measurability sentences (R2). | proved, conditional on Theorem 12.2(1), (T), Proposition E.5(T), and the A1-Scope reading applied to GJ3's (1.10) | `cor:canonical` 12.3, p. 42/43; new ll. 3173–3218 |
| 4 | a ↦ U_a is a strongly continuous one-parameter unitary group: j^C τ_a^C (j^C)^{−1} is multiplication by e^{−iak} (Lemma E.1(ii)), strongly continuous by dominated convergence (dominant 4\|θ\|²); then Lemma E.2(iv), and conjugation by the fixed unitary D. | proved | `prop:ff-symmetries` E.5(T), p. 120/121; new ll. 8462–8463, 8508–8512 |
| 5 | The proof of Theorem 13.2 uses (B1), (B3) and (B4), and not (B2). I checked Steps 1–4: (B3) supplies B, O and ω_±(B) = ±m; (B4) is used in Step 3; (B1) in Step 4. | verified (by reading the proof) | `thm:dichotomy` 13.2, p. 43/44; new ll. 3256–3311 |
| 6 | R_a = \|a\| − \|O\| for \|a\| ≥ \|O\|, so every a with \|a\| ≥ \|O\| + 1/m_1 satisfies R_a > 0 and m_1R_a ≥ 1. | proved (calculation) | new ll. 3264–3269 |
| 7 | At λ = 0 the moment constant vanishes, M = 0. Indeed V_* = 0 (N.20(iv)) and the second term of M² carries λ². Hence Ψ_γ(d) = 0 for d ≥ d_0. | proved (from Theorem 5.1's formula and (eq:Psidef)) | `thm:M2` 5.1; `lem:rate` 10.5 |
| 8 | For λ > 0, Ψ_{m_1} is not exponentially small. Argument: M > 0, since V_* > 0 and S_2 ≥ 1. Exponential decay of Ψ would force exponential tails of W_γ, through Ψ_γ(d) ≥ 32M·T_γ(⌊d⌋/2). That contradicts §1.4's argument: an analytic transform cannot vanish on (−γ/2, γ/2) unless it vanishes identically. | proved (§1.4, Pillar 2(i), together with this two-line step) | `subsec:strategy` §1.4 |
| 9 | `m2/m2.tex`: φ² model with m_1² := m_0² + λ (l. 67). Proposition `prop:rate` (l. 172) has only a "Proof sketch" (l. 185), and the sharpness of the exponent is asserted (l. 179). The numerics give k = 4.03 ± 0.05, with the prefactors "not sharply confirmed" (l. 240). | verified | `m2/m2.tex` |
| 10 | `part_ii/v3_continuum_package.tex` imports "(d) Part I Appendix C: the Γ(e^{−τ}) sum-of-chaoses moment comparison and the layer-cake assembly (proof of thm:stability)". No proof in `part_i/main.tex` cites Part II. | verified | `part_ii/v3_continuum_package.tex` (import (d), ll. 230–233); grep of `main.tex` |
| 11 | The arXiv abstract page of 2010.11121, fetched by me today, gives "Commun. Math. Phys. 387, 299-360 (2021)", the four authors, the title and DOI 10.1007/s00220-021-04152-5. (The orchestrator also reports Crossref; I did not fetch Crossref.) | verified | arxiv.org/abs/2010.11121 |
| 12 | Simon p. 31 prints "Let D_n(A) ⊂ Γ_n(H) be D(A)⊗...⊗D(A) (incomplete tensor product) and D(dΓ(A)) = +_{n=0}^∞ D_n(A) (incomplete direct sum)". | verified | `audit_2026/evidence/simon-dgamma-053.png` |
| 13 | The two new images show Simon p. 141 ("Henceforth the symbol P will denote a semibounded polynomial") and p. 146 ((V.15), "Define H_I(g) = ∫g(x):P(φ_F(x)):dx"). | verified | `simon-semibounded-163.png`, `simon-hg-168.png` |
| 14 | `audit_2026/citation_screenshot_dossier.tex` (modified 22 September 2026) names 54 images. 43 of the 97 images in `audit_2026/evidence/` are not in it: every image added since 31 October, and older ones such as `gjs-p589-06`, `gjs-core-11/12`, `gj2-local-algebra-40`. | verified (script) | `audit_2026/` |
| 15 | Remark N.39 and §D.e: the parallel pairs with a time-integrated partner are reached by the printed proof only after slicing. Pass 1's sentence in A8 Scope rests on this. | verified (pass 1) | `aux:d3-orient` N.39 |

## 3. The repairs, one by one

Before/after texts are LaTeX source, verbatim. The full diff against HEAD (both passes) is `repairs-main.diff`, beside this report. Pass 1's own changes are documented in `wording-main.md`.

### R1. Corollary 12.3 restricted to what its proof proves (`cor:canonical`, 12.3, p. 42 → 43; FROZEN ll. 3126–3131 → new ll. 3172–3186)

Before:
```
\begin{corollary}[the Glimm--Jaffe vacuum is canonical at weak coupling]\label{cor:canonical}
% src: m6/main.tex cor:canonical (v2), transcribed.
Every $w^*$ limit point of the (averaged or unaveraged) finite-volume ground states
constructed in \cite[\S2]{GJ3} coincides on each $\A(O)$ with $\omega_\infty$; in
particular the construction of \cite{GJ3} is subsequence- and averaging-independent in the
weak-coupling region.
\end{corollary}
```
After:
```
\begin{corollary}[the Glimm--Jaffe vacuum is canonical at weak coupling, for cutoffs
$0\le g\le1$]\label{cor:canonical}
% src: m6/main.tex cor:canonical (v2), transcribed; statement restricted 23 November 2026
% (audit ugjs/council/v6-chain-audit.md, findings F-A, F-B).
Let $\mathscr P(\xi)=\xi^4$, and let the cutoff $g$ of \cite[(2.3)]{GJ3} be chosen in $\G$, that
is, with $0\le g\le1$.  Then every $w^*$ limit point of the averaged states $\omega_n$ of
\cite[(2.4)]{GJ3} and of the unaveraged states $\omega_{g_n}$, $g_n=g(\cdot/n)$, coincides on
each $\A(O)$ with $\omega_\infty$; in particular, for such $g$, the construction of
\cite[\S2]{GJ3} is subsequence- and averaging-independent in the weak-coupling region.
\end{corollary}

The states of \cite{GJ3} are built from the ground states of
``$H(g)=H_0+\lambda\int{:}\phi^4(x){:}\,g(x)\,dx-E_g$'' \cite[(1.10), p.~205]{GJ3}; that these
are the $\Om_{g_n}$ of this manuscript rests on the reading recorded in the Scope of
Assumption~\ref{A:cutoff}, applied to \cite{GJ3}, which is not among the sources listed there.
```

Why accurate:
- Sources: claims 1–2.
- The proof fixes g ∈ 𝒢 with g ≡ 1 on [−3, 3]. Then g_n ∈ 𝒢, and only Theorem 12.2(1) is used. That is exactly the restricted statement. GJ3's own requirements (nonnegative, C_0^∞, g ≡ 1 on [−3, 3]) plus 0 ≤ g ≤ 1 make g ∈ 𝒢.
- The quotation is GJ3's (1.10), exact up to the symbol φ, which the record typesets as ϕ.
- GJ3 is not among A1's Sources (A1, FROZEN ll. 751–757). The identification of its H(g) and ground states therefore rests on A1's reading that 𝔇 carries the sources' V(g) to V(g). The sentence after the corollary says so, as the orchestrator allowed.
- I kept the "in particular" clause in its restricted form ("for such g").

Sentences that summarise the corollary:
- §1.4, FROZEN l. 340 → new ll. 364–365: "Corollary~\ref{cor:canonical} then makes the historical construction subsequence- and averaging-independent." → "… then makes the historical construction, with a cutoff $0\le g\le1$, subsequence- and averaging-independent."
- Provenance, FROZEN ll. 446–447 → new ll. 470–472: "(Corollary~\ref{cor:canonical} additionally quotes the averaged-state formula \cite[(2.3)--(2.5)]{GJ3} as the definition of the averaged states it identifies)" → "(… quotes the averaged-state formula \cite[(2.3)--(2.5)]{GJ3} and the Hamiltonian \cite[(1.10)]{GJ3} as the definition of the states it identifies)". The corollary now quotes (1.10) as well.
- §14 "Uniqueness", FROZEN ll. 3295–3296 → new ll. 3360–3362: "$\omega_\infty$ is canonical for the cutoff family (Corollary~\ref{cor:canonical}), and translation invariant without averaging." → "$\omega_\infty$ is canonical for the cutoff family $\G$ (for the construction of \cite{GJ3} with a cutoff $0\le g\le1$: Corollary~\ref{cor:canonical}), and translation invariant without averaging."
- Appendix B (FROZEN ll. 3423–3425, 3496, 3509): these mention the corollary only as a user of translations, or as dated history. They stay unchanged. So do the notice of 11 November (FROZEN l. 150) and FROZEN l. 219 (GJ3 history).

### R2. Strong continuity of translations, and its use in Corollary 12.3

E.5(T) statement (`prop:ff-symmetries`, E.5, p. 120 → 121; FROZEN l. 8356 → new ll. 8462–8463):
- Before: "Then $U_a1=1$, $U_aU_b=U_{a+b}$, and for $f\in\mathcal K_m$ …"
- After: "Then $U_a1=1$, $U_aU_b=U_{a+b}$, $a\mapsto U_a$ is a strongly continuous one-parameter unitary group, and for $f\in\mathcal K_m$ …"

E.5(T) proof (FROZEN l. 8401 → new ll. 8508–8512). Inserted after "… since $\tau_a\tau_b=\tau_{a+b}$.":
```
By
Lemma~\ref{lem:ff-onepart}(ii), $j^{\C}\tau_a^{\C}(j^{\C})^{-1}$ is multiplication by $e^{-iak}$,
strongly continuous in $a$ by dominated convergence; so $(\tau_a^{\C})_{a\in\R}$ is a strongly
continuous one-parameter unitary group on $\mathcal K_m^{\C}$, and so is
$U_a=D\,\Gamma_{\!\mathcal F}(\tau_a^{\C})\,D^{-1}$ by Lemma~\ref{lem:ff-gamma}(iv).
```
- Why accurate: U_a := U_{τ_a} = D Γ_𝓕(τ_a^C) D^{−1} by Lemma E.4's definition, with K_1 = K_2 = K_m. The rest is claim 4.
- Lemma E.1(ii) gives the multiplication formula. Lemma E.2(iv) is printed for "a strongly continuous one-parameter unitary group on 𝔥". The group law is τ_aτ_b = τ_{a+b}, τ_0 = 1.

Corollary 12.3 proof (FROZEN ll. 3149, 3158–3159 → new ll. 3202–3204, 3214–3218):
- The sentence "by \eqref{eq:T} (the estimate below is invariant under $\epsilon\to-\epsilon$). Since" now continues: "…; the integrands are continuous, as $b\mapsto\omega_{g_n}(\tau_bA)=\ip{U_{-b}\Om_{g_n}}{AU_{-b}\Om_{g_n}}$ is, by the strong continuity of $b\mapsto U_b$ (Proposition~\ref{prop:ff-symmetries}(T)). Since".
- After the bound: "…\longrightarrow0 ;" followed by "the integrand in $u$ is the supremum, over $A$ in the unit ball of $\A(O)$, of the continuous functions $u\mapsto|\omega_{g_n}(\tau_{\epsilon nu}A)-\omega_\infty(A)|$, hence lower semicontinuous and measurable."
- Why accurate: τ_bA = U_bAU_b^* and U_b^* = U_{−b}, so ω_{g_n}(τ_bA) = ⟨U_{−b}Ω, AU_{−b}Ω⟩, continuous in b. By (T), ‖(ω_{τ_{−εnu}g_n} − ω_∞)\|_{A(O)}‖ = sup_A \|ω_{g_n}(τ_{εnu}A) − ω_∞(A)\|. A supremum of continuous functions is lower semicontinuous, hence Borel.

### R3 and R5. §13 introduction (FROZEN ll. 3165–3169 → new ll. 3224–3230)

Before:
```
The uniform gap of Theorem~\ref{thm:G} is incompatible with a fully classified two-phase
structure. The incompatibility is stated as a conditional theorem: \emph{all four}
hypotheses below are load-bearing, and (B4) in particular cannot be omitted --- dropping
it was the one proof-breaking defect (P1) found by the independent audit of the
predecessor manuscript (Appendix~\ref{app:provenance}).
```
After:
```
The uniform gap of Theorem~\ref{thm:G}, together with the uniform local moment of
Theorem~\ref{thm:M2} through Theorem~\ref{thm:MAIN}, is incompatible with a fully classified
two-phase structure. The incompatibility is stated as a conditional theorem: its proof uses
(B1), (B3) and (B4), and (B4) in particular cannot be omitted --- dropping
it was the one proof-breaking defect (P1) found by the independent audit of the
predecessor manuscript (Appendix~\ref{app:provenance}); (B2) belongs to the classification
being excluded and is not used.
```
- Source: claim 5, and the proof of Theorem 13.2. Steps 2–3 use Theorem 12.2(1), (3), (4); item (1) rests on (M₂) of Theorem 5.1.
- The theorem itself is not restated.

### R4. Hypothesis 13.1 and the quantifier on a

Hypothesis 13.1 (`hyp:broken`, 13.1, p. 43 → 44; inserted after FROZEN l. 3186 → new ll. 3249–3250): "In (B1) and (B4), ``ground state'' is meant in the spectral sense of Proposition~\ref{prop:spectral}."
- Why accurate: Step 3 applies (B4) to ω_∞, which Theorem 12.2(3) makes a ground state exactly "in the spectral sense" of Proposition 12.1.

Proof of Theorem 13.2 (FROZEN ll. 3201–3204 → new ll. 3264–3269):
- Before: "Fix $a\in\R$ such that [display] where $O$ is the localization interval of the order parameter $B$ from (B3)."
- After: "In Steps~1 and~2, $a\in\R$ is any number with [display] where $O$ is the localization interval of the order parameter $B$ from (B3); every $a$ with $|a|\ge|O|+1/m_1$, $|O|$ the length of $O$, is one, since $R_a=|a|-|O|$ for $|a|\ge|O|$."
- Why accurate: claim 6. Steps 1–2 hold for each such a, which matches the limit \|a\| → ∞ in (eq:limitcluster).

### R5. The other sentences that ascribed Theorem 13.2 to the gap alone

- §1.3(c), FROZEN ll. 319–323 → new ll. 342–347:
  - "a cutoff-uniform gap is incompatible with that two-phase structure (Theorem~\ref{thm:dichotomy}). Thus an extension to such a broken phase would have to abandon the uniform-gap input;"
  - becomes "a cutoff-uniform gap together with the uniform local moment (through Theorem~\ref{thm:MAIN}) is incompatible with that two-phase structure (Theorem~\ref{thm:dichotomy}). Thus an extension to such a broken phase would have to abandon the uniform gap or the uniform local moment;"
- §1.4 "Boundaries", FROZEN ll. 421–424 → new ll. 446–448: "for even $\mathscr P$, a cutoff-uniform gap is incompatible with" becomes "for even $\mathscr P$, a cutoff-uniform gap together with the uniform local moment is incompatible with". This is the locus the orchestrator calls "near old l. 422".
- §14 "Beyond weak coupling", FROZEN ll. 3304–3305 → new ll. 3370–3371: "a proof based on a cutoff-uniform gap cannot extend" becomes "a proof based on a cutoff-uniform gap and a uniform local moment cannot extend".
- **Additional locus, same finding (F-E), not in R5's list:** Remark 13.3 (`rem:gjs7576`, 13.3, p. 44 → 45; FROZEN l. 3269 → new l. 3333). "cannot coexist with the cutoff-uniform gap." becomes "cannot coexist with the cutoff-uniform gap and the uniform local moment." That is why `rem:gjs7576` appears in the list of changed environments.

### R6 and R7. The quadratic-model rate, and "not exponential"

§1.3(b), FROZEN ll. 317–319 → new ll. 339–342.

Before:
```
(b) \emph{Sharp rate}: in the exactly solvable quadratic model the true rate is
$\mathrm{poly}(d)\,e^{-2m_1d}$ (companion note \texttt{m2/}); $\Psi_{m_1}$ is super-polynomial but not
exponential, and this is intrinsic to the filter method used.
```
After:
```
(b) \emph{Sharp rate}: for the exactly solvable quadratic model the companion note \texttt{m2/}
gives, with a proof sketch and numerics, the rate $\mathrm{poly}(d)\,e^{-2md}$, $m$ the mass of
that model; $\Psi_{m_1}$ is super-polynomial and, for $\lambda>0$, not exponential, and this is
intrinsic to the filter method used (\S\ref{subsec:strategy}).
```

§14 "Sharpness", FROZEN ll. 3288–3293 → new ll. 3352–3358.

Before:
```
\emph{Sharpness.} In the exactly solvable quadratic model the true rate is
$\mathrm{poly}(d)\,e^{-2m_1d}$ (companion note \texttt{m2/}: a round trip through the
region where the two Hamiltonians differ, at the local Agmon mass). $\Psi_{m_1}$ is
super-polynomial but sub-exponential. The present filter argument does not obtain the
sharp exponential rate; a proof of such a rate would require an additional resolvent or
Combes--Thomas input not supplied here.
```
After:
```
\emph{Sharpness.} For the exactly solvable quadratic model the companion note \texttt{m2/}
gives, with a proof sketch and numerics, the rate $\mathrm{poly}(d)\,e^{-2md}$, $m$ the mass of
that model (a round trip through the region where the two Hamiltonians differ, at the local
Agmon mass). $\Psi_{m_1}$ is super-polynomial and, for $\lambda>0$, not exponential
(\S\ref{subsec:strategy}). The present filter argument does not obtain an exponential rate; a
proof of such a rate would require an additional resolvent or Combes--Thomas input not supplied
here.
```

**Additional locus, same finding (F-F):** §1.4 "Boundaries", FROZEN ll. 419–421 → new ll. 443–446. "(the filter obstruction above; the solvable quadratic model has $\mathrm{poly}(d)\,e^{-2m_1d}$)" becomes "(the filter obstruction above; for the solvable quadratic model the note \texttt{m2/} gives $\mathrm{poly}(d)\,e^{-2md}$, $m$ that model's mass, with a proof sketch)".

Why accurate:
- The m2/ wording follows claim 9. I do not write "true rate", and I give no formula for m: m2/'s normalisation (λ/2)∫:φ²: differs from the record's.
- "For λ > 0" follows claims 7 and 8.
- "Not exponential … intrinsic to the filter method" is argued in §1.4, Pillar 2(i), which I now cite. I kept the claim.
- "The sharp exponential rate" became "an exponential rate", because the record no longer asserts that m2/'s rate is the sharp one.

### R8. §14 "Part II" (FROZEN ll. 3310–3312 → new ll. 3376–3379)

- Before: "--- is a separate problem with no mathematical dependence in either direction, and its record lives in"
- After: "--- is a separate problem: Part~I does not depend on Part~II, and Part~II re-uses one argument of Appendix~\ref{app:huniform} (from the proof of Theorem~\ref{thm:stability}); its record lives in"
- Source: claim 10.
- §14's "which remains open" (chain F-H) is left unchanged, as instructed.

### R9. [MMST] (`\bibitem{MMST}`, FROZEN ll. 8734–8736 → new ll. 8848–8850)

- "Comm.\ Math.\ Phys.\ \textbf{387} (2021) 1299--1367." becomes "Comm.\ Math.\ Phys.\ \textbf{387} (2021) 299--360; arXiv:2010.11121."
- Source: claim 11, fetched by me. The format follows the record's other arXiv entries ("arXiv:2504.08606 (2025)").

### R10. Open intervals, and the state hypothesis

- Lemma 9.3 (`lem:cluster`, 9.3, p. 37 → 38; FROZEN l. 2677 → new l. 2721): "for a bounded interval $O$" becomes "for a bounded open interval $O$".
- Proposition 12.1 (`prop:spectral`, 12.1, p. 40 → 41; FROZEN ll. 2994–2995 → new ll. 3038–3040):
  - "If $(g_n)\subseteq\G$ satisfies $d(g_n,O)\to\infty$ for every bounded interval $O$, and $\omega_{g_n}\to\omega$ in norm on every $\A(O)$, then $\omega$ is a ground state of"
  - becomes "… for every bounded open interval $O$, and $\omega$ is a state on $\A$ with $\omega_{g_n}\to\omega$ in norm on every $\A(O)$, then $\omega$ is a ground state of".
  - The first line of its proof (FROZEN l. 3007 → new l. 3052) gets "open" as well.
- Why accurate: A(O) is defined for bounded open intervals (§2.1). The proof uses that ω is a bounded functional on A ("by density on $\A$"; "Joint norm continuity").
- The application still matches: Theorem 12.2(3) applies the proposition to ω_∞, which the theorem states to be "a state … on $\A$", with g̃_n ∈ 𝒢 and d(g̃_n, O) → ∞ for every O.

### R11. Lemma E.7(b): the declared reading of (I.40) (proof of `lem:ff-sources`, E.7; inserted before FROZEN l. 8648's "That is, …" → new ll. 8759–8762)

Inserted:
```
The domain in (I.40), ``$D(A)\otimes\dots\otimes D(A)$
(incomplete tensor product)'' joined by an ``(incomplete direct sum)'' over $n$, is read as the
complex span of the vectors $S_n(v_1\otimes\dots\otimes v_n)$ with $v_j\in D(\mu)$, and the
finite sums of such vectors over $n$.
```
- Source: claim 12; the fragments are exact.
- The proof shows these vectors (even with v_j ∈ D(μ^C) ⊇ D(μ)) are in the domain of D^{−1}H_0D, with the action (I.40). Under this reading, D^{−1}H_0D (linear and closed) therefore extends dΓ(μ). That is the step the next sentence draws.
- A1(f)'s quotation is unchanged. The clause sits where the proof uses it.

### R12. Appendix B, entry "The free-field layer" (FROZEN ll. 3506–3507 → new ll. 3578–3580)

- Before: "…(Proposition~\ref{prop:ff-symmetries}); and they are identified with the objects of the sources (Lemma~\ref{lem:ff-sources})."
- After: "…(Proposition~\ref{prop:ff-symmetries}); and, except for the dilation unitary, which has no counterpart in the sources, they are identified with the objects of the sources (Lemma~\ref{lem:ff-sources})."
- Why accurate: Lemma E.7 identifies the vacuum, φ_0, π_0, H_0, U_a and Θ, and nothing about dilations. The e-audit's dictionary records no counterpart of the dilation unitary in the cited sources. A8(viii) is Euclidean.
- This corrects a sentence inside a dated entry, as R12 asked.

### R13. A1 Scope, the dictionary (pass 1's text; FROZEN ll. 797–801 → new ll. 830–834)

- Before (pass 1): "the dictionary between their Fock space and $Q$-space is the unitary $\mathfrak D$ of Lemma~\ref{lem:ff-sources}, which carries their vacuum to $1$, their time-zero fields to $\varphi_0$ and $\pi_0$, their free Hamiltonian to $H_0$ and their translation unitary $U(-a)$ to $U_a$."
- After: "the dictionary between the Fock space of \cite{GJ2} and $Q$-space is the unitary $\mathfrak D$ of Lemma~\ref{lem:ff-sources}, which carries its vacuum to $1$, its time-zero fields to $\varphi_0$ and $\pi_0$, its free Hamiltonian to $H_0$ and its translation unitary $U(-a)$ to $U_a$; that \cite{GJ71,Rosen70} use the same objects is a reading of those sources."
- Why accurate: Lemma E.7(a) is stated for "The Fock space of [GJ2]". Rosen70's field (1.2), p. 158, equals GJ2's (1.2.10) after k → −k. Rosen70's H_0, however, is not given by a formula on the pages read, and GJ71 refers to its [1] "for notation" (p. 253). So "a reading" is the accurate word for both.

### Addition (a). The loose attribution "of Theorem C.5" (my pass-1 W3)

Each locus now uses the wording of Theorem 12.2: "S₂ … of Definition N.14, finite by Theorem C.5".
- Appendix D introduction, FROZEN ll. 4163–4164 → new ll. 4265–4267: "it does not evaluate the constant of Theorem~\ref{thm:stability}, which enters the constants below as $S_2(B)$;" becomes "it does not evaluate the constant $S_2(B)$ of Definition~\ref{aux:notation-S2def}, finite by Theorem~\ref{thm:stability}, which enters the constants below;".
- Theorem D.4 statement (`thm:D4`, D.4, p. 100 → 101), FROZEN ll. 7024–7025 → new ll. 7127–7129: "the unevaluated finite constant $S_2(B_{3\times5})$ of Theorem~\ref{thm:stability}," becomes "the unevaluated constant $S_2(B_{3\times5})$ of Definition~\ref{aux:notation-S2def}, finite by Theorem~\ref{thm:stability},". **This sentence lies inside a theorem environment; the change is an attribution, not mathematics.**
- Remark N.46 (`aux:d4-not`, p. 102 → 104), FROZEN l. 7199 → new ll. 7303–7305: "and the unevaluated constant of Theorem~\ref{thm:stability}," becomes "and the unevaluated constant $S_2(B_{3\times5})$ of Definition~\ref{aux:notation-S2def}, finite by Theorem~\ref{thm:stability},".
- §D.f, first item, FROZEN ll. 7391–7392 → new ll. 7497–7499: "the unevaluated constant $S_2(B_{3\times5})$ of Theorem~\ref{thm:stability} and the finite $V_*$" becomes "… of Definition~\ref{aux:notation-S2def}, finite by Theorem~\ref{thm:stability}, and the finite $V_*$".
- **Left unchanged, as a dated passage:** FROZEN ll. 7971–7974 (new l. 8079). It closes the paragraph "In Appendix A the rows that changed on 7 November 2026 are: …", a record of that day's change. The new notice says how "the finite, unevaluated constant of Theorem C.5" is to be read.

### Addition (b). A5's Dossier line (new ll. 1036–1037)

- "item (ii): \texttt{simon-transfer-180}." becomes "item (ii): \texttt{simon-semibounded-163}, \texttt{simon-hg-168}, \texttt{simon-transfer-180}."
- I opened both new images (claim 13). A5's Sources line cites pp. 141, 146 and 158.

### Addition (c). The dossier index (claim 14)

- §2.4, FROZEN ll. 633–634 → new ll. 658–659: "(\texttt{audit\_2026/}\allowbreak\texttt{evidence/}, index in" becomes "(…\texttt{evidence/}, partly indexed in" (one word changed, one added).
- Appendix B table, FROZEN l. 3398 → new l. 3470: "page images for every import" becomes "page images for every import (the \texttt{.tex} index covers only part of them)".
- No count is written. "Indexed up to 31 October" would be false: older images such as `gjs-p589-06` are not indexed either.

### Addition (e), the notice, the date

`\date` and its comment (FROZEN ll. 76–81 → new ll. 76–82):
```
% Fixed date on purpose: it tracks the last change of the mathematics or of an
% import's status (the restriction of Corollary 12.3 and the corrections of 23 November 2026),
% not the build date, so the title page does not drift on every rebuild.  Update it only for
% such a change.
% The PDF bytes still carry pdftex's build timestamp; for byte-identical output
% build with SOURCE_DATE_EPOCH=1795392000 FORCE_SOURCE_DATE=1 (23 November 2026, 00:00 UTC).
\date{23 November 2026}
```
`date -u -r 1795392000` printed "Mo 23 Nov 2026 00:00:00 UTC".

Title-page notice: pass 1's paragraph is replaced. New ll. 160–178, after the notice of 11 November and before `\end{quote}`, with a blank line and `\smallskip`:
```
\textbf{Audit of 23 November 2026; corrections.}  Two independent audits, a third one of
Appendix~\ref{app:freefield} and one of the \emph{Locality} paragraph of \S\ref{subsec:model},
Lemma~\ref{lem:covparity}, Proposition~\ref{prop:spectral}, Corollary~\ref{cor:canonical},
Theorem~\ref{thm:dichotomy} and \S\ref{sec:discussion}, found every proof they read to hold for
what it covers, and one statement that claimed more than its proof:
Corollary~\ref{cor:canonical}, now restricted to cutoffs $0\le g\le1$ and to
$\mathscr P(\xi)=\xi^4$.  Theorem~\ref{thm:MAIN} and every other theorem are unchanged in
substance; Hypothesis~\ref{hyp:broken} now says that ``ground state'' is meant in the spectral
sense, and \S\ref{sec:dichotomy} that (B2) is not used; Proposition~\ref{prop:ff-symmetries}(T)
now states that translations are strongly continuous; smaller corrections are listed in
Appendix~\ref{app:provenance}.  The wording was also corrected: the description of the rate's
constants (above, ``the finite, unevaluated constant of Theorem~\ref{thm:stability}'' is $S_2$,
Definition~\ref{aux:notation-S2def}; the rate and $M$ are explicit in $S_2$ and the unevaluated
GJS constants), the Scope paragraphs of A1 and A8, the source of A5(ii), the dependence on the
filter (Lemma~\ref{lem:filter}) and the abstract's list of imports.  The repairs were re-checked
by an agent that wrote none of them.  Reports: \texttt{ugjs/council/}
(\texttt{v6-appendix-e-audit.md}, \texttt{v6-chain-audit.md}); gate record:
\texttt{part\_i/README.md}.
```
- The sentence on how the phrase of 7 November is to be read is kept, as (e) asks.
- "Unchanged in substance", not "unchanged": the theorem environments 12.2 and D.4 changed textually, in attributions only (§5).
- The scopes of the two audits are taken from their reports.

### Appendix B: one merged entry for 23 November 2026 (replaces pass 1's entry; new ll. 3593–3621)

The entry has seven numbered items. They cover R1–R13, both mentions of the dossier index, the A5 images and pass 1's wording corrections. It ends "Theorem~\ref{thm:MAIN} and every other theorem are unchanged in substance; no label was renumbered." (verified, §5). The full text is in the diff. Its item (i) names the severity the audit gave Corollary 12.3: "CRITICAL for that statement as written; no other result uses it".

## 4. Findings, decisions, and what depends on later steps

- **Sentences that depend on the orchestrator's later actions:**
  - The notice sentence **"The repairs were re-checked by an agent that wrote none of them."** (new ll. 175–176) is true only once that check has passed.
  - The notice's "Reports: ugjs/council/ (v6-appendix-e-audit.md, v6-chain-audit.md); gate record: part_i/README.md" and Appendix B's "\texttt{ugjs/council/}…\texttt{v6-chain-audit.md} and \texttt{v6-appendix-e-audit.md}" (new ll. 3593–3595) are true only once both reports are archived there and the gate record is written.
  - Every "23 November 2026" (`\date`, notice, Appendix B) is true only if the commit is pushed today.
  - A5's Dossier line names `simon-semibounded-163` and `simon-hg-168`. They are on disk, but per the workspace layout page images belong to the private companion repository, so they still need committing there.
- **Changes beyond the loci you listed:**
  - Remark 13.3 (R5, same finding F-E).
  - §1.4 "Boundaries", the m2/ rate (R6, same finding F-F).
  - The first line of the proof of Proposition 12.1 ("open", R10).
  - The provenance sentence on the corollary's external input (R1).
  - Each is reported above with its text.
- **Statement environments changed textually** (FROZEN against new, by label):
  - expected: `cor:canonical`, `hyp:broken`, `prop:spectral`, `lem:cluster`, `prop:ff-symmetries` (pass 2), and `A:cutoff`, `A:domain`, `A:gjs`, `lem:filter`, `thm:MAIN` (pass 1);
  - additional: `rem:gjs7576` (R5, same finding), and `thm:D4` and `aux:d4-not`. The last two are loci of addition (a), changed in attribution only.
  - Nothing else.
- **Decided not to do:**
  - chain F-H (§14's "remains open"), as instructed;
  - the dated passage of addition (a);
  - Theorem 13.2's statement (R3: not restated);
  - "bounded interval" in `lem:classes`' d(g,O) clause (FROZEN l. 1573), because Definition 2.1 defines d(g,O) for bounded intervals, without A(O);
  - pass 1's W4 (GJ71 "See [1]"), kept as you asked in pass 1;
  - the e-audit's observations O1–O3, which are not findings.
- **Public texts that will be stale** (not mine):
  - `docs/results.md` is generated from `main.tex` (Corollary 12.3's title and statement; all page numbers) and needs regenerating with `docs/extract.py`, which I did not run.
  - The dossier map in `part_i/README.md` (row A5) should list the three images.
  - I did not check whether the companion or README summarise Corollary 12.3 beyond what grep shows (`docs/provenance.md` l. 37 is dated history).
- **Layout:** 127 pages (FROZEN 125); 199 of 238 labels move by one or two pages. Pass 1's W1 and W2 were accepted, and this pass was told not to fight for pages.

## 5. Checks actually run, with output

Build: in `part_i/`, three passes of `SOURCE_DATE_EPOCH=1795392000 FORCE_SOURCE_DATE=1 /Library/TeX/texbin/pdflatex -interaction=nonstopmode main.tex`, then a fourth pass. pdfTeX 3.141592653-2.6-1.40.29 (TeX Live 2026).
- `grep -cE '^!' main.log`: 0
- `grep -c Overfull main.log`: 0
- `grep -icE undefined main.log`: 0
- `pdftotext main.pdf - | grep -nE '\?\?|TODO|Hmm|wait,'`: no output (exit 1)
- Pages: 127
- `shasum -a 256 main.pdf`: `ea42d274d822142edd73008eaaa44a9e43ec1e70088c3c44759cd97e8f2098a1`, the same after the fourth pass; `main.aux` byte-identical after the fourth pass.
- `shasum -a 256 main.tex`: `3da0640725bcf851c2d8acd37dec515adbb2cbfb5c732f151a91e92c5d74bbf7` (8858 lines).
- At the start of pass 2, `main.tex` had sha256 `0f71e2a9…c88022`, my pass-1 state, so nobody else had changed it.

Labels (script: every `\newlabel` of the new `main.aux` against FROZEN's):
- 238 before and after; none added or removed; **no number changes**.
- 199 page changes: 113 by +1 and 86 by +2, all for labels on FROZEN pages 9–122.
- The full list, as label, number, FROZEN page → new page:

def:classes 2.1 9→10; subsec:classes 2.2 9→10; A:cutoff A1 10→11; subsec:imports 2.4 10→11; A:stability A3 13→14; A:patch A6 15→16; eq:P (P) 15→16; A:covar A7 16→17; eq:printednorm 1 17→18; sf:CE2 2.2 17→18; eq:UGJS (U_GJS) 18→19; sf:printed 2.4 19→20; rem:conv 2.5 21→22; eq:T (T) 22→23; lem:covparity 2.8 22→23; subsec:weak 2.6 22→23; prop:scaling 3.2 23→24; rem:wlog 3.3 24→25; eq:fkn1 3 25→26; eq:fkn2 2 25→26; lem:slabFKN 4.1 25→26; sec:slab 4 25→26; lem:slabvac 4.4 26→27; eq:M2 (M₂) 27→28; eq:QV 4 27→28; sec:M2 5 27→28; thm:M2 5.1 27→28; cor:M2phi4 5.2 28→29; eq:VT 6 28→29; eq:normQ 7 29→30; eq:normQ2 8 29→30; prop:gjsnorms 6.2 29→30; rem:row 6.3 29→30; eq:middle 10 30→31; eq:onepoint 9 30→31; lem:onepoint 7.2 30→31; lem:ce2strip 7.4 31→32; lem:expmom 7.6 32→33; thm:dense 7.7 32→33; eq:G (G) 33→34; thm:G 7.8 33→34; eq:fknpath 11 34→35; eq:pairing 12 34→35; eq:wsbound 13 34→35; prop:pathreg 8.1 34→35; eq:derivform 15 35→36; eq:filterdef 17 35→36; eq:weakeigen 16 35→36; lem:filter 9.1 35→36; prop:projreg 8.2 35→36; sec:filter 9 35→36; eq:sep 19 36→37; eq:septransform 20 36→37; lem:separation 9.2 36→37; eq:cluster 23 37→38; lem:cluster 9.3 37→38; sec:lppl 10 37→38; eq:localize 25 38→39; eq:onepath 27 38→39; eq:tworegime 26 38→39; lem:localize 10.2 38→39; lem:tworegime 10.3 38→39; prop:onepath 10.4 38→39; eq:Psidef 29 39→40; eq:Psitail 30 39→40; lem:rate 10.5 39→40; eq:cauchyeps 32 40→41; prop:normal 11.2 40→41; prop:spectral 12.1 40→41; sec:ground 12 40→41; thm:MAIN 12.2 41→42; cor:canonical 12.3 42→43; eq:cutoffcluster 33 43→44; eq:limitcluster 34 43→44; hyp:broken 13.1 43→44; sec:dichotomy 13 43→44; thm:dichotomy 13.2 43→44; rem:gjs7576 13.3 44→45; sec:discussion 14 44→45; app:constants A 45→46; app:provenance B 47→48; app:huniform C 50→51; prop:struct C.1 51→53; eq:Ggrad (C.b) 52→53; eq:Glog (C.a) 52→53; eq:ckappa (C.c) 52→54; lem:Z C.2 53→55; lem:wick C.3 53→55; lem:uv C.4 54→56; thm:stability C.5 56→57; app:comparison D 57→59; prop:discharge C.7 57→59; rem:whyclass C.6 57→58; sec:notation D.a 58→60; aux:notation-gjslattice N.2 59→61; aux:notation-squares N.1 59→61; sec:notation-squares D.a.1 59→61; aux:notation-counts N.3 60→62; aux:notation-box N.4 61→63; aux:notation-cutoffs N.5 61→63; sec:notation-boxes D.a.2 61→63; aux:notation-stripdef N.6 62→64; sec:notation-strips D.a.3 62→64; aux:notation-strip N.7 63→65; aux:notation-counterex N.8 64→65; aux:notation-ringdef N.10 64→66; aux:notation-rings N.11 64→66; aux:notation-tilted N.9 64→66; sec:notation-rings D.a.4 64→66; aux:notation-ringrem N.12 66→67; aux:notation-transl N.13 66→68; sec:notation-S2 D.a.5 66→68; aux:notation-S2 N.15 67→69; aux:notation-S2def N.14 67→69; aux:notation-S2rem N.16 68→69; aux:notation-UDelta N.17 68→70; aux:notation-cU N.18 68→70; sec:notation-cU D.a.6 68→70; aux:notation-kernel N.19 69→71; sec:notation-wick D.a.7 69→71; aux:notation-wick N.20 71→73; aux:notation-hyper N.21 73→75; aux:notation-sharpid N.22 74→76; aux:notation-sharpidrem N.23 75→77; aux:notation-ident N.23′ 76→77; eq:wickpair (W.4) 77→79; sec:d1 D.b 78→80; sec:notation-printed D.a.8 78→79; aux:d1-cov N.25 79→81; aux:d1-wick N.24 79→81; eq:d1-hermite 35 79→81; eq:d1-wick 36 79→81; aux:d1-def N.27 81→83; aux:d1-obs N.26 81→82; aux:d1-moments N.28 82→83; eq:d1-two 37 82→84; eq:d1-major 38 83→84; eq:d1-moment 39 83→85; eq:d1-deriv 40 84→86; eq:d1-identity 41 84→86; lem:D1 D.1 84→86; eq:d1-affine 42 85→87; aux:d1-uses N.29 86→88; eq:d1-quot 43 86→87; aux:d1-check N.30 87→88; sec:d2 D.c 87→89; sub:d2-conv D.c.1 87→89; aux:d2-int N.32 88→90; aux:d2-widest N.31 88→89; lem:D2 D.2 88→90; sub:d2-lemma D.c.2 88→90; aux:d2-uses N.33 91→93; aux:d3-V3 N.34 92→94; sec:d3 D.d 92→93; sub:d3-aux D.d.2 92→94; sub:d3-setting D.d.1 92→93; aux:d3-cyl N.36 93→95; aux:d3-sharp N.35 93→94; aux:d3-cells N.37 94→96; aux:d3-geom N.38 95→96; sub:d3-thm D.d.3 95→97; thm:D3 D.3 95→97; aux:d3-orient N.39 96→98; sub:d3-rem D.d.4 96→98; aux:d3-boundary N.41 97→99; aux:d3-not N.42 97→99; aux:d3-quant N.40 97→99; sec:d4 D.e 98→99; sub:d4-setting D.e.1 98→100; aux:d4-QV N.43 99→100; sub:d4-aux D.e.2 99→100; sub:d4-thm D.e.3 100→101; thm:D4 D.4 100→101; sub:d4-transverse D.e.4 101→103; aux:d4-boundary N.45 102→104; aux:d4-not N.46 102→104; aux:d4-quant N.44 102→104; sub:d4-rem D.e.5 102→104; sec:quant D.f 103→104; sec:quant-fixed D.f.1 103→105; sec:quant-order D.f.2 104→106; sec:quant-boundary D.f.3 107→109; app:D-constants D.g 109→110; aux:constants-comparison N.48 109→111; aux:constants-D3 N.49 110→111; aux:constants-D4 N.50 110→112; aux:constants-phi4 N.51 111→113; aux:constants-76 N.53 112→114; aux:constants-gauss N.52 112→113; aux:constants-s0 N.54 112→114; aux:constants-other N.55 113→115; app:freefield E 115→116; lem:ff-onepart E.1 115→117; lem:ff-gamma E.2 117→119; def:ff-objects E.3 118→119; lem:ff-transport E.4 118→120; prop:ff-symmetries E.5 120→121; lem:ff-sources E.7 122→124; rem:ff-A7 E.6 122→124.

Statement environments (script: theorem, proposition, lemma, corollary, hypothesis, assumption, remark, definition, srcfact, srcfactstar, aux*, compared by label):
- 127 labelled before and after; none added or removed; the 2 unlabelled ones unchanged.
- Changed textually: A:cutoff, A:domain, A:gjs, lem:filter, lem:cluster, prop:spectral, thm:MAIN, cor:canonical, hyp:broken, rem:gjs7576, thm:D4, aux:d4-not, prop:ff-symmetries (explained in §4).

Rendering: pages 1, 2, 3, 6, 7, 8, 11, 13, 16, 21, 36, 38, 41, 43, 44, 45, 46, 48, 50, 60, 101, 104, 108, 122, 126 and 127 were rendered at 80 dpi and looked at; page 50 again after the last edit. These are every page that carries changed text. Nothing lies outside the margins, and the new notice and the new history entry are their own paragraphs.

AGENTS.md 3.8: I listed the control sequences of all added lines. All are standard LaTeX, amsmath or mathrsfs, or defined in the preamble (`\Om` l. 55, `\G` l. 51, `\A` l. 50, `\C` l. 48, `\HH` l. 54, `\ip` l. 56, `\R` l. 46, `\dist` l. 58). The new symbols are defined where they are used:
- ω_n and g_n of GJ3, in the corollary;
- \|O\| ("the length of O") and R_a, in the proof of Theorem 13.2;
- m ("the mass of that model");
- S_n (Appendix E).

Sources read in this pass:
- page images `gjiii-08`, `simon-dgamma-053`, `simon-semibounded-163`, `simon-hg-168`;
- GJ3 PDF pages 3 and 9, rendered;
- `m2/m2.tex` ll. 55–75, 150–200, 230–242;
- `part_ii/v3_continuum_package.tex` ll. 222–240, and grep of `part_ii/v2_interaction_comparison.tex`;
- `audit_2026/citation_screenshot_dossier.tex` (image list, by script);
- the arXiv abstract page of 2010.11121;
- both audit reports in full (sections 1–6).

## 6. Not done, not verified, not run

Not done:
- `docs/results.*` regeneration and `docs/extract.py` (not mine).
- The dossier map in `part_i/README.md`, and the gate record of this pass (not mine).
- Committing the two new images to the private repository (not mine).
- Chain F-H (left, as instructed).
- The dated locus of addition (a).

Not verified:
- The Crossref record of the MMST DOI (fetched only by the orchestrator).
- Whether the companion or other public texts summarise Corollary 12.3 or the §14 claims (beyond a grep of FROZEN's README, docs and CITATION.cff).
- The proofs of `m2/m2.tex` and of the Part II notes (statements only).

Not run: any git command that changes state, any `kb` command, `docs/extract.py`.

## 7. Files written

- `part_i/main.tex`, with its build products (`part_i/main.pdf` tracked; `main.aux`, `main.log`, `main.toc`, `main.out`).
- This report `repairs-main.md`, and `repairs-main.diff` (output of `git diff -- part_i/main.tex`: the full diff against HEAD, both passes), in the council's reports directory.
- Scratch files outside the repository: renders, page-text dumps, the fetched arXiv page and copies of intermediate states. They are not deliverables.
