# Memo `aqft` (R1, 28 October 2026): what the proof consumes, and a shorter route

Everything proposed here is `conjectured` until written and audited. Numbers are from
`companion/council/labels.md`; "l." is a line of `part_i/main.tex`. I read GJS on the images
`gjs74/p-06, p-10 to p-14` and Erice on `erice1/p-29 to p-31` and `erice2/p-07, p-08`.

## A. Verdict on O1-O5

**O1: confirmed as an account of what §7 consumes; superseded as a plan.** Lemma 7.1 (l. 1329)
needs a T-uniform bound on the integral of Q(0)^2 against dq_{h_{T,g}} at fixed g. Lemmas 7.2
and 7.3 need the same at the times s and ±t/2, for Lemma 4.3(ii) and to bound (10) and u_T.
Lemma 7.6 needs E_{mu_g}[X_f^{2n}] <= A K^{2n} (2n)! with A and K independent of n, so that
Theorem 7.7 gets some s_0 > 0. Proposition 7.5 needs only that Ĉ_Q is finite. The rate m_1 of
Theorem 7.8 comes from Lemma 7.4, i.e. CE2, which is printed with constants independent of h.
Nothing of §7 reaches §§8-12 except gamma = m_1 (l. 2153). But the comparison of O3 gives all
these bounds g-uniformly from CE2, so the fixed-g toolkit (Simon, Rosen, Omega_g in L^p) is
only a fallback.

**O2: modified, in four points.**
1. The word "equivalently" is wrong. The Euclidean bound sup_{T,g} of the integral of V(h)^2
   against dq_{h_{T,g}}, at most M^2, implies sup_g ||V(h)Omega_g|| <= M by Steps 5-6 of
   Theorem 5.1 (eq. (6) and the weak-graph passage). The converse fails, because the
   finite-T vectors ψ̂_T are not Omega_g. Only the Hamiltonian form is consumed.
2. The cutoff class is too large. Lemma 10.2 (l. 1992) applies Theorem 5.1 only at g_s in G
   (Lemma 3.1(iii)). The class C_H is needed only for item (5) as it is stated.
3. Only the centred moment is consumed. In the proof of Lemma 9.3,
   F(t) = <(1-P_0)X Omega, e^{itH}(1-P_0)A Omega>, so the variation bound 𝔪 (l. 1928) can be
   ||(1-P_0)X Omega|| ||A||. In Lemma 10.3, C_{j,s}(t) = <(1-P_s)V_j Omega_s,
   β_t(A) Omega_s>, so the outer bound (l. 2035) is M, not 2M.
4. U^{M2} is not an irreducible core; see O3.

