---
title: Notation
---

# Notation

The frozen notation table of the manuscript (§2.3). Every symbol imported from a frozen
source is converted to this notation at transcription time; the conversion log is in
[`part_i/README.md`](../part_i/README.md).

| symbol | meaning / convention |
|---|---|
| P, 2p′ | interaction polynomial; deg P = 2p′, a_{2p′} > 0, p′ ≥ 1 |
| ⟨·,·⟩ | inner product, conjugate-linear in the **first** argument |
| C, μ | time-zero covariance C = (2μ)⁻¹, μ = (−∂ₓ² + m₀²)^{1/2} |
| C_E, C_H, G | the cutoff classes of [Definition 2.1](definitions.md), in the roles fixed there |
| K(g), E(g), H(g), Ω_g, ω_g, β^g | cutoff Hamiltonian data (§2.1) |
| α, τ_a, U_a | patched dynamics (A6); space translations and their Q-space unitaries |
| Θ, θ | parity unitary Θ = Γ(−1); parity automorphism θ = Ad Θ |
| K₁, K₂, C₇, C₈, m₁ | GJS constants (A8); normalization K₂ ≥ 1 |
| ‖·‖_GJS | the printed observable norm (1.1.7)–(1.1.9) of [GJS] |
| N_I | number of unit cells [j, j+1) meeting the interval I in positive measure |
| M | the uniform local moment constant of (M₂), §5 |
| γ vs. m₁ | γ is the abstract gap parameter in §§8–10; instantiated as γ = m₁ in §11 |
| `\mathfrak m` | total-variation bound in the spectral-separation lemma, §9 |
| h_{T,g}, ψ_s, ψ̂_s, c_g | slab objects (A2; §4) |
| Ψ_γ | the rate function of the one-path estimate, §10 |
| d₀ | the LPPL threshold d₀ = 4 + 2/γ |

Two deliberate renamings relative to the frozen sources: the separation-lemma variation
bound is `\mathfrak m` — it was M₀ in `lamport_gap_to_main.tex`, colliding with the moment constant
M — and Θ = Γ(−1) is reserved for the parity unitary throughout.

## Constants

The constants appendix (Appendix A, p. 33) fixes every value against its defining
display; each row was re-verified by hand at gates G3a and G3b. The two that drive the
figures are

```latex
d_0 = 4 + 2/\gamma,
\qquad
\Psi_\gamma(d) = 32M\sum_{n\ge\lfloor d\rfloor}
   \Bigl(\|W_\gamma\|_1 e^{-\gamma n/4} + T_\gamma(n/2)\Bigr) ,
```

with Ψ_γ(d) ≤ C_{N,γ,M}(1+d)^{−N} for every N ≥ 1.
