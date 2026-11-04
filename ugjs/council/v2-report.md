# V2 audit of the comparison note (Phases A and B of `ugjs/PLAN.md`), frozen version V1

Round V2 of `ugjs/PLAN.md` Part 5. Auditor: a fresh agent (Claude Opus 5.5) that drafted nothing of the note and did not
read the drafters' reports or the V1 reports before §§1–4 below were written. Started 2 November 2026, interrupted by a
usage limit, resumed and finished 3 November 2026. Standard: AGENTS.md §§1–5. Severity words as in AGENTS.md §2.
`WORK/` = `/private/tmp/claude-501/-Users-alex-Documents-Uni-Hannover-claude-glimm-jaffe/8bac9e45-6e21-41a1-bdb8-e018c3356462/scratchpad/phaseAB/`.

## Verdict

No CRITICAL finding, and no false mathematical statement in Lemmas D.1–D.2 or Theorems D.3–D.4. I re-derived every
constant by hand from the note's own definitions: c_U, S₂, V̄_*, I_n, b₀, the 3^{p′}/9^{p′} comparison, A, B′, A_f, K_f, s₀,
Σ̄₃ₓ₅ = 4x(5−3x)/(1−x)², the ring count 8j+12, ‖Q_V‖_GJS, M_B, and the φ⁴ numbers 362 880 and 8 709 120. Each one agrees
with Appendix A and, up to the deviations the note declares, with PLAN Part 1. Every transverse application of GJS
Theorem 1.1.7 inside Theorem D.4 is flagged.

- **D.1–D.3 can be `proved, conditional on the V3 repairs` as written,** once one condition is stated. Lemma D.1 depends on
  the record's unproved identification 𝒰_h = L²-lim 𝒰_{h,κ}, and §3 attaches no conditional status to it (V2-2, MINOR).
- **D.4 cannot yet be `proved` as written.** Two things block it:
  1. The GAP the note itself marks: the record never constructs the Wick powers in its V(h).
  2. An unmarked step (V2-1, MAJOR by the letter of AGENTS §2, no mathematical risk). The proof uses two different
     constructions of the same observable Q_V without showing that they agree:
     - Step 4 uses Definition N.24's regularization, through Lemmas D.1, D.2 and N.30;
     - Step 2 uses Lemma N.21's J₀-construction.

  The repair is about a third of a page and needs no new mathematics.
- **The replaced proofs of §8 are correct against the record's statements,** which I quote in §2.4. The defects are
  MINOR bookkeeping:
  - the N_I edit misses main.tex l. 448 and A8(ii), ll. 659–663;
  - the gate records for GA5 and GA6 contain wrong counts and an incomplete list;
  - status words and cross-references are inconsistent in places.

The two source claims the brief asked me to confirm are confirmed on the page images:
- p. 594 prints (1.1.11) with an upright digit, "0(1)". The italic "O(1)" of (1.1.10) on the same page looks different
  (400 dpi crops in `WORK/audits/v2/`). The note's gate record calls this reading "unconfirmed".
- The strip-definition sentence before Theorem 1.1.7 has no closing period.

## 0. Object, version, what was read

- **Object.** `WORK/frozen-v1/`:
  - `comparison.pdf`, 59 pp; sha256 `7e393b9a440fe6a29af13d921aa62b7ecf59e363332355c5981ed0d7be485f87`, identical to
    `WORK/comparison.pdf`;
  - `comparison.tex` and `preamble.tex`;
  - `parts/{notation,d1,d2,d3,d4,quantifiers,consequences,constants,gates}.tex`, identical to `WORK/parts/`
    (`diff -r`, no output);
  - the three check scripts and `aqft_checks.out`.

  All of these I read in full. I re-checked the hash on resuming (3 Nov), and nothing had changed. Printed page = PDF page
  index for the note. I took statement numbers and pages from `WORK/comparison.aux`.
- **Record.** `glimm_jaffe/part_i/main.tex` (3181 lines, mtime 2 Nov 2026 15:35:23). I read:
  - ll. 372–1137 (§2, A1–A8, Remark 2.5, §2.6, §3);
  - ll. 1136–1725 (§§4–7);
  - ll. 1743–1830 (Prop. 8.1);
  - ll. 2052–2311 (§§10–11);
  - ll. 2388–2449 (Thm 12.2);
  - ll. 2655–2686 (App. A);
  - ll. 2864–3083 (App. C from Prop. C.1 to Prop. C.7).

  I checked 36 labels against `main.aux`. The 35 that `labels-main.txt` lists agree with it in number and page;
  the 36th, `eq:UGJS` (p. 11), is not in the table.
- **Plan.** `ugjs/PLAN.md`, all of it (1004 lines).
- **V3 report.** `ugjs/council/v3-appendix-c-report.md`, all of it. It differs from `WORK/audits/V3-appendixC-report.md`
  only by the orchestrator's errata header.
- **GJS 1974.** I rendered PDF pp. 6 and 10–14 (printed pp. 589 and 593–597) at 150 dpi, and PDF pp. 11–12 at 400 dpi, into
  `WORK/audits/v2/`.

## 1. Findings

### CRITICAL

None.

### MAJOR

**V2-1. Theorem D.4 uses two constructions of the sharp-time Wick observable Q_V and never identifies them.**

*Locators:*
- §6, Lemma N.41(i) and its proof: `d4.tex` l. 58 and ll. 80–82, PDF p. 34.
- Theorem D.4, Steps 1, 2 and 4: `d4.tex` ll. 123–126, 135–136 and 163–164, PDF p. 35.
- Lemma N.21: `notation.tex` ll. 938–998, PDF pp. 15–16.
- Definition N.24(b): `d1.tex` ll. 198–213, PDF p. 19.

*Text:*
- Step 2: "Lemma~\ref{aux:notation-hyper}(ii), applied to $Y:=V(h')(0)$, gives
  $\|Q_V\|_{L^2(\dmu)}=\|Y^2\|_{L^2(\dmu)}\le9^{p'}V_*$".
- Lemma N.21(i): "Put $Y_r:=\lambda a_rJ_0W_r$; then $Y=J_0V(h')=\sum_rY_r$".
- Step 4: "Apply Lemma~\ref{lem:D2}(a) with $F=Q_V$ and its pieces $Q_{n,n',k,k'}$".
- Lemma N.41(i): "$Q_V=\sum_{n,n'}\sum_{k,k'}Q_{n,n',k,k'}$". Its proof reads: "expand $V(h')(0)^2$ as in Step~1 of
  the proof of Theorem~5.1 of the record … and split each of the two spatial integrals over the columns".

*Why it fails.* The two steps of D.4 must bound the same element of L²(dμ₀), and the note builds that element two ways.
- **For Lemma D.2.** Its proof invokes Lemma D.1, which needs F ∈ 𝔉, and Lemma N.30, which gives L⁴ membership via
  Lemma N.26(b). So the pieces Q_{n,n′,k,k′} are the localized monomials of Definition N.24(b). These are L²-limits of
  ∫w(x⃗) Π:Φ_κ(0,x_i)^{n_i}:_{c_κ} dx⃗. Here Φ_κ(0,x) = Φ(δ_κ((0,x)−·)) is the **two-dimensional** mollified field,
  Wick-ordered at its variance c_κ.
- **For the base term.** Step 2 uses Y = J₀V(h′). This is the J₀-image of the L²(dφ₀)-limit of
  ∫h′(x):φ₀(ρ_κ(x−·))^n:dx, built with the **one-dimensional** mollifier ρ_κ of Lemma N.20.

So the base term bounds ∫(J₀V(h′))²dq_{h^B}, while the comparison term bounds ⟨ΣQ_{n,n′,k,k′}⟩_h − ⟨ΣQ_{n,n′,k,k′}⟩_{h^B}.
They add up to the bound of D.4 only if the two elements are equal. No statement of the note asserts this with a proof:
- the GAP after Lemma N.20 concerns the record's V(h), not the note's two constructions;
- Lemma N.26(c)–(d) and Lemma N.20(iii) compute equal *norms*, n!∬ff Cⁿ, which do not identify the elements;
- the proof of N.41(i) is a formal expansion.

The step is true. Both limits lie in the n-th chaos and have the same pairings. That makes this the AGENTS §2 MAJOR case
"asserted without justification … no repair is given in the text". It carries no mathematical risk; V3 graded its M-3 the
same way. For Theorem D.3 the analogous identification concerns degree-1 factors only, Φ_κ-smearing against δ_s⊗f, and is
immediate. It is not part of this finding.

*Repair.* Add a lemma. Let f be real, bounded, with compact support, and 0 ≤ n ≤ 2p′. Let X be the one-factor
type-(1.1.5) monomial of Definition N.24(b) at time 0 with kernel f, and W_n(f) the limit of Lemma N.20(iii) with f in
place of h′. Then X = J₀W_n(f) in L²(dμ₀). Proof:
1. By Lemma N.22 (ℓ = 2), E[X^{(κ)}·J₀W_{n,κ′}] = n!∬f(x)f(y)Γ_{κκ′}(x,y)ⁿdxdy, with
   Γ_{κκ′}(x,y) := E[Φ_κ(0,x)Φ(0,ρ_{κ′}(y−·))].
2. Γ_{κκ′}(x,y) is an average of G over a 2D mollifier of radius 1/κ and a spatial 1D mollifier of radius 1/κ′. Bound it
   by a majorant of the form of N.23(iii) and N.20(ii), and note that it converges to G(0,x−y) = C(x−y) for x ≠ y.
3. Dominated convergence gives E[X·J₀W_n] = n!∬ffCⁿ = ‖X‖² = ‖J₀W_n‖², hence ‖X − J₀W_n‖ = 0.
4. Products follow from N.26(c) and the multiplicativity of J₀.

Alternatively, once the GAP's import is made (Simon Thm V.2(b), per V3 C5.5), show that both constructions equal the
imported :φⁿ(h′):.

A third route uses one construction throughout: take the pieces of Q_V as products of J₀-objects. D.1 needs only
F ∈ L^{p₀} (Remark N.27(a)), and L⁴ membership then comes from N.21 (under R8) instead of N.26(b). This leaves only the
reading question of which construction is GJS's (1.1.5) (C5 item 10).

State D.4 as "proved, conditional on …" only after one of these routes is written.

*Severity:* MAJOR (by the letter; no mathematical risk).

### MINOR

**V2-2. Lemma D.1 is not given its conditional status, and Remark N.27(b) overstates its independence from Appendix C.**

*Locators:*
- §3, proof of Lemma D.1, Step 1: `d1.tex` ll. 402–421, PDF p. 23.
- Remark N.27(b): `d1.tex` ll. 507–514, PDF p. 24.
- §7: `quantifiers.tex` ll. 67–70, PDF p. 39.
- Gate record: `gates.tex` ll. 6–8 and 16–18, PDF pp. 58–59.

*Text:*
- Step 1: "The record identifies $\Uc_h$ … with the limit in $L^2(\dmu)$ of $\Uc_{h,\kappa}$ (Appendix~C, notation
  paragraph … ``so that $\Uc_{h,\kappa}\to\Uc_h$ in every $L^p(d\mu_0)$''…) and gives no other construction of $\Uc_h$; the
  V3 audit … records this as its finding M-3."
