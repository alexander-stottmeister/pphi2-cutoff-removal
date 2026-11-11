# Rounds V5 to V5d: mathematics of the free-field appendix (11 November 2026)

One agent (general-purpose, model claude-opus-5-5) that had written none of the audited text, read-only. It audited the mathematics of the repair of the V4f findings in `part_i/main.tex`: Appendix E line by line and the rewritten passages of §2.1, Assumptions A6 and A7, Lemma 2.8, Remark 3.3 and the proofs of Theorems 12.2 and 13.2. It then re-checked the orchestrator's fixes and audited the text they added, three times (V5b, V5c, V5d). Four reports, in the order returned.

Returned by the agent as messages, not as files. Saved here on 11 November 2026 by the orchestrator from the session transcript, before the commit of the repair. The text is verbatim except that paths under the home directory and under the session's temporary folder are replaced: `<scratch>/` is that temporary folder, which is not kept (the files `phase5/...` and the diffs named in the reports were the orchestrator's working copies there), and paths inside this repository are written relative to its root. The line numbers of each report refer to the working tree as it was when that report was written; the times are those of the transcript, in UTC. Findings and dispositions: `part_i/README.md`, "Free-field appendix (2026-11-11)".

---

## V5 (returned 2026-11-11 11:22 UTC)

## Audit of the free-field repair (uncommitted diff against f213cc8, part_i/main.tex, 8590 lines)

**Outcome.** I found no CRITICAL finding. Every computation in Appendix E that I redid by hand comes out as stated. There is one MAJOR gap: Remark 3.3 transports the dynamics α but does not derive that transport. There are fifteen MINOR points, all of precision, scope or notation. F1 and F3–F10 are closed; F2 is only partly closed.

### 1. Findings, most serious first

