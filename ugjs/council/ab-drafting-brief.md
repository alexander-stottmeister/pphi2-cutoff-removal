# Drafting brief: the comparison note (Phases A and B of `ugjs/PLAN.md`), 31 October 2026

Orchestrator: Claude (Fable 5.1), session of 31 October 2026. Drafters: aqft, mp, cqft2 (the
council of `ugjs/PLAN.md`). Repository (read-only for drafters):
`/Users/alex/Documents/Uni/Hannover/claude/glimm_jaffe/`. Work folder (the only place you write):
`/private/tmp/claude-501/-Users-alex-Documents-Uni-Hannover-claude-glimm-jaffe/8bac9e45-6e21-41a1-bdb8-e018c3356462/scratchpad/phaseAB/`
(below: `WORK/`). GJS 1974 page images: `WORK/../gjs74/` (PDF page = printed page − 583; e.g.
printed p. 594 is PDF page 11, file names carry the PDF page); text layer:
`pdftotext -f N -l N WORK/../gjs74.pdf -`.

## 0. Read first, in this order
1. `ugjs/PLAN.md` (1004 lines), all of it; in particular Part 1 (the statements D.1–D.4 and the
   fixed notation), Part 3 (Phases A and B: owners, inputs, deliverables, gates GA and GB),
   Part 4 (imports), Part 7 (status words), Part 8 (frozen sentences and traps 1–28), Part 9
   (findings F1–F14 about the record, and the source misprints to record verbatim).
