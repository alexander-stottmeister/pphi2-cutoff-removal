# Memo R1 — `editor` (handling editor): removing U_GJS from Theorem 12.2

Written 28–30 October 2026. Every route, estimate and plan item below is `conjectured`. The
only exceptions are reports of what a page says, and those were read in this session. Read:
the brief (re-read after its 28 October correction); `docs/status.md` and `docs/imports.md`;
`companion/council/labels.md`; `part_i/main.tex` ll. 1–2939; `part_i/README.md` and
`part_i/C5_reading_record.md`; `m4/r1-check.tex`; `companion/PLAN.md` and
`companion/council/README.md`; companion §4 (`s4-import.tex`); `README.md` ll. 1–140;
`strategy.md` ll. 2215–2310; nine KB nodes (E). Page images, by printed page: GJS
pp. 594–596, 600–602, 622 and 624–632; Erice I pp. 160–163; Erice II pp. 205–206, 236–238
and 242. I rendered two more myself: Simon p. 156 and GJ4 pp. 1568–1569. Record numbers are
from `labels.md`.

## A. Verdict on O1–O5

**O1: confirmed, and cheaper than the brief expects.**
- *Finiteness at each T needs no U_GJS.* For F = Q(s) or V(h)(s), F² lies in every
  L^q(dμ₀). A3 gives Z(h) > 0 and e^{−𝒰_h} ∈ L²(dμ₀), so Hölder bounds ∫F² dq_{h_{T,g}}.
  Lemma 4.3(ii) nevertheless credits this finiteness to U_GJS (F2).
- *Uniformity in T at fixed g.* Simon p. 156 (read on the image), Theorem V.10(iii): "P(t) is
  bounded from L²(Q_F) to L^s(Q_F) so long as s < s(t) ≡ 1 + e^{2mt} … for all interaction
  polynomials and all g's" (cited elsewhere as "Theorem V.11 (iv)"; mp settles which).
  - By A2, P(t) = e^{−tK(g)}, so sup_{T≥t}‖ψ_T‖_s < ∞ for some s > 2.
  - Hölder and ‖ψ_T‖ ≥ c_g (Lemma 4.4) then bound sup_{T≥t}‖Qψ̂_T‖.
  - Since Ω_g ∈ L^s, E_{μ_g}e^{σ|X_f|} < ∞ for every σ ≥ 0, and Lemma 7.6's factorials
    disappear.
  - Theorem C.5 and Lemma C.2 are needed only to keep "sup_{T>0}".
- *Nothing propagates.* Theorems 7.7–7.8 (ll. 1538–1620) use s₀ and Ĉ_Q only to know they
  are finite. §§8–11 receive only γ = m₁ and M.
- *Caveat.* In GJS's printed proof, CE2's h-independent constant comes from Theorem 1.1.8 at
  the same h (pp. 596–597; a verified claim of the KB reference). Phase 1 removes a
  non-literal import from Theorem 7.8, but not its reliance on the GJS expansion.

**O2: confirmed, with three refinements.**
- *Class.* Lemma 10.2 uses Theorem 5.1 only at g_s with g, g′ ∈ 𝒢 sharing a plateau. These
  g_s lie in 𝒢 (Lemma 3.1(iii)). So items (1)–(4) of Theorem 12.2 need U^{M2} over 𝒢 only;
  𝒞_H matters only for the moment clause of item (5).
- *Dependence on the cell.* A bound ‖V_jΩ_s‖ ≤ C(1+r_j)^k would keep the net Cauchy, because
  Lemma 10.5 uses T_γ(r) ≤ C_{q,γ}(1+r)^{−q} for every q (ll. 2134–2135). Dependence on g as a
  whole, which is what fixed-g methods give, does break it. No harmless bound is known, so
  the statement stays uniform in g.