- Remark N.27(b): "Neither Theorem~C.5 nor Lemma~C.2 of the record nor Assumption~A4 is used … Lemma~\ref{lem:D1} is
  qualitative and carries no constant."
- Gate record: "Lemma~\ref{lem:D1} proved (mp; one named dependence…)".

*Why it fails.* The affine relation (8), 𝒰_{h_α} = (1−α)𝒰_{h₁} + α𝒰_{h₂}, rests on the record's sentence at
main.tex ll. 2918–2920. V3 calls that sentence "asserted and proved nowhere in the record" (V3 §7, m-1). It "follows from
Lemma C.4 and the comparison" in L^p; in L² it follows from Lemma C.4 alone, and Lemma C.4 needs R1–R5, R8 and R9.
Alternatively, it follows from R8's definition 𝒰_h := λΣa_n:Φⁿ(h):, which is linear in h.

Either way D.1 is "proved, conditional on R8 (or on Lemma C.4 after R1–R10)". By the note's own rule (notation.tex
ll. 28–31) every statement using these results carries that status. D.1 carries none in §3 or §7, and Remark (b) reads as
if D.1 were free of Appendix C. The dependence is named, so this is bookkeeping (AGENTS §2, "proved, conditional on").

*Repair.* Add after Lemma D.1: "proved, conditional on repair R8 of the V3 audit (which defines 𝒰_h linearly in h); the
regularized-limit route of Step 1 is conditional on Lemma C.4 (R1–R10)". Qualify Remark (b) to match.

*Severity:* MINOR.

**V2-3. Conflicting conditionality of Lemma C.2.**

*Locator:* §3, proof of Lemma D.1, Step 4: `d1.tex` ll. 479–481, PDF p. 24.

*Text:* "(Lemma~C.2 … gives the explicit bound … it is proved conditional on the repairs R1--R10 of the V3 audit, and this
proof does not use it.)"

*Why it fails.* Elsewhere the note says Lemma C.2 is proved conditional on R8 alone:
- `notation.tex` ll. 29–31, p. 2;
- Remark N.32, `d3.tex` l. 53, p. 29;
- `consequences.tex` ll. 24–25, p. 43;
- `quantifiers.tex` l. 103, p. 39.

V3 §2 agrees: "After R8, Lemma C.2 is `proved` from A3 and the Simon definitional import". (The clause "Z(h) < ∞ by
Theorem C.5" of the statement also follows from A3, V3 C2.6.)

*Repair.* Replace "R1--R10" by "R8".

*Severity:* MINOR.

**V2-4. Two status words for the same statements.**

*Locators:* `comparison.tex` ll. 20–21, PDF p. 1; `notation.tex` l. 17 against ll. 28–36, PDF p. 2; `constants.tex`
ll. 14–15 against ll. 302–306, PDF pp. 51 and 55.

*Text:* "Every statement of this section is \emph{conjectured} in the sense of the plan until audited." Then, a few lines
on, for the same statements (Prop. N.15, Lemmas N.5(iv), N.13(iii)–(iv), N.18(iii)–(iv), N.21): "is \emph{proved,
conditional on repairs of the V3 audit}".

*Why it fails.* AGENTS §2 requires exactly one status word per claim. A reader cannot tell which of the two applies now.

*Repair.* Write "conjectured (status after the audits: proved, conditional on …)" wherever the conditional form is meant
as a target.

*Severity:* MINOR.

**V2-5. The N_I edit map is incomplete, and one claim about A8(ii) is wrong.**

*Locator:* §8.1, block `sec6-NI` and the following paragraph: `consequences.tex` ll. 37–52, PDF p. 44.

*Text:*
- "\emph{\S6, l.~1359, replaced:} $N_I:=\#\{k\in\Z:\ |I\cap[k-\tfrac12,k+\tfrac12)|>0\}$…"
- "The sentence of Assumption~A8(ii) (ll.~659--663) that ``the same computation on the squares of p.~593 gives the same
  constants'' is then true".

*Why it fails.* Two lines of the record survive the edit.
1. The notation-freeze table, main.tex l. 448, still reads "$N_I$ & number of unit cells $[j,j+1)$ meeting the interval
   $I$ in positive measure". It would contradict the replaced l. 1359. The edit lists l. 1359, Lemma 6.1, the proofs of
   6.1–6.2 and (in §8.7) Appendix A, ll. 2670 and 2676, but not l. 448.
2. A8(ii), ll. 659–661, says "The cells $[j,j+1)$ used in §§5–6 are this lattice shifted by one half unit". After the
   edit §6 counts on columns, so that clause becomes false, and the sentence is not "then true" without its own edit.

The counterexample is right ((0.4,0.6): N_I = 1, N^□ = 2), and so is the repaired Proposition 6.2. Theorem 5.1,
Steps 2–4, still counts "cells", but harmlessly: at most three columns meet an interval of length 2 in positive measure
too (Lemma N.11(i), §7.3(8)).

*Repair.* Add l. 448 ("columns [k−½,k+½) of the squares of p. 593") and A8(ii), ll. 659–663, to the replacement block.

*Severity:* MINOR.

**V2-6. The GA5 gate record has a wrong count and an incomplete list.**

*Locators:* App. B, `gates.tex` ll. 41–43, PDF p. 59; §8.8, `consequences.tex` ll. 394–397, PDF p. 50.

*Text:*
- "aqft's grep over the ten replacement blocks: no hit".
- "Outside \S\S4--7 the record still cites $(\UGJS)$ in \S1.4 (ll.~290, 302), in Assumption~A8 (ll.~710--803, 868),
  …(l.~2417), … (ll.~2737, 2776) and … (l.~3075)".

*Why it fails.*
- `consequences.tex` has **8** blocks: `sec6-NI`, `lemma-4.3-ii`, `lemma-7.1`, `lemma-7.2`, `lemma-7.3`, `lemma-7.6`,
  `theorem-5.1` and `corollary-5.2`, with BEGIN lines 37, 73, 115, 153, 170, 216, 288 and 328.
  `grep -c BEGIN-REPLACEMENT` prints 10 only because of the header comment (l. 3) and the verbatim command (l. 390).
- `grep -n -e 'eq:UGJS' -e 'U_{\rm GJS}' -e 'UGJS' main.tex` also hits ll. 68, 72, 76, 81 (title page) and 184, 210, which
  the "outside" list omits.

I re-ran the GA5 command itself and its result is right (V2 §3).

*Repair.* Write "eight replacement blocks", and complete the outside list or say it is partial.

*Severity:* MINOR.

**V2-7. The GA6 record's list of statements that carry M is incomplete.**

*Locator:* §8.8, `consequences.tex` ll. 416–420, PDF p. 50.

*Text:* "…and $M$ (through Theorem~5.1: the statements of Lemma~10.2, eq.~(25), of Lemma~10.5 and Theorem~11.1 through
$\Psi_{m_1}$, and of Theorem~12.2, items (1) and (5))".

*Why it fails.* Two more statements contain M (main.tex ll. 2121–2129 and 2152–2158):
- Lemma 10.3, eq. (26): "2Me^{−γr_j/4}", "2M";
- Proposition 10.4, eq. (27): "32M Σ…".

The GA6 grep cannot see them, because it matches labels, not the letter M. The conclusion (trap 10, no GA6 failure) is
unaffected.

*Repair.* Add Lemma 10.3 and Proposition 10.4.

*Severity:* MINOR.

**V2-8. A stale quotation, and inaccurate claims about which statements change.**

*Locators:* §8.9, `consequences.tex` ll. 430–432, PDF p. 50; §8 intro, ll. 15–17, PDF p. 43; §1, `comparison.tex`
ll. 56–59, PDF p. 2.

*Text:*
- §8.9: "(master \S1, ``it does not change the statement of any numbered result of the record'')".
- §8 intro: "they keep their form and change their constants".
- §1: "changes no statement except through the value of the constants that contained $C_8$ (… the constants of
  Lemmas~7.1 and 7.6 and the radius of Theorem~7.7 …)".

*Why it fails.*
- The quoted sentence does not occur in the frozen §1.
- Lemma 7.1's replaced statement gains a term: C₈𝔫(Q)² becomes A‖Q²‖_{L²(dφ₀)} + B′𝔫(Q)². Its form changes, not just a
  constant.
- Theorem 7.7's *statement* (main.tex ll. 1639–1641) contains no radius; s₀ lives in its proof.

*Repair.* Drop the stale quotation. Write "Lemma 7.1's statement gains the term A‖Q²‖_{L²}", and "the radius in the
proof of Theorem 7.7".

*Severity:* MINOR.

**V2-9. The symbol N^col_I is used but never defined.**

*Locators:* §7, `quantifiers.tex` l. 115, PDF p. 39; App. A.6 (C2), `constants.tex` l. 453, PDF p. 57.

*Text:* "bounded with the column count ($N^\square_I$ of Remark~\ref{aux:notation-counts}, $N^{\rm col}_I$ of
\S\ref{sec:d3})", and "its $N^{\rm col}_I$ is the $N^{\square}_I$".

*Why it fails.* §5 (`d3.tex` l. 21) writes N^□_I, and N^col_I occurs nowhere else. This violates AGENTS 3.8.

*Repair.* Delete both occurrences, or define the symbol.

*Severity:* MINOR.

**V2-10. §7 still writes s₀ without the restriction e_j ≠ 0.**

*Locator:* §7, `quantifiers.tex` l. 146, PDF p. 40.

*Text:* "$s_0:=\min_{j\le k}(2kK_{e_j})^{-1}$".

*Why it fails.* For e_j = 0, K_{e_j} = 0, and Lemma 7.6 assumes f ≠ 0. §8.5 and Remark N.52 restrict the minimum to
e_j ≠ 0. A.6(C4) records the discrepancy, but the frozen §7 is unchanged.

