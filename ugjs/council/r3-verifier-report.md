# R3 verifier report on `ugjs/PLAN.md`

30 October 2026. A fresh verifier (Opus) that wrote none of the memos and none of the plan.
I read all 803 lines of `ugjs/PLAN.md`, the R3 brief, `BRIEF.md`, `r1c-orchestrator-rulings.md`
and the memos (background only). Every check below was made against `part_i/main.tex` (by line
number), `companion/council/labels.md`, and the page images under `<scratch>` (printed page =
NN + 583 for `gjs74/`, NN + 131 for `erice1/`, NN + 198 for `erice2/`). Every route of the
plan is still `conjectured`. My re-derivations in section 3 check the plan's sketches; they are
not proofs.

## 1. Verdict

**Not yet.** The comparison argument (D.1–D.4) survives the attack and needs only minor
repairs. But the status framework the author is asked to decide at Checkpoint 1 has two
problems. First, its "proof-reached scope" either breaks Table 2 or rests on an undisclosed
asymmetry (C1). Second, it never examines a literal re-sourcing of U_GJS through GJS Theorem
1.1.11 that could make Phases A–B unnecessary (M1). Revise Parts 0, 1, 3, 5, 7, 8, 10 and 11
and re-verify those parts before the author sees the plan.

Counts: **CRITICAL 1, MAJOR 4, MINOR 20.**

## 2. Findings

### CRITICAL

**C1. "Proof-reached scope" is applied to the transverse case but not to the parallel case.
Table 2 and ruling D12 follow from the plan's definition only under an unstated, asymmetric
reading.**
- *Locators.* Part 0 ll. 27–33 and l. 46; Part 1 table ll. 179–189; Part 5 ll. 468–469;
  Part 7 ll. 599–612; Part 9 F8 l. 726; Part 10 D12 l. 765.
- *Sentences.*
  - l. 46: "It removes U_GJS from Lemma 4.3, Lemmas 7.1–7.3 and 7.6, Proposition 7.5 and
    Theorems 7.7–7.8, under both standards."
  - l. 599: "Table 2: proof-reached scope (an import counts only where its printed proof
    reaches)."
  - ll. 610–612: "CE2's printed proof takes its constant from Theorem 1.1.8 at the same h
    (p. 597). The record does not re-verify it, exactly as for A1–A7."
  - l. 765 (D12): "**Editor**: 'proved', since A8(iv) is literal and the parallel case is
    reached by the printed proof under both standards".
