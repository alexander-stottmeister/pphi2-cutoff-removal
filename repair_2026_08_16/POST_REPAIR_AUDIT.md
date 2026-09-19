# Post-repair audit of Parts I and II

Date: 16 August 2026

## Verdict

The repair strategy in `REPAIR_STRATEGY.md` has been executed in the canonical
documents.  A new audit of the repaired formulas found two additional
proof-breaking defects—the complex asymmetric mixed surrogate in V2 and the
invalid interaction-coercivity compactness argument at `lambda = 0` in V3—and
repaired both.  The subsequent algebraic, analytic, source-scope, propagation,
and build checks found no further proof-breaking defect in the repaired chain.

The scope qualification in Part I is essential: its Main Theorem is conditional
on the exact slab-family hypothesis `U_GJS` and the other enumerated imports.
The source dossier supports `U_GJS`, but does not silently turn that hypothesis
into a newly proved cluster-expansion theorem.  Part II retains its standing
thermal restriction `t >= t_0` and `t_0 L >= 1` wherever the convolution bounds
are consumed.

## Audit basis

The fresh pre-repair reconstruction and source evidence are:

- `fresh_audit_2026_08_16/lamport_reconstruction_parts_i_ii.pdf`: full
  hierarchical Lamport reconstruction;
- `fresh_audit_2026_08_16/critical_audit_parts_i_ii.pdf`: independent critical
  report;
- `fresh_audit_2026_08_16/citation_evidence_dossier.pdf`: every consumed printed
  result paired with page screenshots;
- `fresh_audit_2026_08_16/evidence/`: the individual rendered source pages;
- `fresh_audit_2026_08_16/ledgers/`: claim, dependency, citation, source, and
  finding ledgers.

No new external theorem was introduced by the repair.  Consequently the
existing downloaded-source cross-check and screenshot dossier remain the
complete citation evidence for the canonical chain.

## Part I

### 1. Exact logical scope

The only CE1 uniformity used in the slab transfers is now the displayed
hypothesis

```text
CE_slab = { 1_[-T,T] tensor g : T > 0, g in C_H },
| integral Q dq_{h_{T,g}} | <= C_8 ||Q||_GJS.
```

Every CE1 application in the moment and gap proofs has measure
`dq_{h_{T,g}}`; an affine path replaces `g` by `g_s`, and the cutoff-class
lemma proves `g_s in C_H`.  Thus the proof consumes no larger unspoken cutoff
class.  The title page, abstract, introduction, Main Theorem, and Appendix C
all state that this interface is `U_GJS`, not a theorem independently proved
in the manuscript.

### 2. CE2 localization

For the cylinder polynomial used in the gap proof, the repaired argument first
writes the finite source localization

```text
Q = sum_{a in A} Q_a,
||Q||_GJS = sum_a ||Q_a||_GJS.
```

Compact kernel support and finite polynomial degree make `A` finite.  Therefore

```text
Cov(Q(-t/2), Q(t/2))
  = sum_{a,b} Cov(Q_a(-t/2), Q_b(t/2)).
```

For `t > 2`, the open strip of width `t - 2` separates every localized pair.
Applying CE2 to each pair and summing gives exactly

```text
|Cov(Q(-t/2), Q(t/2))|
 <= C_7 exp[-m_1(t-2)] (sum_a ||Q_a||_GJS)^2
 = C_7 exp(2m_1) exp(-m_1 t) ||Q||_GJS^2.
```

No localized theorem is applied directly to the unlocalized sum.

### 3. Closed-graph passages

The repaired two-point argument uses a bounded family
`u_T = Q psi_{T-t/2}/||psi_T||`.  Every subnet has a weakly convergent
further subnet.  Since the scalar norm ratio tends to one,
`Q hat(psi)_{T-t/2}` has the same weak limit.  The graph of the closed
multiplication operator `Q` is a closed linear subspace of `H x H`, hence
weakly closed.  Strong convergence of the first graph coordinate then forces
the weak limit to be `Q Omega_g`.  Weak lower semicontinuity after applying
`exp(-tH(g)/2)` gives the required inequality.  The moment-transfer lemma now
writes the same graph argument rather than saying it applies “verbatim.”

### 4. Ultraviolet mollifier

The appendix fixes a nonnegative even `C_c^infinity(R^2)` function of unit
integral, supported in the unit ball, and defines
`delta_kappa(z) = kappa^2 delta(kappa z)`.  Positivity, averaging radius,
two-dimensional scaling, and the radius of a double convolution are therefore
all explicit before they are used.

## Part II: V2

### 1. Nyquist-edge enumeration

Let `R_N = pi/eps_N`.  In the symmetric band the edge momenta are `+R_N`
and `-R_N`, each with weight `2^(-1/2)`.

- Three edge momenta have sum `+/- R_N` or `+/- 3R_N`; a fourth non-edge
  input cannot cancel that sum.