*Trace of M (role card (i)).* M is defined in Theorem 5.1 and consumed once, in Lemma 10.2
(eq. (25): ||V_j Omega_s|| <= M for all s in [0,1], all j). Lemma 10.3 uses it in both regimes
(eq. (26)); Proposition 10.4 carries it linearly (eqs. (28), (27): 4M, 32M, shell count 8);
Lemma 10.5 puts it into Psi_gamma and C_{N,gamma,M} (eqs. (29)-(30)); §11 fixes gamma = m_1
(l. 2155). Theorem 11.1 needs Psi_{m_1}(d) < ε for all g, g' ≽ g_0 (Step 1, eq. (32)) and on
the cofinal set {g' ≡ 1 on O_d} (Step 3). Theorem 12.2 carries M in items (1) and (5).

The chain tolerates three weakenings:
- (a) the centred moment of point 3;
- (b) growth in r_j slower than the filter tail, e.g. M(1+r_j)^k, intrinsically
  M(1 + dist(supp h, {g=1}°))^k;
- (c) the class G instead of C_H.

None eases the proof: cells next to the plateau already need volume uniformity. The chain
does not tolerate:
- (d) Dependence on supp g, or on any volume. At a fixed plateau, supp g is unbounded among
  the g ≽ g_0, so the Cauchy criterion of Theorem 11.1 fails.
- (e) Dependence on the profile of g_s near B_j. These profiles range over all smooth
  [0,1]-valued functions, so a profile-wise bound is uniformity under another name.
- (f) A first-order form bound ±V_j <= ε(H(g_s)+c). It would serve the far-time regime,
  where only <Omega_s, V_j f_R(H_s)(1-P_s)A Omega_s> appears, with
  f_R(E) = ∫_{|t|>R} W_gamma(t) e^{itE} dt and |f_R(E)| <= min{T_gamma(R), C/E} for E >= gamma
  (integration by parts). It cannot serve the near-time regime, where Lemma 9.3 needs the
  vector (1-P)V_j Omega. And it is false at cells where g_s is small, since deg V(h_j) = deg P
  and h_j changes sign (KB `result/hamiltonian-bypass-dead`).
- (g) The gap. It bounds the variance by γ^{-1}<VΩ, HVΩ>, which is already +∞ for the Fock
  vacuum (`m4/h6.tex` Props. 2.1-2.2). Expositions p. 57's N^loc <= const(H(g)+I), even if
  uniform in g, gives the first moment of N^loc; V_j needs the (deg P)-th (h6.tex Rem. 4.3).
- (h) A uniform L^{1+δ} bound (h6.tex Thm. 3.2) serves the near-time regime only. The
  far-time regime still needs a second moment of the tail; h6.tex Lemma 3.4 covers only A in
  a domain class, not the unit ball of A(O).

**O3: refuted, by the argument below (itself `conjectured` until written).** The regress
arises only when the difference cutoff meets the neighbourhood of the observable. I call the
following comparison Route L.
- *The comparison.* Compare h := h_{T,g} with its restriction h·1_B, where B is a box of GJS
  lattice squares. GJS squares are "centered at the lattice site" (p. 593), and B contains
  the localization squares of Q_V = V(h)² (at most three squares in the row of time 0) with
  a margin of one square. Along h_α := h·1_B + α·h·1_{B^c}, every cutoff lies in C_E, and
  ⟨Q_V⟩_h − ⟨Q_V⟩_{h1_B} = −∫_0^1 dα Σ_{Δ⊄B} Cov_{h_α}(Q_V, U_{h1_{B^c}1_Δ}).
- *The estimate on each term.* Every square Δ outside B is separated from the squares of Q_V
  by a strip of width at least 1. The term U_{…1_Δ} is a localized monomial of class (1.1.6)
  with r = 1 (p. 593). Theorem 1.1.7 (p. 594: "constants 0 < m_1 and O(1) independent of h,
  Q_1 and Q_2") bounds the term by C_7 e^{−m_1 dist} ||Q_V|| ||U||. The sum over Δ is
  bounded independently of T and g.
- *The base term.* The cutoff h·1_B lies in C_E with support in the fixed compact set B.
  There, Cauchy–Schwarz against dμ_0, Lemma C.2 and Theorem C.5 bound ⟨Q_V⟩_{h1_B}.
- *What is not used.* The argument needs no fourth moment, no fixed-g input and no CE1.

The device is the source's own (GJS (1.1.12), p. 595; Erice I p. 162, proof of Theorem
2.2.2), used there for convergence. Role-card item (iv): Theorem 1.1.7 with the record's
compact-support results (not its fixed-g results) yields U^{M2}, by an estimate.

**O4: confirmed, and moot under Route L.** What the images show:
- Erice I p. 161, (2.2.7) "∫A dq_h ≤ ||A|| uniformly in h" closes a bracketed remark. It is
  printed without absolute-value bars, and its norm (2.2.5) uses η = ∏(K_1 N(Δ)!) with no K_2.
- Pp. 160-161 call h only a "space time cutoff". P. 162 reads "Let 0 ≤ h_0 ≤ h_1 ≤ 1 be two
  space-time cutoffs"; the brief's "0 < h_0 < h_1 < 1" comes from the text layer.
- Erice II fn. 5 (p. 205) is an assertion.

Re-sourcing changes a label, not a proof; Route L needs no CE1 from any source.

**O5: modified.** Levels 2 and 3 remain viable but are no longer the only routes, and their
target moves. After Route L, the content of U_GJS rests on the printed h-independence of
Theorem 1.1.7, and the printed proof of that theorem (pp. 596-597) takes Theorem 1.1.8 "at
the same h". A Level-2 trace would follow that chain. I make no claim about the
non-expansion methods; I know them only from memory, and they are not needed.

**Operator-algebraic routes (role card (iv)): none.** Local normality (Proposition 11.2) comes
after M, so using it would be circular, and its L^1 density controls no unbounded moment. Norm
convergence on A(O) gives only ω_∞(V²) ≤ liminf ω_g(V²), never a g-uniform upper bound.
Cyclicity and the Fock folium carry no quantitative content. What is missing is uniform
integrability (h6.tex §3), and that takes an estimate.

## B. Statements to prove

**Conventions.** Working coordinates of §2.6. C_7 and m_1 are the constants of Theorem 1.1.7
for the printed K_1, K_2 and n̄ = 2p'+1; none depends on h. Squares are GJS lattice squares.

**Notation.**
- For a rectangle R of a×b squares, B(R) is R enlarged by one square on every side.
- Σ_{a,b} := Σ_{k≥1} (a+2k+2)(b+2k+2) e^{−m_1 k}. It bounds Σ_{Δ⊄B(R)} e^{−m_1 dist(Δ,R)},
  since a square at sup-index distance m from R lies at distance at least m−1 from R.
- c_U := λ Σ_{n=1}^{2p'} |a_n| K_1 K_2^{2n} n!.
- S_2(B) := sup{||e^{−U_{h'}}||_{L²(dμ_0)} : h' in C_E, supp h' ⊆ B}, which is finite by
  Theorem C.5.

**L.1 (affine-path identity).** Let h_1, h_2 be in C_E and let F be a finite sum of localized
monomials of class (1.1.5)-(1.1.6). Then α ↦ ⟨F⟩_{h_1+α(h_2−h_1)} is C¹ on [0,1], and
⟨F⟩_{h_2} − ⟨F⟩_{h_1} = −∫_0^1 Cov_{h_α}(F, U_{h_2−h_1}) dα.
Proof plan: α ↦ e^{−U_{h_α}} is convex, so the difference quotients are dominated by
|F||U_{h_2−h_1}|(e^{−U_{h_1}} + e^{−U_{h_2}}). Then Hölder, A3 or Theorem C.5, and Lemma C.2.

**L.2 (localized comparison).** Suppose every monomial of F has its localization squares in R.
Then for every h in C_E,
|⟨F⟩_h − ⟨F⟩_{h1_{B(R)}}| ≤ C_7 c_U Σ_{a,b} ||F||_GJS.
The right side is uniform in h and in lattice translations of R.

**L.3 (replaces U_GJS in §5).** For all g in C_H, all T > 0, and all real measurable h with
||h||_∞ ≤ 1 and supp h in an interval of length 2:
∫ V(h)² dq_{h_{T,g}} ≤ M̃², where
M̃² := e^{15λ|a_0|} 3^{2p'} V_* S_2(B_{3×5}) + C_7 c_U Σ_{1,3} · 9 K_1 K_2^{8p'} (4p')! λ² (Σ|a_n|)².
Here V_* := sup_h ||V(h)||²_{L²(dφ_0)} is finite by the Wick isometry. The factor 3^{2p'}
comes from the comparison ||Y||_4 ≤ 3^{p'}||Y||_2 for chaos of degree at most 2p', the step
used in the proof of Theorem C.5. Steps 5-6 of Theorem 5.1 then give ||V(h)Omega_g|| ≤ M̃ for
every g in C_H.

**L.4 (replaces U_GJS in §7).** Let Q be a cylinder monomial (§6) with support I, and let s be
in R, T > 0 and g in C_H. Let R_I be the 2×N_I rectangle covering the rows that can meet time
s, and B_I := B(R_I). Then
∫ Q(s)² dq_{h_{T,g}} ≤ C(Q) := e^{λ|a_0||B_I|} ||Q²||_{L²(dφ_0)} S_2(B_I) + C_7 c_U Σ_{2,N_I} n(Q)².
For Q = X_f^n this gives C(X_f^n) ≤ A_f K_f^{2n} (2n)!, with
K_f := max{K', (2⟨f,Cf⟩)^{1/2}} and A_f := e^{λ|a_0||B_I|} S_2(B_I) + C_7 c_U Σ_{2,N_I} K_1.
The Gaussian factor is bounded through (4n−1)!! ≤ 4^n (2n)!.

**Minimal fallback hypothesis U^{M2}_min.** sup_{g in G} ||(1−P_g)V(h)Omega_g|| ≤ M for the h
of L.3. Items (1)-(4) of Theorem 12.2 consume exactly this once Lemmas 9.3 and 10.3 use the
centred norm (O2, point 3).

**What each phase changes (role card (ii)).**
- *If Route L passes its gate.* `Proved` from the literal imports A1-A7, A8(i)-(iv), (viii)
  alone: Theorems 5.1 (constant M̃), 7.8 and 11.1, Theorem 12.2 (all five items, both clauses
  of (5)), Proposition 11.2, Corollary 12.3 and Theorem 13.2.
  - A8(v)-(vii') move to provenance.
  - Proposition C.7 shrinks to "every CE application is CE2 as printed".
  - Lemma C.2 and Theorem C.5 become load-bearing.
- *Under the fallback* (O1 executed with literal fixed-g inputs, Route L abandoned).
  - Theorem 7.8 and the gap clause of 12.2(5) become `proved`.
  - The following are `proved, conditional on U^{M2}_min`: Theorems 5.1 and 11.1,
    items (1)-(4) of Theorem 12.2 and the moment clause of (5), Proposition 11.2,
    Corollary 12.3 and Theorem 13.2.
  - Step 1 of Theorem 13.2 alone does not depend on U^{M2}_min.
- *§14, in every case.* The record "neither establishes nor needs" GRS Problem 1. L.3 bounds
  one local second moment and no local density.

**The standard (role card (iii)).** A1-A7 are printed statements whose proofs the record does
not re-verify.
- After Route L the whole record sits at exactly that standard: CE2 is a printed statement,
  its proof not re-verified.
- A Level-2 trace exceeds it in one dimension (the h-dependence is checked display by display)
  and equals it in the other (the convergence of the expansion is still taken from print).
- Only Level 3 makes the input a theorem of the record.

The final record then says, respectively:
- "proved from literal imports; the h-independence used is the one printed in Theorem 1.1.7";
- the same sentence, with "and traced display by display in a new appendix" added;
- "proved".

In the companion after Route L:
- §4 is retitled (every import literal); its record box shows L.3 instead of (U_GJS), and its
  sentence "Theorem 12.2 does not consume it" (Appendix C) is reversed.
- In Figure 1 the violet class disappears; the U_GJS node becomes "Appendix D: CE2 + Lemma
  C.2 + Theorem C.5"; the caption's "No arrow from Appendix C closes the dashed box" goes.
- Figure 2 becomes historical.

Under the fallback, violet leaves only the (G) column.

## C. Routes

**Route L (recommended).**
- *Base.* GJS Theorem 1.1.7 and (1.1.5)-(1.1.9) (pp. 593-594); GJS (1.1.12) (p. 595) as
  precedent; Lemma C.2 and Theorem C.5 of the record.
- *Steps.*
  1. Prove L.1.
  2. Set up the geometry: B(R), the strip widths, and the square count behind Σ_{a,b}.
  3. Prove L.2.
  4. Prove L.3 and use it to replace eq. (6) in Step 5 of Theorem 5.1.
  5. Prove L.4 and use it to replace the CE1 lines of Lemmas 4.3(ii), 7.1-7.3 and 7.6, with
     the new constants in Proposition 7.5 and Lemma 7.6.
  6. Retire A8(v)-(vii'). Rewrite Proposition C.7, the hypothesis and imports paragraph of
     Theorem 12.2, the title-page notice, the abstract, Appendix A (M̃ and C(Q); the number
     in Corollary 5.2 retires) and the Appendix B residue.
  7. Run the build gates.
- *Deliverable.* A draft `ugjs/route-L.tex`, merged as Appendix D of `part_i/main.tex` (an
  appendix keeps the body numbers 2.1-13.3 fixed).
- *Estimate.* 4-5 pages of new proof and about 2 pages of edits; 2 verification rounds.
- *Imports.* None new (section E).
- *Risk.* The step most likely to fail is the scope of (1.1.10) for the pair formed by an
  equal-time two-factor monomial at time 0 and a time-integrated one-factor monomial in one
  square.
  - If a reader restricts (1.1.10) to sharp-time monomials, write U as an integral over x^0
    of sharp-time slices and apply (1.1.10) slice by slice, as Lemma 7.4 already does. This
    costs about half a page more.
  - If the h-independence itself proves restricted, Route L fails, and we fall back.

**Route F (fallback; `mp` owns it).** O1 for §7 with fixed-g inputs. U^{M2}_min then remains the
one named hypothesis. It is smaller than U_GJS: one observable, the net class G, and the
centred moment.

**Level 2 (optional upgrade, not removal).** After Route L it traces the printed proof of
Theorem 1.1.7 (pp. 596-597, Theorems 1.1.8, 1.1.11, §§2-4); without Route L, Theorem 1.1.8.
Size: `cqft`'s estimate.

**Level 3.** Not for this goal.

## D. Recommendation

**Phase 0 (author checkpoint 1; no mathematics).**
- Adopt Route L as the core.
- Ask the human C5 reader for items 1-4 first (pp. 589, 590, 593, 594). These become the
  load-bearing transcriptions, and items 5-9 become history.
- Run this in parallel with Phase 1.

**Phase 1 (Route L).** Gate GL; all of the following must hold.
- GL1. Every use of (1.1.10) names Q_1 and Q_2 with their class, their localization squares,
  the cutoff with its membership in C_E, and the separating strip with its width. A second
  agent re-derives each.
- GL2. The integrability chain of L.1 cites only A3 or Theorem C.5, Lemma C.2, Hölder and
  dominated convergence, with every exponent written out.
- GL3. M̃, Σ_{a,b}, C(Q), A_f and K_f are recomputed by hand, in the style of G3, and entered
  in Appendix A.
- GL4. A reviewer who did not write Lemmas C.2-C.4 and Theorem C.5 re-audits them, because they
  become load-bearing.
- GL5. `grep -n 'UGJS\|C_8' part_i/main.tex` hits provenance lines only. Theorem 12.2 no longer
  contains "Assume U_GJS". G0 and G5 pass, and the `.aux` diff shows 2.1-13.3 unmoved.
- GL6. C5 items 1-4 read MATCHES.
- GL7. An adversarial pass in the style of G6 leaves zero unresolved findings.

If GL1 or GL6 fails, use the fallback described in section C. Author checkpoint 2 comes
before Appendix D is merged into `main.tex`.

**Phase 2 (optional; offer it to the author).** Level 2 on the printed proof of Theorem 1.1.7.

**Never for this goal.** Level 3; and re-sourcing to Erice in place of Phase 1.

## E. Imports and sources (Route L)

All are already in the record; none is new; nothing is to be acquired.

| statement | source | status | read |
|---|---|---|---|
| Theorem 1.1.7, (1.1.10), "independent of h, Q_1 and Q_2"; strip width d | GJS p. 594 | literal, A8(iv) | image read today; human: C5 item 4 |
| (1.1.5)-(1.1.6), including time-integrated monomials; squares centred at lattice sites; n_i < n̄ | p. 593 | literal, A8(ii) | read; C5 item 2 |
| norms (1.1.7)-(1.1.9) | p. 594 | literal, A8(iii) | read; C5 item 3 |
| class "compact support in R², 0 ≤ h ≤ 1" | p. 589 | literal, A8(i) | read; C5 item 1 |
| dilation | p. 590 | literal, A8(viii) | KB verified claim; I did not re-read it |
| hypercontractivity (via Theorem C.5) | Simon Thm. I.17 | literal, A4 | on disk; I did not read it |
| FKN; simplicity (Steps 5-6, Lemma 4.4) | A2, A1 | literal | unchanged |
| finite-volume stability (optional in L.1) | Simon Thm. V.7 | literal, A3 | I did not read it |

The following leave the hypothesis list: A8(v) CE1, A8(vi), and A8(vii) with (vii'). Pages
589, 590, 593 and 594 still need a human reader (C5 items 1-4).

## F. Findings

- **F1 MINOR.** At l. 1349 (the proof of Lemma 7.1, p. 18), `\|Q\widehat\psi_{T_\alpha}\|le`
  prints "‖Qψ̂_{T_α}‖leC_8^{1/2}n(Q)". I checked this on the rendered page. Repair: `\|\le`.
- **F2 MINOR, relevant to the plan.** `docs/imports.md` ("What would discharge it") says "The
  only proportionate route to an unconditional Theorem 12.2 is a display-by-display trace". The
  same claim appears in the KB nodes `problem/level2-h-trace` (summary) and
  `result/hamiltonian-bypass-dead` ("Consequence"), and in
  `companion/sections/s4-import.tex`. Nothing in the record excludes Euclidean routes from the
  printed CE2, and Route L is a candidate. Repair: say "one route" now, and rewrite after
  Phase 1.
- **F3 MINOR.** Theorems 5.1, 7.8 and 11.1, Proposition 11.2, Corollary 12.3 and Theorem 13.2
  rest on (U_GJS), but state no hypothesis beyond the weak-coupling inequality. "Assume U_GJS"
  appears only in Theorem 12.2 (l. 2295) and Proposition C.7 (l. 2921). The standing-import
  convention of §2.4 covers this formally, but Corollary 12.3 quoted on its own reads as
  unconditional. Repair: add "(under Assumption A8, including (vi))", unless Phase 1 makes
  this moot.
- **F4 MINOR.** GJS squares are "the unit lattice square in R² centered at the lattice site"
  (p. 593), while Step 2 of Theorem 5.1 (l. 1188) and Proposition 6.2 (l. 1296) decompose over
  [j, j+1). The counts (at most 3; N_I ≤ ⌊L⌋+2) and every constant are the same on the printed
  lattice, but the text should use that lattice. C5 item 2 already asks for the convention,
  and Route L must build B on the printed lattice.

## G. Traps

1. "Route L proves U_GJS." Say instead: A8(vi) is no longer used. The h-independence consumed
   is the one printed in the statement of Theorem 1.1.7. Its printed proof (pp. 596-597) uses
   Theorem 1.1.8 at the same h, and that proof is not re-verified.
2. "Theorem 12.2 is unconditional." Say instead: it is proved from the literal imports A1-A7
   and A8(i)-(iv), (viii), for 0 ≤ λ/m_0² < ε_P. The human reading of pp. 589-594 (C5) is
   still open.
3. "M is unchanged." It is not: the constant becomes M̃. C_8 disappears, the number
   362 880 C_8 K_1 K_2^{16} λ² of Corollary 5.2 retires, and the M inside Psi_{m_1} and
   C_{N,gamma,M} changes.
4. "(M_2) can be weakened to uniform L^{1+δ}." That covers the near-time regime only. In the
   far-time regime the norm on A(O)* needs the centred second moment.
5. "The gap controls the local moment." It does not: its variance bound γ^{-1}<VΩ, HVΩ> is
   already +∞ for the Fock vacuum.
6. "Uniform local moments settle GRS Problem 1." They do not. Uniform local L^q densities
   would imply (M_2) (h6.tex Prop. 4.1); (M_2) does not imply them.
7. "Erice (2.2.7) makes U_GJS literal." It is a bracketed remark with another norm and an
   unspecified cutoff class: corroboration at most.
8. "The comparison works for any cutoff." It works for h in C_E only. CE2 and Theorem C.5 use
   h ≥ 0 and h ≤ 1 (Remark C.6), and the restriction h·1_B keeps every path cutoff in C_E.
9. "Appendix C is not consumed" (companion §4). After Phase 1, Lemma C.2 and Theorem C.5 are
   load-bearing.
10. "Level 2 is now pointless." It is the only way to lift the weak-coupling input above
    the A1-A7 standard; optional.
11. "A subnet would let M depend on g." It would not help: the theorem concerns the full net,
    and Theorem 11.1 needs M uniform over all g, g' ≽ g_0.
12. "The count of statements that reach A8 (`docs/status.md`; `labels.md`) drops to zero." It
    does not: CE2 is item (iv) of A8. Recompute the index against A8(vi), or retire it.