*Repair.* Write "min_{j: e_j≠0}".

*Severity:* MINOR.

**V2-11. The note contradicts itself on Appendix A's rows, and (C6) misdescribes Lemma N.46.**

*Locators:* App. A.4 closing paragraph, `constants.tex` ll. 377–381, PDF p. 56; Remark N.53(c), ll. 295–297, PDF p. 55;
(C6), ll. 472–475, PDF p. 58; §8.7, `consequences.tex` ll. 367–376, PDF p. 49.

*Text:*
- A.4: "this changes the rows $M^2$, $M^2$ ($\varphi^4$), $K'$ and $\widehat C_Q$ and adds rows for $c_U$, $S_2$, $A$,
  $B'$, $A_f$, $K_f$".
- §8.7: "Unchanged: … $\widehat C_Q$ …"; its new rows include $s_0$, $V_*$, $\overline\Sigma_{3\times5}$ and $M_B$.
- N.53(c): "Proposition~7.5 keeps $\widehat C_Q$".
- (C6): "Lemma~\ref{aux:constants-comparison} uses the strips of Lemma~\ref{aux:notation-strip}, which may have width $0$
  next to the box".

*Why it fails.*
- Whether the Ĉ_Q row changes, and which rows are new, is stated two ways. Ĉ_Q's formula is unchanged, so §8.7 is right.
  A.4 follows PLAN Part 6, which is stale on this point.
- Lemma N.46 assumes "a strip $S_\Delta$ of width $w_\Delta>0$", so (C6) is wrong about it.

*Repair.* Align A.4 with §8.7, and correct (C6).

*Severity:* MINOR.

**V2-12. The GA3 partial-check record overstates agreement with the plan.**

*Locator:* App. B, `gates.tex` ll. 44–46, PDF p. 59.

*Text:* "GA3 (Appendix~\ref{app:constants}, cqft2, independent of aqft's text: every constant agrees with PLAN Part~1 and
with \S\S\ref{sec:d3}--\ref{sec:d4})".

*Why it fails.* Several constants differ from PLAN Part 1, as the note itself records:
- Appendix A.5 lists the differences: (D1) K_f and 𝔫 with N^□ rather than N_I; (D2) s₀ rather than 1/K_f; (D3) the
  transverse squares.
- The note's M_B uses Σ̄₃ₓ₅, not the plan's R-dependent Σ₃ₓ₅.

So "every constant agrees with PLAN Part 1" is false as written. The constants do agree with §§5–6, which I re-derived
(§2.1).

*Repair.* Write "agrees with §§5–6; the deviations from PLAN Part 1 are A.5 (D1)–(D4)".

*Severity:* MINOR.

**V2-13. §1's list of inputs is incomplete and partly inaccurate.**

*Locator:* §1, "Inputs, by name": `comparison.tex` ll. 65–69, PDF p. 2.

*Text:* "From the record: A3 …, A4 (free hypercontractivity, through Theorem~C.5), A8(i)--(iv) …, Lemmas~4.1--4.4,
Proposition~6.2, Remark~6.3, Lemma~7.4, Lemma~C.2, Theorem~C.5; and the Gaussian moments … No new import is made."

*Why it fails.*
- **Lemma C.4 is load-bearing and missing.** It enters through Lemma N.5(iv) → N.18(iv) → Step 3 of D.2, and through
  Lemma N.13(iii) → Prop. N.15(iii), where S₂ depends on the shape only. D.4's uniformity in a needs the latter.
- **Other inputs are missing:** Remark 2.5 (N.21(i), N.33), A2, Lemma 3.1(ii), A5(i) (the Lemma 4.3(ii) replacement) and
  Lemma 6.1.
- **Lemma 7.4 is listed** although no proof of the note uses it as a premise.
- **A4 is used directly,** not only through Theorem C.5: Lemma N.21(ii) applies A4's abstract form.
- **"No new import is made" needs qualifying.** It is literally true, but every conditional status rests on R8, which V3
  writes as an *import paragraph*, and the GAP's closure needs a further one (Simon Thm V.2(b)).

*Repair.* Complete the list, and say "no new import is made by the note; its conditional statuses rest on the import
paragraph R8 proposed by V3, and on the import that would close the GAP".

*Severity:* MINOR.

**V2-14. "The replaced proof of Lemma 4.3(ii) uses Assumption A3 only" is inaccurate.**

*Locators:* §8 intro, `consequences.tex` l. 27, PDF p. 43; replacement block `lemma-4.3-ii`, ll. 73–94, PDF p. 44.

*Text:* "The replaced proof of Lemma~4.3(ii) uses Assumption~A3 only." In the block: "For the observables to which the
lemma is applied ($|V(h)|$ in \S5, cylinder monomials in \S7), $F(\Phi(s,\cdot))\in L^4(d\mu_0)$ for every $s$ (Gaussian
moments of the free field, Appendix~D, \S3)".

*Why it fails.*
- The block also uses the Gaussian moments of §3, and its own Check paragraph (ll. 95–98) lists them and A5(i).
- For F = |V(h)|, membership V(h)(Φ(s,·)) ∈ L⁴(dμ₀) follows from §3 only through the identification of the record's V(h)
  with the note's construction. That is the GAP of §2.7, which the block does not name. A5(i) is named only for
  "Fψ_a ∈ ℋ".

The mathematics of the block is right: the Hölder bound Z(h)^{−1}‖F‖₄²‖e^{−𝒰_h}‖₂ and part (i) at t = 0.

*Repair.* State the inputs, and for |V(h)| either cite the GAP or route the square moment at t = 0 through A5(i) and (2).

*Severity:* MINOR.

**V2-15. A false meta-claim in the statement of Lemma N.18(iii).**

*Locator:* §2.6, Lemma N.18(iii): `notation.tex` ll. 679–684, PDF p. 12.

*Text:* "The coefficient $a_0$ enters the estimates of this note only through the lower bound of Lemma~C.2 …, and through
$\Uc_{h'}$ inside $S_2$".

*Why it fails.* a₀ also enters V_* and the bound on ‖Q_V‖_GJS, through the observable V(h′) ∋ λa₀∫h′. §7.3(9) says
exactly this ("In $V_*$ and in $\GJS{Q_V}$ the term $n=0$ stays").

*Repair.* Write "the interaction's coefficient a₀ enters … only through …".

*Severity:* MINOR.

**V2-16. F-T is not used verbatim, uncontrolled orientations go unflagged, and the Theorem 5.1 replacement omits F-T and
the GAP.**

*Locators:*
- §1: `comparison.tex` ll. 47–53, PDF p. 1.
- Lemma D.2(b) and Remark N.31(2): `d2.tex` ll. 120–125 and 227–233, PDF pp. 26 and 28.
- Lemma N.46, last sentence: `constants.tex` ll. 32–34, PDF p. 51.
- Block `theorem-5.1`: `consequences.tex` ll. 288–312, PDF p. 48.

*Text:*
- §1: "…in the plan's frozen sentence F-T, adapted to this note: … Lemma~7.4 of the record uses only that case;
  Theorem~\ref{thm:D4} of this note also uses the transverse case …".
- N.46: "the bound also holds with $d(\Delta,R)$ in place of $w_\Delta$; the orientations are then not controlled".

*Why it fails.* Three separate problems:
1. PLAN Part 8 requires each frozen sentence "verbatim at its first mention in each document". The note adapts F-T, and
   says so.
2. D.2(b) and N.46's last sentence apply Theorem 1.1.7 across widest, possibly tilted or transverse, strips. They are
   disclosed in prose but not by F-T. D.2(b) is "not used below".
3. The replacement text of Theorem 5.1, Step 5, the text that would enter the record, names neither the transverse case
   nor the GAP. Only the Check paragraph outside the block does. PLAN Phase B: "F-T appears at every transverse
   application".

*Repair.*
1. Use F-T verbatim and add the note-specific clause after it.
2. Attach F-T to D.2(b) and to N.46's last sentence, or delete them.
3. Add to block `theorem-5.1`: "(through Theorem D.4, which uses GJS Theorem 1.1.7 also across transverse strips, F-T;
   and the GAP of …)".

*Severity:* MINOR.

**V2-17. The replaced statement of Lemma 7.6 contains an unproved, partly inaccurate claim.**

*Locator:* block `lemma-7.6`, `consequences.tex` l. 230, PDF p. 47.

*Text:* "\emph{The radius $1/K_f$ is an artefact of the route through the GJS norm.}"

*Why it fails.*
- Inside a lemma statement it asserts non-intrinsicness, which nothing proves.
- The component √2σ_f of K_f comes from the base term A‖X_f^{2n}‖_{L²(dφ₀)}, not from the GJS norm.

§7 has the correct wording (trap 25): "nothing in the note shows that it is intrinsic to $\mu_g$".

*Repair.* Move a remark of §7's wording outside the statement.

*Severity:* MINOR.

**V2-18. The note records no run of two of its check scripts.**

*Locators:* Remark N.12(c), `notation.tex` ll. 500–504, PDF p. 9; A.3, `constants.tex` ll. 216–217, PDF p. 53.

*Text:* "\emph{Numerical check} (\texttt{parts/cqft2\_ringcheck.py}; nothing is deduced from it): … confirms $8j+12$…".

*Why it fails.* `aqft_checks.out` records the interpreter and output of its script. For `cqft2_ringcheck.py` and
`check_d1.py` no output file, interpreter, versions or run date is recorded (AGENTS 6.2–6.3). I re-ran both
(`numerical`): all checks pass (§3).

*Repair.* Store the outputs next to the scripts.

*Amendment, made after reading the drafters' reports (§5), and marked as such.* Run records do exist outside the frozen bundle:
- `WORK/build-cqft2/ringcheck-output.txt` (15:54, "ALL CHECKS PASSED");
- `REPORT-mp.md` §3, which records the interpreter, versions and seed of `check_d1.py`.

The note does not reference either, and `frozen-v1/` does not contain them. The finding is reduced to: reference the records from the note, and include them in the frozen bundle.

*Severity:* MINOR.

**V2-19. The note cites the V3 report under two paths.**

*Locators:* `notation.tex` l. 19, PDF p. 2; Remark N.32, `d3.tex` l. 48, PDF p. 29; `gates.tex` l. 10, PDF p. 58.

*Text:* "report \texttt{audits/}\allowbreak\texttt{V3-appendixC-report.md}" against
"\texttt{ugjs/council/v3-appendix-c-report.md}".