- Four edge momenta can conserve: exactly two are positive and two negative.
  There are `binom(4,2) = 6` orders and their common weight is
  `(2^(-1/2))^4 = 1/4`, giving the factor `6/4 = 3/2`.

With `f(k_0) = c_cross(k_0,R_N)`, `A = sum f`, and `B = sum f^2`,

```text
A <= (t eps_N/4) coth(2t_0),
B <= gamma_e^(-2) A <= (t eps_N^3/16) coth(2t_0),
sum_{k01+...+k04=0} product_i f(k0i)
  = ||f*f||_2^2
  <= ||f*f||_infinity ||f*f||_1
  <= B A^2.
```

Multiplication by `4!(2Lt)^(-2)(3/2)` yields

```text
Delta_4e <= [9t/(256L^2)] coth(2t_0)^3 eps_N^5.
```

The canonical fourth-moment lemma no longer displays the false equality between
the true cross moment and the asymmetric `D_N` sum.  It defines that sum as a
surrogate and states the exact identity

```text
E[X_4 Y_4] = S_cross,N^D + E_N^edge.
```

### 2. Real part of the asymmetric surrogate

The translation-invariant surrogate uses the half-open band `D_N`, which
contains the negative Nyquist edge but not the positive edge.  It therefore
need not be real.  A one-chaos counterexample is immediate: take a real lattice
coefficient equal to one at the self-conjugate lattice edge and a real continuum
field whose negative-edge coefficient is `i` and positive-edge coefficient is
`-i`.  The asymmetric mixed sum is `i`.

The repaired proof consequently defines

```text
Q_cross,j = Re <G_N,j, C_cross^j G_infinity,j>.
```

If `Z_cross,j` denotes the complex Fourier sum, the exact formulas are

```text
Q_cross,j = Re Z_cross,j,
P_N,j = Q_cross,j^true - Q_cross,j
      = Re <G_N,j, [(C_cross+R_N)^j-C_cross^j] G_infinity,j>.
```

The physical-edge sup-norm bound remains valid because taking a real part cannot
increase absolute value.

### 3. Exact shifted partition

The lattice multiplier is folded modulo `2R_N`; the mixed and continuum
multipliers retain their exact output.  Extending `b_N` by zero and setting
`delta b = b_N-b_infinity`, direct expansion gives

```text
Q_N - 2 Q_cross + Q_infinity
 = <delta b, K_infinity delta b>
 + <b_N,(K_N^fold-K_infinity)b_N>
 - 2 Re <b_N,(K_cross-K_infinity)b_infinity,B_N>
 - 2 Re A_cross,j.
```

Here `A_cross,j` is the displayed finite sum over every nonzero exact output
`q = p + 2nR_N`.  The identity precedes all estimates; there is no unnamed
remainder.

### 4. Missing-input estimate for `j = 3`

The formerly compressed step is now derived.  Temporal summation and Tonelli
give

```text
sum_{q_0} F_2(q_0,d)
 <= C t^2 sum_k [gamma(k) gamma(d-k)]^(-1)
 <= C t^2 L [1+log(2+|d|/m)]/gamma(d).
```

The last spatial convolution is proved by the three regions
`|k| <= |d|/2`, `|d-k| <= |d|/2`, and their complement.  Inserting this
into the missing-input sum and splitting
`R_N <= |u| <= 2R_N` from `|u| > 2R_N` gives respectively
`C R_N^(-2) log_N^2` and `C R_N^(-2) log_N`; hence the normalized result is
`C eps_N^2 log_N^2`.

## Part II: V3

### 1. Periodic cutoff tails

The second-chaos tail is obtained from

```text
sum_{k_0}(A^2+k_0^2)^(-2) <= A^(-4) + t/(4A^3)
```

and the spatial tails `sum_{|k|>K} A^(-3) = O(LK^(-2))` and
`sum A^(-4) = O(LK^(-3))`.  For fourth chaos, selecting one high input and
using the displayed `F_3` convolution bound gives
`O((1+t)K^(-2)log^2(1+K/m))` for the squared norm.  The thermal/vacuum Wick
coefficient tail is exponentially small.  Exact recombination then yields the
increment `C log(1+K/m)(K/m)^(-1)`, which is the required Nelson input.

### 2. Compactness for every `lambda >= 0`

Interaction coercivity cannot prove compactness when `lambda = 0`.  The repaired
proof instead uses `W >= -b_K` and the shifted form

```text
q_K >= q_0,K + ||psi||_2^2.
```

In the finite Hermite basis,

```text
q_0,K(psi)
 = sum_n (sum_j gamma_j n_j) |<H_n,psi>|^2.
```

Thus a form-bounded set has coefficient tail at most `R/A` outside
`sum_j gamma_j n_j <= A`; the latter set of multi-indices is finite.  The form
embedding is compact without any assumption that the interaction tends to
infinity.

### 3. Finite cyclic Gaussian covariance

