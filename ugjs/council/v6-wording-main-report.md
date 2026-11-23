# Wording corrections of 22 November in `part_i/main.tex` (editor math-wording, 23 November 2026)

## 1. Outcome

I applied the six corrections (F1, F2, F3, N1, N4, N8) and the dated notice (G) with its Appendix B entry to `part_i/main.tex`, after re-reading every source at its page. The result builds cleanly: 0 errors, 0 Overfull, 0 undefined, 125 pages, no label renumbered, and only the five intended statement environments changed. Two constraints of (H) could not be met: the abstract now ends on page 3, and 30 labels change their page.

## 2. Claims, with status and locator

Line numbers: "FROZEN" means 49f2d23 (= the frozen copy); "new" means the edited working-tree file. Label numbers and pages are taken from `main.aux` (FROZEN / new).

| # | Claim | Status | Locator |
|---|---|---|---|
| 1 | GJS Theorem 1.1.7 prints "Let m₀, K₂ and K₁ be sufficiently large and let λ be sufficiently small. There are constants 0 < m₁ and O(1) independent of h, Q₁ and Q₂ such that (1.1.10) …" So m₁ and C₇ (the O(1)) are printed only as existing, and K₁, K₂ only as "sufficiently large". | verified | GJS p. 594, `audit_2026/evidence/gjs-theorems-11.png` |
| 2 | Theorem C.5 states an explicit bound (1+e^{pb_*})^{1/p} and evaluates nothing further. S₂ is defined in Definition N.14. Proposition N.15(i) states 1 ≤ S₂ < ∞; the bound (1+e^{2b_*})^{1/2} appears in its proof. | verified | `thm:stability` C.5 p. 56 (FROZEN ll. 3979–3992); `aux:notation-S2def` N.14 p. 67 (l. 4794); `aux:notation-S2` N.15 p. 67 (ll. 4802–4829) |
| 3 | V_* := sup_{h'} ‖V(h')‖² equals its bound V̄_* = λ²Σ a_n² n! I_n. Argument: h' = 1_{[a,a+2]} is admissible in Lemma N.20, and the displayed equality of N.20(iv) gives ‖V(1_{[a,a+2]})‖² = V̄_*. So V_* is explicit, and I do not list it among the unevaluated constants. | proved (two lines, this report; not stated in the record) | `aux:notation-wick` N.20(iv), p. 71 |
| 4 | GJS p. 588 prints: "Fock space 𝓕 = L₂(𝒮′(R¹), dφ) is defined by the Gaussian measure dφ with mean zero and covariance μ⁻¹ = (−d²/dx₁² + m₀²)^{−1/2}, see [1]. Also : : denotes Wick ordering with respect to dφ." It also prints (1.6) and "Then H(g, λ, m₀) is essentially self-adjoint and inf spectrum H is a simple eigenvalue" for measurable 0 ≤ g ≤ 1 of compact support. | verified | `audit_2026/evidence/gjs-source-05.png` |
| 5 | GJS p. 589 prints "Φ(0, x⃗) = φ₀(x⃗)" and "dΦ is the Gaussian measure with mean zero and covariance (−Δ + m₀²)^{−1}". | verified | `audit_2026/evidence/gjs-p589-06.png` |
| 6 | Read literally, pp. 588 and 589 disagree by a factor 2. The record's μ⁻¹ equals 2C. The sharp-time restriction of (−Δ+m₀²)^{−1} is ∫dk₀/(2π)(k₀²+μ²)^{−1} = (2μ)^{−1} = C. Reading μ⁻¹ as the index-space inner product ⟨f, μ⁻¹g⟩ = 2⟨f, Cg⟩ (Simon's normalisation ½⟨v,w⟩) makes them consistent. | proved (explicit calculation; Remark 2.5 states the same identity) | `rem:conv` 2.5, p. 21/22 |
| 7 | GJS's reference [1] is J. Dimock and J. Glimm, "Measures on Schwarz distribution space and applications to P(φ)₂ field theories", Adv. Math. 12 (1974) 58–83. It is not in `refs/` (recursive search) and not in the bibliography of `main.tex`. | verified | GJS p. 631 (PDF page 48 of the copy in `refs/`, rendered) |
| 8 | GJ2 works in Fock space: "The Fock space 𝓕 is the Hilbert space completion of the symmetric tensor algebra over L₂(R)" (p. 364). It defines Wick polynomials "as a bilinear form on D(N^{n/2}) × D(N^{n/2})" (p. 365). | verified | `gj2-fock-04.png`, `gj2-fields-05.png` |
| 9 | GJ71 works in Fock space: "In the representation of Fock space for which the operators H_I(κ) are all diagonal …" (p. 255; annihilation and number operators on p. 256). For its Wick-ordered interaction it says "See [1] for notation" (p. 253). | verified | p. 255 rendered from `refs/` (PDF page 3); `gj71-1.png`, `gj71-theorem2-04.png` |
| 10 | Rosen70 works in Fock space: "The boson Fock space 𝓕 is the direct sum …", and its powers of the field are "Wick ordered by placing creators on the left and annihilators on the right" (p. 158). It also uses a Q-space representation of its box-cutoff theory (§2, Theorem 2.1). | verified | p. 158 rendered and viewed (PDF page 2); §2 and Theorem 2.1 read through pdftotext only (PDF pages 7 and 9) |
| 11 | Simon prints "THEOREM V.12. Let g ≥ 0, g ∈ L¹ ∩ L^{1+ε}. Let H(g) be given by (V.15). Then (a) H(g) is essentially self-adjoint on C^∞(H₀)" (p. 158). (V.15) is "H(g) = H₀ + H_I(g)" with "H_I(g) = ∫ g(x) :P(φ_F(x)): dx" on "𝓕 = Γ(F_{m₀})" (p. 146). P is "a semibounded polynomial", defined by "inf_{x∈R} P(x) > −∞" (pp. 140–141). The proof ends "Thus C^∞(H₀) is a core for H" (p. 161), with H the closure of H(g). | verified | p. 158 = `simon-transfer-180.png`; pp. 140, 141, 145, 146, 159, 160, 161 rendered from `refs/` (PDF pages 162, 163, 167, 168, 181–183) |
| 12 | A5(ii) follows from Theorem V.12(a) applied at each g_s, with 𝒞 = C^∞(H₀) = ⋂ₙ D(H₀ⁿ). The argument is written in A5's new Scope sentence. | proved, conditional on the reading of φ_F already recorded in A1's Scope, and on "essentially self-adjoint on C^∞(H₀)" in its usual sense (which includes C^∞(H₀) ⊆ D(H(g))) | `A:domain` A5, p. 15 (new ll. 1011–1015) |
| 13 | GJS p. 595 prints Theorem 1.1.8 with "uniformly as h → 1". GJS p. 629 prints "The estimates of Theorems 1.1.8, 1.1.11, 3.1 and 4.1 are uniform in the space cutoff h". GJS p. 597 prints "the proof follows from Theorem 1.1.8, (1.1.16) and the above determination of Q". | verified | `gjs-theorems-12.png`; `gjs-uniform-46.png` and `gjs-uniformity-46.png` (identical sentence); `gjs-proof-14.png` |
| 14 | Remark N.39, and §D.e for Theorem D.4's class (P), say that the printed proof reaches the parallel pairs with a time-integrated partner "only after slicing", and leave open whether it reaches them. | verified | `aux:d3-orient` N.39 p. 96/97 (FROZEN ll. 6804–6825); `sub:d4-transverse`, FROZEN l. 7134 |
| 15 | W_γ, T_γ, C_{q,γ} (Lemma 9.1), C′_γ, Ψ_γ and C_{N,γ,M} (Lemma 10.5) all depend on χ. Every statement of §§9–12 stays true when χ is fixed once for each γ. | proved (by inspecting the definitions and proofs) | `lem:filter` 9.1 p. 35; `lem:rate` 10.5 p. 39 |