*Why it fails.* The scratchpad copy lacks the council copy's errata header: R1–R10 versus "R1–R8", and Simon chapter I
versus chapter V.

*Repair.* Cite the council copy throughout.

*Severity:* MINOR.

**V2-20. Small locator and wording slips.**

*Locators:*
- `notation.tex` l. 838, PDF p. 14: "(as in the proof of Proposition~3.2 \cite[p.~15]{R})".
- `comparison.tex` ll. 62–63 and l. 18, PDF pp. 1–2: "The two open human readings that it rests on … C5 items 1--4 and
  10--13", and "Status (31 October 2026)".

*Why it fails.*
- The Wick generating-function sentence of Proposition 3.2's proof is on the record's p. 16, as `d1.tex` l. 44 correctly
  says.
- "Two" readings are eight items.
- The status paragraph is dated 31 October, but describes a note with parts and the V3 audit of 2 November.

*Repair.* Correct each.

*Severity:* MINOR.

**V2-21. Lemma N.21(ii) applies R8's chaos action to the note's own chaos without identifying the two.**

*Locator:* §2.7, `notation.tex` ll. 828–836 and 985–988, PDF pp. 14–15.

*Text:* "$\mathcal H_n:=\mathcal H_{\le n}\ominus\mathcal H_{\le n-1}$ (the $n$-th Wick chaos)", and "conditional on the
repair R8 of the V3 audit, which imports the action $\Gamma(e^{-t})Y_r=e^{-rt}Y_r$".

*Why it fails.* R8 imports Simon (I.32) on Simon's Γ_r: the closed span of the Wick monomials :φ(f₁)⋯φ(f_r):. The note
proves Y_r ∈ ℋ_r, defined by orthogonal differences. The identity ℋ_r = Γ_r is standard but unstated.

*Repair.* One sentence: J₀W_{r,κ} is a Bochner integral of the Wick monomials :Φ(0,ρ_κ(x−·))^r:, with all r test
functions equal, so J₀W_r ∈ Γ_r directly.

*Severity:* MINOR.

**V2-22. (About the record, not the note.) A8(vii′) silently corrects a misprint.**

*Locators:* `part_i/main.tex` l. 814 (A8(vii′)); the note's `gates.tex` ll. 35–37, PDF p. 59.

*Text:*
- Record: "\le O(1)e^{-m_1d/2} \tag{1.1.11}".
- Note: "mp reads (1.1.11) on p.~594 as printed with an upright digit, ``0(1)'', … this reading is unconfirmed".

*Why it fails.* At 400 dpi (`WORK/audits/v2/cmp-O1-vs-01.png`) p. 594 prints the italic capital "O(1)" in (1.1.10) and an
upright, narrow "0(1)" in (1.1.11). The glyph matches the upright digit "1" beside it. On p. 595 the summed bound uses
italic "O(1)" again (`crop-p595-sum.png`). The record's l. 814 thus corrects a misprint silently (trap 27; PLAN Part 9b).

*Repair.* Record "0(1) [sic]" at l. 814, and add the item to PLAN 9b. Update `gates.tex` to "confirmed (V2)".

*Severity:* MINOR.

## 2. Holds (checked this session)

### 2.1 Strand 1: geometry and constants (recomputed by hand)

**Squares and conventions.**
- Definition N.1 and Remark N.2(i)–(iii).
- l_s = ⌊s+½⌋. A lattice-line time s = l − ½ goes to row l.
- Half-open squares partition ℝ²; their closures are p. 593's squares. The row convention leaves (1.1.8) unchanged.

**Counts (Remark N.3).**
- N^□_I ≤ ⌊L⌋+2.
- (−0.1,0.1): N_I = 2, N^□ = 1. (0.4,0.6): N_I = 1, N^□ = 2.
- (7) fails with N_I on GJS squares: √2K₁K₂²‖f‖₂ > K₁K₂²‖f‖₂.
- (8) fails too (Remark N.35): the four pieces give 2·K₁K₂⁴·2!·½ + 2·K₁K₂⁴·½ = 3K₁K₂⁴ > 2K₁K₂⁴.
- (N.a) holds with N^□.

**Strips.**
- Definition N.6 and Lemma N.7(i)–(v): widths ρ_t − 1 and ρ_x − 1; the rows-next-to-R argument; monotonicity.
- Remark N.8: the counterexample R = {Δ₀,₀, Δ₀,₄}, Δ = Δ₀,₂ admits no strip.
- Remark N.9: the tilted width is 4/√2 = 2√2.
- Lemma N.29: the widest strip is attained, by continuity of ν ↦ b(ν) − a(ν) on the circle.

**Rings (Lemma N.11).**
- Exactly three columns k_a, k_a+1, k_a+2 meet [a,a+2], since (a−½, a+5/2] contains three integers.
- |B₃ₓ₅| = 15.
- |𝓛_j| = (3+2j)(5+2j) − (1+2j)(3+2j) = 8j+12; ring 1 has 20 squares, 14 in rows ±2 and 6 in the side columns.
- Widths: parallel l−1 = j for |l| = 1+j; transverse j for side columns k_a−1−j and k_a+3+j. A parallel strip has width
  ≤ |l|−1 when |l| ≤ j, and none of positive width when |l| ≤ 1. Corners admit both.
- Closed form Σ(8j+12)x^j = 8x/(1−x)² + 12x/(1−x) = 4x(5−3x)/(1−x)²; at x = ½ it gives 28, and the coefficients are
  20, 28.
- The 3×4 box has rings 8j+10 (§7.3(8)).

**S₂.**
- Lemma N.13: T_a preserves μ₀; Φ_κ(z)∘T_a = Φ_κ(z+a), using evenness of δ_κ; 𝒰_{h,κ}∘T_a = 𝒰_{τ_ah,κ} pointwise; limits by
  Lemma C.4.
- Prop. N.15(i)–(iv): 1 ≤ S₂ < ∞, monotone, and translation-invariant. Hence S₂ depends on the shape only, conditional on
  R1–R10. This is the "translation-invariance sentence" V3 left unchecked; the note's proof is correct given C.4.