- *Hamiltonian form.* By A5(i) and the closed-graph theorem, V(h)e^{−tK(g)} is bounded. So
  ‖V(h)ψ̂_T‖ → ‖V(h)Ω_g‖, and U^{M2} ⇔ sup_g‖V(h)Ω_g‖ ≤ M.

**O3: confirmed, as an estimate.** The unit squares of supp(g′−g) next to the localization of
V(h)² have no separating strip. Their covariance terms need higher moments at every
intermediate cutoff, so the comparison does not close. A second loophole is also closed. GJ4
Theorem 1.1 (J. Math. Phys. 13 (1972), p. 1569) bounds |δE| ≤ MD "independent of g and h".
But it does so only under (1.7), 0 ≤ 𝒫(ξ)g(x) + 𝒫₁(ξ)h(x) (p. 1568). That gives first-order
information only, and excludes negative leading-degree perturbations where g = 0. GJ4 is not
a route, but `result/hamiltonian-bypass-dead` should cite it.

**O4: confirmed.** Erice I p. 161 prints "(2.2.7) ∫A dq_h ≤ ‖A‖ uniformly in h", in brackets,
under "n_i ≤ n̄ … K₁ sufficiently large". Its norm is (2.2.5), η∏‖f_i‖ with
η = ∏_Δ(K₁N(Δ)!). Its observables (2.2.3) admit sharp time, so V(h)² is covered. It still
cannot carry the import:
- No class of h is printed. p. 162 (image) uses an ordered pair 0 ≤ h₀ ≤ h₁ ≤ 1, narrower
  than the Annals' arbitrary h₁, h₂.
- The norm is not the one behind the constants of §§5–7.
- There is no proof.

Re-sourcing would only give "assembled from two sources": still non-literal. Erice II
Theorem 2.2 (p. 206) is a bound "as Λ → ∞" for Schwartz kernels, without a norm. Footnote 5
there is an assertion.

**O5: confirmed in outline, with four corrections from the images.**
1. *Stability enters the constants.* p. 624: "(2.4.34) For m₀ ≥ 1, λ ≤ 1, there is a constant
   K₃, independent of C, m₀ and λ such that 1 ≤ ‖e^{−V(Y)}‖_{L₂(dΦ_C)} ≤ e^{K₃|Y|}", with
   (2.4.35). Then: "These are standard estimates for such integrals (see [1])", where [1] is
   Dimock–Glimm, Adv. Math. 12 (1974) (p. 631; not on disk). And: "which yields (2.4.28), for
   K₂ ≥ K₃²"; Lemma 2.4.6 (p. 622) takes "K₂ = K₂(m₀, K₃)".

   V(Y) carries the cutoff; this is my reading of V(Yh) in (2.0.2), p. 601. So K₂, the norm
   and C₈ rest on a stability bound under the Dirichlet-interpolated measures, and that bound
   is not printed as h-independent. Erice II Theorem 9.5 (p. 237) gives the C-uniform form,
   (9.8), for regions without a cutoff function, and refers to "[1, §II.3, p. 22-27]".

   Call the h-uniform version of (2.4.34)–(2.4.35) **Lemma D.stab**. It cannot be traced: it
   must be acquired or proved, and both Level 2 and Level 3 need it.
2. *Omissions.* p. 627 says the remaining terms "are bounded similarly", and that (3.1) "is
   convergent, as follows similarly to the proof of convergence of (2.3.7)". p. 628 says
   Theorem 4.1's step "is similar to, but easier than the analogous step in the proof of
   Theorem 4.2 below, so we do not give the details". That proof is on pp. 630–631.
3. *Range.* pp. 600–631, not "598–629" (F3).
4. *Target n = 0, B = I* (p. 629). The map must say which annihilator steps, and hence which
   omissions, vanish at n = 0. Convergence uses |m_α| ≤ ‖m_α‖_{2K₂}e^{O(Vol)}, where Vol
   depends on supp h (pp. 624–625). This use is per-h and qualitative, and harmless as long
   as it stays there.

