# Part II implemented route

**Repair addendum (16 August 2026; supersedes all earlier phase-closure and open-
residue statements below).**  A fresh reconstruction and source audit found and the
canonical files now repair: V2's omitted four-edge sector; the false asymmetric-band
cross equality; the need to take the real part of the asymmetric mixed surrogate;
the undefined shifted remainder; the missing $j=3$ input-tail derivation; V3's
compressed periodic tails and finite-mode normalization; and the invalid use of
interaction coercivity for compactness at $\lambda=0$.  V4 and the gate consume the
repaired statements.  All target PDFs compile without unresolved references or
citations.  The controlling strategy and independent post-repair checks are in
`../repair_2026_08_16/`; the full Lamport reconstruction, critical report, source
PDFs, and screenshot dossier are in `../fresh_audit_2026_08_16/`.

**Status addendum (2026-08-12).** Part I of the programme is closed:
`../part_i/main.tex` (36 pp) is the document of record for the spatial-cutoff removal
theorem (gates G0–G6 in `../part_i/README.md`); nothing in this folder depended on the
former Part I status, and no document here required amendment. The single remaining
Part II gate is (II.11); its preparatory scoping pass is
`gate_II11_scoping.tex` (this folder, 9 pp): minimal logical requirements
(pointwise-in-ξ suffices — uniformity demoted), the sharp-time momentum-source
obstruction (Lemma 2.1: the H⁻¹ integral diverges, so step (2) of the old attack plan
is unimplementable as written), the amended architecture (thermal two-torus route,
statements A1–A8, with the interchange and Laplace-transfer lemmas proved), the
fallback route B and its precise defect, the import-acquisition list
(Høegh-Krohn 1974; Figari–Høegh-Krohn–Nappi 1975), and the V0–V4 execution phases with
gates. Phase V0 (numeric falsification checkpoint) **passed 2026-08-12**:
`v0_checkpoint.py` / `v0_checkpoint.out` — thermal formulas ED-verified (corner-projected
CCR checks after a truncation-artifact diagnosis), thermal rate t-uniform (slopes drift
0.0000; measured decay 2^{−1.01r}), interchange mechanism verified on Wick-quartic toys,
and the A4b dictionary constant identified and confirmed to 3.6e-10:
δ_∞ = log(4/π)/(2π). Phase V1 **complete 2026-08-12**:
`v1_thermal_representations.tex` (12 pp) proves A2(a) (kernel identity + exact
interacting mean-shift representation — the harmonic jump interpolant is Mehler-chain
harmonic exactly, the shift constant is the classical action = the momentum half of
¼Q^{(t)}, and the shift phase cancels the CCR phase), A3(a) (lattice + continuum free
closed forms, two independent proofs agreeing), and A3(b) (thermal fixed-coarse rate,
uniform on [t₀,∞]); A2(b) is reduced to the single clause (A1-iv) (periodic FK for
e^{−tK_L}), reassigned to V3. Phase V2 **complete 2026-08-12**:
`v2_interaction_comparison.tex` (16 pp) proves A4(a) (same-noise coupling;
‖`\mathcal U_N`−`\mathcal U`‖_{L²} ≤ C(1+t)(1+L)·ε_N·log_N^{3/2}, all three error mechanisms —
dispersion/missing-modes/aliasing — at O(ε²log^{2–3}) of the squared norm; the second
chaos via an exact-square identity), A4(b) (dictionary |δ_N − log(4/π)/(2π)| ≤ C(m,L)ε_N
with explicit constant; convention lock: truncation-convention polynomial is
φ⁴ − 6δ_∞φ² + 3δ_∞², gate endpoint defined in the lattice-matched convention), A4(c)
(closed-form interpolant H = (ρ/2)sh(ω(s−t/2))/sh(ωt/2); shift fields bounded by coarse
data Σ_M(p) uniformly in N; symbol convergence at rate 2^{−r(1+η)/2}; shifted-interaction
comparison O(2^{−r(1+η)/4} + ε_N log_N)), and A5 (uniform-in-N Nelson bounds, plain and
shifted, by the Part-I App-C pattern: dyadic comparison scale, Γ(e^{−τ})
hypercontractive comparison, doubly-exponential tail). Import register in its §8.
Phase V3 **complete 2026-08-12**: `v3_continuum_package.tex` (15 pp) proves Statement
A1 in full and closes A2(b) — (A1-i) K_L constructed as the strong limit of mode-truncated
semigroups, self-adjoint, ≥ −c_λ and ≥ ½H₀−c, acting as H₀+V_L on cylinder vectors
(operator and form sum; ESA/Segal uniqueness scope-fenced as not consumed); (A1-ii)
e^{−tK_L} trace class ∀t>0 with `\mathcal J_1`-norm cylinder approximation, discrete spectrum,
μ_j ≥ ½ν_j−c, eigenvalue convergence (hypercontractive ladder + one Duhamel at t₂=2s₄
⟹ norm convergence; eigenvalue-DCT); (A1-iii) positivity improving (limit FK + Simon
Thm I.16 two-time pair positivity) ⟹ simple ground state Ω_L > 0, gap γ_L > 0,
ω^{ct}_{L,λ} = its vector state on `\mathfrak W(T_L)`; (A1-iv) Z_∞(t) = Z₀(t)E_per[e^{−`\mathcal U_t`}] and
the Weyl mean-shift identity for e^{−tK_L} in V1 Def 8.1's exact form for all D4-refined
symbols — A2(b) closed (Cor 6.3). Import decision: **proof, not import** — Høegh-Krohn
(1974)/FHN (1975) not consumed; only printed import = Simon-book Γ(A) cluster
(I.12/I.15/I.16/I.17 — the Part-I A:hyper source), dossier addendum E19–E23 with page
images in `dossier_images/`. Phase V4 **proof content complete 2026-08-12**: `v4_assembly.tex` (9 pp) proves A6
(|F_N(t;ξ) − F_∞(t;ξ)| ≤ C_ξ(2^{−rη/4} + ε_N log^{3/2}), via the two mean-shift
representations compared on the V2 coupling space; new action-prefactor and
source-phase lemmas), A7 (normal-ordered partition convergence Z̃_N(t) → Tr e^{−tK_L}
∀t; uniform Ẽ₀-bound; scoping Lemma 3.2 ⟹ Ẽ_j(N) → μ_j, E₁(N)−E₀(N) → γ_L > 0 —
the derived eventual gap — and D_N(t) → D_∞(t)), and A8 (spectral tail bound + scoping
Lemma 3.1 ⟹ **gate (II.11) closed** pointwise in M, ξ; Weyl-reduction Thm 1.1 +
Cor 3.1 + Prop 4.1 ⟹ full-sequence identified fixed-coarse theorem: unique Ω_∞ on
`\mathfrak W_∞` with Ω_∞ = ω^{ct}_{L,λ}∘β, ℤ₂-invariant; the cofinal-subnet cluster statement is
superseded). Errata register (v4 Rem 1.1): V1 (14) integrand reading (interaction only);
scoping A7 free-factor display must be normal-ordered. **Phase closure: NOT yet reached.** The adversarial pass over V0–V4 was run
2026-08-12 but was cut short by usage-credit exhaustion: reviewers for V1, V3 and
V4+scoping completed; the V2 reviewer and the cross-document interface/citation auditor
died mid-run; the independent verification fleet never launched. 14 findings (0
breaking, 5 moderate, 9 minor) were adjudicated by the author instead of independent
refuters and **all 14 are repaired** (all five documents recompile clean). The five
moderate ones: V1 display (15) double-counted the Wick correction (Appell property);
V1 import (I1) cited the flat-kernel model-sheet FK where the Mehler-reference FK is
needed — repaired by restating (I1) as V3 Thm 3.1(ii) under the lattice dictionary,
with an acyclicity note (this shows erratum E1 was understated); V3 Thm 4.1(i)'s form
extension was invalid (lower semicontinuity runs the wrong way) — repaired by a
self-contained Legendre/resolvent-antitonicity argument needing no form core; V3
Lemma 2.5 needed hypothesis (N0) (ℓ-increments ≤ log 2, automatic for the full tails
used); the symbol-difference exponent is −2, not −3 (V4 Lemma 3.2(ii), V2 Lemma 6.4 —
both conclusions survive). New V4 Lemma 6.3 supplies the injective *-hom
β: `\mathfrak W_∞` → `\mathfrak W_{ct}` that Weyl-reduction Cor 3.1 assumes. **Round 2 (12 Aug 2026) closed those coverage gaps** — V2 review, interface/citation
audit, 4 audits of the round-1 repairs, and the verification layer; 11 agents, all
completed. It found **one BREAKING defect, independently by both reviewers and
confirmed by four verifiers: V2 Corollary 5.2 (the "convention lock") was false.** The
lattice and continuum fields' equal-point variances differ by the same δ_∞ as their
Wick constants, so the offsets cancel and **no counterterm survives: the gate endpoint
is (a,b) = (0,0) and the continuum polynomial is plain φ⁴** (V3 §1 had inherited the
wrong endpoint, which would have identified the limit with the ground state of the
wrong operator). No estimate in V0–V4 changes: V3 is proved for arbitrary (a,b) and V4
was already written for (0,0). δ_∞ = log(4/π)/(2π) remains correct as the tadpole
offset. Round 2 also found **7 of the 14 round-1 repairs not sound**, including one
(the hypercontractive-ladder fix) that a failed edit script had never written to the
file, and a numbering regression in which a newly numbered V1 display silently broke 8
citations in V4 (fixed by de-numbering it). All round-2 findings are repaired; all five
documents recompile clean (0 errors, 0 undefined refs, 0 overfulls; V1 13pp, V2 17pp,
V3 16pp, V4 10pp, scoping 10pp). **Round 3 (12 Aug 2026)** audited the round-2 repairs, re-reviewed the corrected
convention, and added an end-to-end chain auditor charged with the species of error
round 2 exposed (is the gate's endpoint the same object at every link?). A mechanical
presence check first confirmed 26/26 round-2 edits were in the files. Outcome: **13
findings, all MINOR — 0 breaking, 0 moderate**, the first round with nothing above
minor, and the chain trace found no mismatch. Two of the round-2 repairs were themselves
slightly wrong (a mis-transcribed constant, 2π too large; and a sparse-family witness
that does not actually witness the necessity of hypothesis (N0) — only a *tower* family
does); V1's uniform shift bound did not follow from the display it cited (true, but only
via the closed form); V4's B₁ was a lattice-only supremum applied to a continuum
quantity; and V2's abstract still carried the refuted δ_∞ framing. All 13 repaired,
all verified present, all five documents compile clean (V1 13pp, V2 17pp, V3 16pp,
V4 10pp, scoping 10pp; 0 errors, 0 undefined refs, 0 overfulls). Severity across the
three rounds: breaking 0→1→0, moderate 5→(7 defective repairs)→0. **The mathematical
content of gate (II.11) and of the full-sequence identified fixed-coarse theorem stands
as written.** **Round 4 (12 Aug 2026)** audited those 13 repairs (three per-file auditors plus a
cross-cutting auditor covering truncation-family consistency, the full citation digraph,
a δ_∞ sweep, ledger truth and every quoted numeric value): **26 verdicts — 19 SOUND,
7 INCOMPLETE, 0 WRONG** — plus 21 new findings, all minor. First round in which no
repair was mathematically wrong; every INCOMPLETE was a citation, register or
statement-vs-proof mismatch. Notable: V4's B₁ cited V3 Lemma 6.1(iv) for the continuum
member when that lemma covers only the truncated family (fixed upstream by extending the
lemma); V1 Theorem 5.4's statement had not been updated to its own repaired proof
(‖H_p‖_∞ ≤ ½‖p‖, no t₀ or m dependence); the round-3 V1 repair had created an unrecorded
V1→V2 citation edge (removed by making the derivation self-contained); V3's
(N0)-necessity remark was wrong in three further ways (witnesses outside Γ_∞, a lossy
ρ_b arguing the wrong direction, and claiming divergence of the integral where only the
proof's bound diverges); and the Γ_N-vs-symmetric-band one-mode asymmetry that round 3
fixed in V2 §5 still survived in §4. All repaired; 19/19 presence check; all five
documents compile clean (V1 13pp, V2 17pp, V3 16pp, V4 11pp, scoping 10pp).
Convergence: breaking 0→1→0→0, moderate 5→7→0→0. **Gate (II.11) and the full-sequence
identified fixed-coarse theorem stand as written**, with no breaking or moderate finding
outstanding and the end-to-end chain trace clean. Remaining residues: the round-4
repairs are unaudited (a round 5 would be optional rather than load-bearing, given two
consecutive all-minor rounds); the η symbol collision (coupling-space field vs the D4
exponent 2−log₂3) is a known notational defect deliberately left for a by-hand fix; and
Part I's audit item C5 (a second human reader for the GJS page images) is the
programme's one user-level external residue. See strategy.md.


The original finest-scale local-state-norm target is false, already for the free massive
MMST lattice field.  The replacement theorem is a fixed-torus, fixed-coarse projective
statement: an interacting cluster state exists along a cofinal subnet, while the free
full sequence converges with an explicit power rate.  Identification of the interacting
cluster state with the continuum \(P(\phi)_2\) vacuum remains open.

## Files

- `lamport_part_ii_quadratic_obstruction.tex`: Lamport-form proof, exact free estimates,
  source-scope audit, claim ledger, and corrected dependency order.
- `lamport_part_ii_model_sheet.tex`: exact torus/lattice/CCR conventions, \(D4\) map,
  nearest-neighbour Hamiltonian, Wick convention, and closed-form construction of the
  finite-scale interacting ground states.
- `lamport_part_ii_projective_compactness.tex`: cofinal-subnet compactness theorem,
  construction of the projective state, symmetry inheritance, and counterexamples to
  stronger formal conclusions.
- `lamport_part_ii_free_fixed_coarse_rate.tex`: explicit covariance-symbol proof of
  \[
    |\omega_{M+r,L}^{(0)}\circ\alpha_M^{M+r}(W_M(\xi))
      -\omega_L^{(0)}\circ\beta_M(W_M(\xi))|
    \le (C_Q/4)2^{-\theta r},
  \]
  with \(\theta=2\eta/(5+\eta)\) and
  \(\eta=2(1-\log_2\sqrt3)\).
- `lamport_part_ii_weyl_reduction.tex`: proof that convergence on every fixed coarse
  Weyl generator implies convergence on the whole coarse algebra, projective consistency,
  and continuum identification; it also proves the precise failure of the cited
  anharmonic Lieb--Robinson hypothesis for the Wick quartic.
- `citation_screenshot_dossier_part_ii.tex`: page images for every source result used in the
  source-scope audit, with explicit positive and negative scope statements.
- `m2_ii_checkpoint.py`: reproducible finite-torus evaluation of the analytically derived
  quadratic forms, group velocity, and Wick asymptotic.
- `m2_ii_checkpoint.out`: checked output from the project virtual environment.
- `free_rate_checkpoint.py`: sampled arithmetic and normalization checks for the analytic
  \(D4\) filter envelope, filter tail, and dispersion inequalities.
- `evidence/`: page images rendered directly from the PDFs in `../refs/part_ii/`.

## Reproduction

From the repository root:

```sh
python3 part_ii/m2_ii_checkpoint.py
python3 part_ii/free_rate_checkpoint.py
```

The scripts require NumPy; the first also requires SciPy.  Their assertions check only
finite-scale consistency; the proof does not use numerical convergence as a substitute
for the analytic limits.

## Mathematical status

- Finest-scale diagonal norm convergence: **disproved**.
- Exact finite-torus interacting model and ground state: **constructed**.
- Interacting fixed-coarse projective cluster state along a cofinal subnet:
  **proved unconditionally**.
- MMST free fixed-coarse/projective convergence: **proved in the cited source and
  strengthened here to an explicit \(D4\) power rate**.
- Exact free gap, group-velocity bound, and Wick logarithm: **proved in the Lamport note**.
- Battle--Federbush as a source for the required OAR-uniform CE1/CE2: **not available**;
  the cited note treats different phase-cell variables and does not state those estimates.
- Full-sequence interacting convergence and identification with the continuum
  \(P(\phi)_2\) state: **open exactly at the coarse Weyl characteristic-functional limit**.
- Interacting scale-uniform gap, local second moment, and Lieb--Robinson estimate: **open**.
- The cited Nachtergaele--Raz--Schlein--Sims theorem: **inapplicable to the Wick quartic
  because it assumes \(V'\in L^1(\mathbb R)\)**.
- Former path `(1-s)H_N+sH`: **undefined without a common Hilbert-space/form realization**;
  it has been removed from the corrected program.

## Adversarial audit status (Part II, gate II.11)

Eight session-rounds ran over `v1`-`v4` and `gate_II11_scoping` (13 Aug: rounds 1-4
repair-audits; rounds 5-7 re-derivations that found and fixed the defective coupling, the
Nyquist zero, and the small-t threading), followed by the **independent fresh audit of
16 Aug 2026** (`../fresh_audit_2026_08_16/`, `../repair_2026_08_16/`): a full Lamport
reconstruction of Parts I+II, a severity-ranked critical audit (8 findings, one CRITICAL:
V2 section 6 judged not derived and rebuilt with an exact Fourier partition), a citation
dossier with page images, and a post-repair audit that found and repaired two further
proof-breaking defects (the complex asymmetric mixed surrogate, now Re(.); the invalid
lambda=0 compactness argument, now a free-form Hermite-tail proof). The two instruments
cross-validated: the fresh audit caught a false edge-sector claim written by the session
rounds hours earlier (four edge momenta CAN conserve; Delta_4e = O(t eps^5)), and the
session rounds' amended coupling, exact second chaos, and standing hypotheses all
survived its re-derivation verbatim.

**Verification of 25 Aug 2026:** frozen SHA-256 hashes match the sources; all 13
load-bearing round-5-7 items present; 109/109 by-number cross-document citations
resolve; independent numerics reproduce the edge enumeration {0:489,1:288,2:108,3:0,4:6},
the cyclic-covariance inverse (5.2e-16), the complex-surrogate witness, and
Delta_4e/eps^5 = const; all five documents compile clean (V1 14pp, V2 24pp, V3 21pp,
V4 14pp, scoping 11pp). V1 Remark 5.5 gained a one-sentence normalization clarification
(canonical modes carry c_omega; verified against the diagonalized chain to 4e-14) —
the only post-freeze edit.

**Status:** V4's ledger records (II.11) closed and the independent adversarial pass
complete; Part II's fixed-coarse program is complete at the stated import scope and
under the standing parameter hypotheses (t >= t_0 with t_0 L >= 1 where the convolution
bounds are consumed; eps_M in A5's constant; omega^ct defined by the constructed K_L).

**Open residues (explicit, none a hidden gap):** the eta symbol collision (V2/V4,
by-hand rename); Part I is conditional on the U_GJS interface (stated on its title page)
with item C5 (second human reader for the GJS page images) outstanding.
