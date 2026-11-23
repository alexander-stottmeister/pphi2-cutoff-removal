# Route T note, sections 1-4: audit of the analysis

Auditor "route-t-audit-analysis", working council of 23 November 2026.

- **Object.** `ugjs/route_t/route_t.tex`, the draft of 23 November 2026: 1492 lines, 25 pages
  (`pdfinfo`). I read it at audit time in the council's scratch directory. Statement numbers and
  pages come from its `route_t.aux`; line numbers are those of the draft.
- **Record.** `part_i/main.tex` at commit 49f2d23, read from the frozen copy. Numbers and pages come
  from `part_i/main.aux`; line numbers are those of that commit.
- **My part.** Everything from the beginning of the note through Theorem T.16 and the proof of
  Theorem T.2. That covers §§1-4: Definition T.1, Theorem T.2, Lemmas T.3-T.13, Theorem T.14,
  Lemma T.15, Theorem T.16 and §4.
- **Not my part.** §§5-7, which the second auditor reads, are given no verdict here, except where
  they bear on the statement of T.2.

## 1. Outcome

Every step of §§1-4 holds as written. There are no CRITICAL and no MAJOR findings, and four MINOR
ones. As far as my part goes, Theorem T.2 is **proved, conditional on** the conditions the note
itself lists (section 2, last row). One of those conditions, Simon's Remark on p. 164, can be
removed by a repair that uses only the record's own imports (finding F1).

## 2. Claims, with status

Locators are label, number and page from `route_t.aux`, then the lines of the draft.

| statement | locator | steps checked | verdict | status word, and what it is conditional on |
|---|---|---|---|---|
| Definition T.1, and the definitions (t1)-(t3) | `def:Mt`, T.1, p. 3, ll. 141-153; `eq:k`, `eq:Xi`, `eq:Psit`, (t1)-(t3), p. 4, ll. 189-204 | Ω_g ∈ D(V(h)) by Prop. 2.6; the resolvent norm; M̃(λ0) ≤ M | holds (MINOR F3) | definition |
| Lemma T.3 (resolvent transforms) | `lem:transforms`, T.3, p. 4, ll. 243-313 | (i)-(iv), all redone by hand | holds | proved (spectral theorem, Fubini) |
| Lemma T.4 (locality discrepancy) | `lem:discrepancy`, T.4, p. 6, ll. 315-330 | identity and bound | holds | proved |
| Lemma T.5 (separation with exponential discrepancy) | `lem:sep`, T.5, p. 6, ll. 337-426; (t4), (t5) | Steps 1-4; principal-value limit and its sign; the choice a = R'/γ | holds | proved |
| Lemma T.6 (resolvent-weighted clustering) | `lem:cluster`, T.6, p. 7, ll. 433-459 | F = G by Step 2 of record Lemma 9.3; T.4; T.5 at R' = R/2; constants | holds | proved, from Prop. 2.7, Locality (§2.1, A6(iii)) and (G_γ) |
| Lemma T.7 (resolvent form of the state derivative) | `lem:deriv`, T.7, p. 8, ll. 466-525; (t6) | Steps 1-4; the domain paragraph | holds | proved, from Prop. 8.2(ii), the first assertion of Lemma 10.2, Prop. 2.6, Lemma 9.1(ii) and (G_γ) |
| Lemma T.8 (two-regime bound) | `lem:tworegime`, T.8, p. 8, ll. 527-552 | the three bounds; T.6's hypotheses at O_{\|t\|} | holds | proved; M̃(λ0) enters as a number |
| Proposition T.9 (one-path estimate) | `prop:onepath`, T.9, p. 9, ll. 554-600 | Steps 1-4; the shell count of six; the factor 12; convergence | holds (MINOR F2) | proved, from T.7, T.8, Prop. 8.2(i), Lemma 9.1(i) and Lemma 3.1 |
| Lemma T.10 (rate function) | `lem:rate`, T.10, p. 9, ll. 602-625 | monotonicity; decay faster than every power; final assertion | holds | proved |
| Lemma T.11 (elementary inequality) | `lem:ineq`, T.11, p. 10, ll. 629-650 | closed form of k; monotonicity; both cases | holds | proved |
| Lemma T.12 (time slicing) | `lem:slice`, T.12, p. 10, ll. 667-735 | Steps 1-4 (joint measurability, separability, Pettis, Bochner, κ → ∞); (ii) | holds | proved, from Def. N.26, Lemmas N.24, N.25, N.28(a) and standard measure theory |
| Lemma T.13 (time-integrated interaction) | `lem:Vbar`, T.13, p. 11, ll. 737-805 | (i)-(iv); the hypotheses of N.28(c), N.28(f)(2), N.23'(ii)-(iii), N.21(ii), N.20(iv) | holds | proved |
| Theorem T.14 (time-integrated copy of D.4) | `thm:TD4`, T.14, p. 12, ll. 807-876; table ll. 878-917 | Steps 1-5; every hypothesis of Lemma D.2; every row of the table against the record's proofs of D.2 and D.4 | holds | proved, conditional on A8(iv) at its printed scope in cases P3 (parallel) and P4 (transverse), and on the reading of A8 Scope (d) for the pieces Q̄_{n,n',k,k'} and U_{Δ,n''} |
| Lemma T.15 (Euclidean to spectral) | `lem:fkn`, T.15, p. 14, ll. 919-1004 | (i) closed graph; (ii) Simon V.15 and its Remark, read on the rendered page; (iii) dominated convergence, measurability, Tonelli | holds (MINOR F1) | proved, conditional on Simon's Remark on p. 164 (removable, F1); from A2, A3, A5(i), Lemma 4.4 and T.13 |
| Theorem T.16 (bound on M̃) | `thm:Mt`, T.16, p. 15, ll. 1006-1023 | the spectral computation; T.11; the P_0 term; T.15(iii) with T.14 at h_{T,g} | holds | proved, conditional as T.14 and T.15 |
| Theorem T.2 and its proof (§4) | `thm:routeT`, T.2, p. 4, ll. 206-239; `sec:assembly`, §4, p. 16, ll. 1033-1068 | (a), (b), (c); same ω_∞; what replaces Ψ_{m1}; constants; greps of the record for (c) | holds (MINOR F4) | proved, conditional on the list below |

**What T.2 is conditional on, in my part.**

1. Assumptions A1-A8 of the record, with A8(iv) used only in the cases P1-P4 and A8(iv)-T not used.
2. The readings the record declares: the Scope paragraphs of A1, A3 and A6, and A8 Scope (d), now
   including the monomials Q̄_{n,n',k,k'} of type (1.1.6) with r = 2. The open items of
   `part_i/C5_reading_record.md` come with these readings.
3. Simon's Theorem V.15 with its Remark (p. 164), in Lemma T.15(ii). This condition is removable
   (F1).
4. The record's statements used as the record states them. Their hypotheses were checked at each
   point of use (section 4); their proofs were not re-audited (section 6).

## 3. Findings

**F1 (MINOR): the Remark of Simon, p. 164, in Lemma T.15(ii).**

- **Locator.** Lemma T.15(ii), ll. 940-965. Also the paragraph "The role of the cutoff h_{T,g}",
  ll. 996-1004, and the status lines at ll. 236-237 and ll. 1409-1411.
- **Quotation** (l. 946): its Remark says "More generally, the above holds if
  $G_j^F\in\bigcap_{p<\infty}L^p(Q_F)$ and $G_j^{s_j}=J_{s_j}G_j$". And ll. 1002-1004: "The
  slab-transfer statement that carries the passage is Simon's (V.47) at two times placed
  asymmetrically in the slab ..., the source of A2; the record's Lemma 4.1 states only the
  symmetric placement $\mp t/2$."
- **What the source prints.** I rendered PDF pages 185-186 of the copy in `refs/` at 150 dpi
  (printed pp. 163-164). The page image `audit_2026/evidence/simon-fkn-185.png` is printed p. 163;
  p. 164 has no dossier image.
  - The note's quotations are accurate. The Remark continues: "and not only if $G_j^F$ is a function
    of only finitely many fields."
  - Theorem V.15 is printed for arbitrary $t_1,\dots,t_n>0$, "where $s_0$ is arbitrary and
    $s_j=s_{j-1}+t_j$" (p. 164). So the asymmetric placement used in (ii), $s_0=-T$,
    $s_1=\tau$, $s_2=\tau'$, $s_3=T$, lies within the printed statement. The citation carries
    what is claimed, at asymmetric times.
  - The Remark has no proof. The printed proof treats bounded functions, then "arbitrary
    polynomially bounded" functions of finitely many fields. Its limit step uses "the
    hypercontractive properties (Theorem V.11 (iv)) of $e^{-tH}$", which the record does not import.
- **Why it matters.** The record's A2 (main.tex ll. 825-838) states the formula "for all bounded
  time-zero functions", "together with the analogous multi-time formulas on finite slabs". Applying
  the Remark to the unbounded X = V(h) is therefore an import beyond A2's stated scope. The note
  discloses it as a condition. The paragraph at ll. 996-1004 does not mention that A2's own
  multi-time clause covers bounded functions at any placement.