So Level 2 can honestly end only as **Level 2+**: the trace, plus the record's own proofs of
D.stab and of every omission on the n = 0 path. The text layer shows about 90 numbered
displays on pp. 600–631; cqft should count them on the images.

## B. Statements to prove

**S1 (P1, fixed g).** For every g ∈ 𝒞_H:
- (a) for all T > 0, s ∈ [−T,T] and cylinder monomials Q, the integrals ∫Q(s)² dq_{h_{T,g}} and
  ∫V(h)(0)² dq_{h_{T,g}} are finite;
- (b) for every Q and every t₀ > 0: Ω_g ∈ D(Q), and sup_{T≥t₀}‖Qψ̂_T‖ ≤ C₁(g,Q,t₀) < ∞;
- (c) for real f ∈ C_c^∞(ℝ) and σ ≥ 0: E_{μ_g}e^{σ|X_f|} ≤ C₂(g,f,σ) < ∞.

C₁ and C₂ depend on g but appear in no statement of §§8–14. Once S1 is proved, these become
proved from literal imports (A1–A5 and CE2): Lemma 4.3, Lemmas 7.1–7.3, Lemma 7.6,
Proposition 7.5, Theorems 7.7–7.8, and the gap clause of Theorem 12.2(5).

**S2 (the core) = Theorem D.1, U^{M2}.** In the working coordinates of §2.6 there is a constant
M = M(m₀,λ,𝒫) < ∞ such that, for every g ∈ 𝒞_H, T > 0, a ∈ ℝ, and real measurable h with
‖h‖_∞ ≤ 1 and supp h ⊆ [a,a+2],

  ∫V(h)(0)² dq_{h_{T,g}} ≤ M²,  where V(h)(0) = λ∫h(x):𝒫(Φ(0,x)):dx.

M is uniform in g, T, h and a. Under Level 2+, M² = 9C₈𝔎(p′)λ²(Σ|a_n|)², where C₈ is the
n = 0 constant of the printed proof; the trace must show that C₈ depends only on
(m₀,K₃,K₂,K₁,λ,ε,𝒫,n̄). Under Level 3, M is the record's own constant, possibly on a smaller
region ε′_𝒫. The form actually consumed is sup_{g∈𝒞_H}‖V(h)Ω_g‖ ≤ M; 𝒢 suffices for items
(1)–(4).

Theorem D.1 changes the status of Theorem 5.1, Lemmas 10.2, 10.3 and 10.5, Proposition 10.4,
Theorem 11.1, Proposition 11.2, Theorem 12.2, Corollary 12.3, Theorem 13.2 and
Proposition C.7, as set out in H. U_GJS itself (all sharp-time polynomials) is retired, not
proved. Not targets: CE2's h-uniformity; anything beyond weak coupling.

## C. Routes (estimates; cqft and cqft2 own the details)

| route | base | output | pages | likely failure → then |
|---|---|---|---|---|
| R1 fixed g | Simon p. 156; A2, A3; Lemma 4.4 | edits to §§4, 7 | 3–5 | Simon's class of g against 𝒞_H → closed graph via A5(i) plus an L^p import for Ω_g; failing that, U_GJS stays in §7 |
| R2a map | GJS pp. 600–631, images | one row per display | 8–15 (tables) | completeness (the earlier audit missed (2.4.34)) → blind recount |
| D.stab | Theorem C.5's method, or Dimock–Glimm | lemma with constants | 5–10 | the bound e^{K₃|Y|}, uniform in C (Theorem C.5 gives neither) → acquire Dimock–Glimm |
| R2b Level 2+ | R2a, D.stab, the omissions | Supplement D | 20–40 | an omission that cannot be supplied → "conditional on <that step>" |
| R3 Level 3 | own expansion, slab cutoffs, one observable | Supplement D | 40–70 | deriving every constant → ε′_𝒫 enters Theorem 12.2 |
| R4 | `from memory`; cqft2 | one memo | unknown | sharp time; free boundary; [0,1]-valued g; general 𝒫 |
| R0 | Erice I p. 161 | one sentence | ≤ 1 | none; no change of status |

