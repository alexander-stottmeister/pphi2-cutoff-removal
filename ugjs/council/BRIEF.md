# Brief for the council: a plan to remove the hypothesis U_GJS from Theorem 12.2

Round 1 (R1), 28 October 2026. Orchestrator: the author's Claude Code session.
Paths are relative to the repository root `glimm_jaffe/` unless they start with
`<scratch>`, which is the session scratchpad named in section 2.

## 0. What you are part of

This repository (`pphi2-cutoff-removal`, public; this folder is its working tree) is an
AI-assisted research record. Its document of record, `part_i/main.tex` (40 pp, last
mathematical change 5 September 2026), proves Theorem 12.2 -- norm convergence of the
full net of spatially cutoff P(phi)_2 ground states on every local algebra, at weak
coupling -- as an implication from eight standing imports A1-A8. Seven are literal
quotations of printed theorems. The eighth, A8(vi), written U_GJS, is not: it is the
cutoff-uniform form of the Glimm-Jaffe-Spencer moment estimate, assembled from four
printed pages, and the record does not re-derive the cluster expansion. Theorem 12.2 is
therefore reported as **proved, conditional on U_GJS**.

The author now wants **a plan to remove that conditional**: to make Theorem 12.2 rest on
nothing but literal imports and the record's own proofs. The council's deliverable in this
round is not the proof but the **plan**: which statement to prove, by which route, in
what order, at what cost, under which gates, and what each phase makes unconditional.

Five members: a constructive quantum field theorist who reads the printed
Glimm-Jaffe-Spencer expansion (`cqft`), a second constructive member for the modern
toolkit (`cqft2`), a mathematical physicist for functional analysis, imports and exact
quantifiers (`mp`), an algebraic quantum field theorist for the architecture of the proof
and what it consumes (`aqft`), and the handling editor of a high-profile
mathematical-physics journal (`editor`). In R1 each member reads independently and writes
a memo; no member sees another's memo. In R2 the editor synthesizes the memos into
`ugjs/PLAN.md`, which is then checked adversarially (R3) and put before the author (R4).
Nothing is executed before the author approves.

## 1. The hypothesis, exactly

`part_i/main.tex` ll. 693-705, Assumption A8(vi), tag `(U_GJS)`, label `eq:UGJS`, p. 10:

    C_E^slab := { h_{T,g} = 1_{[-T,T]} (x) g : T > 0, g in C_H }  subset of  C_E,

    one and the same constant C_8 satisfies
    | int Q(x^0) dq_{h_{T,g}} | <= C_8 ||Q(x^0)||_GJS      (T > 0, g in C_H).