## 3. The changes, one by one (each repairs a MINOR finding of 22 November)

For each change I give: locus, text before and after (LaTeX source, verbatim), the source I read, and why the new text is accurate. The full diff is `wording-main.diff`, beside this report.

### (G) Title-page notice (new paragraph after FROZEN l. 157, before `\end{quote}`; new ll. 159–165; page 2)

Before: none.

After:
```
\smallskip
\textbf{Corrections of wording (23 November 2026).}  Above, ``the finite, unevaluated
constant of Theorem~\ref{thm:stability}'' is $S_2$ (Definition~\ref{aux:notation-S2def});
the rate and $M$ are explicit in $S_2$ and the unevaluated GJS constants.  Also corrected:
Scope of A1, A8; source of A5(ii); dependence on the filter (Lemma~\ref{lem:filter}); the
abstract's list of imports.  No mathematical statement or import status changed
(\texttt{part\_i/README.md}).
```

- The notice has three sentences, set off by a blank line and `\smallskip` like the others; it renders as its own paragraph (checked on the rendered page 2).
- The quotation is the exact phrase of FROZEN l. 133.
- "GJS constants" is the record's own term (notation table, FROZEN l. 610; Appendix A, first row).
- The notice of 7 November and the `\date` with its comment (FROZEN ll. 76–81) are unchanged.
- "No mathematical statement … changed": the comparison of statement environments (§5) finds textual changes only in A1, A5, A8 (Sources, Scope and Dossier prose), in Lemma 9.1 (the χ convention) and in the imports paragraph inside Theorem 12.2 (an attribution).
- The notice carries today's date and names `part_i/README.md` as the record. It is true only if the commit is pushed today and that README records this pass (the orchestrator's part).

