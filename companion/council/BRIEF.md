# Brief for the council: a reader's companion to the cutoff-removal theorem

Round 1 of 6, 23 October 2026. Orchestrator: the author's Claude Code session.

## 0. What you are part of

This repository (`pphi2-cutoff-removal`, public; working tree = this folder) is an
AI-assisted research record. Its document of record, `part_i/main.tex` (40 pp), proves
Theorem 12.2 -- norm convergence of the full net of spatially cutoff P(phi)_2 ground
states on every local algebra, at weak coupling -- *conditional on* one imported
hypothesis, U_GJS. The record is written for verification, not for reading: 61 numbered
statements, eight standing imports, every constant derived, every chain explicit.

The council's task is a **reader's companion**: a new document, `companion/companion.tex`,
at most 20 pages, that a working mathematical physicist can read in 45 minutes and come
away knowing what is proved, under what hypothesis, why it was open, how the proof works,
what is not claimed, and where in the record each step lives. Chains of reasoning are
short; details are weighed, not treated as equally relevant; figures illustrate the main
findings.

Four members: an AQFT person (`aqft`), a QI person (`qi`), a constructive-QFT
mathematical physicist (`cqft`), and the handling editor of a high-profile
mathematical-physics journal (`editor`). In this round (R1) each member reads the record
independently and writes a memo; no member sees another's memo. In R2 the editor
synthesizes the four memos into an outline and a figure list (`companion/PLAN.md`), which
the author approves before drafting (R3), editing (R4), adversarial verification (R5) and
publication (R6).

## 1. The audience

A working mathematical physicist or strong graduate student who knows what a C*-algebra,
a state, a ground state, a spectral gap, a Feynman--Kac formula and a cluster expansion
are, has not read the record, and has 45 minutes. They are sceptical of AI-assisted
mathematics and will look first for what is being oversold.

## 2. Reading list (paths relative to this folder; read in this order)