The classes (Definition 2.1, ll. 392-409): C_E = measurable h: R^2 -> [0,1] with compact
support; C_H = measurable g: R -> [0,1] with compact support; G = smooth g in C_H with
g = 1 on a nonempty open interval (the net). The norm ||.||_GJS is the printed
(1.1.7)-(1.1.9) of GJS, transcribed at ll. 668-680 (`eq:printednorm`): one overall K_1,
local weight K_2^{2N(Delta)} N(Delta)! per unit square, ||w||_2 of the kernel, K_2 >= 1
fixed. The source's own one-sentence statement (Thm 1.1.8, p. 595, Source Fact 2.3,
ll. 684-691) says "uniformly as h -> 1"; the slab-family quantifier is the one GJS state
on p. 629 (Source Fact 2.4, ll. 710-718) and consume on pp. 594-597 (item (vii'),
ll. 720-777); the Scope paragraph (ll. 779-804) gives the three-step reading and says why
it is still a named hypothesis: "assembled from four pages of the source rather than read
off one theorem, and ... this manuscript does not re-derive the cluster expansion."

**Where it is consumed** (every site read by the orchestrator today):

| site | lines | what is consumed |
|---|---|---|
| Lemma 4.3(ii) `lem:slabunbdd` | 1085-1121 | finiteness of square moments `int F^2 dq_{h_{T,g}}` to extend the slab Feynman-Kac-Nelson identities to unbounded F; the proof says U_GJS "supplies those square moments at every later application" |
| Theorem 5.1 `thm:M2`, Step 5 | 1218-1226 | `int V(h)^2 dq_{h_{T,g}} <= C_8 ||Q_V||_GJS <= M^2`, with M^2 = 9 C_8 K(p') lambda^2 (sum |a_n|)^2 explicit (ll. 1158-1164); this is the only place where uniformity in g is used, and it is used for every g in C_H |
| Lemma 7.1 `lem:transfer` | 1329-1351 | `sup_T ||Q psi-hat_T||^2 <= C_8 n(Q)^2` at one fixed g |
| Lemma 7.2 `lem:onepoint` | 1353-1388 | square moments at the needed times, "as in Lemma 7.1", fixed g |
| Lemma 7.3 `lem:twopoint` | 1390-1425 | square moments at two times, fixed g; the bounded family u_T |
| Lemma 7.6 `lem:expmom` | 1504-1536 | Lemma 7.1 with the GJS-norm growth K_1 (K')^{2n} (2n)!, so that exponential moments of phi_0(f) under |Omega_g|^2 d phi_0 are finite for s < 1/K' |
| Proposition C.7 `prop:discharge` | 2919-2937 | "Assume U_GJS": the coverage statement |
| Theorem 12.2 `thm:MAIN` | 2295 | "Assume U_GJS, namely Assumption A8(vi)" |

Downstream of these: Lemma 10.2 `lem:localize` (ll. 1992-2013) applies Theorem 5.1 at
every path cutoff g_s and gives `||V_j Omega_s|| <= M`; Lemma 10.3 `lem:tworegime`
(ll. 2014-2050) uses that M in both regimes; Proposition 10.4, Lemma 10.5, Theorem 11.1,
Propositions 11.2 and 12.1 and Theorem 12.2 inherit it. Lemma 7.4 `lem:ce2strip`
(ll. 1427-1469) uses only CE2 (Source Fact 2.2, printed, constants independent of h).
Proposition 7.5, Theorem 7.7 and Theorem 7.8 (ll. 1471-1621) consume U_GJS only through
Lemmas 7.1-7.3 and 7.6: Prop. 7.5 needs its constant C-hat_Q finite, Theorem 7.7 needs
some s_0 > 0 with finite exponential moments, Theorem 7.8 needs C-hat_Q finite. Item (5)
of Theorem 12.2 (ll. 2311-2317) restates Theorem 7.8 and Theorem 5.1.

**What the record already did towards removal.** Appendix C `app:huniform`
(ll. 2650-2937, p. 35): a mechanism audit M1-M5 of GJS sections 2-4 (every point of
contact with h: kernel norms, h-free covariances, h in vertices majorised at first
contact by |lambda h(x)| <= lambda, exact identities, termination cancelling every
e^{-U}); Proposition C.1 `prop:struct` (ll. 2729-2745), "deliberately limited to the
audited mechanisms; it makes no completeness claim about portions of the source
expansion not reproduced here"; Lemma C.2 `lem:Z` (normalisation Z(h) >= e^{-lambda
|a_0| |Lambda|}); Lemmas C.3-C.4 and Theorem C.5 `thm:stability` (sup over h in C_E
with supp h in a compact Lambda of ||e^{-U_h}||_{L^p(d mu_0)} < infinity, every p);
Remark C.6 (the class 0 <= h <= 1 is used exactly through h >= 0 and h <= 1);
Proposition C.7 (coverage). Its source is `m4/r1-check.tex` ("Gate R1, discharged").

**What the knowledge base says** (read today; `python3 <KB>/kb.py show <id>` prints a
node and is the one `kb` command you may run):

- `glimm_jaffe:problem/level2-h-trace` (open, not scheduled): "trace the h-dependence
  display by display through the printed cluster expansion of GJS pp. 598-629, so that
  the slab-uniform moment estimate becomes a derived statement rather than an import,
  completing prop:struct"; judged disproportionate on 5 September 2026.
- `glimm_jaffe:result/hamiltonian-bypass-dead` (status partial): g-uniform local
  moments were open in 1970-71 (Expositions p. 57: N^loc <= const (H(g)+I) "should be
  valid, uniformly in g"); Expositions Lemma 4.2.2 / London Thm 10.4 cover only
  translation-averaged states; Expositions Thm 3.1.3 (Rosen) has constants independent
  of V and kappa, not of g; a first-order form bound cannot replace (M_2). "A verdict
  on the printed record, not a no-go theorem."
- `glimm_jaffe:decision/ugjs-imported-at-source-scope`, `glimm_jaffe:import/u-gjs`
  (status non-literal), `glimm_jaffe:problem/c5-second-reader` (nine verbatim items,
  verdicts blank), `common:reference/glimm-jaffe-spencer-1974` and
  `common:reference/glimm-jaffe-expositions` (the verified claims you may cite from
  those two sources without re-reading them; everything else must be read at the page).
- `strategy.md` ll. 2223-2275 ("Part I scope amendment", 5 September 2026) records:
  "section 7 (gap) needs only fixed-g, T-uniform finiteness; section 5 (M_2) needs
  g-uniformity along the affine paths"; Level 2 = the h-trace; Level 3 = full
  reconstruction; both "disproportionate for a record whose imports are named". That
  judgement is what the author is now overriding: the question is no longer whether but
  how.

## 2. Reading list and the page-image corpora

Read in this order; paths relative to the repository root.

1. `docs/status.md`, `docs/imports.md` (the public statement of what U_GJS is and is not).
2. `companion/council/labels.md`: every number you may cite, generated from
   `part_i/main.aux` (current: `main.tex` last changed 20 September 2026, the table 23
   October). `companion/companion.pdf` (20 pp) is a reader's guide to the record; its
   section 4 is about U_GJS.
3. `part_i/main.tex`: the abstract and title-page notices (ll. 60-122); Definition 2.1
   (ll. 392-409); A1-A8 in full (ll. 453-827); sections 4, 5, 7 in full (ll. 1034-1621);
   Lemmas 10.2-10.3 (ll. 1992-2050); Theorem 12.2's statement (ll. 2291-2330);
   section 14 (ll. 2495-2553); Appendix C in full (ll. 2650-2937). Section starts:
   3 at l. 901, 4 at 1034, 5 at 1154, 6 at 1252, 7 at 1323, 8 at 1623, 9 at 1781,
   10 at 1953, 11 at 2151, 12 at 2224, 13 at 2385, 14 at 2495, App. A 2556, App. B 2587,
   App. C 2650, bibliography 2944.
4. `m4/r1-check.tex` (the source of Appendix C, with its own section "The gate"), and,
   for `mp` and `aqft`, `m4/h6.tex` ("what the gap cannot do, and how much less than
   (H6) suffices") and `m4/m2-audit.tex` (the (M_2) source-scope audit).
5. `part_i/C5_reading_record.md`; `part_i/README.md` (gates G0-G6: the standard a new
   document of this record must meet).
6. The sources. `refs/` holds third-party PDFs on this machine only (never committed).
   Their text layers garble formulas, and the JSTOR scan of the Annals paper is garbled
   even in running text on the expansion pages; **read the page images**, which the
   orchestrator rendered today into the scratchpad
   `<scratch> = /private/tmp/claude-501/-Users-alex-Documents-Uni-Hannover-claude-glimm-jaffe/8bac9e45-6e21-41a1-bdb8-e018c3356462/scratchpad`:
   - `<scratch>/gjs74/p-NN.png`, NN = 01..49, 170 dpi, from `<scratch>/gjs74.pdf` =
     J. Glimm, A. Jaffe, T. Spencer, *The Wightman axioms and particle structure in the
     P(phi)_2 quantum field model*, Ann. of Math. 100 (1974) 585-632. **Printed page =
     NN + 583.** Section map from the text layer (verify on the image before citing):
     1. The particle structure p. 585; 1.1 The main results p. 590 (Thms 1.1.1-1.1.3
     p. 590, 1.1.4-1.1.6 p. 591, 1.1.7 p. 594, 1.1.8 p. 595, Cor. 1.1.9, Thms 1.1.10,
     1.1.11 p. 596); 2. Inserting contours p. 600 (Props 2.1.1 p. 604, 2.1.2 p. 605,
     Lemma 2.2.1 and Props 2.1.1'/2.1.2' p. 606, 2.3 The increasing contour expansion
     p. 608, 2.4 Norms for convergence p. 612, Table 1 p. 614, Thm 2.4.1 p. 615, Lemmas
     2.4.2 p. 616, 2.4.3 p. 617, Prop 2.4.4 p. 619, Lemmas 2.4.5 p. 620, 2.4.6 p. 622);
     3. Contours removed p. 625 (Thm 3.1 p. 626); 4. The n-particle cluster expansion
     p. 627 (Thm 4.1 p. 628, Thm 4.2 p. 629, Lemma 4.3 p. 630).
   - `<scratch>/erice1/p-NN.png`, NN = 01..67, 150 dpi, from `<scratch>/erice-part1.pdf`
     = J. Glimm, A. Jaffe, T. Spencer, *The particle structure of the weakly coupled
     P(phi)_2 model and other applications of high temperature expansions, Part I:
     Physics of quantum field models*, in: G. Velo, A. Wightman (eds.), *Constructive
     Quantum Field Theory* (Erice 1973), Lecture Notes in Physics 25, Springer 1973,
     pp. 132-198. **Printed page = NN + 131.**
   - `<scratch>/erice2/p-NN.png`, NN = 01..44, 150 dpi, from `<scratch>/erice-part2.pdf`
     = the same, *Part II: The cluster expansion*, pp. 199-242. **Printed page =
     NN + 198.** Contents: 1 Introduction, 2 The main results (p. 205), 3 The cluster
     expansion (p. 208), 4 Clustering and analyticity: proof of the main results
     (p. 215), 5 Convergence: the main ideas (p. 218), 6 An equation of
     Kirkwood-Salsburg type (p. 222), 7 Covariance operators (p. 224), 8 Derivatives of
     covariance operators (p. 228), 9 Gaussian integrals (p. 232), 10 Convergence: the
     proof completed (p. 239; the brief first said p. 240, corrected 28 October after the
     knowledge-base review of the Erice reference node). Theorem pages per the text layer, to be verified: Thms
     2.1, 2.2 p. 206; Cor 2.3 p. 207; Cor 3.4 p. 211; Thm 3.5 p. 212; Thm 6.1 p. 222;
     Prop 7.1 p. 224; Prop 8.1 p. 228; Thm 9.1, Lemma 9.2 p. 234; Prop 9.3, Thm 9.4
     p. 236; Thm 9.5 p. 237; Lemmas 10.1, 10.2 p. 240.
   - Other sources on disk, by text layer or by rendering a page yourself with
     `pdftoppm -r 200 -png -f N -l N "<pdf>" <scratch>/<prefix>` (render **only into
     the scratchpad**; the repository's ignore rules and commit hook refuse rasters, and
     the publication boundary forbids them): `refs/Simon - The P(\Phi)_2 Euclidean
     (Quantum) Field Theory.pdf` (418 pp; its text layer mentions a hypercontractive
     bound "Theorem V.11(iv)" and section I.5), `refs/Glimm & Jaffe - Quantum Field
     Theory and Statistical Mechanics - Expositions.pdf` (405 pp; Theorem 3.1.3 (Rosen,
     higher order estimates) at book p. 32 = PDF 46, Theorem 7.4, p. 57 = PDF 71),
     `refs/Rosen - 1970 - A lambda phi^2n field theory without cutoffs.pdf`,
     `refs/Guerra et al. - 1975 - ... Part 1.pdf` and `Part 2.pdf`, the Glimm-Jaffe
     series I-IV, Nelson 1973, Osterwalder-Schrader.
   - **Not on disk** (you may name them `from memory` as candidates to acquire; you may
     not cite their contents): Rosen 1971 (higher order estimates, CPAM 24),
     Simon-Hoegh-Krohn 1972 (J. Funct. Anal. 9), Dimock-Glimm 1974, Glimm-Jaffe
     *Quantum Physics*, Spencer 1974, Battle-Federbush, Brydges' and Rivasseau's
     cluster-expansion expositions, Abdesselam-Rivasseau, Barashkov-Gubinelli,
     Gubinelli-Hofmanova, Newman 1975, Lebowitz 1974.

## 3. Facts verified by the orchestrator today (page images; cite with these locators)

- Erice Part I, p. 160 (section 2.2, "Relevance to Physics"): "The Schwinger functions
  with a space time cutoff h are given by (2.2.1) S_h(x_1,...,x_n) = int Phi(x_1) ...
  Phi(x_n) dq_h where dq_h is the measure (2.2.2) dq_h = e^{-V(h)} dPhi / int e^{-V(h)}
  dPhi", dPhi Gaussian with covariance (-Delta + m_0^2)^{-1} = C, "V(h) = lambda int
  :P(Phi(x)): h(x) dx is the P(phi)_2 Euclidean action. If h(x) is the characteristic
  function for a set Lambda ... then V(h) is the action for Lambda." Observables (2.2.3)
  A = prod_{i=1}^n int :Phi(x)^{n_i}: f_i(x) dx with f_i in L_2(R^2) or f_i =
  delta_s(t) f_i(x-vec), f_i in L_2(R); supp A = the smallest union of unit lattice
  squares containing the supports. Theorem 2.2.1 (Vacuum Cluster Expansion
  [Gl Ja Sp 1, 2]): gamma = m_0 - epsilon, epsilon > 0, lambda < lambda(epsilon, P, m_0),
  d = dist(supp A, supp B); "there exists a constant M_{A,B} such that (2.2.4)
  | int AB dq_h - int A dq_h int B dq_h | <= M_{A,B} e^{-gamma d}, uniformly in h."
  No class of h is specified on pp. 160-161 beyond "space time cutoff".
- Erice Part I, p. 161, inside square brackets after Theorem 2.2.1: each f_i supported
  in a single square Delta_i; N(Delta) = sum of the n_i with supp f_i in Delta; "Let K_1
  be given and let eta = prod_Delta (K_1 N(Delta)!). We define for a localized A,
  (2.2.5) ||A|| = eta prod_{i=1}^n ||f_i||" (L_2 norms, of f_i(x-vec) in the sharp-time
  case); "Let us assume n_i <= n-bar. Then for K_1 sufficiently large, (2.2.6) M_{A,B}
  <= ||A|| ||B||. If it is not the case that n_i <= n-bar, we obtain (2.2.6) with eta^3
  replacing eta in (2.2.5). Also (2.2.7) int A dq_h <= ||A|| uniformly in h.]" (printed
  without absolute-value bars). This norm differs from the Annals norm (1.1.7): no K_2,
  and K_1 per square instead of once overall.
