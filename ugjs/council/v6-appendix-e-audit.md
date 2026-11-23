# Appendix E of the record: third independent audit (auditor "e-audit", working council of 23 November 2026)

Record audited: `part_i/main.tex` at commit 49f2d23 (8744 lines), read from the frozen copy of that
commit. Appendix E is `app:freefield` (number E, p. 115 by `part_i/main.aux`), ll. 7977-8656.
Line numbers are those of 49f2d23; label numbers and pages come from `part_i/main.aux` of the same
commit; in `part_i/main.pdf` the printed page equals the PDF page index (PDF page 115 carries the
footer "115"). Source page images are cited by file name in `audit_2026/evidence/`.

The auditor wrote none of Appendix E. The earlier reports in `ugjs/council/` were opened only after
sections 1-3 and 2.1-2.7 below had been written; the comparison is section 2.8.

## 1. Outcome

All seven statements of Appendix E (Lemmas E.1, E.2, E.4 and E.7, Definition E.3, Proposition E.5,
Remark E.6) hold. I re-derived every step and found no false statement and no CRITICAL or MAJOR gap.
Every quotation that Appendix E relies on matches the printed page word for word. This covers the
quotations in Appendix E itself, in A1 items (a)-(g) except the pages listed under "Not verified",
and the free-field sentences of the Scope paragraphs of A1, A6 and A7 (Simon, Glimm-Jaffe II,
Glimm-Jaffe I). Three MINOR findings remain:

- an undeclared but harmless reading of Simon's (I.40) in E.7(b);
- strong continuity of a -> U_a, which the proof of Corollary 12.3 uses implicitly, is not stated;
- one sentence of Appendix B is over-inclusive.

The three passages that only one earlier auditor had seen since their last change also hold: Lemma E.1(ii)'s core argument, Lemma E.7(a)(2)'s comparison of closures, and Remark E.6.

## 2. Claims

Step types used below: [calc] an explicit calculation, redone by hand; [rec] an earlier numbered
result of the record, with its hypotheses checked; [ext] a printed statement of a source, read on
the page image in this session; [std] a standard theorem of analysis that the record uses as
background without a citation (Plancherel, Fourier inversion, Fubini, dominated convergence, Hoelder,
Stone, Hille-Yosida, the functional calculus).

### 2.1 Summary table