### F1, abstract (FROZEN ll. 174–175; new ll. 182–183; page 2)

Before:
```
with a super-polynomial rate in $\dist(O,\{g<1\})$, explicit up to the finite constant of
Theorem~\ref{thm:stability}; the limit is locally normal,
```
After:
```
with a super-polynomial rate in $\dist(O,\{g<1\})$, explicit in the imported theorem's
unevaluated constants and one stability constant; the limit is locally normal,
```

- Sources: GJS p. 594 (claim 1); Theorem 5.1 (`thm:M2`), which states that M depends on (λ, 𝒫, m₀) through C₇, m₁, K₁, K₂, S₂(B₃ₓ₅) and V_*; Lemma 10.5 (Ψ_γ is an explicit formula in M, γ and the filter).
- Why accurate: the rate is an explicit formula whose non-explicit inputs are the constants of the imported Theorem 1.1.7 and the single stability constant S₂(B₃ₓ₅). V_* is explicit (claim 3).
- The clause is one clause, as asked. I dropped the pointer to Theorem C.5 for line budget (§4, W1). A longer version, "… and in one stability constant, finite by Theorem C.5", was built and costs one more line.

### F1, §1.2 (FROZEN l. 236; new l. 245; page 5)

Before: `explicit up to the finite constant of Theorem~\ref{thm:stability}:`

After: `explicit in unevaluated constants (Appendix~\ref{app:constants}):`

- Why accurate: true as stated, and the corrected Appendix A paragraph (below) names the constants.
- I did not name them here because every version that did (e.g. "explicit in the unevaluated GJS constants and in S₂ (Definition N.14)") added a line on page 5. I measured the effect: the §1.3 heading moves to page 6, about 3.5 lines spill into §2, and A1's label moves to page 11.
- If the orchestrator prefers naming them, that is the alternative text; it costs those label moves (§4, W1).

### F1, Theorem 12.2, imports paragraph inside the theorem environment (FROZEN l. 3099; new ll. 3127–3128; `thm:MAIN` 12.2, page 41 in both builds)

Before: `contain the finite, unevaluated constant $S_2(B_{3\times5})$ of Theorem~\ref{thm:stability}.`

After:
```
contain the unevaluated constant $S_2(B_{3\times5})$ of Definition~\ref{aux:notation-S2def},
finite by Theorem~\ref{thm:stability}.
```

- This sentence lies inside a theorem environment. The change corrects an attribution only and is not part of the mathematical statement: items (1)–(5) are unchanged.
- Source: Definition N.14 and Proposition N.15(i) (claim 2).

### F1, Appendix A (FROZEN ll. 3378–3380; new ll. 3407–3414; `app:constants` A, page 45, paragraph on page 46 in both builds)

Before:
```
The rows $S_2(B)$, $A$, $A_f$, $M$ and the $\Psi_\gamma$ rows contain the finite constant of
Theorem~\ref{thm:stability}, which is not evaluated (its bound $(1+e^{2b_*})^{1/2}$ at
$p=2$ is explicit but crude); every other constant is explicit.  Until 7 November 2026 the
```
After:
```
The rows $S_2(B)$, $A$, $A_f$, $M$ and the $\Psi_\gamma$ rows contain $S_2$
(Definition~\ref{aux:notation-S2def}), which is not evaluated; Theorem~\ref{thm:stability} at
$p=2$ bounds it by the explicit but crude $(1+e^{2b_*})^{1/2}$ (proof of
Proposition~\ref{aux:notation-S2}(i)).  Nor are the first two rows evaluated: GJS print $m_1$
and $C_7$ only as existing, and the thresholds for $K_1$, $K_2$, $M_*$, $\lambda_*$ only as
``sufficiently large'' or ``sufficiently small'' (p.~594).  Every other constant is explicit
in these, in $V_*$ (explicitly bounded, Lemma~\ref{aux:notation-wick}) and, for $\Psi_\gamma$,
in the filter of Lemma~\ref{lem:filter}.  Until 7 November 2026 the
```

- Sources: claims 1–3; §2.6 (M_*, λ_* are fixed so that the hypotheses printed on p. 594 hold).
- Why accurate: I checked the table row by row. Row 2 is ε_𝒫 = λ_*/M_*². N_I, 𝔎(p′), c_U, Σ̄, K′, K_f, s₀, Ĉ_Q, d₀ and b₀, C_*, c₁, c₂, b_* are explicit in the listed inputs. A, A_f and M contain S₂. The Ψ_γ rows contain M and the filter.
- The dated sentence "Until 7 November 2026 …" is kept verbatim.

### N8, abstract list of imports (FROZEN ll. 188–189; new ll. 196–198; page 3)