**c_U and the interaction (Lemma N.18).** From (1.1.7) as printed (p. 594 image: K₁[Π K₂^{2N(Δ)}N(Δ)!]‖w‖₂, (1.1.9) "‖Q‖ =
Σ_i‖Q_i‖"), with N(Δ) = n and ‖λa_n h1_Δ‖₂ ≤ λ|a_n|:
- c_U = λΣ_{n=1}^{2p′}|a_n|K₁K₂^{2n}n!, uniform in Δ and h;
- Cov(F, U_{Δ,0}) = 0;
- the decomposition (iv), given N.5(iv).

**V_* (Lemmas N.19 and N.20).**
- C(u) = (4π)^{−1}∫t^{−1}e^{−tm₀²−u²/4t}dt = K₀(m₀|u|)/(2π).
- C ≤ (4π)^{−1}(b₀ + 2|log|u||), with b₀ = log 4 + e^{−1} + m₀^{−2}.
- I_n ≤ (4π)^{−n}2^{n+1}(2b₀ⁿ + 2ⁿ(n! + (log 2)ⁿ)).
- c_ρ = 3‖ρ‖_∞/π for min κ ≥ 6, with both cases of (ii).
- V̄_* = λ²Σ_{n=0}^{2p′}a_n²n!I_n, which equals PLAN Part 1's bound.

**3^{p′} and 9^{p′} (Lemma N.21).** q = 4 gives e^{2t} = 3, ‖e^{−t}1‖² = 1/3 = (2−1)/(4−1), and
‖Z‖₂ ≤ e^{2p′t}‖Y‖₂ = 3^{p′}‖Y‖₂. Then ‖Y²‖₂ = ‖Y‖₄² ≤ 9^{p′}V_*. The Gaussian test 3^{1/4}σ ≤ 3σ also checks.

**A and B′ (Theorem D.3).**
- A = e^{3λ|a₀|N_B}S₂(B), with |B̄| = 3N_B.
- B′ = 2C₇c_U N_g x/(1−x): each charged column contributes two rows per width j ≥ 1.

**‖Q_V‖_GJS and M_B (Lemma N.41, Theorem D.4).**
- The weight is ≤ K₁K₂^{8p′}(4p′)!, since n!n′! ≤ (n+n′)! and K₂ ≥ 1. There are 9 ordered column pairs, and
  ‖h′_k‖₂ ≤ 1.
- M_B² = e^{15λ|a₀|}S₂(B₃ₓ₅)9^{p′}V_* + C₇c_UΣ̄₃ₓ₅·9K₁K₂^{8p′}(4p′)!λ²(Σ|a_n|)².
- φ⁴: c_U = 24λK₁K₂⁸, 9·8! = 362 880, 24·362 880 = 8 709 120, 81·24 = 1944, V̄_* = 24λ²I₄.
- p′ = 1: 9K₁K₂⁸·4! = 216K₁K₂⁸.

**A_f, K_f and s₀.**
- (4n−1)!! = (4n)!/(2^{2n}(2n)!) ≤ 2^{2n}(2n)! gives ‖X^{2n}‖₂ ≤ (√2σ)^{2n}(2n)!.
- 𝔫(X_fⁿ)² = K₁(K′)^{2n}(2n)!, so A_f = A + B′K₁ and K_f = max{K′, √2σ_f}.
- Cauchy–Schwarz, then Hölder with k exponents k, gives s₀ = min_{e_j≠0}(2kK_{e_j})^{−1}, finite when
  2k|Re z_j|K_{e_j} < 1.

**Appendix A tables.** Every formula entry agrees with §§2–8. The exceptions, the rows of V2-11, are wording.

### 2.2 Strand 2: integrability chain and consequences

**Lemma D.1** (given the identification, V2-2):
- Lemma N.22, generating function and Fubini.
- Lemma N.23(i)–(iv): g₀, M₀, g₁, b₁, the rearrangement step, and ∫t log(1/t) = ρ²/2 log(1/ρ) + ρ²/4.
- Lemma N.26(a)–(d): Hölder with jN exponents 2jN; Cauchy–Schwarz against w^{⊗2j}; Fatou; the a.e. subsequence.
- Step 0. Step 1: linearity, and fixed representatives u_α = v + αd for all α at once.
- (I1)–(I5): exponents (2,4,4) and (2,2); W = e^{−u₀} + e^{−u₁} ∈ ∩L^q by A3 with ρ = q; the convexity dominator
  e^{−u_β} ≤ W.
- Step 3: the difference quotient, dominated by |d|W.
- Step 4: Z > 0 by A3, continuity, and min > 0.
- Steps 5–6: the quotient rule and the fundamental theorem of calculus.
- Remark N.27(a): (p₀, 2p₀′, 2p₀′) is correct. Remark N.28: the model test gives −½ on both sides.

**Lemma D.2.**
- Step 3: the finite sums, and Cov bilinear on L²(dq_{h_α}) by Lemma N.30.
- Step 4 checks each hypothesis of (1.1.10):
  - the pair (F_a, U_{Δ,n}) consists of localized monomials, with types and degrees n_i < n̄ = 2p′+1;
  - their squares are disjoint, even closed, since w_Δ > 0;
  - the cutoff h_α ∈ 𝒞_E;
  - the weakened form with any separating strip follows because m₁ > 0.
- Step 5: Σ_a‖F_a‖ = ‖F‖ by (1.1.9), Σ_n‖U_{Δ,n}‖ ≤ c_U, and the bound is uniform in α.
- (b) follows from (a). Remark N.31(3): the example g = 1_{[0,1/10]} + 1_{{3}} is right, and it justifies the charged-square
  index set over the plan's.

**Theorem D.3.**
- Lemma N.33: ⟨δ_s⊗f, Gδ_s⊗f′⟩ = ⟨f, Cf′⟩.
- Lemma N.34: the column decomposition.
- Lemma N.36: charged squares lie in columns of K_g at row distance ≥ 2. The strips P_l are parallel, of width
  |l−l_s|−1 ≥ 1.
- Steps 1–4 hold.
- Boundary cases N.39: T ≤ ½ charges row 0 only. s on a lattice line, N_g ∈ {0,1}, and I in one column all hold. For
  |l_s| ≥ 2 and T = ½, h^B = 0 holds only a.e.; harmless.

**Theorem D.4.**
- Steps 1–5: the strips (P) and (T) each have width j for 𝓛_j; corners go to (P); the base term holds by Cauchy–Schwarz,
  Lemma C.2 with Λ = B̄ (|B̄| = 15) and Prop. N.15(iv).
- §6.4: the classification is right. Squares of rows −1, 0, 1 outside the box have no parallel strip of positive width.
  Side squares with 2 ≤ |l| ≤ j have parallel strips only of width ≤ |l|−1 < j. Every (T) use is flagged in Step 4.
- Boundary cases N.43 hold.

**Theorem 5.1, Steps 5–6.** Step 5 is (2) at t = 0 with F₁ = F₂ = |V(h)|, then D.4 at h_{T,g} ∈ 𝒞_E with h′ := h and
supp h ⊆ [a,a+2]. Step 6, the weak-graph passage, needs only the T-uniform (6) and Lemma 4.4.

**§8, block by block, against the record's statements.**

| Statement | Record text | Replacement |
|---|---|---|
| Lemma 4.3(ii) | "For real measurable F, define the clipped truncation F^{[ℓ]} … dominated-convergence majorant whenever the two square moments are finite", ll. 1188–1202 | proof correct: part (i) at t = 0 and Hölder with A3 (inputs: V2-14) |
| Lemma 7.1 | "sup_{T>0}‖Qψ̂_T‖² ≤ C₈𝔫(Q)²; moreover Ω_g ∈ D(Q) and ‖QΩ_g‖² ≤ C₈𝔫(Q)²", ll. 1430–1431 | D.3 with F = Q² at s = 0 and (8) with N_I by columns |
| Lemmas 7.2–7.3 | statements ll. 1455–1458 and 1491–1496 | finiteness at each T suffices; T-uniformity is consumed only through Lemma 7.1 at time 0 (I checked ll. 1478–1482 and 1507–1508) |
| Lemma 7.6 | "E_{μ_g}[X_f^{2n}] ≤ C₈K₁(K′)^{2n}(2n)! … (0 ≤ s < 1/K′)", ll. 1605–1617 | A_f, K_f correct; the cosh series holds by monotone convergence |
| Theorem 7.7 | statement ll. 1639–1641 | statement unchanged; radius correct |
| Theorem 5.1 | "‖V(h)Ω_g‖ ≤ M, M² := 9C₈𝔎(p′)λ²(Σ|a_n|)²", ll. 1257–1265 | M := M_B; eq. (5) without "= M²/C₈" |
| Corollary 5.2 | ll. 1344–1347 | numbers re-derived |
| Prop. 7.5, Theorem 7.8 | — | unchanged |
| Lemma 10.2 | ll. 2091–2111 | h_j = η_jv with supp ⊆ [j−1, j+1], |h_j| ≤ 1, so D.4 covers it; M = M_B, uniform in g ∈ 𝒢 ⊂ 𝒞_H |

**N_I repair.** The counterexample and the rerun proofs of Lemma 6.1 and Prop. 6.2 hold (gaps: V2-5).

**GA5 and GA6.** Commands re-run, outputs as recorded (§3). Every GA5 hit lies in a replaced text, and the replacement
blocks contain no `UGJS`, `C_8` or `1.1.11`.

### 2.3 Disclosures and status

- **The GAP.** Its text after Lemma N.20 is right, and it is cited where D.4 and Theorem 5.1 use it (except V2-14 and
  V2-16).
- **Trap compliance.** Traps 1, 4, 5, 7, 8, 9, 10, 12, 14, 17, 20, 23 and 26 are complied with where the note touches
  them. Trap 25 holds in §7, though not in the Lemma 7.6 statement (V2-17); trap 27 holds in the note (record: V2-22);
  trap 28 holds: the gates are recorded as "Not yet run".
- **AGENTS 3.2 phrases.** They occur only inside quotations of GJS's hypotheses.
- **Control sequences.** All rare ones are standard or defined in `preamble.tex`.

### 2.4 Quotations

**GJS, checked on the page images.**
- p. 589: Φ(τ,f) ≡ Φ(δ_τ⊗f) = ∫Φ(τ,x⃗)f(x⃗)dx⃗; dΦ Gaussian with covariance (−Δ+m₀²)^{−1}; "Let h be a function with
  compact support in R², and let 0 ≦ h ≦ 1."; (1.8).
- p. 593: (1.1.5), (1.1.6); the localization sentence with "side" and the index n; "n_i < n̄"; "Any choice n̄ ≧ deg P is
  sufficient."; "Since there is no restriction on r …"; N(Δ).
- p. 594: (1.1.7)–(1.1.9); the strip sentence, without a period; Theorem 1.1.7 and (1.1.10); "To prove (1.1.11) let
  g = h₂ − h₁".
- p. 595: (1.1.12), first two lines; "We apply Theorem 1.1.7 to each term in the sum to obtain"; "In the monomial Q(x₀)
  of (1.1.5), suppose x₀ = (x_{1,0}, ⋯, x_{r,0})"; "Feyman-Kac".
- p. 596: "monomials of type (1.1.5)"; "We assume that A is localized at times x_{i0} ≦ 0, and that B is localized at
  times x_{i0} ≧ 0."
- p. 597: the rotation sentence and "A = Q₁, B_T = Q₂".

**Record.** Every record quotation and line number I checked is verbatim at the stated lines. I checked all of
those in §8, `consequences.tex`, and those below; a few further locators in §§2–7 were not checked one by one:
- Def. 2.1; A3; A8(i), (ii), (iv); eq. (1); Remark 2.5; §2.6 (l. 995–996);
- Lemma 3.1; Lemmas 4.3, 7.1–7.3 and 7.6; Theorems 5.1 and 7.7; Cor. 5.2;
- Lemmas C.2 and C.4; Theorem C.5 and its proof, ll. 3021–3031; App. A rows; ll. 2110 and 2254.

## 3. Checks run (with output)

1. **Hash.** `shasum -a 256` gives `7e393b9a…85f87` for both `frozen-v1/comparison.pdf` and `comparison.pdf`.
   `diff -r frozen-v1/parts parts`: no output. Same for `comparison.tex` and `preamble.tex`.
2. **Build log** `WORK/comparison.log` (16:38:40). `grep -cE '^!'` gives 0; `grep -c Overfull` 0;
   `grep -icE undefined` 0; "Output written on comparison.pdf (59 pages …)". `pdftotext | grep -nE '\?\?|TODO|Hmm|wait,'`
   gives nothing.
3. **GA5.** `grep -n -e 'eq:UGJS' -e 'C_8' part_i/main.tex | awk -F: '$1>=1133 && $1<1722'` gives 21 lines: 1210 1216
   1262 1313 1321 1324 1346 1430 1431 1436 1439 1440 1449 1463 1464 1502 1609 1614 1617 1621 1631. The `awk`/`grep` over
   the replacement blocks prints nothing (exit 1). Block count: 8.
4. **GA6.** The recorded command gives lines 1731, 1859, 1860, 2110, 2252, 2254, 2394, 2417, 2429, 2430, 2486, 2530.
5. **Labels.** In `main.aux` I checked 36 labels. The 35 listed in `labels-main.txt` agree in number and page, and
   there is no mismatch; `eq:UGJS` is absent from the table.
6. **Numerics** (`numerical`; nothing is deduced; outputs in `WORK/audits/v2/`). Interpreter `/usr/local/bin/python3`,
   which reports `/usr/local/opt/python@3.14/bin/python3.14` 3.14.7, numpy 2.5.2, scipy 1.18.1.
   - `cqft2_ringcheck.py` → `ringcheck.v2run.txt`: "ALL CHECKS PASSED", exit 0.
   - `check_d1.py` → `checkd1.v2run.txt`: "(1) all equal: True"; "(4) … True"; "(5) … True"; exit 0.
7. **Images.** 150 dpi `gjs-p6-06.png`, `gjs-p10-10.png` … `gjs-p14-14.png`; 400 dpi `gjs400-p11-11.png`,
   `gjs400-p12-12.png`. Crops: `crop-p594-strip-end.png`, `crop-p594-norms.png`, `cmp-O1-vs-01.png`, `crop-p595-sum.png`.
8. **Greps.** The AGENTS 3.2 phrase grep finds them only in GJS quotations. The control-sequence scan
   (`grep -oE '\\[A-Za-z]+' | sort | uniq -c`) finds nothing undefined.

## 4. Not checked

- **GJS beyond the pages read.** None of GJS's proofs, and no page other than 589 and 593–597. Not checked either: whether
  the multi-time reading of (1.1.5) lets the printed proof reach D.3's time-integrated partner. The note leaves this
  open, disclosed in Remark N.37.
- **Simon's book.** The content of R8, Simon Thm V.2(b) and Thm I.22.
- **The V3 repairs R1–R10.** Taken as the condition, not re-audited.
- **The record outside the ranges listed in §0.** Including §1, §§8–9 except Prop. 8.1, §§12–14 except Thm 12.2, and
  Appendix B.
- **The C5 reading record.** Only its item headings were read.
- **The human readings.** Whether Definition N.24 is what GJS mean by (1.1.5)–(1.1.6) (C5 item 10).
- **`aqft_checks.py`.** Not re-run; I read its stored output only.
- **The repair of V2-1.** Sketched and checked in outline only: the cross-covariance majorant is not written out.
- **The V1 audit reports.** `WORK/audits/v1-cqft/` and `WORK/audits/v1-mp/` were not read at any point.

## 5. What the drafters flagged that I missed or confirm

Written after §§0–4. Source: `WORK/REPORTS-drafters.md`, which includes `parts/REPORT-mp.md` verbatim, read only at this
point.

### Confirmed at the source, independently

- **N_I counterexample and repair** (aqft E1; cqft2 D1; PLAN F3 inexact). (0.4,0.6) meets one cell and two columns; (7)
  and (8) fail with N_I on GJS's squares (√2K₁K₂² against K₁K₂²; 3K₁K₂⁴ against 2K₁K₂⁴). Not seen by any drafter:
  - the notation table at l. 448;
  - the first clause of A8(ii) (V2-5).
- **Charged squares are needed in D.2** (mp E2; PLAN's index set). Confirmed with the example g = 1_{[0,1/10]} + 1_{{3}}
  (Remark N.31(3)).
- **s₀ = min_{e_j≠0}(2kK_{e_j})^{−1}, not 1/K_f** (mp E3; aqft E4; cqft2 D2). Confirmed. §7 still lacks the restriction
  e_j ≠ 0 (V2-10).
- **The transverse case also enters through the side squares of rows 2 ≤ |l| ≤ j** (cqft2 D3; aqft). Confirmed, and
  flagged at every use inside D.4. Not flagged: D.2(b), the last sentence of N.46, and the `theorem-5.1` replacement
  block (V2-16).
- **"Two localized monomials" covers the mixed pair** (aqft attack 1). It does: p. 594 has "For two localized monomials
  Q₁ and Q₂", and p. 593 "For a localized monomial Q or Q(x₀)" (images).
- **Translation invariance of S₂** (aqft attack 2; cqft2 attack 1). N.13 uses Lemma C.4, which gives L² convergence,
  rather than the L^p sentence of l. 2920 (V3 m-1). The proof is correct, conditional on R1–R10.
- **mp's checks of N.22, N.23 and N.26** (attack 1). Every factor of Π_{Q,j} pairs two distinct integration variables,
  and the ball-rearrangement step, g₁ and b₁ are right (§2.2).
- **Stale statement-change claim** (aqft E2 = mp E1). The orchestrator fixed §1. The stale quotation survives in §8.9, and
  "keep their form" survives in the §8 intro (V2-8).
- **GJS source facts:**
  - p. 594 has no period after the strip sentence (aqft; cqft2);
  - p. 595 prints "Feyman-Kac" (mp E6);
  - (1.1.11) on p. 594 prints the upright "0(1)" (mp E5), which the record's l. 814 silently corrects. All confirmed on
    the images; gates.tex's "unconfirmed" can be replaced by "confirmed (V2)" (V2-22).

### Flagged by a drafter but not carried into the frozen note

- **D.1's conditional status** (V2-2). mp's §2: "If that identification is not accepted as the definition of 𝒰_h, D.1 is
  'proved, conditional on it'." mp's E4 and §4.3 also say that GA2's input list omits the linearity of h ↦ 𝒰_h, Fatou and
  Fubini.
  - I reached V2-2 independently. I add a point mp's report does not make. Per V3 §7 the identification is unproved in
    the record (m-1), and it follows only from Lemma C.4, that is under R1–R10, or from R8 as a definition. So D.1 cannot
    be called unconditionally `proved`, and the gate record's "Lemma D.1 proved (… one named dependence …)" should carry
    the condition.
- **The inputs of the Lemma 4.3(ii) replacement** (V2-14). aqft's report says "uses only A3, Hölder, Gaussian moments",
  which is more accurate than the note's "A3 only". Neither mentions the GAP-dependence for |V(h)|.
- **"Every constant agrees with PLAN Part 1"** (V2-12). The sentence originates in cqft2's report, which in the same
  breath lists D1 and D2 as discrepancies.
- **"The 10 replacement blocks"** (V2-6). The miscount originates in aqft's report.
- **The run records of the numerical checks** (V2-18). They exist in the drafters' folders and reports, as amended above.

### Drafters' points I did not make, and assess here

- **mp: an unconditional alternative for 9^{p′}.** mp (attack 3) says that N.26(b) at j = 2 gives an R8-free fourth-moment
  bound, with a different constant. I agree that it would remove the R8-dependence of the base term of D.4. It does not
  affect V2-1. The note does not use it.
- **mp: the trap-10 rider was once missing from D.4.** It is present in the frozen D.4 statement ("In working coordinates
  (Remark~3.3 of the record), $M_B$ depends on …"), so this is resolved.
- **mp's Lemma L.** Not part of the note; I did not assess it.

### My findings no drafter raised

- **V2-1** (MAJOR by the letter). The merge note (C5), "§6 now uses Lemmas N.20 and N.21", is exactly where the two
  constructions of Q_V meet without an identification.
- **The MINOR findings** V2-3, V2-4, V2-5 (l. 448 and A8(ii)), V2-7, V2-9, V2-11, V2-13, V2-15, V2-17, V2-19, V2-20 and
  V2-21.

---

## V2b (4 November 2026): re-check of the repairs on `WORK/frozen-v2/`

Same auditor, same standard (AGENTS.md §§1–5), same severity words. Started 3 November 2026, interrupted by a usage
limit, finished 4 November 2026.

**Object.** `WORK/frozen-v2/`:
- `comparison.pdf`, 70 pp; sha256 `6dd00a9f0f68d8c0b22310c9eead0265cc5e3aad35361152f337d986131f45a2`, re-checked on
  resuming;
- `comparison.tex`, `preamble.tex` and `parts/*.tex`.

`diff -rq` against `WORK/parts` gives no output, and `cmp` with `WORK/comparison.pdf` shows them identical. Statement
numbers and pages are from `WORK/comparison.aux` (3 Nov 12:42:15); printed page = PDF page.

**Read this round:**
- every changed line of the v1→v2 diffs of all eleven source files, and the new or rewritten passages in full: N.2(iv),
  N.5(iv) tail, N.12(c), N.18(iii), N.19(v), N.21, N.22, N.23, the gap note, N.28(e)–(f), the D.1–D.4 status lines,
  D.2 Step 3, N.36(vi), N.43, D.4, §§8.1, 8.2, 8.5–8.9, A.4–A.6 and `gates.tex`;
- the three disposition files;
- `V1-cqft-report.md`, header, verdict and finding 1 only;
- `parts/check_d1.out` and `build-cqft2/ringcheck-output.txt`.

The record `part_i/main.tex` is unchanged since 2 Nov 15:35:23.

### V2b verdict

The repair of V2-1 is correct. Lemma N.22, Remark N.23(a), (b), (d) and the new part (v) of Lemma N.19 hold as new
claims. Their uses in D.4 (setting, N.43(i), Steps 1, 2 and 4), in §8.6 and in N.36(vi) are correct. N.36(vi) rests on
N.28(f)(1), which I also checked. So D.4's base term and comparison term now concern one element of L²(dμ₀), and the
Euclidean D.4 needs no GAP. No constant changed; Appendix A's rows agree with §§5–6 and §8.

Of my 21 MINOR findings:
- 17 are fixed at the stated locations;
- 4 are fixed only in part: V2-13, V2-16, V2-18 and V2-20, the residues lying in the master and in `constants.tex`
  (and, for V2-18, a run record missing from the frozen bundle);
- none was refused.

The repairs introduce 6 new MINOR defects, V2b-1 to V2b-6. Two concern how conditions are described: V2b-1, in the
status lines of D.2–D.4, and V2b-3, in the gate record. Only V2b-1 changes what can be recorded.

Can D.1–D.4 be recorded exactly as their status lines claim?
- **D.1: yes.** "Proved, conditional on repair R8; on the route written in Step 1, conditional on Lemma C.4 (R1–R10)."
  R8 defines 𝒰_h linearly in h, which is all D.1 needs.
- **D.2: not exactly.** Its alternative "repair R8" is not supported by the text (V2b-1). Step 3 needs the identification
  of 𝒰_{h−h^B} with the limit of its regularizations, and R8's linearity does not give it. Record D.2 as "proved,
  conditional on Lemma C.4 of the record (repairs R1–R10)", or add the few-line R8-route identification described in
  V2b-1.
- **D.3: yes as to the set of conditions** (R8 and R1–R10 of the V3 audit; parallel case only). The parenthetical
  "(repair R8 …)" after "Lemma D.1, through Lemma D.2" must read "(Lemma C.4, R1–R10)".
- **D.4: likewise.** The set of conditions is R8, R1–R10 and F-T, and the same parenthetical must be corrected.

No CRITICAL or MAJOR finding remains open in D.1–D.4.

### V2b-A. The repair of V2-1, audited as a new claim

**Lemma N.22** (`aux:notation-sharpid`; `notation.tex` ll. 1076–1169, PDF pp. 18–19): **holds.** Step by step:

1. **The map J_t.** Lemma N.13(i) with a = (t,0) gives Φ(g)∘T_a = Φ(τ_a g) and (T_a)_*μ₀ = μ₀. τ_a preserves the
   covariance norm, so Φ(0,g)∘T_a = Φ(t,g), and (Φ(t,g))_g has the law of (φ₀(g))_g. Hence J_t is an isometry
   L^p(dφ₀) → L^p(dμ₀), multiplicative, and it takes Wick powers at own variance to Wick powers at own variance.
2. **Covariances.**
   - By N.19(v) and evenness of δ, E[Φ_κ(t,x)Φ_κ(t,y)] = (δ_κ*δ_κ*G)((0,x−y)).
   - For the cross term, approximate δ_t⊗ρ_{κ′}(y−·) by η_ε⊗ρ_{κ′}(y−·); this converges in the covariance norm, as I
     checked by dominated convergence in Fourier space.
   - Continuity and boundedness of δ_κ*G then give Γ_{κ,κ′}(x,y) = ∫(δ_κ*G)((0,x−y′))ρ_{κ′}(y−y′)dy′.
3. **The three inner products.** Each Wick power is ordered at its own variance, so N.20(i) applies (generating function,
   Fubini with moments bounded uniformly). This gives
   - E[X_κ²] = n!∬ff(δ_κ*δ_κ*G)ⁿ,
   - E[X_κY_{κ′}] = n!∬ffΓⁿ,
   - E[Y²] = n!∬ffCⁿ by N.20(iii) and the isometry.
4. **The majorant, uniform in κ ≥ 6.** For a probability density ν with supp ν ⊆ {|v| ≤ ε}, ε ≤ 2/κ, and
   ‖ν‖_∞ ≤ κ²‖δ‖_∞, the bound (ν*G)((0,u)) ≤ 9‖δ‖_∞(b₀+2+2|log|u||) holds. I re-derived both cases:
   - |u| ≥ 2ε: |(0,u)−v| ≥ |u|/2, so C(|u|/2) ≤ (4π)^{−1}(b₀+2log2+2|log|u||).
   - |u| < 2ε: the bound κ²‖δ‖_∞·2π∫₀^{6/κ}rC(r)dr, with ∫₀^{r₀}r(b₀+2|log r|)dr = (r₀²/2)(b₀+1+2|log r₀|), gives
     9‖δ‖_∞(b₀+1+2log(κ/6)). Here log(κ/6) < |log|u|| because |u| < 4/κ ≤ 2/3.
   - The two are combined with ‖δ‖_∞ ≥ 1/π and 2log2 < 2.
   - The majorant applies to ν = δ_κ (ε = 1/κ) and to ν = δ_κ*δ_κ (ε = 2/κ).
5. **Dominated convergence.**
   - (1) At fixed κ, δ_κ*G ≤ κ²‖δ‖_∞m₀^{−2} = ‖δ_κ‖_∞∫G, which uses ∫G = m₀^{−2} from N.19(v). So Γ_{κ,κ′} →
     (δ_κ*G)((0,·)) boundedly as κ′ → ∞, and E[X_κY] = n!∬ff(δ_κ*G)ⁿ.
   - (2) As κ → ∞, both integrands converge off the diagonal to ffCⁿ. They are dominated by
     ‖f‖_∞²1_K1_K(9‖δ‖_∞)ⁿ(b₀+2+2|log|x−y||)ⁿ, which is integrable.
   - Hence ‖X_κ − Y‖² → I − 2I + I = 0.
6. **Kernel hypotheses.** The proof needs f real, bounded, measurable, with compact support. It also needs N.20(iii) for
   such f, whose proof indeed uses only that, with 1_{[a,a+2]} replaced by ‖f‖_∞1_K. n ≤ 2p′ is not used.
7. **Inputs.** None of the V3 repairs (Remark N.23(d) is right). The lemma uses only N.13(i), N.19, N.20 and the
   regularization's definition.

**Lemma N.19(v)** (`notation.tex` ll. 796–801, 873–883, PDF pp. 13–14): **holds.**
- The 2D heat kernel P_t has P̂_t = e^{−t|p|²}.
- ∫₀^∞e^{−tm²}(4πt)^{−1}e^{−r²/4t}dt is exactly (4π)^{−1}∫t^{−1}e^{−tm²−r²/4t}dt = C(r). So G(ζ) = C(|ζ|), the same
  function as the time-zero kernel.
- The Tonelli/Fubini step and polarization go as in (ii). ∫G = m₀^{−2}.

**Remark N.23** (`aux:notation-sharpidrem`; ll. 1171–1192, PDF pp. 19–20): (a), (b) and (d) **hold**; (c) has the
inaccurate clause of V2b-4.
- (a) Definition N.26(b) at r = 1 is X_κ, so N.28(a) and N.22 apply. For products, N.28(c) and the multiplicativity of
  J_t.
- (b) W_n(h′) = Σ_kW_n(h′_k) by linearity of the regularized integrals, so ΣQ_{n,n′,k,k′} = (J₀V(h′))² = Y².

**Uses.**
- **D.4 setting** (`d4.tex` ll. 22–39): V(h′)(0) := Y = J₀V(h′), with Q_V := Y². Holds.
- **N.43(i)** (ll. 101–112): each h′_k is bounded by 1, vanishes outside [a,a+2] ⊆ [k_a−½, k_a+5/2) and outside its
  column, so the hypotheses of N.22 and N.23(a) hold. Holds.
- **Step 1** (ll. 163–170): the a.e. identity, with "a.e.-equal functions have equal dq_h-integrals". Holds.
- **Step 2** (ll. 177–183) and **Step 4** (ll. 209–214) cite N.22 and N.23(b). Holds.
- **§8.6** (`consequences.tex` ll. 361–364 inside block `theorem-5.1`, and the Check, ll. 369–384): it correctly
  separates the constructed Y, which N.22 identifies with the comparison pieces, from the record's V(h), which the GAP
  identifies with it. Holds.
- **N.36(vi)** (`d3.tex` ll. 131–135, 155–168, PDF p. 35): D.3's column pieces have kernels f_i1_{[κ_i−½,κ_i+½)},
  which are L² with bounded support but not smooth. N.36(vi) therefore uses N.28(f)(1), not N.23(c).
  - N.28(f)(1) holds (`d1.tex` ll. 405–412). The regularized monomial is Φ(δ_κ*(δ_t⊗f)), with
    δ_κ*(δ_t⊗f) ∈ C_c^∞, and its covariance-norm distance to δ_t⊗f tends to 0 by dominated convergence with the
    dominator 4|f̂(p₁)|²(|p|²+m₀²)^{−1}.
  - The summation Σ_κΠ_iΦ(s,f_i1_{κ_i}) = Π_iΦ(s,f_i) uses linearity and a.e.-invariance of f ↦ Φ(s,f). Holds.

### V2b-B. Dispositions of the 21 MINOR findings, checked at the stated locations

| finding | claimed | verified on frozen-v2 |
|---|---|---|
| V2-2 | fixed (mp) | **fixed.** Status paragraph after D.1 (`d1.tex` ll. 452–470); Step 1 (ll. 500–502); Remark N.29(b) (ll. 593–597); inputs (ll. 14–18); §7 (`quantifiers.tex` ll. 76–79). New defect in the orchestrator's summary: V2b-3. |
| V2-3 | fixed | **fixed.** `d1.tex` l. 562 now says "repair R8". |
| V2-4 | reframed (orchestrator) | **fixed by the framing.** Master ll. 20–24 and `gates.tex` ll. 3–6: in-section status words are drafters' claims, and the note is conjectured as a whole. `notation.tex` l. 17 and `constants.tex` l. 18 keep "conjectured", which is consistent with that framing. |
| V2-5 | fixed (aqft) | **fixed.** Block `sec6-NI` (`consequences.tex` ll. 57–77) replaces l. 448, A8(ii) ll. 659–663, l. 1359, Lemma 6.1, the proofs of 6.1–6.2 and Theorem 5.1 Steps 2–4 on columns. "Is then true" is withdrawn (ll. 78–84). The replacement wording is correct. |
| V2-6 | fixed | **fixed.** Eight blocks named (ll. 460–462; BEGIN lines 57, 105, 152, 193, 210, 256, 339, 389). The outside list (ll. 467–476) is complete: my grep gives 68, 72, 76, 81, 184, 210, 290, 302, 710, 722, 726, 769, 803, 868, 2417, 2737, 2776, 3075 outside §§4–7. `gates.tex` l. 89 says "eight". |
| V2-7 | fixed | **fixed.** `consequences.tex` ll. 496–501. The line numbers match the record: (25) l. 2099, (26) l. 2126, (27) l. 2155, (29) l. 2214. |
| V2-8 | fixed | **fixed.** §8 intro, ll. 17–27 (Lemma 7.1 "changes its form"); §8.9; master ll. 61–62 ("the radius s₀ in the proof of Theorem 7.7"). |
| V2-9 | fixed | **fixed.** No N^col_I remains (grep), at `quantifiers.tex` l. 128 or at (C2). |
| V2-10 | fixed | **fixed.** `quantifiers.tex` ll. 160–170. The restriction e_j ≠ 0 is there, and the all-zero case reads s₀ := +∞. §8.5 says "any s₀ > 0"; the two agree in effect. |
| V2-11 | fixed | **fixed.** A.4's closing paragraph (`constants.tex` ll. 392–400) and §8.7 (`consequences.tex` ll. 440–448) list the same rows. (C6) is corrected. |
| V2-12 | wording supplied | **fixed.** `gates.tex` ll. 92–94; new A.5 (D9). |
| V2-13 | parts fixed; master the orchestrator's | **partly fixed.** Master ll. 68–81 now list A2, Definition 2.1, Lemma 3.1, Lemma 6.1, Lemma C.4 with its conditions, and A4's direct use. Still missing: Remark 2.5 (used in N.21(i), N.35) and A5(i) (Lemma 4.3(ii) replacement); still listed though no proof of the note uses it as a premise: Lemma 7.4. `notation.tex`'s new "Inputs of this section" (ll. 39–47) is complete for §2. |
| V2-14 | fixed | **fixed.** §8 intro ll. 31–46; block `lemma-4.3-ii` restricted to cylinder monomials, with A5(i) kept for \|V(h)\|. The claim that the record applies part (ii) only at ll. 1462 and 1501, and part (i) at l. 1320, is verified by grep (also l. 1435, part (i)). |
| V2-15 | fixed | **fixed.** N.18(iii) statement and proof (`notation.tex` ll. 717–722, 759–763). |
| V2-16 | (1), (3) fixed; (2) partly | (1) **fixed:** F-T verbatim, master ll. 50–56. (2) **fixed for D.2(a), D.2(b) and Remark N.33(2)** (`d2.tex`); **not fixed for N.48's last sentence** (`constants.tex` ll. 35–38, PDF p. 60), which still uses uncontrolled orientations without F-T. (3) **fixed:** the parenthetical inside block `theorem-5.1` (ll. 361–364); also block `corollary-5.2`, ll. 397–398. |
| V2-17 | fixed | **fixed.** The sentence is out of the statement; the "Remark on the radius" (ll. 286–290) is accurate. |
| V2-18 | fixed | **fixed in substance, residue in the bundle.** `parts/check_d1.out` (12:06; script sha256 prefix 0f1e2374d79c0563, matching the script) is in frozen-v2. N.12(c) records the 3 Nov 12:08 run, and `build-cqft2/ringcheck-output.txt` (mtime 12:08:21) reads "ALL CHECKS PASSED". That file is not in `frozen-v2/`. |
| V2-19 | fixed | **fixed.** No `audits/V3-appendixC-report.md` reference remains. |
| V2-20 | partly | **partly fixed.** `notation.tex` l. 899 now cites p. 16. Not fixed in the master: "Status (31 October 2026)" (l. 18) and "The two open human readings" (ll. 65–66). |
| V2-21 | fixed | **fixed.** Chaos paragraph (ll. 892–896) and N.21(i) (ll. 1041–1046): the objects lie in Simon's Γ_n directly. |
| V2-22 | gates updated | **fixed for the note.** `gates.tex` ll. 41–46. The record's l. 814 is unchanged (integration-time edit). The KB node named there was not checked (no kb access). |

### V2b-C. New findings (all MINOR)

**V2b-1. The alternative "repair R8" in the status lines of D.2–D.4 is not backed by the text.**

*Locators:*
- `d2.tex` ll. 143–147 (status of D.2, PDF p. 31);
- `d3.tex` ll. 259–261 (p. 38);
- `d4.tex` ll. 153–155 (p. 42);
- `quantifiers.tex` ll. 99–102 (p. 47);
- `gates.tex` ll. 9–14 (p. 68).

*Text:*
- D.2: "Proved, conditional on Lemma~\ref{lem:D1} with its condition: repair R8 of the V3 audit, or, on the route written
  in Step~1 of its proof, Lemma~C.4 … Lemma~\ref{lem:D2} inherits that condition through the identification of
  $\Uc_{h-h^B}$ with a limit of regularizations (Step~3)."
- §7: "the linearity of Step~1 of Lemma~\ref{lem:D1}, under repair R8, gives the same decomposition."
- D.3 and D.4: "Lemma~\ref{lem:D1}, through Lemma~\ref{lem:D2} (repair R8 of the V3 audit …)".

*Why it fails.* Step 3 of D.2 (ll. 169–201) decomposes 𝒰_{h−h^B} into the limits U_{Δ,n} of N.28(a). Lemma D.2
applies GJS Theorem 1.1.7 and Lemma N.32 to these limits. The decomposition needs 𝒰_h − 𝒰_{h^B} = L²-lim 𝒰^{(κ)}_w,
i.e. the identification of the record's 𝒰_h with the regularized limit. D.1's own status paragraph (`d1.tex` ll. 452–470)
assigns that identification to Lemma C.4 (R1–R10), or to the reading that defines 𝒰_h as the limit. R8 supplies only
linearity:
- linearity gives 𝒰_{h−h^B} = Σ_Δλ Σ_n a_n:Φⁿ(h1_Δ): with Simon's objects;
- these are not shown to be the U_{Δ,n} of N.28(a).

The step is true. Under R8 it follows from a short computation, ‖λa_n:Φⁿ(h1_Δ): − U^{(κ)}_{Δ,n}‖₂² → 0, using:
- the cross term from (V.3);
- Simon's isometry;
- dominated convergence with the majorant of N.22 for ν = δ_κ and ν = δ_κ*δ_κ.

None of this is written. D.3's and D.4's condition sets contain R1–R10 anyway, so their total conditions are unaffected.
Only the attribution is wrong, and D.2's own line overclaims.

*Repair.* Write "(Lemma C.4 of the record, repairs R1–R10, through the identification of 𝒰_{h−h^B} with the limit of its
regularizations; or the reading that defines 𝒰_h as that limit)" in the three status lines and in `gates.tex`. Delete
§7's "under repair R8, gives the same decomposition", or add the computation above as a lemma.

*Severity:* MINOR. It blocks recording D.2's status line verbatim.

**V2b-2. §7 describes D.2's route as it was before the repair.**

*Locator:* `quantifiers.tex` ll. 99–101 (p. 47).

*Text:* "for the decomposition of $\Uc_{h-h^B}$ into the $U_{\Delta,n}$, Lemma~C.4 of the record through
Lemmas~\ref{aux:notation-cU}(iv) and~\ref{aux:notation-cutoffs}(iv)".

*Why it fails.* D.2's Step 3 no longer uses N.18(iv) or N.5(iv). It goes through D.1's Step 1 and N.28(a)
(`d2.tex` ll. 169–201; aqft's disposition, mp-F3). Appendix A.1, Lemma N.48, still uses N.18(iv), which is a valid second
route.

*Repair.* Describe the route of `d2.tex`.

*Severity:* MINOR.

**V2b-3. The gate record misdescribes D.1's condition.**

*Locator:* `gates.tex` ll. 6–8 (p. 68).

*Text:* "Lemma~\ref{lem:D1} proved, conditional on repair R8 of the V3 audit (the identification of the record's $\Uc_h$
with the $L^2$-limit of its regularizations $\Uc_{h,\kappa}$; on the Step-1 route, conditional on Lemma~C.4, R1--R10)".

*Why it fails.* D.1's status paragraph says R8 gives the *linearity* of h ↦ 𝒰_h. The identification with the L²-limit is
the Step-1 route, which is conditional on Lemma C.4. The parenthetical attributes it to R8.

*Repair.* "(R8 defines 𝒰_h linearly in h; on the Step-1 route the identification of 𝒰_h with the L²-limit of 𝒰_{h,κ}
is Lemma C.4, R1–R10)".

*Severity:* MINOR.

**V2b-4. Remark N.23(c) overstates its scope.**

*Locator:* `notation.tex` ll. 1186–1188 (p. 20).

*Text:* "(c) At degree $1$ and $f\in C_c^\infty(\R)$, … and covers the cylinder pieces of Theorem~\ref{thm:D3}."

*Why it fails.* The pieces of D.3 have the non-smooth kernels f_i1_{[κ_i−½,κ_i+½)}, so (c), stated for C_c^∞, does not
cover them. N.36(vi) says so and uses N.28(f)(1). N.22 at n = 1 covers bounded kernels and would also do.

*Repair.* "and, by Lemma N.22 with n = 1, the column pieces of Theorem D.3".

*Severity:* MINOR.

**V2b-5. N.2(iv) claims the reading is named beside the status words; it is not.**

*Locator:* `notation.tex` ll. 126–127 (p. 4).

*Text:* "It is named beside the status words with C5 item~10."

*Why it fails.* No status line of D.1–D.4 names C5 item 10. D.2's line names "a reading of the source" without the item.
The master says the C5 items are named "at integration" (l. 66).

*Repair.* "It will be named … at integration", or add "C5 item 10" to the status lines of D.2–D.4.

*Severity:* MINOR.

**V2b-6. Appendix A.4's legend and rows disagree.**

*Locator:* `constants.tex` ll. 311–320 (legend) and the rows C₇c_U (l. 335) and B′ (l. 344), PDF pp. 64–65.

*Text:* "``Cond.'' marks a constant whose finiteness or bound uses Lemma~C.2, Lemma~C.4, Theorem~C.5 or the comparison
step".

*Why it fails.* The comparison bounds with C₇c_U and B′ rest on D.2: through N.48 → N.18(iv) → N.5(iv) → Lemma C.4,
or through D.1's condition. So by the legend these rows are "cond." (R1–R10), but they are not marked. A, A_f and M_B
are marked.

*Repair.* Mark both rows "cond.".

*Severity:* MINOR.

### V2b-D. Constants (task 3)

The status lines say no constant changed, and none did. I compared every definition in the v2 sources by grep and
reading against my V2 hand recomputations (§2.1): A, B′, c_U, S₂, 𝔔, Σ̄₃ₓ₅, V̄_*, I_n, b₀, 9^{p′}, M_B, A_f, K_f, K′,
s₀, and the φ⁴ values 362 880, 1944 and 8 709 120. The formulas are unchanged in `d3.tex` l. 248–249, `d4.tex` ll. 50 and
139, `consequences.tex` ll. 261, 303, 343 and 394, `quantifiers.tex` ll. 107–108, 151–152, 160 and 179, and in the
tables of A.4.

Two degenerate conventions are new, and both are consistent:
- Lemma 7.1's case L = 0, A := B′ := 0. Then Q = 0, and Appendix A's A-row concerns D.3, which needs L > 0.
- s₀ := +∞ when all e_j = 0 (§7), against "any s₀ > 0" (§8.5, N.54).

The new A.5 (D9) is right: Σ̄₃ₓ₅ ≥ Σ₃ₓ₅, so M_B bounds the plan's value from above. The table's dependence and
uniformity columns agree with §§5–6 and §8, apart from the "cond." marks of V2b-6.

### V2b-E. Checks run

1. **Hash and identity.** `shasum -a 256 frozen-v2/comparison.pdf` gives `6dd00a9f0f68d8c0…131f45a2`, twice (3 and
   4 Nov). `diff -rq frozen-v2/parts parts`: no output. `cmp frozen-v2/comparison.pdf comparison.pdf`: identical.
2. **Build log** `WORK/comparison.log` (12:42). "Output written on comparison.pdf (70 pages …)"; no `^!` line;
   `grep -c Overfull` gives 0; `grep -icE undefined` gives 0. The marker grep on `pdftotext` gives nothing.
3. **Greps.**
   - `grep -n '^% BEGIN-REPLACEMENT'`: 8 blocks.
   - The outside-§§4–7 grep of `eq:UGJS`/`U_{\rm GJS}`/`UGJS` on main.tex: the list above.
   - `rm col`: none.
   - `V3-appendixC`: none.
   - `lem:slabunbdd` in main.tex: ll. 1320, 1435, 1462, 1501.
4. **Run records.** `shasum` of `check_d1.py` begins `0f1e2374d79c0563`, as recorded in `check_d1.out`.
   `build-cqft2/ringcheck-output.txt` has mtime 3 Nov 12:08:21 and a header "run: 2026-11-03 12:08 CET".
5. **Hand derivations.** All steps of N.22 and N.19(v), and N.28(f)(1) (§V2b-A).

### V2b-F. Not checked in V2b

- The dispositions of the V1 findings (cqft-1…15, mp-F1…F14) beyond where they coincide with V2 items. I read only the
  V1 attacker's verdict and finding 1, and not `V1-mp-report.md`.
- N.28(e) (independence of the mollifier). I checked its reduction to the proof of N.25(iii) in outline only.
- The KB node `a8-vii-prime-silent-correction-of-gjs-0-1` named in `gates.tex` (no kb access).
- Unchanged v2 text. It was audited in V2 on frozen-v1, and I relied on the diffs for what changed.
