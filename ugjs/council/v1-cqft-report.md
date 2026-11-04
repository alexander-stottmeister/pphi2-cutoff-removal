# V1 attack report (cqft) on the comparison note, Phases A and B of `ugjs/PLAN.md`

Attacker: cqft (council of `ugjs/PLAN.md`), round V1, PLAN Part 5. I drafted no part of the note.
Written 3 November 2026. Standard: AGENTS.md §§1–5. Severity words as in AGENTS.md §2.

- **Object.** `WORK/frozen-v1/` (`WORK` = the scratchpad folder `phaseAB/`): `comparison.tex`, `preamble.tex`,
  `parts/*.tex`, and `comparison.pdf` (59 pp, sha256 `7e393b9a440fe6a29af13d921aa62b7ecf59e363332355c5981ed0d7be485f87`).
  `diff -r` of `frozen-v1/parts` against `WORK/parts`, and of the master and preamble: identical. Statement numbers
  and PDF pages are from `WORK/comparison.aux` (build of 16:38, the frozen PDF).
- **Read in full this session:** every part file (`notation.tex`, `d1.tex`, `d2.tex`, `d3.tex`, `d4.tex`,
  `quantifiers.tex`, `consequences.tex`, `constants.tex`, `gates.tex`), the master, the preamble,
  `REPORTS-drafters.md`, `BRIEF-V1.md`, and the V3 report `ugjs/council/v3-appendix-c-report.md` (it differs from
  `WORK/audits/V3-appendixC-report.md` only by the orchestrator's header notes).
- **Record** `part_i/main.tex` (mtime 2 Nov 15:35:23): ll. 372–1722 (§§2–7), 2766–3093 (Appendix C), and ll.
  2108–2111, 2250–2256, 2425–2432. Its `main.aux` numbers and pages equal `labels-main.txt`; label lines are
  shifted by +1 (`app:provenance`) and +2 (the Appendix C labels). Record line numbers below are current ones.
- **PLAN:** Parts 1, 2, 6 and 8, plus grep hits for F-T and "transverse". `part_i/C5_reading_record.md`: the
  header and items 1–4, 10–13.
- **GJS 1974** (`refs/`, PDF page = printed − 583): pp. 589, 593, 594, 595, 596, 597, rendered by me at 200 dpi
  (`WORK/audits/v1-cqft/gjs-06.png`, `gjs-10.png` … `gjs-14.png`). P. 594 was also cropped at 600 and 1200 dpi.

## Verdict

**D.1, D.2 and D.3 can be recorded as `proved, conditional on the V3 repairs`.** The conditions are:
- D.1: through its identification of the record's 𝒰_h with the L²-limit of 𝒰_{h,κ}, which is the content of R8
  together with Lemma C.4;
- D.2: through Lemma C.4 in Lemma N.5(iv);
- D.3: through Lemma C.2 at R8 and Theorem C.5 at R1–R10, with parallel strips only.

Before that, the MINOR status labels of findings 3, 7 and 11 must be corrected. Every application of GJS
Theorem 1.1.7 in §§4–6 has the right objects, squares, strip, cutoff class, measure and constant (H1). Every
transverse application is flagged F-T (H2).

**D.4 cannot be recorded as `proved, conditional on the V3 repairs` as written.** Two dependences are disclosed:
the transverse case of Theorem 1.1.7, imported at the printed scope (F-T), and the §2 GAP. Beyond these, the proof
bounds two different constructions of the sharp-time observable V(h′)(0)² as if they were one, and their equality
is proved nowhere (finding 1, MAJOR). The repair is a few lines.

Further:
- No CRITICAL finding. No false statement in D.1–D.4.
- Both drafters' source claims are confirmed on my own renders: GJS (1.1.11) prints "0(1)" with a digit zero, and
  p. 594's strip sentence has no closing period.
- The N_I counterexample is right. The N_I repair is incomplete (finding 5), and the note rates the record's error
  too low (finding 6).

## Findings

### MAJOR

**1. Two constructions of the sharp-time Wick monomials are used as one object in Theorem D.4, and in the transfer
to Theorem 5.1.**
- *Locators:*
  - §6.3, Theorem D.4 (`thm:D4`), proof, Step 2 (`d4.tex` ll. 135–136, PDF p. 35) and Step 4 (ll. 163–164, p. 36);
  - §2.7, Lemma N.21 (`aux:notation-hyper`), proof of (i) (`notation.tex` ll. 965–974, p. 15);
  - §3, Definition N.24 (`aux:d1-obs`) (`d1.tex` ll. 210–213, p. 20);
  - §4.1, Lemma N.30 (`aux:d2-int`) (`d2.tex` ll. 95–97, pp. 26–27);
  - §8.6, the Theorem 5.1 replacement, Step 5 (`consequences.tex` ll. 302–307, p. 48).
- *Text:*
  - Step 2: "Lemma~\ref{aux:notation-hyper}(ii), applied to $Y:=V(h')(0)$, gives
    $\|Q_V\|_{L^2(\dmu)}=\|Y^2\|_{L^2(\dmu)}\le9^{p'}V_*$."
  - Step 4: "Apply Lemma~\ref{lem:D2}(a) with $F=Q_V$ and its pieces $Q_{n,n',k,k'}$".
  - N.21: "Put $Y_r:=\lambda a_rJ_0W_r$; then $Y=J_0V(h')=\sum_rY_r$".
  - N.24: "The localized monomial $Q$, resp. $Q(x_0)$, is the limit of $Q^{(\kappa)}$, resp. $Q^{(\kappa)}(x_0)$,
    in $L^2(\dmu)$".
  - N.30: "The membership in $L^4(\dmu)$ is Lemma~\ref{aux:d1-moments}(b)".
- *Why it fails.* Y in N.21 is J₀ applied to the time-zero limit W_n of Lemma N.20(iii). W_n is built with the
  one-dimensional mollifier ρ_κ, so Y is the L²(dμ₀)-limit of Wick powers of Φ(0, ρ_κ(x−·)).
  - The pieces Q_{n,n′,k,k′} to which Lemma D.2 is applied are objects of Definition N.24(b). This follows from
    D.2, Step 2 ("which is the class of Lemma D.1") and from N.30. They are limits of Wick powers of
    Φ_κ(0,x) = Φ(δ_κ((0,x)−·)), with the record's two-dimensional mollifier δ_κ.
  - Both objects lie in the n-th chaos and have the same norm (N.20(iii), N.26(d)). Equal norms do not give
    equality, and the cross inner product is never computed.
  - No sentence of the note identifies them. J₀ occurs only in N.21, and `d4.tex` cites neither N.24 nor N.26.
  - So Step 2 and Step 4 bound ⟨·⟩_{h^B} and ⟨·⟩_h − ⟨·⟩_{h^B} of two objects that carry the same name.
  - §8.6 then needs the bound for the J₀ object. The identity ‖V(h)ψ̂_T‖² = ∫V(h)² dq_{h_{T,g}} comes from the
    FKN embedding of a time-zero function (record Lemma 4.1), but the comparison term was proved for the N.24
    object.
  - Read with J₀ pieces instead, the gap moves without closing. N.30 proves L⁴ membership through N.26(b), for
    N.24 objects only. D.1 is stated for the class 𝔉 of N.24; its Remark N.27(a) would cover the J₀ pieces.
  - The merge introduced this. Before it, V_* cited N.26(d) (mp's report, §5(3): "V_* now cites my N.26(d)").
    Appendix A, (C5), records that "§6 now uses Lemmas N.20 and N.21".
- *Repair.* Add one lemma: for real f ∈ L² supported in one column and 0 ≤ n ≤ 2p′, the N.24(b) object
  ∫f(x):Φ(0,x)ⁿ:dx equals J₀W_n(f) almost everywhere.
  - By Lemma N.22 with ℓ = 2, E[X^{(κ)}·J₀W_{n,κ′}] = n!∬f(u)f(v)Γ_{κκ′}(u−v)ⁿ du dv, where
    Γ_{κκ′}(u) := E[Φ_κ(0,u)Φ(0,ρ_{κ′}(·))] → C(u) for u ≠ 0.
  - Γ_{κκ′} is dominated by a κ-uniform logarithmic majorant, as in N.20(ii) and N.23(iii).
  - Hence ‖X_n − J₀W_n‖₂² = I − 2I + I = 0.
  - Alternatively, run D.4 on one construction throughout. The transfer of §8.6 still needs the identification.
  - At degree 1, as used in D.3, the identification is immediate, because δ_κ∗(δ_s⊗f) → δ_s⊗f in the covariance
    norm. One sentence should record it.
- *Severity:* MAJOR. A load-bearing identification is made tacitly. A repair exists, and I see no risk to the
  truth of D.4.

### MINOR

**2. The identification of the note's objects with GJS's monomials is a reading of the source, and the note does
not name it as one.**
- *Locators:* Remark N.25 (`aux:d1-def`, `d1.tex` ll. 216–235, PDF p. 20); D.2, Step 4 (`d2.tex` ll. 180–186,
  p. 27).
- *Text:*
  - N.25: "the record imports the class as printed (A8(ii) …) and gives no construction. Definition~\ref{aux:d1-obs}
    makes the integrals precise in the way the record treats the interaction".
  - D.2: "$Q_1:=F_a$: a localized monomial of type (1.1.5) or (1.1.6), as given".
- *Why.* Source Fact 2.2 speaks of GJS's monomials under GJS's dq_h. GJS print formal integrals (p. 593) and
  Wick order "with respect to the measure dΦ, as in [9], [1]" (p. 589).
  - That N.24's δ_κ-limits are those objects is a reading, of the kind the record names in A8, Scope (d).
  - So is the claim that the record's 𝒰_h is GJS's V(h); the V3 report, §12, leaves that "not checked".
  - Independence of the mollifier in N.24 is not shown.
- *Repair:*
  - Name the reading beside the status words, next to the C5 items.
  - Add mollifier independence. The cross-covariance computation of finding 1 gives it, and so does Simon's (V.3)
    under R8.

**3. Status labels: D.1, D.2 and Lemma C.2 are labelled inexactly.**
- **(a) D.1.**
  - *Locators:* `gates.tex` ll. 6–8 (PDF p. 58), "Lemma~\ref{lem:D1} proved (mp; one named dependence …)";
    Remark N.27(b) (`d1.tex` ll. 507–514, p. 24).
  - *Why.* Step 1 (`d1.tex` ll. 402–421, p. 23) needs 𝒰_{h_α} = (1−α)𝒰_{h₁} + α𝒰_{h₂} for the *record's* 𝒰_h.
    That rests on one of two things:
    - the record's ll. 2918–2920, "so that 𝒰_{h,κ}→𝒰_h in every L^p(dμ₀)", which V3 (m-1, §7) finds "asserted
      and proved nowhere in the record";
    - Lemma C.4 (R1–R10), with R8 supplying the meaning of 𝒰_h (V3 M-3).
  - Per AGENTS §2 the word is therefore "proved, conditional on R8 and Lemma C.4".
  - §2 marks the time-zero face of the same issue as a GAP and §3 does not, although `gates.tex` ll. 16–18 calls
    the two "the time-zero and path-space faces" of M-3.
- **(b) D.2.**
  - *Text:* `gates.tex` ll. 8–11: "Lemma~\ref{lem:D2}, Theorems … proved conditional on Lemma~\ref{lem:D1} and on
    Lemma~C.2 and Theorem~C.5".
  - *Why.* D.2 uses neither of these. It uses Lemma C.4, through N.18(iv) and N.5(iv), as `d2.tex` ll. 154–156
    itself says.
- **(c) Lemma C.2.**
  - *Text:* `d1.tex` ll. 479–481 (p. 24): "it is proved conditional on the repairs R1--R10 of the V3 audit".
  - *Why.* Everywhere else the note has R8 alone (`notation.tex` ll. 30–31, `d3.tex` l. 53). V3, §2: "After R8,
    Lemma C.2 is `proved`".
- *Repair:* correct the three labels.

**4. The dependences on the GAP, and those of the replaced Lemma 4.3(ii), are misstated.**
- *Locators:* `consequences.tex` l. 27 (PDF p. 43); the replacement block `lemma-4.3-ii`, ll. 76–80 (p. 44).
- *Text:* "The replaced proof of Lemma~4.3(ii) uses Assumption~A3 only."
- *Why.* The block also uses "$F(\Phi(s,\cdot))\in L^4(d\mu_0)$ for every $s$ (Gaussian moments of the free field,
  Appendix~D, \S3)", including for F = |V(h)|.
  - For |V(h)| this rests on the GAP (the record's V(h) is identified with N.20's limit) and on finding 1 (§3's
    moments concern N.24 objects).
  - The record's unchanged Theorem 5.1, Step 1 (main.tex ll. 1278–1283: "$Q_V$ is exactly the multiplication
    function $V(h)^2$") rests on the GAP too. The note does not list it.
  - Conversely, D.4's Euclidean statement need not rest on the GAP at all. V_* could be computed for the N.24 object
    by N.26(d), leaving the GAP to the transfer alone.
- *Repair:*
  - Name the GAP and the Gaussian moments at Lemma 4.3(ii) (the |V(h)| case) and at Theorem 5.1, Step 1.
  - Optionally, restate V_* via N.26(d).

**5. The N_I repair (§8.1) is incomplete, and two sentences about unchanged statements are false after it.**
- *Locators:* §8.1 (`sub:cons-NI`, `consequences.tex` ll. 37–52, PDF p. 44); master §1 (`comparison.tex` ll. 55–59,
  p. 2); `consequences.tex` ll. 15–17 (p. 43).
- *Text:*
  - "\S6, l.~1359, replaced: $N_I:=\#\{k\in\Z:\ |I\cap[k-\tfrac12,k+\tfrac12)|>0\}$".
  - "The sentence of Assumption~A8(ii) (ll.~659--663) … is then true".
  - Master: "changes no statement except through the value of the constants that contained $C_8$ (… the radius of
    Theorem~7.7 …)".
  - §8: "Every other statement of the record is unchanged".
- *Why:*
  - **(i)** The record defines N_I a second time, in the notation freeze table at main.tex l. 448: "$N_I$ & number
    of unit cells $[j,j+1)$ meeting the interval $I$ in positive measure". That line is not in the edit, so the
    integrated record would carry two definitions.
  - **(ii)** A8(ii), ll. 659–661, says "The cells $[j,j+1)$ used in \S\S5--6 are this lattice shifted". After the
    edit, §6 uses columns. That clause becomes false; only the "same constants" clause becomes true.
  - **(iii)** Theorem 5.1, Steps 2–4 (ll. 1285–1309) still compute ‖Q_V‖_GJS on the cells [j,j+1), and they are
    kept (`consequences.tex` ll. 319–321). This is harmless: the steps are dead once Step 5 is replaced, and N.41(iii)
    gives the same bound on columns. But the integrated record would count on two lattices.
  - **(iv)** The statement of Lemma 6.1 changes: its counterexample sentence (ll. 1364–1366) is part of the
    statement, becomes false for columns, and is replaced. The content of Proposition 6.2, (7)–(8), changes too.
    Neither contains C₈, contrary to the master's sentence and §8's. Conversely, "the radius of Theorem 7.7" is
    not part of any statement: §8.5 says "The statement of Theorem~7.7 … is unchanged".
- *Repair:*
  - Add l. 448 and A8(ii), ll. 659–663, to the edit.
  - Say which lattice §5, Steps 2–4 use.
  - Correct the two sentences to name Lemma 6.1 and Proposition 6.2.

**6. The note rates its own finding on the record's cell count (E1) too low for the statements it affects.**
- *Locators:* §8.9 (`consequences.tex` ll. 425–429, PDF p. 50); Remark N.35 (`d3.tex` ll. 137–150, p. 30).
- *Text:* "Severity: MINOR (displayed constants $\mathfrak n(Q)$, $K'$; every use needs finiteness only)."
- *Why.* ‖·‖_GJS is the printed norm on p. 593's squares (A8(iii); notation table l. 447). On that reading, the
  counterexample makes the record's Proposition 6.2 (7) false as stated for I = (0.4,0.6).
  - For r = 1, every decomposition into pieces localized in GJS squares has norm sum ≥ √2K₁K₂²‖f‖₂. The pieces in
    each column must sum to f there.
  - The bound (7) with N_I = 1 asserts K₁K₂²‖f‖₂.
  - By AGENTS §2 this is CRITICAL for Proposition 6.2 and MAJOR for the displayed bounds of Lemmas 7.1 and 7.6.
    It is MINOR only for Theorems 7.7, 7.8 and 12.2, which need finiteness.
  - The note's repair removes all of this; only the classification should be split.

**7. D.3's pairs are not literally "the case the printed proof reaches".**
- *Locators:* `comparison.tex` l. 53 (PDF p. 2), "Theorem~\ref{thm:D3} uses the parallel case only"; Remark N.37
  (`aux:d3-orient`, `d3.tex` ll. 270–276, p. 32).
- *Text:* "This is the orientation of Lemma~7.4 of the record …, and the case that the sentence F-T … says the
  printed proof reaches for sharp-time monomials".
- *Why.* F-T and Lemma 7.4 concern pairs of sharp-time monomials. D.3 pairs a sharp-time piece with the
  time-integrated U_{Δ,n}, of type (1.1.6).
  - The printed proof takes "$A=Q_1$, $B_T=Q_2$ in Theorem 1.1.11" (p. 597), for "monomials of type (1.1.5)"
    (p. 596).
  - It therefore reaches D.3's pairs only after U_{Δ,n} is sliced in time and the bound is integrated: the
    multi-time reading of PLAN Part 2, which GJS do not print.
  - N.37's later sentences disclose this; its first sentence and the master overstate it. The import standard
    covers the pair either way.
- *Repair:* write "the parallel case, with a time-integrated partner, which the printed proof reaches after
  slicing".

**8. The F-T disclosure is not carried to the statements that consume Theorem D.4.**
- *Locators:*
  - §8.7 (`sub:cons-rest`, `consequences.tex` ll. 357–365, PDF p. 49);
  - the Corollary 5.2 replacement block (ll. 328–337, p. 48);
  - §7 (`quantifiers.tex` ll. 204–224, p. 41);
  - the M_B rows of the Appendix A table (`constants.tex` ll. 367–372, p. 57).
- *Text:* §8.7: "holds verbatim with the replaced Theorem~5.1 … Lemma~10.2 (proof, l.~2110) and \S11 (l.~2254) cite
  Theorem~5.1's $M$ by name: text unchanged, value $M_B$."
- *Why.* After Phase B, Theorem 5.1, Lemma 10.2, Theorem 11.1 and Theorem 12.2 rest on the transverse case.
  - PLAN Part 1's status table (row "Thm 5.1; Lemmas 10.2, 10.3, 10.5; …", column "after Phase B") reads
    "proved; rests on CE2, including its transverse case; M = M_B".
  - The note's §1 claims disclosure "wherever it is used".
  - The applications themselves are flagged (H2).
- *Repair:* one clause in §8.7, and one in the Corollary 5.2 block.

**9. One record locator is wrong.**
- *Locator:* `consequences.tex` ll. 111–112 (PDF p. 45).
- *Text:* "(The ``le'' is the source line's \verb+\|le+, finding F2 of the plan, l.~1449.)"
- *Why.* The `\|le` is at main.tex l. 1448. L. 1449 is "C_8^{1/2}\mathfrak n(Q)$."

**10. D.2(b) is not PLAN's form.**
- *Locators:* `d2.tex` ll. 120–125 (PDF p. 26); `gates.tex` ll. 21–22.
- *Text:* "(b) (The form of \texttt{ugjs/PLAN.md}, Part~1.) If every square $\Delta\not\subseteq B$ meeting $\supp h$
  is separated from $\bigcup R$ by a strip of positive width".
- *Why.* PLAN Part 1 reads "Assume every square Δ ⊄ B meeting supp h is separated from R by a strip". "Of positive
  width" is an added hypothesis: it excludes the width-0 separation that PLAN's form admits, with the factor
  e⁰ = 1. This is harmless, since (b) is not used.
- *Repair:* "a form of the plan's statement, with positive widths".

**11. The input lists omit Lemma C.4.**
- *Locators:* `comparison.tex` ll. 26–28 and 65–69 (PDF p. 2); Remark N.40 (`d3.tex` ll. 324–326, p. 33).
- *Text:*
  - Master: "From the record: A3 …, Lemma~C.2, Theorem~C.5; … No new import is made."
  - N.40: "Only GJS Theorem~1.1.7 is used, in its parallel case, with the record's Lemma~C.2 and Theorem~C.5".
- *Why:*
  - The note also uses Lemma C.4 (N.5(iv) in D.1–D.2; N.13(iii) for the translation invariance of S₂, hence for A
    and M_B; N.18(iii)), Remark 2.5 and A2.
  - "No new import" holds only modulo R8, which V3 writes as an import paragraph for A3: Simon (V.3), (I.21) and
    (I.32).

**12. Lemma N.18(iii) misstates where a₀ enters.**
- *Locator:* `notation.tex` ll. 680–684 (PDF p. 11).
- *Text:* "The coefficient $a_0$ enters the estimates of this note only through the lower bound of Lemma~C.2 … and
  through $\Uc_{h'}$ inside $S_2$, i.e. through the base terms".
- *Why.* In D.4, a₀ also enters V_*, through the n = 0 term of V(h′). It also enters the comparison term, through
  ‖Q_V‖_GJS ≤ 9K₁K₂^{8p′}(4p′)!λ²(Σ_{n=0}|a_n|)². `quantifiers.tex` ll. 322–324 says so.
- *Repair:* "the measures do not depend on a₀; a₀ enters the bounds through Z, S₂ and the observable".

**13. The frozen sentence F-T is adapted, not verbatim.**
- *Locator:* `comparison.tex` ll. 47–53 (PDF p. 2).
- *Why.* PLAN Part 8: "Each is used verbatim at its first mention in each document". The note writes "Lemma~7.4 of
  the record uses only that case; Theorem~\ref{thm:D4} of this note also uses …" in place of F-T's last sentence.
  The content is the same.
- *Repair:* quote F-T verbatim first, then adapt it.

**14. Two slips in §7.**
- `quantifiers.tex` l. 115 (PDF p. 39): "$N^{\rm col}_I$ of \S\ref{sec:d3}". §5 defines no N^col_I; `d3.tex` writes
  N^□_I.
- ll. 145–146 (p. 40): "$s_0:=\min_{j\le k}(2kK_{e_j})^{-1}$", without e_j ≠ 0. K_{e_j} is undefined for e_j = 0,
  since Lemma 7.6 assumes f ≠ 0. Appendix A, (C4), already lists this second slip.

**15. A source misprint is corrected silently in the record, and the gate record still calls it unconfirmed.**
- *Locators:* main.tex l. 814 (A8(vii′)(a), printed p. 12), which transcribes GJS (1.1.11) as
  "≤ O(1)e^{−m₁d/2}"; `gates.tex` ll. 35–37 (PDF p. 59).
- *Why.* GJS print "≦ 0(1)e^{−m₁d/2}", with a digit zero (S1 below). This is a silent correction (AGENTS 4.6, PLAN
  trap 27). `gates.tex` calls mp's reading "unconfirmed".
- *Repair:* write "[sic: 0(1)]" in the record, add a PLAN Part 9b entry, and update `gates.tex`.

## The two source claims (confirmed)

**S1. GJS (1.1.11), p. 594, prints "0(1)" with an upright digit zero.** I rendered PDF page 11 at 600 dpi. The
crops are `WORK/audits/v1-cqft/p594-1111rhs-600-11.png`, `p594-1110rhsb-600-11.png` and `p594-1110full-600-11.png`,
measured with `glyphs.py` (threshold 128, connected components). This is a numerical aid to reading the page.

| glyph | width × height | dark pixels | slant |
|---|---|---|---|
| glyph before "(1)" in (1.1.11) | 38 × 61 px | 979 | −0.5 px |
| digit "0" of the label "(1.1.10)", same page | 38 × 61 px | 992 | −1.0 px |
| "O" of "O(1)" in (1.1.10) | 56 × 65 px | 1096 | +6.7 px (italic) |

The "1" (34 × 62) and the parentheses (22 × 79) are identical in all three crops. So (1.1.11) prints an upright
digit zero. (1.1.10) and Theorem 1.1.7's text print an italic capital O, and p. 595's derivation prints an italic
"O(1)" too (200-dpi render). mp's reading is right, and so is its E6: p. 595 prints "Feyman-Kac".

**S2. P. 594's strip-definition sentence ends without a period.**
- In my 600-dpi crop of the line ending "from the {Δ^{(2)}_{jl}}" (`p594-stripend-600-11.png`), the last dark
  column is the closing brace. Nothing follows it on the line, out to x = 3500 px.
- The next line is the heading "THEOREM 1.1.7."
- `notation.tex` ll. 257–262 quotes the sentence and records the missing period. `d2.tex` ll. 47–48 quotes a
  fragment of it. C5 item 11 also ends the quotation without a period.

## What holds (checked this session)

**H1. Every application of Theorem 1.1.7 in §§4–6** (D.2, Step 4; D.3, Step 3; D.4, Step 4; N.46):
- *Types.* (1.1.5) and (1.1.6) as printed on p. 593. p. 595's "x₀ = (x_{1,0},…,x_{r,0})" confirms the multi-time
  reading. The equal-time products of individually Wick-ordered powers in Q_{n,n′,k,k′} have r = 2 and are of
  type (1.1.5).
- *Degrees.* Every individual degree is ≤ 2p′ < n̄ = 2p′+1. Total local degrees up to 4p′ are admissible, because
  p. 593 bounds only the n_i. Degree-0 factors and constant pieces are harmless.
- *Kernels.* All are in L².
- *Squares.* The localization squares are in R ⊂ B, and Δ ∉ B. They are disjoint even as closed squares, because
  every assigned width is ≥ 1.
- *Strips.* Checked against N.7(i)–(ii) and N.11(iv):
  - (P): from x⁰ = ±½ to x⁰ = l ∓ ½, width j;
  - (T): from x¹ = k_a + 5/2 to x¹ = k − ½, or the mirror case, width j;
  - D.3's P_l: width |l − l_s| − 1 ≥ 1.
- *Cutoff.* h_α = h^B + α(h − h^B) ∈ 𝒞_E (N.5(ii)), which is the class of p. 589.
- *Measure.* The covariance is taken under dq_{h_α}, at that same cutoff.
- *Constant.* (1.1.10) gives O(1)e^{−m₁d}‖Q₁‖‖Q₂‖. The widest strip exists (N.29); w_Δ ≤ d, m₁ > 0 and
  Σ_n‖U_{Δ,n}‖ ≤ c_U then give C₇c_U‖F_a‖e^{−m₁w_Δ}.
- *The mixed pair.* (Sharp-time piece of V(h′)(0)², time-integrated U_{Δ,n}) is covered by "two localized
  monomials Q₁ and Q₂" (p. 594), read with p. 593's "For a localized monomial Q or Q(x₀)". GJS write ‖A‖ for
  (1.1.5) monomials (p. 596), so ‖Q₁‖ is (1.1.8) there.

**H2. F-T is flagged at every transverse application:**
- D.4: the statement (ll. 118–119), Step 4 (ll. 177–179) and §6.4;
- N.12(b); §7 (ll. 192–199); N.48; §8.6 (ll. 322–323).

The transverse class is every square of ring j with |l| ≤ j: 6 squares per ring in rows −1, 0, 1, and 4(j−1) in
rows 2 ≤ |l| ≤ j. Class (P) has 4j+10 squares per ring. I checked this by hand and with an exact script (checks
below).

**H3. The geometry lemmas hold:** N.7, the counterexample N.8, the tilted strip of N.9 (width 2√2), N.11 (count
8j+12, ring 1 = 14 + 6, closed form 4x(5−3x)/(1−x)², the classes) and N.29.

**H4. The base terms hold:**
- Cauchy–Schwarz.
- Z(h^B) ≥ e^{−λ|a₀||B̄|} with |B̄| = 3N_B, resp. 15. Lemma C.2's hypotheses are checked at l. 2902.
- ‖e^{−𝒰_{h^B}}‖₂ ≤ S₂(B) (N.15(iv)).
- S₂ depends on the shape only (N.13 via Lemma C.4). I checked the identity 𝒰_{τ_a h,κ} = 𝒰_{h,κ}∘T_a.
- ‖F(s)‖_{L²(dμ₀)} = ‖F‖_{L²(dφ₀)} (N.33).
- The 3^{p′} comparison (N.21(ii)), conditional on R8: q = 4, t = ½log 3, ‖c‖² = 1/3, e^{2p′t} = 3^{p′}. Its
  transport to the sharp time via J₀ (N.21(i)) is right *for the J₀ object*; finding 1 concerns the other
  construction.

**H5. D.1's chain holds:**
- Step 0. Step 1's linearity of the limits in w (N.26(a)).
- (I1)–(I5), with exponents (2,4,4) and (2,2).
- The convexity dominator W. Dominated differentiation and continuity of N′ and Z′.
- Z > 0, by A3 and continuity. The quotient rule gives −Cov. The fundamental theorem of calculus closes it.
- N.26's majorant: every factor of Π_{Q,j} pairs two distinct integration variables, because N.22's polynomial has
  no diagonal covariance. Hölder with jN exponents 2jN.
- N.23(ii)–(iii): g₀, g₁, b₁ and the rearrangement step.
- Remark N.28 (both sides equal −½).

**H6. D.2, Steps 1–6, hold given D.1, N.5(iv), N.18(iv) and N.30.**
- Form (a), over the charged squares, is needed for D.3.
- mp's example g = 1_{[0,1/10]} + 1_{{3}} is right. Column 3 meets supp g in one point. The squares Δ_{l,3} with
  |l − l_s| ≤ 1 meet supp h_{T,g}, admit only transverse strips, and are not charged.

**H7. Theorems D.3 and D.4 and their constants hold, with D.4 subject to finding 1.**
- The constants: A, B′, c_U, and ‖Q_V‖_GJS ≤ 9K₁K₂^{8p′}(4p′)!λ²(Σ|a_n|)² on columns.
- The φ⁴ arithmetic:
  - 9·8! = 362 880;
  - 24·362 880 = 8 709 120;
  - 81·24 = 1944;
  - (4n−1)!! ≤ 4ⁿ(2n)!, since C(4n,2n) ≤ 16ⁿ;
  - √105 ≤ 96.

**H8. The N_I counterexample holds.**
- I = (0.4,0.6) has N_I = 1 on the cells and N^□_I = 2 on the columns.
- For f even about ½: ‖φ₀(f)‖_GJS = √2K₁K₂²‖f‖₂.
- For Φ(s,f)²: 2·(K₁K₂⁴·2!·½) + 2·(K₁K₂⁴·½) = 3K₁K₂⁴, against (8)'s 2K₁K₂⁴.
- The replaced counterexample of Lemma 6.1 is right, and the column proofs of Lemma 6.1 and Proposition 6.2 run
  verbatim.

**H9. §8 holds.**
- Every quotation of the record's current text matches main.tex: Lemma 4.3(ii) (ll. 1207–1218), Lemma 7.1
  (ll. 1428–1450), Lemma 7.2 (ll. 1462–1464), Lemma 7.3 (ll. 1500–1503), Lemma 7.6 (ll. 1603–1635), Theorem 5.1
  (ll. 1255–1327) and Corollary 5.2 (ll. 1342–1347).
- The replaced Lemmas 7.1–7.3 and 7.6, the radius s₀ = min_{e_j≠0}(2kK_{e_j})⁻¹, and Corollary 5.2 follow from D.3
  and D.4 as claimed. Theorem 5.1, Step 5 does too, subject to finding 1.

**H10. The boundary cases hold:**
- T < 1: for T ≤ ½ only row 0 is charged; D.4 then uses only transverse strips, and D.3 uses none.
- T ∉ ℤ, and T ∈ ½ + ℤ, where the top row is not charged.
- s on a lattice line: l_s = s + ½, P_l's bounding line is x⁰ = s, and the closed squares are separated.
- N_g = 0 and N_g = 1.
- p′ = 1: n̄ = 3, and 9K₁K₂⁸·4! = 216K₁K₂⁸.
- Ring k = 1.
- |Λ| = 0: h = 0 a.e., 𝒰_h = 0, Z = 1, S₂ = 1.
- λ = 0: M_B = 0.
- a ∈ ½ + ℤ: the 3×4 alternative has rings of 8j+10 ≤ 8j+12 squares.

**H11. The note's quotations of GJS pp. 589 and 593–597 match my renders.**

## Not checked

- The V3 repairs R1–R10 themselves. I took them as stated in the V3 report.
- Simon's book, GJS's references [9] and [1], and GJS pages other than 589 and 593–597.
- Whether the transverse case of Theorem 1.1.7 is true. Nothing in the note or the record proves it.
- The GA6 grep and the gates GA1–GA8 and GB1–GB3 (mp's role, and the orchestrator's).
- The drafters' scripts. I read `parts/aqft_checks.out` only.
- The Fubini steps of N.20(iii) and N.26(a)–(d), which I read but did not re-derive line by line.
- The parts of PLAN, and of the record, not named above.

## Checks run

- sha256 of the frozen PDF, as above. `diff -r` of frozen against WORK: identical.
- `WORK/comparison.log`: 0 errors, 0 Overfull, 0 undefined. `pdftotext | grep '??|TODO|Hmm|wait,'`: nothing.
- GA5 greps, re-run in the repository:
  - the record's lines 1210, 1216, 1262, 1313, 1321, 1324, 1346, 1430, 1431, 1436, 1439, 1440, 1449, 1463, 1464, 1502,
    1609, 1614, 1617, 1621, 1631, as the note lists;
  - the 10 replacement blocks: no match (grep exit status 1).
- *Numerical, nothing deduced from it:*
  - `WORK/audits/v1-cqft/glyphs.py` (Python 3.14.7, PIL 12.2.0, numpy 2.5.2) produced the glyph metrics of S1.
  - `WORK/audits/v1-cqft/ringcheck_cqft.py` (exact integers and fractions):
    - |𝓛_j| = 8j+12 for j ≤ 20;
    - class (P) 4j+10 and class (T) 4j+2;
    - every assigned width equals j;
    - no square of class (T) has a parallel strip of width ≥ j;
    - at x = 1/3 the closed form equals 12, the partial sum to 399 terms.

---

# V1b re-check (cqft), 4 November 2026: the repairs on the second frozen version

## Object and what I read

- **Object.** `WORK/frozen-v2/` contains `comparison.pdf` (70 pp, built 3 November 2026 12:42), `comparison.tex`,
  `preamble.tex` and `parts/*.tex`.
  - sha256 of the PDF: `6dd00a9f0f68d8c0b22310c9eead0265cc5e3aad35361152f337d986131f45a2`. I re-checked it on resuming,
    and it was unchanged.
  - `diff -r` of `frozen-v2` against `WORK/parts` and the master shows no difference.
  - `WORK/comparison.log` of that build: 0 errors, 0 Overfull, 0 undefined. `pdftotext | grep '??|TODO|Hmm|wait,'`
    prints nothing.
- **Numbers and pages.** They are from `WORK/comparison.aux` (12:42), saved as `WORK/audits/v1-cqft/v2-labels.txt`:

  | statement | label | page |
  |---|---|---|
  | Lemma N.22 | `aux:notation-sharpid` | 18 |
  | Remark N.23 | `aux:notation-sharpidrem` | 19–20 |
  | Lemma N.28 (mp's moments lemma; the coordinator's "N.26(c), (f)(1)" are N.28(c), N.28(f)(1) in this build) | `aux:d1-moments` | 24 |
  | Lemma N.36 | `aux:d3-cyl` | 35–36 |
  | Lemma N.43 | `aux:d4-QV` | 41 |
  | Lemma D.1 | | 26 |
  | Lemma D.2 | | 31 |
  | Theorem D.3 | | 37 |
  | Theorem D.4 | | 42 |
  | Appendix B | | 68 |

- **Read this round:**
  - `parts/DISPOSITION-aqft.md`, `-mp.md` and `-cqft2.md`, in full.
  - `audits/V2-report.md`: its verdict and V2-1 in full, and the headings of V2-2 to V2-22.
  - In `frozen-v2`, from `notation.tex`: ll. 1–130, 255–286, 700–770 and 771–1192, which contain
    - N.19 with its new part (v);
    - N.20, the GAP, N.21, N.22 and N.23.
  - From the rest of `frozen-v2`:
    - `d1.tex`: ll. 1–30 and 225–633;
    - `d2.tex`: ll. 100–298, plus a diff of ll. 1–103 against `frozen-v1`;
    - `d3.tex` and `d4.tex`: all;
    - `consequences.tex`: ll. 1–160 and 300–543;
    - `quantifiers.tex`: ll. 120–172 and 230–260;
    - `constants.tex`: ll. 163–182, 505–516 and the grep hits for F-T, GAP and CRITICAL;
    - `gates.tex`: all;
    - `comparison.tex`: ll. 14–100.
  - `part_i/C5_reading_record.md`, item 10 (read in the first round).
- The record `main.tex` (mtime 2 Nov 15:35:23) and `ugjs/PLAN.md` (mtime 30 Oct 17:49) are unchanged since round V1.

## Verdict

**D.1, D.3 and D.4 can be recorded "proved, conditional on …" exactly as their status lines claim.**

**D.2 can be recorded so with one correction (V1b-2).**
- Its Step 3 identifies 𝒰_{h−h^B} with the δ_κ-limit of its regularizations.
- Its status line attributes that identification to "repair R8 …, or, on the route written in Step 1, Lemma C.4".
- In the note only the Lemma C.4 route supplies it. R8 yields the linearity of 𝒰_h, not that identification.
- D.3 and D.4 carry R1–R10 and Lemma C.4 anyway, so no downstream status changes.

**My MAJOR (finding 1) is closed.** I audited Lemma N.22 as a new claim and it holds. Remark N.23(a), (b) and (d)
hold. The hypotheses of N.22 (bounded kernel, compact support, 0 ≤ n ≤ 2p′) cover every object it is applied to. D.3's
non-smooth column pieces are covered by N.28(c) with N.28(f)(1), and also by N.22 at n = 1.

**The GAP is placed as claimed.** D.4 does not use it. In §8 it enters only at Theorem 5.1: directly at Step 1, and at
Step 5's transfer, which relies on Step 1. It also enters at Corollary 5.2, and the statements listed in §8.7 inherit
it.

**No CRITICAL or MAJOR finding remains.**

**My 14 MINOR findings:**
- 9 fixed: 4, 6, 7, 8, 9, 12, 13, 14 and 15.
- 2 fixed with a new defect: 2 and 3.
- 3 only partly fixed: 5, 10 and 11, each at an orchestrator-owned place.

**New MINOR findings:** four, V1b-1 to V1b-4.

## Task 1. Lemma N.22, Remark N.23 and their uses, audited as new claims

**Lemma N.22 holds** (`notation.tex` ll. 1076–1169, PDF pp. 18–19). I checked every step.

- **The map J_t.**
  - It is defined on cylinder functions.
  - The laws are preserved, via N.13(i) with a = (t,0): Φ(g)∘T_a = Φ(τ_a g) and (T_a)_*μ₀ = μ₀.
  - The continuity extension gives Φ(0,g)∘T_a = Φ(t,g), because τ_a(δ₀⊗g) = δ_t⊗g and τ_a preserves the covariance
    norm.
  - Hence J_t is an isometry L^p(dφ₀) → L^p(dμ₀), it is multiplicative, and it maps Wick powers at their own variance
    to Wick powers at their own variance.
- **Covariances.**
  - E[Φ_κ(t,x)Φ_κ(t,y)] = (δ_κ∗δ_κ∗G)((0,x−y)), by N.19(v) and the evenness of δ.
  - Γ_{κ,κ′}(x,y) is computed through Φ(η_ε⊗g) → Φ(t,g). That step needs η_ε⊗g → δ_t⊗g in the covariance norm.
    The text says "the reading of N.21(i)" and does not prove it. It is the dominated-convergence computation written
    out in N.28(f)(1), with dominator 4|ĝ(p₁)|²(p²+m₀²)⁻¹, so I accept it.
  - Continuity and boundedness of δ_κ∗G, which pass the ε-limit, follow from ∫G = m₀⁻² in N.19(v).
  - N.19(v) itself checks out: G(ζ) = ∫₀^∞e^{−tm₀²}(4πt)⁻¹e^{−|ζ|²/4t}dt = C(|ζ|), and ∫G = m₀⁻².
- **Inner products.** E[:A^n::B^n:] = n!E[AB]^n holds for Wick powers at their own variances. E[Y²] = I follows from
  N.20(iii), whose proof indeed uses only that the kernel is bounded with compact support.
- **The majorant 9‖δ‖_∞(b₀+2+2|log|u||).**
  - Case |u| ≥ 2ε: G((0,u)−v) ≤ C(|u|/2) ≤ (4π)⁻¹(b₀+2log2+2|log|u||).
  - Case |u| < 2ε: |(0,u)−v| < 3ε ≤ 6/κ ≤ 1. Then
    κ²‖δ‖_∞·2π·(4π)⁻¹·(36/κ²)/2·(b₀+1+2log(κ/6)) = 9‖δ‖_∞(b₀+1+2log(κ/6)), using
    ∫₀^{r₀}r(b₀+2|log r|)dr = (r₀²/2)(b₀+1+2|log r₀|).
  - log(κ/6) < |log|u|| holds because |u| < 4/κ ≤ 2/3.
  - ‖δ‖_∞ ≥ 1/π makes (4π)⁻¹ ≤ 9‖δ‖_∞.
  - The majorant applies to ν = δ_κ (ε = 1/κ) and to ν = δ_κ∗δ_κ (ε = 2/κ, ‖ν‖_∞ ≤ κ²‖δ‖_∞).
  - One remark: the monotonicity of the bound in r₀ that the text proves is not needed, since the radius was only
    enlarged from 3ε to 6/κ.
- **Limits.**
  - (1) As κ′ → ∞, Γ_{κ,κ′} → (δ_κ∗G)((0,·)) boundedly, by the bound κ²‖δ‖_∞m₀⁻². This gives
    E[X_κY] = n!∬ff(δ_κ∗G)^n.
  - (2) As κ → ∞, both integrands converge off the diagonal, dominated by ‖f‖²_∞1_K1_K(9‖δ‖_∞)^n(b₀+2+2|log|x−y||)^n.
  - Hence ‖X_κ − Y‖² → I − 2I + I = 0.
  - It uses only N.13(i), N.19, N.20 and Gaussian identities, so N.23(d)'s "needs no repair of the V3 audit" holds.

**Remark N.23 (`notation.tex` ll. 1171–1191, PDF pp. 19–20).**
- (a) holds: N.28(a) gives the limit, N.22 identifies it, and N.28(c) with the multiplicativity of J_t gives the
  product kernels.
- (b) holds: Q_{n,n′,k,k′} = λ²a_na_{n′}J₀W_n(h′_k)J₀W_{n′}(h′_{k′}), and W_n(h′) = Σ_kW_n(h′_k) by linearity of the
  regularized integrals. The n = 0 factors are the constants ∫h′_k, and X_κ = J₀W₀ trivially.
- (d) holds.
- (c) is right for f ∈ C_c^∞, but its last clause overstates (V1b-1).

**The uses, and whether the hypotheses cover them:**
- **D.4** (`d4.tex`): the setting (ll. 22–39), Lemma N.43(i) and its proof (ll. 76, 100–112), Step 1 (ll. 163–170),
  Step 2 (ll. 177–181) and Step 4 (ll. 209–211).
  - Every kernel h′_k = h′1_{[k−½,k+½)} is real, measurable, bounded by 1, and vanishes outside one column.
  - Every degree satisfies 0 ≤ n, n′ ≤ 2p′.
  - N.22 and N.23(a)–(b) therefore apply.
  - The base term (Y² through N.21) and the comparison term (the N.26(b) pieces through D.2) now concern one element of
    L²(dμ₀).
- **§8.6:** the Theorem 5.1 block and its Check (`consequences.tex` ll. 353–384, PDF p. 57) concern the same objects.
- **aux:d3-cyl(vi)** (`d3.tex` ll. 131–135 and 155–168, PDF p. 36).
  - The pieces f_i1_{[κ_i−½,κ_i+½)} are in L², have bounded support, and are not smooth.
  - N.28(c) gives the product, and N.28(f)(1) the identification with Φ(s, f_i1_col). I checked the proof of
    (f)(1) (`d1.tex` ll. 405–412): the test-function integral, and the Fourier computation with the integrable
    dominator 4|f̂(p₁)|²(p²+m₀²)⁻¹, whose p₀-integral is 4π|f̂|²(p₁²+m₀²)^{−1/2}.
  - The linearity and isometry of f ↦ Φ(s,f) give Σ_κQ_κ(s) = Q(s) a.e.
  - Because the pieces are bounded, N.22 at n = 1 covers them as well.
- **Other citations:** N.28(f)(2), N.27 (`d1.tex` ll. 238–245, 285–293, 414), Appendix A (`constants.tex` ll. 168–171
  and A.6 (C7), ll. 507–515), §7 (`quantifiers.tex` ll. 194–195, 243–244), and the sentence after N.21
  (`notation.tex` ll. 1072–1074). All cite N.22 and N.23 within their hypotheses.
- I found no application to an unbounded kernel or to a degree above 2p′.

## Task 2. Dispositions of my 14 MINOR findings

| # | claimed | verified at (frozen-v2) | verdict |
|---|---|---|---|
| 2 (the reading not named; mollifier) | fixed | N.27, `d1.tex` ll. 238–245 (p. 23); N.28(e), statement l. 270, proof ll. 391–403 (p. 24; checked: the cross term (δ_κ∗δ′_{κ′})∗G with the M₁ majorant, and limit I_Q); N.2(iv), `notation.tex` ll. 118–128 (p. 4); D.2 Step 4 bullet "The objects", `d2.tex` ll. 231–235, and D.2's status line; after N.43, `d4.tex` ll. 96–98; master inputs ll. 79–80 | fixed, **with a new defect** (V1b-4) |
| 3(a) (D.1 plainly "proved") | fixed | D.1 status, `d1.tex` ll. 452–469 (p. 26); N.29(b), ll. 594–597; Step 1, ll. 500–502 | fixed in §3; the gate record's version is **new defect** V1b-3 |
| 3(b) (D.2: C.2/C.5 vs C.4) | fixed | `gates.tex` ll. 9–10; D.2 status, `d2.tex` ll. 143–151 (p. 31) | the C.2/C.5 attribution is fixed; the "R8, or C.4" alternative is **new defect** V1b-2 |
| 3(c) (C.2 at R1–R10) | fixed | `d1.tex` l. 562 ("conditional on repair R8") | fixed |
| 4 (the GAP at Lemma 4.3(ii) and Theorem 5.1) | fixed | §8 intro, `consequences.tex` ll. 31–46 (p. 51); block `lemma-4.3-ii`, ll. 105–127 (moment bound for the §7 cylinder monomials only; A5(i) for \|V(h)\|); Check, ll. 132–135 (the record applies (ii) only to cylinder monomials, ll. 1462, 1501; Theorem 5.1 Step 5 uses part (i), l. 1320: both checked in main.tex); gapnote ll. 997–1003 | fixed |
| 5 (N_I repair; "no other statement changes") | fixed | block `sec6-NI`, `consequences.tex` ll. 57–77 (p. 52): l. 448, A8(ii) ll. 659–663, l. 1359, Lemma 6.1's statement, the proofs of 6.1 and 6.2, and Theorem 5.1 Steps 2–4 on columns (Step 2's count rechecked: k_max − ½ ≥ k_min + 5/2); a grep of main.tex finds no other cell count except Appendix B's history, l. 2729; §8 intro ll. 17–29 lists the changed statements | **partly fixed**: the master's sentence is unchanged (R-5) |
| 6 (severity of E1) | fixed | N.37, `d3.tex` ll. 189–192 (p. 36), with the new lower bound over one-factor degree-1 decompositions (checked: injectivity of f ↦ Φ(s,f), then the triangle inequality per column); §8.9; A.5 (D1), `constants.tex` l. 417 | fixed |
| 7 ("the case the printed proof reaches") | fixed | N.39, `d3.tex` ll. 330–341 (p. 39); D.3 status ll. 263–264; §6.4 (P) bullet, `d4.tex` ll. 250–252; the master's "Theorem D.3 uses the parallel case only" (l. 56) is accurate as it stands | fixed |
| 8 (F-T not carried downstream) | fixed | §8.7 "Disclosure", `consequences.tex` ll. 430–433 (p. 58); Theorem 5.1 block ll. 361–364; Corollary 5.2 block ll. 397–398 (p. 57); §7 ll. 236–239, 253–255; Appendix A rows `constants.tex` ll. 383, 386, legend ll. 311–320 | fixed |
| 9 (l. 1449) | fixed | `consequences.tex` l. 149 (p. 53): "l. 1448" | fixed |
| 10 (D.2(b) is not PLAN's form) | fixed | `d2.tex` ll. 126–127; §8.9 bullet "The form of Lemma D.2" | **partly fixed**: the gate record is unchanged (R-10) |
| 11 (input lists omit C.4) | fixed | master inputs `comparison.tex` ll. 68–81 (C.4 now listed); `d1.tex` ll. 14–18; `notation.tex` ll. 32–46; N.34, `d3.tex` ll. 62–64; N.42, ll. 392–396 | **partly fixed** (R-11) |
| 12 (N.18(iii) and a₀) | fixed | `notation.tex` ll. 715–722 (p. 12), statement and proof | fixed |
| 13 (F-T not verbatim) | fixed | `comparison.tex` ll. 50–56 (p. 2): PLAN Part 8's sentence verbatim, bracket deferred to integration | fixed |
| 14 (§7: N^col_I; s₀) | fixed | `quantifiers.tex` l. 128 (N^□_I); ll. 159–170 (e_j ≠ 0; s₀ := +∞ if all e_j = 0); `grep 'rm col'` over all parts: no hit | fixed |
| 15 ("0(1)" silently corrected) | fixed in the note | `gates.tex` ll. 38–46 (p. 68): confirmed and recorded, with the [sic] deferred to integration | fixed as far as the note can be: main.tex is unchanged (no edits before integration); PLAN.md has no Part 9b entry (unchanged since 30 Oct); I did not check the KB correction node the gate record names (no kb access) |

**The residuals of findings 5, 10 and 11 (all MINOR):**

- **R-5.**
  - *Locator:* `comparison.tex` ll. 58–62 (PDF p. 2).
  - *Text:* "changes no statement except through the value of the constants that contained $C_8$".
  - *Why:* §8's own introduction now says otherwise. Lemma 6.1's statement and the content of Proposition 6.2
    change through N_I, and Lemma 7.1's statement "changes its form, gaining the term $A\|Q^2\|_{L^2(d\phi_0)}$".
    (The radius is now correctly placed "in the proof of Theorem 7.7".)
  - *Repair:* point to §8's list.
- **R-10.**
  - *Locator:* `gates.tex` ll. 26–27 (PDF p. 68).
  - *Text:* "from which the plan's form (b) follows".
  - *Why:* the plan's form admits width-0 separation, and (b) does not.
  - *Repair:* use `d2.tex` ll. 126–127's wording, "a form of the plan's statement, with positive widths".
- **R-11.**
  - *The status box,* `comparison.tex` ll. 28–29 (p. 1): "with the record's Lemma~C.2 and Theorem~C.5, yields the
    uniform local moment". It still omits Lemma C.4.
  - *The input list,* ll. 68–81, omits two inputs the sections use:
    - Remark 2.5 (N.21(i), N.35, §8 intro l. 44);
    - Assumption A5(i) (the `lemma-4.3-ii` block).

## Task 3. The status lines after D.1–D.4, and the gate record's status paragraph

**D.1** (`d1.tex` ll. 452–469, PDF p. 26).
- *Claim:* "Proved, conditional on repair R8"; on the Step-1 route, conditional on Lemma C.4.
- *What the proof uses:*
  - A2, through N.24, N.25 and N.28;
  - A3, at h₁, h₂ and h_α;
  - the linearity of the record's 𝒰_h. Under R8 it holds by definition, since R8's :Φⁿ(g): is fixed by pairings
    linear in g. On the route written in Step 1 it comes from the identification with lim 𝒰_{h,κ}, that is from
    Lemma C.4.
- *Verdict:* matches.

**D.2** (`d2.tex` ll. 143–151, PDF p. 31). Matches except for the R8 alternative (V1b-2).
- It uses D.1 and N.5(i)–(iii).
- It uses N.28(a) for the one-square pieces U_{Δ,n} (Step 3 no longer goes through N.5(iv) or N.18(iv)) and N.32
  (A3).
- It uses Source Fact 2.2 under the reading named in its status line, and no C.2 or C.5.
- It does use the identification 𝒰_{h−h^B} = lim U^{(κ)}_w at Step 3, ll. 172–175.

**D.3** (`d3.tex` ll. 259–265, PDF p. 38). Matches. The proof uses:
- D.2, and N.36(vi), which needs no repair;
- C.2 (R8);
- N.15(iv), with Theorem C.5 (R1–R10), and N.15(iii), through N.13(iii) and Lemma C.4 (named in the line);
- N.35 (A2, Remark 2.5);
- parallel strips only, with a time-integrated partner.

The "(repair R8 …)" attached to "Lemma D.1, through Lemma D.2" understates what D.2 needs (V1b-2). The line lists
R1–R10 and Lemma C.4 anyway, so the conditions are sufficient as a whole. It does not name the reading that D.2
inherits (V1b-4).

**D.4** (`d4.tex` ll. 153–160, PDF p. 42). Matches.
- The listed conditions are what the proof uses:
  - D.1 through D.2;
  - C.2 (R8);
  - C.5 with N.15, including the common value at all 3×5 boxes, i.e. N.15(iii) and with it Lemma C.4 under R1–R10;
  - R8 for N.21(ii);
  - F-T.
- "It does not use the GAP" holds:
  - the setting defines V(h′) := λΣa_nW_n(h′) of N.20(iv), the constructed object (ll. 22–39);
  - V_* is taken for it (ll. 60–63);
  - Y = J₀V(h′) (N.21);
  - N.22 needs no repair (N.23(d)).
- The record's V(h) appears nowhere in D.4's proof.
- The same remarks on R8 and the reading apply as for D.3.

**Gate record**, `gates.tex` ll. 2–23 (PDF p. 68):
- **D.1:** its parenthetical misdescribes R8 (V1b-3).
- **D.2:** "conditional on Lemma D.1 and its condition" inherits V1b-2.
- **D.3 and D.4:** match the lines above.
- **The GAP sentence holds:** "it enters only at Step 1 of the record's Theorem 5.1 and at Corollary 5.2 (§8), not in
  the Euclidean Theorem D.4". I checked every replaced text of §8:
  - §8.2 (Lemma 4.3(ii)): no GAP; A5(i) serves for |V(h)|;
  - §§8.3–8.5 (Lemmas 7.1–7.3, 7.6, Theorem 7.7): cylinder monomials only;
  - §8.6: Step 1, kept, and Step 5's transfer, which uses the identification "as in Step 1" (ll. 361–364, 375–378);
  - Corollary 5.2's block (ll. 397–398).

  §8.7's "Disclosure" (ll. 430–433) records that the statements carrying M inherit it.
- **A wording difference, not a defect.** The gapnote (`notation.tex` ll. 997–1000) and D.4's setting name "Step 1 …
  and the transfer (§8.6)". The gate record names "Step 1 … and Corollary 5.2". Both are true.

## New findings (V1b), all MINOR

**V1b-1. Remark N.23(c) claims to cover D.3's pieces, which are not smooth.**
- *Locator:* `notation.tex` ll. 1186–1188 (PDF p. 20).
- *Text:* "(c) At degree $1$ and $f\in C_c^\infty(\R)$, … and covers the cylinder pieces of Theorem~\ref{thm:D3}."
- *Why:* the pieces to which Lemma D.2 is applied in D.3 are f_i1_{[κ_i−½,κ_i+½)}, which are not in C_c^∞.
  `d3.tex` ll. 165–168 says so itself. (c) covers only the unsplit factors f_i.
- *Repair:* "covers the unsplit cylinder factors; the column pieces are covered by Lemma N.22 at n = 1 and by N.28(f)(1)".

**V1b-2. D.2's status line offers R8 as a sufficient alternative, but Step 3 needs the identification that only the
C.4 route supplies.**
- *Locators:* `d2.tex` ll. 143–146 and Step 3 ll. 172–175 (PDF pp. 31–32); `gates.tex` ll. 9–10.
- *Text:*
  - status line: "Proved, conditional on Lemma~\ref{lem:D1} with its condition: repair R8 of the V3 audit, or, on the
    route written in Step~1 of its proof, Lemma~C.4 … Lemma~\ref{lem:D2} inherits that condition through the
    identification of $\Uc_{h-h^B}$ with a limit of regularizations (Step~3)";
  - Step 3: "its limit is $\Uc_h-\Uc_{h^B}=\Uc_{h-h^B}$; this last identification is the condition of
    Lemma~\ref{lem:D1}".
- *Why:* by D.1's own status paragraph (`d1.tex` ll. 455–461), R8 supplies the linearity of 𝒰_h. The identification of
  the record's 𝒰_h with the δ_κ-limit is what "Lemma C.4 … gives under the repairs R1–R10". Under R8 alone, Step 3
  would also need R8's :Φⁿ(w): to equal the δ_κ-limit, and the note does not write that step.
  - It is a short computation. The limit lies in Γ_n.
  - Its pairing with :Φ(f₁)⋯Φ(f_n): is lim n!∫w(z)∏_j(δ_κ∗Gf_j)(z)dz = n!∫w∏_j(Gf_j), which is (V.3).
  - So the two are equal.
- *Repair:* either state D.2 (and the gate record's D.2) as conditional on Lemma C.4 (R1–R10, which include R8), or add
  the identification above under R8.
- *Effect:* none on D.3 or D.4, which carry R1–R10.

**V1b-3. The gate record calls R8 "the identification".**
- *Locator:* `gates.tex` ll. 6–8 (PDF p. 68).
- *Text:* "Lemma~\ref{lem:D1} proved, conditional on repair R8 of the V3 audit (the identification of the record's
  $\Uc_h$ with the $L^2$-limit of its regularizations $\Uc_{h,\kappa}$; on the Step-1 route, conditional on
  Lemma~C.4, R1--R10)".
- *Why:* D.1's status paragraph assigns the identification to the C.4 route and the linearity to R8. The parenthetical
  reverses this.
- *Repair:* "(R8 makes $h\mapsto\Uc_h$ linear; on the Step-1 route the identification with the $L^2$-limit rests on
  Lemma C.4, R1–R10)".

**V1b-4. The reading is said to be named beside the status words, but only D.2's line names it.**
- *Locator:* Remark N.2(iv), `notation.tex` ll. 126–127 (PDF p. 4).
- *Text:* "It is named beside the status words with C5 item~10."
- *Why:* the reading is that the note's limits are GJS's monomials and that 𝒰_h is GJS's V(h). It is named in D.2's
  status line and after N.43, but not in the status lines of D.3 (`d3.tex` ll. 259–265) or D.4 (`d4.tex` ll. 153–160),
  nor in the gate record's status paragraph. Both theorems inherit it through D.2.
  C5 item 10 (`part_i/C5_reading_record.md`) is a verbatim check of (1.1.5)–(1.1.6). It confirms the text the reading
  rests on; it is not the reading.
- *Repair:* add "and the reading of Remark N.2(iv)" to the status lines of D.3 and D.4 and to the gate record.

## Checks run (V1b)

- sha256 of `frozen-v2/comparison.pdf` (twice), `diff -r` against WORK, the build-log counts, the `pdftotext` grep, and
  the label table from `WORK/comparison.aux`: results as above.
- `grep 'rm col'` over `frozen-v2/parts/*.tex`: no hit.
- `grep sharpid` over all parts: the citation list I worked through in task 1.
- `stat` of main.tex and PLAN.md: unchanged since round V1.
- No numerics this round. Every check above was made by hand on the text.

## Not checked (V1b)

- V2's findings other than V2-1, and mp's V1 findings and their dispositions. Neither is my brief.
- The GA5 and GA6 lists, and the record lines that §8.8 newly adds (ll. 68, 72, 76, 81, 184, 210).
- The KB correction node named in `gates.tex`, since I have no kb access.
- The parts of `quantifiers.tex`, `constants.tex` and `consequences.tex` outside the lines listed above, including the
  Lemma 7.1 case L = 0 and the replaced Lemma 7.6.
- Simon's book.
- The record beyond the lines cited.

---

# V1c closing pass (cqft), 4 November 2026: the third frozen version

## Object and what I read

- **Object.** `WORK/frozen-v3/` contains `comparison.pdf` (72 pp, built 4 November 2026 18:30), its master, preamble and
  `parts/`.
  - sha256 of the PDF: `1451af6e6a27c4181b1849b4f22ca71d39a947ebef0ff96237d08a36c9fa6829`.
  - The parts and the master are identical to WORK's (`diff -r`).
  - `WORK/comparison.log` (18:30): 0 errors, 0 Overfull, 0 undefined. `pdftotext | grep '??|TODO|Hmm|wait,'` prints
    nothing.
  - The label table is from `WORK/comparison.aux` (18:30), saved as `WORK/audits/v1-cqft/v3-labels.txt`:

    | statement | page |
    |---|---|
    | Remark N.2 | 3 (item (iv) on p. 4) |
    | Remark N.12 | 10 |
    | Lemma N.22 | 18 |
    | Remark N.23 | 20 |
    | Lemma N.28 | 24 |
    | Lemma D.1 | 27 |
    | Lemma D.2 | 31 (status line p. 32) |
    | Lemma N.36 | 36 |
    | Theorem D.3 | 38 |
    | Theorem D.4 | 42 (status line p. 43) |
    | §7.2 | 47 |
    | §8 | 52 |
    | Lemma N.48 | 61 |
    | A.4 legend | 65 |
    | Appendix B | 69 |

- **Read:**
  - the dated re-check sections of `parts/DISPOSITION-aqft.md`, `-cqft2.md` and `-mp.md`;
  - `diff` of every part and of the master between `frozen-v2` and `frozen-v3` (`d1.tex` is unchanged);
  - in full, the changed passages and their surroundings:
    - `notation.tex` ll. 28–40, 118–135, 536–548 and 1176–1206;
    - `d2.tex` ll. 141–218;
    - `d3.tex` ll. 259–270;
    - `d4.tex` ll. 94–99 and 153–166;
    - `quantifiers.tex` ll. 60–80 and 95–110;
    - `constants.tex` ll. 19–40 and 308–322;
    - `gates.tex`, all;
    - `comparison.tex` ll. 17–90;
  - `parts/cqft2_ringcheck.output.txt`;
  - V2-13 and V2-20 in `audits/V2-report.md`.
- `V1-cqft-report.md` itself was unchanged since my V1b append: same 8003 words, same tail.

## Item by item

| item | verified at (frozen-v3) | verdict |
|---|---|---|
| **V1b-1 / V2b-4.** Remark N.23(c) | `notation.tex` ll. 1192–1202, PDF p. 20. (c) now claims only "the unsplit factors $\Phi(s,f_i)$, $f_i\in C_c^\infty(\R)$". It says the pieces $f_i\mathbf 1_{[k-\frac12,k+\frac12)}$ "need not be smooth" and attributes them to N.22 at n = 1 through (a), whose hypotheses they meet (bounded, vanishing outside one column), and to N.28(f)(1). It also says that N.36(vi) uses the latter, with N.28(c), which is true (`d3.tex` ll. 155–168). | **closed**, no new defect |
| **V1b-2 / V2b-1.** D.2's condition | **D.2's status line** (`d2.tex` ll. 143–153, p. 32): "conditional on Lemma~C.4 of the record (repairs R1--R10 of the V3 audit, which include R8)", with "Repair R8 alone makes $h\mapsto\Uc_h$ linear but does not give that identification as this note is written". **Step 3** (ll. 171–206): Lemma C.4 is quoted, and the quotation matches main.tex ll. 2970–2975 (lemma environment from l. 2968), which I read in round V1. Its hypotheses are checked for h and h^B with Λ := supp h; supp h^B ⊆ supp h by N.5(i), and κ ≥ 2. U^{(κ)}_w = 𝒰_{h,κ} − 𝒰_{h^B,κ} holds pointwise by linearity in w, so U^{(κ)}_w → 𝒰_h − 𝒰_{h^B} = 𝒰_{h−h^B}, D.1's definition. **D.3's and D.4's parentheticals** (`d3.tex` ll. 260–261, `d4.tex` ll. 153–154) read "(Lemma~C.4, R1--R10, as stated after Lemma~\ref{lem:D2})". **§7** (`quantifiers.tex` ll. 99–107, 129–131, 204–205, 219–220) and the **§8 dependence paragraph** (`consequences.tex` ll. 31–38) match. | **closed**, no new defect |
| **V1b-3 / V2b-3.** The gate record's D.1 | `gates.tex` ll. 6–9, p. 69: "(which supplies the linearity of $h\mapsto\Uc_h$ and, with Lemma~C.4 on the Step-1 route (R1--R10), the identification …)". R8 is credited with the linearity, and the identification with the Lemma C.4 route. This agrees with D.1's status paragraph (`d1.tex` ll. 452–469) and with §7 (`quantifiers.tex` ll. 76–79). The gate record's D.2 and D.3 entries (ll. 9–13) now carry Lemma C.4 (R1–R10). | **closed**, no new defect |
| **V1b-4 / V2b-5.** Where the reading is named | **Remark N.2(iv)** (`notation.tex` ll. 128–132, p. 4): "named in the status lines of Lemma~D.2 and Theorems~D.3--D.4 and in Appendix~B". **The lines themselves:** `d2.tex` ll. 150–152; `d3.tex` ll. 263–266; `d4.tex` ll. 158–161; `gates.tex` ll. 24–27. **C5 item 10** is described as "still open, asks a human reader to confirm the printed text of (1.1.5)--(1.1.6) and of the multi-time notation (pp.~593, 595) on which the reading rests; it does not check the reading itself". That matches `C5_reading_record.md` item 10 as I read it: items (a)–(d), verdict blank. | **closed**, no new defect. One cosmetic point: the gate record's and the master's one-line summaries of the reading omit its second half ("the record's 𝒰_h is GJS's V(h)"); both cite Remark N.2(iv), which contains it. |
| **V2b-2.** §7's description of D.2's route | `quantifiers.tex` ll. 99–107. It matches `d2.tex`'s Step 3: Step 1 of D.1 with N.28(a) for the convergence, N.5(iii) for the split, and Lemma C.4 for the identification. N.18(iv) and N.5(iv) are no longer cited there. | **closed** |
| **V2b-6.** Appendix A.4 marks | `constants.tex` ll. 313–318 (legend, p. 65) and ll. 339, 348 (rows, p. 66). The rows C₇c_U and B′ are now "cond.". The legend assigns R1–R10 where the comparison bound of N.48 is used: through Lemma C.4 in N.18(iv) and N.5(iv), N.48's own route, and through D.1's condition. The §2 introduction (`notation.tex` ll. 36–39) agrees. | **closed** |
| **V2-16.** F-T at the last sentence of N.48 | `constants.tex` ll. 37–40, p. 61: "where a strip so chosen is transverse to the time-zero line and some $F_a$ is of type (1.1.5), this form uses the transverse case …". This is worded as in D.2(b), and it is right to restrict the clause to sharp-time F_a. | **closed** |
| **V2-18.** The ring-check run record | `notation.tex` ll. 542–546, p. 10, cites `parts/cqft2_ringcheck.output.txt`. The file is in `frozen-v3/parts/`; its header reads "run: 2026-11-03 12:08 CET; interpreter: /usr/local/bin/python3 … 3.14.7", with numpy 2.5.2 and scipy 1.18.1, and it ends "ALL CHECKS PASSED". `cmp` against `build-cqft2/ringcheck-output.txt`: identical (sha256 prefix b2a4a34767503195). One pre-existing point, outside the item: the "relative tolerance $10^{-11}$" stated in N.12(c) is set in the script (`epsrel=1e-11`, `cqft2_ringcheck.py` ll. 117, 119) but not printed in the output (AGENTS 6.6). | **closed** |
| **R-5.** The statements the note changes | `comparison.tex` ll. 58–64, p. 2: "the statements it changes are listed in §8: those whose constants contained $C_8$ (…; Lemma~7.1, whose form changes; …) and those that carry the count $N_I$ … (Lemma~6.1 and the displays (7)--(8) of Proposition~6.2, with the notation table and A8(ii))". This agrees with §8's introduction. | **closed** |
| **R-10.** The wording of form (b) | `gates.tex` ll. 31–33, p. 69: "a form (b) of the plan's statement, with strips of positive width". | **closed** |
| **R-11.** The status box and the input list | **Status box** (l. 28–29, p. 1): now "Lemma~C.2, Lemma~C.4 and Theorem~C.5". **Inputs** (ll. 69–83, p. 2): now include A5(i) "for $\lvert V(h)\rvert$ in the replaced Lemma~4.3(ii)" and Remark 2.5; Lemma 7.4 is removed, correctly, since no proof of the note uses it as a premise. | **closed**, with one new wording defect: V1c-1 |
| **V2-13.** The input list | `comparison.tex` ll. 69–83. A2, Lemma 3.1, A5(i), Lemma 6.1, Remark 2.5 and Lemma C.4 are present. A4 is now "through Theorem~C.5 and the $3^{p'}$ comparison", and Lemma 7.4 is removed. | **closed except one part:** the qualifier V2-13 asked for on "No new import is made" (l. 82–83) is not in the master. §2's introduction has it (`notation.tex` l. 46: "its conditional statuses rest on the import paragraph R8 …"). MINOR residual. |
| **V2-20.** Slips | `comparison.tex` l. 18: "Status (4 November 2026)". ll. 66–67: "The open human readings it rests on, C5 items 1--4 and 10--13 …". `notation.tex` l. 905: Proposition 3.2 at the record's p. 16. | **closed** |

**V1c-1 (MINOR, new wording defect in the master's input list).**
- *Locator:* `comparison.tex` ll. 73–74, PDF p. 2.
- *Text:* "Definition~2.1, Remark~2.5 and Lemma~3.1 (the classes and the working coordinates)".
- *Why:* the parenthetical mislabels two of the three items.
  - Definition 2.1 and Lemma 3.1 are the classes.
  - Remark 2.5 is the conventions lock (the sharp-time covariance and the Wick ordering).
  - The working coordinates are the record's §2.6 with Proposition 3.2 and Remark 3.3 (pp. 14–16). The note uses
    them throughout, and §2's own input list names them (`notation.tex` ll. 39–41), but the master does not.
- *Repair:* "Definition 2.1 and Lemma 3.1 (the classes), Remark 2.5 (the conventions lock), §2.6 with Proposition 3.2
  and Remark 3.3 (the working coordinates)".

## Final word on D.1–D.4

D.1–D.4 can be recorded exactly as their status lines and the gate record's status paragraph (`gates.tex` ll. 2–28)
now claim. I matched each line against what its proof uses.

- **Lemma D.1:** "proved, conditional on repair R8", which supplies the linearity of h ↦ 𝒰_h. On the route written in
  Step 1 it is conditional on Lemma C.4 (R1–R10).
- **Lemma D.2:** proved, conditional on:
  - Lemma C.4 (R1–R10, which include R8), at Step 3 and for D.1's condition;
  - the reading of Remark N.2(iv);
  - F-T, wherever a transverse strip meets a sharp-time F_a.

  It uses neither Lemma C.2 nor Theorem C.5.
- **Theorem D.3:** proved, conditional on:
  - D.1 through D.2 (Lemma C.4, R1–R10);
  - Lemma C.2 (R8);
  - Theorem C.5 with Proposition N.15 (R1–R10), whose part (iii) rests on Lemma C.4;
  - the reading.

  Its strips are parallel only, with a time-integrated partner. It uses no transverse case, no GAP and no Theorem 1.1.11.
- **Theorem D.4:** proved, conditional on:
  - the same conditions as D.3, with N.15's common value at all 3×5 boxes;
  - R8 for N.21(ii);
  - the transverse case of Theorem 1.1.7 at the printed scope (F-T);
  - the reading.

  It does not use the GAP, and Lemma N.22 needs no repair.

The gate record's GAP sentence holds as checked in V1b: the GAP enters only at the record's Theorem 5.1, Step 1, on
which Step 5's transfer relies, and at Corollary 5.2.

No CRITICAL, MAJOR or blocking MINOR finding remains. What is left is MINOR and does not touch any status:
- V1c-1;
- the missing qualifier on "No new import is made" (V2-13);
- the unprinted quadrature tolerance in the ring-check output;
- the cosmetic one-line summaries of the reading.

As the master and the gate record state, the note as a whole stays *conjectured* until the gates of PLAN Part 3 are
recorded as passed, and nothing in it is a theorem of the record before integration (Checkpoint 2). The gate record
marks the closure of this residue as "pending (4 November 2026)"; this pass is the check that closes it.

## Checks run (V1c)

- sha256 of `frozen-v3/comparison.pdf`, `diff -r` against WORK, the build-log counts, the `pdftotext` grep and the
  label table: results as above.
- `cmp` and sha256 of `cqft2_ringcheck.output.txt`. A grep for `tol|epsrel` in that output and in the script: the
  tolerance appears in the script at ll. 117 and 119 and not in the output.
- `grep 'new import|working coordinates'` over the master and §2: results as above.
- No numerics. Every check was made by hand on the text.

## Not checked (V1c)

- The new gate entries GA1–GA8 and GB1–GB3 (`gates.tex` ll. 92–140), beyond the observation that GA1's and GA2's
  descriptions of round V1 agree with this report. In particular I did not check the commit hash 4166883 that GA8
  names, the record's Appendix B, or `README`/`docs` (GB2).
- The V2b section of `V2-report.md` beyond the item list the coordinator gave.
- mp's and aqft's dispositions of items that are not in that list.