| statement | locator | what the proof does | verdict | status |
|---|---|---|---|---|
| E.1(i) | `lem:ff-onepart`, E.1, p. 115; ll. 8031-8033, proof ll. 8057-8075 | Shows that j_m f = mu_m^{-1/2} f^ is isometric on S_R by Plancherel and maps S_R onto S ∩ L²_r. That set is dense, by ♯-symmetrisation. The map extends, and j^C is complex-linear, isometric and onto. | holds | proved |
| E.1(ii) | ll. 8034-8041, proof ll. 8077-8096 | Computes the Fourier transforms of mu f and tau_a f, so tau_a is orthogonal. Multiplication by mu on L²_r is closed, symmetric, at least m and onto, hence self-adjoint. S ∩ L²_r is a core (truncation plus even mollifier). The result is transported by j. | holds | proved |
| E.1(iii) | ll. 8042-8052, proof ll. 8098-8114 | Shows (d_s f)^(k) = f^(sk) and mu_m(sk) = s mu_{m'}(k), giving the isometry. Identities for j, mu, tau and u_s are computed on the Fourier side. | holds | proved |
| Fock-space paragraph | ll. 8117-8142 (p. 117) | Shows A*(v) is bounded from F_n to F_{n+1}, A(v) := A*(v)* restricted to F_fin is well defined, and R_v is symmetric with closure phi_F(v). Identifies these with Simon (I.28)-(I.29). | holds | proved (definitions; quotation verified) |
| E.2(i)-(iv) | `lem:ff-gamma`, E.2, p. 117; ll. 8144-8194 | u^{⊗n} commutes with S_n. The intertwining of A* and A is proved via adjoints, phi_F by mapping graphs, and strong continuity by telescoping and dominated convergence. | holds | proved |
| E.3(a)-(d) | `def:ff-objects`, E.3, p. 118; ll. 8196-8227 | Definition. Its embedded claims (z^N = D Γ(z) D^{-1}; pi_0 self-adjoint; mu^C self-adjoint; e^{itH_0} a strongly continuous group, so H_0 exists by Stone) rest on Thm I.11(a),(c), E.1(ii) and E.2(iv). | holds | embedded claims proved, conditional on A1(e) (Thm I.11 as printed) |
| E.4(i) | `lem:ff-transport`, E.4, p. 118; ll. 8238-8239, proof 8258-8261 | Uses E.2(i) and Thm I.11(a),(c). | holds | proved, conditional on A1(e) |
| E.4(ii) | ll. 8240, 8263-8271 | Uses Simon's essential self-adjointness on F_F and Thm I.11(b), under both readings, then E.2(iii). | holds | proved, conditional on A1(e) |
| E.4(iii) | ll. 8241-8244, 8273-8294 | Induction on polynomial vectors and equality of mixed moments. Wick products are polynomials with coefficients fixed by the moments, under the declared formal-derivative reading of Simon p. 12. | holds | proved, conditional on A1(e) and the declared reading of A1(a) |
| E.4(iv) | ll. 8245-8246, 8296-8339 | Six steps: exponentials, then G in S(R^r) (Fourier), then bounded continuous G, then resolvents of polynomials, then real F in L² (density, a.e. subsequence), then positivity via F = (F^{1/2})². | holds | as E.4(iii) |
| E.4(v), (vi) | ll. 8247-8253, 8341-8348 | Uniqueness from density of polynomial vectors, then multiplicativity, then uniqueness of D via T = id. | holds | as E.4(iii) |
| E.5(T) | `prop:ff-symmetries`, E.5, p. 120; ll. 8354-8365, proof 8400-8438 | E.4 for T = tau_a; commutes with mu; supports shift; Ad maps generated von Neumann algebras; one-particle commutation for H_0; Wick powers by (W.1) and uniqueness in Γ_n; E.4(iv) for V(g). | holds | proved, conditional on A1(a),(c),(d),(e) as read (see 2.7) |
| E.5(P) | ll. 8366-8377, proof 8440-8454 | T = -1, so Θ = (-1)^N; uses the chaos parity; E.4(v) for the Q-space description. | holds | as E.5(T) |
| E.5(D) | ll. 8378-8395, proof 8456-8514 | E.4 for T = d_s; E.1(iii) for pi_0 and H_0; C_{m'}(sz) = C_m(z) from Lemma N.19's formula; (W.1) at both masses; lambda' = s^{-2} lambda. | holds | as E.5(T), plus Lemma N.19's formula (proved in the record) |
| E.6 | `rem:ff-A7`, E.6, p. 122; ll. 8517-8527 | Unitary transport of the domain D(H_0) ∩ D(V(g)) and of the closure, using E.5. | holds | proved, conditional on A1 (essential self-adjointness of K(g)) and E.5 |
| E.7(a)(1) | `lem:ff-sources`, E.7, p. 122; ll. 8538-8539, 8562-8563 | Thm I.11(a) and ΥΩ = Ω. | holds | proved, conditional on A1(e),(g) |
| E.7(a)(2) | ll. 8540-8549, proof 8565-8625 | Computes GJ2's forms from (1.2.10)-(1.2.11) (factor 2^{-1/2}). The closure from 𝔖 is phi_F(θ); 𝔇(N^{1/2}) ⊆ D(phi_F(θ)); GJ2's closures on 𝔇(N^{1/2}) are phi_F(θ); then conjugates by Υ and D. | holds | proved, conditional on A1(e),(g) as read (see 2.7) |
| E.7(a)(3) | ll. 8550-8552, 8627-8631 | Γ(e^{it mu(·)}) is a multiplication group, so its generator is the maximal multiplication by Σ mu(k_j). | holds | as E.7(a)(2) |
| E.7(a)(4) | ll. 8553-8554, 8633-8636 | Γ(e^{-ia·}) is multiplication by e^{-ia Σ k_j}, which is GJ2's U(-a) (3.6.2); Γ(-1) via E.5(P). | holds | as E.7(a)(2) |
| E.7(b) | ll. 8556-8557, proof 8638-8655 | Stone differentiation gives D^{-1} H_0 D ⊇ dΓ(mu). Example 3 makes the closure Z a semigroup generator, so Z + 1 is onto (Hille-Yosida); H_0 + 1 is injective; hence H_0 = Z. | holds | proved, conditional on A1(e),(f) under the reading of finding F1 |

### 2.2 Step-by-step record

**E.1(i)** (ll. 8031-8033; proof ll. 8057-8075).
1. [calc] For f, g in S_R, <j f, j g> = ∫ conj(f^) g^ mu^{-1} dk = <f, g>_m. This is the definition at l. 8009 with Plancherel for the unitary transform. holds.
2. [calc] For real f, f^(-k) = conj f^(k); mu is even; so j f lies in L²_r. holds.
3. [calc] mu^{±1/2} = (k² + m²)^{±1/4} is smooth with polynomially bounded derivatives (k² + m² ≥ m² > 0). Multiplication by it maps S into S, and onto, since the inverse factor does the same; it preserves the ♯-symmetry. Since the Fourier transform maps S_R onto S ∩ L²_r, j(S_R) = S ∩ L²_r. holds.
4. [calc] Density: ½(η_n + η_n^♯) lies in S ∩ L²_r and converges to ½(θ + θ^♯) = θ, because ♯ is isometric. holds.
5. [std] An isometry from a dense subspace onto a dense subspace of a complete space extends to an isometry onto. holds.
6. [calc] On L²_r the inner product is real: substitute k -> -k in conj<θ, θ'>. Hence ‖θ + iθ'‖² = ‖θ‖² + ‖θ'‖². I checked that j^C is complex-linear: j^C(i(v + iw)) = i j^C(v + iw). It is isometric. It is onto, because θ = ½(θ + θ^♯) + i·(2i)^{-1}(θ - θ^♯); I checked that (2i)^{-1}(θ - θ^♯) lies in L²_r. holds.

**E.1(ii)** (ll. 8034-8041; proof ll. 8077-8096).
1. [calc] (mu f)^ = mu f^. (tau_a f)^(k) = (2π)^{-1/2} ∫ e^{-ikx} f(x - a) dx = e^{-iak} f^(k). Both lie in S and are ♯-symmetric: (e^{-ia·} f^)^♯(k) = conj(e^{iak}) conj(f^(-k)) = e^{-iak} f^(k). So mu f and tau_a f lie in S_R. holds.
2. [calc] ‖tau_a f‖_m = ‖f‖_m and tau_a tau_{-a} = 1 on S_R, so tau_a extends to an orthogonal bijection with inverse tau_{-a}. holds.
3. [calc] tau_a mu f and mu tau_a f both have transform e^{-ia·} mu f^. holds.
4. [calc] j tau_a = e^{-ia·} j extends by continuity and by complex linearity. holds.
5. [calc] Let M be multiplication by mu on {θ ∈ L²_r : mu θ ∈ L²}. M maps into L²_r (mu is even and real); it is closed (a.e. subsequence), symmetric, ≥ m, and onto (mu^{-1} ≤ 1/m preserves L²_r). A symmetric operator that is onto is self-adjoint, also in a real Hilbert space: for y in D(M*) pick x with Mx = M*y; then y - x is orthogonal to Ran M = L²_r. holds.
6. [calc] Core. 1_{[-n,n]} θ lies in L²_r (the interval is symmetric) and converges in graph norm by dominated convergence. For an even real mollifier, (θ_n * ρ_ε)^♯ = θ_n * ρ_ε (checked); the convolution lies in C_c^∞ with support in [-n-1, n+1] for ε ≤ 1, where mu ≤ ((n+1)² + m²)^{1/2}. So L² convergence of the mollification gives graph-norm convergence. holds.
7. [calc] Transport by j. j^{-1} M j is self-adjoint with core j^{-1}(S ∩ L²_r) = S_R, on which it equals mu, since j(mu f) = mu j f. So it is the closure of mu restricted to S_R, and <f, j^{-1} M j f> = ∫ mu |j f|² ≥ m ‖f‖²_m. holds.

**E.1(iii)** (ll. 8042-8052; proof ll. 8098-8114).
1. [calc] (d_s f)^(k) = f^(sk) (substitute x = s y). mu_m(sk) = (s²k² + s²m'²)^{1/2} = s mu_{m'}(k). holds.
2. [calc] ‖d_s f‖²_{m'} = ∫|f^(sk)|² mu_{m'}(k)^{-1} dk. With q = sk this is ∫|f^(q)|² mu_{m'}(q/s)^{-1} s^{-1} dq, and mu_{m'}(q/s) = s^{-1} mu_m(q), so it equals ∫|f^(q)|² mu_m(q)^{-1} dq. holds. Corroborated numerically (check 2).
3. [calc] d_{1/s} d_s = 1 on S_R, so d_s is an orthogonal bijection K_m -> K_{m'}. holds.
4. [calc] (j_{m'} d_s f)(k) = mu_{m'}(k)^{-1/2} f^(sk) = s^{1/2} (s mu_{m'}(k))^{-1/2} f^(sk) = (u_s j_m f)(k). holds.
5. [calc] (e_s f)^(k) = s f^(sk). (d_s mu_m f)^(k) = mu_m(sk) f^(sk) = s mu_{m'}(k) f^(sk) = (mu_{m'} e_s f)^(k). holds. Corroborated numerically (check 4).
6. [calc] (d_s tau_a f)(x) = s^{-1} f(x/s - a) = s^{-1} f((x - sa)/s) = (tau_{sa} d_s f)(x). holds.
7. [calc] u_s is unitary. (u_s^{-1} θ)(k) = s^{-1/2} θ(k/s). u_s w(·) u_s^{-1} = w(s·), and e^{it mu_m(sk)} = e^{its mu_{m'}(k)}. holds.

Boundary: at s = 1, m = m' and u_1 = d_1 = e_1 = 1. At a = 0, tau_0 = 1.

**Fock-space paragraph** (ll. 8117-8142).
- [calc] ‖S_{n+1}(v ⊗ ψ)‖ ≤ ‖v‖ ‖ψ‖.
- [calc] For χ in F_{n+1}, <χ, A*(v)ψ> = <B*χ, ψ_n> with B = A*(v) restricted to F_n, which is bounded. So F_fin ⊆ D(A*(v)*), A(v) maps F_{n+1} into F_n, and A(v) annihilates F_0.
- [calc] R_v is symmetric on F_fin, hence closable.
- [ext] The identification with Simon (I.28)-(I.29) for v = f in K: the printed definitions agree (`simon-fock-045`, `simon-fock-046`), including "We emphasize that f ∈ H, not H_C, in (I.29)".

All hold.

**E.2** (ll. 8144-8194).
- (i) [calc] u^{⊗n} is unitary and commutes with permutations, hence with S_n. The group law and the inverse follow from (u'u)^{⊗n} = u'^{⊗n} u^{⊗n}, and u^{⊗0} = 1 gives Ω -> Ω.
- (ii) [calc] The first identity holds because u^{⊗(n+1)} S_{n+1} = S_{n+1} u^{⊗(n+1)}. For the second I re-ran the chain at ll. 8178-8179: it uses <A*(v)χ', ψ'> = <χ', A(v)ψ'> on F_fin, the first identity for u^{-1} and uv, and density of F_fin(h').
- (iii) [calc] Γ(u) ⊕ Γ(u) maps the graph of R_v restricted to F_fin(h) onto that of R_{uv} restricted to F_fin(h'), since Γ(u)F_fin(h) = F_fin(h'). A unitary maps closures to closures.
- (iv) [calc] Telescoping gives ‖u_t^{⊗n}(v_1 ⊗ … ⊗ v_n) - v_1 ⊗ … ⊗ v_n‖ ≤ Σ_j ‖u_t v_j - v_j‖ Π_{i≠j} ‖v_i‖. The operators have norm 1, so the convergence extends to all vectors. Dominated convergence applies to the series with dominant 4‖ψ_n‖². Continuity at t_0 follows from the group law.

All hold.

**E.3** (ll. 8196-8227).
- (a) [ext] Thm I.11(c), "DF_n = Γ_n" (`simon-fock-046`), with D unitary, gives L² = ⊕ Γ_n. Γ(z1) acts as z^n on F_n.
- (b) [rec] mu h lies in S_R (E.1(ii)). pi_0(h) is unitarily equivalent to a real multiplication operator, hence self-adjoint. pi_0(th) = t pi_0(h) because phi_0 is linear (a.e.; this follows from Simon's (c) on p. 15 by expanding E[(phi(av + bw) - a phi(v) - b phi(w))²] = 0).
- (c) [std] Functional calculus under unitary equivalence.
- (d) [rec + std] mu^C is self-adjoint and equals mu on S_R (E.1(ii)). e^{it mu^C} = (j^C)^{-1} e^{it mu(·)} j^C is strongly continuous. Then E.2(iv) applies, and Stone's theorem gives H_0.

All hold. "It is unique (Lemma E.4(vi))" (l. 8200) is a forward reference; E.4(i)-(v) are proved for an arbitrary choice of the unitaries of Thm I.11, so it is not circular.

**E.4** (ll. 8229-8349).
- (i) [ext + rec] T^C is unitary.
  - U_T 1 = D_2 Γ(T^C) Ω = D_2 Ω = 1 (Thm I.11(a)).
  - U_T Γ_n = Γ_n (Thm I.11(c) and E.2(i)).
  - Γ(T^C) Γ(z1) = Γ(zT^C) = Γ(z1) Γ(T^C).

  holds.
- (ii) [ext] "the φ(f) are essentially self-adjoint on F_F(H)" (`simon-fock-046`), so phi_F(f) is self-adjoint. Thm I.11(b) gives the conclusion under either reading:
  - strong reading: D_i phi_F(f) D_i^{-1} = phi_i(f) directly;
  - weak reading (an identity on D_i F_fin): D_i phi_F(f) D_i^{-1} ⊆ M_{phi_i(f)} by closedness, and A ⊆ B with both self-adjoint gives B = B* ⊆ A* = A.

  [rec] E.2(iii) with u = T^C. holds.
- (iii) [std] Products of Gaussian variables have all moments (Hoelder), so polynomial vectors lie in L² and in each D(M_{phi(f)}). [rec] (ii) gives U_T M_{phi_1(f)} p = M_{phi_2(Tf)} U_T p, and the induction starts at U_T 1 = 1. Mixed moments are preserved, since E[P(phi_1)] = <U_T 1, U_T P(phi_1)>.

  [ext, declared reading] Simon p. 12 (`simon-wickprod-034`) prints the recursion with "∂/∂f_i" undefined. Read as a formal partial derivative, :g_1⋯g_n: is fixed up to a constant by its partial derivatives, which by induction are the lower Wick products. These are compatible: ∂_j of :…ĝ_i…: and ∂_i of :…ĝ_j…: are both the product with g_i and g_j removed. The constant is fixed by <·> = 0. The coefficients are combinations of mixed moments. The same page's "WARNING! Not all algebraic relations are preserved by : :" (ff^{-1} = f^0 but :fg: ≠ :f^0:) supports reading the operation as one on formal expressions. holds, under that reading.
- (iv) holds: I re-ran every step.
  - Step 1 [std]: the functional calculus, and phi_i is linear.
  - Step 2 [std]: Fourier inversion G(x) = (2π)^{-r/2} ∫ G^(t) e^{it·x} dt, with G^ in L¹; Fubini applies with dominant |G^(t)| |χ'| |ψ'|.
  - Step 3 [calc]: G_n = (G e^{-|·|²/n}) * ρ_n lies in S, because derivatives fall on ρ_n and Gaussian decay survives; |G_n| ≤ sup|G|; G_n -> G pointwise by continuity.
  - Step 4 [calc]: (M_F - i)^{-1} = M_{(F-i)^{-1}}.
  - Step 5 [ext + rec]: Γ_n is the closed span of Wick monomials, which are polynomial vectors by (iii) (A1(c), `simon-gamman-038`), and L² = ⊕ Γ_n (E.3(a)). The proof then takes real parts, uses (iii), a common a.e. subsequence, dominated convergence of the bounded resolvents, and the fact that equal resolvents at i give equal self-adjoint operators.
  - Step 6 [calc]: U_T F = M_{U_T G} U_T G = (U_T G)² with G = F^{1/2}; then min{F, n} -> F in L².
- (v) [calc] The induction of (iii) uses only W1 = 1 and the field relation. Polynomial vectors are dense (Step 5). U_{T'} U_T has the two properties for T'T, and U_T^{-1} has them for T^{-1}. holds.
- (vi) [calc] W = D' D_1^{-1} satisfies W1 = 1 and W phi_1(f) W^{-1} = phi_1(f). By (v) with T = id, U_id = D_1 Γ(1) D_1^{-1} = 1. holds.

**E.5(T)** (ll. 8354-8365; proof ll. 8400-8438).
1. [rec] E.4(i),(ii) with K_1 = K_2 = K_m and T = tau_a, which is an orthogonal bijection by E.1(ii). holds.
2. [rec] U_a U_b = U_{a+b} by E.4(v), since (tau_a tau_b f)(x) = f(x - a - b). Hence U_0 = 1 and U_a* = U_{-a}; Lemma 2.8 uses the latter. holds.
3. [rec + calc] pi_0: U_a i^N = i^N U_a (E.4(i)); U_a phi_0(mu h) U_a* = phi_0(tau_a mu h) (E.4(ii)); tau_a mu h = mu tau_a h (E.1(ii)); tau_a h is real Schwartz. holds.
4. [std] W(f,0) and W(0,h): functional calculus. holds.
5. [calc] Local algebras. supp tau_a f = supp f + a, so tau_a is a bijection of the real C_c^∞(O) onto the real C_c^∞(O+a). Ad U maps (M ∪ M*)'' onto (UMU* ∪ UM*U*)''. The generating set is closed under adjoints: W(f,0)* = W(-f,0) and W(0,h)* = W(0,-h). Direction: Ad U_a moves supports by +a. holds.
6. [calc] A: O -> O + a is a bijection of the bounded open intervals, and tau_a is isometric. holds.
7. [rec] H_0: j^C tau_a^C (j^C)^{-1} = e^{-iak} commutes with e^{it mu(k)}. Then E.3(d) and E.2(i), and Stone's theorem identifies the generators. holds.
8. [ext + calc] Wick powers. For n = 0, U_a(∫g · 1) = ∫g = ∫tau_a g. For n ≥ 1, substitute x' = x + a: ∫(tau_a f_j)(x') C(x' - y') dx' = ∫f_j(x) C(x - (y' - a)) dx. The proof then applies (W.1) to g and to tau_a g (both real, L¹ ∩ L², compactly supported, hence in L^{1+ε}), E.4(iii) and unitarity. Both elements lie in Γ_n (A1(d), E.4(i)), and the tau_a f_j range over S_R. Uniqueness in Γ_n is the source's "the unique random variable in Γ_m(H)" (`simon-wickdef-158`). holds.
9. [rec] V(g) is real; E.4(iv) gives U_a M_{V(g)} U_a* = M_{V(tau_a g)}. holds.

Sign check: j tau_a = e^{-ia·} j, so U_a = 𝔇 U(-a) 𝔇^{-1} (E.7(a)(4)), where GJ2's (3.6.2) is U(α) = e^{+iα Σ k_j} (`gj2-cutoff-independence-38`). The same page prints "U(-α) φ(x) U(+α) = φ(x+α)", that is U(-a) φ(f) U(a) = φ(tau_a f), which matches U_a phi_0(f) U_a* = phi_0(tau_a f). It also prints U(-α) H(g) U(+α) = H(g') with g'(x) = g(x - α), which matches U_a K(g) U_a* = K(tau_a g).

Not stated: that a -> U_a is strongly continuous (finding F2).

**E.5(P)** (ll. 8366-8377; proof ll. 8440-8454).
1. [rec] U_{-1} = D Γ(-1) D^{-1} = (-1)^N (E.3(a) with z = -1); it is a self-adjoint unitary that fixes 1.
2. [rec] Θ phi_0(f) Θ = phi_0(-f) = -phi_0(f), by E.4(ii) and linearity.
3. [rec] Θ commutes with i^N (both are diagonal on ⊕ Γ_n), so Θ pi_0 Θ = -pi_0.
4. [calc] W, A(O) and A follow as in (T) with f -> -f.
5. [rec] -1 is central, so Γ(-1) commutes with Γ(e^{it mu^C}) (E.2(i)), and Θ H_0 Θ = H_0.
6. [ext + rec] Θ is (-1)^n on Γ_n (A1(d)), so Θ V(g) = V(g) for even P; then E.4(iv).
7. [rec] R ψ = ψ(-·) is unitary with R1 = 1 and R phi_0(f) R^{-1} = phi_0(-f), by the stated hypothesis. E.4(v) with T = -1 gives R = Θ.

All hold.

**E.5(D)** (ll. 8378-8395; proof ll. 8456-8514).
1. [rec] E.4(i),(ii) with T = d_s, which is an orthogonal bijection by E.1(iii). holds.
2. [rec + calc] pi_0: U_s i^N_{(m)} = i^N_{(m')} U_s (E.4(i)). U_s phi_0^{(m)}(mu_m h) U_s* = phi_0^{(m')}(d_s mu_m h) = phi_0^{(m')}(mu_{m'} e_s h) by E.1(iii). The CCR are preserved, since ∫(d_s f)(e_s h) = ∫ f h. holds.
3. [calc] supp d_s f = supp e_s f = s · supp f, so the generators of A^{(m)}(O) go to those of A^{(m')}(sO). holds.
4. [rec + calc] H_0: d_s^C e^{it mu_m^C} (d_s^C)^{-1} = (j_{m'}^C)^{-1} u_s e^{it mu_m(·)} u_s^{-1} j_{m'}^C = e^{its mu_{m'}^C}. So U_s e^{itH_0^{(m)}} U_s* = e^{itsH_0^{(m')}}, with generators U_s H_0^{(m)} U_s* and s H_0^{(m')}. holds.
5. [rec] U_a and Θ: E.4(v), with d_s tau_a = tau_{sa} d_s extended by continuity. holds.
6. [calc] n = 0: ∫g = s^{-1} ∫g(x/s) dx. holds.
7. [calc] C_{m'}(sz) = C_m(z) for z ≠ 0. In Lemma N.19's formula at mass m' (`aux:notation-kernel`, N.19, p. 69; l. 4966) substitute u = s²t: u^{-1} du = t^{-1} dt, u m'² = t m², s²z²/(4u) = z²/(4t). holds.

   Independent check via the Fourier side: with q = sk and mu_{m'}(q/s) = s^{-1} mu_m(q), the factor s^{-1} of dk cancels the factor s of mu. No power of s survives in one space dimension. Corroborated numerically (check 1).
8. [calc] Substituting x' = sx: ∫(d_s f)(x') C_{m'}(x' - sy) dx' = ∫f(x) C_{m'}(s(x - y)) dx = ∫f(x) C_m(x - y) dx. holds. Corroborated numerically (check 3).
9. [ext + calc] (W.1) at mass m for g, with E.4(iii) and unitarity; (W.1) at mass m' for g~ = s^{-1} e_s g, with y' = sy. The weight is s g~(sy) = g(y). Uniqueness in Γ_n(K_{m'}) then gives U_s :phi^n(g):_{C_m} = s^{-1} :phi^n(e_s g):_{C_{m'}}. holds.
10. [calc] Since s lambda' = s^{-1} lambda when lambda' = s^{-2} lambda, U_s V_{m,lambda}(g) = s V_{m',lambda'}(e_s g); then E.4(iv). holds.

Consistency checks:
- lambda/m² = lambda'/m'²: the dimensionless coupling is invariant.
- Remark 3.3 takes s = m_0/M_*, so m_0 = s M_* and lambda' = (M_*/m_0)² lambda = s^{-2} lambda, as E.5(D) requires.
- Proposition 3.2 reaches the same lambda' by the Euclidean substitution (ll. 1594, 1600).

Boundary: at s = 1, U_1 = U_id = 1 and lambda' = lambda.

**E.6** (ll. 8517-8527).
1. [rec, reading] A1 (l. 637) does not name the domain of the operator sum; E.6 takes D(H_0) ∩ D(V(g)). This is the standard meaning, and it is at most a weaker requirement: if A ⊆ B with B symmetric and A essentially self-adjoint, then closure(A) ⊆ closure(B) ⊆ B* ⊆ A* = closure(A). holds.
2. [rec] U_a maps D(H_0) onto itself and D(M_{V(g)}) onto D(M_{V(tau_a g)}) (E.5(T)). tau_a g lies in C_H, and unitary conjugation commutes with closure. holds.
3. [rec] Θ: the same argument for even P. holds.
4. [rec] Dilation: U_s(H_0 + V_{m,lambda}(g)) U_s* = s(H_0^{(m')} + V_{m',lambda'}(e_s g)) on the transported domain, and e_s g lies in C_H. Essential self-adjointness at (m', lambda') follows from this unitary equivalence. holds.

**E.7** (ll. 8529-8656).
- (a), (1). [rec] Υ is unitary (E.1(i), E.2(i)).

  [ext] GJ2 (1.2.1)-(1.2.3) and "||ψ||² = Σ||ψ_n||²" (`gj2-fock-04`) are the norm conventions of the record, so the factors n^{1/2} of GJ2's a(k) and of A(θ) agree.

  Thm I.11(a) and ΥΩ = Ω. holds.
- (2): every step holds.
  1. [calc] For symmetric ψ_n, √(n+1) S_{n+1}(θ ⊗ ψ_n) = (n+1)^{-1/2} Σ_j θ(k_j) ψ_n(…k̂_j…) (redone).
  2. [ext, reading] (1.2.7), read with the δ-integration, gives <χ, a*(k) ψ> = <a(k) χ, ψ>.
  3. [calc] ∫θ(k) a*(k) dk = A*(θ) and ∫θ(k) a(-k) dk = A(θ^♯), since A is conjugate-linear.
  4. [calc] The coefficient functions are Schwartz, Fubini applies, and ∫e^{-ikx} f = (2π)^{1/2} f^. The constant (4π)^{-1/2}(2π)^{1/2} = 2^{-1/2} (check 5).
  5. [calc] (j f)^♯ = j f for real f; θ' = mu^{1/2} h^ = j(mu h); i(A*(θ') - A(θ')) = A*(iθ') + A(iθ').
  6. [calc] The closure from 𝔖 is phi_F(θ): symmetric Schwartz functions are dense in F_n, and R_θ is bounded on ⊕_{n≤N} F_n.
  7. [calc] ‖R_θ ψ‖ ≤ √2 ‖θ‖ ‖(N+1)^{1/2} ψ‖ on F_fin, by orthogonality across n and ‖A(θ) restricted to F_n‖ ≤ √n ‖θ‖.
  8. [calc] 𝔇(N^{1/2}) ⊆ D(phi_F(θ)) by truncation and closedness. 𝔖 is N-norm dense in it. The form extends, the operator it defines is phi_F(θ) restricted to 𝔇(N^{1/2}), and its closure is phi_F(θ).

     [ext] The quotation "the bilinear forms φ(f) and π(g) define operators whose closures on 𝔇(N^{1/2}) are self-adjoint" matches `gj2-fields-05`.
  9. [rec + ext] Υ^{-1} phi_F(j f) Υ = phi_F(f) and Υ^{-1} phi_F(i j mu h) Υ = Γ(i1) phi_F(mu h) Γ(i1)^{-1} (E.2(iii)). Conjugation by D, with Thm I.11(b) under either reading (E.4(ii)) and E.3(a),(b), gives phi_0(f) and i^N phi_0(mu h) i^{-N} = pi_0(h).

  Sign of pi_0: from (1.2.10)-(1.2.11) the commutator of the braces is 2δ(k + k'), so [phi(x), pi(y)] = (i/4π) · 2 · 2π δ(x - y) = iδ(x - y). Hence [phi_0(f), pi_0(h)] = i ∫ f h on a common core, the standard sign. The record does not use this.
- (3) [rec + std] 𝔇^{-1} e^{itH_0} 𝔇 = Γ(e^{it mu(·)}) is multiplication by e^{it Σ mu(k_j)}. Its generator (Stone; direct sum over n) is the maximal multiplication by Σ mu(k_j). GJ2's (1.2.5) is read with its maximal domain, as declared. holds.
- (4) [rec + ext] 𝔇^{-1} U_a 𝔇 = Γ(e^{-ia·}), which is multiplication by e^{-ia Σ k_j} = U(-a) (3.6.2, printed with e^{+iα(k_1+⋯+k_j)}). 𝔇 Γ(-1) 𝔇^{-1} = D Γ(-1) D^{-1} = Θ, since Υ commutes with Γ(-1) (E.2(i)) and by E.5(P). holds.
- (b), every step holds.
  1. [ext] "We also drop "D" treating it as an identity" (`simon-fock-046`).
  2. [calc + std] For v_j in D(mu^C), t -> S_n(e^{it mu^C} v_1 ⊗ …) is differentiable at 0, by the product rule for the norm-one multilinear map (v_1, …, v_n) -> v_1 ⊗ … ⊗ v_n. Stone's theorem then puts these vectors in D(D^{-1} H_0 D) with the action (I.40). This rests on the reading in F1.
  3. [ext] Simon's mu is "the closure of the operator defined on S" (`simon-freefield-100`). [rec] By E.1(ii) it is j^{-1} mu(·) j, self-adjoint, ≥ m, and the restriction of mu^C.
  4. [calc] H_0 ⊇ Z, the closure of D dΓ(mu) D^{-1}.
  5. [ext] Example 3 (`simon-dgamma-054`) applies with A = mu positive self-adjoint on the real space K_m. Its convention is e^{-t dΓ(A)} = Γ(e^{-tA}), so Z is the generator in the e^{-tZ} sense. [std] Hille-Yosida (necessity half) gives that Z + 1 maps D(Z) onto L².
  6. [rec] H_0 ≥ 0 by (3), so H_0 + 1 is injective; with Z ⊆ H_0 this gives H_0 = Z.

### 2.3 Calculations redone by hand (list)

I redid each of the following:
- the isometry of j_m and of d_s;
- the transforms of tau_a f, d_s f and e_s f;
- mu_m(sk) = s mu_{m'}(k);
- j_{m'} d_s = u_s j_m and u_s w(·) u_s^{-1} = w(s·);
- d_s mu_m = mu_{m'} e_s and d_s tau_a = tau_{sa} d_s;
- C_{m'}(sz) = C_m(z), with no power of s in one space dimension;
- the smeared-kernel identity and the weight s g~(sy) = g(y);
- the factor s^{-1} of the Wick powers, including n = 0;
- lambda' = s^{-2} lambda and the factor s of V and of H_0;
- the sign e^{-iak} of j tau_a and its match with GJ2's U(-a);
- 2^{-1/2} = (4π)^{-1/2}(2π)^{1/2} in GJ2's smeared fields;
- θ^♯ for the a(-k) terms;
- i(A* - A) = A*(i·) + A(i·);
- the CCR sign of pi_0;
- the bound √2 ‖θ‖ ‖(N+1)^{1/2} ψ‖;
- the adjoint chain of E.2(ii);
- the telescoping estimate of E.2(iv);
- the six steps of E.4(iv);
- the Hille-Yosida step of E.7(b);
- the direction of every map of local algebras: tau_a(A(O)) = A(O+a), theta(A(O)) = A(O), Ad U_s(A^{(m)}(O)) = A^{(m')}(sO), and tau_{-a}(A(O)) = A(O-a) as used in Theorem 12.2(4).

Boundary cases re-run: s = 1; a = 0; n = 0 and n = 1 Wick powers (:phi^1(g): = phi_0(g), consistent with E.4(ii)); real versus complex test functions; f = 0.

On real versus complex test functions: pi_0, W(0,h) and A(O) are defined with real test functions only. E.7(a)(2) is stated for real f, h, as GJ2's "For real f(x), g(x)". The complex-linear extensions tau_a^C and d_s^C are used only on the one-particle space.

### 2.4 External claims used by Appendix E: quotation and hypotheses

Each quotation below was compared with the image word for word.

| printed statement | used in | image | quotation | hypotheses at the point of use |
|---|---|---|---|---|
| Simon, Definition p. 15, "(c) <φ(v)φ(w)> = ½<v,w>"; Theorem I.6 | E intro (realisations), A1 | `simon-gaussproc-037` | matches | real Hilbert space K_m; two processes indexed by the same space |
| Simon (I.28), (I.29a-c), p. 23-24 | Fock paragraph, E.4, E.7 | `simon-fock-045`, `simon-fock-046` | matches | f ∈ H real; the record extends A*(v) to v ∈ h by the same formula |
| Simon p. 24, "the φ(f) are essentially self-adjoint on F_F(H)" | E.4(ii) | `simon-fock-046` | matches | f ∈ H |
| Simon Theorem I.11 (a)-(c), p. 24 | E.3, E.4, E.7 | `simon-fock-046` | matches | real Hilbert space; carried to the realisation of §2.1 by the unitary built in Simon's proof of Theorem I.6 (`simon-gamman-038`: "U(exp iφ(f))U^{-1} = exp(iφ'(f))", U maps Wick monomials to Wick monomials) |
| Simon p. 24, Remark 1, "We also drop "D" treating it as an identity" | E.7(b) | `simon-fock-046` | matches | - |
| Simon p. 27, Fourier normalisation "throughout these notes" | A1 Scope, E conventions | `simon-fourier-049` | matches | - |
| Simon (I.40), p. 31 | E.7(b) | `simon-dgamma-053` | matches (the domain clause "D(dΓ(A)) = +_{n=0}^∞ D_n(A) (incomplete direct sum)" is not quoted but is used) | A = closure of mu on the real K_m; reading of D_n(A): finding F1 |
| Simon Example 3, p. 32 | E.7(b) | `simon-dgamma-054` | matches (the elision is marked) | A positive self-adjoint on H |
| Simon Theorem II.17, (II.46)-(II.48), p. 78-79 | E.7(b), A1 Scope | `simon-freefield-100`, `simon-freefield-101` | matches | F_{m_0} = K_{m_0}: same norm under the same unitary Fourier transform; S_R is dense by E.1(i) |
| Simon p. 12, Wick recursion | E.4(iii), (iv) | `simon-wickprod-034` | matches inside the quotation marks; the record's lead-in "For Gaussian random variables" narrows the printed "several random variables", which is harmless | reading of ∂/∂f_i declared in E.4(iii) |
| Simon p. 16-17, Γ_n as closed span/span of Wick monomials | E.4(iv) Step 5, E.5 | `simon-gamman-038`, `simon-gamman-039` | matches | - |
| Simon (V.1), (V.3), p. 134-136 | E.5 (through A1(d), (W.1)) | `simon-wickdef-156`, `-157`, `-158` | matches; "h(x_j)" [sic] is reported by the record | K_m contains S_R densely and continuously imbedded; S(x,y) = C(x-y) is locally integrable (N.19) |
| GJ2 (1.2.1)-(1.2.6), p. 364 | E.7 | `gj2-fock-04` | matches | - |
| GJ2 𝔖, (1.2.7), (1.2.10), (1.2.11), closures on 𝔇(N^{1/2}), p. 365 | E.7(a)(2) | `gj2-fields-05` | matches | real f, g with mu^{-1/2} f~, mu^{1/2} g~ ∈ L_2: true for real Schwartz functions |
| GJ2 (3.6.2), p. 398 | E.7(a)(4), A7 | `gj2-cutoff-independence-38` | matches | - |
| GJ2 p. 397, algebra 𝔄(𝒮) (A6 Scope, next to the E.7 dictionary) | A6 Scope | `gj2-locality-37` | matches | - |
| GJ1 p. 1948, (3.4) and 𝔄(O) (A6 Scope) | A6 Scope | `gj1-propagation-04` | matches | - |

### 2.5 Dictionary of conventions

| object | Simon (pp. 15, 23-24, 27, 31-32, 78-79) | GJ2 (pp. 364-365, 398) | record, Appendix E | dictionary |
|---|---|---|---|---|
| Fourier transform | unitary, (2π)^{-n/2} ∫ e^{-iΣ t_i x_i} (p. 27) | written f~; its normalisation is not on these pages and is not needed | unitary (l. 8001); App. D uses ∫ e^{-ikx} (l. 4960) but only N.19's kernel is taken over | same as Simon; GJ2's smeared fields are computed from (1.2.10)-(1.2.11) with ∫e^{-ikx} f = (2π)^{1/2} f^ |
| real one-particle space | H; for the free field F_{m_0}, ‖f‖² = ∫|f^|² (k² + m_0²)^{-1/2} dk (II.46) | none (complex L_2(R) in momentum) | K_m, ‖f‖²_m = 2<f, C_m f> = ∫|f^|² mu_m^{-1} dk | K_{m_0} = F_{m_0} = H; j f = mu^{-1/2} f^ maps K_m onto L²_r ⊂ L²(R, dk) |
| complexification | H_C = H ⊕ H with i(ψ, φ) = (-φ, ψ) (p. 23) | - | K^C, inner product conjugate-linear in the first argument | (ψ, φ) <-> ψ + iφ; j^C: K^C -> L²(R, dk) unitary |
| covariance | <φ(v)φ(w)> = ½<v, w> (p. 15); <Ω_0, e^{iφ(f)} Ω_0> = exp(-¼‖f‖²) (p. 24) | <Ω, φ(f)² Ω> = ½‖mu^{-1/2} f^‖² (computed from (1.2.10)) | E[phi_0(f) phi_0(g)] = <f, C g> = ½<f, g>_m | identical |
| Fock space | F(H) = ⊕ H_C^{⊗_s n}; F_F finite vectors (I.28) | F = ⊕ F_n, F_n = L_2 ⊗_s …, ‖ψ‖² = Σ‖ψ_n‖² (no n!), Ω_0 = {1, 0, …} | F(h) = ⊕ S_n h^{⊗n}; F_fin | Υ = Γ(j^C): F(K^C) -> F(L²(R, dk)) |
| creation / annihilation | A*(f)ψ = √(n+1) S_{n+1}(f ⊗ ψ), f ∈ H only; A(f) = A*(f)* restricted to F_F | (a(k)ψ)_{n-1} = n^{1/2} ψ_n(k, …); a*(k) the form (1.2.7) | A*(v), A(v), v ∈ h | ∫θ(k) a*(k) dk = A*(θ); ∫θ(k) a(-k) dk = A(θ^♯), θ^♯(k) = conj θ(-k) |
| field | φ(f) = 2^{-1/2}(A*(f) + A(f)), essentially self-adjoint on F_F | φ(x) = (4π)^{-1/2} ∫ e^{-ikx} mu^{-1/2} {a*(k) + a(-k)} dk | phi_F(v) = closure of 2^{-1/2}(A*(v) + A(v)); phi_0(f) = D phi_F(f) D^{-1} | GJ2 φ(f) = 2^{-1/2}(A*(j f) + A(j f)), carried by 𝔇 = D Υ^{-1} to phi_0(f) |
| momentum | - | π(x) = i(4π)^{-1/2} ∫ e^{-ikx} mu^{1/2} {a*(k) - a(-k)} dk | pi_0(h) = i^N phi_0(mu h) i^{-N} | GJ2 π(h) = 2^{-1/2}(A*(i j mu h) + A(i j mu h)), carried by 𝔇 to pi_0(h); [phi_0(f), pi_0(h)] = i ∫ f h |
| Fock to Q-space | D of Thm I.11: DΩ_0 = 1, Dφ(f)D^{-1} = φ_H(f), DF_n = Γ_n | - | D = D_m, unique (E.4(vi)) | 𝔇 = D Υ^{-1} |
| free Hamiltonian | H_0 = dΓ(mu) (II.48), mu the closure from S (II.47); semigroup convention e^{-t dΓ(A)} = Γ(e^{-tA}) (I.41) | (H_0 ψ)_n = Σ mu(k_j) ψ_n (1.2.5), mu(k) = (k² + m_0²)^{1/2} (1.2.6) | e^{itH_0} = D Γ(e^{it mu^C}) D^{-1} | H_0 = D · closure(dΓ(mu)) · D^{-1} (E.7(b)); 𝔇 H_0^{GJ} 𝔇^{-1} = H_0 (E.7(a)(3)) |
| translations | - | U(α) = multiplication by e^{+iα(k_1+⋯+k_j)} (3.6.2), "Schrödinger picture"; U(-α) φ(x) U(+α) = φ(x+α) | (tau_a f)(x) = f(x - a); U_a = D Γ(tau_a^C) D^{-1}; j tau_a = e^{-ia·} j | U_a = 𝔇 U(-a) 𝔇^{-1}; Ad U_a: phi_0(f) -> phi_0(tau_a f), supports move by +a |
| parity | Γ(-1) (notation of second quantization) | - | Θ = U_{-1} = (-1)^N | 𝔇 Γ(-1) 𝔇^{-1} = Θ |
| Wick kernel | (V.1): ½<f, g>_H = S(f ⊗ g) | - | S(x, y) = C(x - y), C from N.19 | - |
| dilation | - | - | d_s f = s^{-1} f(·/s), e_s h = h(·/s), u_s θ = s^{1/2} θ(s·); m = s m', lambda' = s^{-2} lambda | no counterpart in the cited sources; GJS's scaling is Euclidean (A8(viii)) |

### 2.6 Places in the body that cite Appendix E (checked as far as the citation goes)

`grep -n 'ff-\|app:freefield' part_i/main.tex` also matches "cutoff-" and "off-diagonal"; those false positives are excluded below.

| place | locator | cites | verdict |
|---|---|---|---|
| Introduction notice | ll. 139-151 (p. 2) | App. E; A1(e)-(g); E.7 | holds. Items (e), (f) are from Simon and (g) from GJ2 for E.7 only, as A1 and E.7 confirm. |
| §2.1 | `subsec:model`, 2.1, p. 8; ll. 462-491 | E.3, E.7, E.5 | holds. pi_0 and H_0 are E.3(b),(d) and self-adjoint. They are the sources' objects by E.7(a)(2),(3) and E.7(b). "These are the local algebras of the sources" rests on E.7(a)(2) together with the readings declared in A6's Scope. tau_a(A(O)) = A(O+a) and theta(A(O)) = A(O) are E.5(T),(P). |
| Notation table | ll. 607-609 | E.3, E.5 | holds |
| A1 (e)-(g), Scope, Used in | `A:cutoff`, A1, p. 10; ll. 705-749 (pp. 11-12), 776-801 (p. 12-13), 812 | E.1, E.4(ii), E.5(D), E.7 | holds. All quotations of items (e)-(g) match; those of (b) and (c) match, as do those of (a) and (d) on pp. 12 and 134-136 (for pp. 10 and 137-138 see "Not verified"). The Scope's statement that E.4(ii) covers the weak reading of Thm I.11(b) is right. Example 3 is used only in E.7(b) (confirmed by grep: its only other occurrence is A1, p. 12). (II.48) is taken as the source's definition of H_0, and F_{m_0} = H_C. |
| A6 Scope | `A:patch`, A6, p. 15; ll. 1025-1048 (p. 16) | E.7 | holds as far as E.7 goes. 𝔇 carries the closures of GJ2's phi(f), pi(f) for real f, and H_0^{GJ}, so it carries generated von Neumann algebras onto A(O). The remaining identifications (GJ1's and GJ2's p. 397 fields being (1.2.10)-(1.2.11); real test functions) are declared readings there. |
| A7 statement, Sources, Scope | `A:covar`, A7, p. 16; ll. 1061-1094 (pp. 16-17) | E.5(T),(P), E.6, E.7(a) | holds. U_a = U(-a) under 𝔇 matches GJ2's printed covariance. The three identities are E.6. On "(Θψ)(q) = ψ(-q) in Q-space", see observation O2. |
| Lemma 2.8 | `lem:covparity`, 2.8, p. 22; ll. 1477-1490 | E.5(T) for U_a* = U_{-a}; E.4(iv) for Θ ≥ 0 on Ω_g | holds. U_0 = 1 by E.4(v) with T = id, and Ω_g ∈ L² is non-negative, so E.4(iv) applies. |
| Remark 3.3 | `rem:wlog`, 3.3, p. 24; ll. 1617-1635, 1683-1686 | E.5(D), E.6 | holds. m = m_0 = s M_* = s m' with s = m_0/M_*. All displayed factors (s^{-1} f(·/s), h(·/s), sO, s H_0, s V with lambda', U_{sa}, Θ) agree with E.5(D). The K identity is E.6. |
| Theorem 12.2(4), proof | `thm:MAIN`, 12.2, p. 41; ll. 3110-3123 (pp. 41-42) | E.5(T), (P) | holds. tau_{-a}(A(O)) = A(O-a), and theta maps A(O) onto itself. |
| Corollary 12.3, proof | `cor:canonical`, 12.3, p. 42; ll. 3136-3149 | E.5(T) | holds as far as the citation goes, except for the implicit measurability of a' -> omega(tau_{eps a'} A), which needs strong continuity of a -> U_a (finding F2). The identification of GJ3's sigma_{a'} with tau_{eps a'} is GJ3-side and not checked. |
| Theorem 13.2, Step 1 | `thm:dichotomy`, 13.2, p. 43; ll. 3207-3216 | E.5(T) | holds. tau_a(B) ∈ A(O+a) and ‖tau_a(B)‖ = ‖B‖. |
| Appendix B, free-field entry | `app:provenance`, B, p. 47; ll. 3483-3519 (pp. 48-49), 3542-3545 (p. 49) | App. E, E.5, E.6, E.7 | holds, except for one over-inclusive clause (finding F3). |

### 2.7 Status words for E.1-E.7

| statement | status | conditional on |
|---|---|---|
| E.1 | proved | nothing external |
| E.2 | proved | nothing external |
| E.3 | definition, well posed; its embedded claims are proved | A1(e): Thm I.11 (a), (c), used literally |
| E.4 | proved, conditional | A1(e) as printed (Thm I.11 (a)-(c), under both readings of (b), and essential self-adjointness on F_F); the formal-derivative reading of A1(a), declared in the proof of (iii); A1(c) |
| E.5 | proved, conditional | as E.4; A1(d) and (W.1) at masses m and m', including the reading of Theorem V.2(b) that A1's Scope records for unbounded g; that reading is inherited from the definition of V(g), and for bounded g, the only g the body uses according to A1's Scope, the element is the explicit limit of Lemma N.23'. Also Lemma N.19's formula. |
| E.6 | proved, conditional | A1 (essential self-adjointness of K(g) for g ∈ C_H, read on D(H_0) ∩ D(V(g)), which is equivalent) and E.5 |
| E.7 | proved, conditional | GJ2's printed definitions, read as recorded: (1.2.10)-(1.2.11) smeared as ∫φ(x) f(x) dx with real f, as GJ2 itself writes on p. 397; (1.2.5) on its maximal domain; "closures on 𝔇(N^{1/2})". Simon's Thm I.11, (I.40) with "D" dropped as the source says and D_n(A) read as in F1, Example 3 and (II.46)-(II.48). |

### 2.8 Comparison with the earlier audit reports

I wrote this subsection after everything else in this file. Only then did I open `ugjs/council/v4f-free-field-report.md`, `ugjs/council/v5-math-report.md` and `ugjs/council/v5-sources-report.md`.

- **No verdict differs.** V5 (mathematics) redid the computations of E.1-E.7 by hand and found them correct, and V5d closed its last points. V5 (sources) found every quotation exact. I reach the same verdicts independently, on the final text of 49f2d23. V4f audited the state before the repair; its MAJOR findings F1, F4, F6 and F7 (pi_0 and H_0 undefined; the dilation unitary asserted; translation and parity actions on the net neither derived nor imported) are closed by E.3, E.5(D), E.5(T) and E.5(P), as I verified.
- **The three passages seen by one auditor only since their last change hold.** These are Lemma E.1(ii)'s core argument (ll. 8089-8096), Lemma E.7(a)(2)'s comparison of closures (ll. 8597-8619) and Remark E.6 (ll. 8517-8527). I checked their final wording, including the density of 𝔖 in 𝔇(N^{1/2}) that V5c-1 asked for and the passage to the closure for Θ that F-K asked for (2.2).
- **Same observations.**
  - GJ2's (1.2.12) sign: my O1 matches V5 (mathematics) F-F, "Separately".
  - V5 F-G's remark that Example 3 could be dropped (the symmetrised products of D(mu^C) form a dense, e^{itH_0}-invariant subset of D(H_0), hence a core) agrees with my reading of E.7(b). It is an alternative, not a defect.
  - The formal-derivative reading of E.4(iii) was raised as F-O and as sources N1. It is now declared in the record, and I accept it as a declared reading.
- **New here**, not raised by any earlier report:
  - F1: the undeclared reading of the domain D_n(A) in (I.40). V5 (sources) checked the quotation "D_n(A) ⊂ Γ_n(H)", "(incomplete tensor product)" as exact, which it is; the point is the reading, not the quotation.
  - F2: the strong continuity of a -> U_a used implicitly by Corollary 12.3. V5 (sources) m6 and V5 (mathematics) dealt with Corollary 12.3 only as to which properties of tau it uses.
  - F3: Appendix B's "they are identified with the objects of the sources", which includes the dilation unitary.
  - O4: A1's Scope speaks of "the sources of the cutoff construction" collectively, while E.7 covers GJ2 only. This is the analogue, for GJ71 and Rosen70, of V5 (sources) N3 / V5 (mathematics) N-2 on GJ1, which the record now declares as a reading in A6's Scope.
- **Locators.** The page offsets that V5 (sources) records (Simon: PDF page = printed + 22; GJ2: PDF page = printed - 360) are consistent with the image names I used (for example `simon-fock-045` shows printed p. 23, and `gj2-fock-04` shows p. 364). I did not open `refs/` to confirm them.

## 3. Findings

**F1 (MINOR). Undeclared reading of the domain of Simon's dΓ(A) in Lemma E.7(b).**

Locator: `lem:ff-sources`, E.7, p. 122 (proof of (b) on p. 124), ll. 8640-8648; A1(f), ll. 723-726 (p. 12).

Quotation. E.7(b): "Let $v_1,\dots,v_n\in D(\mu^{\C})$. Then $t\mapsto\Gamma_{\!\mathcal F}(e^{it\mu^{\C}})S_n(v_1\otimes\dots\otimes v_n)=S_n(e^{it\mu^{\C}}v_1\otimes\dots\otimes e^{it\mu^{\C}}v_n)$ is differentiable at $t=0$, [...] So these vectors lie in the domain of $D^{-1}H_0D$, which acts on them by the formula (I.40) with $A=\mu$. [...] That is, $D^{-1}H_0D$ extends $d\Gamma(\mu)$". A1(f) quotes "``$D_n(A)\subset\Gamma_n(\mathcal H)$'' the ``(incomplete tensor product)'' $D(A)\otimes\dots\otimes D(A)$". The printed p. 31 (`simon-dgamma-053`) reads "Let D_n(A) ⊂ Γ_n(H) be D(A)⊗…⊗D(A) (incomplete tensor product) and D(dΓ(A)) = +_{n=0}^∞ D_n(A) (incomplete direct sum)".

Why it is a finding. The algebraic tensor power of the real subspace D(A) is not a complex subspace and is not contained in the symmetric space Γ_n(H) ≅ F_n(H). The proof reads D_n(mu) as the complex span of the symmetrised products S_n(v_1 ⊗ ⋯ ⊗ v_n) with v_j ∈ D(mu^C), and D(dΓ(mu)) as finite sums over n. It needs the second of these for "D^{-1} H_0 D extends dΓ(mu)". Neither reading is declared, and the domain clause is not quoted. Correctness is unaffected, for two reasons:
- The two natural readings coincide: symmetrise, or intersect the complexified algebraic tensor power with F_n. S_n maps the algebraic tensor power into itself and is the identity on F_n.
- D(mu^C) = D(closure mu) + i D(closure mu), since mu is even and real, so complexifying first or last gives the same span.

Repair. One clause in E.7(b) or in A1's Scope: "(I.40)'s D_n(A) is read as the complex span of the symmetrised products of vectors of D(A), the only reading under which it is a subspace of Γ_n(H), and D(dΓ(A)) as their finite sums over n (the source's 'incomplete direct sum')".

Severity: MINOR.

**F2 (MINOR). Strong continuity of a -> U_a is not stated, and the proof of Corollary 12.3 uses it.**

Locator: `prop:ff-symmetries`(T), E.5, p. 120, ll. 8354-8365; `cor:canonical`, 12.3, p. 42, ll. 3137-3148.

Quotation. E.5(T) states "$U_a1=1$, $U_aU_b=U_{a+b}$, and [...]", with no continuity in a. Corollary 12.3 writes "let $\sigma_{a'}$ denote the space-translation automorphisms used there (our $\tau_{\epsilon a'}=\mathrm{Ad}\,U_{\epsilon a'}$ of Proposition~\ref{prop:ff-symmetries}(T) [...])" and then "$\omega_n(A)=\frac1n\int\ip{\Om_{g_n}}{\sigma_{a'}(A)\Om_{g_n}}\,\bar h(a'/n)\,da'=\int_{-1}^{1}\bar h(u)\,\omega_{g_n}(\tau_{\epsilon nu}A)\,du$".

Why it is a finding. The integrals over a' and over u need u -> omega_{g_n}(tau_{eps n u} A) to be measurable. The bound ‖(omega_n - omega_∞)|A(O)‖ ≤ ∫ h̄(u) ‖…‖ du needs its integrand to be measurable. Once the first function is continuous, the integrand is lower semicontinuous, as a supremum of continuous functions, and so measurable. Both properties hold because a -> U_a is strongly continuous, but Appendix E never states this. The fact follows in one line: j^C tau_a^C (j^C)^{-1} is multiplication by e^{-iak}, strongly continuous in a by dominated convergence, so a -> tau_a^C is a strongly continuous unitary group and E.2(iv) applies. Equivalently, through E.7(a)(4), U_a corresponds to GJ2's multiplication operators U(-a).

Repair. Add to E.5(T): "and a -> U_a is a strongly continuous one-parameter unitary group (Lemmas E.1(ii) and E.2(iv))".

Severity: MINOR.

**F3 (MINOR). One clause of Appendix B says more than Lemma E.7 proves.**

Locator: `app:provenance`, B, entry "The free-field layer", ll. 3501-3507 (p. 49).

Quotation. "Repaired by Appendix~\ref{app:freefield}: the momentum field, the free Hamiltonian and the unitaries of translation, parity and dilation are defined through the unitary between Fock space and $Q$-space of the source's Theorem I.11 (Assumption~\ref{A:cutoff}(e)--(f)); their action on the fields, on the local algebras, on $H_0$ and on $V(g)$ is proved (Proposition~\ref{prop:ff-symmetries}); and they are identified with the objects of the sources (Lemma~\ref{lem:ff-sources})."

Why it is a finding. "They" includes the dilation unitary. Lemma E.7 identifies the vacuum, phi_0, pi_0, H_0, U_a and Θ with objects of GJ2, and H_0 with Simon's dΓ(mu). No cited source has a Fock-space dilation unitary, and E.7 identifies none; the same entry says that A8(viii) "imports a Euclidean scaling only" (l. 3495).

Repair. "... and, except for the dilation unitary, which has no counterpart in the sources, they are identified with the objects of the sources (Lemma E.7)".

Severity: MINOR.

**Observations (not findings against the record).**
- **O1. GJ2's (1.2.12) has the opposite sign; the record does not use it.** GJ2 p. 365 (`gj2-fields-05`) prints "e^{iπ(g)} e^{iφ(f)} = e^{-i(f,g)} e^{iφ(f)} e^{iπ(g)}". From (1.2.10)-(1.2.11) I compute [φ(x), π(y)] = iδ(x - y), using the form a*(k) of (1.2.7) and a(k) of p. 364. The Weyl form of this CCR is e^{iπ(g)} e^{iφ(f)} = e^{+i∫fg} e^{iφ(f)} e^{iπ(g)}. Check on Q = x, P = -i d/dx: e^{iP} e^{iQ} = e^{i} e^{iQ} e^{iP}. So the printed sign agrees only if GJ2's (f, g) means -∫fg; I did not check how GJ2 defines (f, g). The record says the Weyl relations are not used (l. 7996), and Appendix E does not use them. This bears only on any future use of (1.2.12).
- **O2. The Q-space formula for Θ holds in the record's own realisation.** A7 asserts "(Θψ)(q) = ψ(-q) in Q-space" (l. 1065), and its Scope (ll. 1085-1087) calls this a presupposition on the realisation. For the realisation L²(S'(R), dphi_0) of §2.1 with phi_0(f)(q) = q(f) the presupposition holds. The centred Gaussian measure has an even characteristic functional, so q -> -q preserves it, and the identity phi_0(f)(-q) = -phi_0(f)(q) passes to L² limits. So E.5(P)'s last sentence applies there. §2.1 does not write phi_0(f)(q) = q(f) explicitly. No proof depends on this.
- **O3. Theorem I.11 transfers to the record's realisation.** The appendix carries Simon's Thm I.11 to L²(S'(R), dphi_0) through Theorem I.6 (ll. 7990-7993). The unitary of Simon's proof of Theorem I.6 (`simon-gamman-038`, `simon-gamman-039`) fixes 1, maps fields to fields and Wick monomials to Wick monomials, so composing it with D gives (a)-(c) for the other realisation. The record does not write this line; I count it as immediate.
- **O4. E.7 covers the Fock-space objects of GJ2 only.** A1's Scope says "The sources of the cutoff construction work in Fock space; the dictionary between their Fock space and Q-space is the unitary 𝔇 of Lemma E.7" (ll. 797-801, p. 13). E.7 proves the dictionary for GJ2's objects (1.2.1)-(1.2.11) and (3.6.2) only. A1's Sources line also lists GJ71, Rosen70 and the GJS page; I did not check whether these work in GJ2's Fock space or in a Q-space realisation (see "Not checked").

## 4. Checks actually run

1. Read the frozen `part_i/main.tex` (commit 49f2d23):
   - ll. 136-155 (introduction notice);
   - ll. 440-562 (§2.1);
   - ll. 590-839 (notation, A1, start of A2);
   - ll. 940-1100 (end of A4, A5, A6, A7, start of A8);
   - ll. 1455-1514 (Lemma 2.8, §2.2 start);
   - ll. 1560-1709 (proof of Proposition 3.2, Remark 3.3);
   - ll. 3050-3249 (Theorem 12.2, Corollary 12.3, Hypothesis 13.1, Theorem 13.2 Steps 1-4);
   - ll. 3478-3545 (Appendix B, free-field entry and external residue);
   - ll. 4955-5044 (Lemma N.19 statement, proof of (ii), (i) and part of (iii));
   - ll. 7970-8744 (Appendix E in full, and the bibliography).
2. `grep 'newlabel{<label>}' part_i/main.aux` for 29 labels. Output used above: app:freefield {E}{115}; lem:ff-onepart {E.1}{115}; lem:ff-gamma {E.2}{117}; def:ff-objects {E.3}{118}; lem:ff-transport {E.4}{118}; prop:ff-symmetries {E.5}{120}; rem:ff-A7 {E.6}{122}; lem:ff-sources {E.7}{122}; subsec:model {2.1}{8}; A:cutoff {A1}{10}; A:patch {A6}{15}; A:covar {A7}{16}; A:domain {A5}{15}; A:gjs {A8}{17}; lem:covparity {2.8}{22}; rem:wlog {3.3}{24}; thm:MAIN {12.2}{41}; cor:canonical {12.3}{42}; thm:dichotomy {13.2}{43}; eq:wickpairing {W.1}{11}; aux:notation-kernel {N.19}{69}; aux:notation-wick {N.20}{71}; aux:notation-ident {N.23'}{76}; eq:T {T}{22}; app:comparison {D}{57}; app:provenance {B}{47}; A:fkn {A2}{13}; sec:setting {2}{8}; subsec:imports {2.4}{10}.
3. `grep -n 'ff-\|app:freefield' part_i/main.tex`: every true citation of Appendix E was read (table 2.6).
4. `pdfinfo part_i/main.pdf`: Pages: 125. `pdftotext` page by page: PDF page 115 carries the footer "115". Phrase-to-page mapping, used for the page numbers in 2.6 and section 3:
   - "The free-field layer" on pp. 2, 48; "Repaired by" on p. 49;
   - "construction work in Fock" on p. 13; "Since 11 November 2026 the three" on p. 16;
   - "used there (our" on p. 42; "Step 1: uniform cutoff" on p. 43;
   - "Example 3" on pp. 12, 124; "In the same way Proposition" on p. 122.
5. Opened 20 page images in `audit_2026/evidence/`: `simon-fock-045`, `simon-fock-046`, `simon-fourier-049`, `simon-dgamma-053`, `simon-dgamma-054`, `simon-freefield-100`, `simon-freefield-101`, `simon-gaussproc-037`, `simon-gamman-038`, `simon-gamman-039`, `simon-wickpair-033`, `simon-wickprod-034`, `simon-wickdef-156`, `simon-wickdef-157`, `simon-wickdef-158`, `gj2-fock-04`, `gj2-fields-05`, `gj2-cutoff-independence-38`, `gj2-locality-37`, `gj1-propagation-04`.
6. Numerical corroboration (status `numerical`; nothing is deduced from it).
   - Environment: the scratch script `check_dilation.py` in the auditor's work directory (not archived), run with the system python3 3.14.7 (the project has no `.venv`), numpy 2.5.2, scipy 1.18.1.
   - Tolerances: `quad` with epsabs 1e-12 and epsrel 1e-10 (outer integral of check 6: 1e-10 and 1e-8). No randomness.
   - Test function: f(x) = (1+x) e^{-x²/2}, whose transform (1 - ik) e^{-k²/2} was itself checked by direct quadrature.
   - The cross-check C(u) = K_0(m|u|)/(2π) is `from memory`; it agreed with N.19's integral to 2.5e-16 at four points.

   Output, abridged to the differences:
   - [1] C_{m'}(sz) vs C_m(z): (m', s, z) = (1, 2, 0.3), (0.7, 0.5, 1.7), (2, 3, 0.05), (1, 1, 0.9); differences 1.39e-17, 0, 2.50e-16, 0.
   - [2] ‖d_s f‖²_{m'} vs ‖f‖²_m: (m', s) = (1, 2), (0.6, 0.4), (1.5, 1); differences 0, 0, 0 (values 1.225385479067, 4.690170757762, 1.560450393213).
   - [3] smeared kernels: (m', s, y) = (1, 2, 0.4), (0.8, 0.5, -0.9); differences 8.33e-16, 4.44e-16.
   - [4] d_s mu_m f = mu_{m'} e_s f on the Fourier side: differences 0, 1.11e-16.
   - [5] (4π)^{-1/2}(2π)^{1/2} = 0.707106781186547; 2^{-1/2} = 0.707106781186548.
   - [6] ‖f‖²_m vs 2<f, C_m f> through N.19's kernel at m = 1.3: 1.7484752850 and 1.7484752850, difference 4.26e-13.

## 5. Not done, not verified, not run

**Not checked** (not findings):
- Whether the cutoff-construction sources other than GJ2 (GJ71, Rosen70, the GJS page listed in A1's Sources; GJExp and Simon Thm V.12 in A5) use GJ2's Fock-space objects or a Q-space realisation. This matters for the A1 Scope sentence in O4; E.7 covers GJ2 only.
- That GJ1's fields and Fock space are GJ2's. A6's Scope declares this as a reading; I read only p. 1948 of GJ1.
- How GJ2 defines (f, g) in (1.2.12) (O1), and GJ2's Fourier normalisation f~.
- Theorem V.2(b) of Simon and the normalisation of its phi_F (pp. 137-138). E.5's Wick identities inherit A1(d)'s reading for unbounded g.
- Lemma N.19 beyond its formula, the proof of (ii) and the parts of (i) and (iii) read. Appendix E uses only the formula and the kernel identity of (ii).
- Lemma N.23' (the explicit limit for bounded g).
- The rest of the proofs of Theorem 12.2, Corollary 12.3, Theorem 13.2 and Remark 3.3 beyond their citations of Appendix E. These were assigned to the second auditor, as were A1's own imports (essential self-adjointness, the simple ground state, positivity).
- GJ3's averaged-state formula (2.3)-(2.5) and its translation convention eps.
- The dossier index file in `audit_2026/` and the dossier map in `part_i/README.md`.
- The Bessel-function closed form of the 1D kernel used in numerical check 1 (`from memory`).

**Not verified** (quotations not compared with a page image in this session):
- A1(a)'s quotations of Simon p. 10 ((I.15), (I.18a), (I.18b));
- A1(d)'s quotations of Simon pp. 137-138 (the norm formula, Theorem V.2(b), (V.6b));
- A6's Scope quotation of GJExp p. 42.

Appendix E's own steps use none of these, except that E.5 inherits A1(d)'s existence statement for the Wick powers. Every other quotation that Appendix E uses, and every quotation in the free-field sentences of the passages in 2.6, was compared with its page image.

**Not run**:
- no LaTeX build (not requested);
- no git command that changes a repository;
- no `kb` command;
- no source PDF from `refs/` opened, since every page needed was in the evidence images;
- no subagents.

**Not done**: none of the tasks 1-6 of the brief is left undone.

## 6. Files written

- `reports/v6-appendix-e-audit.md` in the council's scratch directory (this report).
- `check_dilation.py` and its output `check_dilation.out` in the auditor's scratch work directory (not for archiving).
- The per-page text dumps `pg_*.txt` of the frozen `part_i/main.pdf`, used only for page locators, in the same work directory.
- Nothing under the repository.