- *What is wrong.* The printed proof of Theorem 1.1.7 reaches even the *parallel* case only
  through Theorem 1.1.8 at the same h.
  - p. 597 (image): "the proof follows from Theorem 1.1.8, (1.1.16) and the above
    determination of Q". There Q is fixed "From the choice B = I" in Theorem 1.1.11.
  - p. 595 (image): Theorem 1.1.8 is printed "uniformly as h → 1".
  - So at a general cutoff in 𝒞_E the reduction needs an h-uniform Theorem 1.1.8. Today
    (Lemma 7.4 at h_{T,g}) that is the content of U_GJS on the slab class. After Phase A it
    is more: D.3 applies CE2 at the non-slab path cutoffs h^B + α(h_{T,g} − h^B).

  The definition admits three readings of "reaches".
  - **(H0)** The printed proof is trusted together with its own uses of its ingredients.
    This includes Theorem 1.1.8 "at the same h". It is the only reading under which Table 2
    comes out as written. But it trusts, for Theorem 7.8, the very uniformity it declines to
    import for Theorem 5.1. That is the asymmetry the record rejected on 5 September 2026
    (`strategy.md` ll. 2250–2252: "it accepted the h-uniform conclusion of p. 597 while
    declining the h-uniform premise consumed there"; KB decision node, "What was
    rejected"). Under H0, keeping U_GJS a hypothesis rests on statement-literalness, which
    is a criterion of the *other* standard.
  - The two consistent readings, H1 and H2, each break Table 2:
    - **(H1)** The reduction counts as reaching a case when the theorems it cites hold there as
      printed. Then the h-uniform Theorem 1.1.8 must be read off a printed statement: (1.1.16)
      "uniformly in h" with B = I (p. 596). GJS make exactly this specialisation on pp. 600
      and 629. The same reading makes U_GJS's content a printed statement that its printed
      proof explicitly covers (p. 629: "Theorem 1.1.8 is the special case B = I, n = 0").
      Table 2's ladder (U_GJS conditional until Phase B, A8(iv)-T conditional until Phase C) is
      then beaten by a Phase-0 re-sourcing (M1).
    - **(H2)** "Reaches" requires the cited theorem's printed statement to cover the use. Then
      the parallel case at h ≠ 1 is not reached either.
      - Lemma 7.4 and Theorem 7.8 are "proved, conditional on the h-uniform Theorem 1.1.8
        consumed on p. 597". This is `cqft`'s position in D12.
      - Phase A makes that hidden premise *larger*: all of 𝒞_E instead of the slab class.
      - Table 2's "proved" is then wrong for Theorem 7.8 after A, and for Theorem 12.2 after C.
        After C, Lemma 7.4 still imports the parallel case (Part 3 ll. 386–388).

  The record already contains the H2 argument: A8 Scope (b), main.tex ll. 790–796,
  "consistency therefore requires the constant of Theorem 1.1.8 to be uniform on the same
  class, which is (U_GJS)". Finding F8 (l. 726) would rewrite that sentence. The rewrite is
  right under statement scope and wrong under proof-reached scope. Part 5 l. 468 calls C5
  items 5–6 (Theorem 1.1.8; p. 629) "history"; under H2 they stay load-bearing.
- *Repair.*
  - Define proof-reached scope as H0, H1 or H2 in Part 0 and Part 7.
  - If H0, disclose the asymmetry beside Table 2 and at Checkpoint 1 question 1.
  - Then redo Table 2, D12, the third column of the Part 1 table, l. 46, F8 (make its repair
    depend on the standard) and Part 5 l. 468.
  - Under H2, the Table 2 columns after Phase A carry the h-uniform Theorem 1.1.8 on 𝒞_E as
    a condition, and Phase A is not progress under that standard. Today's column already
    carries U_GJS, which covers Lemma 7.4's slab cutoffs.
  - Under H1, the plan must present M1.

### MAJOR

**M1. The plan never examines the printed statement of Theorem 1.1.11 as a literal source of
the h-uniform moment bound.**
- *Locators.* Part 0 l. 27 ("There is one judgement call."); Part 4 ll. 394–409 (no row for
  Theorem 1.1.11); Part 11 ll. 774–778 (Checkpoint 1, question 1).
- *What the source prints* (images).
  - p. 596, before Theorem 1.1.10: "We let A and B denote monomials of type (1.1.5) of degree
    |A| and |B| … We assume that A is localized at times x_{i0} ≦ 0, and that B is localized
    at times x_{i0} ≧ 0. Let B_T denote the translate of B at time T > 0".
  - Theorem 1.1.11: "(1.1.15) Q = Σ_{0<t_j<T} Q_n(t_j) satisfies (1.1.16)
    |∫(A − Q)B_T dq_h| ≦ O(1)‖A‖‖B‖e^{−γT}, uniformly in h. We shall choose t_j = j, j ∈ Z."
  - With B = I and 0 < T < 1 the sum is empty. (1.1.16) then reads |∫A dq_h| ≤ O(1)‖A‖‖I‖,
    uniformly in h, where ‖I‖ = K₁ by (1.1.7) (empty product, w = 1).
  - GJS make this specialisation themselves, three times:
    - p. 597: "From the choice B = I, it follows that Q = ∫A dq_h + O(1)‖A‖e^{−m₀(1−ε)T}";
    - p. 600: "Proof of Theorem 1.1.8 … Choose T = 0 and B = I in Theorem 1.1.11. Then
      Q = 0";
    - p. 629: "Theorem 1.1.8 is the special case B = I, n = 0".
  - An integer time translation preserves the lattice, the norm and 𝒞_E. After one, the
    bound covers every sharp-time (1.1.5) monomial at every h of the p. 589 class. That
    includes U_GJS, with C₈ = O(1)K₁.
- *Why it matters.*
  - Under statement scope ("Every import is a printed statement, used at its printed scope",
    l. 24), this would make A8(vi) literal by re-sourcing. That is a Phase-0-sized edit,
    needs no transverse case, and keeps M in its present form, 9C₈𝔎(p′)λ²(Σ|a_n|)².
  - Under proof-reached scope, this is the case GJS's printed proof names (p. 629), which
    the transverse case is not.
  - A referee, and the author at Checkpoint 1, will ask why U_GJS is still "assembled from
    four pages" (main.tex ll. 802–803; KB `decision/ugjs-imported-at-source-scope`) when one
    printed theorem states it.
  - Neither the plan nor the record addresses this. The record quotes (1.1.16) only as an
    ingredient of Theorem 1.1.7 (ll. 767–768).
- *Objections the ruling must weigh.*
  - Is a degree-zero B "a monomial of type (1.1.5)"? p. 593 sets no restriction on r, and
    GJS use B = I three times.
  - Is "uniformly in h" in (1.1.16) uniform over the class? The record reads Theorem 1.1.7's
    "independent of h" that way, and the plan relies on that reading.
  - The proof's reliance on (2.4.34) (F1) applies equally to Theorem 1.1.7.
- *Repair.*
  - Before Checkpoint 1, the orchestrator rules on this reading.
  - The plan adds the option ("Phase 0′: re-source A8(vi) to (1.1.16) with B = I and
    0 < T < 1") to Part 0, Part 4, both tables of Part 7, and Checkpoint 1 question 1.
  - If accepted, it says what Phases A–B still buy: one GJS theorem fewer, and M taken from
    CE2 and Appendix C.
  - If rejected, it says why, and applies the same reason to Theorem 1.1.7.

**M2. Gate GB1's grep cannot see the hypothesis it is meant to detect.**
- *Locator.* Part 3 ll. 342–343: "GB1. Theorem 12.2 and Proposition C.7 no longer contain
  'Assume U_GJS'. `grep -n 'UGJS\|C_8' part_i/main.tex` hits provenance lines only."
- *What is wrong.*
  - main.tex typesets the hypothesis as `$U_{\rm GJS}$`. The pattern matches only the label
    `eq:UGJS` and `C_8`.
  - Run today it hits 36 lines and misses 18 of the 19 lines carrying `U_{\rm GJS}`. Among
    the misses:
    - both "Assume $U_{\rm GJS}$" lines (2295, 2921);
    - the abstract (93, 108), §1.2 (157, 173, 199) and §1.4 (280);
    - Theorem 12.2's imports paragraph (2317, 2325);
    - Appendix B (2643) and Appendix C (2654, 2660).
  - The gate would pass with "Assume U_GJS" still in place.
  - "Hits provenance lines only" is a judgement, not a count.
  - The pattern is inherited from `aqft` GL5.
- *Repair.*
  - Use `grep -n -e 'U_{\\rm GJS}' -e 'UGJS' -e 'C_8' part_i/main.tex`, and write the
    expected surviving lines into the gate.
  - Add `grep -c 'Assume \$U_{\\rm GJS}' part_i/main.tex`, which must print 0.

**M3. The human readings are a gate in Part 3 and an open caveat in Parts 7 and 8.**
- *Locators.*
  - l. 344–345: "GB2. C5 items 1–4 and the new items 10–12 (Part 5) read MATCHES before any
    status word changes"; l. 351: "If GA1 or GB2 fails, U_GJS is kept".
  - ll. 583–584: "Wherever the word 'proved' appears in public text …, the open human
    readings C5 items 1–4 and 10–12 are named beside it."
  - l. 623: "(d) The human readings are open."
  - ll. 660–661: "with the open readings named".
- *What is wrong.*
  - If GB2 holds, the readings are closed before "proved" is first used. Part 7's "open
    human readings" and referee objection (d) then cannot arise.
  - If Part 7 is what is meant, GB2 is not a gate.
  - GB2 also says "before any status word changes". Yet gate GA has no reading condition,
    although Phase A changes a status word (Theorem 7.8 → proved). Phases A and B are thus
    held to different standards without saying so.
- *Repair.* Decide whether the readings gate status changes.
  - If yes: put the condition in both GA and GB, and delete "open" in ll. 584, 623 and 661.
  - If no: make GB2 "recorded, and named as open beside every status word", and make the
    fallback at l. 351 independent of it.

**M4. "A8(iv)-T … strictly narrower than U_GJS" is unsupported.**
- *Locators.* Part 1 ll. 187–189 ("Under proof-reached scope it is a named hypothesis,
  strictly narrower than U_GJS"); Part 7 l. 607 ("named hypothesis, narrower than U_GJS");
  Part 0 l. 32 ("a narrower named hypothesis").
- *What is wrong.* A8(iv)-T and U_GJS are different statements.
  - A8(iv)-T is transverse clustering of sharp-time monomials at every h ∈ 𝒞_E. U_GJS is a
    moment bound on the slab class.
  - The plan shows no implication in either direction. U_GJS gives no clustering.
  - A8(iv)-T with Appendix C gives a bound A‖F‖_{L²} + B′‖F‖_GJS, in which A grows with the
    observable's box (trap 5, ll. 667–668). That is not C₈‖F‖_GJS for all F.
  - Under H2 of C1, A8(iv)-T is not the only premise left either.
- *Repair.* State what is true: a *different* named hypothesis. It is one case of a printed
  theorem statement that its printed proof does not reach, in place of an interface
  assembled from four pages. Together with the literal imports it yields everything §5
  consumes.

### MINOR

- **m1. D.3 overstates the uniformity of its constant A.** Part 1 ll. 129–130 say "Both are
  uniform in T > 0, in s and in the position of I." But A depends on N_B (l. 129), which
  grows with the distance from I to supp g. Harmless, since §7 fixes I. *Repair:* "A is
  uniform in T and s; B′ is uniform also in the position of I."
- **m2. The strip-width remark is false for a general set R.** Notation, ll. 90–92: "If the
  sup-index distance is m ≥ 2, an axis-parallel strip gives d(Δ,R) ≥ m − 1."
  Counterexample: R = {Δ_{0,0}, Δ_{0,4}}, Δ = Δ_{0,2}. The sup-index distance is 2, and no
  strip separates Δ from R. The remark holds when R lies in a rectangle S and m is the
  distance from Δ to S, which is how D.3 and D.4 use it. *Repair:* say so.
- **m3. D.2 omits the degree bound n_i < n̄.** D.2 (ll. 111–117) does not require the pieces
  of F to satisfy n_i < n̄. That is a standing condition of the class on p. 593 ("We assume
  a bound on the n_i in (1.1.5), n_i < n̄"). D.3 and D.4 satisfy it, since their degrees are
  ≤ 1 and ≤ 2p′ < n̄ = 2p′ + 1.
- **m4. Two symbols in the statements to prove are undefined.**
  - A_f (l. 137). My computation from D.3 gives A_f = A + B′K₁, using
    ‖X_f^{2n}‖_{L²(dφ₀)} = σ_f^{2n}((4n−1)!!)^{1/2} ≤ (√2σ_f)^{2n}(2n)! together with (8).
  - Σ₃ₓ₅ (ll. 146, 151). It should be defined as Σ_{Δ⊄B₃ₓ₅} e^{−m₁ d(Δ,R)}.
- **m5. One input of D.1 is missing, so gate GA2 cannot pass as worded.**
  - D.1's inputs (ll. 107–108) and gate GA2 (ll. 312–313: "cites only A3, Lemma C.2,
    Theorem C.5, Hölder and dominated convergence") both omit F ∈ L²(dμ₀). This is the
    Gaussian-moment item listed as elementary in Part 4, l. 407.
  - Without it the Hölder step on the stated dominator does not close.
  - *Repair:* add that item to both.
- **m6. G-0 omits three build checks** (ll. 289–293):
  - the Overfull count of AGENTS §7.1;
  - the `pdftotext … | grep` check for `??`/`TODO`;
  - G5's "every page rendered and inspected".
- **m7. F-T is worded for statement scope only.** Its bracketed clause (ll. 638–640, "Appendix
  D also uses the transverse case, at the printed statement's scope") does not fit
  proof-reached scope, where it must name A8(iv)-T. Part 8 gives no variant.
- **m8. Part 0 abbreviates three frozen sentences.** Part 0 (ll. 58–66) shortens them with "…",
  while Part 8 (l. 634) requires verbatim use. Their content agrees with F-A, F-B
  (proof-reached) and F-C. *Repair:* mark them as abbreviations, or quote them in full.
- **m9. The claim about (1.1.6) monomials rests on pages the plan does not cite.**
  - Part 2 ll. 240–242: "Space-time monomials (1.1.6) are reached in any orientation after
    slicing".
  - This rests on the multi-time reading of (1.1.5), which p. 593 alone does not settle.
    p. 595 prints "In the monomial Q(x₀) of (1.1.5), suppose x₀ = (x_{1,0}, ···, x_{r,0})",
    and p. 596 prints "localized at times x_{i0}".
  - Under that reading, (1.1.6) kernels lie in L²(R^{2r}) and the class is closed under
    rotation.
  - Under a single-time reading, a rotated (1.1.6) monomial with r ≥ 2 would also leave the
    class, and GJS's own Q = ΠΦ(f_i) on p. 595 would not be of type (1.1.6).
  - *Repair:* add p. 595 to the new C5 item 10 (ll. 470–471) and to the disclosure's
    supporting pages.
- **m10. The word "explicit" in the rate needs a qualifier after Phase B.** M, and hence
  Ψ_{m₁}, will then contain the unevaluated S₂. The affected sentences are the abstract's
  "explicit super-polynomial rate" (main.tex l. 100) and §1.2's "An explicit rate holds"
  (l. 160). Part 6 (ll. 542–543) lists their line ranges but not this point.
- **m11. The plan is silent on the definition of ε_P.** §2.6 (main.tex ll. 887–888) defines ε_P
  through "the Glimm–Jaffe–Spencer expansion is valid at bare mass M_*". After Phase B only
  Theorem 1.1.7's hypotheses are consumed (r1b (vi)). Part 6 does not say whether this
  definition is reworded.
- **m12. The Part 1 status table (ll. 179–184) omits two items.** These are Proposition C.7
  ("Assume U_GJS", main.tex l. 2921) and Remark 13.3, which per labels.md reaches A8 and
  cites U_GJS.
- **m13. Several line locators are off by a few lines.** No number is wrong.

  | item | correct lines | plan says |
  |---|---|---|
  | Scope paragraph | ll. 779–809 | 779–804 (l. 507) |
  | A8 *Used in* | ll. 811–812 | 812 (l. 523) |
  | Proposition C.7 | ll. 2919–2939 | 2919–2937 (l. 540) |
  | "classical Bessel facts" | begins l. 2838 | 2839 (F13) |
  | Remark C.6 sentence | spans ll. 2914–2916 | — |
  | companion sentence (`s4-import.tex`) | starts l. 73 | 74–75 (ll. 287, 515) |
  | Theorem 12.2(5) | ll. 2308–2314 | — |
- **m14. Trap 15 overstates.** Trap 15 (ll. 688–689) says "Neither is true". The memos show
  only that neither is established. *Repair:* write "neither is established", with the
  `m4/h6.tex` locators that `aqft` cites.
- **m15. Integration has no fallback.** Gate GI exists (ll. 354–359), but nothing says what
  happens if it fails.
- **m16. Part 0's description of Phase C fits only option C1.** Part 0 (ll. 51–52) says "an
  isotropic clustering theorem of the record. 45–70 pp". Option C2 is "more than 31–46 pp"
  and C3 is ≤ 5 pp (ll. 369–378).
- **m17. The box term is placed in the wrong lemma.** Part 2 l. 216 says "That is exactly the
  box term of Lemma D.2". The base term occurs in D.3 and D.4, not in D.2's statement.
- **m18. The Phase A fallback understates what Lemma L needs.** Phase A fallback, ll. 321–325:
  - Lemma 7.1′ holds only for T ≥ t_* (`mp`'s own trap 3).
  - Lemma L(iii) uses Theorem C.5 (for Z_N) and a Jensen–Chebyshev step that `mp` tested
    numerically.
  - "Proved in-house from A2 and A4" covers only L(i).
  - *Repair:* state the change of statement and the extra inputs.
- **m19. Part 9b misses two misprints on pages it cites.** Both were read on the images.
  - p. 597 prints "n = 0 in Theorem 1.1.11 Then Q" without a period. r1c §1 and main.tex
    l. 760 insert one silently.
  - p. 593 prints "Δ_{j_1} × ··· × Δ_{j_n} ⊂ R^{2r}", with index n against r.
  - Trap 23 (ll. 703–704) should also cite (1.1.16)'s "uniformly in h" (p. 596).
- **m20. The plan does not say that its two companion notices are different.** One is Phase
  0's (l. 287; Checkpoint 1 (g)); the other is Checkpoint 2 question 8 (l. 801, "A dated
  notice now"). The plan should say so.

## 3. What I checked at the source

### A. Locators of the record
- **labels.md.** Every number the plan uses resolves and matches its title:
  - 2.2–2.4, 3.1–3.3, 4.1–4.4, 5.1, 5.2, 6.2, 6.3;
  - 7.1–7.8, 10.2–10.5, 11.1, 11.2, 12.2, 12.3, 13.1–13.3, C.1–C.7;
  - A1–A8, and eq. (5) = `eq:QVnorm`;
  - 61 numbered statements and 125 labels (`grep -c newlabel part_i/main.aux` = 125).
- **main.tex, read and matched against the plan's claims.**

  | lines | content |
  |---|---|
  | 59; 64–84; 93–111 | `\date`, title notices, abstract |
  | 154–205; 157–163; 173; 199 | §1.2: quotation, table row (i), dependency graph |
  | 245–345 (289–293; 342) | §1.4 |
  | 392–409; 436; 438 | Definition 2.1; notation table |
  | 516–535; 553 | A3; A4 Scope |
  | 636–817 | A8: (ii) 643–654, (iii) 656–667, (iv) 669–678 with "(any orientation)" at 673, (v)–(viii) 680–777, l. 760, ll. 767–768, Scope 779–809, l. 780, Scope (b) 790–796, *Used in* 811–812 |
  | 884–899 | standing weak-coupling assumption |
  | 1034–1151 | §4, including Lemma 4.3 at 1085–1121 |
  | 1154–1249 | §5: Steps 1–6, eq. (5), Corollary 5.2, 362 880 at l. 1247 |
  | 1252–1320 (1260; 1296–1305) | §6 |
  | 1323–1620 | §7: `\|le` at 1349; 1363–1365; 1402–1403; Lemma 7.4 at 1427–1469; 1452; Lemma 7.6 at 1504–1536 |
  | 1953–2060 | Lemmas 10.1–10.3 |
  | 2157, 2202, 2349, 2412, 2480 | statements of 11.1, 11.2, 12.3, 13.2, 13.3 |
  | 2291–2326 | Theorem 12.2 (2295; (5) at 2308–2314; imports paragraph 2316–2325) |
  | 2546; 2556–2585 | §14 "Standing scope"; Appendix A |
  | 2650–2939 | Appendix C: 2661–2663; 2676–2677; 2683; 2699; 2708–2709; 2725–2727; 2729–2745; Lemma C.2 2771–2784; Lemmas C.3–C.4; 2838–2839; Theorem C.5 2859–2907; 2914–2916; Proposition C.7 2919–2939 |

  Result: no number mismatch. Line offsets are listed in m13.
- **Other files.**
  - `docs/imports.md` ll. 30–60 (l. 56 "The only proportionate route"; l. 57 "pp. 598–629").
  - `companion/sections/s4-import.tex` ll. 70–78.
  - `strategy.md` ll. 2235–2262 and 2275.
  - `part_i/README.md` ll. 126–232 (the G0–G6 definitions; l. 155).
  - `part_i/C5_reading_record.md`, all of it.
  - The abstract of `m4/r1-check.tex` (ll. 33–72; item (2), "never estimated").
  - `m4/m2-audit.tex` ll. 150–190.
  - `README.md` ll. 17–18.
- **KB nodes** (via `kb show`):
  - `common:reference/glimm-jaffe-spencer-1974`;
  - `common:reference/glimm-jaffe-spencer-erice-1973`;
  - `glimm_jaffe:` `problem/level2-h-trace`, `result/hamiltonian-bypass-dead`, `import/u-gjs`,
    `decision/ugjs-imported-at-source-scope`, `result/main-theorem-conditional`,
    `problem/c5-second-reader`.

### B. Page facts (all read on the images)

**GJS (Annals 1974).**

| page | image | what I read |
|---|---|---|
| 589 | p-06 | "Let h be a function with compact support in R², and let 0 ≦ h ≦ 1"; (1.8); footnote 5 |
| 593 | p-10 | (1.1.5)–(1.1.6); the "localized" definition; "centered at the lattice side j_i ∈ Z²"; "n_i < n̄"; "Any choice n̄ ≧ deg P is sufficient"; "For a localized monomial Q or Q(x₀)" |
| 594 | p-11 | (1.1.7)–(1.1.9); "with disjoint localization squares …, let d be the width of the widest strip bounded by two parallel lines, and separating"; Theorem 1.1.7 and (1.1.10); (1.1.11), whose display bounds by O(1)e^{−m₁d/2} |
| 595 | p-12 | (1.1.12) with Σ_{i∈Z²} V(g_i); "We apply Theorem 1.1.7 to each term in the sum"; "suppose x₀ = (x_{1,0}, ···, x_{r,0})"; Theorem 1.1.8 "uniformly as h → 1" |
| 596 | p-13 | "monomials of type (1.1.5)"; "localized at times x_{i0} ≦ 0" and "≧ 0"; Theorems 1.1.10–1.1.11; (1.1.14)–(1.1.16) "uniformly in h"; "t_j = j" |
| 597 | p-14 | "From the choice B = I"; the rotation sentence, verbatim as quoted in the plan at ll. 233–235 |
| 600 | p-17 | proof of Theorem 1.1.8 ("Choose T = 0 and B = I in Theorem 1.1.11. Then Q = 0"); C_Y = YCY + (1 − Y)C(1 − Y), "diagonalization"; (2.0.1) |
| 601 | p-18 | (2.0.2), with V(Yh) and V((1−Y)h); (2.0.5) with a spurious ∫₀¹ds |
| 611 | p-28 | (2.3.4); "We have used (2.0.1) to factor" |
| 612 | p-29 | (2.3.8), with denominator |
| 613 | p-30 | (2.4.3) with e^{γt} |
| 614 | p-31 | Table 1; 𝒦 = 𝒦₁𝒦₂𝒦₃𝒦₄ |
| 615 | p-32 | (2.4.4) 𝒦₂ = e^{−(1−ε)m₀Σδn}; (2.4.5) |
| 622 | p-39 | Lemma 2.4.6; "K₂ = K₂(m₀, K₃)"; (2.4.28) |
| 624 | p-41 | (2.4.34) "1 ≦ ‖e^{−V(Y)}‖_{L₂(dΦ_C)} ≦ e^{K₃|Y|}", with K₃ "independent of C, m₀ and λ" (h is not mentioned); (2.4.35); "(see [1])"; a display without denominator; "for K₂ ≧ K₃²"; e^{O(Vol)} |
| 628 | p-45 | "we do not give the details"; proof of Theorems 1.1.8 and 1.1.11; e^{γt} |
| 629 | p-46 | "Theorem 1.1.8 is the special case B = I, n = 0"; the uniformity sentence |
| 630 | p-47 | (seen while locating the reference list) |
| 631 | p-48 | ref. [1], Dimock–Glimm, Adv. Math. 12 (1974) 58–83; ref. [6], GJ IV, J. Math. Phys. 13 (1972) 1558–1584 |

**Erice lectures.**
- Erice I p. 160 (p-29): (2.2.3), with sharp time δ_s(t)f(x⃗) allowed; Theorem 2.2.1, with
  "d = dist.{suppt. A, suppt. B}".
- Erice I p. 161 (p-30): (2.2.4) "uniformly in h"; the bracket (2.2.5)–(2.2.7).
- Erice II p. 236 (p-38): "the stronger hypothesis of [1], C ∈ ℬ^loc_{q,δ(q)}".
- Erice II p. 237 (p-39): Theorem 9.5, (9.8) with K₁₂, then "K₁₀".
- For the rest of the Erice material I relied on the reviewed KB node's verified claims.

**Simon.**
- p. 155 (`<scratch>/simon/s-177`): Proposition V.10; §V.3, "g ∈ L^{1+ε}(R) ∩ L¹(R);
  g ≥ 0".
- p. 156 (s-178): "THEOREM V.10", with (iii) "‖P(t)‖_{2,s} ≤ ‖F_{(0,t)}‖_r".
- p. 158 (s-180): "‖F(0,t)‖_{r′}".

**Verdict on the transverse case.** I agree with the plan (Part 2, ll. 233–242). The printed
proof of Theorem 1.1.7 does **not** reach a sharp-time monomial across a strip transverse to
the time-zero line. My reasons:
1. (1.1.5) monomials have fixed sharp times (one per factor) and spatial L² kernels (p. 595,
   p. 596). (1.1.6) monomials integrate all r times against an L²(R^{2r}) kernel.
2. Theorem 1.1.11, which the proof invokes "after rotating and translating the strip", takes
   A and B of type (1.1.5), localized at times ≤ 0 and ≥ 0 (p. 596).
3. Any strip of positive width that separates row-0 squares from far squares in rows −1, 0, 1
   is non-horizontal. Rotating it to horizontal tilts the time-zero line. At 90°, the image of
   a sharp-time monomial has fixed spatial position and integrated times. Its kernel is a δ in
   the spatial variables, so it is neither (1.1.5) (its times are not fixed) nor (1.1.6) with an
   L² kernel.
4. Swapping roles fails for the same reason, and slicing U_Δ does not help, because the
   sharp-time partner remains.
5. No printed application uses this case. GJS's p. 595 pairs are both of type (1.1.6), and
   Lemma 7.4 uses only horizontal strips. Erice I Theorem 2.2.1 asserts the case (isotropic
   d, sharp time allowed) without printing a proof.

Two qualifications: the multi-time reading of (1.1.5) needs p. 595 (m9), and the parallel
case is reached only through Theorem 1.1.8 at the same h (C1).

**F1 confirmed at the source.**
- (2.4.34) is a stability bound under dΦ_C, cited to [1] = Dimock–Glimm, and it fixes
  K₂ ≥ K₃² (pp. 622, 624).
- V(Y) carries h: p. 601 writes V(Yh).
- The kernels behind the norm (2.4.3) contain ∫(…)e^{−V(Y_j)}dΦ_C ((2.3.4), (2.3.8),
  pp. 611–612). So M1's "No Gaussian expectation, no e^{−U}, no h appears in the norm"
  (l. 2677), M3 (l. 2699), M4 (ll. 2708–2709), M5 (ll. 2725–2727) and abstract item (2) of
  `m4/r1-check.tex` are false about the source.

### C. The statements against what the record consumes
- **Lemma 4.3(ii)** (ll. 1085–1121). Finiteness at each T needs only A3, Hölder and the
  Gaussian moments of F (F7 confirmed).
- **Theorem 5.1, Steps 5–6** (ll. 1218–1241). Step 5 consumes ∫V(h)(0)² dq_{h_{T,g}} ≤ M²
  for every T > 0 and g ∈ 𝒞_H. This is the full second moment at sharp time zero. D.4
  delivers it for every h ∈ 𝒞_E, and Step 6 is unchanged.
- **Lemmas 7.1–7.3** (ll. 1329–1425).
  - They consume sup_{T>0} at time 0 (Lemma 7.1) and boundedness of the vectors at ∓t/2
    through Lemma 7.1.
  - D.3 delivers these for every T > 0 and s (beyond F7, only s = 0 is actually needed).
- **Lemma 7.6** (ll. 1504–1536). It needs n-independent A_f and K_f; D.3 gives them (m4).
  Theorem 7.7 needs only some s₀ > 0.
- **Lemma 10.2** (ll. 1992–2013). It consumes the Hamiltonian bound ‖V_jΩ_{g_s}‖ ≤ M for
  g_s ∈ 𝒢 (Lemma 3.1(iii)). Delivered.
- **Theorem 12.2(5)** (ll. 2308–2314). It consumes sup over g ∈ 𝒞_H. Delivered.
- Nothing is consumed that D.3 and D.4 fail to deliver: T > 0 rather than T ≥ t_*, 𝒞_E ⊃
  slabs, the full rather than the centred moment, sharp time rather than smeared. The
  exceptions are noted at m1 (A's uniformity) and m18 (the fallback is T ≥ t_* only).

### D. Re-derivation of the comparison route
1. **Affine-path identity (D.1).**
   - U_{h_α} = U_{h₁} + αD with D = U_{h₂} − U_{h₁} ∈ L^p by A3 (ll. 517–519).
   - α ↦ e^{−U_{h_α}} is convex, so e^{−U_{h_α}} ≤ e^{−U_{h₁}} + e^{−U_{h₂}}.
   - Hölder with exponents (2, 4, 4) closes, provided F ∈ L²(dμ₀) (m5).
   - Z(α) > 0, and d/dα(N/Z) = −Cov_{h_α}(F, D). The identity holds, with C¹ on [0, 1].
2. **Geometry and summation.**
   - On GJS squares, row 0 is [−½, ½] in time, so time 0 is interior to it.
   - Around B₃ₓ₅, ring k contains (3+2k)(5+2k) − (1+2k)(3+2k) = 8k + 12 squares, each with
     strip width d ≥ k:
     - above or below the box: a horizontal strip of width k;
     - to the side: a column gap ≥ k + 1 from R's columns, hence a vertical strip of
       width ≥ k.
   - So Σ ≤ Σ_k (8k+12)e^{−m₁k}. `aqft`'s bound (2k+3)(2k+5) ≥ 8k + 12 is a valid but
     cruder upper bound.
   - Uniform in T, h and a.
   - In D.3, every square of supp h_{T,g} outside B lies in rows |l − l_s| ≥ 2. This gives
     2N_g Σ_{k≥1} e^{−m₁k}, which times C₇c_U is B′.
3. **Pairs and norms.**
   - Theorem 1.1.7 is printed for "two localized monomials". p. 593 defines "localized" for
     both forms, so the mixed pair is covered by the statement.
   - U_{Δ,n} is of type (1.1.6) with r = 1. Its norm is ≤ K₁K₂^{2n}n!λ|a_n|, since
     ‖h1_Δ‖₂ ≤ 1.
   - The n = 0 term is constant. The squares are disjoint because Δ ⊄ B ⊇ R, and
     d(F_a, Δ) ≥ d(R, Δ).
4. **Base term.**
   - |⟨F⟩_{h^B}| ≤ ‖F‖_{L²}·S₂(B)·e^{λ|a₀||B|}, by Cauchy–Schwarz, Theorem C.5 and Lemma C.2.
   - S₂ is invariant under translations, since μ₀ and 𝒞_E are. This sentence is not yet
     written.
   - ‖V²‖₂ = ‖V‖₄² ≤ 9^{p′}‖V‖₂², by the comparison ‖Y‖_q ≤ (q−1)^{p′}‖Y‖₂ in the proof of
     C.5 (ll. 2870–2880).
   - V_* by Wick orthogonality, with C > 0, log-singular and locally integrable.
   - I read the proof of C.5 (ll. 2868–2907) and found no error. This is not the
     independent audit GA4 asks for.
5. **Passage to Ω_g and to §7.**
   - Steps 5–6 hold as written with M_B.
   - Lemma 7.6: E_{μ_g}[X_f^{2n}] ≤ (A + B′K₁)·max{K′, √2σ_f}^{2n}(2n)!, using
     (4n−1)!! ≤ 4^n(2n)!.
6. **Hypotheses.**
   - Theorem 1.1.7 requires "m₀, K₂ and K₁ sufficiently large and λ sufficiently small"
     (p. 594). Lines 884–899 fix m₀ = M_*, λ < λ_* and the printed K₁, K₂.
   - n̄ = 2p′ + 1 (l. 652), and all degrees used are ≤ 2p′.
   - C.2 and C.5 hold for every λ ≥ 0.
   - No new hypothesis is needed.

**Weakest step.** At the level of imports, the transverse application in D.4 (A8(iv)-T). At
the level of the record's own mathematics, Theorem C.5: it becomes load-bearing, its constant
is not evaluated, and it has not yet been independently audited. At the level of the status
logic, the "reach" of the parallel case (C1).

### E–I. Results
- **E.**
  - No route is called proved.
  - Theorem 12.2 is "proved, conditional on U_GJS" wherever today's status is given
    (ll. 11, 55–57, 585–586, 641–643).
  - Table 1 is consistent with its own definition, modulo M1. Table 2 is not (C1).
- **F.**
  - Gates are checkable, except GB1 (M2) and GB2 (M3).
  - Every phase has a fallback except integration (m15).
  - Estimates are labelled as such (ll. 10, 41, 265, 288, 305, 339, 366).
  - Nothing is scheduled ahead of the checkpoint that decides it. M1, if pursued, belongs to
    Checkpoint 1.
- **G.** Findings register.
  - **Confirmed at the source:**
    - F1, at pp. 601, 611–612, 622, 624 and in the record's lines;
    - F2, at the TeX source only (I did not build);
    - F3 (record lines and p. 593); F4 (`docs/imports.md` l. 56, the KB summaries, companion
      ll. 73–75); F5 (`docs/imports.md` l. 57, `strategy.md` ll. 2235 and 2275, README
      l. 155, companion l. 75, pp. 628 and 631);
    - F6 (all six statements); F7; F9 (ll. 290–293; Source Fact 2.3 = `sf:CE1`);
    - F10 (images of pp. 155–156; "Theorem V.11 (iv)" in the text layer only);
    - F11, all three parts (l. 2683 against p. 600; l. 2676 against p. 613; (2.4.4) on
      p. 615 is script 𝒦₂);
    - F12; F13; F14 (l. 780 against p. 595).
  - **Confirmed as a description, but its repair depends on the standard:** F8 (see C1).
  - **Part 9b, confirmed:** pp. 593, 600, 601, 611; the missing denominator ((2.3.8) on
    p. 612 against p. 624); Erice II p. 237 "K₁₀"; Simon pp. 156/158 (r against r′).
- **H.** Internal inconsistencies are listed under C1 (l. 46 against Table 2), M3, m7, m8,
  m16 and m20. The frozen sentences agree in content between Parts 0 and 8. The constants
  are named consistently, with mappings given (c_U, S₂, M_B).
- **I.** Omissions are listed under M1, m10, m11 and m12.

## 4. What I could not check
- **Simon.** The image of p. 167 (I used the text layer for "Theorem V.11 (iv)"). Also
  `mp`'s Hölder chain for Lemma L beyond the exact identity (40/7 − 1)/(20/11 − 1) = 121/21,
  and `mp`'s numerical Jensen–Chebyshev test.
- **GJ IV pp. 1568–1569** (Phase C3's formal-positivity claim; the editor's reading).
- **Dimock–Glimm and the Phase C1 references** (not on disk).
- **`cqft`'s first-order computation for "1 ≤" in (2.4.34).** I checked only the direction of
  Jensen's inequality in a₀.
- **Companion register items F3, F18 and F21** (not opened).
- **The rendered PDF of main.tex** (I did not build).
- **The independent audit of Lemmas C.2–C.5** that GA4 requires. I read them only.
- **Earlier treatments of (1.1.16) with B = I.** I searched `part_i/`, `docs/`, `m4/`,
  `strategy.md` and the KB decision node, and found no such discussion. I did not search
  every file of the repository, so the record may treat the M1 reading somewhere I did not
  look.
- **Scratch file.** The only file I wrote apart from this report is `<scratch>/gjs74-verifier.txt`,
  a `pdftotext` extraction used to locate V(Y) and reference [1] before reading the pages.

---

## R3b. Re-verification of the revised plan (round R2b), 30 October 2026

Same verifier. Read for this round:
- rulings R9–R13 (`r1c-orchestrator-rulings.md` §5, ll. 151–204);
- the revised `ugjs/PLAN.md`, all 958 lines (10,773 words);
- the council `README.md`.

I re-read GJS p. 596 (`gjs74/p-13`) on the image. Pages 593–595, 597, 600, 622, 624, 628, 629
and 631 were read on the images earlier in this session (section 3B above). I ran the gates'
grep commands on `part_i/main.tex` myself. Line numbers "l." below are those of the revised
`PLAN.md` unless "main.tex" is said.

### R3b.1 Verdict

**After the listed fixes.** Every R3 item is resolved as R9–R13 say. Two items are only partly
resolved:
- the M1 resolution introduces N1;
- the M2 resolution introduces N2.

Both MAJOR items are text fixes that need no new ruling.

Counts for the revision: **CRITICAL 0, MAJOR 2, MINOR 14.**

### R3b.2 Check (a): the R3 items, one by one

| R3 item | ruling | resolved? | where in the revised plan |
|---|---|---|---|
| C1 | R9 | yes. One standard and one status table. "Under both standards" is withdrawn. The paragraph has one wording slip (n6). | l. 26–29; l. 690–727; D12 l. 916; D15 l. 919; F8 row l. 875; Part 5 l. 578 |
| M1 | R10, R11 | yes, as Phase 0′. New: N1 (MAJOR), n1–n5, n11, n12 | S0′ l. 104–129; Part 0 l. 31–39; Part 3 l. 351–398; Part 4 l. 505; Part 7 l. 694–701, 740–750; F-0′ l. 787–789; Q1 l. 927–929; D16 l. 920 |
| M2 | R13 | patterns fixed. The expected-survivor list is wrong (N2) | GB1 l. 439–447; G-0′ l. 390 |
| M3 | R12 | yes | l. 317–319; GA8 l. 421; GB2 l. 448–449; fallback l. 452–454; l. 574–576; l. 684–686; l. 765 |
| M4 | R9 | yes, but "neither implies the other" overclaims (n7) | l. 729–738; trap 6 l. 816–817 |
| m1 | R13 | yes | l. 160–163 |
| m2 | R13 | yes | l. 90–93 |
| m3 | R13 | yes | l. 134, 141, 410 |
| m4 | R13 | yes (A_f := A + B′K₁; Σ₃ₓ₅ defined) | l. 171, 186 |
| m5 | R13 | yes | l. 136, 404, 413–414, 515 |
| m6 | R13 | yes | l. 342–344 |
| m7 | R13 | yes | l. 782–783 |
| m8 | R13 | partly. Marked as abbreviations, but two paraphrase (n8) | l. 62–67 |
| m9 | R13 | yes | l. 291–294, 507, 580–582 |
| m10 | R13 | yes | l. 632–634 |
| m11 | R13 | yes, but Theorem 1.1.11's statement prints no smallness hypothesis (n3) | l. 376, 635–638 |
| m12 | R13 | yes | l. 221, 223 |
| m13 | R13 | yes | l. 668–675, and in place at l. 310, 339, 364, 371, 617, 627, 630, 868, 871, 880 |
| m14 | R13 | yes. The h6 numbers are right: the `m4/h6.pdf` text layer prints Proposition 2.1, Proposition 2.2, Theorem 3.2 and Lemma 3.4 | l. 839–841 |
| m15 | R13 | yes | l. 465–467 |
| m16 | R13 | yes | l. 58–60 |
| m17 | R13 | yes | l. 269–270 |
| m18 | R13 | yes | l. 422–427 |
| m19 | R13 | yes | l. 855–856, 890–891 |
| m20 | R13 | yes (three dated notices) | l. 656–661 |

### R3b.3 New findings

#### MAJOR

**N1. Phase 0′ states its literal basis at T = 0, a value p. 596 does not cover.**
- *Locators.* Part 0 l. 32–34; S0′ l. 114–118; Part 4 l. 505; Part 7 table l. 699; F-0′
  l. 787–789; Checkpoint 1 question 1, l. 927–929.
- *Sentences.*
  - l. 114–116: "Then apply (1.1.16) … with B = I, n = 0, T = 0. This is p. 600: 'Choose T = 0
    and B = I in Theorem 1.1.11. Then Q = 0.'"
  - l. 117–118: "The variant 0 < T < 1 (the verifier's) gives the same bound".
  - F-0′: "Its moment input A8(vi) is GJS Theorem 1.1.11, (1.1.16), at B = I, n = 0, T = 0,
    the specialization GJS print as their proof of Theorem 1.1.8 (p. 600)".
- *What is wrong.*
  - p. 596 (image, re-read) fixes the range of T before Theorems 1.1.10–1.1.11: "Let B_T
    denote the translate of B at time T > 0, so that B_T is localized at times ≧ T."
    Theorem 1.1.10 repeats "T > 0" in its own hypothesis.
  - T = 0 is the value GJS choose in their *proof* of Theorem 1.1.8 (p. 600). Their
    *statement* prints only T > 0.
  - The plan's one standard is "a printed statement, used at the scope at which it is
    printed" (l. 26–27, 690–691), and Phase 0′ is "a re-sourcing, not a proof" (trap 2,
    l. 807–808). Such a re-sourcing cannot rest on a parameter value that only the proof
    uses.
  - The in-scope values 0 < T < 1 give the identical bound. In my check, the sum
    Q = Σ_{0<t_j<T} Q_n(t_j) is empty because t_j = j; I_T = I; and e^{−γT} ≤ 1. The plan
    already says this (l. 117–118), but only as a variant.
- *Repair.*
  - In all six places, make "(1.1.16) at B = I, n = 0 and any 0 < T < 1" the literal basis.
  - Cite p. 600's T = 0 as GJS's own choice, which gives the same bound.
  - Add to S0′ a fourth objection, "T = 0 lies outside the printed T > 0", answered by this.
- *Severity.* MAJOR. The frozen sentence and Checkpoint 1 would otherwise put a
  statement-versus-proof slip into the one claim that rests on that distinction.

**N2. Gate GB1's expected surviving hits are incomplete, so the gate cannot pass with the
plan's own edits.**
- *Locator.* Part 3 l. 439–447: "The surviving hits must be exactly: A8(vi), marked retired,
  with its tag and label kept for provenance; the Scope paragraph's history sentences;
  Appendix B's corrections history and External residue; Appendix C's introduction, as
  history. Any other hit fails the gate."
- *What is wrong.*
  - On today's main.tex the gate's grep gives 54 hits: the 36 of the old pattern plus the 18
    lines that carry `U_{\rm GJS}` and nothing else matched. `grep -c 'Assume \$U_{\\rm GJS}'`
    prints 2 (main.tex ll. 2295, 2921).
  - I matched every hit against the plan's own edit map (Parts 3 and 6). These would survive
    Phase B, and none is in the list:
    - the title-page notices, main.tex ll. 68, 72, 76, 81. They are kept "marked superseded"
      (l. 372).
    - A8(v) at main.tex l. 685 (C₈ in CE1's display) and A8(vii′) at l. 722
      (`\eqref{eq:UGJS}`). They are kept "as corroboration" (l. 368) and then moved "to
      provenance" (l. 626).
    - The notation table at main.tex l. 436 and the standing assumption at l. 897 ("C_7, C_8,
      K_1, K_2 denote the printed constants"). No edit is planned for either.
    - Eq. (5) at main.tex l. 1214, "… = M²/C₈". It sits in Step 4, which the plan keeps
      (l. 199, 624), and it becomes false once M = M_B (n14).
    - Corollary 5.2 at main.tex l. 1247, if it is "retired" rather than restated (l. 201,
      624–625).
  - Every other hit is either removed by a planned edit or in the list.
    - Removed by a planned edit: main.tex ll. 93, 108, 157, 173, 199, 280, 1111, 1117, 1163,
      1222, 1225, 1331–1350, 1364–1365, 1403, 1510–1532, 2295, 2317, 2325, 2568, 2574–2575,
      2921 and 2923.
    - In the list: main.tex ll. 693–708, 796, 800, 2631, 2643, 2654 and 2660.
- *Repair.*
  - Write the expected survivors as line ranges of the edited file. Add the title notices,
    A8(v) and A8(vii′) (as provenance), and Corollary 5.2 if it is kept.
  - Add edits for main.tex ll. 436, 897 and 1214 to Part 6.
- *Severity.* MAJOR. The gate is wrong in a way that forces either a false failure or the
  deletion of history that the plan says to keep.

#### MINOR

- **n1. "n = 0" is attributed to p. 600.** F-0′ (l. 788–789) and Part 0 (l. 33–34) attribute
  "B = I, n = 0, T = 0" to p. 600. But p. 600 prints only T = 0 and B = I, with no n; "n = 0"
  comes from p. 629 ("the special case B = I, n = 0"). *Repair:* cite both pages.
- **n2. S0′ does not fix ε.** Theorem 1.1.11 begins "Let n and ε > 0 be given" (p. 596), and
  its O(1) depends on n and ε. *Repair:* name both when C₈ is defined (l. 107–109).
- **n3. Theorem 1.1.11 prints no smallness hypothesis.**
  - Its statement (p. 596) says only "Let n and ε > 0 be given", unlike Theorem 1.1.7
    (p. 594).
  - The rewording of ε_𝒫 is to "name the printed hypotheses of the theorems actually
    imported: Theorems 1.1.7 and 1.1.11" (l. 376, 635–638). For 1.1.11 it must say where GJS
    print them:
    - Theorem 4.1, p. 628: "Let m₀, K₂ and K₁ be sufficiently large, and let λ be
      sufficiently small". Theorems 1.1.8 and 1.1.11 are proved from it on pp. 628–629.
    - p. 600: "convergence of our expansions requires both sufficiently small λ and
      sufficiently large m₀".
  - *Repair:* cite those pages, and add this as a further objection in the Scope paragraph.
- **n4. The localization step is missing.** S0′'s derivation (l. 110–118) applies (1.1.16),
  which is stated for localized A, to "every sharp-time monomial". *Repair:* add one line: a
  general monomial is a sum of localized pieces, and its norm is the sum of theirs by
  (1.1.9).
- **n5. A quotation is truncated without marking.** l. 115–116 closes the p. 600 quotation with
  "Then Q = 0.". p. 600 prints "Then Q = 0, so Theorem 1.1.8 is a special case of Theorem
  1.1.10." *Repair:* mark the truncation, as l. 361 and l. 589 do.
- **n6. "The record can take neither" contradicts the recommendation.** Part 7 l. 720–724 says
  "There are two ways to avoid this, and the record can take neither". But the second way
  ("Reading the h-uniform Theorem 1.1.8 off a printed statement is exactly Phase 0′") is the
  one the plan recommends. *Repair:* "neither keeps proof-reached scope a second standard.
  The first is the asymmetry the record rejected; the second is the one standard itself
  (Phase 0′)."
- **n7. "Neither implies the other" asserts an unproved negative.** Part 7 l. 733 and trap 6
  (l. 817) say it. What is shown is less: U_GJS is a moment bound that states no clustering,
  and the comparison route does not give U_GJS from A8(iv)-T, since A grows with the
  observable's box. *Repair:* "neither is known to imply the other". Ruling R9 uses the same
  words, and the same correction applies there.
- **n8. Two Part 0 "abbreviations" paraphrase the frozen sentences.**
  - "… one GJS theorem imported, Theorem 1.1.7, also used across transverse strips …" (l. 66)
    is not a fragment of F-B (l. 796–799).
  - "… its transverse use is a theorem of the record." (l. 67) is not in F-C (l. 800–801).
  - *Repair:* use verbatim fragments.
- **n9. The table row "GJS statements imported" counts only theorems.** In every column the
  record also imports printed GJS statements A8(i)–(iii) (the p. 589 class, the p. 593
  observables, the p. 594 norms) and A8(viii) (the p. 590 dilation). So "(none, if Lemma 7.4
  is re-based on S3)" (l. 701) is wrong as worded. *Repair:* rename the row "GJS theorems
  imported", or list the four items.
- **n10. A page reading is attributed to the orchestrator without a record of it.** Part 2
  l. 264 says "`cqft`, `editor` and the orchestrator read pp. 622 and 624", and the F1 row
  (l. 868) says "the orchestrator (30 October)". But r1c §§1 and 5 and the council README
  record the orchestrator reading only pp. 593–597, 596 and 600, and the R2 plan said "not
  re-checked by the orchestrator". *Repair:* record that reading, or drop the attribution.
- **n11. Phase 0′ rests on two more checklist items than it names.**
  - p. 596's preamble: "monomials of type (1.1.5)" (the admissibility of a degree-zero B) and
    "B_T … at time T > 0". This is new item 12, which Part 5 (l. 586–587) and D9 (l. 913)
    assign to Phases A/B only.
  - p. 593's "Since there is no restriction on r" (item 2).
  - *Repair:* name items 2 and 12 among Phase 0′'s readings (Part 5 l. 579; G-0′ l. 387–388;
    D9).
- **n12. G-0′'s grep misses two status sentences.**
  - Its pattern `'Assume \$U_{\\rm GJS}'` (l. 390) misses "Assuming the exact slab-uniform
    interface $U_{\rm GJS}$" (main.tex l. 93) and "\emph{Assuming $U_{\rm GJS}$" (l. 157).
    Both are sentences that Phase 0′ must rewrite.
  - `grep -n -i 'assum[a-z]*[^.]*U_{\\rm GJS}' part_i/main.tex` finds all four (ll. 93, 157,
    2295, 2921).
- **n13. Two phases edit the same paragraph.** Phase 0 ("The A8(iv) Scope gains F-T", l. 333)
  and Phase 0′ ("The Scope paragraph, ll. 779–809, is rewritten", l. 364) both edit A8's single
  Scope paragraph (main.tex l. 779), and both are recommended "now" (l. 69–70). *Repair:* say
  that the two edits are made in one pass, or in which order.
- **n14. One planned edit is missing.** The Phase B edits keep Steps 1–4 of Theorem 5.1
  (l. 624–625). But Step 4's display, eq. (5), ends "= M²/C₈" (main.tex l. 1214), which is
  false once M = M_B; C₈ also stays at main.tex ll. 436 and 897. *Repair:* add these edits
  (they are also needed for N2).

### R3b.4 Checks (b)–(g)

- **(b) Phase 0′ and S0′.**
  - *Quotations.* p. 596's (1.1.16), "uniformly in h", and "We shall choose t_j = j, j ∈ Z"
    are verbatim (image re-read). The p. 600 quotations at l. 361 and l. 589 are verbatim,
    with "[sic]" correctly marked (but see n5 for l. 115–116). p. 629's "Theorem 1.1.8 is the
    special case B = I, n = 0" (l. 238) is verbatim.
  - *B = I and n = 0.* Both are admissible by GJS's own use (pp. 597, 600, 629) and by p. 593
    ("no restriction on r").
  - *T.* See N1.
  - *Integer time translation.* Right. It maps the time into (−1, 0]. It preserves GJS
    squares, the norm (1.1.8), 𝒞_E, μ₀ and the Wick ordering, and the cutoff moves with the
    observable.
  - *Constants.* ‖I‖ = K₁ by (1.1.7) (empty product, w = 1). C₈ = O(1)K₁, with O(1)
    depending on n = 0 and ε (n2).
  - *Objections.* The three are answered as R3 proposed. Two more are needed: T (N1) and
    Theorem 1.1.11's unprinted smallness hypotheses (n3).
  - *Is "literal under the record's standard" justified by the plan's own definition?* Yes
    for 0 < T < 1, given the two readings the plan names (degree-zero B; "uniformly in h"
    read over the class, as the record already reads Theorem 1.1.7). Not as worded for T = 0.
- **(c) The single table** (l. 694–701).
  - It is consistent with its definition (l. 703–704), and its columns are cumulative.
  - The declined-0′ note (l. 709–714) agrees with F-A\* and with Part 1 l. 226–229.
  - The row "GJS statements imported" needs n9.
- **(d) The proof-reached paragraph and A8(iv)-T.**
  - The paragraph's argument is right and matches R9 (p. 597 "at the same h"; p. 595 "as
    h → 1"; `strategy.md` ll. 2250–2252, checked). Its wording needs n6.
  - The A8(iv)-T text is correct ("not a different standard, not a narrower form") except
    for n7.
- **(e) Gates, run on main.tex.**
  - GB1's grep gives 54 hits; the `Assume` grep gives 2.
  - After the planned Phase 0′ edits (Theorem 12.2 at main.tex l. 2295; Proposition C.7 at
    l. 2921), the `Assume` grep prints 0, as G-0′ and GB1 require.
  - The expected-survivor list fails: N2. G-0′'s pattern is too narrow: n12.
- **(f) Internal consistency.**
  - *Frozen sentences, Part 0 against Part 8.* F-0, F-0′ and F-A appear as verbatim
    fragments. F-B and F-C do not (n8).
  - *Phase names* are consistent: 0, 0′, A, B, C and integration, with rounds V0, V0′ and
    V1–V5.
  - *Checkpoint questions* are consistent. Part 0 l. 73–74 summarises Part 11 l. 926–958.
    D10 points to Q3, which exists. Q8 matches the F-T variant at l. 782–783.
  - One overlap in the map of edits: n13.
  - Part 4's "after Phase B, A8(vi) and Theorem 1.1.11 are no longer used" (l. 517–518)
    agrees with the table.
- **(g) Locators.**
  - All seven m13 corrections are right, both in Part 6 (l. 668–675) and in place.
  - The new locators are also right:
    - main.tex ll. 767–768, 797–799, 802–803, 2295, 2316–2325, 59, 93–111, 157–163, 173,
      199, 278–284, 342, 2639–2648, 2653–2663, 887–888, 290–293 and 2546 (checked against
      main.tex);
    - `strategy.md` ll. 2250–2252.

### R3b.5 What I checked, and what I could not

- **Checked.**
  - The revised plan, all of it, and r1c §5.
  - p. 596 on the image, re-read in this round.
  - GB1's grep, the `Assume` grep and a broader `Assum*` grep, all run on main.tex.
  - main.tex ll. 2495–2556 and 2620–2664.
  - The `m4/h6.pdf` text layer, for the numbers in trap 18.
- **Not checked.**
  - Whether the orchestrator's reading of pp. 622 and 624 is recorded anywhere outside r1c
    and the council README (n10).
  - The companion's §1 claims ledger and Figures 1–2, which the Phase 0′ notice refers to.
  - The `docs/` files and `CITATION.cff` that Phase 0′ would edit.
- **No build was run, and no file was touched except this report.**
