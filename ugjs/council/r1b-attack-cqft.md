# R1b: attack on the comparison route (mp's Route M, aqft's Route L), by `cqft`, 30 October 2026

Read this session: `memo-mp.md` §§A-C; `memo-aqft.md` §§A-C; `main.tex` ll. 884-899 (standing
assumption), Prop. 3.2, Appendix C (Lemmas C.2-C.4, Thm C.5). On the images, earlier in this session:
GJS pp. 588-632; Erice I pp. 160-163.

## Verdict: REPAIRABLE GAP, not fatal. No error found in the route's own steps.

The route is GJS's own device. In the proof of (1.1.11) (p. 595) the reference cutoff agrees with h
near the observable, so every difference square is strip-separated from it. My R1 verdict on O3
("confirmed, no loophole found") was wrong: I examined only paths g → g' whose difference region meets
the observable's neighbourhood. I withdraw it. The gap below concerns how far the import reaches, not
the logic. Its repair costs one paragraph.

## The checks

**(i) The pair (sharp-time Q_V piece, time-integrated one-square piece U_Δ).**
- Theorem 1.1.7 (p. 594) is stated for "two localized monomials Q_1 and Q_2". Page 593 calls both
  (1.1.5) Q(x_0) and (1.1.6) Q = ∫dx_0 Q(x_0) "localized" when w is supported in a product of squares,
  and gives a norm for each, (1.1.7)/(1.1.8). So the statement covers mixed pairs on its face.
- U_Δ = λΣ_n a_n ∫ h1_Δ :Φ^n: is a sum of (1.1.6) monomials with r = 1 and n ≤ 2p' < n̄. Its norm is
  at most λ|a_n| K_1 K_2^{2n} n!, since ||h1_Δ||_{L²(R²)} ≤ 1. The n = 0 term is constant and has zero
  covariance.
- The slicing fallback (U_Δ = ∫dx^0 U_Δ(x^0), CE2 applied slice by slice, ∫dx^0 ||w(x^0,·)||_2 ≤ ||w||_2
  over a unit interval) also works. It is the sharp/sharp reading Lemma 7.4 uses.
- Precedent: in (1.1.11)-(1.1.12) GJS apply 1.1.7 to Q = ∏Φ(f_i), f_i ∈ C_0^∞(O), paired with V(g_i),
  for squares in every direction from O. Both members there are *time-integrated*. **There is no
  printed precedent with a sharp-time member** (next item).

**(ii) Strip geometry and summation. This is where the gap lies.**
- The bookkeeping is correct. A square at sup-index distance m ≥ 2 from the core rectangle is
  separated by an axis-parallel strip of width ≥ m − 1, horizontal or vertical according to the
  dominant offset. Then Σ_Δ e^{−m_1 d_Δ} over all squares outside B is finite and independent of T, g
  and the translation (aqft's Σ_{a,b}, mp's S_*).
- Two small corrections. aqft writes e^{−m_1 dist}, but (1.1.10)'s exponent is the strip width d, so
  the bound must use d ≥ m − 1, which their Σ_{a,b} already does. B must be built from GJS squares
  "centered at the lattice site" (p. 593), not from the record's [j, j+1) (my F4).
- **The gap.** g-uniformity needs the squares of rows −1, 0, 1 that lie far out in space. These are
  separated from the time-0 observable only by *vertical* strips, and horizontal strips alone give a
  row sum proportional to |supp g|. So the route uses CE2 for a **sharp-time** Q_1 across a
  **vertical** strip.
  - The printed statement covers this case. Its d is "the width of the widest strip bounded by two
    parallel lines", with no orientation, and Source Fact 2.2 says "(any orientation)".
  - The printed proof does not reach it. It runs "After rotating and translating the strip ...
    choosing A = Q_1, B_T = Q_2 in Theorem 1.1.11" (p. 597), and Theorem 1.1.11 takes A, B "of type
    (1.1.5)" (p. 596). Rotation by 90° turns a sharp-time monomial into one at fixed spatial
    position, extended in the new time. That is neither (1.1.5) (no sharp new-time) nor (1.1.6) (its
    kernel is not in L²(R^{2r})).
  - GJS never use this case on the pages I read. The record has not used it either: Lemma 7.4 needs
    only horizontal strips.
  - Erice I Theorem 2.2.1 (pp. 160-161) asserts clustering "uniformly in h" with d = dist(supp A,
    supp B), and its (2.2.3) allows δ_s(t)f(x). That is a second printed *assertion* of the case, with
    its proof deferred to [GlJaSp 1, 2] (p. 193).
- *Repair (one paragraph).* State in the import paragraph that the g-uniform bound uses the
  vertical-strip, sharp-time case of the printed statement of Theorem 1.1.7. Under the record's
  standard this is literal, but its printed proof covers it only through a rotation that leaves
  (1.1.5)-(1.1.6). Any later trace must include that case. Without this sentence, "imports nothing new"
  overstates the position.