- Erice Part I, p. 162 (text layer, to be confirmed on `erice1/p-31.png`): the proof of
  Theorem 2.2.2 takes "0 < h_0 < h_1 < 1 ... two space-time cutoffs", the path
  h_alpha = alpha h_1 + (1 - alpha) h_0, differentiates (2.2.2), and applies
  Theorem 2.2.1 and (2.2.6); then "We let h_0, h_1 be characteristic functions of sets."
  p. 163: "Since the cluster estimates are uniform in h, they carry over to the infinite
  volume limit h = 1."
- Erice Part II, p. 205 (section 2): (2.2) V(Lambda) = int_Lambda :P(Phi(x)): dx in
  L_p(S', dPhi_C), (2.3) e^{-lambda V(Lambda)} in L_p for all p in [1, infinity) and
  Re lambda >= 0; "To simplify the discussion, we take Lambda to be a union of lattice
  squares, and in the limits Lambda -> infinity, we further restrict Lambda to be a
  square centered at the origin." Footnote 5: "More general cutoffs, as required for
  the proof of Euclidean covariance of the limit Lambda -> infinity, can be introduced
  by inserting a nonnegative L_infinity function h in the integral (2.2). Such an h does
  not affect the subsequent discussion." (2.4) Z(Lambda) = Z(Lambda, C) = int
  e^{-lambda V(Lambda)} dPhi_C; (2.5) dq_Lambda = dq_{Lambda,C} = Z(Lambda,C)^{-1}
  e^{-lambda V(Lambda)} dPhi_C, with C in the set of convex combinations of Dirichlet
  covariance operators (1.6).
- Erice Part II, p. 206: observables (2.7) A = int :Phi(x_1)^{n_1}: ... :Phi(x_j)^{n_j}:
  w(x_1,...,x_j) dx with w in S(R^{2j}) ("although weaker bounds would suffice");
  Theorem 2.1 (lambda in the closure of the half circle (2.1), epsilon/m_0^2
  sufficiently small, d the width of a strip separating supp A and supp B): "There is a
  constant M = M_{A,B} and a positive constant m independent of A and B such that
  | int AB dq_{Lambda,C_emptyset} - int A dq_{Lambda,C_emptyset} int B dq_{Lambda,C_emptyset} |
  <= M_{A,B} e^{-md}, uniformly in Lambda, as Lambda -> infinity. Furthermore, M is
  independent of translations in either A or B." (The subscript is C with the empty-set
  symbol, the free covariance of (1.5), p. 202; the brief first wrote C_0, corrected 28
  October after the knowledge-base review.) Theorem 2.2: "Let lambda belong to the closure of the
  half circle (2.1), and let epsilon/m_0^2 be sufficiently small. For A of the form
  (2.7), | int A dq_{Lambda,C} | is bounded uniformly in lambda and in Lambda, as
  Lambda -> infinity." Note: (2.7) has Schwartz kernels in space-time; the record's
  observables are sharp-time.