2. Your own memo in `ugjs/council/` (`memo-aqft.md`, `memo-mp.md`, `memo-cqft2.md`), then
   `r1b-attack-cqft.md`, `r1c-orchestrator-rulings.md`, and §3 of `r3-verifier-report.md` (the
   verifier's re-derivations of the geometry and the ring count).
3. The record `part_i/main.tex` (42 pp; PDF `part_i/main.pdf`, same folder): §2.4 Assumption A8
   (from l. 646; the printed norm is eq. (1), label `eq:printednorm`, l. 680), §2.6 (working
   coordinates), §4 (slab lemmas), §5 (Theorem 5.1 `thm:M2` l. 1255, Corollary 5.2 `cor:M2phi4`
   l. 1342), §6 (cylinder monomials; Remark 6.3 `rem:row` l. 1412), §7 (Lemmas 7.1–7.6, Lemma 7.4
   `lem:ce2strip` l. 1526; Theorems 7.7–7.8), Appendix C (Lemma C.2, Theorem C.5 `thm:stability`
   l. 3008, Proposition C.7). Statement numbers and pages: `WORK/labels-main.txt` (generated
   from `main.aux`). Cite numbers from that table only, never from memory.
4. `/Users/alex/Documents/Uni/Hannover/claude/AGENTS.md`, §§1–4: binding on every line you write.
5. `WORK/preamble.tex` and `WORK/comparison.tex`: the macros and the section plan.

## 1. The deliverable and who writes what
One standalone LaTeX note, master `WORK/comparison.tex` with `WORK/preamble.tex` (both the
orchestrator's; do not edit) and parts in `WORK/parts/`. Each drafter writes only the files
assigned here, plus `WORK/parts/REPORT-<name>.md`. Nothing else: no edit in the repository, no
git, no kb, no file outside `WORK/parts/` except your own scratch build folder
`WORK/build-<name>/`.

| drafter | files (sections of the master) |
|---|---|
| cqft2 | `parts/notation.tex` (§2) and `parts/constants.tex` (Appendix A, gate GA3) |
| mp | `parts/d1.tex` (§3, Lemma D.1) and `parts/quantifiers.tex` (§7) |
| aqft | `parts/d2.tex` (§4, Lemma D.2), `parts/d3.tex` (§5, Theorem D.3), `parts/d4.tex` (§6, Theorem D.4), `parts/consequences.tex` (§8) |

Conventions of the master:
- Environments `dlemma` / `dtheorem` share the counter D.n and are used exactly four times in
  the whole note, in this order: D.1 (`dlemma`, in `d1.tex`, label `lem:D1`), D.2 (`dlemma`,
  `d2.tex`, `lem:D2`), D.3 (`dtheorem`, `d3.tex`, `thm:D3`), D.4 (`dtheorem`, `d4.tex`,
  `thm:D4`). Auxiliary statements use `auxlemma`, `auxprop`, `auxcor`, `auxdef`, `auxrem`
  (counter N.n), labels `aux:<part>-<slug>` (e.g. `aux:notation-strip`). Proofs in `proof`.
  A missing step is marked in place with the `gapnote` environment (prints "GAP") and one line
  saying what is missing.
- Macros: only those of `preamble.tex` (`\R \Z \E \A \G \CE \CH \HH \Om \ip \supp \dist \spec
  \UGJS \GJS{..} \ev{F}{h} \Cov \Uc \dmu \dphi`). Define no macro; write everything else out.
- Citation keys: `R` (the record) and `GJS` only. Refer to the record's statements with number
  and page, e.g. "Lemma 7.4 of the record \cite[p.~21]{R}", numbers from `labels-main.txt`.
- The parts are `\input` inside a `\section`; start each part with a comment line naming the
  drafter and the date, then subsections (`\subsection*` or numbered, your choice), no
  `\section`.
- Write incrementally and save often. If your session is cut off, the orchestrator resumes you
  from your transcript; leave the file in a compilable state whenever you can.

## 2. Mathematical content, part by part
Use PLAN Part 1's notation verbatim: working coordinates z = (x⁰, x¹) of §2.6, time first;
GJS squares centred at lattice sites (p. 593; finding F3: not the record's cells [j, j+1));
Δ_{l,k} with row l = time and column k = space; boxes B, |B|; h^B := h·1_B, h_α := h^B + α(h − h^B);
d(Δ,R) the strip width of p. 594; S₂(B); c_U; the printed constants C₇, m₁, K₁, K₂, n̄.

**`notation.tex` (cqft2).**
(a) Coordinates, squares, rows and columns; fix the convention for a time on a lattice line
(half-open cells [l−½, l+½) × [k−½, k+½), or GJS's own convention if p. 593 prints one) and use
it everywhere; l_s := the row containing time s.
(b) Boxes, |B|, h^B and the path h_α: prove h^B ∈ 𝒞_E and h_α ∈ 𝒞_E from A8(i)'s definition
(quote it from the record).
(c) The strip-width lemma: if R lies in a rectangle S of squares and Δ is at sup-index
distance m ≥ 2 from S, then an axis-parallel strip separates Δ from R and d(Δ,R) ≥ m − 1;
state the orientation of the strip in each case (parallel or transverse to the time-zero
line). Record as a remark that the bound fails for general R (R = {Δ_{0,0}, Δ_{0,4}},
Δ = Δ_{0,2}).
(d) The ring count: ring k around a 3×5 box has 8k + 12 squares, each at strip width ≥ k;
hence Σ₃ₓ₅ ≤ Σ_{k≥1} (8k+12) e^{−m₁k}, evaluated in closed form. Prove it, and check k = 1 by
listing the squares.
(e) S₂(B) := sup{‖e^{−𝒰_{h′}}‖_{L²(dμ₀)} : h′ ∈ 𝒞_E, supp h′ ⊆ B̄}: finite by Theorem C.5
(p = 2, Λ = B̄; list its hypotheses and check them), and the translation-invariance sentence
(S₂(B) depends on B through its shape only) proved from the invariance of μ₀ and of 𝒞_E.
(f) c_U: for U_Δ := λ Σ_{n≥1} a_n ∫_Δ h :Φⁿ: dz with 0 ≤ h ≤ 1, derive ‖U_Δ‖_GJS ≤ c_U :=
λ Σ_{n=1}^{2p′} |a_n| K₁ K₂^{2n} n! from the printed norms as transcribed in eq. (1) of the
record, writing out the kernel and its L² norm on Δ (|Δ| = 1); say why the n = 0 term has no
covariance and where it goes.
(g) V_* := sup_{h′} ‖V(h′)‖²_{L²(dφ₀)} ≤ λ² Σ_n a_n² n! ∫∫ C(x−y)ⁿ dx dy over [−1,1]², C the
kernel of (2μ)^{−1}, with the positivity of C stated and justified; the 9^{p′} comparison
‖Y‖₄ ≤ 3^{p′} ‖Y‖₂ taken from the proof of Theorem C.5 (quote the step and its line).
(h) The printed constants: C₇ and m₁ (Theorem 1.1.7, A8(iv)), K₁ and K₂ ≥ 1 (the norms,
A8(iii)), n̄ = 2p′+1 (A8(ii)), with their locators in the record and in GJS.

**`constants.tex` (cqft2).** Recompute by hand, line by line and independently of aqft's text,
every constant of D.3 and D.4 and of the consequences: c_U, S₂(B), A, B′, A_f, K_f, s₀, Σ₃ₓ₅,
V_*, M_B. One table: constant | formula | depends on | uniform in | derived where (section of
the note). Any discrepancy with PLAN Part 1 or with aqft's parts is a finding; list it.

**`d1.tex` (mp).** Lemma D.1 with the full chain of gate GA2:
(i) F ∈ L^p(dμ₀) for every p < ∞, for finite sums of localized monomials of type (1.1.5) or
(1.1.6) with L² kernels and n_i < n̄: write the Gaussian moment bound out (Wick monomials of
the free field; either explicit moments or Nelson's hypercontractive estimate as the record
states A4; say which);
(ii) e^{−ϱ𝒰_h} ∈ L¹(dμ₀) for every ϱ > 0 and h ∈ 𝒞_E: A3 as the record states it (quote);
(iii) Hölder with every exponent written;
(iv) α ↦ 𝒰_{h_α} is affine, hence e^{−𝒰_{h_α}} ≤ (1−α)e^{−𝒰_{h₁}} + αe^{−𝒰_{h₂}} (convexity
of exp), giving the dominator |F| |𝒰_{h₂−h₁}| (e^{−𝒰_{h₁}} + e^{−𝒰_{h₂}});
(v) Z(h_α) > 0 (Lemma C.2) and the quotient rule, giving
d/dα ⟨F⟩_{h_α} = −Cov_{h_α}(F, 𝒰_{h₂−h₁});
(vi) continuity of the derivative in α (C¹), and the integrated identity.
State exactly the class of F, and whether h₂ − h₁ (which may change sign) is used anywhere as
a cutoff (it is not: it is an observable).

**`quantifiers.tex` (mp).** For D.2, D.3, D.4 and every consequence: the order of quantifiers,
and for every constant what it depends on and what it is uniform in (PLAN: A depends on
(λ, 𝒫, m₀) and N_B and is uniform in T and s; B′ on C₇, m₁, K₁, K₂, λ, 𝒫, N_g, uniform also in
the position of I; M_B uniform in h ∈ 𝒞_E, in a and in h′). Boundary cases, each written out:
T < 1 (slab thinner than one row), T not an integer, s on a lattice line, N_g = 1, I meeting one
column only, p′ = 1, ring k = 1, a such that [a, a+2] meets three columns (the "meeting in
positive measure" reading), the n = 0 term of 𝒫. Check traps 8–11, 17, 20 and 25 of PLAN Part 8
against the drafts of aqft when they exist (read `parts/d2.tex`–`parts/d4.tex` at the end of
your work; if they are not there yet, say so in your report).

**`d2.tex` (aqft).** Lemma D.2 as stated in PLAN Part 1. Every application of (1.1.10) is
written out per gate GA1: Q₁ (a localized piece of F: type (1.1.5) or (1.1.6), its squares,
n_i < n̄), Q₂ = U_Δ (type (1.1.6), its square Δ, degrees n ≤ 2p′ < n̄), the cutoff h_α with
its membership in 𝒞_E (from `notation.tex`), the strip (its orientation and its width
d(Δ,R)), and the resulting term C₇ c_U ‖piece‖_GJS e^{−m₁ d(Δ,R)}. Then Lemma D.1 at h₁ = h^B,
h₂ = h (so 𝒰_{h−h^B} = Σ_{Δ⊄B} U_Δ, with the squares meeting supp h), the sum over pieces
and squares, and the norm additivity (1.1.9) for the sum of pieces. Quote A8(iv) as the record
states it, including "independent of h, Q₁ and Q₂", and say at which h the covariance is taken.

**`d3.tex` (aqft).** Theorem D.3 as stated in PLAN Part 1: the setting (g ∈ 𝒞_H, the interval
I, the time s and its row l_s, N_g, N_B, B = B_s(g,I) with |B| = 3N_B), the statement, and the
proof: (1) the base term ⟨F⟩_{h^B} by Cauchy–Schwarz in L²(dμ₀), Lemma C.2 (Z(h^B) ≥
e^{−λ|a₀||B|}) and S₂(B); (2) the comparison term by Lemma D.2 with R the squares of F (row
l_s, the columns meeting I) and the geometry: every square of supp h_{T,g} outside B lies in a
column meeting supp g at row distance ≥ 2 from l_s, separated from R by a strip parallel to the
time-zero line of width ≥ |l − l_s| − 1 (the case the printed proof reaches: say so), and
Σ_{Δ⊄B} e^{−m₁ d(Δ,R)} ≤ 2 N_g Σ_{j≥1} e^{−m₁ j}; (3) how F, a finite linear combination of
cylinder monomials of the record's §6 at sharp time s supported in I, is written as a sum of
localized monomials, and what the record's §6 (Proposition 6.2, Remark 6.3) gives for its
GJS norm. Boundary: T < 1 and the rows actually met by supp h_{T,g}; I meeting one column.

**`d4.tex` (aqft).** Theorem D.4 as stated: h ∈ 𝒞_E arbitrary, a ∈ ℝ, h′ real measurable with
‖h′‖_∞ ≤ 1 and supp h′ ⊆ [a, a+2]; Q_V := V(h′)(0)² written as a sum of localized monomials
of type (1.1.5) with r ≤ 2 points at time 0 and n_i ≤ 2p′ < n̄ (Wick re-expansion of the
product; this is where p. 593's "there is no restriction on r" is used; say so); R in row 0;
the box B₃ₓ₅ (rows −1, 0, 1 times the at most three columns meeting [a, a+2], enlarged by one
column on each side; |B₃ₓ₅| = 15); the base term with S₂(B₃ₓ₅), e^{15λ|a₀|}, V_* and the
9^{p′} comparison; the comparison term by Lemma D.2 with the ring sum Σ₃ₓ₅; the transverse
strips: for squares in rows −1, 0, 1 outside B₃ₓ₅ the separating strip is transverse to the
time-zero line, and at EVERY such application the text says so and points to F-T (the
master's §1 carries the sentence); then M_B as in PLAN Part 1. Say which squares are reached
by a parallel strip and which only by a transverse one.

**`consequences.tex` (aqft).** For each of Lemma 4.3(ii), Lemmas 7.1, 7.2, 7.3, 7.6,
Theorem 7.7 (its radius s₀), Theorem 5.1 (Step 5 replaced by D.4 at h = h_{T,g}, M := M_B) and
Corollary 5.2: quote the record's current statement and the lines of its proof that cite
A8(vi), (U_GJS) or C₈ (from `main.tex`, with line numbers), write the replacement text, and
check in writing: the replaced proof cites neither `eq:UGJS` nor C₈ (gate GA5), and the new
constants A, B′, A_f, K_f, s₀ appear in no statement of §§8–14 (gate GA6: grep the record and
record the command and its output). Lemma 7.6: E_{μ_g}[X_f^{2n}] ≤ A_f K_f^{2n} (2n)! with
A_f := A + B′K₁ and K_f := max{K′, √2 σ_f}, σ_f² = ⟨f, C f⟩, using
‖X_f^{2n}‖_{L²(dφ₀)} = σ_f^{2n} ((4n−1)!!)^{1/2} ≤ (√2 σ_f)^{2n} (2n)! (prove this inequality)
and the record's eq. (8); Theorem 7.7's s₀ = 1/K_f. State what changes in the proof of
Theorem 12.2 (nothing, if every statement is unchanged) and which rows of the record's
Appendix A change.

## 3. Rules (binding; AGENTS.md §3)
- Every step is one of: an explicit calculation; an application of an earlier numbered
  statement of this note; an application of a statement of the record or of a GJS printed
  statement as quoted in A8, with the invoked hypotheses listed and checked at the point of
  use. No other sources: Phases A and B make no new import (PLAN Part 3).
- "clearly", "obviously", "standard", "similarly", "by the same argument", "one can show",
  "it is easy to see", "sufficiently large/small": only if the omitted argument follows
  immediately. Every constant is derived. The order of quantifiers is stated. Thresholds are
  inequalities.
- A missing step is marked in place (`gapnote`) with one line saying what is missing. A GAP is
  not a failure of the draft; a hidden gap is.
- Status words: `proved` only for what the note proves completely from the named inputs;
  otherwise `partial` (name the extra hypothesis) or `conjectured`. The note as a whole is
  `conjectured` until audited; do not write status sentences about the record (the
  orchestrator does, from PLAN Part 8's frozen sentences).
- Never state a fact about a GJS page you did not read in this session; read the image or the
  text layer, quote verbatim, record misprints verbatim (PLAN Part 9b: "lattice side", the
  missing period on p. 597, "Theorem 1.1.10" on p. 600, and the rest).
- PLAN Part 8, traps 1–28, in particular 1, 2, 4, 5, 7, 8, 9, 10, 12, 13, 14, 20, 23, 26, 27.
  Never "U_GJS is proved". Never "unconditional". Never "CE1 follows from CE2" without the
  bounded-support qualification.
- Squares are GJS squares centred at lattice sites (F3). "decouple", not "Dirichlet" (F11).
  "h → 1", not "h ↑ 1" (F14).
- Test each new identity or inequality on one special case by hand and say so. A numerical
  check (e.g. of the ring count or the moment identity) is welcome, labelled `numerical`,
  with the script path under `WORK/parts/`; nothing is deduced from it.
- Never present a floating-point computation as a premise.

## 4. Report (`WORK/parts/REPORT-<name>.md`, written last)
1. What you drafted: files, statements, estimated pages.
2. Status of each statement (proved / partial / conjectured, in the sense of §3) with every GAP
   listed by locator.
3. Boundary cases checked, special-case tests, numerical checks (script paths).
4. Deviations from PLAN Part 1 and why (each is a finding for the audit).
5. What you could not do, and what the auditors should attack first.
6. Errors you found in the record or in PLAN.md: locator, exact text, why.
7. Build result of your test build (§5): errors, undefined references, Overfull count, pages.

## 5. Test build
In `WORK/build-<name>/`: copy `../preamble.tex`, write a stub master that `\input`s the
preamble and your parts (with `\begin{document}` ... `\end{document}` and the two `\bibitem`s of
the master if you cite), run `pdflatex -interaction=nonstopmode` twice, fix your part's LaTeX
errors. References to labels in other drafters' parts show as `??` in your stub; that is
expected and is not an error. Do not modify `WORK/comparison.tex` or `WORK/preamble.tex`.