For mesh `delta=t/n` and `r=exp(-delta gamma)`, the normalized cyclic Mehler
chain has precision

```text
A_n = (1-r^2)^(-1)[(1+r^2)I-r(S+S*)].
```

The proposed covariance

```text
C_d = (r^d+r^(n-d))/(1-r^n)
```

satisfies the homogeneous recurrence away from `d=0` and
`(1+r^2)C_0-2rC_1=1-r^2`; hence it is exactly `A_n^(-1)`.  This gives the
periodic covariance and its Mittag-Leffler Fourier series with no informal
transplant.

### 4. Weyl mean shift and action

The Schrödinger Weyl action is derived from the central BCH commutator:

```text
(W(alpha,beta)psi)(q)
 = exp(i alpha q+i alpha beta/2) psi(q+beta).
```

Writing `q_s=eta_s+H_s`, with periodic `eta`, `H_0=-beta/2`, and
`H_t=beta/2`, cancels the half-phase exactly.  The mesh cross terms cancel
node by node because `-H''+gamma^2H=0` and `H'(t)=H'(0)`.  Spatial Parseval
produces the factor `1/(4L)`, and integration by parts gives

```text
(1/(4L)) integral_0^t (|H'|^2+gamma^2|H|^2)
 = gamma coth(t gamma/2)|b|^2/(8L).
```

This is the action printed in V1, V3, and V4.

### 5. Trace passage and simplicity

Trace convergence is not inferred from strong convergence.  The diagonal kernels
obey `0 <= K_R(t;x,x) <= exp(tb_K) M_t(x,x)`, and the dominating diagonal has
integral `Z_0,<=K(t)`.  Symmetry plus the semigroup identity gives
`integral K_R(t;x,x) = ||exp[-t(H_0+W_R)/2]||_2^2`, hence the trace.  Dominated
convergence applies to the Trotter mesh and then to `R -> infinity`.

Both finite- and infinite-mode simplicity proofs now include the missing strict
step.  If `u>0` is a top eigenvector and an orthogonal real top eigenvector `h`
existed, both `h_+` and `h_-` would be nonzero.  Positivity improvement gives

```text
r|h| = |T h_+ - T h_-| < T h_+ + T h_- = T|h|
```

almost everywhere.  Pairing with `u` and using self-adjointness gives the strict
contradiction `r<u,|h|> < <Tu,|h|> = r<u,|h|>`.

## Downstream propagation

- `v4_assembly.tex` cites the repaired edge identity, real surrogate, folded and
  exact-output multipliers, explicit alias term, and separate physical edge.
- `gate_II11_scoping.tex` records the executed coupling and the exact principal,
  alias, four-edge, and shifted partitions.
- The V4 acceptance ledger no longer says the adversarial pass is incomplete.
- The Part I and Part II README files carry repair addenda that supersede stale
  historical closure claims.

## Independent finite checks

These checks are verification only; the proofs above are analytic.

- Spatial enumeration with band radius `r=5` found edge-sector tuple counts
  `{0:489, 1:288, 2:108, 3:0, 4:6}` and weighted four-edge excess `1.5`.
- For `n=11`, `gamma=1.7`, `t=2.3`, the maximum entrywise error in
  `A_n C-I` was `5.197e-16`.
- Numerical integration of the mode action at `b=1.2-0.7i`, `L=1.4`,
  `t=2.1`, `gamma=1.3` gave `0.255277136151`, versus the closed form
  `0.255277136147` (relative error `1.553e-11`).

## Build and regression gates

The final build gate was executed with two consecutive successful direct
`pdflatex` runs after the last substantive edit for:

- `part_i/main.tex`;
- `part_ii/v2_interaction_comparison.tex`;
- `part_ii/v3_continuum_package.tex`;
- `part_ii/v4_assembly.tex`;
- `part_ii/gate_II11_scoping.tex`.

The resulting PDFs have respectively 38, 24, 21, 14, and 11 pages.  Their final
logs contain no undefined reference, undefined citation, LaTeX error, or fatal
error.  Literal regression searches find no live false claim that all
three-or-more edge sectors are impossible, no live unnamed `R_tail`, and no
load-bearing “same count” or unexplained finite-mode transplant.  Historical
erratum sentences that explicitly say a former term was deleted are not live proof
steps.  The final canonical sources, PDFs, and three audit PDFs are frozen in
`FINAL_ARTIFACT_HASHES.txt` by SHA-256.  A full Ghostscript null-device parse of
all eight PDFs completed with exit status zero.

## Remaining external residue

There is one deliberately visible scope residue, not a hidden proof gap:
`U_GJS` has not been independently re-proved from the full GJS polymer expansion.
Therefore Part I is a rigorous conditional theorem, not an unconditional theorem
obtained by enlarging the printed citation through paraphrase.  No corresponding
open residue remains in the repaired Part II derivations beyond their explicitly
listed imports and standing parameter hypotheses.