- **Repair** (only the record's imports).
  1. Apply A2's multi-time formula on the slab [-T, T] at the times -T < τ < τ' < T. Use the
     bounded functions 1, X^{[ℓ]}, X^{[ℓ]}, 1, with X^{[ℓ]} = (-ℓ)∨(X∧ℓ) the clipped truncation of
     Lemma 4.3(ii).
  2. Divide by Z(h_{T,g}) and cancel e^{-2TE(g)}, exactly as in the note. This gives (ii) for
     X^{[ℓ]}.
  3. Let ℓ → ∞ as in the proof of Lemma 4.3(ii). On the path side, use dominated convergence with
     the majorant |J_τX||J_{τ'}X|. It lies in L¹(dq_{h_{T,g}}) because J_τX ∈ L⁴(dμ_0), hence
     J_τX ∈ L²(dq_{h_{T,g}}) by Lemma N.32, and Cauchy-Schwarz applies.
  4. On the Hilbert side, X^{[ℓ]}ψ_b → Xψ_b in L², with ψ_b ∈ D(X) by A5(i) and the dominator
     |X|²|ψ_b|². Then e^{-(τ'-τ)H}X^{[ℓ]}ψ_{T-τ'} converges because the semigroup is bounded.
  5. Delete "Simon's Theorem V.15 with the Remark on p. 164" from the conditions of T.15, T.16 and
     T.2 and from §7. Replace the sentence at ll. 1002-1004 accordingly.

  Lemmas 4.1-4.3 as stated do not suffice: they cover symmetric times in a symmetric slab. If the
  Remark is kept instead, the dossier needs an image of p. 164 (PDF page 186). The note's §7.4,
  item 2, names the truncation route but does not carry it out.

**F2 (MINOR): Proposition T.9, Step 3, strict inequalities.**

- **Locator.** Proposition T.9, Step 3, ll. 582-583.
- **Quotation.** "points $y<a_O-d$ and $y'>b_O+d$ of $B_j$ would give $y'-y>2$".
- **Reason.** B_j is disjoint from the open interval O_d = (a_O - d, b_O + d). Its points
  therefore satisfy y ≤ a_O - d or y ≥ b_O + d, and the strict inequalities leave out the
  endpoints.
- **Repair.** Write ≤ and ≥. Then y' - y ≥ b_O - a_O + 2d > 2, which still contradicts
  diam B_j ≤ 2. Correctness is unaffected.

**F3 (MINOR): Definition T.1, the reason for the resolvent bound.**

- **Locator.** Definition T.1, ll. 149-150.
- **Quotation.** "The operator $(\lambda_0-iH(g))^{-1}$ is bounded with norm $\le\lambda_0^{-1}$
  because $H(g)\ge0$."
- **Reason.** The bound holds for every self-adjoint H, since $|\lambda_0-iE|\ge\lambda_0$ for real
  E. Positivity plays no role.
- **Repair.** "because H(g) is self-adjoint". Correctness is unaffected.

**F4 (MINOR): coordinates of the new rate, and the integration list.**

- **Locator.** Theorem T.2, ll. 206-222; §7.3, ll. 1450-1454.
- **Reason.** T.2 is proved in the working coordinates (§1.1, ll. 119-121), as the record's
  Theorem 12.2 is. The record reads its rate in the original coordinates through Remark 3.3(1),
  as d ↦ Ψ_{m_{1,*}}(sd) (main.tex ll. 1660-1669 and 1698-1701). The same transport applies
  verbatim to Ψ̃. It gives d ↦ Ψ̃_{m_{1,*},λ0}(sd), with λ0 in working units. Neither T.2 nor the
  integration list of §7.3 says so.
- **Omissions from the §7.3 list.** It also leaves out the record's other places that name M,
  Ψ_γ or d_0 as ingredients of the rate:
  - Remark 3.3, ll. 1656-1657;
  - the notation table, ll. 613 and 618-619;
  - Appendix A, ll. 3369-3372 and 3378;
  - the imports paragraph of Theorem 12.2, ll. 3098-3099 ("The constant $M$ of item (5), and
    through it the rate $\Psi_{m_1}$ of item (1)");
  - the introduction, ll. 237-241 and 351.
- **Repair.** Add one sentence to T.2 and add these items to §7.3. Correctness is unaffected.

## 4. Step-by-step record

Each step is typed as one of three kinds:

- **[calc]**: an explicit calculation, redone by hand.
- **[rec]**: a numbered statement of the note or of the record. Its statement was read in
  main.tex and its hypotheses were checked here.
- **[ext]**: a printed external statement, read on the rendered page.

Every step below holds, except where a finding is named.

**Definition T.1.**

- [rec] Prop. 2.6 requires h real, in L¹ ∩ L², of compact support. A bounded h supported in
  [a, a+2] is such an h.
- [calc] The resolvent bound (F3).
- [calc] M̃(λ0) ≤ λ0^{-1}‖V(h)Ω_g‖ ≤ ‖V(h)Ω_g‖ for λ0 ≥ 1.

**Lemma T.3.**

- (i) [calc]
  - HP_0 = 0, so e^{itH}P_0 = P_0 and e^{itH} - P_0 = e^{itH}Q.
  - Continuity by strong continuity of the group.
  - |F| ≤ ‖XΩ‖‖QAΩ‖ ≤ ‖XΩ‖‖A‖.
- (ii) [calc]
  - ∫_0^∞ e^{-λ0 v}e^{-ivE}dv = (λ0+iE)^{-1}; the weak Bochner identity follows by Fubini against
    the finite measure ⟨x, P_H(·)y⟩.
  - Hence F̃(t) = ⟨XΩ, (λ0+iH)^{-1}e^{itH}QAΩ⟩ = ⟨u, e^{itH}QAΩ⟩. This uses
    ((λ0+iH)^{-1})^* = (λ0-iH)^{-1}, and that Q commutes with the resolvent.
  - Q = P_H([γ,∞)) under the spectral hypothesis, which gives the support.
  - The variation is at most ‖u‖‖QAΩ‖ ≤ m̃, by Cauchy-Schwarz over partitions.
- (iii) [calc] The same computation with (λ0-iE)^{-1}, giving G̃(t) = ⟨QA^*Ω, e^{-itH}u⟩, with
  the image measure on (-∞, -γ].
- (iv) [calc]

**Lemma T.4.** [calc]

- For t ∈ (-R, R), F - G = 0 on (-R, t], so F̃ - G̃ = e^{-λ0 t}c.
- By T.3(iv), |c| ≤ 2m̃e^{λ0 t} for every t ∈ (-R, R); the infimum as t ↓ -R gives
  |c| ≤ 2m̃e^{-λ0 R}.
- The bound uses m̃, built from the resolvent-weighted vector u, not ‖XΩ‖. This is the point at
  which the route stops needing M.

**Lemma T.5.**

- **Step 1** [calc]
  - (t - iε)^{-1} = i∫_0^∞ e^{-(ε+it)E'}dE'.
  - Fubini applies (the absolute integrand is e^{-t²/(2a)}e^{-εE'}).
  - ∫e^{-t²/(2a)}e^{itk}dt = (2πa)^{1/2}e^{-ak²/2}.
  - f̌ ∈ [0,1], increasing to Φ(√a E) as ε ↓ 0.
  - This agrees with the record's (20), main.tex ll. 2631-2638.
- **Step 2** [calc]
  - |t - iε| ≥ |t|, and |t|^{-1} ≤ |t|/R'² for |t| ≥ R'.
  - So ∫_{|t|≥R'}|f| ≤ a e^{-R'²/(2a)}/(πR'²), uniformly in ε.
- **Step 3** [calc], the principal value.
  - (t - iε)^{-1} = (t + iε)/(t² + ε²).
  - Imaginary part: put t = εs; dominated convergence with dominator sup|φ|·(1+s²)^{-1} gives the
    limit πφ(0) = π.
  - Real part: symmetrize; dominated convergence with dominator 2 sup|φ'| (mean value theorem).
    Since φ(t) - φ(-t) = -2e^{-t²/(2a)} sinh(λ0 t), the limit is -2J.
  - The limit of ∫_{-R'}^{R'} φ(t)(t-iε)^{-1}dt is -2J + iπ. Times c/(2πi) this is
    c/2 + icJ/π; the sign checked: -2J/(2πi) = iJ/π.
  - |c/2 + icJ/π| = |c|(1/4 + J²/π²)^{1/2} ≤ |c|(1/2 + J/π), since J ≥ 0.
  - J ≤ ∫_0^{λ0 R'} sinh x/x dx ≤ sinh(λ0 R'), by tanh x ≤ x.
- **Step 4** [calc]
  - The identity holds for each ε.
  - The left side converges by dominated convergence, since 0 ≤ f̌ ≤ 1.
  - The last term converges by Step 3, so the tail term converges too. Its limit is bounded by
    2m̃a(πR'²)^{-1}e^{-R'²/(2a)}, uniformly in ε, because |F̃ - G̃| ≤ 2m̃.
  - The Gaussian tail 1 - Φ(x) ≤ e^{-x²/2}/2 follows from (x+y)² ≥ x² + y².
  - The three-term decomposition of F̃(0) = ρ̃(ℝ) is exact.
  - With a = R'/γ, both exponents equal γR'/2, and a/(πR'²) = 1/(πγR').
- **Boundary.** At c = 0, R' = R the bound is the record's Step 4 before simplification (main.tex
  ll. 2663-2666).

**Lemma T.6.**

- [rec] F and G are those of the proof of Lemma 9.3 (main.tex ll. 2687-2690).
- [rec] F = G on (-R, R) by Step 2 of Lemma 9.3 (ll. 2698-2710). Its inputs are:
  - Prop. 2.7: β^g_t(A(O)) ⊆ A(O_{|t|}) for every g ∈ C_H.
  - Affiliation of X with A(O_{|t|})', given by hypothesis, since dist(B, O_{|t|}) ≥ R - |t| > 0.
  - Ω ∈ D(X), X = X^*, and e^{-itH}Ω = Ω.

  The condition γR ≥ 1 of Lemma 9.3 is not used in that step.
- [rec] The hypotheses of T.3 hold. H(g) ≥ 0 is self-adjoint, and (G_γ) gives the spectrum and
  dim ker = 1, with Ω = Ω_g.
- [rec] T.4 gives |c| ≤ 2m̃e^{-λ0 R}. T.5 is applied with R' = R/2 ≤ R.
- [calc] (1 + 2/(πγR/2))e^{-γR/4} = (1 + 4/(πγR))e^{-γR/4}.
- [calc] 2e^{-λ0 R}(1/2 + sinh(λ0 R/2)/π) ≤ e^{-λ0 R} + e^{-λ0 R/2}/π, by 2 sinh x ≤ e^x.
- Why R' = R/2: at R' = R the c-term is bounded only by m̃(e^{-λ0 R} + 1/π), which does not decay.
- For small γR, min{1, Ξ} = 1 and the bound is T.3(iv).

**Lemma T.7.**

- **Step 1** [rec] The record's first display, ll. 2738-2742, using Prop. 8.2(ii) and the
  self-adjointness of the bounded H_s^{-1}Q_s. Ω_s ∈ D(V(v)) by Prop. 2.6.
- **Step 2** [rec] The first assertion of Lemma 10.2 (ll. 2771-2772) and finite additivity
  (§2.1, ll. 505-507). h_j = η_j v is real, smooth and of compact support, so Ω_s ∈ D(V_j) by
  Prop. 2.6.
- **Step 3** [calc] For E ≥ γ, (λ0+iE)^{-1}(i + λ0E^{-1}) = E^{-1}, and both functions vanish at
  E = 0. Q = 1_{[γ,∞)}(H) under (G_γ).
- **Step 4** [rec] Lemma 9.1(ii). Its hypothesis is H self-adjoint with spectrum in
  {0} ∪ [γ, ∞); and 1 - P_{ker H} = Q. The integral is applied to the vector
  (λ0+iH)^{-1}QAΩ and paired with V_jΩ. [calc] The resolvent commutes with e^{itH} and with Q.
- **Spectral test by hand.** ∫E^{-1}dρ = ∫(i + λ0E^{-1})(λ0+iE)^{-1}dρ.
- **Domains.**
  - Everything applied to Q_sAΩ_s is bounded: H_s^{-1}Q_s by γ^{-1} through (G_γ), and the
    resolvents by λ0^{-1}.
  - The only unbounded operator is V_j, applied only to Ω_s ∈ D(V_j). V(v)Ω_s is needed only in
    Step 1, where Prop. 2.6 supplies it.

**Lemma T.8.**

- [rec] (g_s, h_j) ∈ 𝒜. g_s ∈ 𝒢 ⊂ C_H by Lemma 3.1(iii). h_j is real and measurable, with
  ‖h_j‖_∞ ≤ 1 and supp h_j ⊆ [j-1, j+1] (main.tex ll. 2772-2774). So ‖u_{j,s}‖ ≤ M̃(λ0).
- [calc] e^{itH}QAΩ = Qβ_t(A)Ω.
- [rec] The hypotheses of T.6:
  - V_j is self-adjoint (A1).
  - V_j is affiliated with A(O')' whenever dist(B_j, O') > 0 (Locality, §2.1; h_j is bounded).
  - Ω_s ∈ D(V_j).
  - β_t(A) ∈ A(O_{|t|}), an open bounded interval (Prop. 2.7).
  - R ≥ r_j - |t| > 0 [calc].
- Ξ is nonincreasing [calc].

**Proposition T.9.**

- **Step 1** [calc] supp v ⊆ ℝ \ O_d, hence r_j ≥ d.
- **Step 2** [calc] The split at |t| = r_j/2.
- **Step 3** [calc]
  - Each side holds at most three j, since a half-open interval of length 3 contains three
    integers. Hence at most six j per shell.
  - The one-side argument needs |O_d| > 2, which is why the threshold is d ≥ 1 (F2).
- **Step 4** [rec] Prop. 8.2(i): P_s is norm-C¹ on (0,1) and norm-continuous on [0,1]. The
  fundamental theorem of calculus is applied on [ε, 1-ε]. The norm of the hermitian functional is
  handled as in the record, ll. 2869-2871.
- **Factor.** 12 = 2 × 6.
- **Convergence** [calc] For n ≥ 1, 4/(πγn) ≤ 4/(πγ), and Lemma 9.1(i) bounds T_γ.

**Lemma T.10.** [calc]

- ⌊d⌋ ≥ (1+d)/4 for d ≥ 1.
- The geometric sums.
- (1+n/2)^{-q} ≤ 2^q(1+n)^{-q}.
- Σ_{n≥m}(1+n)^{-q} ≤ m^{1-q}/(q-1).
- The constant on [0, 1).
- The constant C_N also depends on χ, through ‖W_γ‖_1 and C_{q,γ}; the "Constants" paragraph
  (ll. 224-228) says so.

**Lemma T.11.** [calc]

- ∬_{[-1/2,1/2]²}φ(τ-τ') = ∫_{-1}^1(1-|u|)φ(u)du.
- Integration by parts gives (E - 1 + e^{-E})E^{-2}.
- k(2) = (1 + e^{-2})/2 = 1/c_k.
- Case E ≤ 2: monotonicity of k.
- Case E ≥ 2: 2(E-1)/E² ≥ 1/E ≥ 1/(1+E²) ≥ 1/(λ0² + E²).

**Lemma T.12.**

- **Step 1** [calc] A_κ(·)(q) is continuous and w is bounded with compact support, so pointwise
  Fubini applies.
- **Step 2** [rec]
  - N.24 with ℓ = 2 gives E[Q^{(κ)}(t)²] = n!∬w w G_{κκ}((0, x-y))^n.
  - N.25(iii) gives G_{κκ} ≤ M_1.
  - N.25(iv) with d = 1 gives finiteness.
  - The bound c_w is independent of t and of κ ≥ 2.
- **Step 3** [calc]
  - (z, q) ↦ A_κ(z)(q) is continuous in z for each q and measurable in q for each z. It is
    therefore jointly measurable (a Carathéodory function).
  - The Tonelli bound is ‖φ‖_2(n!c_κ^n)^{1/2}‖w‖_1.
  - L²(dμ_0) is separable. The σ-algebra is generated by the Φ(f) (main.tex ll. 4732-4734), and
    Φ(f) = lim Φ(f_m) pointwise, because every q ∈ 𝒮' is continuous on 𝒮(ℝ²), which is separable.
  - Pettis's theorem gives strong measurability. Boundedness by c_w^{1/2} on a unit t-interval
    gives Bochner integrability.
  - The integral is identified by its pairings with every φ ∈ L².
- **Step 4** [rec] N.28(a) for types (a) and (b). [calc] A pointwise limit of strongly measurable
  functions is strongly measurable. Dominated convergence with the dominator 2c_w^{1/2} on a unit
  interval.
- **(ii)** [rec] (1.1.8) and Remark N.2(ii). [calc] Cauchy-Schwarz on an interval of length 1.
- **"Borel versions"** [calc]

**Lemma T.13.**

- **(i)** [rec]
  - T.12 with Δ_{0,k}, after taking a Borel version of h'.
  - N.28(f)(2). Hypotheses: a real, bounded, measurable kernel vanishing outside one column, and
    0 ≤ n ≤ 2p'.
  - Remark N.23(b) (linearity), N.11(i) (h' = Σ_k h'_k over the three columns k_a, k_a+1, k_a+2)
    and N.23'(iii).
- **(ii)** [rec]
  - N.23'(ii), d = 2, gives V̄_{n,k} ∈ Γ_n(ℋ_G) in Simon's sense.
  - The Bochner norm inequality, and the isometry of J_τ on every L^p (proof of N.22).
  - N.20(iv) with N.23'(iii) for V_*.
  - The argument of N.21(ii) uses only Y ∈ ⊕_{r≤2p'}Γ_r, which V̄(h') is.
- **(iii)** [rec] N.28(c), type (a).
- **(iv)** [calc] The kernel norm acquires the factor ‖1_{[-1/2,1/2)}‖_2 = 1. The weights are as
  in N.43(iii). There are at most 9 ordered column pairs.

**Theorem T.14.** I read the record's proofs of Lemma D.2 (main.tex ll. 6323-6449) and Theorem
D.4 (ll. 7043-7125) and compared them step by step.

- **Step 1.** N.32: V̄ ∈ L⁴(dμ_0) ⊂ L²(dq_h).
- **Step 2.** C.2: Z(h^B) ≥ e^{-λ|a_0||Λ|} with |Λ| = 15. N.15(iii)-(iv): ‖e^{-𝒰_{h^B}}‖_2 ≤ S_2.
  Cauchy-Schwarz, with ‖V̄²‖_2 ≤ 9^{p'}V_* from T.13(ii).
- **Step 3.** It depends only on R = S_a and B. Q̄ is localized in row 0 and in the columns of h',
  exactly where Q_V is.
- **Step 4.** The hypotheses of D.2(a), checked:
  - F is a finite sum of localized monomials of type (1.1.6), with kernels in L²(ℝ⁴) and
    individual degrees ≤ 2p' < n̄.
  - R is non-empty and contains every localization square.
  - B ⊇ R is a box, and h ∈ 𝒞_E.
  - Every Δ ∈ 𝒟(h,B) receives a strip of width j ≥ 1 that separates it from ⋃S_a.
  - ⟨F⟩_h = ∫V̄² dq_h, since F = V̄² holds μ_0-almost everywhere.
- **Step 5.** The constant M_B² is identical to D.4's (main.tex ll. 7016-7018).
- **The table, ll. 878-917.** All 14 rows are right as stated:
  - setting (changed);
  - box and rings (unchanged);
  - V_* (used through the Bochner inequality);
  - N.43(i)-(iii) (changed as stated; the same bound);
  - Steps 1, 2 and 3 (unchanged);
  - the comparison with N.21(ii) (it applies, via N.23'(ii));
  - Step 4 (the same form; Q_1 is now of type (1.1.6));
  - "class (T) is now P4, not A8(iv)-T". This is literally right by the record's definition of
    A8(iv)-T, "Source Fact 2.2 applied to a sharp-time monomial $Q_1$ of type (1.1.5)" (main.tex
    ll. 1156-1159).
  - Step 5 and Appendix C (unchanged).
- **The GJS-norm bound** of the time-integrated pieces is the same number as for Q_V
  (T.13(iv)).

**Lemma T.15.**

- **(i)** [rec] A5(i): Ran e^{-sK(g)} ⊆ D(V(h)). The range of e^{-sH} is the same. X is closed,
  and the closed graph theorem applies.
- **(ii)** [ext] Simon's Theorem V.15 with its Remark (F1). Its hypotheses, checked:
  - g ∈ C_H is ≥ 0, bounded and of compact support, so g ∈ L¹ ∩ L^{1+ε}.
  - X ∈ ⋂_p L^p, by (V.6b) in A1(d).
  - t_1 = T+τ, t_2 = τ'-τ and t_3 = T-τ' are all > 0 for T ≥ 1.
  - s_0 = -T, which is allowed since s_0 is arbitrary.
  - The dictionary is A2's display (Simon's H is K(g); his U(g⊗(s_0,s_n)) is 𝒰_{1_{[s_0,s_n]}⊗g}).

  [calc] The factor e^{-2TE(g)} cancels since t_1+t_2+t_3 = 2T, and ⟨Ω_0, e^{-2TH}Ω_0⟩ = ‖ψ_T‖².
  X is symmetric, and ψ_{t_1} and e^{-t_2 H}Xψ_{t_3} lie in D(X) by A5(i).
- **(iii)**
  - [rec] U ↦ ∫UW dq is bounded on L²(dμ_0) for W ∈ L⁴, by Hölder (2,4,4) and A3 at ρ = 4.
  - The Bochner identity of T.13(i), and two commutations of bounded functionals with Bochner
    integrals.
  - The dominator: Xψ_b = Xe^{-H/2}ψ_{b-1/2} for b ≥ 1/2, and ‖ψ_T‖ ≥ c_g by Lemma 4.4. It is
    uniform in T ≥ 1.
  - The pointwise limit: ψ_s → c_gΩ_g (Lemma 4.4), and Xe^{-H/2}Ω = XΩ.
  - Measurability: the integrand is continuous off the diagonal, and the diagonal is null.
  - Fubini, dominated convergence and Tonelli then give ∫k dμ_{XΩ}.

**Theorem T.16.** [calc]

- ‖(λ0-iH)^{-1}QXΩ‖² = ∫(λ0²+E²)^{-1}dμ ≤ c_k⟨QXΩ, k(H)QXΩ⟩, by T.11 on spec H ⊆ [0,∞).
- The P_0 term k(0)|⟨Ω,XΩ⟩|² is ≥ 0, and the cross terms vanish.
- [rec] T.15(iii), then T.14 at h_{T,g} ∈ 𝒞_E (Lemma 3.1(ii)) with h' = h.
- No gap is used.

**Theorem T.2 and §4.**

- **(a)** This is T.16.
- **(b)**
  - Theorem 7.8 (main.tex ll. 2350-2358): (G) for every g ∈ C_H, with 0 a simple eigenvalue.
    This gives (G_γ) with γ = m1.
  - T.9 and T.10 hold with M' = M̃_*.
  - Theorem 11.1, Steps 1-3 (ll. 2938-2965): Step 1 uses T.9 with d ≥ 1; Step 2 is unchanged;
    Step 3 uses T.10.
  - Proposition 11.2 is unchanged.
  - Theorem 12.2 (1)-(4) (proof, ll. 3102-3124): (3) via Prop. 12.1; (4) via Lemma 2.8 and
    Prop. E.5.
  - Corollary 12.3 (ll. 3134-3160): Ψ̃(2n-R) → 0.
- **(c)** Checked by grep, section 5.
- **The questions of the brief.**
  - Same ω_∞: yes. It is the local-norm limit of the net, and net limits are unique.
  - What replaces Ψ_{m1}: Ψ̃_{m1,λ0}, with M' = c_k^{1/2}M_B, for any fixed λ0 ≥ 1.
  - Constants: M̃_* does not depend on λ0, g or h. Ψ̃ depends on m1, λ0, χ and M_B.
  - The threshold is d ≥ 1.
  - Decay: faster than every inverse power, but not exponential (the T_{m1} terms), as in the
    record.

**Boundary values re-run.**

- λ0 = 1. At E = 0, T.11 reads 1 ≤ c_k.
- E = 0, generally: λ0^{-2} ≤ c_k k(0) = c_k.
- γR small: T.6 reduces to the trivial bound.
- d = 1: ⌊d⌋ = 1, and |O_d| > 2 still holds. Below d = 1, Step 3's one-side argument can fail.
- λ = 0: then V ≡ 0, V_* = 0, S_2 = 1 and c_U = 0. So M_B = 0 and Ψ̃ = 0 for d ≥ 1. This is
  consistent with ω_g = ω_0 for every g.
- p' = 1 and h' = 0: no change.
- T = 1, τ = -1/2: b = T + τ = 1/2, the edge of the dominator's range.
- a ∈ 1/2 + ℤ: the columns are as in N.45.

## 5. Checks run

**Label tables.**

- `route_t.aux`, all labels. The numbers and pages in the table of section 2 are taken from it,
  for example `thm:TD4` → T.14, p. 12 and `lem:fkn` → T.15, p. 14.
- `part_i/main.aux`, 238 labels. Every record number I cite was taken from it.

**Rendering.**

- `pdftoppm -r 150` of PDF pages 184-186 of Simon's book in `refs/`; I read pages 185 and 186
  (printed pp. 163-164).
- I opened `audit_2026/evidence/simon-fkn-185.png`: printed p. 163, the same page.

**Greps of the record.**

- `thm:M2` enters the chain at l. 2776 (Lemma 10.2), l. 2921 (head of §11) and l. 3104 (proof of
  12.2(5)). Its other occurrences are imports, scope or remarks.
- `thm:D4` occurs in proofs outside Appendix D only in Theorem 5.1 (ll. 1923, 1932, 1939) and
  Corollary 5.2 (l. 1971).
- §7, ll. 2055-2389: no `thm:M2`, `thm:D4`, `M_B`, "transverse" or `lem:localize`. Its only
  application of Source Fact 2.2 is Lemma 7.4, across the parallel strip {|x⁰| < t/2-1}
  (l. 2202). The rest goes through Theorem D.3.
- §13, ll. 3163-3275: it uses `lem:cluster` with the bounded X = B (Step 1, ll. 3207-3222), and
  `thm:MAIN`(1), (3), (4) only through local-norm convergence. There is no M and no Ψ. This
  answers the question the note leaves open in §7.3, l. 1444. I did not audit §13.

**The note's build artifacts** (not rebuilt).

- In `route_t.log`, `grep -cE '^!'` gives 0, `grep -c Overfull` gives 0 and
  `grep -icE undefined` gives 0.
- `pdftotext route_t.pdf - | grep -nE '\?\?|TODO|Hmm|wait,'` prints nothing.
- 25 pages.
- Token scan: `grep -oE '\\[A-Za-z]+' route_t.tex | sort | uniq -c | sort -n`. Every control
  sequence used at most twice is a LaTeX command or a macro defined in the preamble (\Z, \C,
  \Ran), or a symbol defined in the record: ν = δ in the notation of N.23', χ of Lemma 9.1, ψ̂ of §4.

**Numerics** (`numerical`; nothing above is deduced from them).

- **Setup.** Interpreter: the system `python3`, Python 3.14.7, numpy 2.5.2, scipy 1.18.1;
  mpmath 1.4.1 for the note's script. Scripts are in the council scratch directory
  `work/route-t-audit-analysis/`, which is not in the repository.
- **(a) A copy of the note's `check_route_t.py`,** run with `-I`. Seed 20261123. The output is
  byte-identical to the note's `check_route_t.output.txt` (`diff` empty) and ends with "ALL CHECKS
  PASSED".
- **(b) My `audit_checks.py`.** Seed 20261124.
  - **Free-field test of T.3, T.4 and T.6.** H = H_0 with mass m0 and gap γ = m0, Ω = Ω_0,
    X = φ_0(1_{[-1,0]}), A = φ_0(1_{[R,R+1]}). Klein-Gordon locality makes F = G on (-R,R)
    exactly. The proofs of T.3-T.6 use ‖A‖ only through ‖QAΩ‖ and ‖QA^*Ω‖, so ‖AΩ‖ stands in
    for it.
  - **Quadrature.** k ∈ [0, 20000], 40-point Gauss-Legendre on each unit interval.
  - **Runs.** Runs 1 and 2 each had one FAIL, in the test of T.4 at m0 = 1, λ0 = 3, R = 8. Both
    were artifacts of my test, not of the note.
    - Run 1 compared (F̃-G̃)(t)e^{λ0 t}, which multiplies round-off by e^{λ0 t} ≈ e^{20}.
    - Run 2 estimated c at t = 0, where c ≈ 1.5·10⁻¹³ sits at the round-off level.
    - Run 3 estimates c at t = -0.9R and uses the tolerance 10⁻¹³ + 10⁻⁶|c e^{-λ0 t}|.
  - **Run 3 output** (excerpt; all lines PASS, "ALL CHECKS PASSED"):
    ```
    PASS free field m0=1 R=4: F = G on (-R,R) (locality): max |Im F(t)| on 5 points of (-R,R) = 5.53e-15 (tolerance 1e-6); max |F| = 4.29e-03; outside, |Im F(-1.5R)| = 6.13e-02, |Im F(1.3R)| = 4.78e-02
    PASS ... m0=1 lam0=1 R=4: (Ft-Gt)(t) = c e^{-lam0 t} on (-R,R) (T.4): c = -3.537873e-04j; max deviation 5.76e-16
    PASS ... m0=1 lam0=1 R=4: |Ft(0)| <= m~ min(1,Xi(R)) (T.6): |Ft(0)| = 8.2059e-04, m~ = 1.5102e-01, Xi(R) = 6.6339e-01
    PASS ... m0=2 lam0=1 R=6: (T.6) |Ft(0)| = 8.0968e-08, m~ = 6.6732e-02, Xi(R) = 1.2070e-01; (T.4) max deviation 2.46e-16
    PASS ... m0=1 lam0=3 R=8: (T.6) |Ft(0)| = 3.0018e-06, m~ = 7.7750e-02, Xi(R) = 1.5688e-01; (T.4) max deviation 1.99e-16
    PASS ... |c| <= 2 m~ e^{-lam0 R} in all three cases (e.g. 3.538e-04 <= 5.532e-03)
    PASS T.5 at R'=R/2 with |c|<=2m~e^{-lam0R} is <= Xi(R): max of lhs - Xi = -2.690e-45  (gamma in {0.01,0.1,1,5}, lam0 in {1,2,10}, 1200 values of R in [0.05,60])
    PASS floor(d) >= (1+d)/4 for d >= 1: exact rationals, d in [1,10^4] step 1/4 and [1,3] step 1/1000
    PASS shell count <= 6: max indices j per shell [n,n+1) = 6 over 2e4 random configurations
    ```
  - **The shell bound of six is attained,** in some simulated configurations.

## 6. Not done, not verified, not run

**Not done.**

- §§5-7 of the note: Proposition T.17, Remark T.18, Proposition T.19, the readings R1 and R2, and
  the status tables. They belong to the second auditor; I give no verdict on them, except F4 on
  §7.3.
- I did not compare the note's paragraphs on the sketch of 22 November (ll. 461-464 and
  1025-1031) with the sketch itself.

**Not verified.** These record statements were used as the record states them. I read each
statement and checked its hypotheses at the point of use, but did not re-audit the proof.

- Lemma 9.1; Propositions 2.6, 2.7, 8.1 and 8.2.
- Theorem 7.8 and its chain (Lemmas 7.1-7.6, Theorem 7.7, Theorem D.3).
- Lemma D.1. I read D.2's proof against the use made of it, without a full re-audit.
- Lemma C.2 (read); C.4 and C.5.
- Proposition N.15; Lemmas N.20-N.28 (statements read, proofs in part); N.32.
- Simon's Remark itself, which is printed without proof.
- GJS pages: not read by me; not needed for §§1-4.

**Not run.**

- No LaTeX build: not asked of an auditor. The note's own log was inspected.
- No exact or interval arithmetic. No step of §§1-4 is computer-assisted; the numerics only
  corroborate.

## 7. Comparison with the drafter's report (read after my verdicts were written)

`reports/route-t-drafter.md` rates claims 1-15, my part, the way I do.

- **Where I add.**
  - F1 supplies the truncation variant of T.15(ii), which the drafter says it "did not write".
  - §13 of the record, which the drafter left unexamined, uses neither M nor Ψ (section 5).
  - F2, F3 and F4 are not in the drafter's report.
- **The drafter's three least-sure points, as far as my part goes.**
  - (1) The measure theory of T.12 holds.
  - (3) The principal-value step of T.5 holds, with the sign right.
  - (2) T.15(ii) is F1.
- **Not opened.** I did not open the earlier audit reports in `ugjs/council/`. They audit the
  record, not the note.

## 8. Files written

- `reports/route-t-audit-analysis.md`: this report, in the council scratch directory.
- Scratch, in the council scratch directory `work/route-t-audit-analysis/`, which is not in the
  repository: `check_route_t_copy.py`, `check_route_t_copy.output.txt`, `audit_checks.py`,
  `audit_checks.output.txt` (run 3), `audit_checks.run1.output.txt`,
  `audit_checks.run2.output.txt`, and `simon/simon-p184-184.png`, `simon-p185-185.png`,
  `simon-p186-186.png`.
- Nothing under the repository, and nothing in the note's directory.

## 9. Re-check of the revision (23/24 November 2026)

**Object.**

- The revised `ugjs/route_t/route_t.tex`: 1812 lines, 30 pages. Numbers and pages come from its
  `route_t.aux`: T.1-T.19 unchanged, with the new equations (t7) and (t8) on p. 16 (`lem:fkn`,
  T.15, p. 15).
- The drafter's account, `reports/route-t-revision.md`.
- The diff, `reports/route-t-revision.diff`.

**Provenance of the diff.** The drafter's saved copy of the audited draft has 1492 lines. Its
lines 149-150, 582-583, 946-947 and 1002-1004 are word for word the lines I audited and quoted.
`diff -u` between that copy and the revised note reproduces the body of the supplied diff byte
for byte. So the diff is the whole change.

Lines below are those of the revised note. Record lines are those of `part_i/main.tex` at
49f2d23, read in the frozen copy.

### 9.1 Item 1: the new proof of Lemma T.15(ii), audited as a new claim

**Verdict:** holds. Every step was checked as a calculation or as an application of a stated
result, with that result's hypotheses checked at the point of use. One new MINOR finding (R1)
concerns how far "the Remark is not used" reaches.

**Step 1, the bounded formula (ll. 972-997, (t7) and (t8)).**

- [calc] A2's display puts the later time on the left, ⟨f, e^{-TK}h'⟩ with f embedded at T. So
  the multi-time instance with 1, F_1, F_2, 1 at -T < τ < τ' < T is
  ⟨Ω_0, e^{-(T-τ')K}F_2 e^{-(τ'-τ)K}F_1 e^{-(T+τ)K}Ω_0⟩ = ∫J_τF_1 J_{τ'}F_2 e^{-𝒰_{h_{T,g}}}dμ_0,
  which is (t7).
- [calc] F_1 = F_2 = 1 gives Z(h_{T,g}).
- [calc] The factor e^{-2TE(g)} cancels, since (T-τ') + (τ'-τ) + (T+τ) = 2T.
  ⟨Ω_0, e^{-2TH}Ω_0⟩ = ‖ψ_T‖².
- [calc] F_2 is a bounded real multiplication operator and e^{-(T-τ')H} is self-adjoint. So
  ⟨Ω_0, e^{-(T-τ')H}F_2 Y⟩ = ⟨F_2ψ_{T-τ'}, Y⟩. The left side of (t8) is real, which gives the
  second equality of (t8).
- [calc] T ≥ 1 and |τ|, |τ'| ≤ 1/2 put τ and τ' strictly inside (-T, T).

**Item 1(a): is the asymmetric bounded two-time formula covered by A2?**

What I read:

- **A2** (main.tex ll. 825-838). The display is stated "For all bounded time-zero functions
  $f,h'$, $T>0$, and $g\in\CH$". It continues "together with the analogous multi-time formulas
  on finite slabs (used in \S\ref{sec:slab} in the two- and one-time forms ...)".
- **A2's sources line** (ll. 840-841): Simon, Cor. V.14 and Thm. V.15; "equivalently" GRS,
  Thms. II.14 and II.16.
- **Lemma 4.1** (ll. 1725-1736). It is stated "For $T>0$, $t\in[0,2T]$, $s\in[-T,T]$, and
  bounded nonnegative measurable functions $F_1,F_2$ of the time-zero field". Formula (2) has
  two times ∓t/2; formula (3) has one time s anywhere in [-T, T].
- **Simon, printed p. 163** (`audit_2026/evidence/simon-fkn-185.png`): (V.46), Corollary V.14
  and Theorem V.15.
- **Simon, printed p. 164** (PDF page 186, rendered from `refs/`).
  - "where $s_0$ is arbitrary and $s_j=s_{j-1}+t_j$", with
    $G_j^{(F)}=G_j(\phi_F(f_1),\dots,\phi_F(f_k))$.
  - The proof "Suppose first that $G_0,\dots,G_n$ are bounded ... This proves (V.47) in case are
    bounded".
  - The Remark ends "and not only if $G_j^F$ is a function of only finitely many fields".
- **GRS, printed pp. 148-149** (`audit_2026/evidence/grs-fkn-39.png`, `grs-fkn-40.png`).
  - Theorem II.14 (II.32) is the two-time formula for "any vectors $u,v$".
  - Theorem II.16 (II.34), the General Feynman-Kac-Nelson Formula, holds "For
    $t_1\ge0,\dots,t_n\ge0$". At the interior times it has "$G_i$ ... a polynomially bounded
    function from $R^{m_i}\to R$" of finitely many fields; general functions appear only at the
    ends, "$u,v\in L^p(Q_F)$ for some $p>2$".

**Decision.** The formula is A2's printed statement. It is not a consequence the record already
draws, and it is not a new reading.

- **Placement.** Neither A2's words nor its printed sources restrict where the times sit (Simon:
  "$s_0$ is arbitrary"; GRS: t_i ≥ 0). The record itself reads the undisplayed multi-time clause
  for bounded measurable functions at interior times of a slab: at two symmetric times in
  formula (2), at one arbitrary time in formula (3). Two asymmetric times is the same kind of
  instance. It needs no reading that the record does not already make.
- **Not a drawn consequence.** The record states no two-time formula at asymmetric times.
- **The note's account is accurate.** "The record uses these formulas in Lemma 4.1 at the
  symmetric times $\mp t/2$ and, in its formula (3), at one time $s$ placed anywhere in $[-T,T]$.
  A2's wording does not restrict the positions of the times" (ll. 974-976).
- **One qualification, the function class:** finding R1 below.

**Item 1(b): J_τ(X^{[ℓ]}) = (J_τX)^{[ℓ]} (ll. 1002-1007). Holds.**

- [rec] For a cylinder function F = f(φ_0(g_1), ..., φ_0(g_k)), c_ℓ∘F is the cylinder function
  (c_ℓ∘f)(...). J_τ maps it to (c_ℓ∘f)(Φ(τ, g_1), ...) = c_ℓ∘J_τF, by the definition of J_τ on
  cylinder functions (proof of Lemma N.22, main.tex ll. 5274-5283). That proof also shows J_τ is
  well defined, since it preserves laws.
- [calc] For F ∈ L²(dφ_0), take cylinder F_m → F in L². This is the density by which N.22
  extends J_τ.
- [calc] Since |c_ℓ(a) - c_ℓ(b)| ≤ |a-b|, we get ‖c_ℓ∘F_m - c_ℓ∘F‖_2 ≤ ‖F_m - F‖_2 and
  ‖c_ℓ∘J_τF_m - c_ℓ∘J_τF‖_2 ≤ ‖J_τF_m - J_τF‖_2 = ‖F_m - F‖_2, by the L²-isometry.
- [calc] Equal L²-limits give the identity.
- A2's "sharp-time embeddings" J_t and the J_t of N.22 are the same map. The record identifies
  them at Theorem 5.1, Step 1, ll. 1870-1872.

**Item 1(c): the two dominated-convergence steps (ll. 1008-1024). Both hold.**

- **Path side.**
  - [calc] |c_ℓ(y)| ≤ |y| and c_ℓ(y) → y. By (b), the left side of (t8) for F_i = X^{[ℓ]} is
    ∫(J_τX)^{[ℓ]}(J_{τ'}X)^{[ℓ]} dq_{h_{T,g}}.
  - [rec] X ∈ L⁴(dφ_0) by (V.6b) of A1(d), whose hypotheses I checked: n ≥ 1, h bounded with
    compact support, hence in L^{1+ε}; p = 4; the n = 0 term is a constant.
  - [rec] J_τ is an isometry of L⁴ (proof of N.22).
  - [rec] Lemma N.32. Its hypotheses: h_{T,g} ∈ 𝒞_E, which holds by Lemma 3.1(ii) (g ∈ 𝒞_H, and
    [-T,T] is a compact interval); and J_τX ∈ L⁴(dμ_0). It gives J_τX ∈ L²(dq_{h_{T,g}}).
  - [calc] Cauchy-Schwarz makes the majorant |J_τX||J_{τ'}X| integrable.
- **Hilbert side.**
  - [rec] A5(i). Its hypotheses: g ∈ 𝒞_H; b > 0 with b = T+τ, T-τ' ≥ 1/2; and V' = V(h) with
    h ∈ L¹ ∩ L² of compact support. It gives ψ_b = e^{bE}e^{-bK}Ω_0 ∈ Ran e^{-bK} ⊆ D(X).
  - [rec] X is the maximal multiplication operator (A1), so |X|²|ψ_b|² ∈ L¹.
  - [calc] |X^{[ℓ]} - X| ≤ |X|, so dominated convergence gives X^{[ℓ]}ψ_b → Xψ_b. This is the
    computation of Lemma 4.3(ii), whose hypothesis "Whenever $F\psi_a\in\HH$" A5(i) supplies.
  - [calc] e^{-(τ'-τ)H} is bounded, and the inner product is continuous.

**Item 1(d): do the stated conditions match the proof? They match. The inventories have small
gaps (finding R2).**

- The proof of T.15 now uses A2 (bounded, multi-time), A1(d), A3 (in (iii)), A5(i), N.22,
  N.32, Lemma 3.1(ii), Lemma 4.4, the computation of Lemma 4.3(ii), and T.13.
- The places that state conditions name exactly this, with no Simon Remark: the Summary
  (ll. 90-93), the status after T.2 (ll. 262-269), the paragraph on the role of the cutoff
  (ll. 1064-1068), the §7.1 rows for T.2, T.15 and T.16 (ll. 1653-1657, 1675-1678), and §7.2
  (ll. 1698-1699).
- T.16 is "conditional as T.14", which is right.

**Numerics** (`numerical` only; they prove nothing).

- My `recheck_t8.py` tests (t8) in a one-mode interacting model, with seed 20261124.
  - Setup: H = N + V, where V(q) = 0.8q/(1+q²) + 0.4cos 2q, F_1 = tanh 2q + 0.2, F_2 = 1/(1+q²),
    T = 1.5, τ = -0.3, τ' = 0.45.
  - Hamiltonian side: diagonalization in the Hermite basis. Path side: 4·10⁶ exact
    Ornstein-Uhlenbeck paths, dt = 0.0025.
  - Result: path side -0.086983 ± 0.000283; (t8) gives -0.086852, which is 0.46 standard errors
    away. The swapped ordering gives -0.081695, 18.7 standard errors away.
  - The Hamiltonian side is converged: -0.086851813578, -0.086851813638 and -0.086851813638 at
    basis sizes 60, 90 and 120.
- A copy of the revised `check_route_t.py`, rerun, gives output byte-identical to the note's:
  23 PASS, "ALL CHECKS PASSED".

### 9.2 Item 2: my findings F2, F3, F4

- **F2: closed.** T.9, Step 3, ll. 610-615, now reads "$y\le a_O-d$ and $y'\ge b_O+d$ ... would
  give $y'-y\ge b_O-a_O+2d>2$, contradicting $B_j\subseteq[j-1,j+1]$".
- **F3: closed.** Definition T.1, ll. 170-172, now reads "because $H(g)$ is self-adjoint and
  $|\lambda_0-iE|\ge\lambda_0$ for real $E$".
- **F4: closed.**
  - The "Coordinates" paragraph (ll. 255-260) agrees with Remark 3.3(1) (main.tex ll. 1619,
    1660-1669, 1698-1701): s = m_0/M_*. The transported bound uses only the inequality of
    item (1) in the working model, at sO and sd. So d ↦ Ψ̃_{m_{1,*},λ0}(sd), with λ0 in working
    units, is the rate in the original coordinates.
  - The §7.3 list (l. 1729 ff.) now contains every site I named. I spot-checked the record lines
    251, 257, 280, 1656-1657, 3083-3099 and 3290-3291 that are quoted there; all match.

### 9.3 Item 3: the other hunks in §§1-4

Each holds, and nothing is broken.

- **The Summary's first sentence (ll. 90-93):** "Route T adds no input to the record's
  imports". This is true relative to A2 as the record states and reads it; R1 adds a precision.
- **§1.1 (ll. 129-138).**
  - The images `gjs-proof118-17.png`, `gjs-thm41-45.png` and `gjs-uniform-46.png` exist.
  - The PDF page indices 7, 17, 45 and 46 for pp. 590, 600, 628 and 629 follow the
    printed-minus-583 rule of pp. 593-597 ↔ 10-14.
  - "read ... on 23 November 2026" is a dated statement about reading, not about a push.
- **Definition T.1** (F3), **the Coordinates paragraph and the status of T.2** (F4, F1), **T.9
  Step 3** (F2), **T.15(ii)** (section 9.1), and **the paragraph on the role of the cutoff**
  (ll. 1058-1068).
  - The role paragraph is accurate: "The record's Lemma 4.1 states the two-time formula only at
    the symmetric times $\mp t/2$, and its one-time formula (3) at any time $s$".
- **§4(c) (ll. 1118-1141).**
  - The new quotation of main.tex ll. 3104-3106 is exact.
  - The conclusion that (M_2) reaches items (1)-(2) only through Theorem 11.1, which is
    re-proved, holds.
- **Nothing broken.**
  - The statement of T.2 is untouched: no hunk falls in its environment.
  - The constants are unchanged.
  - `route_t.log` has 0 lines matching `^!`, 0 Overfull and 0 undefined.
  - `pdftotext | grep -nE '\?\?|TODO|Hmm|wait,'` prints nothing.
  - All labels resolve.
  - The §7.2 paragraph on §13, which takes over my result, cites ll. 3207-3221, 3225, 3227 and
    3234. I checked all four; they are correct.

### 9.4 Item 4: the first page, as far as my audit goes

The "Status of this note" paragraph (ll. 63-72) says the note was "Audited on the same day by
two independent agents ... the re-check of this revision is appended there) and revised for their
findings, none CRITICAL or MAJOR". For my audit this is accurate:

- I audited it on 23 November 2026.
- I wrote nothing of the note, and I read the drafter's report only after my verdicts.
- My four findings were MINOR, and all four are applied.
- This re-check is the appended part.

Two remarks:

- The path `ugjs/council/route-t-audit-analysis.md` is a forward reference. It becomes true when
  the orchestrator archives this report under that name.
- The source comment at l. 3 still says "Draft for an independent audit" (R3).

### 9.5 New findings

**R1 (MINOR): what "Simon's Remark is not used" covers.**

- **Locator.** T.15(ii), Step 1 (ll. 976-979) and ll. 1025-1027; the §7.1 row T.15 (l. 1677).
- **Quotation.** "Simon's Remark on p.~164 ... would give (ii) directly; the proof above does not
  use it."
- **Reason.**
  - (t7) is applied to F_1 = F_2 = X^{[ℓ]}, which is not a function of finitely many fields.
  - A2 covers this, as the record states it ("For all bounded time-zero functions") and reads it
    (Lemma 4.1 is stated for bounded measurable functions at interior times).
  - But the multi-time theorems A2 cites print the interior functions as functions of finitely
    many fields: Simon V.15, and GRS II.16, which admits general L^p functions only at the two
    ends. For other functions at interior times, Simon's printed text has only the Remark
    itself, without proof.
  - So the Remark is no longer invoked, but at this instance it is still the printed basis of
    A2's function class. My F1 repair proposed this very step and missed the point. It predates
    Route T: the record's Lemma 4.1 makes the same extension. Route T adds nothing to it, and
    "adds no input" stands.
- **Repair** (about five lines; it is a new claim, so I checked it).
  1. Let |F_i| ≤ C. Choose bounded cylinder functions F_i^{(m)} with |F_i^{(m)}| ≤ C and
     F_i^{(m)} → F_i in L²(dφ_0). Use the density of N.22 and clip at C, which keeps both
     properties.
  2. (t7) holds for F_i^{(m)} by the bounded case of V.15, a printed statement with a printed
     proof: n = 3, G_0 = G_3 = 1, t_j > 0.
  3. The left side converges. With y = e^{-(T+τ)K}Ω_0, (F_1^{(m)} - F_1)y → 0 by dominated
     convergence along a.e.-convergent subsequences (dominator 4C²|y|²). Then
     F_2^{(m)}z_m - F_2z = F_2^{(m)}(z_m - z) + (F_2^{(m)} - F_2)z → 0, and the semigroup is
     bounded.
  4. The right side converges. By (b), |J_τF_i| ≤ C, and
     ‖J_τF_1^{(m)}J_{τ'}F_2^{(m)} - J_τF_1J_{τ'}F_2‖_2 ≤ C(‖F_1^{(m)} - F_1‖_2 +
     ‖F_2^{(m)} - F_2‖_2). Moreover e^{-𝒰_{h_{T,g}}} ∈ L²(dμ_0) by A3.
  5. T.15(ii) then rests on V.15 as printed, with A3 and N.22, and the Remark is used nowhere.

  The same sentence would serve the record's Lemma 4.1.

**R2 (MINOR): the inventories.**

- **Locator.** §7.1, row T.15 (ll. 1675-1677) and row T.2 (ll. 1653-1657).
- **Reason.**
  - The T.15 row omits A1(d) (V.6b), used for X ∈ L⁴. It also omits the proof of Lemma N.22,
    used for J_τ on cylinder functions, its density extension and its L⁴-isometry.
  - The T.2 row cites "§4(c) and the status line of Theorem T.14". These omit Lemma 3.1, Lemma
    4.4 and the computation of Lemma 4.3(ii). Those are listed only in the rows of T.8-T.10 and
    T.15.
  - The status paragraph after T.2 (l. 267: "listed in §7", that is, all rows) covers everything.
    So the conditions are complete, but the row inventories are not.
- **Repair.** Add A1(d) and N.22 to the T.15 row. Let the T.2 row read "listed in §4(c) and in
  the rows of this table".

**R3 (MINOR): a stale source comment.**

- **Locator.** l. 3.
- **Quotation.** "% Draft for an independent audit; not integrated into the record."
- **Reason.** The note is now "revised after two independent audits" (l. 57).
- **Repair.** Update the comment.

### 9.6 Checks run, not done, files written

**Checks run** (all reported above).

- The provenance of the diff, verified by spot lines and by regenerating it.
- Record passages re-read: A2 with its sources, scope and dossier (ll. 825-853); Lemma 4.1
  (ll. 1725-1748); ll. 3104-3106; Remark 3.3 (ll. 1656-1657); ll. 3083-3099; 251, 257, 280;
  3290-3291; §13 (ll. 3205-3236); N.22 (ll. 5274-5283).
- Sources read: Simon pp. 163-164 and GRS pp. 148-149, on images or renders.
- The build-log greps and the label table.
- The revised script, rerun.
- `recheck_t8.py`, with its basis-size check.

**Not done.**

- The hunks of §§5-7 outside my part (the sources auditor's).
- GRS beyond pp. 148-149.
- The first page's last sentence, about the pages of the 23 November record.

**Not run.** No LaTeX build; I inspected the note's own log.

**Files written.**

- This section, appended to `reports/route-t-audit-analysis.md`.
- Scratch, in `work/route-t-audit-analysis/`, not in the repository: `recheck_t8.py`,
  `recheck_t8.output.txt`, `recheck_t8_basis.output.txt`, `check_route_t_revised_copy.py` with
  its output, and `regen.diff`, `given.body`, `regen.body`.
- A stray empty scratch file outside the council directory was created by a shell-redirect slip
  and deleted at once.

**Final line.** As far as my part goes, Theorem T.2 is **proved, conditional on exactly** these
four conditions:

1. A1-A8 of the record, with A8(iv) used only in the cases P1-P4 and A8(iv)-T not used, and with
   A2's multi-time clause used for bounded measurable functions at two asymmetric interior times
   of the slab [-T, T]. This is the reading the record already makes in Lemma 4.1; its printed
   basis for functions not of finitely many fields is Simon's Remark, removable by R1's repair.
2. The readings the record declares: A1, A3 and A6 Scope, and A8 Scope (d) including the type
   (1.1.6), r = 2 pieces. The open items of `part_i/C5_reading_record.md` come with them.
3. The record's statements, used as the record states them: those of §4(c), of T.14's status
   line, and of the §7.1 rows, including Lemmas 3.1, 4.4, N.22 and N.32.
4. Nothing else. In particular, Simon's Remark is no longer a condition of the note's own
   argument.

## 10. Confirmation of the second round (24 November 2026)

**Object.**

- The note `ugjs/route_t/route_t.tex`: 1916 lines, 33 pages. Lines and pages below are those of
  this version; statement and equation numbers come from its `route_t.aux`.
- The drafter's account: the section "Second round" of `reports/route-t-revision.md`.
- The diff: `reports/route-t-revision2.diff`, 362 lines.
- The sources auditor's points F13-F18: section "Re-check of the revision" of
  `reports/route-t-audit-sources.md`.

**Provenance.**

- The drafter's saved copy `route_t.rechecked.tex` is exactly the version I re-checked in §9: its
  `diff -u` from the audited draft reproduces the first-round diff byte for byte.
- `diff -u` from that copy to the current note reproduces `route-t-revision2.diff` byte for byte.
  So I read every hunk of the round.
- The checks ran between 23:48 on 23 November and 00:02 on 24 November 2026.

**Overall verdict.**

- Every hunk holds, and nothing is broken.
- There are three new points, none CRITICAL or MAJOR:
  - C1 (MINOR) on Simon's class F;
  - C2 (MINOR) on the record of 23 November;
  - C3 (cosmetic).

### 10.1 Item 1: Steps 0 and 1 of Lemma T.15(ii) (ll. 987-1070)

**Verdict: holds.** The wording about Simon's class F understates what is printed (C1).

**Step 0 (ll. 987-994).** The identity J_τ(c_ℓ∘F) = c_ℓ∘J_τF is checked as in §9.1(b). Its new
consequence holds: if |F| ≤ C then F = c_C∘F, hence J_τF = c_C∘J_τF and |J_τF| ≤ C almost
everywhere.

**Step 1, preamble (ll. 1003-1016).**

- The A2 paragraph is the one I accepted in §9.1(a).
- The two Simon quotations are verbatim, checked on the renders of p. 163 (`simon-fkn-185.png`)
  and p. 164 (PDF page 186): "measurable functions on $R^k$ with $|G_j(x)|\le C(1+|x|^N)$", and
  "Suppose first that $G_0,\dots,G_n$ are bounded ... This proves (V.47) in case are bounded".
  The latter is a misprint in the source, quoted without [sic] (C3).
- "GRS's Theorem II.16 likewise" is right (`grs-fkn-40.png`): its interior G_i are polynomially
  bounded functions of finitely many fields.

**Item (1), approximants (ll. 1018-1025).**

- The density claim holds on the page A1(c) cites. Simon p. 16 (`simon-gamman-038.png`) prints
  "Let Γ(H) denote the space L²(M, dμ)", the Γ_n(H) as "the closed subspaces generated by
  {:φ(f_1)...φ(f_n): | f_i ∈ H}", and "(I.25) Γ(H) = ⊕_{n=0}^∞ Γ_n(H)".
- S(ℝ) is dense in H_C by the definition of H_C (A1, "completing the real-valued S(R)").
- A Wick monomial depends continuously on its arguments, so Wick monomials with real Schwartz
  arguments are L²-dense. They are polynomials in finitely many fields.
- One detail: c_C∘P needs a real P. A real F_i is approximated at least as well by the real part
  of a complex polynomial (C3).
- The estimate ‖c_C∘P_{i,m} - F_i‖_2 = ‖c_C∘P_{i,m} - c_C∘F_i‖_2 ≤ ‖P_{i,m} - F_i‖_2 holds.

**Item (2), (t7) for the approximants (ll. 1026-1038).** The hypotheses of Theorem V.15, checked
at the point of use:

- n = 3; s_0 = -T; t_1 = T+τ, t_2 = τ'-τ, t_3 = T-τ', all > 0 because -T < τ < τ' < T. Then
  s_1 = τ, s_2 = τ', s_3 = T.
- One list f_1, ..., f_k carries all G_j, as V.15 requires ("Let f_1, ..., f_k ∈ F. Let
  G_0, ..., G_n be measurable functions on R^k").
- G_0 = G_3 = 1; G_1 and G_2 are c_C∘p for polynomials p, so they are bounded and continuous.
  |G_j| ≤ C(1+|x|^N) holds with N = 0 (with the constant 2C, say).
- g ∈ 𝒞_H is ≥ 0, bounded and of compact support, so g ∈ L¹ ∩ L^{1+ε}.
- The dictionary is that of A2 and the declared readings: Simon's H = H_0 + H_I(g) is K(g), his
  U(g⊗(s_0,s_3)) is 𝒰_{h_{T,g}}, his J_s is the J_s of N.22 (G_j^{s_j} = J_{s_j}G_j^{(F)},
  p. 164), and his φ_F is φ_0.

**The complex conjugation** [calc]. V.15's left side is ⟨Ω_0, A Ω_0⟩ with
A = e^{-(T+τ)K}F_1 e^{-(τ'-τ)K}F_2 e^{-(T-τ')K}. All factors are self-adjoint, so
A* = e^{-(T-τ')K}F_2 e^{-(τ'-τ)K}F_1 e^{-(T+τ)K}, which is the operator of (t7). Hence (t7)'s
left side is the complex conjugate of V.15's left side, and the right side ∫J_τF_1 J_{τ'}F_2 e^{-𝒰}
dμ_0 is real. The conjugation is right.

**Simon's class F.** The printed text supports more than the note says (C1).

- p. 78 (PDF 100, `simon-freefield-100.png`), Theorem II.17: "Let $F_{m_0}$ be the Hilbert space
  of all real distributions on R whose Fourier transforms are functions with the property that
  the norm: $\|f\|_F^2=\int|\hat f(k)|^2dk/\sqrt{k^2+m_0^2}$ (II.46) is finite".
- p. 85 (PDF 107, rendered from `refs/`): "Throughout this section we fix a bare mass, m."
- p. 86 (PDF 108): "we first study the connections between the indexing spaces F and N", and
  Proposition III.2, "Let f ∈ F ... $\|j_\sigma f\|_N=\|f\|_F$".
- p. 89 (PDF 111, `simon-free-fkn-111.png`), Theorem III.6, the free-field FKN formula: "Let
  $f_1,\dots,f_n$ be elements of F". Its G_j^F ≡ G_j(φ_F(f_1), ..., φ_F(f_n)) is the same
  notation as V.15.
- p. 146 (PDF 168): "Let $H_0$ be the Hamiltonian for the free field $\phi_F$ on
  $\mathfrak F=\Gamma(F_{m_0})$".

So V.15's F is Simon's indexing space of the time-zero field φ_F, the space F_{m_0} of (II.46).
Real Schwartz functions belong to it by that definition. The record already proves F_{m_0} = H_C
(A1, Scope, ll. 791-797). The only reading involved is the identification of φ_F with φ_0, which
A1's Scope declares. The note's sentence calls this a "reading under which A2 cites Theorem V.15"
and implies that F is undefined.

**Items (3)-(5) (ll. 1039-1057).**

- The Hilbert side holds: dominated convergence along subsequences with dominator 4C²|y|², the
  bounded semigroup, and the split F_2^{(m)}z_m - F_2z = F_2^{(m)}(z_m - z) + (F_2^{(m)} - F_2)z.
- The path side holds. J_τ is an L²-isometry (N.22), and |J_sF| ≤ C by Step 0, so
  ‖ab - a'b'‖_2 ≤ C(‖F_1^{(m)} - F_1‖_2 + ‖F_2^{(m)} - F_2‖_2). Also e^{-𝒰} ∈ L² by A3 (ρ = 2),
  and Cauchy-Schwarz applies.
- The F_i ≡ 1 case is V.15 itself.
- The closing sentence (l. 1059: "rests on Theorem V.15 as printed, on A1(c), A3 and Lemma N.22,
  and on A2's dictionary") and the sentence on the Remark (ll. 1094-1096: "uses it nowhere,
  neither for $V(h)$ nor for the bounded truncations") are true.
- R1 is closed.

### 10.2 Item 2: F15 as applied (§5.4, "Translations", ll. 1381-1408; §5.5, item 3, ll. 1640-1644)

**Verdict: holds.** One notational point goes to C3.

**The identity and its source.** The proof of Lemma N.13(iii) (main.tex l. 4771) prints
"$\Phi_\kappa(z)\circ T_a=\Phi(\tau_a\tau_z\delta_\kappa)=\Phi_\kappa(z+a)$". At ll. 4772-4773 it
prints that c_κ "does not depend on $z$". N.13(i) (l. 4744) prints that "$F\mapsto F\circ T_a$ is
an isometry of every $L^p(\dmu)$". [calc] Substituting x_i ↦ x_i + a in the regularized integral
gives the monomial with kernel w(·-a), pointwise. N.28(a) gives the limits, and the isometry makes
them agree almost everywhere. The paragraph is right. For non-integer a, the translated kernel is
re-split over lattice squares, which is exactly the norm question the item then treats.

**The bound.** (n+n')!/(n!n'!) = C(n+n', n) ≤ 2^{n+n'} ≤ 2^{4p'}, since n, n' ≤ 2p'. I checked this
in exact integers for p' ≤ 20 (`numerical`; for example 6 ≤ 16, 70 ≤ 256, 924 ≤ 4096 at
n = n' = 2p').

**When it arises:** only in P4, and only for pieces with |k - k'| = 1.

- For k = k', both factors already share a square, and a translation can only split them.
- For |k - k'| = 2, the rotated times differ by more than 1.
- For |k - k'| = 1, only two-time slices whose rotated times are less than 1 apart can merge, and
  only under a non-integer translation. The printed proof's translation of a strip bounded by
  lattice lines (half-integers) is of that kind.
- "Raise no question in P1-P3" is right. In P3 both factors start in row 0, so a translation can
  only split them, which lowers the weight because n!n'! ≤ (n+n')!.

**The integer alternative.** An integer translation sending the strip's near edge to x⁰ = -1/2
keeps A at times ≤ 0 and preserves the lattice and every norm. It loses half a unit of the
separation T in (1.1.16), a factor e^{γ/2} ≤ e^{γ}. So "at most one unit ... a factor at most
e^{γ}" is a true upper bound. This γ is GJS's γ of (1.1.16), quoted at l. 1250, namely
γ = m_0(1-ε) in the proof of Theorem 1.1.7. It is not the gap constant γ of (G_γ) that §1.1
fixes (C3).

### 10.3 Item 3: F13, F14, F16, F17, F18, R2, R3

- **F13: applied and true.** The new §7.3 item (l. 1831) cites main.tex ll. 835-838 ("used in §4
  in the two- and one-time forms") and l. 848 (A2's "Used in"); both are verified.
- **F14: applied and true.**
  - The T.17 status (ll. 1439-1441) and its §7.1 row now except "the reach of P4's degree-$0$
    pieces" and list it as conditional.
  - This matches T.17(c): "(for P4, granted the rotation presupposition)". The other assertions on
    R2 are unconditional; the proof states this for P4 ("not reached on R2 either way").
- **F16:** item 4 below.
- **F17: applied and true.** §4(c) (ll. 1192-1195) now lists T.15's inputs (Lemmas 3.1(ii), 4.4,
  N.22, N.32; Lemma 4.3(ii)'s computation; A1(c), A1(d), A2, A3, A5(i)). The T.2 row (l. 1747) cites
  "§4(c) and the rows of this table", and the rows cover Lemma 3.1(iii) (rows T.8-T.10).
- **F18: applied.**
  - The degree-0 sentence (ll. 1541-1545) is now right. Q̄_{0,n',k,k'} = (λa_0∫h'_k)V̄_{n',k'} and
    U are both time-integrated with one factor, so slicing both gives one-time slices, and
    Steps 1-4 apply.
  - "The commission" is now defined (ll. 150-153). Its content (items (a)-(d), the three
    categories) I cannot verify: I have not seen the commission text. The council brief says the
    author "has authorised" the note.
- **R1: closed** (§10.1).
- **R2: closed.** The T.15 row (l. 1765 ff.) adds A1(c), A1(d) and N.22, with what N.22 supplies.
  The T.2 row is as above.
- **R3: closed.** The header (ll. 2-4): "Audited by two independent agents and re-checked on
  23 November 2026; revised for their findings. Not integrated into the record."

### 10.4 Item 4: the first page (ll. 55-82), sentence by sentence

**1. Title block (ll. 57-59):** "Written by an AI agent (Claude), commissioned by the author and
supervised by the council's orchestrator (an AI agent) ... revised after two independent audits and
their re-checks". True as far as I can check.

- The council brief says the author "has authorised" this work and that "The orchestrator
  supervises". "Commissioned" is the note's word for "authorised"; the orchestrator should confirm
  it.
- The re-checks' points were applied in this round.

**2. "Authorship" item (ll. 67-70):** the same, and true.

**3. "Audits" item (ll. 71-75).** True, given the archiving at the two named paths.

- My audit and my re-check were both made on 23 November 2026. So were the sources auditor's,
  by their report.
- No finding in either report is CRITICAL or MAJOR, nor in this confirmation.
- The note was revised for the audits, and the re-checks' MINOR points were applied.
- Not said: this confirmation, whose points C1-C3 will not be applied if it is the last check
  before archiving. The sentence stays true. A reader may still assume that every audit point
  was applied.
- Optional addition: "A confirmation of the last round is appended to the analysis report; its
  points are listed there."

**4. "Not read by a human" (l. 76).** I cannot verify this. It is consistent with the brief.

**5. "Not integrated" (ll. 77-78):** "This note changes nothing in the record: it is not
integrated, and Theorem 12.2 of part_i/main.tex is stated and proved there as before". True as
"unchanged by this note".

- In REPO's working tree (`main.tex` of 23:21), items (1)-(5) and the proof of Theorem 12.2 are
  as at 49f2d23 (diff of the block).
- One sentence of its imports paragraph, inside the theorem environment, has been reworded there
  by another editor. It now reads "contain the unevaluated constant $S_2(B_{3\times5})$ of
  Definition~\ref{aux:notation-S2def}, finite by Theorem~\ref{thm:stability}" (see C2).

**6. "Which record" (ll. 79-81):** "The record of 23 November 2026 (127 pages) has the same
statement numbers as 49f2d23, and different pages". True as of now.

- REPO's `main.pdf` (23:21) has 127 pages.
- REPO's `main.aux` has the same 238 labels, none renumbered and 199 on different pages (for
  example `thm:MAIN` 12.2 is on p. 41 at 49f2d23 and on p. 42 now).
- The orchestrator should re-check this sentence if REPO is rebuilt before the commit.
- The record of 23 November also differs in text where the note's claims reach (C2).

### 10.5 Item 5: did the round break anything?

No.

- `route_t.log` has 0 lines matching `^!`, 0 Overfull, 0 undefined, and no rerun warning.
- `pdftotext | grep -nE '\?\?|TODO|Hmm|wait,'` prints nothing.
- 33 pages; no machine paths in the note, the script or the diff.
- `route_t.aux` has T.1-T.19 and (t1)-(t8). For example `lem:fkn` is T.15, p. 15; (t7) is on
  p. 16; (t8) is on p. 17.
- The theorem environment of T.2 is byte-identical to the re-checked version.
- The §7.1 status table changed only in the rows T.2, T.15 and T.17, as described. Each row
  matches its proof.
- The note's `check_route_t.output.txt` is byte-identical to my rerun of §9 (23 PASS).

### 10.6 New findings

**C1 (MINOR): Simon's class F is printed, not a reading.**

- **Locator.** T.15(ii), Step 1, item (2), ll. 1036-1038.
- **Quotation.** "That the real Schwartz functions belong to Simon's class $F$ (``Let
  $f_1,\dots,f_k\in F$'', p.~163, where $F$ is not restated) is the reading under which A2 cites
  Theorem~V.15 for the record's time-zero fields."
- **Reason.**
  - F is not restated on pp. 163-164, but Simon's notation fixes it. It is the indexing space of
    the time-zero field φ_F: p. 85 (mass fixed), p. 86 ("the indexing spaces F and N";
    Proposition III.2), p. 89 (Theorem III.6, "Let $f_1,\dots,f_n$ be elements of F"), and p. 146
    ("the free field $\phi_F$ on $\mathfrak F=\Gamma(F_{m_0})$").
  - That space is F_{m_0} of (II.46), p. 78, the "real distributions on R whose Fourier transforms
    are functions" with finite norm, which contains the real Schwartz functions.
  - The record proves F_{m_0} = H_C (A1, Scope, ll. 791-797). Only φ_F ↔ φ_0 is a declared reading.
  - The sentence understates the printed basis. Correctness is unaffected.
- **Repair.** "Simon's $F$ (p.~163) is his indexing space of the time-zero field $\phi_F$
  (pp.~85--86, 89, 146), the space $F_{m_0}$ of (II.46), p.~78, which contains the real Schwartz
  functions and which A1's Scope identifies with $\HH_C$."

**C2 (MINOR): the record of 23 November differs in text where the note's claims reach.**

- **Locator.** First page, "Which record" (ll. 79-81) and "Not integrated" (ll. 77-78); T.2(b);
  §4(b) on Corollary 12.3.
- **Reason.**
  - In REPO's working tree, Corollary 12.3 has a restricted statement. Its title now ends
    "..., for cutoffs $0\le g\le1$". Its text begins "Let $\mathscr P(\xi)=\xi^4$, and let the
    cutoff $g$ of \cite[(2.3)]{GJ3} be chosen in $\G$". Theorem 12.2's imports paragraph is
    reworded in one sentence.
  - The first page says only that numbers agree and pages differ.
  - T.2(b) claims "Corollary 12.3" at 49f2d23. REPO's restricted Corollary 12.3 is still proved
    from Theorem 12.2(1) in the form "$\le\Psi_{m_1}(2n-R)\longrightarrow0$" (with Lemma 2.8 and
    Proposition E.5(T)). So T.2(b)'s argument applies to both versions. Correctness is unaffected.
- **Repair.** Add to "Which record": "Its text differs in places; in particular Corollary 12.3 is
  restricted to $\mathscr P(\xi)=\xi^4$ and $0\le g\le1$, and the argument of Theorem T.2(b) for
  it applies to that version as well."

**C3 (cosmetic).**

- **[sic] for the source's misprint.** l. 1015, "This proves (V.47) in case are bounded", lacks the
  [sic] mark that the record uses for misprints. My own §9 quotation lacks it too.
- **Real polynomials.** l. 1018 or l. 1022: write "real polynomials", since c_C∘P needs a real P.
- **The symbol γ.** l. 1406 and l. 1643: the "e^{γ}" factor uses GJS's γ of (1.1.16), but §1.1
  reserves γ for the gap constant of (G_γ). Write it as GJS's γ = m_0(1-ε) of (1.1.16).

### 10.7 Checks run, not done, files

**Checks run** (all reported above).

- The provenance of both diffs.
- Every hunk read in the note.
- Record passages, at 49f2d23 in the frozen copy: A2 (ll. 825-853); N.13 (ll. 4738-4792); A1,
  Scope (ll. 791-797).
- REPO, read-only: `main.pdf`, `main.aux` and the Theorem 12.2 / Corollary 12.3 block of
  `main.tex`.
- Simon pp. 16, 78, 85, 86, 89, 146, 163 and 164, and GRS p. 149, on page images or on renders
  from `refs/`. A per-page text layer of Simon was used only to locate pages.
- The build artifacts and the label table.
- The exact binomial check, and the comparison of the script output.

**Not done.**

- The commission text (F18), which I have not seen.
- "Not read by a human".

**Not run.**

- No LaTeX build.
- No new numerical test of (t7): the approximation is a limit argument. My §9 test of (t8) in an
  interacting toy stands.

**Files written.**

- This section.
- Scratch, in `work/route-t-audit-analysis/`, not in the repository: `simon/simon_pages.txt` (the
  text layer); `simon/simon-p-107.png`, `simon-p-108.png`, `simon-p-168.png`; `round2_regen.body`,
  `round2_given.body` and `rc_vs_audited.body`; `repo_lab.txt`, an abandoned label extraction
  whose regex failed on nested braces. The comparison was redone in Python, which wrote nothing,
  and the companion file was never created because of a path slip.

**Final line.** As far as my part goes, Theorem T.2 is **proved, conditional on exactly** these
four conditions:

1. A1-A8 of the record, with A8(iv) used only in the cases P1-P4 and A8(iv)-T not used. A2 is used
   for bounded measurable functions at two asymmetric interior times of [-T, T]. That use is now
   also derived from the bounded case of Simon's Theorem V.15, printed with its proof
   (pp. 163-164), together with A1(c), A3 and Lemma N.22. So Simon's Remark on p. 164 is used
   nowhere.
2. The readings the record declares: A1, A3 and A6 Scope, among them the identification of
   Simon's φ_F and H_0 + H_I(g) with the record's φ_0 and K(g); and A8 Scope (d), including the
   type (1.1.6), r = 2 pieces. The open items of `part_i/C5_reading_record.md` come with them.
3. The record's statements, used as the record states them: those listed in §4(c) and in the rows
   of §7.1.
4. Nothing else.