1. `README.md`: at least "What this is", "Status", "The proof in five pictures".
2. `docs/status.md`, `docs/imports.md`, `docs/index.md`.
3. `companion/council/labels.md`: every number you may cite, generated from `main.aux`.
4. `part_i/main.tex` (152 KB). Read the abstract and section 1 in full (lines 60-360;
   section 1.4, lines 245-360, is the record's own attempt at an operator-algebraic
   overview); section 2.4 "Standing imports" in full (lines 453-828; A8 includes the
   Scope paragraph and item (vii')); sections 2.5-2.6; the statements of every numbered
   result (`docs/results.json` has them all); the proofs in your role's area; section 14
   (lines 2495-2555); Appendix B. Section starts: 3 at line 901, 4 at 1034, 5 at 1154,
   6 at 1252, 7 at 1323, 8 at 1623, 9 at 1781, 10 at 1953, 11 at 2151, 12 at 2224,
   13 at 2385, 14 at 2495, App. A 2556, App. B 2587, App. C 2650.
5. `docs/results.json`: the 61 statements with statement text, dependencies (`uses`,
   `proof_uses`), `imports_A8`, `cites_UGJS`. Machine-readable; `python3 -c` is the
   quickest way in.
6. `part_i/README.md`: gates G0-G6, the G6 findings and their dispositions, the step
   maps from the Lamport reconstructions.
7. `part_i/C5_reading_record.md`.
8. Part II (`cqft` and `editor`): the addenda at the top of `part_ii/README.md`, the
   Part II table in `docs/status.md`, the abstract and section 1 of
   `part_ii/gate_II11_scoping.tex`.
9. `strategy.md` (160 KB, chronological): do not read it whole. grep for
   "Part I scope amendment", "GATE STATUS", "Hamiltonian bypass".
10. `docs/PLAN.md` and `docs/figures/make_figures.py`: what the site computes vs draws.

Optional, low priority: `refs/` holds the source PDFs on this machine (they are not in
the public tree). You may open one to check a quotation; `pdftotext` garbles formulas,
so render the page (`pdftoppm -f N -l N -png -r 120 <pdf> <prefix>`) before asserting
that a formula differs. A discrepancy goes into section G of your memo, never into the
companion.

## 3. Facts of the record you build on (all read by the orchestrator today)

- Theorem 12.2 (`thm:MAIN`, p. 30): (1) full-net convergence with rate Psi_{m_1}(d) for
  g = 1 on O_d; (2) local normality; (3) ground state in the spectral sense;
  (4) translation and, for even P, Z_2 invariance; (5) spec H(g) in {0} u [m_1, inf),
  dim ker H(g) = 1, and the uniform local moment. Status: **proved, conditional on U_GJS**
  (and on the literal imports A1-A7).
- Imports: A1-A7 are literal quotations of printed theorems; A8 is the GJS package (CE1,
  CE2, the printed norms, U_GJS). Of the 61 numbered statements, 24 reach A8 through
  their proof chain (computed by `docs/extract.py`). Lemma 9.1 does not.
- U_GJS, in the record's wording: A8(vi), the cutoff-uniform form of GJS Thm 1.1.8 on the
  slab family h_{T,g}; since 5 September 2026 imported at the scope at which the source
  states it (p. 629) and uses it (pp. 594-597: the affine path and the derivation of
  Thm 1.1.7 from 1.1.8); not a quantifier strengthened beyond the source; still a named
  hypothesis, because it is assembled from four pages and the cluster expansion is not
  re-derived (Appendix C audits the mechanism and proves two analytic prerequisites only).
- Negative scope (abstract, section 1.3, section 14): no uniqueness of omega_inf among
  locally normal ground states; no sharp exponential rate (the solvable quadratic model
  has poly(d) e^{-2 m_1 d}; the filter cannot do better: strip analyticity); nothing
  outside 0 <= lambda/m_0^2 < eps_P (Thm 13.2, conditional on Hyp. 13.1).
- Open items: C5 (a second human reader of the GJS page images; nine items, all verdicts
  blank; a transcription check, not mathematics); Level 2 (h-trace of GJS pp. 598-629,
  the only proportionate route to an unconditional theorem; not scheduled); the
  Hamiltonian bypass for (M_2) is recorded as dead (a verdict on the printed record, not
  a no-go theorem).
- Part II: nothing in Part I depends on it. The root README says "open at gate (II.11)";
  that wording governs. `strategy.md` and V4's ledger say "(II.11) closed at the stated
  import scope"; `part_ii/README.md` says "phase closure NOT yet reached". The record is
  internally inconsistent here; the companion says so in one sentence and uses the
  README's wording. The per-claim statuses are the table in `docs/status.md`.
- Corrections of 25 September 2026 that the companion must respect: Lemma 9.1(i) is
  credited only with W_gamma in L^1 and finite moments of every order (hence
  T_gamma(r) <= C_{q,gamma} (1+r)^{-q}); the computed kernel shape ("shallower than t^-2
  early, steeper than t^-6 late", one admissible chi) is a numerical observation about
  one choice of chi, never a lemma. Psi_gamma is an upper bound on a norm difference,
  never a measured decay of any state.
- The page-1 notice of every public document of this record: AI-assisted, not refereed,
  C5 open, human verification ongoing (README, first section).

## 4. Non-negotiables (the workspace's AGENTS.md binds you; these are the parts that matter here)

1. Never state a fact about a file that you have not read in this session; label anything
   recalled `from memory`. Never invent a theorem number, page, quotation or author.
2. No new mathematics. The companion explains the record; it proves nothing more and
   claims nothing less. Contextual remarks (how a step relates to methods the reader
   knows) are allowed if marked as context and if they cite only the record's own
   bibliography (the `\bibitem`s of `main.tex`).
3. Status words: proved / partial / conjectured / numerical / refuted. Theorem 12.2 is
   "proved, conditional on U_GJS"; never "proved" bare.
4. Every theorem, lemma and equation number comes from `companion/council/labels.md`.
5. The U_GJS wording of section 3 above: nothing stronger, nothing weaker.
6. If you believe the record is wrong or unclear somewhere, it goes into section G of your
   memo with a locator and a severity (CRITICAL: the result does not follow; MAJOR: a step
   asserted without valid justification; MINOR: exposition). Not into the companion.
7. Read-only on everything except your own memo file. No `git` command that changes
   state, no `kb` command, no edit to any other file, no build. Do not spawn agents.

## 5. The memo

Write `companion/council/memo-<role>.md` (`aqft`, `qi`, `cqft`, `editor`): at most 2500
words for sections A-F and H; G and the editor's I-M come on top. Exactly these sections:

A. **Must know** (at most 5 items). One sentence the reader must retain, plus locator(s)
   (number and page from labels.md).
B. **Should know** (at most 8 items). Same format.
C. **Pointer table.** The statements and sections a human reader should *not* read in the
   companion: one line each, why it is routine or bookkeeping, where it lives. This is
   where "do not treat everything as equally relevant" is decided.
D. **The longest chain.** The longest inferential chain in the record as the reader
   experiences it, as a numbered list of steps with locators; then your proposal for
   cutting it into pieces of at most 3 steps, each ending at a displayed checkpoint
   (a statement the reader can hold on to).
E. **Figures.** At most 4 proposals of your own (purpose; what is drawn; what is computed
   vs drawn; what the figure must NOT suggest). Then a verdict on each of the seven
   candidates F1-F7 below: keep / change (how) / drop (why).
F. **Traps.** Statements a companion would be tempted to overstate, each with the correct
   wording.
G. **Findings** about the record itself (optional): locator, the exact sentence or display,
   why it fails, a repair if you see one, severity. Or the word "none".
H. **Your reader's first question**, one paragraph: what *your* community asks first, and
   the answer the companion should give.

Report back to the orchestrator in your final message (not in the memo): the memo path,
its word count (`wc -w`), and your G findings in at most 5 lines. Do not paste the memo.

## 6. Candidate figures

Vector only (TikZ/pgfplots; TeX Live 2026 has both); every caption ends "Illustration,
not evidence"; one colour, the site's `#8250df`, marks everything conditional on U_GJS.

| # | figure | serves |
|---|---|---|
| F1 | Architecture spine: GJS CE2 (printed) and CE1 as U_GJS (dashed, conditional colour) -> (M_2) Thm 5.1 and (G) Thm 7.8 -> LPPL Prop 10.4 -> Cauchy Thm 11.1 -> Thm 12.2 with its five items | Tier 1: the one picture to retain |
| F2 | The affine path and the three moves: g, g' = 1 on O_d, the path g_s = (1-s)g + s g', the derivative dot Omega_s = -H_s^{-1} Q_s V(v) Omega_s annotated with filter / light cone / clustering | why standard tools fail, and what replaces them |
| F3 | The filter: hat W_gamma(E) = chi(E)/E with the notch on [-gamma/2, gamma/2] (left); abs W_gamma(t) on log-log axes with its envelope (right), computed by `make_figures.py` | super-polynomial but not exponential |
| F4 | Two-regime bound (Lemma 10.3): spacetime, the cone O_{abs t}, the cell B_j at distance r_j, the switch at abs t = r_j/2 from 2M e^{-gamma r_j/4} to 2M | light cone meets gap |
| F5 | Slab transfer: h_{T,g} = 1_{[-T,T]}(x^0) g(x^1) in the (x^0, x^1) plane; e^{-T H(g)} Omega_0, normalised, -> Omega_g by simplicity alone (Lemma 4.4); sharp-time moments <-> matrix elements of e^{-t H(g)} | Euclidean input to Hamiltonian output; the gap as an output |
| F6 | The rate Psi_gamma(d) (Lemma 10.5): its two summands and the (1+d)^{-N} envelopes, computed | assembly |
| F7 | Status map: proved / conditional on U_GJS / open, for the 61 statements of Part I (24 conditional, from `results.json`) and the Part II table | what is conditional, precisely |

The site already has five static figures (`docs/figures/*.svg`; `docs/PLAN.md` lists
them): F3 and F6 reuse its computed curves, F4 redraws its light cone, F1 replaces its
61-node import graph by the spine.

## 7. Role cards

**aqft: the algebraic quantum field theorist.** You think in nets of von Neumann
algebras, states and folia, GNS, spectrum conditions, ground and KMS states, w*- versus
norm topology on local duals, local normality and quasi-equivalence. Your reader asks: in
what sense omega_inf is a ground state of (A, alpha) (Prop 12.1: the spectral sense; alpha
the patched Glimm--Jaffe dynamics of A6: is alpha a one-parameter automorphism group of A,
and where is that imported?); why norm convergence on A(O)* and not w*, and what it buys
(Prop 11.2: the local Fock folia); whether Cor 12.3 says the Glimm--Jaffe vacuum is
*unique* (it says canonical for the cutoff family; uniqueness among locally normal ground
states is explicitly not claimed); what the plateau net is and why it is directed
(Def 2.1); what simplicity of the ground state is used for (Lemma 4.4, Prop 8.2); why
"the ground-state property costs an identity, not an estimate" (Prop 12.1). Judge
section 1.4 of `main.tex` as a first draft of the companion: which paragraphs are already
right, which chains are too long, which parentheticals must go.

**qi: the quantum-information theorist.** You think in gapped Hamiltonians,
Lieb--Robinson bounds, quasi-adiabatic continuation (Hastings;
Bachmann--Michalakis--Nachtergaele--Sims; both are in the record's bibliography), local
perturbations perturb locally, spectral flow, filter functions with fast-decaying Fourier
transforms, and you know that the quasi-adiabatic filter is super-polynomial but
subexponential for the same reason the record gives. Your reader asks: why the standard
machinery does not start (V(g') - V(g) has infinite norm; no Lieb--Robinson bound for
continuum bosons; the exact light cone of A6 / Prop 2.7 replaces it); what the LPPL
estimate is here (Lemmas 10.1-10.3, Prop 10.4); why the gap must be uniform in the cutoff
(Thm 7.8) and what the moment (Thm 5.1) does ("the operator-algebraic softening of
unboundedness"); why super-polynomial and not exponential (Lemma 9.1 and the
strip-analyticity remark of section 1.4; section 14 names what a sharp rate would need);
how Psi_gamma is assembled (Lemma 10.5) and what its two summands mean; the
eight-cells-per-shell count. Any analogy to quasi-adiabatic continuation is context
(rule 4.2), citing only [Hastings] and [BMNS] as the record cites them; do not import
facts about those papers from memory beyond what the record says.

**cqft: the constructive quantum field theorist.** You know the Glimm--Jaffe construction
(I-IV), Nelson's Euclidean methods, the Feynman--Kac--Nelson formula, hypercontractivity,
Simon's P(phi)_2 book, Guerra--Rosen--Simon, the Glimm--Jaffe--Spencer cluster expansion
(Thms 1.1.1, 1.1.7, 1.1.8, 1.1.11; the norms (1.1.7)-(1.1.9)), the spatial cutoff g, the
Expositions volume. Your reader asks: exactly what is imported (A1-A8 with sources, as
the record cites them); what U_GJS is and whether the source-scope reading (A8 Scope
paragraph, item (vii'), Source Facts 2.2-2.4) is fairly described, judged as a reader of
the record; how the Euclidean -> Hamiltonian transfer works (section 4 slab lemmas;
Lemma 4.4, normalisation by simplicity only; section 5, (M_2) via fourth moments and the
GJS norm of V(h)^2; section 6, norms and cell counts; section 7: CE2 on a strip ->
semigroup decay -> density Thm 7.7 -> gap Thm 7.8) and why there is no circularity; the
scaling reduction (section 3, Prop 3.2) and why the dimensionless condition matches the
source's; which of the 61 statements are routine bookkeeping: your section C is the most
important of the four. You also own the Part II page: read the three Part II items of
the reading list and draft, as an extra section P, the one-page account using the
README's "open" wording and the `docs/status.md` table verbatim.

**editor: the handling editor.** You are the handling editor of a high-profile
mathematical-physics journal. You decide what a 45-minute reader needs, in what order,
at what density, and you arbitrate every weighting dispute in R2. In addition to A-H
deliver: (I) a first outline with a page budget per section, total at most 20 pages
including figures; (J) the editorial rules you will enforce in R4 (starting proposal: no
paragraph with more than three inferential steps without a displayed checkpoint; every
section opens with the one sentence to retain; one figure per Tier-2 idea; forward
references only to numbered statements of the record); (K) the referee's first three
questions and where the companion answers each; (L) a draft abstract of at most 150 words
and a draft page-1 status notice of at most 80 words; (M) what in section 1.4 of
`main.tex` is already right for the companion and what must change. Keep your reading
notes: in R2 you receive the other three memos and write `companion/PLAN.md`.
