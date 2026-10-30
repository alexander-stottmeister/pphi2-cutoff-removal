# PLAN — removing the hypothesis U_GJS from Theorem 12.2 (round R2b, editor)

Corrected after R3b (30 October 2026): items N1, N2 and n1–n14 of `r3-verifier-report.md`, section R3b, are applied.

30 October 2026. This plan was revised after the R3 verification
(`ugjs/council/r3-verifier-report.md`: 1 CRITICAL, 4 MAJOR and 20 MINOR findings), under the
orchestrator's rulings R9–R13 (`r1c-orchestrator-rulings.md`, §5). It synthesizes:
- the R1 memos in `ugjs/council/` (`memo-mp.md`, `memo-aqft.md`, `memo-cqft2.md`,
  `memo-cqft.md`, `memo-editor.md`);
- the attack memo `r1b-attack-cqft.md`;
- the orchestrator's page facts and rulings R1–R13, which bind it.

It is written for the author's approval. Nothing in it has been executed.
- Every route and every statement to be proved is `conjectured` until written and audited.
- Every page count and round count is an estimate.
- Today Theorem 12.2 is **proved, conditional on U_GJS**. It stays so until a phase's gate
  has passed and the author has approved the change.
- Numbers of the record come from `companion/council/labels.md`; lines from
  `part_i/main.tex`.
- Page facts come from r1c §§1 and 5 (read by the orchestrator on the images), from the
  verifier's report §3B (read on the images), or from the reviewed KB reference nodes.
  Anything else is marked as a memo's report.

---

## Part 0. Summary (one page)

**One standard.** The record imports printed statements and uses each at the scope at which
it is printed. A1–A7 meet this, and so does every import below. "Removed" means three things:
Theorem 12.2 no longer says "Assume U_GJS"; every import is such a statement; and everything
else is proved in the record.

**Phase 0′: the status change. It is a re-sourcing, not a proof.**
- What GJS print: the content of U_GJS as one statement, Theorem 1.1.11, (1.1.16), "uniformly
  in h" (p. 596), at B = I, n = 0 and any 0 < T < 1, inside the printed range T > 0. GJS's
  own choice in their proof of Theorem 1.1.8, T = 0 and B = I (p. 600), gives the same bound;
  p. 629 names the case "B = I, n = 0".
- After an integer time translation, it covers every sharp-time monomial at every cutoff of
  the p. 589 class, with C₈ = O(1)K₁.
- Re-basing A8(vi) on it makes A8(vi) literal, and Theorem 12.2 becomes proved from the
  literal imports A1–A8. M keeps its form. Cost: 2–3 pp of edits (estimate).
- It changes bookkeeping only. It does not change what the record trusts in GJS.

**Phases A and B: the mathematical content** (`conjectured`).
- *Form.* One note, Appendix D: 5–9 pp and two audits (estimate).
- *The comparison.* Compare dq_h with the measure of h restricted to a box of GJS squares
  around the observable; this is GJS's own device (p. 595). Squares outside the box are
  strip-separated, so CE2 as printed bounds their terms. The box term is bounded by Lemma C.2
  and Theorem C.5.
- *The two phases.* Phase A treats §7 with strips parallel to the time-zero line. Phase B
  treats (M₂) for every g, with transverse strips.
- *The trade.* The record proves that clustering implies the uniform local moment, and its
  GJS imports shrink from two theorems (1.1.7 and 1.1.11) to one (1.1.7). The price: Theorem
  1.1.7 is then used for sharp-time observables across transverse strips. That case is
  covered by its printed statement but not reached by its printed proof (p. 597); sentence
  F-T discloses it.

**Phase 0**, documentation (1–2 pp): repair Appendix C (F1), widen A8(ii), add F-T, and correct
"the only proportionate route" and the page range.

**Phase C** (optional, not scheduled) closes the transverse case. Options: C1, an isotropic
forest expansion, 45–70 pp; C2, a re-derivation of Theorem 1.1.7's printed proof, more than
31–46 pp; C3, a scouting memo, at most 5 pp.

**Frozen sentences.** These are abbreviated here; the full text is in Part 8.
- Today and after Phase 0: "Theorem 12.2 is proved, conditional on U_GJS …".
- After 0′: "Theorem 12.2 is proved from the literal imports A1–A8 …".
- After A: "… the uniform gap of Theorem 7.8 rests on GJS Theorem 1.1.7 alone …".
- After B: "… with one GJS theorem imported: Theorem 1.1.7, which is also used for sharp-time
  observables across strips transverse to the time-zero line …".
- After C: "… the uniform local moment and the transverse clustering it uses are theorems of
  the record."

**The orchestrator's recommendation (R11).** Phase 0′ now. Phase 0 now. Phases A and B as the
substantive work, at the author's choice. Phase C priced, not scheduled.

**Checkpoints.**
1. Before any edit: accept Phase 0′? Run Phases A and B? Which Phase 0 edits? Which form?
2. After the A/B audits: integrate? Phase C? Name "A8(iv)-T"? The companion?

**The council.** Three members found the comparison independently, and a fourth attacked it:
a repairable gap. A fresh verifier found the literal re-sourcing and a flaw in the plan's
first two-standard framework. The orchestrator verified the pages and issued rulings R1–R13.

---

## Part 1. The statements to prove

**Notation.** One notation is chosen; the members' names are in brackets.
- *Coordinates and squares.* Working coordinates of §2.6, z = (x⁰, x¹), time first. Squares
  are GJS's "unit lattice square[s] … centered at the lattice side [sic] j_i ∈ Z²" (p. 593).
  Δ_{l,k} is the square centred at (l, k): **row** l is time, **column** k is space.
- *Boxes.* A box B is a rectangle of squares; |B| is its number of squares, which equals its
  area. h^B := h·1_B, and h_α := h^B + α(h − h^B), α ∈ [0,1], stays in 𝒞_E.
- *Strip width.* d(Δ,R) is "the width of the widest strip bounded by two parallel lines, and
  separating" Δ from R (p. 594). If R lies in a rectangle S of squares, and m ≥ 2 is the
  sup-index distance from Δ to S, then an axis-parallel strip gives d(Δ,R) ≥ m − 1. For a
  general R the remark fails (R = {Δ_{0,0}, Δ_{0,4}}, Δ = Δ_{0,2}; verifier m2).
- *Stability constant.* S₂(B) := sup{‖e^{−𝒰_{h′}}‖_{L²(dμ₀)} : h′ ∈ 𝒞_E, supp h′ ⊆ B̄}. It is
  finite by Theorem C.5 (p = 2, Λ = B̄), and not evaluated. By translation invariance of μ₀ and
  𝒞_E it depends on B only through its shape; that sentence still has to be written
  (r1b (iii)).
- *One square's interaction.* c_U := λ Σ_{n=1}^{2p′} |a_n| K₁ K₂^{2n} n! bounds ‖U_Δ‖_GJS for
  U_Δ := λ Σ_{n≥1} a_n ∫_Δ h :Φⁿ: dz with 0 ≤ h ≤ 1. The n = 0 term is constant and has no
  covariance. [`mp` u_*; `cqft2` c_V]
- *Printed constants.* C₇ and m₁ come from Theorem 1.1.7. K₁ and K₂ ≥ 1 come from the printed
  norms (A8(iii)), with n̄ = 2p′+1 (A8(ii)). None depends on h; all are fixed by ll. 884–899.