- Annals pp. 598 and 626 text layers (`pdftotext`): running text partly legible, every
  display garbled. The council reads images.

## 4. Non-negotiables (the workspace's AGENTS.md binds you; these are the parts that matter here)

1. Never state a fact about a file that you have not read in this session; label
   anything recalled `from memory`. Never invent a theorem number, page, quotation,
   author, constant or page count. Render the page before asserting what a display says.
2. Status words: proved / partial / conjectured / numerical / refuted for claims;
   literal / non-literal for imports. Theorem 12.2 is "proved, conditional on U_GJS".
   A route you propose is `conjectured` until someone proves it; say so.
3. Every theorem, lemma and equation number of the record comes from
   `companion/council/labels.md`.
4. Quantifiers written out. Every constant you name: what it depends on, what it is
   uniform in. "Sufficiently small" only with the source's own hypothesis named.
5. Cost estimates are in pages of finished proof and in rounds of verification, not in
   hours; and they are labelled as estimates.
6. Read-only on everything except your own memo file. You may write scratch files and
   page images **only** under `<scratch>`. No `git` command that changes state; no `kb`
   command except `show`; no edit to any other file; no build; do not spawn agents.
7. If you believe the record is wrong or unclear somewhere, it goes into section F of
   your memo with a locator and a severity (CRITICAL / MAJOR / MINOR), not anywhere else.

