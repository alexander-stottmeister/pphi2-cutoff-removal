# Repair strategy for Parts I and II

Date: 16 August 2026

This file records the repair before the canonical manuscripts are changed.  It is
the controlling plan for the present pass; the earlier status claims in
`strategy.md` and the two README files are historical and are not acceptance
evidence for this repair.

## Baseline

SHA-256 values before this repair:

| file | SHA-256 |
|---|---|
| `part_i/main.tex` | `6c4432d321a19a44b16e523d4fc0bb1ff50e9ec5736f40a9c948150e30a5d2c0` |
| `part_ii/v2_interaction_comparison.tex` | `fb5df945167b8e402a57d1725d7e637f9a49feb72aa0e581ec26a4de65c9f8a5` |
| `part_ii/v3_continuum_package.tex` | `6a87298a91279c0f96e13af7f4c14877ec23fe31f7b97e38d30167db7e21784d` |
| `part_ii/v4_assembly.tex` | `42412aeb3781dddd8f43af5130e84091485c9b1d92eeab226f6c4836e9a85fb1` |
| `part_ii/gate_II11_scoping.tex` | `a0c627d1c4a6ee38b736b15971c802fe4dbabf123c24d5f891e6f89b86b07b11` |

The independent reconstruction and source dossier used to locate the defects are
in `fresh_audit_2026_08_16/`.  They are evidence, not substitutes for correcting
the canonical files.

## Mathematical repair invariant

Every load-bearing assertion must be in exactly one of these classes:

1. proved in the canonical document by a displayed derivation;
2. imported with a source, exact scope, and an explicit assumption label; or
3. labelled open/conditional and excluded from unconditional conclusions.

No unnamed remainder, implicit representative convention, appeal to “the same
count”, or “transplant” may carry a convergence theorem.

## Part I

1. Replace the claim that Appendix C independently proves the whole GJS cluster
   expansion with the exact interface actually consumed:
   \(U_{\mathrm{GJS}}\), the CE1 bound with one constant on the slab family
   \(h_{T,g}=\mathbf 1_{[-T,T]}\otimes g\).  GJS Theorem 1.1.8 and p. 629 are
   recorded as evidence for this interface, but not promoted into a stronger
   theorem by paraphrase.  The Main Theorem is conditional on
   \(U_{\mathrm{GJS}}\) and all other enumerated imports.
2. In the CE2-to-gap step, write the finite localization decomposition
   \(Q=\sum_aQ_a\), expand the connected covariance into the double sum, apply
   CE2 pairwise, and sum the source norms exactly.
3. Define the ultraviolet mollifier with every property used later:
   smoothness, compact support, positivity, evenness, unit integral, and the
   two-dimensional scaling.

## Part II, V2

1. Restore the four-edge sector.  Six arrangements have edge weight \(1/4\),
   hence the correction is
   \[
   \Delta_{4e}=4!(2Lt)^{-2}\frac32
   \sum_{k_{0,1}+\cdots+k_{0,4}=0}\prod_i
   \widehat c_\times(k_{0,i},\pi/\varepsilon_N).
   \]
   Derive its explicit \(O(tL^{-2}\varepsilon_N^5)\) bound.
2. Replace the shifted comparison's ambiguous covariance powers and
   `R_tail` with normalized symbols.  The lattice symbol is folded modulo the
   band, the mixed and continuum symbols use exact outputs, and every mixed
   alias output is represented by a displayed term \(A_{\times,j}\).
3. Prove separately: uniform symbol bounds, fundamental-band multiplier
   differences, high-output decay, coefficient convolution telescopes,
   alias/missing-mode coefficient tails, and the physical Nyquist-edge
   remainder.  Only then take square roots and assemble the Wick-binomial sum.
4. Correct every constant declaration that silently uses \(t\ge t_0\) or
   \(t_0L\ge1\).

## Part II, V3 and downstream assembly

1. Replace “same envelope tail counts” by the complete periodic quartic and
   quadratic tail sums, including normalization and the thermal/vacuum Wick
   constant difference.
2. Expand the finite-mode “transplant” at its two load-bearing points: the
   weighted Gaussian coordinate unitary and the normalized Mehler/FKN trace
   kernel.  Earlier proved finite-dimensional lemmas may be invoked only after
   the identification and all constants are written.
3. Amend V4 and the gate document so A6 cites the repaired V2 result and no
   superseded false assertion remains part of the dependency chain.

## Acceptance gates

1. Every modified TeX file compiles to a PDF with no undefined references or
   undefined citations.
2. Literal regression searches find no live occurrence of the false
   “four edges impossible” claim, no live `R_tail`, and no load-bearing “same
   envelope tail counts” or unexplained “transplant”.
3. The repaired shifted proof has an exact algebraic partition before any
   estimate is applied.
4. The Part I title page, abstract, import ledger, theorem statement, and
   Appendix C agree on the conditional scope of \(U_{\mathrm{GJS}}\).
5. A fresh post-repair audit starts from the canonical files, checks all
   altered formulas independently, and records any remaining proof-breaking
   issue.  The repair is not complete merely because LaTeX compiles.

## Execution outcome

All scheduled repairs were applied.  The post-repair audit then found and fixed
two further breaking issues:

1. the half-open-band mixed Fourier surrogate in V2 can be complex at the
   Nyquist edge, so the exact scalar decomposition must use its real part;
2. V3's interaction-coercivity compactness argument does not cover
   `lambda = 0`, so compactness must be proved from the finite free Hermite
   spectrum and the form inequality `q_K >= q_0,K + ||.||^2`.

It also expanded the `j = 3` missing-input sum, the cyclic Gaussian covariance,
the Weyl BCH/endpoint shift, the Cameron--Martin normalization, the diagonal
trace limit, and both positivity-improving simplicity arguments.  V4, the gate,
and both README status headers now consume the repaired statements.  The full
verification record is `POST_REPAIR_AUDIT.md`.
