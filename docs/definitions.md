---
title: Definitions
---

# Definitions

The objects the statements quantify over. Exact LaTeX for every numbered definition is
in the [result inventory](results.md); this page is the orientation.

## The model (§2.1)

ℋ = L²(S′(ℝ), dφ₀) is Q-space over the time-zero free field of mass m₀ > 0, with dφ₀
Gaussian of covariance C = (2μ)⁻¹, μ = (−∂ₓ² + m₀²)^{1/2}. Weyl operators
W(f,h) = exp i(φ₀(f) + π₀(h)) generate the local net

```latex
\mathfrak A(O)=\{W(f,h):f,h\in C_c^\infty(O)\ \text{real}\}'' ,
\qquad
\mathfrak A=\overline{\textstyle\bigcup_O \mathfrak A(O)}^{\,\|\cdot\|} ,
```

with O ranging over bounded open intervals. For P(ξ) = Σ_{n≤2p′} a_n ξⁿ with a_{2p′} > 0
and p′ ≥ 1, and real compactly supported h ∈ L¹ ∩ L²,

```latex
V(h):=\lambda\int h(x)\,{:}\mathscr P(\varphi_0(x)){:}_C\,dx ,
```

a self-adjoint multiplication operator affiliated with A(U) for every bounded open
U ⊇ supp h, and finitely additive on common domains. For a cutoff g,

```latex
K(g):=H_0+V(g),\quad E(g):=\inf\operatorname{spec}K(g),\quad H(g):=K(g)-E(g),
```

with normalized ground state Ω_g (A1), ω_g := ⟨Ω_g, · Ω_g⟩ and β^g_t = Ad e^{itH(g)}.

## The three cutoff classes (Definition 2.1)

```latex
\mathcal C_{\mathrm E}:=\{h:\mathbb R^2\to[0,1]\ \text{measurable},\ \operatorname{supp}h\ \text{compact}\}
```
the **Euclidean class**, the printed class of [GJS, p. 589];

```latex
\mathcal C_{\mathrm H}:=\{g:\mathbb R\to[0,1]\ \text{measurable},\ \operatorname{supp}g\ \text{compact}\}
```
the **Hamiltonian class**, the printed class of [GJS, (1.6), p. 588];

```latex
\mathcal G:=\{g\in C_c^\infty(\mathbb R):0\le g\le1,\ g\equiv1\ \text{on a nonempty open interval}\}
```
the **plateau net class**, directed by g ⪯ g′ ⟺ {g = 1}° ⊆ {g′ = 1}°.

The roles are fixed once and for all, and this division is what the whole argument is
organised around:

| class | what quantifies over it |
|---|---|
| C_E | the Euclidean estimates of A8 |
| C_H | the uniform moment (§5) and the uniform gap (§7) |
| G ⊂ C_H | the convergence theorem (§11, §12) |

For a bounded interval O and r ≥ 0,

```latex
O_0:=O,\qquad O_r:=\{x\in\mathbb R:\operatorname{dist}(x,O)<r\}\ (r>0),
\qquad d(g,O):=\operatorname{dist}\bigl(O,\mathbb R\setminus\{g=1\}^\circ\bigr).
```

O_r is the light cone of radius r around O, and d(g,O) is the distance from O to the
edge of the plateau — the quantity the rate is expressed in. Elementary memberships and
affine-path stability are Lemma 3.1.