Before: `… results on self-adjointness and the simple positive ground state,` then `Feynman--Kac--Nelson transfer, …`

After: `… results on self-adjointness and the simple positive ground state, Wick` / `powers and the free field, Feynman--Kac--Nelson transfer, …`

- "The free field" names A1(e)–(g); A1's own paragraph title is "Fock space and the free field".
- "Wick powers" names A1(a)–(d) and the construction paragraph of A3. These were also missing from the list, although N8 named only (e)–(g).
- The words fit into the free space of the abstract's last line, so they cost no line (measured).

### N1, A1 Scope (FROZEN ll. 797–798; new ll. 806–815; `A:cutoff` A1, page 10 in both builds; the sentence is on page 13 (new))

Before:
```
there (Lemma~\ref{lem:ff-onepart}(i)).  The sources of the cutoff construction work in Fock
space; the dictionary between their Fock space and $Q$-space is the unitary $\mathfrak D$ of
```
After:
```
there (Lemma~\ref{lem:ff-onepart}(i)).  Of the sources of the cutoff construction,
\cite{GJS} works in $Q$-space: its ``Fock space $\mathcal F=L_2(\mathcal S'(R^1),d\phi)$'' has ``covariance
$\mu^{-1}=(-d^2/dx_1^2+m_0^2)^{-1/2}$, see [1]'' and ``Wick ordering with respect to
$d\phi$'' \cite[p.~588]{GJS}.  Literally $\mu^{-1}=2C$; reading $\mu^{-1}$ as the inner product
$2\ip f{Cg}$ of $\HH_C$, which makes $d\phi$ our $d\phi_0$ consistently with
$\Phi(0,\vec x)=\phi_0(\vec x)$ and the covariance $(-\Delta+m_0^2)^{-1}$ of $d\Phi$
\cite[p.~589]{GJS} (Remark~\ref{rem:conv}), is a reading of the kind recorded in
Assumption~\ref{A:gjs}, Scope~(d), not proved here (the source's [1] is not among ours).
\cite[p.~364]{GJ2}, \cite[p.~255]{GJ71} and \cite[p.~158]{Rosen70} work in Fock space; the
dictionary between their Fock space and $Q$-space is the unitary $\mathfrak D$ of
```

- The remainder is unchanged, including the sentence "They define V(g) by normal ordering in Fock space; that 𝔇 carries their V(g) to the V(g) defined here is not proved in this manuscript and remains a reading …".
- Sources: claims 4–10.
- The three quotation fragments are exact substrings of the printed sentence on p. 588.
- The dictionary is stated as printed versus used: printed μ⁻¹ (= 2C); used C. The identification is declared a reading, not proved, of the A8 Scope (d) kind.
- The consistency claim with p. 589 is claim 6. I wrote "consistently with", not "the only reading": a second way to reconcile the two pages would rescale the Euclidean measure as well, and the record uses p. 589's dΦ literally (A2, A3).
- I left A1's Sources line (l. 751) unchanged: it names GJS p. 588 first, which is correct, and the Scope now says what that page does.
- "Of the sources of the cutoff construction" deliberately excludes Simon's book, which works in both spaces.

### F3, A5 (FROZEN ll. 987–988, 992, 997; new ll. 1004–1007, 1011–1015, 1020–1021; `A:domain` A5, page 15 in both builds)

Before (Sources, item (ii)):
```
(ii) is part of the cutoff construction; essential self-adjointness pinpoints, in their
roles per the audit: \cite[Thm.~V.12]{SimonBook}, \cite[Thm.~5.3]{Rosen70}, \cite{GJ2}. % whitelisted: …
```
After:
```
(ii): ``Let $g\ge0$, $g\,\epsilon\,L^1\cap L^{1+\epsilon}$.  Let $H(g)$ be given by (V.15).
Then (a) $H(g)$ is essentially self-adjoint on $C^\infty(H_0)$'' \cite[Thm.~V.12, p.~158]{SimonBook}, % whitelisted: …
(V.15) being ``$H(g)=H_0+H_I(g)$'', ``$H_I(g)=\int g(x)\,{:}P(\phi_F(x)){:}\,dx$'', with $P$
``semibounded'' \cite[pp.~141, 146]{SimonBook}; also \cite[Thm.~5.3]{Rosen70}, \cite{GJ2}.
```
Scope, appended after "(audit finding S3).":
```
For (ii), Theorem V.12(a) at each $g_s$ % whitelisted: …
($0\le g_s\in C_c^\infty\subset L^1\cap L^{1+\varepsilon}$, $P:=\lambda\mathscr P$
semibounded, $\phi_F$ as in the Scope of~\ref{A:cutoff}, so $H(g_s)=H_0+V(g_s)$) puts
$\mathscr C:=C^\infty(H_0)=\bigcap_nD(H_0^n)$ in $D(H_0)\cap D(V(g_s))$ as a core of the
self-adjoint $K(g_s)$; the identity on $\mathscr C$ is the linearity of $h\mapsto V(h)$.
```
Dossier: `(E17--E19).` became `(E17--E19); item (ii):` / `\texttt{simon-transfer-180}.`

