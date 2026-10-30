# Memo `cqft2` (R1): the modern constructive toolkit

Everything proposed here is **conjectured**: proof sketches, not written to the record's standard, not verified. Every modern paper named is **from memory**, not on disk, unread. GJS pages cited were read today on `<scratch>/gjs74` images (printed page = NN + 583).

## A. Verdicts on O1-O5

**O3: refuted as stated; this changes the plan.** A comparison without regress exists if the affine path starts at the *localization* of the cutoff to a box around the observable, not at another slab cutoff.

Setup: F is a polynomial in localized monomials on GJS's lattice (squares centred at lattice sites, p. 593), all squares inside a rectangle S; B is S enlarged by R >= 1 squares; for h in C_E, h^B := h 1_B, k := h - h^B, k_i := k 1_{Delta_i}. Then h^B + alpha k lies in C_E, and GJS's own identity (1.1.12) (p. 595) gives

  <F>_h - <F>_{h^B} = - int_0^1 dalpha sum_i Cov_{h^B + alpha k}(F, U_{k_i}).

- **Cells.** Each Delta_i in supp k is separated from S by a strip of width d_i >= R. Theorem 1.1.7 (p. 594: constants "independent of h, Q_1 and Q_2") bounds each term by C_7 e^{-m_1 d_i} ||F||_GJS c_V, where c_V := lambda K_1 sum_{n>=1} |a_n| K_2^{2n} n! >= ||U_{k_i}||_GJS. The sum over i converges over the plane.
- **Start.** <F>_{h^B} <= e^{lambda|a_0||B|} S_2(B) ||F||_{L^2(dmu_0)}, by Cauchy-Schwarz, Lemma C.2 and Theorem C.5, where S_2(B) := sup of ||e^{-U_h'}||_{L^2} over h' in C_E with supp h' in B. Uniform in h, since supp h^B lies in B.

The regress of O3 is real only for paths that change the cutoff next to the observable.

The catch is where uniformity in g is won or lost. Cells in the observable's own time row are separated from it only by strips *transverse* to the time-zero line.
- The printed *statement* of Theorem 1.1.7 covers them: any localized monomials, (1.1.5) included, and "the widest strip" of any orientation.
- Its printed *proof* does not. It says "After rotating and translating the strip ... choosing A = Q_1, B_T = Q_2 in Theorem 1.1.11" (p. 597), and Theorem 1.1.11 takes A and B "of type (1.1.5)" (p. 596). A 90-degree rotation turns a sharp-time monomial into a sharp-space one, which is not of type (1.1.5) and has no finite (1.1.7) norm.
- With strips parallel to the time-zero line only, the cell sum grows with supp g: no uniformity in g.

**O1: confirmed, with a cheaper replacement.** At fixed g, take B = (rows within R of the observable's row) x (columns meeting supp g). Every cell of supp k is then separated by a strip *parallel* to the time-zero line: the regime of Lemma 7.4, which the printed proof reaches (here with a single-square (1.1.6) partner, as GJS use on p. 595). This gives

  sup_T <F>_{h_{T,g}} <= A_g ||F||_{L^2(dmu_0)} + C_7 c_V N_g (2 e^{-m_1 R}/(1 - e^{-m_1})) ||F||_GJS,

with N_g the number of columns meeting supp g. For F = X_f^{2n}, ||F||_{L^2} <= 2^n ((2n)!)^{1/2} sigma_f^{2n} (sigma_f^2 = <f,Cf>) and ||F||_GJS <= K_1 (K')^{2n} (2n)! by (8). So Lemma 7.6 holds with radius >= 1/max(K', sqrt(2) sigma_f). Neither Simon's V.11 nor Rosen nor Omega_g in L^p(dphi_0) is needed.

**O2: confirmed.** Refinement: sections 10-11 consume (M_2) only for g in G (setting of l. 1955; Lemma 10.2 via Lemma 3.1(iii)). C_H is needed only for the moment clause of Theorem 12.2(5), l. 2313. Restricting to G helps no method in C (G allows arbitrarily many transitions per unit length).

**O4: confirmed, and sharpened.** The O3 comparison is the strongest re-sourcing available. It rests (M_2) on a printed statement the record already imports (A8(iv)), in the Annals norm, with no new source. Still a status change, not a proof: the transverse case has no printed proof.

**O5: modified.** A Level-2 trace of the Annals text reaches U^{M2} only through the time-direction proof of Theorem 1.1.8 (pp. 627-629, partly read today); the transverse case lies outside the printed proof of Theorem 1.1.7, so no trace of it supplies that case. A Level-3 isotropic expansion (M1) proves both. No non-expansion method fits this cutoff class.

## B. Statements to prove

**(S1, Phase 1).** For every g in C_H there are A_g, B_g < infinity, depending on (lambda, P, m_0, C_7, m_1, K_1, K_2) and on g only through supp g, such that for all s, all T > |s| and every sharp-time cylinder polynomial F at time s:

  |int F dq_{h_{T,g}}| <= A_g ||F||_{L^2(dmu_0)} + B_g ||F||_GJS.

Effect: Lemma 4.3(ii), Lemmas 7.1-7.3 and 7.6, Proposition 7.5 and Theorems 7.7-7.8 stop depending on A8(vi). They rest on A8(iv) (literal), in the regime its printed proof reaches; the gap clause of Theorem 12.2(5) follows.

**(S2, Phase 1', optional).** U^{M2} over all of C_E: for every h in C_E and every real measurable h' with ||h'||_inf <= 1 and supp h' in an interval of length 2,

  int V(h')^2 dq_h <= M'^2 := e^{15 lambda|a_0|} S_2(B_15) ||V(h')^2||_{L^2(dmu_0)} + C_7 c_V ||Q_V||_GJS sum_{l>=1} (8l+12) e^{-m_1 l},

with B_15 a box of 3 x 5 squares, ||Q_V||_GJS as in (5), and ||V(h')^2||_{L^2} <= 9^{p'} ||V(h')||_{L^2}^2 (the hypercontractive step in the proof of C.5). M' is independent of h and of the position of h'. Effect: Theorem 5.1, hence Lemma 10.2 through Theorem 12.2, rests on literal imports only. Caveat: A8(iv) is used where its printed proof does not reach.

**(S3, Phase 2).** An isotropic clustering theorem of the record. There are eps_0(P) > 0, m > 0 and C such that, for lambda/m_0^2 <= eps_0, every h in C_E, and all localized sharp-time or space-time monomials Q_1, Q_2 at Euclidean distance d >= 1:

  |Cov_h(Q_1,Q_2)| <= C e^{-md} N(Q_1) N(Q_2)  and  |<Q>_h| <= C N(Q),

with N a kernel norm growing at most like K^{deg} deg!. With Route L this proves S2 outright, and A8(iv) and A8(vi) become theorems of the record.

## C. Routes

**L. Localize and compare (classical; recommended for Phase 1).**
- *Delivers:* S1 (parallel strips) and S2 (transverse strips).
- *Steps:*
  1. Path-derivative lemma, by dominated convergence with dominator |F||U_k|(e^{-U_{h^B}} + e^{-U_h}) in L^1 (A3, C.5).
  2. Decomposition into (1.1.5) and (1.1.6) monomials on GJS's lattice.
  3. Strip widths and shell counts.
  4. Theorem 1.1.7, term by term.
  5. The starting value, via C.2 and C.5.
  6. Corollaries for sections 5 and 7.
- *Length:* 6-9 pp, 2 verification rounds.
- *Imports:* none new.
- *Risk:* low for S1. The one reading needed is that a (1.1.5)-(1.1.6) pair under a parallel strip is covered. S2 needs the printed statement accepted in the transverse case.

**M1. BKAR forest formula + polymer expansion** (Brydges-Kennedy, Abdesselam-Rivasseau, Kotecky-Preiss; from memory).
- *Delivers:* S3, hence S2 and S1.
- *Hypotheses:* P bounded below, no evenness; weak coupling only.
- *Where uniformity is won:*
  - Vertices: delta U_h / delta Phi(x) = lambda h(x) :P'(Phi(x)):, majorised by lambda at first contact (as in M3 of Appendix C).
  - Per-cube stability is exactly Theorem C.5 with Lambda = Delta. A functional of the field on Delta has the same law under the interpolated covariance C(X)(x,y) = X_{Delta(x)Delta(y)} C(x,y) as under C.
  - Cubes decouple by a Gaussian Hölder inequality, "Sigma <= p blockdiag(Sigma) implies E prod F_Delta <= prod ||F_Delta||_p" (from memory). For two variables it is consistent with Nelson's condition p >= 1 + |rho|, so it should follow from A4's abstract form. It does not involve h.
  - C(X) keeps C's diagonal blocks, so Wick ordering is unchanged and the ultraviolet estimates are the cube-local Lemmas C.3-C.4.
- *Where uniformity is lost:* nowhere.
- *Sharp time:* harmless. There are no Dirichlet lines, and C(X) restricted to a time line is a Schur product of positive kernels. The decoupling is isotropic, so it gives the transverse case directly.
- *Risk:* the tree sum with local factorials.
  - A cube with n tree lines carries a Gaussian factor of order (n!)^{(2p'-1)/2}.
  - Its tree neighbours are distinct cubes, so prod e^{-m_0 d} <= e^{-c m_0 n^{3/2}} (my heuristic).
  - Lines between adjacent cubes do not decay and must be paid for by lambda. This bookkeeping, with every constant derived, is the step most likely to slip.
  - Fallback: M3's Dirichlet decoupling.
- *Length:* 45-70 pp, 4-6 rounds.
- *Verdict:* beats a Level-3 rewrite of the GJS contour and annihilator expansion, and is the only route here that proves the transverse case.

**M2. Battle-Federbush phase cells** (from memory). Multiscale, built for ultraviolet problems. Here Wick ordering plus C.5 already settle the ultraviolet, and one scale suffices. No gain; about twice M1's length.

**M3. Glimm-Jaffe, *Quantum Physics*, cluster-expansion chapter** (from memory). A possibly more legible, isotropic (Dirichlet-line) base for Level 2 or 3. Coverage of [0,1]-valued h and sharp-time observables: unknown; acquire before judging. Length 25-40 pp as a trace base.

**M4. Variational Boué-Dupuis (Barashkov-Gubinelli; from memory).**
- *Delivers:* bounds on log Z and on exponential moments of smeared fields, on tori or weighted infinite volume, possibly at any coupling. For S2 it needs volume-uniform *local* bounds for every [0,1]-valued h.
- *Where uniformity is lost:* the pathwise estimates pair Wick powers of regularity -eps with h (drift)^m. Multiplication by h on B^s_{p,p} (s > 0) is bounded only through h's regularity. By my own heuristic, a profile with N transitions per unit length has multiplier norm of order N^s, unbounded over C_H and over G.
- *Sharp time:* needs a trace argument.
- *Clustering:* none.
- *Length:* at least 60 pp; risk high. Not viable for this class.

**M5. Stochastic quantization (Da Prato-Debussche, Mourrat-Weber, Gubinelli-Hofmanova; from memory).**
- *Delivers:* "coming down from infinity" local moment bounds for the invariant measure, uniform in volume and initial data, at any coupling.
- *Where uniformity is won:* the cross terms lambda h :Z^k: v^m are absorbed by the coercive lambda h v^{2p'} pointwise, with the common weight h (Young).
- *Where it is lost:* at M4's multiplier step. The slab indicator of [-T,T] in Euclidean time is itself a jump in a spatial direction of the SPDE.
- *Extra steps:* invariance of dq_h under the regularized dynamics; the limit kappa to infinity (C.4-C.5); the sharp-time trace via the Da Prato-Debussche splitting.
- *Length:* 60-100 pp; risk high.
- *Payoff:* U^{M2} beyond weak coupling, which strengthens Theorem 5.1 but not Theorem 7.8.

**M6. Correlation inequalities.**
- GKS holds for P = Q - mu X with Q even and mu >= 0, under free, Dirichlet and half-Dirichlet boundary conditions (Simon's book §VIII.3, Thm VIII.13, pp. 273-274; text layer only). Lebowitz and Newman bounds need the Griffiths-Simon class (from memory).
- d<F>/dh(x) = -lambda Cov(F, :P:(x)), and the Wick counterterms enter with the opposite sign (:phi^4: = phi^4 - 6c phi^2 + 3c^2). So GKS-II gives no monotonicity in h under free boundary conditions, and moments of Wick powers are not sign-definite.
- Not viable; even P only; at most a cross-check of Corollary 5.2.

## D. Recommendation

1. **Phase 1, first: S1 by Route L.**
   - Gate D1: an appendix in which every application of Theorem 1.1.7 states its pair types, a strip parallel to the time-zero line, its width, and the C.2/C.5 constants.
   - G0-G6 rerun on the new pages.
   - A C5-like human reading of pp. 593, 594, 596 and 597.
   - Fallback: mp's fixed-g Hamiltonian replacements.
2. **Phase 1', in parallel, at the author's choice: S2 by Route L.**
   - Gate: the author and editor accept in writing that A8(iv) is used at its printed statement scope in the transverse case, and the import note quotes the p. 597 sentence.
   - Otherwise S2 is not claimed and A8(vi) stays.
3. **Phase 2: S3 by M1** (or cqft's Level-2 trace of Theorem 1.1.8, aimed at S2 alone).
   - Gate: G0-G6 plus an independent hand recomputation of the tree and polymer constants.
   - Fallback: Phase 1/1' status.
4. **Never:** M2, M4, M5 or M6 as routes.

## E. Imports and sources

**Route L.**
- Imports, all already in the record: A3; A4 (via C.5); A8(i) (class, p. 589, read); A8(iv) (Theorem 1.1.7, p. 594, read).
- (1.1.12) (p. 595, read) is re-proved, not imported.
- New assumption items: none.
- Human page reading still needed: p. 593 (squares centred at lattice sites; (1.1.5)), p. 596 (Theorem 1.1.11's A and B "of type (1.1.5)"), p. 597 (the rotation sentence).

**Acquisition list for M1/M3.** None is on disk; bibliographic data from memory and unverified; read each statement before use.
1. Brydges-Kennedy (1987): the forest formula.
2. Abdesselam-Rivasseau (1995), "Trees, forests and jungles": BKAR, positivity of the interpolated matrix.
3. Kotecky-Preiss (1986): polymer criterion; or Brydges' Les Houches course (1984).
4. A Gaussian Hölder (Brascamp-Lieb-type) inequality, or a proof of it in the record from A4.
5. Glimm-Jaffe, *Quantum Physics* (2nd ed.): the cluster-expansion chapter.
6. Rivasseau, *From Perturbative to Constructive Renormalization* (1991).

**Not to acquire** (they document section C only): Barashkov-Gubinelli, Gubinelli-Hofmanova, Mourrat-Weber, Da Prato-Debussche.

**On disk:** Simon's book §VIII.3 (read on the text layer only); GRS 1975, Parts 1-2 (unread).

## F. Findings

- **F1 (MINOR).** l. 1349 (proof of Lemma 7.1): `\|Q\widehat\psi_{T_\alpha}\|le` is missing a backslash; the PDF prints the letters "le" instead of "<=". Repair: `\|\le`.
- **F2 (MINOR).** GJS squares are "centered at the lattice site j_i in Z^2" (p. 593). The record uses cells [j, j+1) (ll. 438, 1188, 1260, 1296) and "the row of unit squares meeting x^0 = -t/2" (l. 1452) without saying that this is GJS's lattice translated by (1/2, 1/2), which is legitimate by translation covariance of C_E, dq_h and the norms. Harmless: Lemma 7.4's width t-2 holds in both conventions. Repair: one sentence in A8(iii).
- **F3 (MINOR, no current consequence).** l. 673 transcribes "(any orientation)", and ll. 2661-2663 say Theorem 1.1.7 "needs no separate scope discussion". The printed proof (p. 597) reaches sharp-time monomials only for strips parallel to the time-zero line. The record uses only that case (Lemma 7.4); any transverse use must say so.

## G. Traps

1. Not "Route L verifies GJS's uniformity" but "Route L derives (M_2) from the printed statement of Theorem 1.1.7 and Appendix C; it verifies none of GJS's proofs".
2. Not "U_GJS removed" after Phase 1' but "A8(vi) is no longer assumed; (M_2) rests on A8(iv) at its printed statement scope, in a case its printed proof does not reach".
3. Not "CE1 follows from CE2" but "for observables of bounded support, with constant A ||F||_{L^2(dmu_0)} + B ||F||_GJS, not C_8 ||F||_GJS".
4. Not "Theorem 7.8 is unconditional" but "Theorem 7.8 no longer depends on A8(vi)".
5. Not "uniform because 0 <= h <= 1" but "h enters only through vertices bounded by lambda and stability bounds proved for 0 <= h <= 1 (C.3-C.5)".
6. Not "modern methods give the uniform moment" but "no non-expansion method is known to this member (from memory) to be uniform over [0,1]-valued measurable cutoffs".
7. Not "a Level-2 trace can confirm S2's input": the printed proof of Theorem 1.1.7 does not cover the transverse sharp-time case.