**Statement S0′ (Phase 0′; a re-sourcing, not a proof)** [verifier M1; ruling R10].
- *Statement.* For every h in the p. 589 class (𝒞_E, A8(i)), every x⁰ ∈ ℝ, and every
  sharp-time monomial Q(x⁰) of type (1.1.5) with n_i < n̄:
  |∫Q(x⁰) dq_h| ≤ C₈ ‖Q(x⁰)‖_GJS, where C₈ := O(1)·K₁.
  Here O(1) is the constant of Theorem 1.1.11 at n = 0 and a fixed ε > 0 ("Let n and ε > 0
  be given", p. 596), and K₁ = ‖I‖ by (1.1.7) (empty product, w = 1). C₈ depends on n = 0, ε
  and the printed thresholds only, and is uniform in h and Q.
- *Derivation, to be written in the record.*
  - A general monomial is a sum of localized pieces, and its norm is the sum of theirs by
    (1.1.9). It therefore suffices to treat a localized Q(x⁰) (n4).
  - An integer time translation takes the sharp time into (−1, 0]. It maps GJS squares to
    GJS squares and leaves the norm (1.1.8) and the class of h invariant. It also transports
    dq_h, by the translation invariance of μ₀.
  - Then apply (1.1.16), "|∫(A − Q)B_T dq_h| ≤ O(1)‖A‖‖B‖e^{−γT}, uniformly in h" (p. 596),
    with B = I, n = 0 and any 0 < T < 1. This is inside the printed range: "Let B_T denote the
    translate of B at time T > 0" (p. 596). The sum Q = Σ_{0<t_j<T} Q_n(t_j) is empty because
    t_j = j ("We shall choose t_j = j, j ∈ Z"), I_T = I, and e^{−γT} ≤ 1. So
    |∫A dq_h| ≤ O(1)‖A‖‖I‖. This is the literal basis (N1).
  - GJS's own choice in their proof of Theorem 1.1.8 is T = 0: "Choose T = 0 and B = I in
    Theorem 1.1.11. Then Q = 0, so Theorem 1.1.8 is a special case of Theorem 1.1.10 [sic]"
    (p. 600). It gives the same bound, but T = 0 is the proof's value, not the statement's.
- *Consequence.* (U_GJS) holds on 𝒞_E ⊃ 𝒞_E^slab with this C₈. M keeps its form,
  M² = 9C₈𝔎(p′)λ²(Σ|a_n|)².
- *Objections the Scope paragraph must answer* (verifier M1 and R3b).
  - Is a degree-zero B "a monomial of type (1.1.5)"? p. 593 sets no restriction on r ("Since
    there is no restriction on r"), and GJS use B = I on pp. 597, 600 and 629.
  - Is "uniformly in h" uniform over the class? The record already reads Theorem 1.1.7's
    "independent of h" that way.
  - The printed proof relies on (2.4.34) (F1). That applies equally to Theorem 1.1.7.
  - T = 0 lies outside the printed T > 0. Answer: the literal basis is 0 < T < 1; p. 600's
    T = 0 is GJS's own choice and gives the same bound (N1).
  - Theorem 1.1.11 prints no smallness hypothesis; its statement says only "Let n and ε > 0 be
    given" (p. 596). GJS print the hypotheses for Theorem 4.1, from which they prove Theorems
    1.1.8 and 1.1.11 (pp. 628–629): "Let m₀, K₂ and K₁ be sufficiently large, and let λ be
    sufficiently small" (p. 628). Also p. 600: "convergence of our expansions requires both
    sufficiently small λ and sufficiently large m₀" (n3).
- *Status.* A8(vi) becomes literal. Phase 0′ does not reduce what the record trusts in GJS:
  today's U_GJS is the same mathematics, assembled from four pages, and Phase 0′ cites the one
  printed statement that carries it.

**Lemma D.1 (affine-path identity)** [`aqft` L.1; `mp` Route M step 3; `cqft2` step 1;
r1b (iv)].
- *Statement.* Let h₁, h₂ ∈ 𝒞_E, and let F be a finite sum of localized monomials of type
  (1.1.5) or (1.1.6), with kernels in L² and n_i < n̄. Then α ↦ ⟨F⟩_{h₁+α(h₂−h₁)} is C¹ on
  [0,1], and ⟨F⟩_{h₂} − ⟨F⟩_{h₁} = −∫₀¹ Cov_{h_α}(F, 𝒰_{h₂−h₁}) dα.
- *Inputs.* F ∈ L^p(dμ₀) for every p (Gaussian moments; Part 4); A3; Hölder; dominated
  convergence with the dominator |F||𝒰_{h₂−h₁}|(e^{−𝒰_{h₁}} + e^{−𝒰_{h₂}}), from convexity in
  α. No constant.

**Lemma D.2 (localized comparison)** [`aqft` L.2; `cqft2` §A; `mp` O3].
- *Statement.* Let F be as in D.1, with every piece satisfying n_i < n̄ (p. 593) and all
  localization squares in a set R. Let B ⊇ R be a box and h ∈ 𝒞_E. Assume every square
  Δ ⊄ B meeting supp h is separated from R by a strip. Then
  |⟨F⟩_h − ⟨F⟩_{h^B}| ≤ C₇ c_U ‖F‖_GJS Σ_{Δ⊄B, Δ∩supp h≠∅} e^{−m₁ d(Δ,R)}.
- Each term is (1.1.10) applied to a piece of F and U_Δ, at a cutoff of the path.
- Every application names the types of the pair, its squares, the cutoff and its membership
  in 𝒞_E, and the strip with its orientation and width (gate GA1).

**Theorem D.3 (Phase A; fixed g, parallel strips)** [`cqft2` S1; `aqft` L.4 restricted;
alternative: `mp`'s Lemmas 7.1′ and 7.6′ with Lemma L].
- *Setting.*
  - Let g ∈ 𝒞_H, let I ⊂ ℝ be a bounded interval, and let s ∈ ℝ, with l_s the row of time s.
  - N_g is the number of columns meeting supp g in positive measure.
  - B = B_s(g,I) is rows l_s−1 to l_s+1 times the smallest interval of N_B columns that
    contains every column meeting supp g ∪ I. So |B| = 3N_B.
- *Statement.* Let F be a finite linear combination of cylinder monomials (§6) supported in I,
  at sharp time s. Then for every T > 0,
  |∫F dq_{h_{T,g}}| ≤ A ‖F‖_{L²(dφ₀)} + B′ ‖F‖_GJS,
  with A := e^{3λ|a₀|N_B} S₂(B) and B′ := 2 C₇ c_U N_g e^{−m₁}(1−e^{−m₁})^{−1}.
- *Constants.*
  - A depends on (λ, 𝒫, m₀) and on N_B. It is uniform in T and s.
  - B′ depends on C₇, m₁, K₁, K₂, λ, 𝒫 and N_g. It is uniform also in the position of I.
  - Both depend on g, which is all §7 needs.
- *Why the strips are parallel.* Every square of supp h_{T,g} outside B lies in a column of
  supp g, at row distance ≥ 2 from l_s. It is separated from F by a strip parallel to the
  time-zero line, of width ≥ |l−l_s| − 1. This is the case the printed proof reaches.
- *The base term* ⟨F⟩_{h^B} is bounded by Cauchy–Schwarz, Lemma C.2 and Theorem C.5.
- *Consequences*, with proofs changed in place:
  - Lemma 7.1: sup_{T>0}‖Qψ̂_T‖² ≤ A‖Q²‖_{L²} + B′𝔫(Q)², and Ω_g ∈ D(Q).
  - Lemmas 7.2–7.3: square moments at the times s and ±t/2.
  - Lemma 7.6: E_{μ_g}[X_f^{2n}] ≤ A_f K_f^{2n}(2n)!, with A_f := A + B′K₁, K_f := max{K′, √2σ_f},
    σ_f² := ⟨f,Cf⟩. This uses ‖X_f^{2n}‖_{L²(dφ₀)} = σ_f^{2n}((4n−1)!!)^{1/2} ≤ (√2σ_f)^{2n}(2n)!
    and (8). Theorem 7.7 then has s₀ = 1/K_f.
  - Lemma 4.3(ii): only A3 and Hölder at each T (F7).

**Theorem D.4 (Phase B; uniform in g, transverse strips)** [`aqft` L.3; `cqft2` S2;
alternative `mp` Theorem 5.1′].
- *Statement.* For every h ∈ 𝒞_E, every a ∈ ℝ, and every real measurable h′ with ‖h′‖_∞ ≤ 1 and
  supp h′ ⊆ [a, a+2]:
  ∫ V(h′)(0)² dq_h ≤ M_B², where
  M_B² := e^{15λ|a₀|} S₂(B₃ₓ₅) · 9^{p′} V_* + C₇ c_U Σ₃ₓ₅ · 9 K₁ K₂^{8p′} (4p′)! λ² (Σ_n|a_n|)².
- *The quantities.*
  - B₃ₓ₅ is rows −1, 0, 1 times the at most three columns meeting [a, a+2], enlarged by one
    column on each side.
  - R is the set of localization squares of Q_V = V(h′)², which lie in row 0.
  - Σ₃ₓ₅ := Σ_{Δ⊄B₃ₓ₅} e^{−m₁ d(Δ,R)} ≤ Σ_{k≥1} (8k+12) e^{−m₁k}. Ring k around B₃ₓ₅ has 8k+12
    squares, each at strip width ≥ k: verifier's re-derivation, §3D.2. `aqft`'s bound
    (2k+3)(2k+5) is valid but cruder.
  - V_* := sup_{h′} ‖V(h′)‖²_{L²(dφ₀)} ≤ λ² Σ_n a_n² n! ∫_{−1}^{1}∫_{−1}^{1} C(x−y)ⁿ dx dy, where
    C > 0 is the kernel of (2μ)^{−1}.
  - 9^{p′} is the comparison ‖Y‖₄ ≤ 3^{p′}‖Y‖₂ from the proof of Theorem C.5.
  - The last factor bounds ‖Q_V‖_GJS (eq. (5)).
- *Constants.* M_B depends on (λ, 𝒫, m₀) through C₇, m₁, K₁, K₂ and the unevaluated
  S₂(B₃ₓ₅). It is uniform in h ∈ 𝒞_E (hence in T > 0 and g ∈ 𝒞_H), in a and in h′.
- *Where the transverse case enters.* Squares in rows −1, 0, 1 outside B₃ₓ₅ are separated from
  the time-zero observable only by strips transverse to the time-zero line (r1c §1; verifier
  §3B).
- *Consequences.*
  - Theorem 5.1 holds with M := M_B. Steps 1–4 and 6 are kept; Step 5 cites D.4 at
    h = h_{T,g}.
  - Corollary 5.2's number (362 880 C₈K₁K₂¹⁶λ²) retires.
  - The Euclidean bound implies the Hamiltonian one, and the converse holds only as T → ∞
    (`mp`, `aqft`). Lemma 10.2 consumes the Hamiltonian form, for g ∈ 𝒢 only (Lemma 3.1(iii)).
- *Alternative constant* (`mp`): a spatial box (c−4, c+4) for all times, with Lemma L, giving
  M_♯² := 9^{p′} A₈² v₂² + 9 C₇ S_* u_* 𝔎(p′) λ² (Σ|a_n|)². It uses the same transverse strips.

**Statement S3 (Phase C target)** [`cqft2` S3; `cqft` Theorem E re-targeted per r1b]. There are
ε₀(𝒫) > 0, m > 0 and C such that the following holds for λ/m₀² ≤ ε₀, every h ∈ 𝒞_E, and all
localized sharp-time or space-time monomials Q₁, Q₂ at Euclidean distance d ≥ 1:
|Cov_h(Q₁,Q₂)| ≤ C e^{−md} 𝒩(Q₁) 𝒩(Q₂).
- Here 𝒩 is a kernel norm growing at most like K^{deg} deg!.
- Status: `conjectured`. The threshold ε₀ would enter Theorem 12.2's region.

**What each phase makes proved.** These are targets. "Proved" means proved from the literal
imports and the record's own proofs. The open C5 readings are named beside the word
wherever it is used (Part 7).

| statement | after Phase 0′ | after Phase A | after Phase B |
|---|---|---|---|
| Lemma 4.3; Lemmas 7.1–7.3, 7.6; Prop 7.5; Thms 7.7–7.8; gap clause of 12.2(5) | proved (A8(vi) literal) | proved; rests on CE2 only | proved; CE2 only |
| Thm 5.1; Lemmas 10.2, 10.3, 10.5; Prop 10.4; Thm 11.1; Prop 11.2; Cor 12.3; Thm 13.2 (under Hyp 13.1) and Rem 13.3 | proved (A8(vi) literal) | proved (A8(vi) literal) | proved; rests on CE2, including its transverse case; M = M_B |
| Thm 12.2 | proved from the literal imports A1–A8 | same | same; A8(vi) retired |
| Prop C.7 | restated without "Assume" | restated | "every use of clustering is CE2 as printed" |
| A8(vi) | literal (Thm 1.1.11) | literal; used by Thm 5.1 only | retired |

*If the author declines Phase 0′*:
- Phase A makes the first row proved and leaves the second row and Theorem 12.2 "proved,
  conditional on U_GJS".
- Phase B then makes everything proved and retires A8(vi).

---

## Part 2. What the record has and what it lacks

**Theorem 1.1.11 and the 5 September 2026 reading.**
- The record already quotes (1.1.16), but only as an ingredient of Theorem 1.1.7
  (ll. 767–768).
- Its Scope paragraph (c) cites p. 629's "Theorem 1.1.8 is the special case B = I, n = 0" as
  evidence for a reading of Theorem 1.1.8 (ll. 797–799).
- The 5 September reading stopped there. It treated (1.1.16) and p. 629 as evidence for how to
  read Theorem 1.1.8, not as the import itself (R10). The two readings are the same
  mathematics with different bookkeeping.
- Phase 0′ cites the printed statement that carries the content, so U_GJS stops being
  "assembled from four pages" (ll. 802–803).

**Appendix C and its reach.** Appendix C audits five mechanisms of GJS §§2–4 (M1–M5) and proves
two h-uniform facts: Lemma C.2 (normalisation) and Theorem C.5 (stability), with Lemmas C.3–C.4.
Proposition C.1 is "deliberately limited to the audited mechanisms" (ll. 2729–2745).
- **Finding F1 (MAJOR).** These sentences are false about the source:
  - M1, l. 2677: "No Gaussian expectation, no e^{−U}, no h appears in the norm";
  - M3, l. 2699: "the single point where h touches a quantitative estimate";
  - M4, ll. 2708–2709: "(by M5, no constant of the source depends on it)";
  - M5, ll. 2725–2727: "no stability estimate, enters any constant of the proof";
  - Remark C.6, ll. 2914–2916.
- **What the source shows.**
  - (2.4.34), p. 624, "1 ≦ ‖e^{−V(Y)}‖_{L₂(dΦ_C)} ≦ e^{K₃|Y|}", is a stability bound under
    the interpolated measures, cited to Dimock–Glimm. It fixes "K₂ ≧ K₃²" (Lemma 2.4.6,
    p. 622), and so every downstream constant.
  - V(Y) carries h (V(Yh), p. 601).
  - The kernels behind the norm (2.4.3) contain integrals of e^{−V(Y_j)} ((2.3.4), (2.3.8),
    pp. 611–612).
- **What survives.** Proposition C.1, by its limitation clause. Theorem 12.2 does not consume
  Appendix C, so no theorem changes.
- **Who read it.** `cqft`, `editor` and the orchestrator read pp. 622 and 624 on the images
  (the orchestrator's reading is recorded in r1c §5). The verifier confirmed the finding at
  pp. 601, 611–612, 622 and 624.

**What Theorem C.5 supplies, and what it does not.**
- *Supplies:* for every p < ∞ and compact Λ, sup{‖e^{−𝒰_h}‖_{L^p(dμ₀)} : h ∈ 𝒞_E,
  supp h ⊆ Λ} < ∞. With Lemma C.2's Z(h) ≥ e^{−λ|a₀||Λ|}, this is exactly the base term of D.3
  and D.4.
- *Does not supply:*
  - a bound under GJS's interpolated covariances;
  - growth e^{K|Λ|} linear in the volume, which (2.4.34) needs;
  - an evaluated constant, so M stops being explicit after Phase B;
  - the translation-invariance sentence (r1b (iii)).
- *Load-bearing.* Lemmas C.2–C.4 and Theorem C.5 become load-bearing in Phases A and B.
  `cqft` and the verifier re-read C.5's chain and found no error. The independent audit GA4
  is still required.

**The transverse case** (r1c §1; verifier §3B).
- *What the statement says.* Theorem 1.1.7 (p. 594) is printed for "two localized monomials Q₁
  and Q₂, with disjoint localization squares", with d "the width of the widest strip bounded by
  two parallel lines". No orientation is prescribed. The record writes "(any orientation)"
  (l. 673).
- *What the proof reaches.* The printed proof (p. 597) runs "After rotating and translating
  the strip … choosing A = Q₁, B_T = Q₂ in Theorem 1.1.11". Theorem 1.1.11 takes "monomials of
  type (1.1.5)", localized at times ≤ 0 and ≥ 0 (p. 596). A sharp-time monomial rotated by 90°
  has a fixed spatial position and integrated times, so it is neither (1.1.5) nor (1.1.6).
  Hence the printed proof reaches sharp-time pairs only across strips parallel to the
  time-zero line, the only case Lemma 7.4 uses.
- *Space-time monomials.* Monomials of type (1.1.6) are reached in any orientation, after
  slicing, under the multi-time reading of (1.1.5). That reading rests on p. 595, "In the
  monomial Q(x₀) of (1.1.5), suppose x₀ = (x_{1,0}, ···, x_{r,0})", and on p. 596, "localized
  at times x_{i0}" (m9). This is how GJS's own use on p. 595 is covered.
- *A second assertion of the case.* Erice I Theorem 2.2.1 (pp. 160–161) asserts the case,
  "uniformly in h" with d = dist, and leaves the proof to the Annals and to Erice II.
- *What the record says today.* "needs no separate scope discussion" (ll. 2661–2663; F12).
- *Even the parallel case.* The printed proof reaches it only through Theorem 1.1.8 at the
  same h (p. 597). This is why the record has a single standard (Part 7).

**Lattice.** GJS squares are centred at lattice sites (p. 593). The record counts in cells
[j, j+1) (ll. 438, 1188, 1296). The counts are invariant, but the boxes of Appendix D must be
built from GJS's squares (F3).

**What the record lacks:**
- the literal re-sourcing (Phase 0′);
- a written comparison (D.1–D.4);
- the disclosure F-T;
- an audit of Lemmas C.2–C.5 as load-bearing results;
- a citation for Lemma C.4's "classical Bessel facts", l. 2838 (F13);
- a proof of the transverse case (Phase C).

---

## Part 3. The phases

Every phase is `conjectured` until written and audited. Page counts are estimates. Following
R12, no gate waits for a human MATCHES verdict. Gates check only that the C5 checklist items
exist, with their pages and the text to confirm.

### Phase 0: documentation (before any mathematics; R4)
- **Owner.** The orchestrator applies the edits after Checkpoint 1; the editor drafts the
  sentences.
- **Inputs.** F1, F3, F4, F5, F11, F12 (Part 9); r1c §1; verifier §3B.
- **Deliverable in `main.tex`.**
  - Appendix C: the F1 sentences qualified (l. 2677, l. 2699, ll. 2708–2709, ll. 2725–2727,
    ll. 2914–2916).
  - A new mechanism M6: stability under the interpolated measures, (2.4.34)–(2.4.35), and the
    e^{O(Vol)} convergence factor.
  - Proposition C.1's description narrowed; M2's "Dirichlet" made "decoupled", with M1's
    e^{τt} corrected (F11).
  - A8(ii) widened to name (1.1.6) and the square convention (F3).
  - The A8(iv) Scope gains F-T (Part 8; F12). If Phase 0′ is also approved, this edit and
    Phase 0′'s rewrite of the same Scope paragraph (main.tex l. 779) are made in one pass (n13).
  - An Appendix B corrections entry.
- **Deliverable elsewhere.**
  - `docs/imports.md`, l. 56 ("only proportionate route") and l. 57 (page range 600–631).
  - The KB nodes `problem/level2-h-trace` and `result/hamiltonian-bypass-dead`.
  - A dated note in `strategy.md` and in `part_i/README.md`.
  - The companion's correction notice for §4 (`s4-import.tex`, from l. 73).
- **Estimate.** 1–2 pp of edits; one round (V0).
- **Gate G-0.**
  - Three pdflatex runs: 0 errors, 0 undefined, 0 Overfull (AGENTS §7.1).
  - `pdftotext main.pdf - | grep -nE '\?\?|TODO'` empty.
  - Every changed page rendered and inspected (G5).
  - The `.aux` diff shows all 125 labels unmoved.
  - A fresh reader checks each changed sentence against the page image it describes.
  - The status of U_GJS is unchanged, and the text says so.
- **Fallback.** None needed.
- **Status change.** None.

### Phase 0′: re-base A8(vi) on Theorem 1.1.11 (R10; the status change; no proof)
- **Owner.** The orchestrator applies the edits after Checkpoint 1. The editor drafts. `mp`
  checks the translation step.
- **Inputs.** GJS pp. 596, 597, 600 and 629 (the orchestrator re-read pp. 596 and 600 on the
  images, r1c §5; the verifier read all four); A8(i)–(iii); C5 items 2, 9 and 12.
- **Deliverable in `main.tex`.**
  - A8(vi) re-based. An unnumbered source fact, `srcfactstar` like (vii′), so that no number
    moves, quotes verbatim:
    - p. 596: "Let B_T denote the translate of B at time T > 0"; Theorem 1.1.11, with
      (1.1.14)–(1.1.16), "uniformly in h", and "We shall choose t_j = j, j ∈ Z". The literal
      basis is (1.1.16) at B = I, n = 0 and any 0 < T < 1 (N1);
    - p. 600, as GJS's own choice giving the same bound: "Choose T = 0 and B = I in Theorem
      1.1.11. Then Q = 0", with "Theorem 1.1.10" marked [sic] (9b).
  - The integer time translation is written out, and C₈ := O(1)K₁.
  - The Scope paragraph, ll. 779–809, is rewritten, in one pass with Phase 0's F-T (n13). It
    states the one standard and the re-sourcing. It says why the 5 September reading stopped
    short, and that the two readings are the same mathematics. It replaces Scope (b) (F8) and
    answers the five objections of S0′.
  - A8(v) (CE1) and (vii)–(vii′) stay, as corroboration.
  - Theorem 12.2, l. 2295: "Assume U_GJS, namely Assumption A8(vi), and" is deleted. The
    imports paragraph, ll. 2316–2325, is rewritten.
  - Proposition C.7 (ll. 2919–2939) loses "Assume".
  - Title page: a new dated paragraph; earlier paragraphs kept, marked superseded. `\date`
    (l. 59) is updated, as on 5 September 2026.
  - Abstract (ll. 93–111); §1.2 (ll. 157–163, 173, 199); §1.4 (ll. 278–284, 342); Appendix B
    External residue (ll. 2639–2648); Appendix C introduction (ll. 2653–2663).
  - §2.6, ll. 887–888: ε_𝒫 is reworded to name the hypotheses of the theorems imported (m11).
    For Theorem 1.1.11 GJS print them with Theorem 4.1 (p. 628) and on p. 600 (n3).
- **Deliverable elsewhere.**
  - `docs/status.md`, `docs/imports.md`, `docs/index.md` and `docs/_config.yml`; the Status
    section of `README.md`; `CITATION.cff`; `docs/results.*` regenerated.
  - KB: `import/u-gjs` (now literal, through Theorem 1.1.11), the decision node superseded,
    and `result/main-theorem-conditional` superseded.
  - The companion's status notice (m20).
- **Estimate.** 2–3 pp of edits; one round (V0′).
- **Gate G-0′.**
  - The page facts of pp. 596 and 600 are quoted verbatim in the new source fact, each with a
    `% src:` comment.
  - C5 items 2, 9 and 12 and a new item 13 (p. 600) exist in `part_i/C5_reading_record.md`,
    with page, image and the text to confirm; item 2 includes p. 593's "Since there is no
    restriction on r", item 12 p. 596's "B_T … at time T > 0" (n11).
  - The Scope paragraph is rewritten as listed.
  - `grep -n -i 'assum[a-z]*[^.]*U_{\\rm GJS}' part_i/main.tex` prints nothing. Today it finds
    ll. 93, 157, 2295 and 2921 (n12).
  - The `.aux` labels are unchanged: 125 labels, same numbers.
  - Three pdflatex runs clean, with the checks of G-0.
  - A fresh agent checks every quotation against the image and every status sentence
    against Part 7.
- **Fallback.** If the author declines, or V0′ finds the reading wrong (for instance that
  "monomials of type (1.1.5)" excludes degree zero), A8(vi) stays as today. Part 7's note for
  a declined 0′ then applies.
- **Status change.** Theorem 12.2 becomes proved from the literal imports A1–A8 (Part 7).

### Phase A: §7 at fixed g (D.1, D.2, D.3; parallel strips; R1)
- **Owner.** `aqft` drafts `ugjs/comparison.tex`, Part A. `mp` drafts D.1 and the fallback.
  `cqft2` drafts the strip geometry and the constants.
- **Inputs.** A3; A4 (through Theorem C.5); A8(i)–(iv); Lemma C.2; Theorem C.5; Lemmas
  4.1–4.4; Proposition 6.2; Remark 6.3; Lemma 7.4; the Gaussian moments (Part 4). No new
  import.
- **Deliverable.** D.1, D.2 and D.3, and the replaced proofs of Lemmas 4.3, 7.1–7.3, 7.6 and of
  Theorem 7.7.
- **Estimate.** 3–5 pp; audited together with Phase B, two rounds.
- **Gate GA** (in the style of G0–G6).
  - **GA1.** Every use of (1.1.10) names Q₁ and Q₂ with their types (n_i < n̄), their squares,
    the cutoff with its membership in 𝒞_E, and the strip with its orientation (here
    *parallel*) and width. A second agent re-derives each.
  - **GA2.** The integrability chain of D.1 cites only A3, Lemma C.2, Theorem C.5, the
    Gaussian moments of F, Hölder and dominated convergence, with every exponent written.
  - **GA3.** A, B′, A_f and K_f are recomputed by hand (G3 style) and entered in Appendix A.
  - **GA4.** An independent audit of Lemmas C.2–C.4 and Theorem C.5, including the
    translation-invariance sentence.
  - **GA5.** No proof in §§4, 6, 7 cites `eq:UGJS`.
  - **GA6.** A written check that A, B′, Ĉ_Q and s₀ appear in no statement of §§8–14.
  - **GA7.** A G6-style adversarial pass with zero unresolved findings.
  - **GA8.** The C5 checklist contains items 1–4 and 10, with pages and text.
- **Fallback.** `mp`'s Lemma L, which changes Lemma 7.1's statement to T ≥ t_* := 1/m₀.
  - L(i), the L²→L⁴ bound, is proved in-house from A2 and A4, or cited as Simon p. 156,
    Theorem V.10(iii).
  - L(iii) also needs Theorem C.5 (for Z_N) and a Jensen–Chebyshev step that `mp` checked
    only numerically (`numerical`). That step must be proved.
  - If this also fails, §7 keeps its present input.
- **Status change.** Part 7.

### Phase B: (M₂) for every g (D.4; transverse strips)
- **Owner.** Same note, Part B. `aqft` drafts, `cqft2` does the constants, `mp` the quantifiers.
- **Inputs.** As for Phase A, plus A8(iv) in its transverse case, at the scope at which its statement is printed
  (F-T).
- **Deliverable.** D.4, and Theorem 5.1 with M := M_B (Step 5 replaced). Corollary 5.2 is
  recomputed or retired, its number kept. F-T appears at every transverse application.
- **Estimate.** 2–4 pp, plus about 2 pp of edits for A and B together.
- **Gate GB.**
  - GA1–GA7 for the transverse uses, each flagged in the text.
  - **GB1** (R13). Run `grep -n -e 'U_{\\rm GJS}' -e 'UGJS' -e 'C_8' part_i/main.tex`. The
    surviving hits, written in the gate record as line ranges of the edited file, must be
    exactly these (today's lines in brackets; verifier N2):
    - the title-page notices, kept marked superseded (ll. 68, 72, 76, 81);
    - A8(v), as provenance (l. 685);
    - A8(vi), marked retired, with its tag and label kept for provenance (ll. 693–708);
    - A8(vii′), as provenance (l. 722);
    - the Scope paragraph's history sentences (ll. 796, 800);
    - Appendix B's corrections history and External residue (ll. 2631, 2643);
    - Appendix C's introduction, as history (ll. 2654, 2660);
    - Corollary 5.2 (l. 1247), if it is kept rather than restated with M_B.

    Any other hit fails the gate. The notation table (l. 436), §2.6 (l. 897) and eq. (5)
    (l. 1214) must no longer hit; Part 6 lists their edits. Also,
    `grep -c 'Assume \$U_{\\rm GJS}' part_i/main.tex` must print 0.
  - **GB2** (R12). The C5 checklist contains items 1–4 and 10–13, with pages, images and the
    text to confirm. The status sentences name them as open.
  - **GB3.** Appendix A's M rows are rewritten. M contains S₂, which is unevaluated, and
    Appendix A says so.
- **Fallback.** If GA1 fails for a transverse application, Phase B is not integrated. The
  record stays at Phase A, with Theorem 5.1 still resting on A8(vi) (Theorem 1.1.11 after
  Phase 0′).
- **Status change.** Part 7.

### Integration of Phases A and B (after Checkpoint 2)
- The note becomes Appendix D of `main.tex`, with the edits of Part 6.
- **Gate GI.**
  - G0–G6 are re-run.
  - The G1/G2 step maps gain rows for Appendix D and for every changed proof (source
    `ugjs/comparison.tex`).
  - The `.aux` diff shows all 125 labels unmoved, plus the new D-labels.
  - `labels.md` and `docs/results.*` are regenerated.
- **Fallback** (m15). If GI fails, the integration commit is not made, and `main.tex` keeps
  its state before integration. The note stays in `ugjs/`, and the status stays at the last
  integrated phase.

### Phase C: close the transverse case (optional; priced, not scheduled; R3)
- **C1. Isotropic forest-formula expansion** (`cqft2` M1).
  - Method: Brydges–Kennedy / Abdesselam–Rivasseau interpolation, a polymer expansion, and
    per-square stability from Theorem C.5.
  - It proves S3 in every orientation.
  - Estimate: 45–70 pp, 4–6 rounds.
  - Risk: the tree sum with local factorials.
- **C2. Re-derive the printed proof of Theorem 1.1.7**, including the rotated sharp-time
  case.
  - This is `cqft`'s Route E1, re-targeted as r1b requires.
  - Estimate: more than 31–46 pp.
  - It needs `cqft`'s Lemma S, an h-uniform stability bound linear in |Y| under the
    decoupled covariances. Lemma S is either proved or taken from Dimock–Glimm, which would
    have to be acquired.
- **C3. Scouting memo** (≤ 5 pp) on the orchestrator's conjecture: an energy-weighted moment
  obtained from the concavity of the ground-state energy and a g-uniform local energy-shift
  bound. The one printed g-uniform shift bound on disk, GJ4 Theorem 1.1 (J. Math. Phys. 13
  (1972), p. 1569), assumes 0 ≤ 𝒫(ξ)g(x) + 𝒫₁(ξ)h(x) ((1.7), p. 1568; the editor's reading of
  the image, not checked by the verifier). That condition excludes negative perturbations
  where g = 0, and the memo must address this first.
- **Gate GC.**
  - G0–G6 pass.
  - Every constant is derived, and the tree and polymer constants are recomputed
    independently by hand.
  - The transverse case is covered explicitly.
  - Theorem 12.2's region is restated if ε₀ < ε_𝒫.
- **Fallback.** The status reached after Phase B stands.
- **Status change.** The transverse use of A8(iv) rests on a theorem of the record. A8(iv)
  stays imported for Lemma 7.4's parallel case, unless Lemma 7.4 is also re-based on S3.

---

## Part 4. Imports and sources

| statement | source | status | read; human item |
|---|---|---|---|
| Theorem 1.1.11, (1.1.16), "uniformly in h", at B = I, n = 0 and any 0 < T < 1 (printed range T > 0) | GJS p. 596; GJS's own choice T = 0 (p. 600) gives the same bound; "B = I, n = 0" named p. 629 | literal; it becomes A8(vi) in Phase 0′ and is retired after Phase B | orchestrator (r1c §5), verifier; C5 items 2, 9, 12, 13 |
| Theorem 1.1.7, (1.1.10): constants "independent of h, Q₁ and Q₂"; strip of any orientation | GJS p. 594, A8(iv) | literal; the transverse use is disclosed (F-T) | r1c §1, verifier; C5 items 4, 11 |
| (1.1.5)–(1.1.6), "localized", squares centred at lattice sites, n_i < n̄; multi-time reading | pp. 593, 595, 596 (A8(ii), to be widened) | literal | r1c §1, verifier; C5 items 2, 10 |
| norms (1.1.7)–(1.1.9) | p. 594, A8(iii) | literal | C5 item 3 |
| cutoff class: compact support, 0 ≤ h ≤ 1 | p. 589, A8(i) | literal | KB verified claim, verifier; C5 item 1 |
| dilation | p. 590, A8(viii) | literal | KB verified claim; C5 item 4 |
| finite-volume stability | Simon Thm V.7, A3 | literal | unchanged |
| hypercontractivity | Simon Thm I.17, A4 | literal | used through Theorem C.5 |
| FKN; simplicity | A2; A1 | literal | unchanged |
| Lemma C.2, Lemmas C.3–C.4, Theorem C.5 | the record | proved; load-bearing in A and B | audit GA4 |
| Gaussian moments of F, Wick orthogonality, positivity and local integrability of Cⁿ | elementary | to be written out, about 0.25 p | — |

After Phase 0′, A8(v) (Theorem 1.1.8, CE1) and (vii)–(vii′) become corroboration. After
Phase B, A8(vi) and Theorem 1.1.11 are no longer used.

**Alternative for Phase A** (`mp`'s Lemma L), read on the images by `mp`:
- Simon's book, p. 156, "THEOREM V.10", statement (iii);
- its proof, item (iv), p. 158;
- P(t) = exp(−tH(g)), V.12(c), p. 159;
- the hypotheses of §V.3, p. 155: g ∈ L^{1+ε} ∩ L¹, g ≥ 0.

The book cross-references this theorem as "Theorem V.11 (iv)" (p. 167; text layer only). Its
statement has ‖F_{(0,t)}‖_r, its proof ‖F(0,t)‖_{r′}; record both verbatim.

**Phase C sources.** None is on disk; the bibliographic data are from memory and unverified.
- *C1, to acquire* (`cqft2`):
  1. Brydges–Kennedy (1987);
  2. Abdesselam–Rivasseau (1995), "Trees, forests and jungles";
  3. Kotecký–Preiss (1986), or Brydges' Les Houches course (1984);
  4. a Gaussian Hölder inequality of Brascamp–Lieb type, or a proof of it from A4;
  5. Glimm–Jaffe, *Quantum Physics*, the cluster-expansion chapter;
  6. Rivasseau (1991).
- *C2, to acquire only if C2 is chosen and Lemma S is cited rather than proved:*
  Dimock–Glimm, Adv. Math. 12 (1974) 58–83, GJS ref. [1] (p. 631). Erice II p. 236 reports
  that [1] assumes "C ∈ ℬ^loc_{q,δ(q)}".
- *On disk, unread:* GRS 1975, Parts 1–2; Simon §VIII.3; GJ III, Acta Math. 125 (1970).

**Not routes** (`cqft2`, from memory): Boué–Dupuis, stochastic quantization, correlation
inequalities. None is known to the council to be uniform over [0,1]-valued measurable
cutoffs. They are not to be acquired.

**Erice I (2.2.7) and Theorem 2.2.1** (KB reference node) are corroboration only.

**KB reference nodes missing:** Simon (only if Lemma L is cited), GJ4 (if C3 runs), and
Dimock–Glimm (if acquired).

---

## Part 5. Verification rounds and human readings

**Rounds.** In each round the drafter is not the verifier.
- **V0** (Phase 0) and **V0′** (Phase 0′): one fresh agent checks every changed sentence and
  quotation against the page image and `labels.md`, and every status sentence against Part 7.
- **V1** (note, first audit):
  - `cqft` audits as attacker. It reads GJS on the images and has already re-checked
    Theorem C.5's chain.
  - `mp` audits the quantifiers and D.1.
  - Every finding is dispositioned in writing.
- **V2** (note, second audit): a fresh Opus agent that drafted nothing makes a G6-style pass,
  instructed to refute. One strand covers the geometry and constants, the other the
  integrability chain and Steps 5–6.
- **V3** (Lemmas C.2–C.4, Theorem C.5): an agent that did not write them audits them as
  load-bearing results. The author's own line-by-line check follows (the README lists human
  verification as ongoing).
- **V4** (integration): gate GI; `labels.md` and `docs/` regenerated; the KB review that
  AGENTS.md requires.
- **V5** (Phase C, if run): two verifiers, one for the proofs and one for the constants by
  hand, plus a human reading of any source table.

**Human readings** (R12). These are user-level open items, as C5 is today. They are named as
open beside every status word, and no gate waits for them; gates check only that the items
exist with pages and text. The checklist is `part_i/C5_reading_record.md`:
- **items 1–4** (pp. 589, 590, 593, 594): load-bearing in every phase. Item 2 is extended to
  quote p. 593's "Since there is no restriction on r", which Phase 0′ needs (n11);
- **items 5–8**: corroboration once Phase 0′ re-bases A8(vi);
- **item 9** (pp. 596–597, including (1.1.16) "uniformly in h"): load-bearing for Phase 0′,
  together with items 2 and 12 (n11);
- **new item 10** (pp. 593 and 595): (1.1.5) and (1.1.6) verbatim; "localized" defined for
  both; squares "centered at the lattice side [sic]"; and p. 595's
  "x₀ = (x_{1,0}, ···, x_{r,0})" (m9);
- **new item 11** (p. 594): Theorem 1.1.7's "two localized monomials … with disjoint
  localization squares" and "the widest strip bounded by two parallel lines", with no
  orientation prescribed;
- **new item 12** (pp. 596–597): Theorem 1.1.11's "monomials of type (1.1.5)", localized at
  times ≤ 0 and ≥ 0; "Let B_T denote the translate of B at time T > 0"; and the rotation
  sentence. F-T rests on these, and so does Phase 0′ (degree-zero B; T > 0);
- **new item 13** (p. 600): "Proof of Theorem 1.1.8, assuming Theorem 1.1.10 [sic]. Choose
  T = 0 and B = I in Theorem 1.1.11. Then Q = 0"; Phase 0′ cites it as GJS's own choice (N1).

The orchestrator and the verifier have read the content of items 9–13 on the images (r1c §§1
and 5; verifier §3B). The verdicts belong to the human reader.

---

## Part 6. Deliverable form and the map of edits

**Form** (editor's decision; R5).
- Phases 0 and 0′ are edits only; Part 3 lists them.
- Phases A and B form one note, `ugjs/comparison.tex`. After Checkpoint 2 it is integrated as
  a new **Appendix D** of `part_i/main.tex`, after Appendix C: D.1–D.4 with full proofs, cited
  by the changed proofs in §§4, 5 and 7.
- *Why an appendix.*
  - D.1–D.2 serve both phases, and Phase C would attach there too.
  - The audit boundary is a single document.
  - The 61 numbered statements become 65, and no number from 2.1 to C.7 moves.
- *Alternatives not taken.*
  - `mp`'s Lemma 4.5 keeps all numbers too, but splits the argument across §§4 and 5.
  - A separate supplement or paper is disproportionate at 5–9 pp.

**Phase A edits at integration** (in place):
- Lemma 4.3(ii), ll. 1109–1118: A3 and Hölder.
- Lemma 7.1, ll. 1329–1351: the D.3 bound; `\|le` at l. 1349 fixed.
- Lemmas 7.2–7.3: ll. 1363–1365 and 1402–1403 cite D.3.
- Lemma 7.6, ll. 1504–1536: A_f, K_f, radius 1/K_f; and Theorem 7.7's s₀.
- §1.4, ll. 290–293: the density sentence (F9).
- A8(vi), ll. 708–709: "§§5 and 7" becomes "§5". A8's *Used in*, ll. 811–812.
- Theorem 12.2's imports paragraph, ll. 2316–2325.
- Appendix A: rows K′ and Ĉ_Q; new rows A, B′, A_f, K_f, S₂ and c_U.
- A3's *Used in* gains Appendix D.
- A dated title-page paragraph and `\date`.

**Phase B edits at integration:**
- Theorem 5.1: M becomes M_B (ll. 1156–1167); Step 5 (ll. 1218–1228) cites D.4. Corollary 5.2
  is restated with M_B or retired, its number kept.
- Step 4's eq. (5), l. 1214, ends "= M²/C₈", which is false once M = M_B. The bound on
  ‖Q_V‖_GJS stays; "= M²/C₈" is deleted (n14).
- The notation table (l. 436, "K_1, K_2, C_7, C_8, m_1") and §2.6 (l. 897, "C_7, C_8, K_1, K_2
  denote the printed constants") drop C₈ (N2).
- A8(vi) is marked "retired on <date>". (v)–(vii′) go to provenance. The Scope paragraph
  (ll. 779–809) adds F-T in its integrated form.
- Theorem 12.2's imports paragraph (ll. 2316–2325) names one GJS theorem. "Assume" is already
  gone after Phase 0′; if Phase 0′ was declined, it is deleted here.
- Proposition C.7 (ll. 2919–2939): "every use of clustering is CE2 as printed", with the
  orientations stated.
- **"Explicit" rate** (m10). M, and hence Ψ_{m₁}, now contain the unevaluated S₂. The
  abstract's "explicit super-polynomial rate" (l. 100) and §1.2's "An explicit rate holds"
  (l. 160) gain the qualifier "explicit up to the finite constant of Theorem C.5".
- **ε_𝒫** (m11). §2.6, ll. 887–888, which defines ε_𝒫 through "the Glimm–Jaffe–Spencer
  expansion is valid at bare mass M_*", is reworded to name the printed hypotheses of the
  theorems actually imported: Theorems 1.1.7 and 1.1.11 after Phase 0′, Theorem 1.1.7 after
  Phase B. Theorem 1.1.11's statement prints none; GJS print them with Theorem 4.1, "Let m₀,
  K₂ and K₁ be sufficiently large, and let λ be sufficiently small" (p. 628), and on p. 600
  (n3).
- Appendix A: the M rows; C₈ dropped; a note that the M in Ψ and in C_{N,γ,M} has changed.
- Appendix B: a corrections entry; External residue lists C5 items 1–4 and 9–13.
- §14 "Standing scope" (l. 2546).
- The statements without "Assume U_GJS" (F6) become moot.

**Outside `main.tex`.**
- `docs/status.md`: the Part I section and the "29 of 61" paragraph. Reachability of A8
  stops meaning "conditional"; recompute against `eq:UGJS`, or retire the index (`aqft` G12).
- `docs/imports.md`; `docs/results.*` regenerated by `docs/extract.py` with the column
  redefined; `docs/index.md`; `docs/_config.yml`; the imports figure; `README.md` (Status and
  the figure caption); `CITATION.cff`. These are changed at Phase 0′ and again at integration.
- **KB.**
  - At Phase 0: the F1 correction node, and the two "only proportionate route" nodes.
  - At Phase 0′: `import/u-gjs` re-based; `decision/ugjs-imported-at-source-scope` and
    `result/main-theorem-conditional` superseded.
  - At integration: results for D.1–D.4; a problem node for the transverse case (Phase C)
    replacing `problem/level2-h-trace`; `problem/c5-second-reader` amended for items 10–13.
- **Companion: three notices, each dated** (m20):
  1. Phase 0's correction notice for §4 (`s4-import.tex` from l. 73: "the only proportionate
     route", the page range).
  2. Phase 0′'s status notice: its §1 claims ledger, §4 and Figures 1–2 describe the record
     before the re-sourcing.
  3. The integration notice: Appendix D now carries the moment bound.

  A revised edition follows only when the author decides: §4 retitled, Figure 1's violet
  class removed, Figure 2 historical, "Theorem 12.2 does not consume it" reversed.
- **Gates.** The note carries GA and GB; integration carries GI. The orchestrator's separate
  README keeps the record of rounds.

**Corrected locators** (verifier m13):
- Scope paragraph: ll. 779–809.
- A8 *Used in*: ll. 811–812.
- Proposition C.7: ll. 2919–2939.
- "classical Bessel facts": from l. 2838.
- Remark C.6: ll. 2914–2916.
- companion `s4-import.tex`: from l. 73.
- Theorem 12.2(5): ll. 2308–2314.

---

## Part 7. Acceptance criteria and the status table

**Acceptance.**
- A status word below may be used only once the gate of the phase that produces it has passed,
  with no GAP left. Phases A and B also need gate GI.
- Wherever "proved" appears in public text (README, `docs/`, CITATION.cff, the companion), the
  open human readings (C5 items 1–4 and 9–13, Part 5) are named beside it. No gate waits for
  them (R12).
- Today Theorem 12.2 is "proved, conditional on U_GJS". It changes only when a gate has passed
  and the author has approved (R8).

**One standard** (R9). The record imports a printed statement and uses it at the scope at which
it is printed. That is the standard of A1–A7. Phase 0 changes no entry of the table. The
columns are cumulative.

| | today | after Phase 0′ | after Phase A | after Phase B | after Phase C |
|---|---|---|---|---|---|
| Thm 12.2 | proved, conditional on U_GJS | **proved** | proved | proved | proved |
| Thm 7.8; gap clause of 12.2(5) | proved, conditional on U_GJS | proved | proved; rests on Thm 1.1.7 alone (parallel strips) | same | same |
| Thm 5.1; moment clause of (5); Lemma 10.2 onward | proved, conditional on U_GJS | proved; rests on Thm 1.1.11 | same | proved; rests on Thm 1.1.7, including its transverse case; M = M_B | proved; transverse use by the record's own theorem |
| A8(vi) | non-literal, assembled | literal (Thm 1.1.11, B = I, n = 0, 0 < T < 1) | literal; Thm 5.1 only | retired | retired |
| A8(iv) use | parallel strips (Lemma 7.4) | same | parallel strips (Lemma 7.4, D.3) | both orientations, disclosed by F-T | parallel only; the transverse case is a theorem of the record |
| **GJS theorems imported** | Thm 1.1.7; U_GJS assembled from Thm 1.1.8 and pp. 594–597, 629 | Thms 1.1.7, 1.1.11 | Thms 1.1.7, 1.1.11 | Thm 1.1.7 | Thm 1.1.7, parallel case (none, if Lemma 7.4 is re-based on S3) |

In every column the record also imports printed GJS statements that are not theorems:
A8(i)–(iii) (the p. 589 class, the p. 593 observables, the p. 594 norms) and A8(viii) (the
p. 590 dilation) (n9).

"Proved" means proved from A1–A8, each a printed statement at its printed scope, and from the
record's own proofs, including Lemmas C.2–C.5 from Phase A on. Two cautions apply:
- The record does not re-verify any import's proof, exactly as for A1–A7. In particular,
  CE2's printed proof takes its constant from Theorem 1.1.8 at the same h (p. 597).
- The open readings are named beside the word.

*If the author declines Phase 0′:*
- Theorem 12.2, Theorem 5.1 and the moment clause stay "proved, conditional on U_GJS" until
  Phase B.
- Theorem 7.8 and the gap clause become proved at Phase A.
- A8(vi) stays non-literal until Phase B retires it.
- The imported statements are today's until Phase B, and then Theorem 1.1.7 alone.

**Why "proof-reached scope" cannot be the record's standard** (R9; verifier C1). Suppose an
import counted only where its printed proof reaches. Then A8(iv) itself would count at no
cutoff other than h → 1. Its printed proof obtains its constant from Theorem 1.1.8 "at the
same h" (p. 597), and Theorem 1.1.8 is printed "uniformly as h → 1" (p. 595). Lemma 7.4, and
with it Theorem 7.8, would then be conditional today on an h-uniform Theorem 1.1.8. There are
two ways to avoid this, and neither keeps proof-reached scope a second standard (n6):
- Trusting that use of Theorem 1.1.8 for Theorem 7.8 while declining it for Theorem 5.1 is the
  asymmetry the record rejected on 5 September 2026 (`strategy.md` ll. 2250–2252).
- Reading the h-uniform Theorem 1.1.8 off a printed statement is the one standard itself
  (Phase 0′).

Hence there is one standard. The transverse case stays a disclosure (F-T), not a second
standard.

**The optional name "A8(iv)-T"** (R9; verifier M4).
- *What it is.* For transparency, the author may name the transverse case as a separate item,
  A8(iv)-T: transverse clustering of sharp-time monomials at every h ∈ 𝒞_E.
- *What it is not.* It is not a different standard, and it is not a narrower form of U_GJS.
  A8(iv)-T and U_GJS are different statements, and neither is known to imply the other
  (n7): U_GJS is a moment bound on the slab class and states no clustering. With Appendix C, A8(iv)-T gives
  bounds A‖F‖_{L²} + B′‖F‖_GJS, with A growing with the observable's box, not C₈‖F‖_GJS for
  all F.
- *What it does.* It is one case of a printed theorem statement that its printed proof does
  not reach. Together with the literal imports, it yields everything §5 consumes.

**The trade of Phases A and B after Phase 0′** (R11). After Phase 0′, Phases A and B are not
needed for the status of Theorem 12.2. They are the mathematical content of the removal:
- *Gains.* The record proves that clustering implies the uniform local moment (D.1–D.4), so
  the moment bound becomes a theorem of the record and not an import. The GJS theorems
  imported shrink from two (Theorems 1.1.7 and 1.1.11) to one (Theorem 1.1.7).
- *Cost.* That one statement is used in its transverse case for the sharp-time observable, a
  case its printed proof does not reach (F-T).
- Phase A alone uses only strips in the time direction.
- *The orchestrator's recommendation* (R11, recorded as the orchestrator's): Phase 0′ now;
  Phase 0 now; Phases A and B as the substantive work, at the author's choice; Phase C priced,
  not scheduled.

**What a referee of a high-profile journal would still object to.**
- *After Phase 0:* nothing has changed in substance, and the record says so honestly.
- *After Phase 0′:*
  - It is a re-sourcing, not a proof: the record still trusts GJS's printed argument exactly
    as before.
  - Why did the record call U_GJS "assembled from four pages" when one printed theorem
    states it? The answer is recorded (Part 2).
  - Is degree-zero B admissible in (1.1.16)? Answered in the Scope paragraph (S0′).
- *After Phase A:* the gap rests on Theorem 1.1.7 alone, a 1974 theorem.
- *After Phase B:*
  - The transverse use must be disclosed prominently.
  - M contains the unevaluated constant of Theorem C.5.
  - Lemmas C.2–C.5 are load-bearing new mathematics and need refereeing.
  - The human readings are open.
- *After Phase C:*
  - 45–70 pages of new expansion to referee.
  - A possibly different weak-coupling region.
  - Why the parallel case is still imported, if S3 could replace it.

---

## Part 8. Traps and frozen sentences

**Frozen sentences.** Each is used verbatim at its first mention in each document.
- **F-T** (in the A8(iv) Scope from Phase 0 on; R2, R9): "GJS Theorem 1.1.7 is printed for
  localized monomials separated by a strip of any orientation (p. 594). Its printed proof
  rotates the strip into the time direction (p. 597) and so reaches sharp-time monomials only
  across strips parallel to the time-zero line. Lemma 7.4 uses only that case[; Appendix D
  also uses the transverse case, at the printed statement's scope]."
  - The bracketed clause is added at integration.
  - If the author names A8(iv)-T (Checkpoint 2), the bracket instead reads "[; Appendix D
    also uses the transverse case, listed separately as A8(iv)-T]" (m7).
- **F-0** (today, after Phase 0, and if Phase 0′ is declined and Phase A stalls): "Theorem 12.2
  is proved, conditional on U_GJS (Assumption A8(vi)), which is imported at the scope at which
  the source states and uses it and is not re-derived."
- **F-0′:** "Theorem 12.2 is proved from the literal imports A1–A8. Its moment input A8(vi) is
  GJS Theorem 1.1.11, (1.1.16), at B = I, n = 0 and any 0 < T < 1 (p. 596), the case GJS
  name on p. 629 and specialize to T = 0 in their proof of Theorem 1.1.8 (p. 600); the record
  does not re-derive the cluster expansion."
- **F-A** (Phase 0′ and Phase A): "Theorem 12.2 is proved from the literal imports A1–A8; the
  uniform gap of Theorem 7.8 rests on GJS Theorem 1.1.7 alone, and GJS Theorem 1.1.11 is used
  only for the local moment of Theorem 5.1."
- **F-A\*** (Phase A with Phase 0′ declined): "Theorem 12.2 is proved, conditional on U_GJS,
  which it now uses only for the local moment of Theorem 5.1; the uniform gap of Theorem 7.8
  rests on GJS Theorem 1.1.7 alone."
- **F-B:** "Theorem 12.2 is proved from printed statements only, with one GJS theorem
  imported: Theorem 1.1.7, which is also used for sharp-time observables across strips
  transverse to the time-zero line, a case its printed statement covers and its printed proof
  does not reach. The uniform local moment is a theorem of the record (Appendix D)."
- **F-C:** "Theorem 12.2 is proved from printed statements only; the uniform local moment and
  the transverse clustering it uses are theorems of the record."

**Traps.** Each item gives the wording to avoid, then the wording to use, with its source.
1. Not "U_GJS is proved". After Phase 0′ write "A8(vi) is imported literally, as GJS Theorem
   1.1.11"; after Phase B, "A8(vi) is no longer used; Theorem D.4 proves the bound Theorem 5.1
   needs, from A8(iv) and Appendix C". (`aqft`, `cqft2`, `editor`)
2. Not "Phase 0′ removes the dependence on GJS" or "Phase 0′ proves the moment bound". Write:
   "a re-sourcing, not a proof; the record trusts GJS's printed argument as before". (R10)
3. Not "U_GJS was wrongly imported until now". Write: "the same mathematics, with different
   bookkeeping". (R10)
4. Not "Theorem 12.2 is unconditional". Use the frozen sentence for the stopping point, with
   the open readings named. (all)
5. Not "no longer depends on the h-uniformity of the GJS expansion". Write: "no longer imports
   U_GJS; it imports Theorem 1.1.7, whose printed proof takes its constant from Theorem 1.1.8
   at the same h (p. 597)". (`mp`, `cqft`, `cqft2`, `editor`)
6. Not "proof-reached scope" as a standard of the record (R9). Not "A8(iv)-T is narrower than
   U_GJS": they are different statements, neither known to imply the other (M4; n7).
7. Not "the note verifies GJS's uniformity". Write: "derived from the printed statement; none
   of GJS's proofs is verified". (`cqft2`, `cqft`, `editor`)
8. Not "CE1 follows from CE2". Write: "for observables of bounded support, with constant
   A‖F‖_{L²} + B′‖F‖_GJS". (`cqft2`)
9. Not "the slab bound is equivalent to (M₂)". Write: "it implies (M₂)". (`mp`, `aqft`)
10. Not "M depends only on (λ, 𝒫, m₀)". Add "through C₇, m₁, K₁, K₂ and the unevaluated
    constant of Theorem C.5, in working coordinates (Remark 3.3)". Not "M is unchanged":
    after Phase B it is M_B, and 362 880 C₈K₁K₂¹⁶λ² retires. (`mp`, `aqft`, `editor`)
11. Not "Lemma 10.2 needs g-uniformity or the net is not Cauchy". Write: "growth polynomial in
    r_j suffices; dependence on |supp g| does not". (`mp`, `aqft`, `editor`)
12. Not "Appendix C is supporting evidence", or "not consumed". From Phase A on, Lemma C.2 and
    Theorem C.5 are load-bearing. (`mp`, `aqft`)
13. Not "Appendix C shows the constants are h-independent". Write: "it audits five mechanisms;
    (2.4.34) lies outside them". (`cqft`, `editor`)
14. Not "Theorem C.5 is the stability estimate GJS need": it holds under dμ₀ only, for fixed Λ,
    without linear growth. (`cqft`)
15. Not "GJS insert Dirichlet boundary conditions": GJS decouple,
    C_Y = YCY + (1−Y)C(1−Y) (p. 600). (`cqft`)
16. Not "Erice I makes U_GJS literal", or "Erice II's footnote 5 shows h is harmless". Write:
    "corroboration; assertion". (all)
17. Not "Phase B removes weak coupling": D.4 needs CE2. (`mp`, `editor`)
18. Not "(M₂) can be weakened to uniform L^{1+δ}", or "the gap controls the local moment".
    Write: "neither is established". `aqft` cites `m4/h6.tex` Theorem 3.2 and Lemma 3.4 for the
    first, and Propositions 2.1–2.2 for the second (m14).
19. Not "the Expositions p. 57 problem is solved", or "GRS Problem 1 is settled": (M₂) is weaker
    than either. (`mp`, `aqft`)
20. Not "the comparison works for any cutoff". It works for h ∈ 𝒞_E only, using h ≥ 0 and
    h ≤ 1 (Remark C.6). (`aqft`)
21. Not "the count of statements reaching A8 drops to zero": recompute the index or retire it.
    (`aqft`, `editor`)
22. Not "modern methods give the uniform moment": none is known to the council to be uniform
    over [0,1]-valued cutoffs (from memory). (`cqft2`)
23. Not "a trace of GJS can confirm the transverse case": the printed proof does not cover it.
    (`cqft2`, r1b)
24. Not "Simon Theorem V.11". Write: "Theorem V.10, p. 156, statement (iii)", recording the
    source's r against r′. (`mp`)
25. Not "Lemma 7.6's radius is intrinsic": it is an artefact of the GJS-norm route. (`mp`)
26. Never swap "uniformly as h → 1" (p. 595) for "uniform in h" (p. 629) or for (1.1.16)'s
    "uniformly in h" (p. 596), or the reverse. Quote each where it is printed. (`cqft`; m19)
27. Record source misprints verbatim; never correct them silently (Part 9b). (`cqft`)
28. No sentence may say a phase is done before its gate record exists.

---

## Part 9. Findings register (deduplicated; none applied by the council; R7)

### 9a. About the record

| ID | locator | finding | sev. | found by | confirmed at the source |
|---|---|---|---|---|---|
| F1 | App C: M1 l. 2677, M3 l. 2699, M4 ll. 2708–2709, M5 ll. 2725–2727, Rem C.6 ll. 2914–2916; Prop C.1's description; `m4/r1-check.tex` abstract item (2) | Says no stability estimate enters GJS's constants; (2.4.34), p. 624, cited to Dimock–Glimm, fixes K₂ ≥ K₃² (Lemma 2.4.6, p. 622) | MAJOR (no theorem affected) | `cqft`, `editor` | images of pp. 622, 624: `cqft`, `editor` and the orchestrator (30 October; r1c §5); the verifier at pp. 601, 611–612, 622, 624 and in the record's lines |
| F2 | l. 1349 | `\|le` prints "le" for ≤ | MINOR | `mp`, `aqft`, `cqft2`, `cqft` (`editor` noted) | four members; `aqft` on the rendered page; the verifier in the TeX source |
| F3 | ll. 438, 1188, 1260, 1296–1305, 1452 | Cells [j, j+1) against GJS squares centred at lattice sites (p. 593); counts unchanged, but Appendix D must use GJS squares | MINOR | `mp`, `aqft`, `cqft2`, `cqft` | orchestrator (r1c §1); verifier |
| F4 | `docs/imports.md` l. 56; KB `problem/level2-h-trace`, `result/hamiltonian-bypass-dead`; companion `s4-import.tex` ll. 73–75 | "The only proportionate route … is a display-by-display trace": unsupported | MINOR | `mp`, `aqft` | verifier |
| F5 | `docs/imports.md` l. 57; `strategy.md` ll. 2235, 2275; `part_i/README.md` l. 155; companion l. 75; KB problem node | Range "pp. 598–629"; the argument runs to p. 631 (Thm 4.1: "we do not give the details", p. 628) | MINOR | `editor` (and companion register F21) | verifier (incl. pp. 628, 631) |
| F6 | statements of Thms 5.1, 7.8, 11.1, 13.2, Prop 11.2, Cor 12.3 | Lack "Assume U_GJS" though their proofs consume it | MINOR (moot after 0′) | `aqft` (companion register F3) | verifier (all six) |
| F7 | Lemma 4.3(ii), ll. 1109–1118 | Credits square-moment finiteness at each T to U_GJS; A3 and Hölder suffice | MINOR | `editor` | verifier |
| F8 | A8 Scope (b), ll. 790–796 | "consistency therefore requires …": importing CE2's statement commits the record to nothing about Thm 1.1.8. Under the one standard (R9) the repair stands; Phase 0′ rewrites the paragraph | MINOR | `editor`, `cqft` (r1b) | verifier (as a description) |
| F9 | §1.4, ll. 290–293 | "proved from the factorial moments of Source Fact 2.3": the moments come from Lemma 7.1, hence from U_GJS | MINOR | `mp` | verifier |
| F10 | A4 Scope, l. 553 | "Thms V.10, V.12": Simon prints Proposition V.10 (p. 155) and Theorem V.10 (p. 156), and cites the latter as V.11 | MINOR | `mp` | verifier (images of pp. 155–156; "V.11 (iv)" from the text layer) |
| F11 | M2 l. 2683; M1 l. 2676 | "Dirichlet-on-contours", but GJS decouple, C_Y = YCY + (1−Y)C(1−Y) (p. 600). e^{τt} for the printed e^{γt} (p. 613). (2.4.4) is script 𝒦₂ (p. 615) | MINOR | `cqft` | verifier (all three); `editor` (p. 600) |
| F12 | l. 673 "(any orientation)"; ll. 2661–2663 "needs no separate scope discussion" | The transverse case is not disclosed | MINOR now; load-bearing in Phase B | `cqft2`, `cqft` (r1b) | orchestrator (r1c §1); verifier |
| F13 | Lemma C.4, from l. 2838 | "classical Bessel facts" uncited; load-bearing once C.4 is | MINOR | `editor` | verifier |
| F14 | l. 780 | "uniformly as h↑1"; GJS print "h → 1" (p. 595) | MINOR | companion register F18 (`cqft`) | `editor`, verifier |

### 9b. About the sources

These are recorded verbatim by any trace, never corrected silently.

| locator | what is printed | reported by; confirmed |
|---|---|---|
| GJS p. 593 | "centered at the lattice side [sic]" | orchestrator; verifier |
| GJS p. 593 | "Δ_{j_1} × ··· × Δ_{j_n} ⊂ R^{2r}": index n against r (m19) | verifier |
| GJS p. 597 | "n = 0 in Theorem 1.1.11 Then Q", without a period. r1c §1 and the record (l. 760) insert one silently (m19) | verifier |
| GJS p. 600 | "Theorem 1.1.10" twice, where the specialization is of Theorem 1.1.11 | `cqft`; orchestrator ("[sic]", r1c §5); verifier |
| GJS (2.0.5), p. 601 | a spurious ∫₀¹ ds | `cqft`; verifier |
| GJS p. 611 | cites "(2.0.1)" for (2.0.2) | `cqft`; verifier |
| GJS (2.4.34), p. 624 | "1 ≤" holds by Jensen only for a₀ ≤ 0 (`cqft`'s computation; verifier checked only the direction); the display omits the denominator of (2.3.8), p. 612 | `cqft`; verifier (denominator) |
| Erice II p. 237 | "K₁₀" for K₁₂ | `cqft`; verifier |
| Simon pp. 156 and 158 | statement ‖F_{(0,t)}‖_r against proof ‖F(0,t)‖_{r′}; cross-referenced as "Theorem V.11 (iv)" | `mp`; verifier |

---

## Part 10. Disagreements and how they were ruled

| # | question | positions | ruling |
|---|---|---|---|
| D1 | Can a comparison from CE2 deliver U_GJS's content (O3)? | `cqft`, `editor`: no; the regress does not close (both considered paths between general cutoffs). `mp`, `aqft`, `cqft2`: yes, with a box reference cutoff | **R1**: the box comparison is the core. `cqft` withdrew its verdict (r1b); the editor's concerned the other path |
| D2 | Instrument for §7 at fixed g | `mp`: Lemma L. `editor`: Simon V.10(iii). `aqft`, `cqft2`: box comparison | **R1**: box comparison with parallel strips; Lemma L as fallback |
| D3 | Is the transverse use of A8(iv) a literal import? | `mp`, `aqft`: literal. `cqft2`: a status change only. r1b: a repairable gap | **R2, R9**: literal under the one standard, disclosed by F-T; optional name A8(iv)-T |
| D4 | Is the slab bound equivalent to (M₂)? | brief O2 and the `editor` memo: yes. `mp`, `aqft`: implies only | **Editor**: implies only; the editor's memo held only as T → ∞ (trap 9) |
| D5 | Target of an expansion route | `cqft`: B = I branch of Thm 1.1.8. `cqft2`: isotropic forest. `editor`: Level 2+ | **R3** with r1b: Phase C targets the transverse case of Thm 1.1.7 (S3) |
| D6 | Erice re-sourcing | all: corroboration | **Editor**: Erice may be cited as corroboration in the Scope, never in a status sentence |
| D7 | Deliverable form | `mp`: Lemma 4.5. `aqft`: Appendix D. `editor` memo: supplement | **Editor (R5)**: Appendix D (Part 6) |
| D8 | Lemma 7.6's radius | `mp`: every s. `cqft2`: radius 1/K_f | **Editor**: a finite radius suffices for Theorem 7.7 |
| D9 | Which C5 items carry weight | `aqft`: 1–4. `mp`: new 10–11. `cqft2`: pp. 593–597. `cqft`: 5, 6, 9 | **Editor, after R10**: 1–4 always; 2, 9, 12 and 13 for Phase 0′; 10–12 for A/B; 5–8 corroboration |
| D10 | Write A and B together? | `mp`: jointly, gated separately. `cqft2`: B at the author's choice | **R1**; Checkpoint 1, question 3 |
| D11 | Base term of Phase B | `aqft`, `cqft2`: a 3×5 box. `mp`: spatial box with Lemma L | **Editor**: 3×5 box; `mp`'s constant as alternative |
| D12 | Status of Thm 7.8 after Phase A | `cqft`: "conditional on A8(iv)". `mp`, `aqft`: "proved". The R2 plan: "proved under both standards" | **R9**: one standard; "proved" (after Phase 0′ already). The phrase "under both standards" is withdrawn |
| D13 | Level 3 / expansion at all | `mp`, `aqft`: not for this goal. `cqft2`: M1. `cqft`: E3 as fallback | **R3**: Phase C, optional, priced |
| D14 | Severity of F1 | MAJOR (all) | no disagreement |
| D15 | Two standards (statement scope against proof-reached scope; verifier C1) | the R2 plan: the author chooses. Verifier: proof-reached scope breaks Table 2 or rests on an undisclosed asymmetry | **R9**: one standard (A1–A7's); proof-reached scope cannot be the record's (Part 7); Table 2 removed |
| D16 | U_GJS as a literal import through Theorem 1.1.11 (verifier M1) | the R1 memos and the R2 plan did not examine it. Verifier: (1.1.16) with B = I is the printed statement of U_GJS's content | **R10**: adopted as Phase 0′, a status change and not a proof. **R11**: Phases A and B become the substantive derivation, with the trade stated (Part 7) |

---

## Part 11. The two author checkpoints

**Checkpoint 1** (after re-verification, before any edit; R6, R10, R11). The author is asked:
1. **Phase 0′.** Accept Phase 0′ as the status change? That is: re-base A8(vi) on GJS Theorem
   1.1.11, (1.1.16) at B = I, n = 0 and any 0 < T < 1 (p. 596; the case is named on p. 629,
   and GJS's own T = 0 on p. 600 gives the same bound), so that Theorem 12.2 is proved from
   the literal imports A1–A8. It is a re-sourcing, not a proof.
1′. **Phases A and B.** Run them as the substantive derivation? The trade (Part 7): the
   record proves the moment bound, and its GJS imports drop from two theorems to one, at the
   cost of the disclosed transverse use of Theorem 1.1.7. The orchestrator recommends:
   Phase 0′ now; Phase 0 now; Phases A and B at the author's choice; Phase C priced, not
   scheduled.
2. **Phase 0.** Which of these edits may the orchestrator apply?
   - (a) the F1 repair with M6;
   - (b) A8(ii) widened;
   - (c) F-T in the A8(iv) Scope;
   - (d) "the only proportionate route" in `docs/imports.md` and the two KB nodes;
   - (e) the page range;
   - (f) the companion's correction notice;
   - (g) the Appendix B entry.
3. **Phases A and B together.** If 1′ is yes: one note with two theorems, audited twice (R1)?
   Or Phase A alone first?
4. **Deliverable.** Appendix D, as recommended, or `mp`'s Lemma 4.5?
5. **Human readings.** Who reads C5 items 1–4 and 9–13, and when? When does the author check
   Lemmas C.2–C.5, which become load-bearing in Phases A and B?

**Checkpoint 2** (after gates GA and GB, before integration). The author is asked:
6. **Integration.** Integrate Appendix D and the edits of Part 6 as a dated amendment, with a
   new `\date`?
7. **Phase C.** None; the scouting memo C3 only; C1, with the acquisitions of Part 4; or C2,
   with Dimock–Glimm to acquire?
8. **A8(iv)-T.** Name the transverse case as a separate item, for transparency? It is not a
   standard (Part 7), and F-T then takes its bracketed variant.
9. **Companion.** The integration notice now, and a revised edition (§4, Figures 1–2) when?
10. **Records.** Update `docs/`, the README, CITATION.cff and the KB in the same commit as the
   integration, or separately?