What is printed and what is a reading (sources: claims 11 and 12):

- The hypotheses of Theorem V.12, checked for every g_s ∈ 𝒢: g_s ≥ 0 and g_s ∈ C_c^∞ ⊂ L¹ ∩ L^{1+ε}.
- P := λ𝒫 is semibounded in Simon's sense, inf P > −∞. For λ > 0 its leading coefficient λa_{2p′} is positive and its degree even. For λ = 0 it is P = 0; note that Simon's paraphrase "i.e. a_{2n} > 0" on p. 140 does not cover P = 0.
- The operators:
  - (V.15) is the operator sum H₀ + H_I(g). Its domain is D(H₀) ∩ D(H_I) (p. 146, problem (A)), and H₀ there is closed, since p. 146 speaks of cores for it.
  - With φ_F read as in A1's Scope (the reading already recorded there for Theorem V.2(b)), H_I(g_s) is V(g_s) and H(g_s) is H₀ + V(g_s). Its closure is K(g_s) (A1), and Lemma E.7(b) identifies Simon's H₀.
- The core:
  - "Essentially self-adjoint on C^∞(H₀)", in its usual sense, gives C^∞(H₀) ⊆ D(H₀) ∩ D(V(g_s)), and the closure of the restriction is self-adjoint.
  - That closure lies inside the self-adjoint K(g_s). A self-adjoint operator has no proper symmetric extension, so the two are equal, and C^∞(H₀) is a core for every K(g_s).
  - C^∞(H₀) does not depend on s.
- The identity: on 𝒞, V(g_s) = (1−s)V(g) + sV(g′) pointwise (V is linear in h, §2.1), so K(g_s)ξ − K(g_{s₀})ξ = (s−s₀)V(g′−g)ξ.