Verification rounds: R1 two; R2a two; D.stab two; R2b three, plus a human reading; R3 four
to six.

## D. Recommendation

1. After Checkpoint 1, run three things in parallel:
   - **P1** (R1, mp);
   - **P2a** (R2a, cqft);
   - **D.stab** (cqft2 with mp), starting once the map has fixed the covariance family and
     (2.4.34)–(2.4.35).
2. **Checkpoint 2** comes after the P1 and P2a gates and an attempt at D.stab. It chooses
   R2b, R3, or stopping.
3. Then **P2b** or **P3**, and finally **P4**, the integration.
4. R0 is optional; R4 gets one memo. Never: full U_GJS; re-sourcing counted as a change of
   status; CE2's h-uniformity; anything beyond weak coupling.

Gates:
- **P1:**
  - no proof in §§4, 6, 7 cites `eq:UGJS`;
  - the new import is quoted verbatim, with page image, *Used in* and *Dossier*;
  - a written check that C₁, C₂, Ĉ_Q and s₀ appear in no statement of §§8–14;
  - the `.aux` labels are unchanged;
  - a fresh adversarial agent confirms no findings, and the build is clean.
- **P2a:**
  - each display on the n = 0 path gets exactly one verdict: *h absent*;
    *majorised at first contact* (with the page); *identity*; *per-h qualitative*;
    *h-uniform via a named lemma*; *vacuous at n = 0*; or *omitted in print* (quoted);
  - no row is "unknown";
  - a blind per-page recount agrees;
  - every external citation is listed.
- **D.stab:** the dependence of every constant is stated, and an agent who did not write the
  proof checks it.
- **P2b/P3:**
  - S0–S6 (J);
  - the chain of constants is recomputed by hand, in the order m₀, K₃, K₂, K₁, λ;
  - an agent told to find a missed h-dependence confirms none.
- **P4:** G0–G6 are re-run, and every public status sentence agrees with H.

Fallbacks:
- P1 fails → U_GJS stays in §7.
- Many omissions cannot be supplied → R3.
- The core stalls → A8(vi) is restated as U^{M2}, and the open step is named.

## E. Imports and sources

| statement | source | status; phase |
|---|---|---|
| L² → L^s bound for e^{−tK(g)} | Simon Thm V.10(iii), p. 156 | on disk, read; new literal item A4(ii); P1 |
| P(t) = e^{−tK(g)}; e^{−𝒰_h} ∈ L^p | A2; A3 | literal, existing; P1 |
| CE2 | A8(iv), GJS p. 594 | literal; kept |
| estimates at fixed h, GJS §§2–3, n = 0 path | GJS pp. 600–631 | on disk (images); new item A8(vi′) = Table D.1; literal only under standard R (H); P2b |
| stability under dΦ_C | Dimock–Glimm 1974 | to acquire; otherwise prove D.stab |
| Gaussian integrals, C in the family | Erice II §9, pp. 232–239 | on disk, pp. 236–238 read; its proofs point to [1] |
| h-uniform moment bound | Erice I (2.2.7) | read; corroboration only |
| g-uniform energy shift | GJ4 Thm 1.1 | read; KB only |
| Bessel bounds on G(ζ) | Lemma C.4, "classical" | to be cited or proved (F5) |

KB nodes read (nine):
- glimm_jaffe: `import/u-gjs`, `decision/ugjs-imported-at-source-scope`,
  `problem/level2-h-trace`, `result/hamiltonian-bypass-dead`, `problem/c5-second-reader`,
  `result/main-theorem-conditional`;
- common: the references `glimm-jaffe-spencer-1974`, `glimm-jaffe-expositions` and
  `glimm-jaffe-spencer-erice-1973`.

