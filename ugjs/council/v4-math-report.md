# Round V4 and its re-checks V4b–V4e: mathematics of the integration (7 November 2026)

One agent (general-purpose, model claude-opus-5-5) that had written none of the audited text. It audited the mathematics of the new and repaired parts of `part_i/main.tex` after the integration of Appendix D, and was sent the orchestrator's fixes four more times. Five reports, in the order returned.

Returned by the agent as a message, not as a file. Saved here on 11 November 2026 by the orchestrator from the session transcript. The text is verbatim except that paths under the home directory and under the session's temporary folder are replaced: `<scratch>/` is that temporary folder, which was emptied on 10 November 2026, and paths inside this repository are written relative to its root.

---

## V4 (returned 2026-11-07 21:23 UTC)

## (1) Verdict

The new mathematics in the five audited parts is correct. I re-derived by hand every display, constant and threshold in Appendix C: the notation paragraph, Lemmas C.2–C.4 and Theorem C.5, including (C.a)–(C.c), C_*, C(𝒫), C_{p'}, b(𝒫), c_1, A_n, L_m, B_n, c_2, b_0', b_1, b_2(p) and b_*. I did the same for Lemma N.19(iii),(v) and Lemma N.23' with (W.4). I found no false display, no wrong constant and no CRITICAL gap. All boundary cases hold: κ=2, κ∈[2,4), n=1, p'=1, λ=0, |Λ|=0, c_2=0, R<a and n=0.

I checked every Simon quotation against the page image and each one is verbatim. Every import is used inside its printed hypotheses:
- V.2(a): h∈C_E is bounded with compact support.
- V.2(b): h∈L¹∩L² ⊂ L^{1+ε} with ε=1.
- V.7(a): g=h≥0, h∈L¹∩L^{1+ε}(R²), and P=ϱλ𝒫 is semibounded.
- I.17: p=2≤q<∞.
- I.22: stated for q>2; at q=2 the inequality is trivial.

There is one MAJOR gap, inherited from the formal-integral text. §2.1 asserts with no argument that V(h) is affiliated with A(U), and that property is load-bearing. There are ten MINOR items. All V3 items M-1..M-3 and m-1..m-9 are closed.

## (2) Items

| Item (locator, current file) | Verdict |
|---|---|
| §2.1 definition V(h)=λΣa_n:φ_0^n(h):_C (l. 436–445) | holds. Well defined by A1(d). Reality follows from uniqueness, since the conjugate has the same real pairings. |
| §2.1 "self-adjoint multiplication operator" (l. 445–446) | holds |
| §2.1 "affiliated with A(U) for every bounded open U⊇supp h" (l. 446–447) | **gap MAJOR (F1)** |
| §2.1 finite additivity "since h↦:φ_0^n(h):_C is linear" (l. 447–449) | holds: uniqueness plus linearity of the right side of (W.1) |
| §2.1 "N.23' proves … L²-limit of the mollified Wick powers" (l. 451–454) | gap MINOR (F2: bounded h only); φ_κ is undefined at that point (F10) |
| A1(a) quotes p.12, (I.15), (I.18a), (I.18b) p.10 (l. 548–556) | holds, verbatim |
| A1(b) Thm I.3 (I.21) p.11; Cor I.4 (I.23a) p.12 (l. 557–560) | holds (F11: "jointly" missing, MINOR) |
| A1(c) Γ_n quote p.17, read as the closed span (l. 561–564) | holds; locator MINOR (F9) |
| A1: "Gaussian random process indexed by H_C", S=C as "kernel of ⟨·,C·⟩" (l. 542–546, 569–570) | gap MINOR (F3: Simon's ½ convention) |
| A1(d)/(W.1) quote of (V.3) p.136 with its [sic] (l. 565–576) | holds as a quotation. Its use as the definition for g∈L^{1+ε} is gap MINOR (F4). |
| A1 V.2(b) quote p.138; isometry quote p.137; "L¹∩L²⊂L^{1+ε}" (l. 577–582) | holds |
| A1 Scope: "printed for any H whose kernel S is locally integrable [Def. p.135]" (l. 593–596) | gap MINOR (F9: one hypothesis of the Definition omitted; it holds) |
| A1 Scope: "for the class L¹∩L² … constructed … (N.23'), so nothing below rests on that reading alone" (l. 598–601) | gap MINOR (F2) |
| A3 construction: H_G, (W.2), V.2(a) quote, (W.3), (V.6a) and Remark 1, U_h ∈ ⊕Γ_n and in every L^p, (I.32) with Γ(e^{-t}1)=e^{-nt} on Γ_n (l. 654–692) | holds (F3 and F4 apply as for A1) |
| A3 Source: V.7(a) quote and its hypotheses (l. 694–702) | holds. Observation: Theorem C.5, whose proof does not use this clause, already gives e^{-ϱ𝒰_h}∈L¹, so the import is redundant (not a defect). |
| A3 Scope (l. 704–712) | holds; the readings are named as readings |
| A4 Sources: I.22 quote p.38 (l. 734–739) | holds, verbatim |
| A4 Scope: I.17 printed for p,q∈(1,∞), p≤q (l. 743–744) | holds |
| A4 Scope: "every use below has 2≤p≤q<∞" (l. 744–745) | gap MINOR (F6) |
| App C: heat-kernel formula for G; positive, radial, nonincreasing; ∫G=m_0^{-2} (l. 3282–3289) | holds |
| (C.a) via N.19(iii),(v) (l. 3290–3296) | holds |
| K_0 identity (l. 3296–3298, not used) | holds: t=(r/2m)e^u gives m²t+r²/4t = mr cosh u |
| (C.b) with differentiation under the integral (l. 3299–3314) | holds. The constant is sharp, since xK_1(x)→1. |
| R=diam Λ, \|Λ\|≤πR² (l. 3315–3316) | holds |
| δ, δ_κ, ‖δ‖_∞≥1/π, Φ_κ smooth in z (l. 3321–3336) | holds |
| c_κ formula and independence of z (l. 3337–3340) | holds |
| (C.c) and C_*=(b_0+π‖δ‖_∞)/(4π), κ≥2 (l. 3341–3355) | holds. Re-derived: 4πc_κ ≤ b_0+2log κ+2·(π/2)‖δ‖_∞. |
| He_n and :y^n:_c, including c=0 (l. 3355–3365) | holds |
| 𝒰_{h,κ} defined pointwise; X_{n,κ}∈Γ_n equals the Bochner integral (l. 3366–3376) | holds (N.23'(i)) |
| Lemma C.2 and proof (l. 3380–3398) | holds |
| Lemma C.3: C(𝒫), C_{p'}, b(𝒫), the polynomial bound (l. 3403–3445) | holds. Young's inequality re-derived, (2p'−1)·A/(4p') ≤ A/2. Hand tests: p'=1, x²−c ≥ −2(1+c); and :x⁴:_c with C(𝒫)=6, C_2=54. |
| Lemma C.3 second display and c_1 (l. 3411–3423, 3445–3450) | holds. The sentence "max with 1 only makes c_1 positive" is MINOR (F7). |
| Lemma C.4: A_n, L_m, B_n, c_2 (l. 3456–3473) | holds |
| C.4 Step 1, chaos decomposition, isometry, cross term via (W.2) (l. 3477–3505) | holds |
| C.4 Step 2 (J1) (l. 3510–3518) | holds: ∫_{B(0,a)}G ≤ (a²/4)(b_0+1+2log(1/a)); the difference (b_0+2)(1+log κ)−… equals 1+b_0 log κ |
| (J2), (J3) (l. 3519–3526) | holds: the segment stays in {\|ξ\|≥\|ζ\|/2}, where \|∇G\| ≤ 1/(π\|ζ\|) |
| C.4 Step 3, both cases κ≥4 and 2≤κ<4 (l. 3528–3544) | holds. The r=ae^{-s} sum is re-derived; A_n totals exactly. |
| C.4 Step 4 (l. 3546–3554) | holds: 2π·3n·(2/πκ) = 12n/κ |
| C.4 Step 5 and its tests (l. 3556–3564) | holds |
| Theorem C.5: comparison from I.17 and (I.32) (l. 3586–3599) | holds |
| C.5 thresholds b_0', b_1, f, f', b_2(p), b_* (l. 3601–3616) | holds: f'(b) = b^{-1}[(4p'²)^{-1}(b/2c_1)^{1/p'}−1] |
| C.5 chain: κ≥2^{4p'}, 2q≥2, Chebyshev, bracket = (√c_2/c_1)e^{-L/4} ≤ e^{-1} using c_1≥1, tail ≤ e^{-2pb} (l. 3618–3640) | holds |
| C.5 layer cake ≤ e^{pb_*}+1 (l. 3641–3647) | holds (b_*>0; p>0 is implicit) |
| C.5 claim "depends on Λ only through \|Λ\|, diam Λ, monotonically" (l. 3576–3579, 3647–3653) | holds: b_2 is nondecreasing in c_1, because f decreases and its lower endpoint increases |
| Sentence after the proof (l. 3656–3658) | holds (for q<2 use ‖·‖_q ≤ ‖·‖_2) |
| Symbol collisions b_1, c_1/c_2 vs c_κ | MINOR (F8) |
| N.19(iii) (l. 4557, proof l. 4615–4628) | holds |
| N.19(v) (l. 4563–4568, proof l. 4640–4649) | holds |
| N.23' statement, including ∫S=(2m_0)^{-1} resp. m_0^{-2} (l. 4964–4978) | holds |
| N.23'(i) (l. 4980–4983, 5000–5022) | holds |
| N.23'(ii): (W.4) and the limit of the pairings (l. 5024–5068) | holds. Hand tests: n=1, and n=2 with A_1=A_2=X. |
| N.23'(ii) uniqueness sentence (l. 5069–5071) | gap MINOR (F4) |
| N.23'(ii) parenthetical "(which holds: …)" (l. 4984–4986) | gap MINOR (F5) |
| N.23'(iii) (l. 4990–4995, 5073–5081) | holds |

## (3) Findings

**F1 — MAJOR (inherited, exposed by the new definition).**
- **Locator:** l. 446–447.
- **Text:** "it is affiliated with $\A(U)$ for every bounded open $U\supseteq\supp h$".
- **Why it fails:** V(h) is now the element of ⊕Γ_n fixed by the pairings (W.1). Nothing in §2.1, A1 or Appendix D shows that this element is measurable with respect to the fields localized in U. The property is load-bearing:
  - Prop. propagation (l. 1176–1180): "e^{itV(χg)}∈A(O)".
  - Lemma tworegime (l. 2458–2459): "X=V_j (affiliated with every A(U) … by §2.1)".
  - The overview (l. 268) lists "+affiliation+".
  - A grep for "affiliat" finds no proof elsewhere.
- **Repair (a few lines; every use has bounded h, e.g. h_j=η_jv):**
  1. By N.23'(iii), with N.20(iii) after scaling and splitting into length-2 pieces, :φ_0^n(h):_C is the L²-limit of W_{n,κ}(h)=∫h:φ_κ^n:dx.
  2. For κ > 1/dist(supp h, R∖U), every test function ρ_κ(x−·), x∈supp h, is supported in U. So W_{n,κ}(h) is measurable for Σ_U := σ{φ_0(f): f∈C_c^∞(U)}.
  3. L²(Σ_U) is closed, so the limit is Σ_U-measurable.
  4. A real Σ_U-measurable multiplication operator is affiliated with {e^{iφ_0(f)}: f∈C_c^∞(U)}'' ⊆ A(U).
  5. For unbounded h, either restrict the claim, or approximate by truncations using the isometry.

**F2 — MINOR.**
- **Locator:** l. 598–601, "for the class $L^1\cap L^2$ with compact support the same element is constructed in this manuscript as an explicit $L^2(d\phi_0)$-limit (Lemma~\ref{aux:notation-ident}), so nothing below rests on that reading alone". Also l. 451–454.
- **Why it fails:** N.23' assumes w bounded, and the convergence it cites (N.20(iii)) needs ‖w‖_∞≤1, support in an interval of length 2, and n≤2p'. Example: h=|x|^{-1/3}1_{[-1,1]} lies in L¹∩L² with compact support and is not covered. For such h, existence rests on V.2(b) under the φ_F reading alone. Every use below has bounded h, so no conclusion is affected.
- **Repair:** say "bounded h of compact support". Alternatively, extend N.20/N.23' to w∈L²(R) of compact support: the d=1 dominator |w(x)||w(y)|(b_0+2+2|log|x−y||)^n is integrable by Young's inequality.

**F3 — MINOR (convention).**
- **Locator:** l. 542–546 ("completing … in the norm ⟨f,Cf⟩^{1/2}. Q-space … is the Gaussian random process indexed by H_C … E[φ_0(f)φ_0(g)]=⟨f,Cg⟩"), l. 569–570 ("the kernel S(x,y)=C(x−y) of ⟨·,C·⟩"), and l. 655–659 (H_G).
- **Why it fails:** Simon's Definition on p.15 says "(c) ⟨φ(v)φ(w)⟩ = ½⟨v,w⟩", and his (V.1) on p.134 reads "½⟨f,g⟩_H = S(f⊗g)". In Simon's convention, the process indexed by H_C as normed here would have covariance ½⟨f,Cg⟩. The process φ_0 is indexed by the space with inner product 2⟨f,Cg⟩. S is still the covariance kernel C, so (W.1), (W.2), (I.21), (I.32), I.17 and I.22 are all unaffected.
- **Repair:** one clause recording Simon's ½ normalisation (p.15, Remark 1).

**F4 — MINOR.**
- **Locator:** A1(d), l. 565–570, "For g∈L^{1+ε}(R) … is 'the unique random variable in Γ_m(H) with …' [(V.3)]"; A3, l. 661–669; N.23'(ii), l. 5069–5070, "two elements of the closed span Γ_n(H) with the same inner products against every spanning vector coincide".
- **Why it fails:**
  - Simon prints (V.3) for g∈𝒮 (p.135–136). "Exists for X" means that the map g↦:φ^m(g): extends from 𝒮. Reading (V.3) as the characterisation for g∈L^{1+ε} needs two facts: the extension is continuous in ‖·‖_{1+ε} ((V.6a/b) at p=2), and the right side is continuous in g (\|Sf_j\| ≤ ‖f_j‖_∞‖S‖_1).
  - Γ_n(H) is spanned with f_j∈H, but only monomials with f_j∈𝒮 are tested. That these are total needs either the import (Simon's "unique" asserts exactly this, independently of g) or the multilinear L²-continuity of Wick monomials.
- **Repair:** add both remarks, and cite the import for uniqueness in N.23'(ii).

**F5 — MINOR.**
- **Locator:** l. 4984–4986, "(which holds: for d=1 and ν=ρ by Lemma N.20(iii); for d=2 and ν=δ by Lemma N.28(a) with r=1)".
- **Why it fails:** N.20 covers 0≤n≤2p', ‖w‖_∞≤1 and supp w ⊆ [a,a+2]. N.28 covers n<n̄=2p'+1 and kernels vanishing outside one GJS square. The lemma is stated for all n≥0 and all bounded w of compact support. General w follows by linearity and scaling, which is unstated; n>2p' is not covered as cited.
- **Repair:** restrict to n≤2p' and add "by linearity in w". Only n≤2p' is used.

**F6 — MINOR.**
- **Locator:** l. 744–745, "every use below has 2≤p≤q<∞".
- **Why it fails:** the first use listed under "Used in", §path Step 1 (l. 2088–2093), has p_T=1+e^{-m_0T}∈(1,2). That use is inside Simon's printed range and the display's range 1<p≤q<∞, so nothing is affected, but the sentence is false as written.
- **Repair:** write "1<p≤q<∞ (§path: p=1+e^{-m_0T}; Appendices C, D: p=2)".

**F7 — MINOR (exposition).**
- **Locator:** l. 3422–3423, "the maximum with 1 only makes c_1 positive, as the proof of Theorem C.5 needs".
- **Why it fails:** Theorem C.5 uses c_1≥1 (l. 3632, "(as c_1≥1)") in the b_1 step, not merely c_1>0.
- **Repair:** say "makes c_1≥1".

**F8 — MINOR (notation).**
- b_1 is the threshold of Theorem C.5 (l. 3606) and also the kernel constant of N.25(iii) (l. 5236).
- The constants c_1, c_2 (l. 3418, 3462) collide with the variance c_κ (l. 3338) at κ=1,2. This was inherited from HEAD.

**F9 — MINOR (locators and bookkeeping).**
- l. 546: the uniqueness of the process is Theorem I.6 on p.15; pp.16–17 contain its proof.
- l. 563: "read here as the closed span" — p.16 prints "Let Γ_n(H) be the closed subspaces generated by …".
- The Sources line (l. 586–587) omits p.15/16.
- l. 593–596: facts (a)–(c) are Chapter I statements, not printed under the Definition of p.135. That Definition also requires "𝒮_R(R^n) as a dense continuously imbedded subspace", which is not listed. It holds, since ⟨f,Cf⟩ ≤ ‖f‖²/(2m_0) and C, G are strictly positive.
- A1 "Used in" (l. 606–609) omits §2.1, Appendix C (Lemma C.2 cites A1(c)) and Appendix D (N.20, N.23').

**F10 — MINOR.**
- **Locator:** l. 453, "∫h(x):φ_κ(x)^n:dx".
- **Why it fails:** φ_κ is defined only at l. 4666–4668 (AGENTS 3.8).
- **Repair:** add "(φ_κ as in Appendix D)".

**F11 — MINOR.**
- **Locator:** l. 557, "for Gaussian random variables f,g".
- **Why it fails:** Theorem I.3 needs f, g jointly Gaussian; its proof uses that af+βg is Gaussian, and Simon p.8 distinguishes "g.r.v." from "jointly Gaussian". Every use here is inside one Gaussian process, so nothing is affected.
- **Repair:** write "jointly Gaussian".

## (4) V3 items

| Item | Status | Where it is closed |
|---|---|---|
| M-1 | closed | (C.a) through N.19(iii),(v); (C.b) derived from the heat kernel; (J1)–(J3) derived; K_0 defined (unused) |
| M-2 | closed | (C.c) derived, with explicit C_* |
| M-3 | closed | A1(a)–(d); A3 construction paragraph; N.23'(i); C.2, C.4 Step 1 and C.5 now cite them. F3 and F4 remain as MINOR residue. |
| m-1 | closed | l. 3376–3378, 3656–3658 |
| m-2 | closed | l. 3355–3365 |
| m-3 | closed | l. 3393, 3446–3448, 3502; Remark C.6 |
| m-4 | closed | l. 3421–3423, 3471–3473, 3576–3579 |
| m-5 | closed | l. 3601–3647 |
| m-6 | closed | c_1≥1; λ=0 and \|Λ\|=0 handled separately |
| m-7 | closed | p,q range now stated; (I.32) moved to A3; I.22 cited. F6 is new. |
| m-8 | closed | N.23'(i) |
| m-9 | closed | l. 694 |

The deviations from the V3 repair texts are all valid:
- The gradient bound replacing R3 is valid and sharp.
- C_* replacing R6 is valid for κ≥2, which is the only range used; R6 claimed κ≥1.
- b_1 is at least R10's b_1, because c_1≥1.

## (5) Not checked, and checks run

**Not checked:**
- The proofs of Simon's Theorems I.3, I.6, I.17, I.22, V.2 and V.7 (I read the statements only).
- Whether Simon's φ_F has covariance C (the manuscript itself declares this unchecked).
- Whether V.7's ∫g:P(φ): is built from (V.3); pp. 139–150 not read.
- The GJS and Fock-space readings.
- N.13, N.20, N.25 and N.28: read as inputs, not audited line by line. N.19(i) and (iv) not checked; (ii) was checked only as the argument that (v) reuses.
- Downstream consumers (the S_2 proposition, §§slab and path), except the p_T range noted in F6.
- The dossier images. I rendered the pages from the PDF in refs/ instead.

**Build:** I compiled a copy of main.tex (sha256 prefix 8fab2c791e2fd40f, mtime 7 Nov 21:51:50) three times with /Library/TeX/texbin/pdflatex in <scratch>/audit-math/build.
- `^!` count 0, Overfull 0, undefined 0, LaTeX Warnings 0.
- The pdftotext grep for ??, TODO, Hmm and "wait," found nothing.
- 109 pages.
- Numbering from that build's .aux: A1 p.9, W.1 p.9, A3 p.10, W.2 p.10, W.3 p.11, A4 p.11, App C p.44, C.a and C.b p.46, C.c, C.2 and C.3 p.47, C.4 p.48, C.5 p.50, N.19 p.63, N.23' p.70, W.4 p.71. Printed page equals PDF page in this build.

**Simon page images viewed** (150 dpi, PDF page = printed page + 22): printed pp. 8, 9, 10, 11, 12, 14, 15, 16, 17, 24, 25, 34, 38, 134, 135, 136, 137, 138, 151, 152.

**Numerics** (numerical only; nothing is deduced from them). Environment: /usr/local/bin/python3 3.14.7, numpy 2.5.2, scipy 1.18.1, tolerance 1e-12, seed 20261107. Results:
- (C.a) holds on 4000 log-spaced points r∈[1e-10,100] for m∈{0.2,0.5,1,3,10}; minimum margin 0.14. The heat-kernel integral equals K_0/2π to 12 digits.
- (C.b) holds; the maximum ratio is 1.000000000000000.
- (C.c) holds for bump mollifiers with s∈{1,0.5,0.2}, m∈{0.3,1,3} and κ from 2 to 1e5. The slope 1/2π is attained. An independent position-space value of c_2 is 0.231395, against 0.231398 from the Fourier computation.
- The polynomial bound of Lemma C.3 holds on 60 random polynomials; the minimum relative margin is 0.64.
- The Step 3 integral inequality holds for n=1..8.
- (J1) and (J2) hold at κ∈{2,6,20}.
- Lemma C.4 end to end at n=1, with h the indicator of the unit disc, holds with ratio ≤ 5e-6.
- The threshold chain of Theorem C.5 holds on [b_*, 20b_*] for 5 parameter sets.
- The first (C.c) run in check_appC.py truncated the integration grid and is superseded by check_ckappa.py.

Files are in <scratch>/audit-math/scripts:
- check_appC.py (output check_appC.output.txt)
- check_uv_n1.py (output check_uv_n1.output.txt)
- check_ckappa.py (output check_ckappa.output.txt)

I modified no file in the workspace.

---

## V4b, re-check of the fixes (21:40 UTC)

## V4b re-check of the F1–F11 fixes in part_i/main.tex

**Object checked.** The working file as of mtime 7 Nov 22:31:32 (sha256 prefix 57096fa200f8640d, 7728 lines). I diffed it against my V4 copy and read every edited passage named in your message.

**Verdict.** The Locality proof is complete and correct for the statement it makes. F1–F11 are closed. The edits introduce six MINOR items (N1–N6) and no MAJOR or CRITICAL defect. N1 is the one that matters most: restricting the claim to intervals means two existing consumers of the affiliation are no longer literally covered by it. The proof already covers them; one sentence is missing.

### (1) Locality proof (l. 447–449, 461–484): holds

I checked each step and the hypothesis it uses.

1. **Bounded h.** Split h into pieces supported in intervals of length 2 and scale each to ‖·‖_∞ ≤ 1. Each piece then meets the hypotheses of N.20(iii) (supp ⊆ [a,a+2], n ≤ 2p'). N.23'(iii) identifies each limit with :φ_0^n:. Linearity in h, which follows from uniqueness, gives W_{n,κ}(h) → :φ_0^n(h):_C.
2. **Choice of κ.** For κ > 1/dist(supp h, ℝ∖U), each ρ_κ(x−·) with x ∈ supp h has support in [x−1/κ, x+1/κ], a compact subset of U, so it lies in C_c^∞(U). The integrand h(x):φ_κ(x)^n: is Σ_U-measurable, or zero where h = 0.
3. **Closure.** By N.23'(i) the pointwise integral equals the Bochner integral, and a Bochner integral of a function valued in the closed subspace L²(Σ_U) stays in that subspace. L²-limits stay in it as well.
4. **Unbounded h.** Write h_N = h·1_{|h|≤N}. Then :φ^n(h) − φ^n(h_N): = :φ^n(h−h_N):, and (V.6b) at p = 2, ε = 1 gives ‖·‖_2 ≤ c‖h−h_N‖_2. Dominated convergence (|h−h_N| ≤ |h| ∈ L²) sends this to 0. The text says this case rests on the φ_F reading.
5. **M_U ⊆ A(U).** M_U = {W(f,0) : f ∈ C_c^∞(U)}'' ⊆ A(U) holds because U is a bounded open interval, the only sets for which A(·) is defined (l. 437).
6. **Functional calculus.** W(tf_j,0) = e^{itφ_0(f_j)}, so bounded Borel functions of the strongly commuting φ_0(f_j) lie in M_U.
7. **Monotone class.** Cylinder sets form an algebra generating Σ_U. M_U is strongly closed, so the class {E : 1_E ∈ M_U} is monotone and therefore contains Σ_U. Bounded Σ_U-measurable functions follow by uniform approximation (unstated, immediate).
8. **Affiliation.** The spectral projections of V(h) are 1_{v⁻¹(B)} with v⁻¹(B) ∈ Σ_U, so V(h) is affiliated with A(U).

### (2) F2–F11

| Item | Verdict |
|---|---|
| F2 (l. 453–459, 649–652) | closed; residual nit N6 |
| F3 (l. 574–582, 606–609, 712–717) | closed. 2⟨f,Cf⟩ ≤ ‖f‖²/m_0 is correct since ‖C‖ = 1/(2m_0). The quotes of p.15(c) and (V.1) p.134 are verbatim on the images. H_G's analogue, 2⟨f,Gf⟩ ≤ 2‖f‖²/m_0², is left implicit ("as for H_C"). |
| F4 (l. 616–629, 728–729, 5157–5159) | closed. The quotes of (V.6b) p.138 and of the "extends to a larger test function space" sentence p.136 are verbatim. The continuity argument is right for n ≥ 1, and uniqueness is now cited to the source's "unique". Residual nit N2. |
| F5 (l. 5070–5074) | closed |
| F6 (l. 804–807) | closed. §path has p_T = 1+e^{−m_0T} and p_T' = 1+e^{m_0T} < ∞. |
| F7 (l. 3504–3505) | closed |
| F8 (l. 3458–3460, 3698–3700) | closed |
| F9 (l. 582, 598–600, 635–636, 642–646, 657–662) | closed. Thm I.6 is on p.15 and "closed subspaces generated by" is on p.16 (images checked). The Definition's hypotheses on pp.134–135 are now listed. |
| F10 (l. 457–459) | closed |
| F11 (l. 593–595) | closed |

### (3) New items (all MINOR)

**N1. The interval restriction no longer literally covers two consumers.**
- *Where.* §2.1 now gives affiliation only for bounded open intervals U ⊇ supp h (l. 448–449). Two places need more:
  - Prop. propagation, l. 1245–1246: "$e^{itV((1-\chi)g)}\in\A(B)'$". Here (1−χ)g with g ∈ C_H generally has support on both sides of B, so no interval U containing that support avoids B.
  - Lemma cluster, Step 2, l. 2421–2424: "there is a bounded open $U\supseteq B$ disjoint from $O_{|t|}$". With A(U) defined only for intervals, this needs B to lie on one side of O_{|t|}.
- *Why it fails.* Lemma cluster's Step 2 is false for general compact B, for example B = [−2,−1] ∪ [1,2] and O = (−½,½).
- *Why nothing downstream breaks.*
  - In the only use (Lemma tworegime, l. 2526–2527), B_j ⊆ [j−1,j+1]∖O_d with |O_d| ≥ 2d > 8, so B_j lies on one side and an interval U exists.
  - The Locality proof never uses connectedness of U, and M_U ⊆ A(B)' whenever U ∩ B = ∅ by the Weyl relations (∫f h' = 0).
- *Repair.* State Locality for every bounded open set U, defining A(U) and M_U by the same formula, and add "M_U ⊆ A(B)' if U ∩ B = ∅". Alternatively, split (1−χ)g into its left and right parts using finite additivity, and record one-sidedness in Lemma cluster.

**N2. The n = 0 case.**
- *Where.* l. 624–627 claim continuity in ‖·‖_{1+ε} "both sides … ∏_j… bounded and integrable", and the Locality step at l. 470–471 applies the same (V.6b) bound to every n ≤ 2p'.
- *Why it fails.* At n = 0 the product is empty (= 1, not integrable), g ↦ ∫g is not continuous on L^{1+ε}(ℝ), and (V.6b) fails: g = 1_{[0,L]} has ratio L^{ε/(1+ε)} → ∞.
- *Why it is harmless.* The n = 0 term is the constant λa_0∫h with h ∈ L¹.
- *Repair.* Say n ≥ 1, with :φ^0(g): := ∫g for g ∈ L¹.

**N3. Range of the c_κ citation.**
- *Where.* l. 3420 cites N.25(iii) for the z-independence of c_κ.
- *Why it fails.* N.25(iii) assumes κ, κ' ≥ 2, while δ_κ, and with it c_κ, is introduced for κ ≥ 1. Appendix C uses only κ ≥ 2.
- *Repair.* Say "κ ≥ 2", or cite N.23''s statement, which covers κ ≥ 1.

**N4. A2 missing from the inputs list.**
- *Where.* l. 3231–3233.
- *Why it fails.* The list of inputs omits A2. A3's construction paragraph uses the definition of dμ_0, and N.25(i) uses "By Assumption A2 and Parseval".

**N5. Dossier images missing from disk.**
- *Where.* A1's Dossier (l. 666–669) and A3's Dossier (l. 777–779) cite simon-gaussproc-037 (p.15), simon-gamman-038 (p.16) and simon-wickdef-156 (p.134). At about 22:35, `ls audit_2026/evidence/` shows that none of these three files exists. The others cited are present: 032–034, 039, 047, 060, 157–160, 174.
- *Why it fails.* The provenance sentence at l. 3213–3215 says the pages "are in audit_2026/evidence/", which is false for pp. 15, 16 and 134.
- *Repair.* Copy the three images in, or reword the sentence.

**N6. "The only h used below" (l. 649).**
- *Why it fails.* Prop. smoothing (l. 1222–1223) and A5(i) still state results for every real h ∈ L¹∩L² of compact support. Only bounded h are consumed (l. 2258, 2476, 2528).
- *Repair.* Write "the only h consumed below", or restrict Prop. smoothing to bounded h.

### Checks run

- Built a copy three times with /Library/TeX/texbin/pdflatex in <scratch>/audit-math/build4b. The copy is byte-identical to the workspace file.
  - Results: `^!` 0, Overfull 0, undefined 0, LaTeX warnings 0.
  - The pdftotext grep for ??, TODO, Hmm and "wait," found nothing.
  - The PDF has 110 pages.
- Re-read the Simon page images I rendered from refs/ for the new quotes: pp. 15, 16, 134, 136, 138.
- Listed audit_2026/evidence/ for N5.
- Modified no file in the workspace.

### Not checked

- The other edits in the diff that are unrelated to F1–F11: A8 Scope and Used-in lines, the C5 reading items, the constants table, and the S_2 remarks beyond their quotation of Theorem C.5.
- Prop. propagation, Lemma cluster and Lemma tworegime beyond their interface with the affiliation claim.

---

## V4c, re-check (21:58 UTC)

## V4c re-check of the N1–N6 fixes in part_i/main.tex

**Verdict.** All six fixes hold, and the N1 repair is complete and correct. I found no CRITICAL or MAJOR defect. Four MINOR items remain (R1–R4 below), and none changes a result.

**Object.** main.tex, mtime 7 Nov 22:51:18, sha256 prefix 39ae25aa54eb143e, 7759 lines. I diffed it against my V4b copy and read every changed passage. Numbering is from my build's .aux and matches your correction: Lemma 9.3 = lem:cluster, 10.3 = lem:tworegime, Theorem 13.2 = thm:dichotomy, Proposition 2.6 = prop:smoothing, Proposition 2.7 = prop:propagation, Theorem 5.1 = thm:M2.

### N1: Locality and its consumers

**(a) Every step holds.**

*Locality paragraph (l. 462–498):*
- **Choice of κ for a general open U.** The bounded-h argument never uses connectedness. For κ > 1/dist(supp h, ℝ∖U), the interval [x−1/κ, x+1/κ] lies in U for every x ∈ supp h, so ρ_κ(x−·) ∈ C_c^∞(U).
- **M_U.** It contains the bounded Σ_U-measurable multiplications, so V(h) is affiliated with M_U. If U is an interval, M_U ⊆ A(U) by the definition of the net.
- **Finitely many components meet supp f.** The components of a bounded open set are disjoint bounded open intervals. They cover the compact set supp f, so finitely many cover it, and by disjointness only those meet it.
- **The pieces are compact.** supp f ∩ I_k = supp f ∖ ⋃_{l≠k} I_l is closed and lies inside I_k.
- **Smoothness of f_k.** f_k = f on the open set I_k, and f_k = 0 on the open set ℝ∖(supp f ∩ I_k). These two sets cover ℝ, and f vanishes on their overlap, so f_k ∈ C_c^∞(I_k).
- **Product and inclusion.** f = Σ f_k, so W(f,0) = ∏_k W(f_k,0) with each factor in A(I_k), which gives M_U ⊆ A(O')' for every bounded open interval O' disjoint from U.
- **The d/2 neighbourhood.** U := {dist(·, supp h) < d/2} is bounded, open, contains supp h and misses O'. Hence V(h) is affiliated with A(O')'.

*Proposition 2.7 (l. 1263–1274):*
- **Replacing B by its convex hull.** conv B ⊂ O because O is an interval.
- **The cut-off χ.** O'' exists, with χ = 1 on O'' and χ ∈ C_c^∞(O). By Locality, with U = O, e^{itV(χg)} ∈ A(O).
- **The rest of g.** supp((1−χ)g) ⊆ ℝ∖O'', so d ≥ dist(B, ℝ∖O'') > 0. O' = {dist(·, B) < d/2} is an interval with A ∈ A(O'), and dist(supp((1−χ)g), O') ≥ d/2 by the triangle inequality, so Locality gives e^{itV((1−χ)g)} ∈ A(O')'.
- **Conclusion.** The two exponentials commute (both are multiplication operators), so Ad e^{itV(g)}(A) = Ad e^{itV(χg)}(A) ∈ A(O). The strong-density extension is valid: the set of A for which this holds is a von Neumann algebra containing every W(f,h) with f, h ∈ C_c^∞(O).

*Lemma 9.3, Step 2 (l. 2447–2450).* O_{|t|} is a bounded open interval with dist(B, O_{|t|}) ≥ R−|t| > 0. Affiliation of X with A(O_{|t|})' means X commutes with A(O_{|t|})'' = A(O_{|t|}) ∋ β_t(A). That is exactly what Step 2 uses.

**(b) "Locality of the net over intervals" is a fair name for what the record presupposes.** It is the commutation of W(f,h) and W(f',h') when supports are disjoint (Weyl relations, symplectic form ∫(fh'−hf') = 0).
- The record already relied on it before this edit: the old Lemma 9.3 Step 2 used A(O_{|t|}) ⊆ A(U)'.
- Nothing beyond it is used. The other ingredients are isotony, which holds by definition, and elementary von Neumann algebra facts.
- It is still stated nowhere and has no source (R2).

**(c) Consumers.** A grep for "affiliat" gives l. 269, 448, 486–497, 2424, 2552, 2958, 3217.
- **Lemma 10.3 (l. 2552–2555):** it supplies exactly Lemma 9.3's new hypothesis, via Locality with B_j = supp h_j compact.
- **Theorem 13.2, Step 1 (l. 2955–2958):** B = B* ∈ A(O) by (B3), l. 2928. Since dist(Ō, O') > 0 forces O' ∩ O = ∅, B ∈ A(O')' by locality.
- **Proposition 2.7:** covered, as above.
- **No other non-interval U:** every argument of \A( in the file is O, O_{|t|}, O', O_T, U (an interval), O_1, O_2, sO, O+a, I_k or I. M_U is the only object attached to a general open set.

### N2–N6

| Item | Verdict |
|---|---|
| N2 (A1(d), l. 616 and 643–646; Locality, l. 464–465) | closed. With the empty product, (W.1) gives ⟨1, :φ^0(g):⟩ = ∫g and :φ^0(g): ∈ Γ_0, so the constant is ∫g. N.23'(ii) at n = 0 is consistent: X_κ = X = ∫w with w ∈ L¹, (W.4) at n = 0 reads 1 = 1, and Γ_0 is the constants. Residuals R1 and R4. |
| N3 (l. 3448–3449) | closed |
| N4 (l. 3261; A2 Used in, l. 714–716) | closed; N.25(i) is "By Assumption A2 and Parseval" |
| N5 | closed. `ls`: simon-gaussproc-037, simon-gamman-038 and simon-wickdef-156 exist (22:39, PNG 826×1234). Viewed: printed p.15 (Definition (c), Theorem I.6), p.16 ("closed subspaces generated by"), p.134 ((V.1)). |
| N6 (A1 Scope, l. 666–668) | closed. Every proof that uses V(h) uses a bounded h: V(g) with g ∈ C_H; V(χg) and V((1−χ)g); V(v) with v = g'−g, g, g' ∈ G; V_j = V(η_jv) with ‖·‖_∞ ≤ 1; the h of Theorem 5.1 and Corollary 5.2 (‖h‖_∞ ≤ 1); the h' of N.20 and N.21 (‖h'‖_∞ ≤ 1). Proposition 2.6 is used only at l. 2285, 2502 and 2555, with V(v) and V_j. Lemma N.19 (the kernel lemma) contains no V(h); I take it you meant N.20. Residual R3. |

### Remaining MINOR items

**R1 (left over from N2) — A3, l. 740–757.**
- *Text:* "for $g\in L^{1+\varepsilon}(\R^2)$ … the Wick power ${:}\Phi^n(g){:}$ is the unique element … and, for every $p\ge2$, $\|{:}\Phi^n(g){:}\|_p\le c\,(p-1)^{n/2}\|g\|_{1+\varepsilon}$ with $c$ depending on $\varepsilon$ and $n$ only".
- *Why it fails:* This is still stated for every n. At n = 0 the bound is false: take g = 1_{[0,L]²}, so ∫g / ‖g‖_{1+ε} → ∞. Nothing uses it at n = 0, because :Φ^0(h): = ∫h for h ∈ C_E.
- *Repair:* write "n ≥ 1", as in A1(d).

**R2 — the locality of the net is used but neither stated nor sourced.**
- *Where:* l. 494 ("by the locality of the net ($\A(I)\subseteq\A(O')'$ for disjoint intervals $I$, $O'$)"), l. 2957, and Lemma 9.3 Step 2. π_0 appears only in W(f,h) at l. 432 and is defined nowhere.
- *Why it matters:* AGENTS 4.1 asks that external facts be imported. The fact is standard and correctness is unaffected.
- *Repair:* one line, either "W(f,h)W(f',h') = e^{−i∫(fh'−hf')}W(f',h')W(f,h), so disjoint supports commute" with a source (Simon Ch. I or GJ), or an import entry.

**R3 — l. 475–476.**
- *Text:* "every $h$ for which a proof below uses $V(h)$ is bounded".
- *Why it fails:* Proposition 2.6's proof (l. 1246–1253) uses V(h) for every real h ∈ L¹∩L² of compact support. It does not use Locality, and A1 Scope (l. 666–668) states the caveat correctly.
- *Repair:* add the same caveat, or write "every $h$ whose locality is used below is bounded".

**R4 (nit) — l. 5187–5188.**
- *Text:* "$w\in L^{1+\varepsilon}$ … so ${:}\Phi^n(w){:}$ exists".
- *Why it is imprecise:* For n = 0 the object exists by the n = 0 convention (w ∈ L¹), not by Theorem V.2. Harmless.

### Checks run

- I built a copy three times with /Library/TeX/texbin/pdflatex in <scratch>/audit-math/build4c. The copy was byte-identical to the workspace file at check time.
  - errors (`^!`): 0
  - Overfull: 0
  - "undefined": 0
  - LaTeX Warnings: 0
  - pdftotext grep for ??, TODO, Hmm and "wait,": nothing
  - 110 pages
- I modified nothing in the workspace.

### Not checked

- Edits outside N1–N6: the orientation text of Proposition C.7 (l. 3790–3796), the constants paragraph (l. 7669–7670), and Corollary 5.2's constant (8 709 120 C_7K_1²K_2^{24} Σ λ³, which differs in form from the 9·C_7c_UΣ𝔎(p')λ² of Theorem 5.1; I did not reconcile them).
- Lemma 9.3, Steps 1 and 3.
- The Trotter part of Proposition 2.7.
- The uses of A5(i) in §slab.

---

## V4d, re-check (22:09 UTC)

## V4d re-check of the R1–R4 fixes in part_i/main.tex

**Verdict:** R1–R4 are closed. One MINOR point remains in the new A6 Scope sentence: it calls the identification of the source's algebras with A(O) "a reading" without saying which step is unproved. That step is the one the uses depend on. There is no CRITICAL or MAJOR finding.

**Object checked:** the version of 23:04:37, plus the only later change, at 23:07:05 (sha256 prefix bf56ca41bbbb4bef). That change extends the corrections-history sentence at l. 3231–3234: Locality now holds for every bounded open set, the hypothesis of Lemma 9.3 is restated, and locality is listed as A6(iii). That description is accurate. From the build's .aux: A:patch is A6, Proposition 2.7 is prop:propagation, Theorem 13.2 is thm:dichotomy.

### R1 — A3, construction paragraph, l. 739–761: closed
The construction is now stated "for $n\ge1$ and $g\in L^{1+\varepsilon}(\R^2)$". The new sentence handles n=0: "(W.2) with the empty product gives the constant ${:}\Phi^0(g){:}:=\int g$, as in Assumption A1(d); the bound above is used only for $n\ge1$". The claim h∈C_E ⊂ L¹∩L^{1+ε} is correct. The later clause "lies in every $L^p(d\mu_0)$ by (V.6a)" is trivially true for the constant term.

### R2 — new item A6(iii), l. 877–900: closed, with one MINOR point

**(a) Quotations are verbatim.** I checked audit_2026/evidence/gj2-locality-37.png (printed p. 397) and my own 200 dpi render of PDF page 37 of the GJ 1970 II paper in refs/. Each quoted fragment appears on the page exactly as printed:
- "as the weak closure of the bounded functions of the $t=0$ fields"
- "as $f$ runs over the $C^\infty$ functions with support in"
- "disjoint open sets"
- "elements of"
- "commute"

The two displayed integrals ∫φ(x,0)f(x)dx and ∫π(x,0)f(x)dx also match. The page is the proof of Theorem 3.5.1, as the Sources line says. Leaving out the script set symbols is fine.

**(b) The reading sentence (l. 889–891) — MINOR.**
- Text: "That these algebras are the $\A(O)$ of \S\ref{subsec:model}, generated by the Weyl operators $W(f,h)$, is a reading of the source, and items (i) and (ii) are imported under the same reading."
- What it gets right: it does not claim a proof, and it puts (iii) at the same status as (i) and (ii).
- Why it falls short: it bundles two different things under "reading".
  1. Identifying GJ's φ(x,0), π(x,0) (Fock space) with the record's φ_0, π_0 is a genuine dictionary reading.
  2. Identifying the algebras is mathematics. Let 𝔄(O) be the source's algebra. The inclusion 𝔄(O) ⊆ A(O) is immediate, because bounded functions of φ_0(f) and π_0(f) lie in {W(tf,0), W(0,tf)}''.
  3. The uses need the other inclusion, A(O) ⊆ 𝔄(O):
     - Locality needs A(O') ⊆ 𝔄(O') to pass GJ's commutation from 𝔄(O') to all of A(O').
     - Theorem 13.2 needs B ∈ A(O) to lie in 𝔄(O).
  4. That inclusion requires W(f,h) ∈ 𝔄(O). This follows from the Weyl relation W(f,h) = e^{±(i/2)∫fh} W(f,0) W(0,h), which the record neither states nor imports.
- Repair (one sentence): "𝔄(O) ⊆ A(O) is immediate. The inclusion A(O) ⊆ 𝔄(O), which the uses of (iii) need, rests on the Weyl relation W(f,h) = e^{±(i/2)∫fh}W(f,0)W(0,h) (sign by convention), which is not proved here." Alternatively, import that relation explicitly.

**(c) A6(iii), restricted to intervals, covers every use.**
- **Locality (l. 493–494):** each I_k is a bounded open interval inside U, and O' is a bounded open interval disjoint from U. So A(I_k) ⊆ A(O')', hence W(f_k,0) ∈ A(O')' and M_U ⊆ A(O')'.
- **Theorem 13.2, Step 1 (l. 2969–2971):** O and O' are bounded open intervals with dist(Ō,O') > 0, so they are disjoint.
- **Other uses:**
  - Proposition 2.7 (l. 1285) reaches (iii) only through Locality.
  - Lemma 9.3 uses it only through its hypothesis, supplied by Locality (Lemma 10.3) or by A6(iii) (Theorem 13.2).
  - A grep for A(·)' and "commut" before Appendix C finds no other implicit use of locality.
- **Used in and Dossier lines:** accurate, and the image file exists (23:03, 1000×1505).

### R3 — l. 475: closed
The text now reads "every $h$ whose locality is used below is bounded". Locality is used only for V(χg) and V((1−χ)g) in Proposition 2.7 and for V_j in Lemma 10.3, and all of these are bounded.

### R4 — l. 5200–5203: closed
The text now reads "$w\in L^1\cap L^{1+\varepsilon}$ … (for $n=0$ it is the constant $\int w$ of the convention in Assumption A1(d), resp. Assumption A3)", which is consistent with A1(d) and A3.

### Checks run
- Built a copy of the 23:07:05 file (byte-identical to the workspace file at check time) three times with /Library/TeX/texbin/pdflatex in <scratch>/audit-math/build4d:
  - errors (`^!`): 0
  - Overfull: 0
  - "undefined": 0
  - LaTeX Warnings: 0
  - pdftotext grep for ??, TODO, Hmm, "wait,": empty
  - 110 pages
- The build of the 23:04:37 version gave the same counts.
- I modified nothing in the workspace.

### Not checked
- The rest of the GJ2 page (the proof of (3.5.1) and reference [8]).
- The pages behind the existing A6 dossier items gj1-locality-06 and gj2-local-algebra-40.
- Edits outside R1–R4 other than the provenance sentence at l. 3231–3234.

---

## V4e, re-check (22:17 UTC)

## V4e re-check: new definition of A(O) in part_i/main.tex

**Verdict:** the change of definition closes my V4d point. With the dictionary reading alone, the source's algebra and the new A(O) coincide. No proof needs W(f,h) with both f and h nonzero as an element of A(O). One MINOR inaccuracy is new: A6's Scope says the manuscript does not use the Weyl relations, but Remark 3.3 does. One MINOR nit predates the change. There is no CRITICAL or MAJOR finding.

**Object checked:** the 23:12:52 version plus the only later change at 23:14:28 (sha256 prefix eab9ac4d305f6a67). That change adds the Appendix B clause at l. 3249–3250, "…with the generators of $\A(O)$ written as in the sources, $W(f,0)$ and $W(0,h)$ (§2.1)", which is accurate. Numbering from my build: A:patch = A6, A:covar = A7, rem:wlog = Remark 3.3; the parity sentence (l. 2896) is in the proof of the Main Theorem, §12.

### (a) The equivalence sentence (l. 437–445) is correct and complete

Let 𝔅(O) be the von Neumann algebra generated by the bounded Borel functions of φ_0(f) and π_0(f), for real f ∈ C_c^∞(O).

- **A(O) ⊆ 𝔅(O).** Each generator W(f,0) = e^{iφ_0(f)} and W(0,h) = e^{iπ_0(h)} is a bounded Borel function of a single field.
- **𝔅(O) ⊆ A(O).**
  - The unitary groups W(tf,0) and W(0,tf) lie in A(O), because tf ∈ C_c^∞(O) is real.
  - Anything commuting with e^{itT} for every t commutes with the spectral projections of T. So {e^{itT}}'' contains those projections, and every bounded Borel function of T is a norm limit of their combinations.
  - That bicommutant lies in A(O).
- **Comparison with the source (GJ2, p. 397).** Once φ(x,0) and π(x,0) are read as φ_0 and π_0, the source's algebra for an interval O ("the weak closure of the bounded functions" of the t = 0 fields, f smooth with support in O) is 𝔅(O). That equals A(O) by the two inclusions above. Two details do not affect this:
  - A closed support inside the bounded open set O is compact, so "support in O" means C_c^∞(O).
  - A complex f gives a normal field whose real and imaginary parts commute. Its bounded functions lie in the algebra generated by the real-f fields.

So both inclusions hold given only the dictionary, and the Weyl relations are no longer needed for this identification.

### (b) No proof uses a generator W(f,h) with both entries nonzero

- **Remark 3.3 (l. 1454–1460).** The conclusion σ_s(A(O)) = A(sO) needs only the two special cases of the formula: σ_s(W(f,0)) = W(s⁻¹f(·/s), 0) and σ_s(W(0,h)) = W(0, h(·/s)), applied through the implementing unitary U_s. Both images are generators of A(sO).
- **Main Theorem, §12 (l. 2896).** "θ maps W(f,h) to W(−f,−h)" is true as an identity, but the claim θ(A(O)) = A(O) needs only the cases (f,0) and (0,h).
- **Prop. 2.7 (l. 1291).** Updated correctly to generators W(f,0) and W(0,h).
- **The sentence "no proof below uses a generator other than W(f,0) and W(0,h)" (l. 444–445)** is accurate.

**New finding (MINOR) — A6 Scope, l. 903–905.**
- Text: "matching that generating set to the source's would need the Weyl relations, which this manuscript neither states nor uses."
- Why it fails: Remark 3.3 introduces "the scaling automorphism of the Weyl algebra, $\sigma_s(W(f,h))=W(s^{-1}f(\cdot/s),h(\cdot/s))$ (a symplectic map)". It then has σ_s carry the mass-m_0 Fock state to the mass-M_* Fock state and obtains U_s from that. An automorphism of the Weyl algebra induced by a symplectic map, and its implementation through Fock states, presuppose the Weyl relations. So the manuscript does use them there, implicitly. Nothing about A(O) depends on this.
- Repair, either of:
  1. Change the clause to "…which this manuscript neither states nor uses for the local algebras (Remark 3.3 presupposes them for its scaling automorphism; only its action on W(f,0), W(0,h) enters σ_s(A(O)) = A(sO))".
  2. Rewrite Remark 3.3 to define U_s directly, as second quantization of the one-particle dilation, with U_sφ_0(f)U_s* and U_sπ_0(h)U_s* given explicitly.

### (c) Nothing else in the record conflicts with the new definition

- **Notation table:** has no entry for A(O) or W.
- **Appendix B (l. 3249–3250):** consistent.
- **A7:** makes no statement about generators. Theorem 13.2, Step 1 uses τ_a(B) ∈ A(O+a), which needs only U_aW(f,0)U_a* = W(f(·−a),0) and U_aW(0,h)U_a* = W(0,h(·−a)). That presupposition is unchanged by the edit.
- **Locality paragraph:** "If U is an interval, M_U ⊆ A(U)" holds, because M_U is generated by W(f,0) with f ∈ C_c^∞(U), and these are generators of A(U). The component step W(f_k,0) ∈ A(I_k) also holds.
- **Imports A6(i)–(iii):** now refer to exactly the source's algebras under the dictionary, which is a cleaner match than before.
- **Elsewhere:** the only other "Weyl" mentions (l. 3087–3093) concern Part II's lattice Weyl algebras 𝔚_N(O), not A(O).

**Nit (MINOR, predates this change) — l. 432, 439.** π_0 is still not defined anywhere in Q-space; it appears only inside W(f,h) and in the A6 Scope dictionary. The new sentence uses π_0(f) explicitly as a self-adjoint operator with unitary group W(0,tf). Repair: one clause defining π_0 as the dictionary image of the sources' π(·,0), or as the Q-space momentum field of Simon Ch. I.

### Checks run

- Built a copy of the 23:14:28 file three times with /Library/TeX/texbin/pdflatex in <scratch>/audit-math/build4e. The copy was byte-identical to the workspace file at check time.
  - errors (`^!`): 0
  - Overfull: 0
  - "undefined": 0
  - LaTeX Warnings: 0
  - pdftotext grep for ??, TODO, Hmm, "wait,": empty
  - 110 pages
- I modified nothing in the workspace.

### Not checked

- The rest of Remark 3.3: whether the π-part of the Fock states scales correctly, and the stated formulas for H_0 and V.
- The justification of Θπ_0(h)Θ = −π_0(h), used for θ(W(0,h)) = W(0,−h).
- The translation covariance of the net, used for τ_a(A(O)) = A(O+a).