**(iii) The base term.**
- Bound: |⟨Q_V⟩_{h1_B}| ≤ ||Q_V||_{L²(dμ_0)} ||e^{−U_{h1_B}}||_{L²(dμ_0)} / Z(h1_B).
- Q_V is a function of the sharp-time field. Φ(τ, f) is defined on path space (p. 589), and its time-0
  marginal is the Fock measure (conventions lock, Remark 2.5). So
  ||Q_V||_{L²} = ||V(h)||²_{L⁴} ≤ 3^{2p'} ||V(h)||²_{L²}, with sup over admissible h finite by the Wick
  isometry with the log-singular kernel of (2μ)^{−1}.
- Lemma C.2 gives Z ≥ e^{−λ|a_0||B|}, and Theorem C.5 gives the sup over h ∈ C_E with supp h ⊂ B.
- Uniformity over the position of B needs one sentence: μ_0 and C_E are translation invariant, so the
  C.5 bound for B + a equals that for B. aqft asserts this in L.2. It must be written.
- I re-checked C.5's chain on the page: the Wick lower bound (C.3, which uses h ≥ 0 and h ≤ 1); the
  Wick-isometry estimate (C.4, near-diagonal split at 4/κ and the gradient bound beyond it);
  Chebyshev in L^{2q} with Nelson's (2q−1)^{p'}; the choice 2q = e^{L/4p'}; the doubly exponential
  tail. I found no error.
- C.5 now becomes load-bearing and needs its own independent audit, as mp and aqft say. Its constant
  is finite but not evaluated, so the M of Theorem 5.1 stops being explicit and Corollary 5.2's
  number retires.

**(iv) The differentiation identity.**
- U_{h_α} is affine in α, so e^{−U_{h_α}} ≤ e^{−U_{h_0}} + e^{−U_{h_1}} by convexity. The difference
  quotients are therefore dominated by |Q_V| |U_{h1_{B^c}}| (e^{−U_{h_0}} + e^{−U_{h_1}}).
- A3 gives U_h ∈ L^p and e^{−ρU_h} ∈ L¹ for every h ∈ C_E and every ρ, so the dominator is integrable
  by Hölder. Z(h_α) > 0 and is continuous.
- U_{h1_{B^c}} = Σ_Δ U_Δ is a finite sum (compact support), and every h_α ∈ C_E. A3 suffices; C.2 and
  C.5 are needed only for (iii). This is (1.1.12) with the domination written out (aqft L.1; mp
  "following Prop. 8.1").

**(v) Imports and the "same h" circularity.**
- The route cites only the printed statement of Theorem 1.1.7 (A8(iv)), at cutoffs in C_E, as
  Lemma 7.4 already does. That the source proves 1.1.7 from 1.1.8 at the same h (p. 597) is a fact
  about the source's proof. The record re-verifies no import's proof, A1-A7 included. So the status is
  the same as for A1-A7: "proved, conditional on literal A8(iv)".
- Two wording duties follow. First, A8's Scope (b) currently concludes "consistency therefore
  requires the constant of Theorem 1.1.8 to be uniform on the same class, which is (U_GJS)". Left
  standing, it makes the record contradict its own new status, so it must be rewritten. Second, the
  disclosure: the h-independence used is printed in 1.1.7, and its printed proof rests on 1.1.8 at
  the same cutoff (my trap G3), with the scope note of (ii).

**(vi) Hypotheses.**
- Theorem 1.1.7: "Let m_0, K_2 and K_1 be sufficiently large and let λ be sufficiently small."
  ll. 884-899 fix source-admissible M_*, λ_* and work in coordinates with m_0 = M_*, λ < λ_*, "so that
  the unit-lattice statements of Assumption A8 apply literally", with C_7, K_1, K_2, m_1 the printed
  constants. The route uses exactly these.
- C.2 and C.5 hold for every λ ≥ 0. Prop. 3.2's dilation keeps C_E and maps the GJS lattice to the
  working lattice, where B is built.
- Nothing new is needed. C_8 and ε_P's reference to "the expansion" become unused.

**(vii) Other points.**
- (a) mp's base term (Lemma L, T ≥ t_*) and aqft's (box B, every T) are both sound in outline. The
  arithmetic of mp's exponent check (121/21 < e²) is correct; I did not re-derive its Hölder chain.
- (b) Lemmas 7.1-7.3 and 7.6 (L.4) are uniform even in g. The factorial growth needed by Lemma 7.6
  survives, since (4n−1)!! ≤ 4^n (2n)!.
- (c) Appendix C's audit becomes provenance, but my F1 still stands as a misstatement about the source.
- (d) The route's M depends on C.5's unevaluated constant. That is acceptable, but Appendix A must
  say so.

## Consequence for Route E1

If Route L/M passes its audit, U_GJS is removed at the record's import standard (A1-A7, literal A8
items). **Route E1 becomes an optional upgrade, not a necessity.** Moreover, E1 as I scoped it (the
B = I branch of Theorem 1.1.8) would no longer be the right upgrade. To check what the record would
then rest on, a trace must target Theorem 1.1.7 itself: (1.1.11) at n = 0 with l-terms, both strip
orientations, and the rotated sharp-time case of (ii). That is larger than my 31-46-page estimate.