No reference node exists for Simon, GJ4 or Dimock–Glimm. A human reads Simon p. 156 and
the h-rows of Table D.1 (C6).

## F. Findings about the record

**F1 (MAJOR for Appendix C's narrative; no numbered result changes).** Three passages of
Appendix C are false as statements about GJS:
- M3, l. 2699: "This is the single point where h touches a quantitative estimate."
- M4, ll. 2708–2709: "(by M5, no constant of the source depends on it)".
- M5, ll. 2725–2727: "no stability estimate, enters any constant of the proof".

GJS p. 624 (2.4.34) and p. 622 (Lemma 2.4.6) contradict all three: a stability bound for
e^{−V(Yh)} under dΦ_C fixes K₂. Proposition C.1 survives only because it is limited to
"mechanisms M1–M5 as recorded". The G6 disposition of R4 (`part_i/README.md`) and abstract
item (2) of `m4/r1-check.tex` ("never estimated") rest on the same claim. That file's Remark
rem:remaining(b) already records that OCR did not let it certify (2.4.6)–(2.4.17) and (3.2)–(3.6).

Repair: add a mechanism M6 ("stability under dΦ_C; K₃ → K₂"), narrow the three sentences,
and have the Scope paragraph name K₃'s uniformity in h.

**F2 (MINOR).** The proof of Lemma 4.3(ii), ll. 1109–1118, attributes the finiteness of square
moments at each T to U_GJS. A3 and Hölder suffice.

**F3 (MINOR).** "pp. 598–629" as the range of the trace appears in five places:
`docs/imports.md` l. 57; `strategy.md` ll. 2235 and 2275; `part_i/README.md` l. 155;
companion §4, l. 75; the KB problem node. The argument runs to p. 631, and its stability input
is Dimock–Glimm. This confirms, at the source, item F21 of the companion's register.

**F4 (MINOR).** Scope (b), ll. 793–796, says "consistency therefore requires the constant of
Theorem 1.1.8 to be uniform". But importing CE2's printed statement commits the record to
nothing about Theorem 1.1.8; only trust in GJS's proof would. Repair: "the source derives
that constant from Theorem 1.1.8 at the same h".

**F5 (MINOR).** Lemma C.4, l. 2839, uses "classical Bessel facts" with no citation. They become
load-bearing once D.stab builds on Lemma C.4.

Still open, re-read today: companion register items F2 (`\|le`, l. 1349), F3 and F18
(l. 780).

## G. Traps

1. Not "U_GJS is proved", but "U_GJS is no longer imported; Theorem D.1 proves U^{M2}".
2. Not "unconditional", but "proved from the literal imports A1–A8 and the record's own
   proofs", with C5 and C6 named.
3. After P1, not "the gap is independent of GJS's expansion", but "Theorem 7.8 no longer uses
   U_GJS; it rests on CE2 as printed".
4. Not "the trace verifies GJS", but "it checks the h-dependence of every estimate it uses;
   the estimates at fixed h are imported".
5. p. 629 states the uniformity; it does not prove it. Appendix C audited five mechanisms and
   missed (2.4.34).
6. Erice I is corroboration, not a literal import. Erice II's footnote 5 is an assertion.
7. No "M depends only on (λ,𝒫,m₀)" without the chain of constants and the working coordinates
   (Remark 3.3).
8. The weak-coupling region is unchanged only under Level 2+. A route that covers 𝒢 only must
   say so.
9. "29 of 61 statements conditional": once A8 is literal, reaching A8 no longer means
   conditional.
10. Methods recalled from memory are `conjectured` until read.

---

## H. Acceptance criteria and status words

**What "removed" means (ruling for Checkpoint 1).** Four conditions:
- Theorem 12.2's statement no longer says "Assume U_GJS".
- No proof cites `eq:UGJS`.
- Every import is a printed statement, used at the scope at which it is printed.
- Everything else is proved in the record.

The author must decide one point: does a printed estimate inside GJS's proof, cited at fixed h
with its hypotheses checked, count as a printed statement?
- **Standard R**: yes, as referees in the field accept. Then Level 2+ suffices.
- **Standard S**: no, only theorem statements count. Then only Level 3 removes the
  conditional.

I recommend R, with the residue stated in the text.

| outcome | Thm 12.2 | A8(vi) | Thm 5.1 | Thm 7.8 |
|---|---|---|---|---|
| today | proved, conditional on U_GJS | non-literal | proved, conditional on U_GJS | proved, conditional on U_GJS |
| R0 only | unchanged | non-literal; corroborated by Erice I (2.2.7) | unchanged | unchanged |
| P1 | proved, conditional on U_GJS; gap clause of (5) proved | non-literal; consumed only in Thm 5.1 Step 5 | proved, conditional on U_GJS | **proved** |
| core stalls after P1 | proved, conditional on U^{M2}, with A8(vi) restated | non-literal: the consumed consequence of the stated uniformity | proved, conditional on U^{M2} | proved |
| Level 2+, standard R | **proved**: A1–A8 literal, A8(vi′) = Table D.1 at fixed h | retired | proved | proved |
| Level 2+, standard S | proved, conditional on A8(vi′), a printed proof (non-literal) | retired | proved, conditional on A8(vi′) | proved |
| Level 3 | **proved**, on ε′_𝒫 = min(ε_𝒫, ε_rec) | retired | proved, with the record's own M | proved |

"Proved" always means an implication from literal imports plus the record's own proofs. Wherever
the word is used publicly, C5 (and C6) are named beside it. No word may be used before its
phase gate (D) has passed with no GAP left.

What a referee of a high-profile journal would still object to:
- **R0:** nothing changed. A lecture-note summary, with a different norm and no printed class,
  is cited for the very paper whose scope is in question.
- **P1:** the main theorem is still conditional. Simon's classes of g and 𝒫 must be checked
  against 𝒞_H and 𝒫. m₁ still comes from a 1974 theorem.
- **Stall:** acceptable as a research record that names what is missing, but not a theorem.
- **Level 2+:**
  - Citing estimates from inside a proof is trusting the proof; the text should say so.
  - Is the trace complete, given that the earlier audit missed (2.4.34)?
  - D.stab and the supplied omissions are new mathematics and need refereeing as such.
  - C5 and C6 are open.
  - ε_𝒫 is still not explicit.
- **Level 3:**
  - 40–70 pages of new expansion to referee.
  - Why import CE2 from GJS, when the new expansion could give clustering?
  - The region has changed.
  - M is no longer GJS's constant.

## I. Proportionality

**Worth the cost for this record.**
- **P1** (3–5 pp, two rounds). It makes the gap clause rest on literal imports only. It also
  shrinks the core to one observable, of degree ≤ 4p′ and spread over at most three cells, so
  no factorial bookkeeping is left.
- **P2a** (8–15 pp of tables, two rounds). It is the basis for the decision at Checkpoint 2,
  and it corrects Appendix C.
- **D.stab** (5–10 pp, two rounds). Every expansion route needs it, and it puts the record's
  own analysis exactly where h acts.

**Worth the cost because the author has decided.**
- **P2b**, if the map leaves few omissions at n = 0. My working threshold is about ten,
  each ≤ 2 pp; this is an estimate, to be revised with the map.
- **P3**, otherwise, or if the author wants a standalone paper.

**Optional.** R0; one scouting memo on other methods (R4); CE2's h-uniformity as a by-product
of a trace with general B.

**Never.** Full U_GJS; CE2's h-uniformity as a goal; dropping weak coupling; moving constants to
Erice's norm.

**Totals (estimates).**
- The recommended path (P1, P2a, D.stab, P2b, P4): 40–75 pp of finished text and tables, about
  10–12 verification rounds.
- The Level 3 path: 55–100 pp, about 12–15 rounds.

**If the core stalls,** the record should:
- integrate P1;
- restate A8(vi) as U^{M2};
- publish the map with the open steps named;
- set the KB problem `level2-h-trace` to `partial`;
- carry a title-page notice: "Theorem 12.2 is conditional on U^{M2}, a cutoff-uniform bound
  on one local observable; the uniform gap is not."

It must not call the map a proof, or the restated hypothesis literal.

## J. Deliverable form

**Documents.** The work is developed in `ugjs/`:
- `ugjs/p1/` holds the P1 note.
- `ugjs/map/` holds the map as a LaTeX table, plus one machine-readable row per display, so
  that counts can be checked by script.
- `ugjs/supplement/` holds the supplement in progress.

The final home is `part_i/supplement_D.tex`, "Supplement D to Part I: the cutoff-uniform local
interaction moment". Its gate record goes in `part_i/README.md`. `part_i/main.tex` gains an
**Appendix D** of at most 3 pp: Theorem D.1 with its quantifiers, the constant chain, the list
of imports, and a pointer to the supplement. Placed after Appendix C, it moves no existing
number. Why this form:
- Not inside `main.tex`: 20–70 pp against 40, a separate review, and stable labels.
- Not a separate paper now: a trace is not one. A Level 3 supplement could become one later,
  if the author chooses.

**Edits to `main.tex` in P1** (in place, no new numbered environment):
- Lemma 4.3(ii), proof ll. 1109–1118: A3 and Hölder.
- Lemma 7.1, ll. 1329–1351: sup over T ≥ t₀, with a constant depending on g; fix `\|le`.
- Lemmas 7.2–7.3: the U_GJS parentheticals at ll. 1363–1365 and 1402–1403 become "Lemma 7.1".
- Lemma 7.6, ll. 1504–1536: the bound for all σ ≥ 0.
- Theorem 7.7: s₀ no longer constrained.
- A4 gains item (ii), Simon V.10(iii), with its Scope, Used-in and Dossier lines.
- A8(vi), ll. 708–709: "§§5 and 7" becomes "§5"; A8's Used-in line, l. 812, likewise.
- Proposition C.7, ll. 2919–2937.
- Theorem 12.2's imports paragraph, ll. 2316–2325.
- §1.4, ll. 289–293 (density "from the factorial moments").
- Appendix A, rows K′ and Ĉ_Q.
- A dated title-page paragraph, and `\date` at l. 59.
- "Assume U_GJS" in the statements of Theorems 5.1, 11.1 and 13.2, Proposition 11.2 and
  Corollary 12.3, until P4.

**Edits to `main.tex` in P4:**
- Title-page notices: a new dated paragraph; the 16 August and 5 September paragraphs are
  kept, marked superseded.
- Abstract, ll. 93–111.
- §1.2: the quotation (ll. 157–163), table row (i) (l. 173) and the graph (l. 199).
- §1.4: ll. 278–284 and l. 342.
- A8: item (vi) marked "retired on <date>"; (vii)–(vii′) kept as history; (vi′) added under
  Level 2+; the Scope paragraph rewritten.
- Theorem 5.1, Step 5: cite Theorem D.1.
- Theorem 12.2: drop "Assume U_GJS, namely Assumption A8(vi), and"; rewrite the imports
  paragraph; under Level 3, change the region here and in §2.6.
- Appendix A: rows C₈ and M.
- Appendix B: a new corrections entry; External residue now lists C5 and C6.
- Appendix C: repair F1. Keep Proposition C.1, for its number, with a pointer to Table D.1.
  Proposition C.7 loses "Assume".
- §14, "Standing scope".
- Appendix D, new.
- `part_i/C5_reading_record.md` is unchanged (an optional item 10 for Erice I p. 161). A new
  `part_i/C6_reading_record.md` covers the traced rows.

**Outside `main.tex`:**
- `docs/status.md`: rewrite the Part I section, and redefine the "29 of 61" paragraph.
- `docs/imports.md`: the U_GJS section marked retired; "What would discharge it" becomes an
  account of how it was discharged; correct the page range.
- `docs/results.*`: regenerate with `docs/extract.py`, whose column becomes "reaches a
  non-literal import".
- `docs/index.md`, `docs/_config.yml`, the imports figure, the Status section and figure
  caption of `README.md`, and `CITATION.cff`.
- Companion: a dated notice now, saying that §4 and Figures 1–2 describe the record before
  the removal. A revised edition at P4: §4 becomes "The import that was removed"; Figure 1
  loses the dashed box; in Figure 2, Supplement D closes it.
- KB:
  - supersede `import/u-gjs`, `decision/ugjs-imported-at-source-scope` and
    `result/main-theorem-conditional`;
  - resolve `problem/level2-h-trace`, or set it to `partial`;
  - new result nodes, a correction node for F1, and reference nodes for Simon, GJ4 and
    Dimock–Glimm;
  - amend `result/hamiltonian-bypass-dead` to cite GJ4.

**Gates.** The supplement gets S0–S6, mirroring G0–G6. Under Level 2+, the step map of S1/S2
*is* Table D.1: each printed display corresponds to one row, and each environment of the
supplement to a source row or to `[new]`. Two items are added:
- S-T: completeness of the map, checked by an independent recount.
- C6: the human reading of the h-rows, open like C5.

`main.tex` re-runs G0–G6 at each integration. Page images stay in the private evidence folder,
behind the publication boundary; Table D.1 quotes short excerpts only.

## K. Plan skeleton for `ugjs/PLAN.md` (R2)

- **Part 0.** One page: what "removed" means (standard R or S); the route; the costs; the
  sentence the record uses at each stopping point.
- **Part 1.** S1 and S2: quantifiers, constants, the consumed and minimal forms, and what each
  makes proved.
- **Part 2.** What the record has and what it lacks: how far Appendix C reaches (F1), the
  n = 0 path, D.stab, the printed omissions.
- **Part 3.** The phases P0 (optional), P1, P2a, D.stab, P2b or P3, and P4. For each: owner,
  inputs, deliverable, pages, rounds, gate, fallback, status change.
- **Part 4.** Imports and sources, with the acquisition list; Dimock–Glimm first.
- **Part 5. Verification rounds:**
  - V1 (P1): mp drafts; a fresh Opus agent refutes, with Simon p. 156 on the image.
  - V2 (P2a): cqft drafts; a second agent recounts blind, page by page; the orchestrator
    settles disagreements on the image.
  - V3 (D.stab): cqft2 and mp draft; constants recomputed by hand.
  - V4 (P2b or P3): two verifiers, one for the proofs and one for "find an h-dependence the
    table missed".
  - V5 (P4): a G6-style pass, section by section.
  - Human, C6: every row of Table D.1 not marked "h absent", and every quoted omission, read
    on the images. C5 is unchanged.
  - KB review, as AGENTS.md requires.
- **Part 6.** Deliverables and the map of edits (J).
- **Part 7.** Acceptance criteria and status words (H).
- **Part 8.** Traps, and one frozen sentence for each stopping point (G).
- **Part 9.** Register of findings from all memos, with who re-checked each at the source.
- **Part 10.** Register of disagreements.
- **Part 11. The two author checkpoints.**
  - **Checkpoint 1** (after R3, before anything runs): standard R or S; P1, P2a and D.stab in
    parallel; acquire Dimock–Glimm; fix F1 now or at P4.
  - **Checkpoint 2** (after the P1 gate, the P2a gate and the D.stab attempt): P2b, P3, or
    stop; integrate P1 now, as a dated amendment, or at P4; restate A8(vi) as U^{M2} in the
    meantime; the companion's notice.