**F-A. MAJOR: Remark 3.3 (`rem:wlog`), ll. 1600–1608.**
- Text: "Every conclusion of Theorem 12.2 … therefore holds for the original model with the dictionary: … dynamics $\alpha_t\leftrightarrow\alpha_{st}$, the light cone being form-invariant".
- Why it fails: the remark never derives this correspondence, and it never says what α is for the original model at $(m_0,\lambda)$. That α is either the import A6(ii) at the original parameters, or it is defined by transport; the remark says neither. Item (3) of Theorem 12.2 (ground state of $(\mathfrak A,\alpha)$) depends on this. Item (2), local normality, is not in the dictionary either, though it is immediate because $\mathrm{Ad}\,U_s$ is spatial.
- The conclusion is true. I derived it:
  - $U_sH_{m_0,\lambda}(g)U_s^*=sH_{M_*,\lambda'}(g(\cdot/s))$ (subtract $E$), so $\mathrm{Ad}U_s\circ\beta^g_t=\beta'^{g(\cdot/s)}_{st}\circ\mathrm{Ad}U_s$.
  - For $A\in\mathfrak A(O)$ and $g\equiv1$ on $O_{|t|}$, (P) of A6(ii) at both parameter points gives $\mathrm{Ad}U_s\,\alpha_t(A)=\alpha'_{st}(\mathrm{Ad}U_s A)$. Here $\mathrm{Ad}U_sA\in\mathfrak A'(sO)$, and $g(\cdot/s)\equiv1$ on $(sO)_{s|t|}$.
  - This extends to $\mathfrak A$ by density. The spectral condition is invariant under $t\mapsto st$ for $s>0$.
- Repair: insert these lines. State that A6(ii) is used at $(m_0,\lambda)$, or define $\alpha^{(m_0)}_t:=\mathrm{Ad}U_s^*\circ\alpha'_{st}\circ\mathrm{Ad}U_s$. Add "(2): $\mathrm{Ad}U_s$ is spatial".

**F-B. MINOR: Theorem 12.2(1) read through Remark 3.3, ll. 1603–1609 and 2978.**
- In original coordinates the remark sets $m_1:=s\,m_{1,*}$, and the transported rate is $\Psi_{m_{1,*}}(sd)$, built with the working-coordinate $M$.
- That is not $\Psi_{m_1}(d)$ with this $m_1$: $\Psi_\gamma$ of eq. (Psidef), l. 2789, is not scale-covariant (it contains $M$, $W_\gamma$, $T_\gamma$ and $d_0=4+2/\gamma$).
- The remark states the right thing, but the symbol $m_1$ now means two things.
- Repair: add one sentence saying that, in original coordinates, item (1) reads $\Psi_{m_{1,*}}(s\,d)$ and not $\Psi_{m_1}(d)$.

**F-C. MINOR: Remark 3.3, ll. 1609–1614, the local-moment clause.**
- "equivalently, it holds for supports of length 2 … constant $(\lceil s\rceil+1)\,s\,M$" is a consequence, not an equivalence.
- For $s\le1$ one piece suffices and gives $sM$. For $s\ge1$, $\lceil s\rceil$ pieces made with indicator functions suffice.
- The stated bound is valid: $\Omega_g\in D(V(h_k))$ by Prop. `prop:smoothing`, and finite additivity holds.
- Repair: replace "equivalently" by "consequently".

**F-D. MINOR: Prop. E.5(D) Wick-power paragraph, ll. 8350–8385, versus the Scope of A1, ll. 763–765.**
- The proof uses (W.1), the uniqueness clause of A1(d) and the kernel formula of Lemma N.19 at the mass $M$.
- A1(d) and N.19 are stated at $m_0$ only, and the Scope declares only items (e) and (f) as used at $M_*$.
- The source (V.3) is general and the proof of N.19 is mass-generic, so nothing is false.
- Repair: add to the Scope "items (a)–(d) and Lemma N.19 are used at $M_*$ as well".

**F-E. MINOR: Appendix E intro, ll. 7892–7895.**
- "Its external inputs are the printed statements … items (e) and (f)" is incomplete. The appendix also uses:
  - A1(a) in E.4(iii);
  - A1(c) in E.3(a) and E.4 Step 5;
  - A1(d) in E.5;
  - implicitly Thm. I.6, to apply Thm. I.11 to the concrete realisation $L^2(\mathcal S'(\mathbb R),d\phi_0)$.
- The Used-in line, l. 788, is correct ("(a), (c)–(g)").
- Repair: list (a), (c), (d) and Thm. I.6, or Simon's remark on p. 23 that "any of the above models will do".

**F-F. MINOR: Lemma E.7(a)(2), ll. 8411–8417 and 8466–8469, and the Scope of A6, ll. 1000–1002.**
- GJ2 p. 365 (image gj2-fields-05) prints that φ(f), π(g) "define operators whose closures on $\mathfrak D(N^{1/2})$ are self-adjoint". The record closes on $\mathfrak S$ instead.
- The two closures coincide: $D(N^{1/2})\subseteq D(\varphi_{\mathcal F}(\theta))$, where the form operator agrees with $\varphi_{\mathcal F}(\theta)$, and $\mathfrak S$ is a core. The text does not say so, yet A6 Scope speaks of "the closures of the source's Fock-space fields".
- Repair: one sentence equating the two closures.
- Separately, not a defect of the record: GJ2's Weyl relation (1.2.12) carries $e^{-i(f,g)}$. From (1.2.10)–(1.2.11) I compute $[\varphi(f),\pi(g)]=i(f,g)$, which gives $e^{+i(f,g)}$. The record does not use (1.2.12).

**F-G. MINOR: Lemma E.7(b), ll. 8488–8501, and the Scope of A1, ll. 768–774.**
- The record identifies Simon's μ, which (II.47) defines as "the closure of the operator defined on S" in $F_{m_0}$, with $j^{-1}\mu(\cdot)j$ on its maximal domain. The core property of $\mathcal S\cap L^2_{\rm r}$ is not argued.
- The isometry $F_{m_0}\cong\mathcal H_C$ depends on Simon's Fourier normalisation in (II.46), which I could not see on the dossier pages.
- "$-T$ generates a contraction semigroup, so $T+1$ maps $D(T)$ onto" uses Hille–Yosida without naming it.
- What Example 3 must supply is only $\mathrm{Ran}(T+1)=L^2$. Neither (I.41) nor the $L^p$ clause is used. Example 3 could be dropped altogether: the span of $S_n(v_1\otimes\dots\otimes v_n)$ with $v_j\in D(\mu)$ is dense, $e^{itH_0}$-invariant and in $D(H_0)$, so it is a core.
- Affects only the identification lemma, not the body.

**F-H. MINOR: two Fourier conventions in one manuscript.**
- App. E, l. 7901, uses $\hat f=(2\pi)^{-1/2}\int e^{-ikx}f$. App. N, ll. 4864–4866, uses $\hat f=\int e^{-ikx}f$.
- The A1 Scope sentence "the map $f\mapsto\mu^{-1/2}\hat f$ carries $F_{m_0}$ isometrically onto $L^2_{\rm r}$" is true only in the App. E convention and does not say so.
- No computation mixes the two: E.5(D) takes only the heat-kernel formula from N.19. Repair: say so in both places.

**F-I. MINOR: notation clashes.**
- $M$ is a mass in E.5(D) ($m=sM$, $V_{M,\lambda'}$) but the moment constant in the notation table and in Remark 3.3 ("$sM$").
- $J=\Gamma_{\mathcal F}(j^{\mathbb C})$ (E.7) versus $J_t$ (A2).
- $\Omega_0$ is the Fock vacuum in A1(e), (g) and E.7(a)(1) ("$\mathfrak D\Omega_0=1$") but $1$ in the body.
- $N$ (number grading) versus $N_I$.
- Repair: rename the mass in E.5(D) (e.g. $m'$), write $\Omega^{\rm GJ}$ for the source's vacuum, and rename $J$.

**F-J. MINOR (F2 residue): l. 360 (introduction) uses $\Omega_0$ before its definition at l. 451.**
- The Appendix B entry, ll. 3417–3418, says "$\varphi_0$ and $\Omega_0$ are introduced where they are first used".
- Repair: add a forward reference at l. 360, or qualify the entry.

**F-K. MINOR: Lemma 2.8, ll. 1448–1450.**
- "Θ … commutes with $H_0$, and … $\Theta V(g)\Theta=V(g)$; hence $\Theta\Omega_g=c\Omega_g$" skips the passage to the closure $K(g)$.
- Remark E.6 makes that passage for $U_a$ but not for Θ.
- Repair: "so Θ maps $D(H_0)\cap D(V(g))$ onto itself and $\Theta K(g)\Theta=K(g)$".

**F-L. MINOR: Prop. E.5(D), l. 8382, at the boundary λ = 0.**
- $\frac{\lambda}{s\lambda'}V_{M,\lambda'}$ divides by zero at λ = 0, which the standing hypothesis $0\le\lambda$ admits. The identity is trivially true there.
- Repair: write $\lambda s^{-1}\sum_n a_n{:}\cdots{:}=s\,\lambda'\sum_n a_n{:}\cdots{:}$.

**F-M. MINOR: Lemma E.1 is stated on $\mathcal S_{\mathbb R}$ but used on all of $\mathcal K^{\mathbb C}$.**
- E.1(ii) and (iii) give $j\tau_a=e^{-ia\cdot}j$ and $j_Md_s=u_sj_m$ on $\mathcal S_{\mathbb R}$ only.
- E.5(T), (D) and E.7(a)(4) use them on all of $\mathcal K^{\mathbb C}$; the extension by continuity and complex linearity is not stated.

**F-N. MINOR (pre-existing): (W.1), l. 673, has $f_j\in\mathcal S(\mathbb R)$; it must be real.**
- The same holds for "entries in $\mathcal S(\mathbb R)$" at ll. 8306 and 8376.
- The uniqueness clause is used correctly: uniqueness in (V.3) for a single $g\in\mathcal S$ implies that the S-Wick monomials have zero orthogonal complement in $\Gamma_n$. The record leaves this inference implicit.

**F-O. MINOR: Lemma E.4(iii), ll. 8159–8165.**
- The argument is complete if Simon's recursion is read as defining a formal polynomial: ∂/∂f_i is a formal partial derivative, which is how A1(a) quotes it.
- Under that reading the coefficients are determined inductively by the mixed moments, also for linearly dependent $f_j$.
- Repair: say "polynomial in formal variables" once.

### 2. Checked and found correct (hand computations)

**Lemma E.1**
- (i): isometry, density of $\mathcal S\cap L^2_{\rm r}$, reality of inner products on $L^2_{\rm r}$, unitarity and complex linearity of $j^{\mathbb C}$.
- (ii): Fourier transforms of $\mu f$ and $\tau_af$.
- (iii): $\widehat{d_sf}(k)=\hat f(sk)$; $\mu_m(sk)=s\mu_M(k)$; $\|d_sf\|_M=\|f\|_m$ by $q=sk$; $j_Md_s=u_sj_m$; $d_s\mu_m=\mu_Me_s$ (both sides have transform $s\mu_M(k)\hat f(sk)$); $d_s\tau_a=\tau_{sa}d_s$; unitarity of $u_s$; $u_sw(\cdot)u_s^{-1}=w(s\cdot)$.

**Fock-space paragraph and Lemma E.2.** All items, including the adjoint argument for $A(v)$ and the telescoping estimate.

**Definition E.3.** Well-defined; $H_0$ via Stone's theorem; $\pi_0(th)=t\pi_0(h)$.

**Lemma E.4**
- (i)–(iii) and (v)–(vi).
- (iv), Steps 1–6: Fourier inversion and Fubini; $G_n\in\mathcal S$, $|G_n|\le\sup|G|$, pointwise convergence; resolvent passage; common a.e. subsequence; positivity via $(U_TG)^2$; truncation.
- Theorem I.11(b) under both readings: a self-adjoint operator contained in a self-adjoint one equals it.
- No circularity between E.3 and E.4(vi).

**Proposition E.5**
- (T): π-relation; generators of $\mathfrak A(O)\mapsto\mathfrak A(O+a)$; $H_0$ invariance; Wick pairing with $y=y'-a$; n = 0; a = 0.
- (P): all items, including $\Theta\pi_0\Theta=-\pi_0$, $(-1)^n$ on the chaoses, positivity and the realisation $R=U_{-1}$.
- (D):
  - $U_s\pi_0^{(m)}(h)U_s^*=\pi_0^{(M)}(e_sh)$;
  - $U_se^{itH_0^{(m)}}U_s^*=e^{itsH_0^{(M)}}$;
  - $C_M(sz)=C_m(z)$ (substitution $u=s^2t$);
  - $\int(d_sf)(x')C_M(x'-sy)\,dx'=\int f\,C_m(x-y)$;
  - the second pairing with $y'=sy$ and $s\tilde g(sy)=g(y)$, giving the factor $s^{-1}$;
  - $\lambda'=s^{-2}\lambda$ and the final factor $s$;
  - n = 0 ($\int g=s^{-1}\int e_sg$) and s = 1.

**Remark E.6** (domains and closure for $U_a$ and $U_s$).

**Lemma E.7**
- Formulas for $A^*(\theta)$ and $A(\theta)$; $\int\theta(k)a(-k)\,dk=A(\theta^\sharp)$.
- The factor $(4\pi)^{-1/2}(2\pi)^{1/2}=2^{-1/2}$.
- $\varphi(f)=\varphi_{\mathcal F}(jf)$ and $\pi(h)=\varphi_{\mathcal F}(i\,j\mu h)$.
- The sign: $\Gamma(i)\varphi_{\mathcal F}(v)\Gamma(i)^{-1}=\varphi_{\mathcal F}(iv)$, so $\pi_0=i^N\varphi_0(\mu h)i^{-N}$ matches (1.2.11).
- $[\varphi(f),\pi(h)]=i(f,h)$, and $\pi=i[H_0,\varphi]$.
- $U_a\leftrightarrow U(-a)$, consistent with GJ2's $U(-\alpha)\varphi(x)U(\alpha)=\varphi(x+\alpha)$ and with A7.
- (b), given $\mathrm{Ran}(T+1)=L^2$.

**Body passages**
- §2.1: definitions, the "Equivalently" clause, and the generator set $\{W(f,0),W(0,h)\}$.
- A6(i) is exactly the inclusion that Prop. 2.7's Trotter step uses, via $(O_r)_\delta=O_{r+\delta}$.
- A7 identities for every $\mathscr P$.
- Lemma 2.8: phase; $U_a^*=U_{-a}$; $c=+1$ by positivity and $\Omega_g>0$.
- Remark 3.3: $K$-identity; ground vectors; $\omega^{(m_0)}_g=\omega^{(M_*)}_{g(\cdot/s)}\circ\mathrm{Ad}U_s$; localization; plateau distance; translations and parity via $U_sU_aU_s^*=U_{sa}$; gap $s\,m_{1,*}$ via $\mathrm{spec}$; $\|V_{m_0,\lambda}(h)\Omega_g\|\le sM$ on supports of length $2/s$.
- Proof of Thm 12.2(4) and Step 1 of Thm 13.2: now justified by Prop. E.5(T), (P). Step 2 isotony holds. Cor. 12.3 now has τ defined.

**Collateral checks**
- No remaining $W(f,h)$ with $f\ne0\ne h$, and no $\sigma_s$ or "Fock state" in the body.
- The notation table matches.
- The title notice, the introduction sentence and the Appendix B entry are accurate about the mathematics: counts of 4 MAJOR and 6 MINOR, no statement of a theorem changed. The exceptions are F-E and F-J.

**Numerical (corroboration only)**
- Script: `<scratch>/chk.py`; `/usr/local/opt/python@3.14/bin/python3.14 -I`, numpy 2.5.2, scipy 1.18.1, `quad` default tolerances.
- $C_M(sz)=C_m(z)=K_0(m|z|)/(2\pi)$ at $(m,s,z)\in\{(1,.5,.3),(2,3,1.7),(.7,1,.05)\}$: agreement to about $10^{-14}$ relative.
- $\|d_sf\|_M=\|f\|_m$ for a Gaussian $f$ at $(m,s)\in\{(1,.5),(2,3)\}$: agreement to about $10^{-16}$.

**Build log, read only.** `grep -cE '^!'`, `Overfull` and `-icE undefined` on `main.log` each print 0; 123 pages.

### 3. Status of F1–F10

| Finding | Status | How |
|---|---|---|
| F1 | closed | π₀ and H₀ defined (Def. E.3), identified with the sources (E.7) |
| F2 | partly closed | φ₀ now defined before use; Ω₀ still used at l. 360 (F-J) |
| F3 | closed | W(f,h) only for f = 0 or h = 0 |
| F4 | closed | U_s = U_{d_s}; action on both field halves and on the net proved without Weyl relations |
| F5 | closed | V identity from E.5(D); factor s explicit |
| F6 | closed | τ_a := Ad U_a; τ_a(𝔄(O)) = 𝔄(O+a) proved |
| F7 | closed | Θπ₀Θ = −π₀ proved |
| F8 | closed | l. 3388 reworded |
| F9 | closed | A6(i) states the inclusion |
| F10 | closed | mass superscripts in Remark 3.3 |

### 4. Not checked
- The quotations word for word (assigned to another auditor), and gj2-fock-04.
- Simon's Fourier normalisation in (II.46) and his definition of $\Delta_+$.
- The sources of A6(i)–(ii): GJ1 §III and GJExp Ch. 4.
- The proofs of §§`sec:filter`–`sec:lppl`, beyond the uses of τ and θ.
- The provenance claim that the four gaps predate 7 November.
- Whether $\Psi_\gamma$ as defined in `lem:rate` is the rate of item (1) beyond reading its definition.
- main.pdf (not opened); I did not rebuild.

**Files changed: none.** Commits: none. KB nodes: none. Scratch file only: `<scratch>/chk.py`.

---

## V5b, re-check of the fixes (11:33 UTC)

## V5b re-audit of `part_i/main.tex` (read-only; 8717 lines; build log 124 pages, 0 errors, 0 Overfull, 0 undefined)

**Outcome.** All fifteen findings F-A to F-O are closed. The new mathematics checks out by hand: the derivation in Remark 3.3, the core argument in Lemma E.1(ii) and the closure comparison in Lemma E.7(a)(2). Four new MINOR points remain; none is CRITICAL or MAJOR.

### 1. Status of F-A to F-O

| Finding | Status | Reason |
|---|---|---|
| F-A | closed | See "Remark 3.3" under section 3. |
| F-B | closed | Item (1) now states that the rate in original coordinates is $d\mapsto\Psi_{m_{1,*}}(sd)$, "not the function $\Psi_\gamma$ formed with the gap $\gamma=s\,m_{1,*}$". |
| F-C | closed | "Consequently" replaces "equivalently"; "one piece if $s\le1$" is added; the domain of each piece is cited from Prop. `prop:smoothing`. |
| F-D | closed | The Appendix E Conventions and the A1 Scope now say that A1(a)–(d) (Conventions: (a)–(g)) and Lemma N.19 hold for every mass and are used at $M_*$ (or $m'$). |
| F-E | closed | The appendix intro lists (a), (c), (d), (e), (f), Theorem I.6 for the realisation, and Lemma N.19. |
| F-F | closed | See "Lemma E.7(a)(2)" under section 3. |
| F-G | closed | See "Lemma E.1(ii)" and "Lemma E.7(b)" under section 3. The Fourier normalisation is now cited from Simon p. 27; the image simon-fourier-049 prints $(2\pi)^{-n/2}$, as cited. |
| F-H | closed | The Conventions paragraph states both Fourier normalisations and says only the kernel formula is taken from Appendix N. |
| F-I | closed | See "Rename" under section 3. |
| F-J | closed | l. 360 now says $\Omega_0\equiv1$, with a reference to §2.1. |
| F-K | closed | Lemma 2.8 and Remark E.6 now pass to the closure $K(g)$ for Θ. |
| F-L | closed | The display now reads $\lambda s^{-1}=s\lambda'$, which holds since $\lambda'=s^{-2}\lambda$; λ = 0 is no longer a problem. |
| F-M | closed | Lemma E.1(ii) and (iii) now state the extensions to $\mathcal K^{\mathbb C}$, and the proofs argue them (continuity, then complex linearity). |
| F-N | closed in (W.1) and Appendix E, one residue | (W.1) now says "for real $f_1,\dots,f_n$", and ll. 8416 and 8486 say $\mathcal S_{\mathbb R}(\mathbb R)$. The uniqueness sentence of A1(d), ll. 691–692, still reads "$f_j\in\mathcal S(\mathbb R)$" without "real" (N-1). |
| F-O | closed | The proof of Lemma E.4(iii) now says "formal variables" and "formal partial derivative". |

### 2. New findings (all MINOR)

**N-1. MINOR: A1(d), ll. 690–692.**
- Text: "…determined by its pairings with the Wick monomials with $f_j\in\mathcal S(\R)$, as the source's 'unique' in (V.3) asserts."
- Why: this is the F-N residue. The Wick monomials need real $f_j$.
- Repair: write $\mathcal S_{\mathbb R}(\mathbb R)$, or "real $f_j\in\mathcal S(\mathbb R)$".

**N-2. MINOR: A6 Scope (the new GJ1 sentence, diff ll. 167–172, near ll. 1030–1036 of the new file).**
- What GJ1 p. 1948 prints (I read gj1-propagation-04): (3.4), $e^{iH_0t}\mathfrak A(O)e^{-iH_0t}\subset\mathfrak A(O_t)$, with "$O_t$ … the region $O$ expanded by $t$". Here $\mathfrak A(O)$ is generated by the spectral projections of $\varphi(f)$, $\pi(f)$ with supp f ⊂ O, and the test functions are taken from $\mathcal S(\mathbb R^1)$ two paragraphs earlier.
- This does carry A6(i), via three facts:
  - such $f$ with $O$ bounded lie in $C_c^\infty(O)$;
  - spectral projections generate the same von Neumann algebra as the unitary groups (the "Equivalently" clause of §2.1);
  - Prop. 2.7 needs $O_r$ for every $r\ge0$, which (3.4) gives for $t\ge0$.
- Three readings are not recorded, though:
  - that GJ1's $\varphi$, $\pi$ and its Fock space are those of GJ2 (1.2.10)–(1.2.11). The Scope says "imported through the same unitary $\mathfrak D$", but $\mathfrak D$ is built on GJ2's objects;
  - that only real $f$ enter (GJ1 states essential self-adjointness "for real f");
  - for $t<0$ the text does say "read as $O$ expanded by $|t|$". It is a reading; the printed (3.3), with Δ vanishing outside the light cone for both signs of $t$, supports it.
- Repair: add one clause, "that GJ1's fields and Fock space are those of GJ2 (1.2.1)–(1.2.11), with real test functions, is a reading of the source, of the same kind as for item (iii)".

**N-3. MINOR: Lemma E.7(a)(2) (diff ll. 713–724).**
- Text: "the operator that the form defines on $\mathfrak D(N^{1/2})$ is therefore a restriction of $\varphi_{\mathcal F}(\theta)$".
- Why: the inference needs a definition of that operator, and the text gives none. The natural one is: the vector $X\psi$ with $\langle\chi,X\psi\rangle=$ form$(\chi,\psi)$ for $\chi\in\mathfrak S$, obtained by continuity in the $N^{1/2}$-graph norm.
- It also needs that both $X$ and $\varphi_{\mathcal F}(\theta)$ are continuous in that norm. The displayed bounds give this for $\varphi_{\mathcal F}$, and it holds for $X$ by the same bounds.
- The conclusion is correct; one sentence is missing.
- Repair: add "(the form being continuous on $\mathfrak S\times\mathfrak S$ in the norm of $(N+1)^{1/2}$ in its second argument, by the same bounds)".

**N-4. MINOR: title-page notice, ll. 149–151.**
- Text: "The repair was audited on 11 November 2026 by two agents … and their findings were applied and re-checked (rounds V5 and V5b; `part_i/README.md`)."
- Why: when this was written, V5b was still running (this report is V5b). `/usr/bin/grep -n V5 part_i/README.md` returns nothing, so the cited record does not yet contain these rounds.
- Repair: update README before relying on the sentence, and state the V5b outcome (closed, with the residues above).

### 3. Checked and found correct

**Remark 3.3** (the new derivation, step by step)
- $E^{(m_0)}=sE^{(M_*)}$, so $U_sHU_s^*=sH'$.
- The β intertwining, through $U_se^{itH}U_s^*=e^{istH'}$.
- The α intertwining. A cutoff $g\in\mathcal G$ with $g\equiv1$ on $O_{|t|}$ exists, including $t=0$; $s\,O_{|t|}=(sO)_{s|t|}$; (P) is used for both models; the extension to $\mathfrak A$ is by density and isometry.
- $\omega^{(m_0)}_\infty$ is defined by transport.
- Item (1): equality of the local norms; the rate $\Psi_{m_{1,*}}(sd)$; convergence of the net through the order isomorphism.
- Item (2): $\mathrm{Ad}\,U_s$ is spatial, hence normal.
- Item (3), against the definition in Prop. 12.1 (l. 2976ff., $\check f(E)=\int f(t)e^{itE}\,dt$):
  - $\int f(t)F(st)\,dt=\int f_s(u)F(u)\,du$ with $f_s=s^{-1}f(\cdot/s)\in L^1$;
  - $\check f_s(E)=\check f(sE)$, which vanishes on $[0,\infty)$ because $s>0$;
  - invariance, continuity and boundedness transport.
- Item (4): $U_sU_aU_s^*=U'_{sa}$ and $U_s\Theta U_s^*=\Theta'$.
- Item (5): $\mathrm{spec}\,H=s\cdot\mathrm{spec}\,H'$; dim ker = 1; $\|V_{m_0,\lambda}(h)\Omega_g\|=s\|V'(h(\cdot/s))\Omega'_{g'}\|\le sM$; at most ⌈s⌉+1 pieces.

**Lemma E.1(ii): the core argument**
- The maximal multiplication operator by $\mu_m(\cdot)$ on $L^2_{\rm r}$ is closed and symmetric, with a bounded inverse $\le m^{-1}$ that preserves $L^2_{\rm r}$. Hence it is self-adjoint in the real space and bounded below by $m$.
- $\mathbf 1_{[-n,n]}\theta$ lies in $L^2_{\rm r}$ because the indicator is even, and it converges in graph norm by dominated convergence.
- An even real mollifier preserves the symmetry $\theta(-k)=\overline{\theta(k)}$; I checked $(\theta*\rho)(-k)=\overline{(\theta*\rho)(k)}$.
- The supports stay in $[-n-1,n+1]$, where $\mu$ is bounded, so $L^2$ convergence gives graph convergence.
- $C_c^\infty\cap L^2_{\rm r}\subseteq j(\mathcal S_{\mathbb R})$, and the transport by $j$ is correct.

**Lemma E.7(a)(2): the closure comparison**
- The components $A^*(\theta)\psi_n$ are mutually orthogonal (different particle numbers), as are the $A(\theta)\psi_n$.
- The bounds $(n+1)\|\theta\|^2$ and $n\|\theta\|^2$ hold.
- The truncations of $\psi\in D(N^{1/2})$ are Cauchy in the graph norm, so $D(N^{1/2})\subseteq D(\varphi_{\mathcal F}(\theta))$.
- The closures coincide, modulo N-3.

**Lemma E.7(b)**
- The source's μ ((II.47), the closure from $\mathcal S$) equals $\mu^{\mathbb C}|_{\mathcal K}$, by E.1(ii).
- The sign of the convention $e^{-tT}$ is consistent with Example 3 / (I.41).
- The use of Hille–Yosida is correct.

**Rename.** In Appendix E, ll. 7960–8640, no bare $M$ remains as a mass (the only hits are $\mathcal M$). The search `mu_M`, `C_M`, `V_{M,`, `K_{M,`, `\mathcal K_M` returns nothing. Remark 3.3 uses $m'=M_*$ consistently, keeps $M$ for the moment constant, and has the superscripts $(m_0)$/$(M_*)$ name models. Remark E.6 says $K_{m',\lambda'}$. $J$ is now $\Upsilon$ everywhere it occurs (ll. 8513–8594). The source's vacuum is named $\Omega_{\mathcal F}$ in E.7(a)(1). The note separating $N$ from $N_I$ is present.

**Prop. E.5(D)** after the rename: every display is consistent, and I redid the λ' step.

**A1 Scope.** The realisation and Theorem I.6 sentence, and the statement that Simon's $\mathcal H_C$ is not the record's $\mathcal H_C$, are accurate.

**Remaining edits.** Corollary 12.3 now names $\tau=\mathrm{Ad}\,U$ of Prop. E.5(T); the A7 Scope is reworded; and the Appendix B entry (iii) is reworded and matches the uses in Theorem 12.2(4), Corollary 12.3 and Theorem 13.2.

**Checks actually run.**
- `/usr/bin/grep -cE '^!'`, `-c Overfull` and `-icE undefined` on `part_i/main.log` (11 Nov 11:30) each print 0; the log says "Output written on main.pdf (124 pages)".
- `grep -c ''` on main.tex prints 8717.

### 4. Not checked
- The quotations word for word, apart from the two new page images I read: gj1-propagation-04 and simon-fourier-049.
- Whether GJ1's free-field conventions match GJ2's (N-2).
- The diff outside the hunks listed in v1-to-v3.diff.
- main.pdf (not opened); I did not rebuild.
- The README content beyond the grep for "V5".

Files changed: none. No commits, no KB nodes, and no new scratch files this round.

---

## V5c, check of the last edits (11:38 UTC)

## V5c: check of the last edits (v3-to-v5.diff, 115 lines; read-only)

**Outcome.** N-1, N-2 and N-3 are closed. The new sentences in Remark 3.3 and in the introduction are mathematically accurate. The 115 lines contain two new MINOR points and nothing more serious.

**N-1: closed.** The uniqueness sentence of A1(d) now reads "Wick monomials with real $f_j\in\mathcal S(\mathbb R)$" (diff ll. 29–30).

**N-2: closed.** A6's Scope (diff ll. 39–42) now records as a reading of the source that the fields and the Fock space of GJ1 are those of GJ2 (1.2.1)–(1.2.11), with real test functions, "of the same kind as for item (iii)".

**N-3: closed.** Checks of Lemma E.7(a)(2) (diff ll. 101–112):
- $\|T\psi\|\le 2^{-1/2}(\|A^*\psi\|+\|A\psi\|)\le\sqrt2\,\|\theta\|\,\|(N+1)^{1/2}\psi\|$ holds on $\mathcal F_{\rm fin}$.
- The truncations of $\psi$ are Cauchy in the graph norm, so $D(N^{1/2})\subseteq D(\varphi_{\mathcal F}(\theta))$.
- The extended form equals $\langle\chi,\varphi_{\mathcal F}(\theta)\psi\rangle$, so $X$ is the restriction of $\varphi_{\mathcal F}(\theta)$ to $D(N^{1/2})$, and its closure is $\varphi_{\mathcal F}(\theta)$.

**Remark 3.3 (diff ll. 49–64): accurate.**
- Item (5) gives the gap as $s\,m_{1,*}$ and names it as the $m_1$ at the end of the proof of Proposition 3.2. That matches the sentence there: "the rate in the original coordinates is $m_1:=s\,m_{1,*}$".
- The closing sentence says that the working coordinates have $s=1$, i.e. $m_0=M_*$, so $m_1=m_{1,*}$. For a general pair $(m_0,\lambda)$ it gives the rate $d\mapsto\Psi_{m_{1,*}}(sd)$ and the gap $s\,m_{1,*}$. Both agree with items (1) and (5). The moment constant is covered separately by item (5).

**Introduction (diff ll. 17–19): accurate.** It says that $\Psi_{m_1}$ and $m_1$ are stated in the working coordinates of §2.2 and points to Remark 3.3 for a general pair.

**Lemma E.4(iii) and Appendix B (diff ll. 72–75, 85–87):** the rewording is consistent with what A1(a) quotes.

**New findings, both MINOR:**

- **V5c-1. Lemma E.7(a)(2), diff ll. 106–108.**
  - Text: "the form … being continuous in $\psi$ for the norm $\|(N+1)^{1/2}\psi\|$, extends to $\mathfrak S\times\mathfrak D(N^{1/2})$".
  - Why: extending by continuity also needs $\mathfrak S$ to be dense in $D(N^{1/2})$ for that norm. This is true: truncate, then approximate each component by symmetric Schwartz functions, since the norm is equivalent to the $L^2$ norm on each $\mathcal F_n$. The text does not say it.
  - Repair: add "($\mathfrak S$ is dense in $\mathfrak D(N^{1/2})$ for this norm: truncate, then approximate each $\psi_n$ in $\mathcal F_n$)".

- **V5c-2. Notation, Lemma E.7.**
  - $T$ is introduced in (a)(2) for $2^{-1/2}(A^*(\theta)+A(\theta))$. In (b) of the same lemma and proof, $T$ is the closure of $d\Gamma(\mu)$, and in Lemma E.4 it is the orthogonal bijection.
  - Nothing is mathematically affected.
  - Repair: rename the operator in (a)(2), e.g. to $X_\theta$.

**Checks run:** I read the diff file in full and redid the bound above by hand. I did not rebuild and did not open main.pdf.

**Not checked:** the README gate record, which per the coordinator will change in the same commit; and anything outside these 115 lines.

Files changed: none.

---

## V5d, check of the two remaining points (11:39 UTC)

V5d: both points are closed. I read the whole of v5-to-v6.diff and found nothing new in those lines. Everything was read-only; no files were changed.

- **V5c-1: closed.** The proof of Lemma E.7(a)(2) now says that 𝔖 is dense in D(N^{1/2}) for the norm ‖(N+1)^{1/2}ψ‖ (truncate, then approximate each ψ_n in F_n by symmetric Schwartz functions). It says this before it extends the form, which makes the extension by continuity valid. The steps after it are unchanged and still hold.
- **V5c-2: closed.** The operator on finite-particle vectors is now R_θ, and the closure of dΓ(μ) in (b) is now Z. The Z-argument still reads correctly after the rename: Z+1 onto, H_0+1 injective, hence H_0 = Z. A search of lines 8520–8660 of `part_i/main.tex` finds no standalone T left, so in that part T now means only the orthogonal bijection of Lemma E.4.

I did not rebuild the PDF; the build counts (0 errors, 0 Overfull, 0 undefined) are the ones you reported.