## 5. The orchestrator's conjectures, to be confirmed, refuted or modified (all `conjectured`)

- **O1 (section 7 at fixed g).** Section 7 consumes U_GJS only for finiteness at one
  fixed g, uniformly in T, with no use of the value of the constant: Lemmas 7.1-7.3 need
  `sup_T int Q(s)^2 dq_{h_{T,g}} < infinity` for the sharp-time monomials Q of section 6
  (and finiteness at each T for the Feynman-Kac-Nelson extension, Lemma 4.3(ii)); Lemma
  7.6 needs `E_{mu_g}[X_f^{2n}] <= C_g (K_g)^{2n} (2n)!` for some constants depending on
  g, so that some s_0 > 0 exists; Proposition 7.5, Theorems 7.7 and 7.8 then go through
  with g-dependent constants, and the gap value m_1 comes from CE2 alone. Candidate
  replacements, each a printed theorem or a lemma already in the record: the slab
  Feynman-Kac-Nelson identities (A2, Lemma 4.1) and the ratio bound
  ||psi_{s'}|| / ||psi_s|| <= 1/c_g of Lemma 4.4; an L^2 -> L^q bound for the
  interacting semigroup e^{-t H(g)} at fixed g for t >= t_q (Simon's book, "Theorem
  V.11(iv)" per its text layer, to be read; Simon-Hoegh-Krohn 1972 `from memory`), or
  alternatively Rosen's higher-order estimates (Expositions Thm 3.1.3) with the standard
  bound ||Q (N+1)^{-r/2}|| < infinity and the semigroup's smoothing e^{-t_0 H} Omega_0
  in D(H^k); Theorem C.5 and Lemma C.2 for the small-T range (support in a fixed
  compact set); Gaussian moments of X_f for Lemma 7.6 together with Omega_g in L^p(d
  phi_0) for all p (source to be located). If O1 holds, Theorem 7.8 (G) is conditional
  on CE2 only, and the gap clause of Theorem 12.2(5) becomes unconditional.
- **O2 (the irreducible core).** After O1, U_GJS is consumed only in Theorem 5.1, hence
  only through Lemma 10.2 and the moment clause of Theorem 12.2(5). The minimal
  replacement statement is

      U^{M2}:  sup_{T>0, g in C_H} int V(h)^2 dq_{h_{T,g}} <= M^2
               for every real measurable h with ||h||_infinity <= 1 and supp h in an
               interval of length 2, with M depending on (lambda, P, m_0) only;

  equivalently (by Theorem 5.1's Steps 5-6, which need only this), sup_{g in C_H}
  ||V(h) Omega_g|| <= M. One observable type, degree <= 4p', at most three unit cells
  (Theorem 5.1, Steps 1-4). No statement about arbitrary polynomials and no factorial
  bookkeeping in the degree is needed any more.
- **O3 (no comparison trick).** U^{M2} cannot be obtained from CE2 (printed,
  h-independent constants) plus fixed-g bounds by the affine-path identity of GJS
  (1.1.12): the cells of supp(g' - g) that meet the localization squares of V(h)^2 have
  no separating strip, their covariance terms need moments of V(h)^2 V(g_i) at every
  intermediate cutoff, and Cauchy-Schwarz turns the needed second moment into a fourth
  one -- an infinite regress. Check this; a loophole here would change the plan.
- **O4 (re-sourcing is a status change, not a removal).** Erice Part I (2.2.7) is a
  printed one-line statement of an h-uniform moment bound; with GJS p. 629 it would let
  the import be documented as literal in the knowledge base's sense ("taken at the scope
  the source itself prints"). But its norm is not the Annals norm the record's constants
  use, its class of h is unspecified, its proof is a reference to the Annals paper, and
  Erice Part II's footnote 5 is an assertion, not a proof. The council decides what a
  referee would accept and what the record should say; the orchestrator's view is that
  the author's request means a proof, and that re-sourcing is at most a Phase 0.
- **O5 (the two proof routes for U^{M2}).** Level 2: an h-trace, display by display, of
  the printed proof of Annals Theorem 1.1.8 (Theorem 4.1 of section 4, which rests on
  Theorem 3.1 and Theorem 2.4.1 with Lemmas 2.4.2-2.4.6 and Propositions 2.1.1-2.1.2,
  2.4.4), recorded as a table "display / where h enters / verdict / what the record
  adds", plus own proofs of whatever the printed text asserts without display, so that
  Proposition C.1's limitation is lifted; or the same trace through Erice Part II
  sections 3-10 with h inserted per its footnote 5, adapted to the sharp-time observable
  (Part II's (2.7) has Schwartz kernels). Level 3: a self-contained proof of U^{M2} in
  the record, by a cluster expansion written for the slab family (classical
  Dirichlet-interpolation style, or a modern forest-formula formulation), or by a
  non-expansion method (the variational Boue-Dupuis method of Barashkov-Gubinelli, the
  stochastic-quantization bounds of Gubinelli-Hofmanova, correlation inequalities for
  phi^4 -- all `from memory`, none on disk).

## 6. The memo

Write `ugjs/council/memo-<role>.md` (`cqft`, `cqft2`, `mp`, `aqft`, `editor`): at most
3500 words for sections A-G (`cqft` and `cqft2` may use 5000, because they carry the
route details); the editor's sections H-K come on top. Exactly these sections:

A. **Verdict on O1-O5.** For each: confirmed / refuted / modified, with the reasons and
   the locators (record lines or source pages read on the image).
B. **The statement(s) to prove.** Written out with every quantifier and the dependence
   of every constant, for each phase you propose. Say what each one makes unconditional
   in the status vocabulary (which theorems of the record change status, and to what).
C. **Routes.** For every route you consider viable: the base (printed source and pages,
   or the method), the steps as a numbered list, the deliverable (document, where it
   lives, how it attaches to `part_i/main.tex`), an estimate of pages of finished proof,
   the imports it needs with their status (on disk and read / on disk unread / to
   acquire), and the risk: the one step most likely to fail, and what happens then.
D. **Recommendation.** The phasing you recommend (what first, what in parallel, what
   never), with a gate for each phase (a checkable criterion, in the style of
   `part_i/README.md` G0-G6) and the fallback if the phase fails.
E. **Imports and sources.** The complete list of external statements the recommended
   route would rest on, with status; which of them become new assumption items, which
   are literal, which still need a page read by a human.
F. **Findings** about the record itself (optional): locator, the exact sentence or
   display, why it fails, a repair if you see one, severity. Or the word "none".
G. **Traps.** Claims a plan or the final document would be tempted to make and must not,
   each with the correct wording.

Report back to the orchestrator in your final message (not in the memo): the memo path,
its word count (`wc -w`), your recommended route in at most 3 lines, and your F findings
in at most 5 lines. Do not paste the memo.

## 7. Role cards

**cqft: the reader of the printed expansion.** You know the Glimm-Jaffe-Spencer
cluster expansion in both printed forms, the Dirichlet-covariance interpolation, the
contour and annihilator expansion of the Annals paper, its norms (1.1.7)-(1.1.9) and
(2.4.3)-(2.4.5), Table 1, and the Erice lectures. Your job: read, on the images, the
whole printed proof of Annals Theorem 1.1.8 -- from Theorem 4.1 (p. 628) back through
Theorem 3.1 (p. 626), Theorem 2.4.1 and Lemmas 2.4.2-2.4.6 (pp. 615-624), Propositions
2.1.1-2.1.2 and Lemma 2.2.1 (pp. 604-606), the expansion steps of sections 2.2-2.3
(pp. 606-612) -- and produce the **map** the Level-2 document would have to fill: for
each printed theorem, lemma and numbered display, where h enters (vertex, measure,
normalisation, nowhere), whether the printed constant is h-independent on its face or by
the reasoning of Appendix C's M1-M5, and what a complete trace must add. Count the
displays. Then do the same, more briefly, for Erice Part II sections 3-10 with footnote
5's h inserted, and say which base you would trace and why; address the sharp-time
observable (Annals (1.1.5), Erice I (2.2.3) allow delta_s(t) f(x); Erice II (2.7) does
not). Decide whether the trace should target full U_GJS (all sharp-time polynomials in
the Annals norm) or only U^{M2}, and what the Level-2 document can honestly claim at the
end: a theorem of the record, or a verified citation of a proof. Judge O4: what Erice
(2.2.7) is and is not. Estimate the Level-2 document's length and the Level-3 escalation
if a step's h-dependence cannot be read off. You own section C for the expansion routes.

**cqft2: the modern constructive toolkit.** You know cluster expansions in their later
formulations (Brydges-Kennedy and Abdesselam-Rivasseau forest formulas, Battle-Federbush
phase-cell expansions, the Glimm-Jaffe book's version), and the non-expansion methods
for P(phi)_2 and Phi^4: the variational (Boue-Dupuis) method of Barashkov-Gubinelli,
stochastic quantization and the "coming down from infinity" bounds of
Gubinelli-Hofmanova, correlation inequalities (Griffiths, Lebowitz, Newman's Gaussian
domination) for phi^4-type interactions. None of these papers is on disk: everything you
say about them is `from memory` and you label it so, and your route descriptions name
exactly which statements would have to be acquired and read before use. Your job: for
each candidate method, the exact statement it could deliver for U^{M2} -- the sharp-time
observable V(h)^2 at time zero, under dq_{h_{T,g}} with h_{T,g} = 1_{[-T,T]} (x) g, g any
measurable [0,1]-valued function of compact support, uniformly in T and g -- its
hypotheses (coupling range, polynomial P, evenness), the point where the uniformity over
[0,1]-valued cutoffs rather than regions Lambda is won or lost, the sharp-time issue, an
estimate of the length of a self-contained proof in this record's standard (every
constant derived), and the risk. Say which, if any, beats the classical route, and
whether any gives U^{M2} beyond weak coupling (which would strengthen Theorem 5.1 but
not Theorem 7.8). Read the record's section 5 and Appendix C before judging; Theorem
C.5 is the record's own h-uniform stability bound and shows how the class 0 <= h <= 1
enters. You also own the "import acquisition" list.

**mp: functional analysis, quantifiers, imports.** You own O1 and O2. Go through Lemma
4.3(ii), Lemmas 7.1-7.3, 7.6, Proposition 7.5, Theorems 7.7-7.8 and write, as precise
statements with proof sketches, the fixed-g replacements: which hypotheses each needs,
which printed source supplies each (locate the theorem in Simon's book or the
Expositions on disk and give its page; what is not on disk is `to acquire`), where the
small-T and large-T ranges split, whether an L^2 -> L^q semigroup bound or Rosen's
higher-order estimates (or both) are needed, and what Omega_g in L^p(d phi_0) requires.
Check that no constant of section 7 propagates into sections 9-12 (the gap value m_1
enters as gamma; Lemma 7.6's radius 1/K' and Proposition 7.5's C-hat_Q must not). Write
U^{M2} with every quantifier and check against Lemma 10.2 and Theorem 5.1's Steps 5-6
that nothing more is consumed; say whether Lemma 10.2 could live with a bound depending
on the cell index j through r_j (it cannot, the orchestrator believes, because the net is
not Cauchy otherwise -- check). List what Appendix A (constants) would have to say after
each phase. You also check O3 carefully, as an estimate.

**aqft: the architecture.** You think in nets of algebras, states, folia, ground states,
and in what a proof consumes. Your job: (i) trace the g-uniform M from Lemma 10.2 through
Lemma 10.3, Proposition 10.4, Lemma 10.5 and Theorem 11.1, and judge whether the
local-perturbations-perturb-locally architecture admits any weakening of (M_2) -- a
g-dependent M with controlled growth, a dependence on the local profile of g near the
cell, a form bound in place of the vector bound, a use of the gap to bound local moments
(the Expositions p. 57 statement) -- and say why not, or how; (ii) say what Theorem 12.2
and its item (5) become after each phase (split the gap clause from the moment clause),
and what Corollary 12.3, Theorem 13.2 and section 14 must say; (iii) judge the standard:
A1-A7 are printed theorems whose proofs the record does not re-verify; after a Level-2
trace, U^{M2} would be a printed theorem whose proof the record *has* re-verified
display by display; after Level 3 it would be a theorem of the record. Is the first
already the standard of A1-A7, or less, or more? What does the final record say in
each case, and how would the companion's section 4 and figure 1 change? (iv) O3 and O4
from your side: whether anything in Theorems 1.1.1 or 1.1.7 of GJS (printed, literal)
plus the record's fixed-g results could yield U^{M2} by an operator-algebraic argument
(cyclicity, local normality, the Fock folium of Proposition 11.2) rather than by an
estimate.

**editor: the handling editor.** You decide what "removed" means and whether the plan
is proportionate. Deliver, in addition to A-G: (H) the acceptance criteria: for each
outcome (re-sourced; section 7 unconditional; U^{M2} by Level 2; U^{M2} by Level 3), the
status words the record may use for Theorem 12.2, A8(vi), Theorem 5.1 and Theorem 7.8,
and what a referee of a high-profile journal would still object to; (I) the
proportionality: which phases are worth their cost for *this* record, which should be
offered to the author as optional, and what the record should say if the core phase
stalls; (J) the deliverable form: new documents and their names (a supplement to Part I,
an Appendix D, a separate paper?), the exact edits to `part_i/main.tex` each phase forces
(title-page notice, abstract, Theorem 12.2's hypothesis list, A8(vi), Appendix C,
Appendix B's residue, the C5 record), the companion's and `docs/` changes, and how the
new work attaches to the gate system G0-G6; (K) the plan skeleton you will write in R2:
section list, phases with gates, the verification rounds (who verifies what; the human
reading of page images as a C5-like item for the trace), and the two author
checkpoints. Keep your reading notes: in R2 you receive the other four memos and write
`ugjs/PLAN.md`.