So the printed statement gives A5(ii). What remains is the φ_F reading (unchanged in kind from A1's Scope) and the usual meaning of "essentially self-adjoint on". Simon does not define C^∞(H₀) on the pages read; ⋂ₙ D(H₀ⁿ) is the standard meaning. The argument needs only that the set does not depend on g.

Other points:
- Prop. 8.2(ii), which consumes A5(ii) (FROZEN ll. 2525–2543), uses exactly a common core and this identity.
- No gap was found, so there is no new finding of severity above MINOR.
- The whitelist comment travels with each line that names V.12, in its positive (esa) role. The forbidden-string rule concerns V.12 only in a hypercontractivity context (`strategy.md` §4.3).
- The wording "in their roles per the audit" was dropped from the item (ii) line. A4's Scope still records audit finding S2.

### N4, A8 Scope (FROZEN ll. 1346–1350; new ll. 1370–1376; `A:gjs` A8, page 17 in both builds; the paragraph is on page 21 (new))

Before:
```
Assumptions~\ref{A:cutoff}--\ref{A:covar} are imported, and no stricter one is available
to this manuscript, since the printed proof of Theorem 1.1.7 itself obtains its
$h$-independent constant from Theorem 1.1.8 at the same $h$ (p.~597) while Theorem
1.1.8 is printed only ``uniformly as $h\to1$'' (p.~595).  Four points of scope are
recorded.
```
After:
```
Assumptions~\ref{A:cutoff}--\ref{A:covar} are imported.  The printed proof of Theorem 1.1.7
takes its $h$-independent constant from Theorem 1.1.8 at the same $h$ (p.~597), whose
estimate is printed ``uniformly as $h\to1$'' (p.~595) and ``uniform in the space cutoff $h$''
(p.~629, Source Fact~\ref{sf:printed}).  A stricter standard, admitting only cases that a
printed proof reaches, is not adopted: it would exclude A8(iv)-T (point (b)), and
Theorems~\ref{thm:D3}, \ref{thm:D4} would need the slicing of Remark~\ref{aux:d3-orient}.
Four points of scope are recorded.
```

- Sources: claims 13 and 14; Scope (b) and item (iv-T) (A8(iv)-T is "a case of the printed statement that its printed proof does not reach").
- The word "only" before "uniformly as h→1" was false, since p. 629 prints uniformity in h for Theorem 1.1.8's estimate. The conclusion "no stricter one is available" rested on that word.
- I did not adopt the cqft memo's stronger sentence, that a stricter standard "separates exactly A8(iv)-T from the rest". Remark N.39 and §D.e leave undecided whether the printed proof reaches D.3's and D.4's parallel pairs with a time-integrated partner without slicing. cqft's argument that it does (its N3) is cqft's alone; I did not check it.
- **Flag for the orchestrator:** this changes what the record says about A8's import standard. It says no longer "no stricter standard is available", but "a stricter one exists and is not adopted, and it would exclude A8(iv)-T". The status of no import changed: every item is still imported at its printed scope.

### F2, Lemma 9.1 statement (FROZEN ll. 2551–2552; new ll. 2577–2580; `lem:filter` 9.1, page 35 in both builds)

Before:
```
Choose an even $\chi\in C^\infty(\R;[0,1])$ with $\chi=0$ on $[-\gamma/2,\gamma/2]$ and
$\chi=1$ outside $(-\gamma,\gamma)$, and set
```
After:
```
Fix, once for each $\gamma>0$, an even $\chi\in C^\infty(\R;[0,1])$ with $\chi=0$ on
$[-\gamma/2,\gamma/2]$ and $\chi=1$ outside $(-\gamma,\gamma)$; $W_\gamma$, $T_\gamma$,
$C_{q,\gamma}$ below and $\Psi_\gamma$, $C_\gamma'$, $C_{N,\gamma,M}$ of Lemma~\ref{lem:rate}
depend on this choice.  Set
```

- This is the default one-sentence repair; the scaling normalisation was not used. Claim 15.
- Every statement stays true as written:
  - Lemma 9.1(i) and (ii) hold for every admissible χ.
  - Lemma 10.5 and Theorem 11.1 use Ψ_γ for the fixed χ.
  - §11 sets Ψ_{m₁} := Ψ_γ at γ = m₁, a single function once χ is fixed for that γ.
  - Remark 3.3's Ψ_{m₁,*} and "Ψ_γ formed with γ = s m₁,*" are each one function.
- d₀ = 4 + 2/γ does not depend on χ and is not listed.
- The Appendix A Ψ_γ rows are unchanged; the corrected Appendix A paragraph now names the filter for them.
- Theorem 12.2 states Ψ_{m₁}, consistent with the fixed choice.

### Appendix B, corrections history (new item after FROZEN l. 3519; new ll. 3554–3557; `app:provenance` B, page 47 in both builds; the item is on page 49)

After:
```
\item \emph{Corrections of wording} (23 November 2026, status council of 22 November): the
constants of the rate (abstract, \S1.2, Theorem~\ref{thm:MAIN}, Appendix~\ref{app:constants}),
the Scope of~\ref{A:cutoff} and~\ref{A:gjs}, the source of~\ref{A:domain}(ii),
Lemma~\ref{lem:filter} (filter); see the title-page notice.
```

- §1.2 is "The result" (checked in the contents).
- A one-line pointer and this three-line item move the same 30 labels (both measured), so I kept the informative version. A four-line version that also named the council's MINOR findings moved 37.

## 4. Findings

**W1 (constraint not met; layout only, no mathematics). The abstract cannot end on page 2.**
- Locator: title page, pages 1–3.
- In FROZEN, page 2 is full to within 1.9 pt: the last body line has yMax 761.6, against 763.5 on full body pages (measured with pdftotext -bbox).
- Any new paragraph before the abstract therefore pushes the abstract's tail to page 3. The shortest notice that carries the content you required takes 5 lines. The abstract also grows by 1 line, because the F1 clause is longer.
- The abstract now ends on page 3, 7 lines in, followed by the contents.
- I shortened the notice and the abstract clause as far as I could (G, F1 above); nothing short of rewriting the dated notices would make room.
- Repair options for the orchestrator: (a) accept this; (b) set the new notice after the abstract (the abstract then ends on page 2, but the notice no longer closes the title-page notices, and the contents and §1 shift the same way); (c) shorten an earlier notice (excluded by the brief).
- Severity: not a defect of the record. I report it as an unmet constraint.

**W2 (constraint partly met). Label pages: 30 of 238 labels change their page; no number changes; 125 pages kept.** The causes, from the measured shift along the document:
- (a) The A1 and A5 additions, required for N1 and F3, add about 10 lines to §2.4. Eleven labels on pages 13–27 move by one page (list in §5); the shift is absorbed by page 29, and pages 29–49 are identical to FROZEN.
- (b) The Appendix B item: page 49 had 11.6 pt free; a one-line list item costs 22.6 pt, and widow control then moves 2 lines into Appendix C. Nineteen labels on pages 52–113 (Appendices C–D) move by one page; Appendix E and the bibliography are unchanged.
- Earlier drafts moved 151, then 102, 81 and 37 labels. The front-matter growth is kept under the 88 pt that page 7 can absorb, so that A1 stays on page 10.
- Consequence: the page numbers in `docs/results.*` (and any other page locator) need regenerating. I did not run `docs/extract.py`, as instructed.

**W3 (MINOR). The same loose attribution remains outside my loci.**
- In `part_i/main.tex`, Appendices C and D speak of "the (finite,) unevaluated constant of Theorem C.5" or "S₂(B₃ₓ₅) of Theorem C.5": FROZEN ll. 4164, 7024–7025, 7199, 7390–7392, 7971–7974.
- In the public texts: `docs/imports.md` l. 32 ("Its constant M_B contains the finite, unevaluated constant of Theorem C.5") and `docs/status.md` l. 59 (inside the dated entry of 7 November: "… so the rate of Theorem 12.2(1) is explicit up to that constant").
- Why it fails: S₂ is defined in Definition N.14; Theorem C.5 makes it finite.
- The new notice says how the phrase is to be read, but names only the notice above it.
- Repair: the same correction as in Theorem 12.2 ("S₂ of Definition N.14, finite by Theorem C.5"), or leave the record as is and rely on the notice. `docs/` belongs to the other editor.
- Severity: MINOR.

**W4 (MINOR, not changed). "They define V(g) by normal ordering in Fock space" holds as printed for GJ2 (p. 365) and Rosen70 (p. 158) only.**
- GJ71 writes the Wick-ordered interaction and says "See [1] for notation" (p. 253), and its [1] is not on disk.
- I kept the sentence, as you asked.
- Severity: MINOR (attribution).

**W5 (bookkeeping, MINOR). Dossier and images.**
- The Simon pages read for A5(ii) beyond p. 158 have no page images in `audit_2026/evidence/`: pp. 140–141, 146 and 159–161, which are PDF pages 162–163, 168 and 181–183 of the copy in `refs/`.
- The Dossier line names only `simon-transfer-180`.
- The dossier map in `part_i/README.md` (row A5) does not yet list `simon-transfer-180`. I may not edit that file.
- Severity: MINOR.

**W6 (note, not a defect). The printed proof of Theorem V.12(a) (Simon p. 161) proves the core property on the vectors e^{−tH₀}u, u ∈ 𝔇, and concludes "Thus C^∞(H₀) is a core".**
- The inclusion C^∞(H₀) ⊆ D(H_I(g)) belongs to the statement; the proof does not show it separately. It is true for g ∈ L² by the N-estimate GJ2 prints as (1.2.9) on p. 365 (my remark; not checked in detail).
- The record imports the printed statement and, as for every import, does not re-verify its proof.

## 5. Checks actually run, with output

Build: in `part_i/`, `SOURCE_DATE_EPOCH=1794355200 FORCE_SOURCE_DATE=1 pdflatex -interaction=nonstopmode main.tex`, three passes, then a fourth to confirm reproducibility. pdfTeX 3.141592653-2.6-1.40.29 (TeX Live 2026).

- `grep -cE '^!' main.log`: 0
- `grep -c Overfull main.log`: 0
- `grep -icE undefined main.log`: 0
- `pdftotext main.pdf - | grep -nE '\?\?|TODO|Hmm|wait,'`: no output (exit 1)
- Pages: 125
- `shasum -a 256 main.pdf`: `4afbfb411d609943c9b4e3ef92516b16ad4da255b251307361ae811fd07d7cc4`. The fourth pass gave the same hash and `main.aux` was byte-identical to the third pass's.
- `shasum -a 256 main.tex`: `0f71e2a9def0e74f2f48c6aa9144aa8e222a5ca0bbf3502e40fb2fa11cb88022` (8782 lines; FROZEN 8744)
- At the start, `diff -q` of `part_i/main.tex` against FROZEN reported the files identical; FROZEN's `main.pdf` had sha256 `87084de8…80e`, 125 pages.

Labels (script: every `\newlabel` of the new `main.aux` against FROZEN's, number and page):
- 238 labels before and after; none added, none removed, **no number changes**.
- 30 page changes, each by exactly +1:
  - §§2.4–4: `A:stability` A3 13→14, `A:patch` A6 15→16, `eq:P` 15→16, `sf:CE2` 2.2 17→18, `sf:printed` 2.4 19→20, `rem:conv` 2.5 21→22, `subsec:weak` 2.6 22→23, `eq:fkn1` (3) 25→26, `eq:fkn2` (2) 25→26, `lem:slabFKN` 4.1 25→26, `lem:slabvac` 4.4 26→27.
  - Appendices C and D: `eq:ckappa` 52→53, `app:comparison` D 57→58, `sec:notation` D.a 58→59, `aux:notation-gjslattice` N.2 59→60, `aux:notation-stripdef` N.6 62→63, `sec:notation-strips` D.a.3 62→63, `aux:notation-kernel` N.19 69→70, `aux:notation-sharpidrem` N.23 75→76, `aux:d1-cov` N.25 79→80, `eq:d1-two` (37) 82→83, `eq:d1-deriv` (40) 84→85, `eq:d1-identity` (41) 84→85, `lem:D2` D.2 88→89, `sub:d2-lemma` D.c.2 88→89, `aux:d3-orient` N.39 96→97, `sub:d3-rem` D.d.4 96→97, `aux:constants-D4` N.50 110→111, `aux:constants-phi4` N.51 111→112, `aux:constants-s0` N.54 112→113.

Statement environments (script: theorem, proposition, lemma, corollary, hypothesis, assumption, remark, definition, srcfact, srcfactstar, aux*, compared by label):
- 127 labelled before and after; none added or removed; the 2 unlabelled ones unchanged.
- Changed textually: `A:cutoff` (A1), `A:domain` (A5), `A:gjs` (A8), `lem:filter` (Lemma 9.1), `thm:MAIN` (Theorem 12.2). Nothing else.

Rendering: pages 2, 3, 5, 13, 15, 16, 21, 35, 42, 46 and 49 were rendered at 80 dpi and looked at, pages 2 and 3 again after the last edit. Nothing lies outside the margins; the new notice and the new history item are their own paragraphs; the abstract ends on page 3, 7 lines in, followed by the contents.

AGENTS.md 3.8: I listed the control sequences of all added lines. All are standard LaTeX, amsmath or mathrsfs, or defined in the preamble: `\ip` l. 56, `\HH` l. 54, `\R` l. 46, `\dist` l. 58, `\Z`, `\A`, `\G`. The new symbols are defined where they are used or point to their definition:
- C^∞(H₀) := ⋂ₙ D(H₀ⁿ), in A5's Scope;
- H_I(g), P and (V.15), quoted;
- φ_F, through A1's Scope;
- dφ and μ⁻¹, quoted with their formula;
- S₂, through Definition N.14;
- M_*, λ_*, through §2.6; V_*, through N.20; the filter objects, through Lemmas 9.1 and 10.5.

Sources: I rendered or opened every page image cited in claims 1–15. `docs/` and `README.md` were read in FROZEN only, for the public sentences below.

## 6. Sentences for the public texts (for the orchestrator to apply)

`README.md` ll. 71–72. FROZEN text: "with a super-polynomial rate in dist(O, {g < 1}), explicit up to the finite constant of / Theorem C.5. The limit is …". Replace with:

> with a super-polynomial rate in dist(O, {g < 1}), given by an explicit formula in constants that are not evaluated: those of the imported GJS Theorem 1.1.7, which the source prints only as existing or as thresholds, and the stability constant S₂ (Definition N.14), finite by Theorem C.5. The limit is …

`docs/index.md` l. 37 (one line):

> with a super-polynomial rate in dist(O, {g < 1}), given by an explicit formula in unevaluated constants: those of the imported GJS Theorem 1.1.7 and the stability constant S₂ (Definition N.14), finite by Theorem C.5. The limit is locally normal,

`CITATION.cff` ll. 18–19 (plain ASCII, like the rest of that abstract). FROZEN text: "… with a super-polynomial rate, explicit up to one finite / stability constant; the uniform local moment …". Replace with:

> … with a super-polynomial rate given by an explicit formula in unevaluated constants, those of the imported clustering theorem and one finite stability constant; the uniform local moment …

## 7. Not done, not verified, not run

Not done:
- The abstract does not end on page 2 (W1).
- 30 labels change page (W2).
- No page images were added for Simon pp. 140–141, 146, 159–161 (W5).
- The dossier map row A5 in `part_i/README.md` and the record of this pass in `part_i/README.md` are not written: the files are not mine.
- The loci of W3 are not changed.
- The public sentences of §6 are not applied.

Not verified:
- cqft's claim that the printed proof reaches D.3's and D.4's parallel pairs after a Fubini step over single-time slices (its N3).
- The normalisation of Simon's φ_F beyond what A1's Scope already records as a reading.
- The definition of C^∞(H₀) in Simon's book (not found on the pages read).
- GJ71's [1] and GJS's [1] (not on disk).
- Rosen70's Theorem 2.1 page was read only through pdftotext, not on a rendered image.

Not run: `docs/extract.py` (as instructed), any git command that changes state, any KB command.

Other: `git status` shows `part_i/C5_reading_record.md` as modified. I did not touch it; another agent did. The dates "23 November 2026" in the notice and in Appendix B are true only if the commit is pushed today.

## 8. Files written

- `part_i/main.tex`, with the build products `part_i/main.pdf` (tracked), `main.aux`, `main.log`, `main.toc`, `main.out`.
- The report `wording-main.md` and the diff `wording-main.diff` (output of `git diff -- part_i/main.tex`), both in the council's reports directory.
- Scratch files outside the repository: measurement scripts, renders and two copies of intermediate states. They are not deliverables.
