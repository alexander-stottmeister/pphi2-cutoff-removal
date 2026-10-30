# Memo of `cqft` (reader of the printed Glimm-Jaffe-Spencer expansion), R1, written 28-30 October 2026

Read on the page images this session: GJS Annals pp. 588-632 (`gjs74/p-05` to `p-49`), every page;
Erice II pp. 203-227 and 232-242 (section 8, pp. 228-231, not read); Erice I pp. 160-163 and 193. Record: `part_i/main.tex` at the line
ranges of the brief, `m4/r1-check.tex`, `C5_reading_record.md`, `part_i/README.md`, the companion's
section 4, the KB nodes named in the brief. Numbers of the record are from `companion/council/labels.md`.
"Annals p. N" is the printed page; display numbers are the source's own.

## A. Verdict on O1-O5

**O1 (section 7 at fixed g): confirmed in structure, from the expansion side; the details are `mp`'s.**
Nothing in section 7 needs the cluster expansion beyond CE2 (Source Fact 2.2), whose statement prints
"constants 0 < m_1 and O(1) independent of h, Q_1 and Q_2" (Annals p. 594), and by the brief's reading
section 7 exports only m_1 (Theorem 7.8; `mp` checks this). One caveat the plan must carry: the printed proof of
Theorem 1.1.7 takes its h-independent constant from Theorem 1.1.8 *at the same h* (p. 597: "the proof
follows from Theorem 1.1.8, (1.1.16) and the above determination of Q"). After O1, Theorem 7.8 no longer
cites U_GJS, but it still rests on a printed theorem whose printed proof uses the uniformity. That is the
standard of A1-A7 (printed statements, proofs not re-verified), not a proof of independence (trap G3).

**O2 (irreducible core U^{M2}): confirmed as the minimal *consumed* statement; modified as the minimal
*proof target*.** Theorem 5.1 consumes CE1 only in Step 5, for Q_V = V(h)^2 at time 0 (ll. 1218-1226).
But the expansion's cost does not shrink with the observable. The observable enters only through the
initial term and its norm; the expansion itself creates vertices of unbounded local degree N(Delta),
inserts contours of side 2[N(Delta)^{1/4}]+1 (2.3.2), p. 609, and carries the factorials N(Delta)! of
(2.4.5) whatever A is. What does shrink the work is B = I, T = 0 (next paragraph), and that branch
proves the bound for *every* (1.1.5) observable at once. Recommendation: prove the B = I bound for all
(1.1.5) monomials, uniformly over C_E. It costs the same as U^{M2}, restores Lemmas 4.3, 7.1-7.3 and
7.6 in their present form, and makes Phase 1 optional rather than necessary.

**O3 (no comparison trick): confirmed, as an estimate (no loophole found).** Along h_1 + alpha g
((1.1.12), p. 595), the cells of supp g within distance O(1) of supp V(h) have no separating strip. Their
covariance terms need sup over the path of the expectation of V(h)^2 V(g_i), a moment of degree up to
6p' at intermediate cutoffs. Cauchy-Schwarz turns that into a degree-8p' moment, and so on, so the
regress does not close. A second circularity: CE2 at the intermediate cutoffs is, in its printed proof,
CE1 at those cutoffs (p. 597). A closure would need a uniform moment bound for a class of observables
closed under multiplication by V(g_i), which is U_GJS itself.

**O4 (re-sourcing is a status change, not a removal): confirmed, with three refinements read on the
images.** (i) Erice I (2.2.7), p. 161, is printed inside square brackets that open after (2.2.4): "Also
(2.2.7) ∫Adq_h ≤ ||A|| uniformly in h.]", without absolute-value bars. Its norm (2.2.5) is
eta prod ||f_i|| with eta = prod_Delta (K_1 N(Delta)!): K_1 per square, no K_2. That is not the Annals
norm (1.1.7). (ii) Its observables (2.2.3) are products of single-point Wick powers with
f_i = delta_s(t) f_i(x) allowed. So it covers the U^{M2} observable type literally, and the sharp time
too. (iii) The class of h is unspecified on pp. 160-161. Page 162 works with "0 ≤ h_0 ≤ h_1 ≤ 1" (the
image prints ≤; the text layer's "<" is an artefact) and an ordered pair. The bracketed bound is
attributed to [GlJaSp 1, 2], which p. 193 identifies as the Annals paper ("to appear") and Erice II. So
Erice I adds a second printed assertion, not a second proof. Both proofs route the h-dependence through
a stability estimate cited to Dimock-Glimm (Annals (2.4.34), p. 624; Erice II Theorem 9.5, p. 237;
section C). Re-sourcing therefore changes the documentation, not the status. It belongs to Phase 0, and
it must not be described as making A8(vi) literal.

**O5 (two proof routes): modified.** Level 2 as defined ("trace ... display by display", "a verified
citation") cannot be completed on the Annals text, for three reasons read on the pages.
(a) The branch Theorem 1.1.8 needs is the one GJS do not display. "Proof of Theorem 1.1.8 ... Choose T = 0
and B = I in Theorem 1.1.11" (p. 600). With T = 0 every term is a remainder (r-) term (y_0 ≥ T, p. 608),
and r-terms take their contractions from (2.0.5) "so that no annihilators occur" (p. 610). The displayed
estimates of Lemma 2.4.5 are its annihilator cases i = 1, 2. The r-term cases are "The remaining cases
i = 3, 4 are bounded similarly" (p. 621). Theorem 3.1 displays its annihilator term, and for the rest
"The remaining terms ... are bounded similarly" (p. 627).
(b) A quantitative h-entry exists that Appendix C does not list. Lemma 2.4.6's bound (2.4.28) is proved
on p. 624 from "(2.4.34) 1 ≤ ||e^{-V(Y)}||_{L_2(dPhi_C)} ≤ e^{K_3|Y|}". There K_3 is "independent of C,
m_0 and λ" (h is not mentioned), and the estimate is called standard "(see [1])", where [1] is
Dimock-Glimm, Adv. Math. 12 (1974), not on disk. K_3 then fixes K_2 ("for K_2 ≥ K_3^2";
"K_2 = K_2(ε, m_0, K_3)") and hence every constant of Theorems 2.4.1, 3.1, 4.1, 1.1.7 and 1.1.8 (finding F1).
(c) The pages carry misprints and one omission that a trace must record rather than silently correct
(section C, table).
So the honest end state of the expansion route is a **theorem of the record**: a re-derivation of the
B = I branch with the Annals as template, plus one new h-uniform stability lemma. The Erice II variant
is no cheaper (section C).

## B. The statements to prove

Notation: C_1, C_2 are the Annals covariance classes (pp. 603-605), built from C_0 = (-Delta + m_0^2)^{-1}
by *decoupling* C_Y = YCY + (1-Y)C(1-Y) (p. 600) and convex sums. From these definitions (my
deduction; p. 604 prints |C_*| ≤ C_0, p. 603 "C_i(x,y) = C_{i-1}(x,y), unless x and y are separated"):
0 ≤ C(x,y) ≤ C_0(x,y), with equality when no contour separates x and y. V(Y) := V(h 1_Y).

**Lemma S (h-uniform stability; the one new ingredient).** There are K_3 = K_3(P) and c_0 = c_0(P) such
that the following holds for all m_0 ≥ 1, 0 ≤ λ ≤ 1, every finite union Y of unit lattice squares,
every C in C_1 ∪ C_2 and every h in C_E:
||e^{-V(Y)}||_{L^2(dPhi_C)} ≤ e^{K_3|Y|} and ∫ e^{-V(Y)} dPhi_C ≥ e^{-c_0 λ|Y|}.
The lower bound is to come from Jensen's inequality (Wick mismatch only on contours, a null set). It
replaces the printed "1 ≤ ||e^{-V(Y)}||", which Jensen gives only for a_0 ≤ 0; for a_0 > 0 it fails at
small λ > 0 (my first-order computation).

**Lemma G.** (2.4.35) holds with K_3 independent of C in C_1 ∪ C_2, for vertices at sharp times and
in squares.

**Theorem E (the target of Phase 2).** Let P be bounded below (Annals p. 588) and fix n̄ = 2p'+1.
There are thresholds m_0 ≥ m_*(P), then K_2 ≥ K_2^*(m_0, K_3), then K_1 ≥ K_1^*(m_0, K_2), then
λ ≤ λ_*(m_0, K_2, K_1), all chosen in that order (the printed order, p. 616). With them there is
C_8 = C_8(m_0, K_2, K_1, P) such that

|∫ Q(x^0) dq_h| ≤ C_8 ||Q(x^0)||_GJS

for every Q of the form (1.1.5) with n_i < n̄, every x^0 and every h in C_E. Dilation (A8(viii)) turns
the thresholds into λ/m_0^2 < ε'_P, a threshold of the record's own that replaces ε_P. Proposition 3.2
must be redone with it.

**Corollary U.** U_GJS holds, since C_E^slab ⊂ C_E. By Theorem 5.1, Steps 1-4, so does U^{M2}: for every
T > 0, g in C_H and real h' with ||h'||_∞ ≤ 1 and supp h' in an interval of length 2,
∫ V(h')^2 dq_{h_{T,g}} ≤ M^2. Here M^2 = 9 C_8 K_1 K_2^{8p'} (4p')! λ^2 (Σ|a_n|)^2 is unchanged in form;
C_8 is now derived, not imported.

**What changes status.** Phase 0 changes nothing. After Phase 1 (`mp`), Theorem 7.8 and Lemmas 7.1-7.3
and 7.6 no longer cite U_GJS. Theorem 7.8 becomes "proved, conditional on A8(iv)". After Phase 2,
Theorem E and Corollary U are "proved" if Lemmas S and G are proved in the record. They are
"proved, conditional on <Dimock-Glimm import>" if those two lemmas are cited. Theorem 5.1,
Lemma 4.3 and Proposition C.7 lose their U_GJS hypothesis, and so do Lemma 10.2 and everything after
it. Theorem 12.2 becomes "proved, conditional on A1-A7 and the literal items of A8". A8(vi) becomes a
theorem of the record, and A8(vii)/(vii') become historical evidence.

## C. Routes (the expansion routes; with the map)

**C.0 The map: the printed proof of Annals Theorem 1.1.8, read on the images.**
"Branch" = needed for B = I, T = 0. "Face" means the printed constant is visibly h-free; "M3", "M4", "M5"
mean h-free by that mechanism of Appendix C. Nearly all the trace's own work falls in the branch rows.

| printed unit (page) | where h enters | constant | branch; what a trace must add |
|---|---|---|---|
| Thm 1.1.8 (595); proof (600); "special case B = I, n = 0" (629) | measure dq_h | "uniformly as h → 1"; uniform in h (629) | yes. p. 600 names "Theorem 1.1.10" where the argument uses 1.1.11 (misprint). T = 0 against "no initial ... remainder terms" (614). Reduce Q(x^0) to times ≤ 0 (p. 596) by translation within C_E |
| (1.8) (589) | the action | none | Wick order w.r.t. the free dPhi |
| (2.0.1), C_Y (600) | nowhere | face | yes; decoupling, not Dirichlet (F2) |
| (2.0.2) (601) | V(h) = V(Yh) + V((1-Y)h) | M4, exact | yes; factorization for decoupled C |
| (2.0.3)-(2.0.8) (601-602) | e^{-V(h)} rides in F | M4 | yes; (2.0.5) printed with a spurious ∫_0^1 ds; integrability under every dPhi_{C(s)}: Lemma S |
| (2.1.1)-(2.1.10), Props 2.1.1, 2.1.2 (603-605) | nowhere | face | yes; write the sketched proofs (that of 2.1.1 invokes (2.1.6) inside itself); unit intervals at sharp time |
| (2.2.1)-(2.2.7), Lemma 2.2.1, Props 2.1.1'/2.1.2' (605-607) | vertex: "after differentiating e^{-V(h)}, contributes a factor O(λ)" (607) | M3 | (2.2.1) yes; (2.2.5) no; (2.2.7) only with n_a = 0 ("1 = 1", 607) |
| (2.3.1)-(2.3.2), T1, T2, steps I, II (608-610) | nowhere | face | yes |
| (2.3.3)-(2.3.8) (611-612) | e^{-V(Y_j)} inside the "numerical kernels" w', w; the ratios (2.3.5)-(2.3.6) | **not h-free; M1/M5 miss it** | yes; p. 611 cites "(2.0.1)" for (2.0.2) (misprint) |
| (2.4.1)-(2.4.5), Table 1, Thm 2.4.1 (612-616) | through w | M1 true of the functional, not of w | yes; constants in the order m_0, K_2, K_1, λ (616) |
| Lemma 2.4.2, (2.4.6)-(2.4.12) (616-617) | vertex O(λ) | M3 | no (l-terms) |
| Lemma 2.4.3, (2.4.13)-(2.4.16) (617-619) | none | face | only the trivial n_a = 0 step at T = 0 |
| Prop 2.4.4, (2.4.17)-(2.4.18) (619) | none | face | yes |
| Lemma 2.4.5, (2.4.19)-(2.4.26) (620-621) | vertex v ≤ O(λ) | M3 | yes, but the branch is cases i = 3, 4: "bounded similarly". **Write them** |
| Lemma 2.4.6, (2.4.27)-(2.4.33) (622-624) | none | face | yes; the proof is displayed for l-terms only; write the r-version |
| (2.4.34)-(2.4.35), the bound on w'' (624) | **stability of e^{-V(Y)} under dPhi_C; K_3, then K_2 ≥ K_3^2** | **not on its face** (K_3 "independent of C, m_0 and λ"); outside M1-M5 and Theorem C.5 | yes; Lemmas S, G; restore the denominator of (2.3.8), which the display omits |
| convergence (624-625) | e^{O(Vol)}, Vol "the area of the set of points within unit distance of suppt h" | qualitative, per h | yes; prove that the non-final terms vanish for each compactly supported h. "a fraction β > 0 ... is the step I" is asserted |
| Ch. 3, (3.1)-(3.6), Thm 3.1 (625-627) | vertex, "v(x) is O(λ) times the characteristic function of a lattice square" (626) | M3 | yes; the r-case ("remaining terms ... bounded similarly", 627); convergence "follows similarly" |
| Ch. 4, (4.1)-(4.4), Thm 4.1 (627-629) | division by ∫e^{-V}dPhi_{C_0} | M5, exact here | (4.3)-(4.4) yes; (4.1)-(4.2) and Thm 4.1, whose details are not given ("we do not give the details"), are not needed |
| (4.5)-(4.7), Thm 4.2, Lemma 4.3 (629-631) | h = 1 | none | no |

**Counts.** Sections 2-4 carry 81 numbered displays (8 + 10 + 7 + 8 + 35 + 6 + 7, counted on the images)
and about 100 unnumbered ones (my page-by-page count, ±10%). The branch uses about 58 numbered displays
(estimate). h touches the printed proof at four loci: vertices (pp. 607, 616, 620, 626, 631), the
factored kernels via (2.4.34) (pp. 611-612, 624), the factor e^{O(Vol)} (pp. 624-625), and the final
division (p. 628), which is exact. Only the second is quantitative and not readable off the page.

**Erice II, sections 3-10, briefly.** Section 3, Props 3.1-3.3, Thm 3.5: h enters only through
V(h 1_Λ) in the factorization (Prop 3.3, exact); Prop 3.1's proof is omitted ("We omit the proof").
Sections 4, 5: Prop 5.1 is combinatorics; Props 5.2 and 5.3 carry e^{K_2|X|} and e^{K_3|Λ|}, i.e.
stability. Section 6, Thm 6.1: "By the dominated convergence theorem, Z_{∂Δ}(Δ) → 1" (p. 222), per h;
an h-uniform version needs Lemma S. Section 7 is covariance bounds, h-free; Prop 7.5's c(x) is the
Dirichlet Wick mismatch (Wick order relative to C_∅, p. 205). Section 8 I did not read. Section 9: Thms 9.1-9.4 are h-free.
Thm 9.5, (9.8) |Z| ≤ e^{K_12|Λ|}, is the stability input: "The simple proof of [1, §II.3, p. 22-27]
is self contained" (p. 237); the sentence after (9.8) says "K_10", a misprint for K_12. Thm 9.7: "For
details see [1]" ([1] is Dimock-Glimm, p. 242). Section 10 carries h through Cor 9.6. Observables (2.7)
have kernels in S(R^{2j}): no sharp time, and Thm 9.1's hypothesis w ∈ L_q, q > 1, fails for
delta_s(t) kernels.

**C.1 Route E1 (recommended): re-derive the Annals B = I branch.** Base: Annals pp. 588-631 (read).
Steps: (1) complete the table above, one row per display of the branch, with misprints recorded verbatim;
(2) prove Lemma S, Lemma G and the Jensen lower bound for C_1 ∪ C_2 and h in C_E; (3) write the r-cases
of Lemmas 2.4.5 and 2.4.6 and of Theorem 3.1; (4) the T = 0 start and the convergence lemma; (5) assemble
Theorem E with constants in the printed order, then the dilation; (6) Corollary U.
Deliverable: `ugjs/expansion.tex`, attached as a supplement that replaces A8(vi) by a theorem; the edits
to `main.tex` are the editor's.
Estimate: 31-46 pages of finished proof (table 6-8, Lemma S 8-12, Lemma G 3-5, written cases 10-15,
convergence and assembly 4-6), and 4 verification rounds plus one human page-image reading of the
table.
Imports: the Annals (on disk, read); Simon Thm I.17 = A4 (literal, already imported) for the chaos
bounds. Dimock-Glimm is needed only if Lemmas S and G are cited rather than proved (to acquire).
Risk: Lemma S's linear growth e^{K_3|Y|}, uniformly over the *decoupled* class. Convex combinations of
decoupled covariances have no Markov property, so the per-square Nelson argument (Theorem C.5's method,
which gives neither dPhi_C nor linear growth) must be run with local factorial Gaussian bounds of
Erice II Thm 9.4 type. If it fails, switch to Dirichlet interpolation, which is Route E3.

**C.2 Route E2: Erice II with footnote 5's h.** Not cheaper. Stability (Thm 9.5) and integration by
parts (Thm 9.7) are again "see [1]"; Prop 3.1 is omitted; sharp time must be added; the norm is "some
(n-dependent) S-norm" (p. 215), so M changes form. Use it as a cross-check and as the Dirichlet template.

**C.3 Route E3 (Level 3).** A self-contained single-scale cluster expansion for C_E, with Lemmas S, G
and a Kirkwood-Salsburg or Mayer bound for the partition-function ratios: 40-60 pages, 5-6 rounds
(estimate). Trigger: a written r-case of Lemma 2.4.5, Lemma 2.4.6 or Theorem 3.1 does not close.
(2.4.34) alone does not trigger it, because Lemma S replaces exactly that step.

## D. Recommendation

1. **Phase 0, now, no proof:** correct Appendix C's audit in the record and in the KB (findings F1, F2).
   Name (2.4.34) in `docs/imports.md` as the input that the trace must supply. Erice I (2.2.7) may be
   cited as a second printed assertion. *Gate P0:* the four sentences of F1 are withdrawn or qualified,
   and the status of U_GJS is unchanged and said to be unchanged. No fallback is needed.
2. **Phase 1, in parallel (`mp`'s O1):** section 7 at fixed g. *Gate P1:* section 7 contains no
   `\eqref{eq:UGJS}`, and every replaced estimate cites a literal import or a lemma of the record.
   *Fallback:* section 7 waits for Phase 2.
3. **Phase 2a, first in the expansion line:** Lemmas S and G and the Jensen bound, as a stand-alone note.
   *Gate H1:* every constant is derived with its dependence (K_3(P), c_0(P)); each use of h ≥ 0 and of
   h ≤ 1 is marked; the class C_1 ∪ C_2 is explicit; two independent verification rounds return zero
   confirmed findings. *Fallback:* acquire Dimock-Glimm and check its hypotheses against the decoupled
   class (the status becomes "conditional"), or move to Dirichlet interpolation (Route E3).
4. **Phase 2b:** the table of C.0, extended to one row per display of the branch, and the written r-cases.
   *Gate H2:* no display of the branch is without a row and a verdict, and no row is without a page.
   A human reads the table against the images as a C5-like item (new items after item 9). Every
   "similarly" of the branch is replaced by a written proof. *Gate H3:* an independent agent verifies
   the written cases, and the constants are recomputed by hand in the style of G3a/G3b.
   *Fallback:* Route E3.
5. **Phase 2c:** assemble Theorem E and Corollary U; the editor makes the edits to `main.tex`.
   *Gate:* G0-G6 re-run on every changed document.

**Never:** the Hamiltonian bypass (`glimm_jaffe:result/hamiltonian-bypass-dead`), the comparison trick
of O3, re-sourcing presented as removal, and Level 2 presented as a "verified citation".

## E. Imports and sources

| source | status | role after the recommended route |
|---|---|---|
| GJS, Ann. of Math. 100 (1974) 585-632 | on disk, read (pp. 588-632) | template; Thm 1.1.7 stays A8(iv), literal (Lemma 7.4) |
| Dimock-Glimm, Adv. Math. 12 (1974) 58-83 (Annals ref. [1], p. 631; Erice II ref. [1], p. 242) | **to acquire** | only if Lemma S or G is cited: then a new, non-literal assumption item, unless it states the bound for decoupled covariances and for 0 ≤ h ≤ 1; Erice II p. 236 says [1] assumes "C ∈ B^loc_{q,δ(q)}, ∀q > 1" |
| Erice II, LNP 25, pp. 199-242 | on disk, read | cross-check; Dirichlet template for E3 |
| Erice I, (2.2.7), p. 161 | on disk, read | documentation (Phase 0) |
| Simon, Thm I.17 (= A4) | literal, imported | chaos hypercontractivity in Lemma S, as in Thm C.5 |
| Glimm-Jaffe III, Acta Math. 125 (1970) (Erice II ref. [3]) | on disk per the brief, unread | possible model for Lemma S |

A human must read on the images: the table of C.0 against GJS pp. 588-631, and C5 items 5, 6 and 9.

## F. Findings about the record

**F1 (MAJOR): Appendix C's audit says no stability estimate enters GJS's constants; GJS p. 624 shows one
does.** Locators: `main.tex` ll. 2672-2745 (M1-M5, Proposition C.1 and its proof, pp. 35-36), l. 2914
(Remark C.6), and the source `m4/r1-check.tex` (abstract item (2), Mechanisms 3 and 5, "Proposition
(structural uniformity)", "Theorem (R1 discharged)"). The sentences:
"This is the single point where h touches a quantitative estimate." (l. 2699, p. 36);
"Consequently no upper or lower bound on ∫e^{-U}dμ_0, and no stability estimate, enters any constant of
the proof." (ll. 2725-2727, p. 36);
"No Gaussian expectation, no e^{-U}, no h appears in the norm" (l. 2677, p. 35);
"Nothing else about h ... is touched anywhere" (l. 2914).
*Why they fail.* The kernels w', w of the norm (2.4.3) are defined by (2.3.4) and (2.3.8) as ratios of
integrals of e^{-V(Y_j)} under the interpolated measures (pp. 611-612). Their bound (2.4.28) is proved
from "(2.4.34) 1 ≤ ||e^{-V(Y)}||_{L_2(dPhi_C)} ≤ e^{K_3|Y|}". K_3 is "independent of C, m_0 and λ", h is
not mentioned, and the estimate is cited to [1] (p. 624). It fixes K_2 ("for K_2 ≥ K_3^2";
"K_2 = K_2(ε, m_0, K_3)") and hence every constant downstream, C_7 and C_8 included. Convergence also
uses e^{O(Vol)}, with Vol defined from suppt h (pp. 624-625). M5 is right only about the final division
(4.3)-(4.4). Theorem C.5 does not supply (2.4.34): it is a statement under dμ_0, for fixed Λ, without
linear growth in |Y|.
*Repair.* Add an item M6 (stability under the interpolated measures, (2.4.34)-(2.4.35); the convergence
factor), withdraw or qualify the four sentences, restate Proposition C.1, and correct
`docs/imports.md` ("What would discharge it") and `glimm_jaffe:problem/level2-h-trace`: the trace must
add an h-uniform stability lemma.
*Severity MAJOR, not CRITICAL.* Theorem 12.2 assumes U_GJS and does not consume Appendix C; but an
asserted claim of the record about its source is false.

**F2 (MINOR): M2 calls the covariances Dirichlet; the source decouples.** M2, l. 2683, p. 36:
"between free and Dirichlet-on-contours covariances". Annals p. 600 defines the diagonalization
"C_Y = YCY + (1 - Y)C(1 - Y)", which is decoupling, not Dirichlet; Dirichlet is the interpolation of
Erice II (p. 208). In the same audit, M1 (l. 2676) writes e^{τt} for the printed e^{γt}, and says
(2.4.4)-(2.4.5) are "built from K_1, K_2, N(Δ)", although (2.4.4) is script-K_2 = e^{-(1-ε)m_0 Σδn}.
Repair: "free and decoupled ('diagonalized', p. 600) covariances", e^{γt}, and "(2.4.4)-(2.4.5) built from
m_0, ε, K_2, N(Δ)" (script-K_2 is not the constant K_2).

**F3 (MINOR): a typo in the proof of Lemma 7.1.** `main.tex` l. 1349 has
`\|Q\widehat\psi_{T_\alpha}\|le C_8^{1/2}`, which prints as "∥leC8 n(Q)" on p. 18 of `main.pdf`.
Repair: `\|\le`.

**F4 (MINOR): the cells are not the source's localization squares.** The record uses cells [j, j+1)
(notation table l. 438; Theorem 5.1 Step 2, l. 1188; proof of Proposition 6.2, ll. 1296-1305). GJS
localize in unit squares "centered at the lattice site j in Z^2" (p. 593; p. 600, "centered at integer
coordinates"). The counts and constants are unchanged, because cell counting is translation invariant.
Repair: use [j - 1/2, j + 1/2) or say why it does not matter. A Phase-2 document must use the source's
squares.

## G. Traps

1. *"Appendix C shows that the GJS constants are independent of h."* Say instead: Appendix C audits five
   mechanisms; the stability input (2.4.34) on GJS p. 624 lies outside them (F1).
2. *"Phase 2 re-verifies the printed proof display by display."* Say instead: Phase 2 re-derives the
   B = I branch with the printed proof as template. The estimates of the branch that GJS leave as
   "bounded similarly" (pp. 621, 627) are written by the record.
3. *"After Phase 1, Theorem 7.8 is independent of U_GJS."* Say instead: after Phase 1, Theorem 7.8 no
   longer cites U_GJS. It rests on A8(iv) (GJS Theorem 1.1.7, literal), whose printed proof takes its
   constant from Theorem 1.1.8 at the same h (p. 597).
4. *"Erice I (2.2.7) makes A8(vi) literal."* Say instead: Erice I (2.2.7) is a second printed assertion,
   in square brackets, with another norm and an unspecified class of h. Its proof is a reference to
   the Annals and to Erice II (p. 193).
5. *"Theorem C.5 is the stability estimate GJS need."* Say instead: Theorem C.5 holds under dμ_0, for
   fixed Λ, without linear growth in |Λ|. GJS need e^{K_3|Y|} under every C in C_1 ∪ C_2.
6. *"The GJS expansion inserts Dirichlet boundary conditions."* Say instead: the Annals expansion
   decouples, C_Y = YCY + (1 - Y)C(1 - Y) (p. 600); Erice II uses Dirichlet lines (p. 208).
7. *"U^{M2} needs less of the expansion than U_GJS."* Say instead: U^{M2} and the B = I bound for all
   (1.1.5) observables cost the same. What the B = I branch saves is the l-terms, the annihilators
   and Chapter 4.
8. *Silent corrections.* Record verbatim, with the reading adopted: (2.0.5)'s spurious ∫_0^1 ds; p. 600's
   "Theorem 1.1.10" for 1.1.11; p. 611's "(2.0.1)" for (2.0.2); the lower bound "1 ≤" in (2.4.34)
   (Jensen gives it only for a_0 ≤ 0); the denominator of (2.3.8), which the display on p. 624 omits;
   Erice II's "K_10" for K_12 (p. 237).
9. *"Uniformly as h → 1" and "uniform in h" are different sentences.* The first is Theorem 1.1.8's
   (p. 595), the second is p. 629's. Quote both, never one for the other.
10. *"GJS prove Theorem 1.1.8."* Say instead: GJS derive it as the case B = I, T = 0 (p. 600; "B = I,
    n = 0", p. 629) of Theorem 1.1.11. The proof of that theorem leaves the needed branch to
    "similarly" and cites [1] for (2.4.34)-(2.4.35).
11. *Estimates are estimates.* The page and round counts of C and D are estimates, and every route
    here is `conjectured` until proved.
