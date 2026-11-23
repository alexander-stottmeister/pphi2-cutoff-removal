# Route T note: audit of its claims about the sources and about what rests on what

Auditor: `route-t-audit-sources`, working council of 23 November 2026 (an AI agent). Date: 23 November 2026.

**Object.** `ugjs/route_t/route_t.tex`: the draft of 23 November 2026, 1492 lines, 25 pages, audited in
the council's scratch area. It is read against:
- the record, `part_i/main.tex` at commit 49f2d23 (8744 lines; numbers and pages from `part_i/main.aux`);
- GJS = Glimm, Jaffe, Spencer, Ann. of Math. 100 (1974) 585–632 (the copy in `refs/`, which is not in
  the repository);
- Simon's book (the copy in `refs/`).

My commission covers items 1–5: the source claims and the dependency claims. The analysis in Lemmas
T.3–T.16 is the other auditor's part.

**Locators.**
- Note: number, label and page from `route_t.aux`, plus line numbers of `route_t.tex`.
- Record: number, label and page from `main.aux`, plus line numbers at 49f2d23.
- GJS: printed page / PDF page, with printed = PDF + 583. I verified the offset: PDF 2 begins §1, which
  the table of contents puts on p. 585, and the header of PDF 10 reads 593.
- Simon: printed = PDF − 22. Verified: PDF 185 carries the header 163.

## 1. Outcome

The note quotes GJS and Simon exactly. Every application of GJS Theorem 1.1.7 that the note makes
(P1–P4) lies within the printed statement. Its case-by-case verdicts on what the printed proof reaches
are correct in substance, and so is its account of where Theorem 5.1, Theorem D.4 and A8(iv)-T enter
the record. I found no CRITICAL and no MAJOR defect, and twelve MINOR ones. Two of the MINOR findings
matter for the author's decision:
- F1: the note under-reports the printed evidence for reading R1 (pp. 600, 628–629).
- F2: its Summary omits that Route T adds one input, Simon's Remark on p. 164, which goes beyond A2 as
  the record states it.

## 2. Claims checked

| # | Claim in the note (locator) | Checked against | Verdict |
|---|---|---|---|
| S1 | GJS: Ann. of Math. 100 (1974), no. 3, 585–632; Glimm, Jaffe, Spencer (§1.1, p. 2, ll. 106–109) | JSTOR cover page (PDF 1): "Annals of Mathematics, Vol. 100, No. 3 (Nov., 1974), pp. 585-632"; first page p. 585 (PDF 2) | holds |
| S2 | Images `gjs-theorems-10/11/12`, `gjs-thm1111-13`, `gjs-proof-14` show pp. 593–597 = PDF 10–14 (ll. 110–113) | page headers of the five images; my own renders of PDF 10–14 | holds |
| S3 | p. 593: (1.1.5), (1.1.6), the "localized" sentence (§5.1, p. 17, ll. 1077–1080) | p. 593 (PDF 10) | holds, verbatim |
| S4 | p. 594: the strip sentence ("no period in the source"), Theorem 1.1.7, (1.1.10) (ll. 1081–1087) | p. 594 (PDF 11) | holds, verbatim |
| S5 | p. 595: "We apply Theorem 1.1.7 to each term in the sum to obtain", the sum over i ∈ Z²∩supp g, the ordered-times sentence, Theorem 1.1.8 (ll. 1088–1094) | p. 595 (PDF 12); p. 594 for "f_i ∈ C_0^∞(O)" | holds, verbatim |
| S6 | p. 596: the A and B sentence, the equal-times sentence, Q(T) of Theorem 1.1.10, Theorem 1.1.11 "with r = 1", (1.1.16) (ll. 1095–1102) | p. 596 (PDF 13) | holds, verbatim |
| S7 | "Corollary 1.1.9 … applies Theorem 1.1.8 to ``Q_1 = …''" (ll. 1102–1104) | p. 596 prints "Apply the theorem to" | gap, MINOR (F8) |
| S8 | p. 597: the rotation sentence (ll. 1105–1107) | p. 597 (PDF 14) | holds, verbatim |
| S9 | p. 629: "the estimates of Theorems 1.1.8, 1.1.11, 3.1 and 4.1 are uniform in the space cutoff h" (p. 19, ll. 1184–1185) | p. 629 (PDF 46, `gjs-uniform-46`) | holds; the printed sentence begins "The" |
| S10 | Theorem 1.1.1 glossed as "(convergence of the Schwinger functions)" (ll. 1167–1168) | p. 590 (PDF 7) | gap, MINOR (F8) |
| S11 | Simon Theorem V.15, p. 163, quoted (Lemma T.15 `lem:fkn`, p. 14, ll. 940–944) | p. 163 (PDF 185; `simon-fkn-185`) | holds, verbatim |
| S12 | Simon p. 164: "where s_0 is arbitrary …" and the Remark (ll. 944–947) | p. 164 (PDF 186) | holds, verbatim (the quotation stops before "and not only if …") |
| S13 | A2 "imports this theorem (it cites Simon's Corollary V.14 and Theorem V.15)"; Simon's H is the record's K(g); Lemma 4.1 is the symmetric two-time case (ll. 947–950) | A2 (`A:fkn`, A2, p. 13, ll. 825–841); l. 558 (K(g) := H_0 + V(g)); Lemma 4.1 (`lem:slabFKN`, 4.1, p. 25, ll. 1725–1735) | the citation, H = K(g) and Lemma 4.1 hold; "imports this theorem" is a gap, MINOR (F2): A2 is stated for bounded functions |
| S14 | (V.6b) "quoted in Assumption A1(d)" (l. 954) | `main.tex` ll. 686–689; Simon p. 138 (PDF 160) | holds |
| S15 | Simon Theorem I.22 at p = 4, m = 2p', "as quoted in Assumption A4" (Lemma T.13 `lem:Vbar`, p. 11, ll. 784–785) | `main.tex` ll. 948–951; Simon p. 38 (PDF 60) | holds |
| S16 | Simon: *The P(Φ)₂ Euclidean (Quantum) Field Theory*, Princeton University Press, 1974 (ll. 113–116) | title page (PDF 5) | holds |
| A1 | Every application of Theorem 1.1.7 in the Route T chain is one of P1–P4 (Theorem T.2(c) `thm:routeT`, p. 4, ll. 216–221; §4(c), p. 16, ll. 1066–1068) | uses of `sf:CE2` in proofs: l. 2203 (Lemma 7.4), ll. 6289–6425 (Lemma D.2), l. 6773 (D.3), l. 7095 (D.4); none in §§8–12; Proposition C.7 (`prop:discharge`, C.7, p. 57) | holds |
| A2 | The table of §5.2 (`sec:cases`, p. 17, ll. 1116–1134): types, r, orientation and cutoffs of P1–P4 and of D.4 class (T) | Lemma 7.4 (`lem:ce2strip`, 7.4, p. 31, ll. 2175–2217); D.3 Step 3 (ll. 6768–6793); D.4 Steps 3–4 (ll. 7071–7119); T.14 Step 4 (ll. 841–861) | holds |
| A3 | P1–P4 lie within the printed statement of Theorem 1.1.7 (§5.5, p. 20, ll. 1267–1268; T.14 `thm:TD4`, p. 12, ll. 862–864) | pp. 593–594, hypothesis by hypothesis (table below) | holds |
| A4 | P3 and P4 are not A8(iv)-T "as the record defines it" (ll. 862–864) | A8 (iv-T), ll. 1156–1158; Lemma D.2(a), ll. 6291–6294 | holds |
| R1 | R1 and R2 are each a possible reading of p. 596 (§5.3 `sec:readings`, p. 18, ll. 1141–1150) | p. 596 | holds |
| R2 | The arguments for R1 and R2, and "The printed text does not decide between R1 and R2" (ll. 1151–1157) | pp. 597, 600, 628, 629 | gap, MINOR (F1) |
| R3 | "GJS's own use needs R1" (ll. 1159–1169) | pp. 594–597 | holds for products of r ≥ 2 fields; already recorded in `ugjs/PLAN.md` (F10) |
| R4 | "Reached" is defined (§5.4, p. 18, ll. 1173–1181) and used consistently | T.17, T.18, T.19, §5.5, Summary, §7 | the definition holds; consistency fails at T.17(c), R1 half: gap, MINOR (F3) |
| R5 | T.17(a) (`prop:reach`, p. 19): P1 is reached on R1 and on R2 | the pairs of Lemma 7.4 | holds (the rotation by π can be avoided, F6) |
| R6 | T.17(b): P2 and D.4 class (P) are reached after slicing, on R1 and R2 | T.19; N.43(ii) (`aux:d4-QV`, p. 99, l. 6955) | holds |
| R7 | T.17(c): P3 and P4 are reached on R1 | proof, ll. 1214–1236 | gap, MINOR (F3) |
| R8 | T.17(c): P3 and P4 are not reached on R2 | same | holds for the pieces with n, n′ ≥ 1; the pieces with a degree-0 factor are reached (F4) |
| R9 | T.17(d): D.4 class (T) is reached on neither reading; the quotation of §D.e.4 (ll. 1238–1243) | `sub:d4-transverse` (D.e.4, p. 101, ll. 7154–7156) | holds; the quotation is verbatim |
| R10 | Remark T.18 (`rem:obstruction`, p. 20) and the Summary's "no variant … can be reached on R2" (p. 1, ll. 86–87) | N.7(iv) (`aux:notation-strip`, p. 63), N.11(v), N.12(b) (`aux:notation-ringrem`, p. 66, ll. 4706–4716) | the substance holds for the comparison around boxes of fixed shape; "proved" and the Summary's wording are too general: gap, MINOR (F5) |
| R11 | "Two further questions … affect P1–P4 alike" (ll. 1182–1187) | Remark N.2(ii) (`aux:notation-gjslattice`, p. 59, l. 4289); Lemma N.13 (`aux:notation-transl`, p. 66) | the first question holds; the translation question does not arise for sharp-time pieces: MINOR (F6) |
| R12 | "Rotating" presupposes rotation covariance; the record proves translation covariance only (ll. 1187–1191) | grep `rotat` in `main.tex` (8 lines, none a covariance lemma); Lemma N.13 | holds; the presupposition is not carried into §5.5 and §7.2 for P4 (F3) |
| N1 | The quotation of Remark N.39 (§6, p. 21, ll. 1300–1303); N.39 "leaves open" whether the printed proof reaches the pair | `aux:d3-orient` (N.39, p. 96), ll. 6814–6819 | holds, verbatim |
| N2 | Finding N3 of 22 November is described correctly (Summary ll. 92–94; l. 1304) | council record of 22 November (cqft memo, finding N3; not in the repository) | holds |
| N3 | T.19(i)–(iii) (`prop:N39`, p. 21): the slicing and Fubini step is complete | A3 (ll. 857–860: e^{−ϱU_h} ∈ L¹ for every finite ϱ, Z(h) > 0); N.28(b) (ll. 5804–5808); N.36(ii),(v); N.38(i),(ii); N.17, N.18(i); D.2 Step 3 (ll. 6365–6368); D.3 Step 3 | holds, given Lemma T.12 (the other auditor's part) |
| N4 | T.19(iv): reached on R1 and R2; the same for D.4 class (P) | p. 596; N.43(ii) | holds |
| N5 | "The uniform gap … rests only on applications the printed proof reaches" (ll. 1374–1375) | §7 uses SF 2.2 only through Lemma 7.4 and D.3; Proposition C.7 | holds, subject to the questions common to every case |
| N6 | T.19 status "Proved" (l. 1332; table l. 1418) | AGENTS.md §2; status lines of T.14 and D.3 (ll. 6737–6745) | gap, MINOR (F12) |
| D1 | Theorem 5.1 enters the chain only at Lemma 10.2 (l. 2776), hence Lemmas 10.3–10.5 and l. 2921, and in the proof of Theorem 12.2 "for item (5)" (l. 3104) (§4(c), ll. 1058–1062) | grep of `thm:M2`, `eq:M2` and M in §§8–12: ll. 2765–2910, 2921, 3079, 3085, 3098, 3104–3105 | holds in substance; ll. 3104–3105 also route (M₂) into items (1)–(2) (F7) |
| D2 | Theorem D.4 enters only through Step 5 of Theorem 5.1 (ll. 1062–1063) | l. 1932; Corollary 5.2 (l. 1971) lies outside the chain; l. 3088 is the imports paragraph | holds |
| D3 | A8(iv)-T enters only through D.4; the quotation of A8 (iv-T) "Used in …" (ll. 1063–1065) | `main.tex` ll. 1166–1169 | holds; the quotation is correct, with the elision marked |
| D4 | A search of §7 (ll. 2055–2389) for `thm:M2`, `thm:D4`, `M_B` and "transverse" finds nothing (ll. 1065–1066) | my grep, extended to `eq:M2` and `iv-T` | holds |
| D5 | The table of §1.2 (p. 3), column "uses M?" | Lemmas 10.1–10.5, Theorem 11.1, Proposition 11.2 | holds |
| D6 | §7.2 (p. 23, ll. 1425–1430): items (1)–(4) and Corollary 12.3 are "proved, conditional on …"; under the strict standard, also on R1 | — | holds; F2 and F3 name what is missing |
| D7 | §7.2 (ll. 1432–1434): the gap clause of item (5) uses P1 and P2 only; the moment clause still rests on A8(iv)-T | proof of Theorem 7.8; Theorem 12.2(5), l. 3079 | holds |
| D8 | §7.3 (p. 24, ll. 1438–1455) lists completely what the note does not do | `main.tex` | gap, MINOR (F7; see also F2 and F3) |
| D9 | §13 consumes Theorem 12.2 and was "not checked" (ll. 1443–1445) | `main.tex` ll. 3200–3240 | I checked it: §13 uses item (1) only as local-norm convergence (l. 3225), and uses (3), (4) (ll. 3227, 3234), Lemma 9.3 (l. 3208) and Theorem 7.8; Route T does not affect it |
| D10 | Summary: "it trades A8(iv)-T, which no reading of the printed proof reaches, for reading R1" (p. 1, ll. 87–89) | Lemma T.15(ii) | gap, MINOR (F2) |
| D11 | §5.5: "The case Route T needs is (iii)" (p. 20, l. 1267) | — | gap, MINOR (F9) |
| D12 | The status words of §7.1 (p. 23) | AGENTS.md §2 | justified for T.2, T.14, T.15, T.16; T.17(c), T.18 and T.19: F3, F5, F12 |
| B1 | The note's build | `route_t.log`, `route_t.pdf` | 0 errors, 0 Overfull, 0 undefined, no flagged strings; 25 pages |

**The hypotheses of the printed Theorem 1.1.7, checked for each application.** Printed hypotheses:
- p. 593: a monomial "of the form (1.1.5)" or "(1.1.6)", "localized" (the kernel is supported in a
  product of unit lattice squares), with "n_i < n̄";
- p. 594: "two localized monomials Q₁ and Q₂, with disjoint localization squares", and d "the width of
  the widest strip bounded by two parallel lines, and separating" them, with no orientation prescribed;
- "m₀, K₂ and K₁ … sufficiently large", "λ … sufficiently small";
- constants "independent of h, Q₁ and Q₂".

| case | Q₁ | Q₂ | n_i < n̄ | disjoint | strip | cutoffs | within the printed statement |
|---|---|---|---|---|---|---|---|
| P1 | Q_a(−t/2): (1.1.5), factors of degree 1 at one time | Q_b(t/2), the same | 1 < n̄ | rows of ∓t/2 (t > 2) | {abs(x⁰) < t/2 − 1}, parallel, width t − 2 | every h ∈ C_E | yes |
| P2 | c_β Q_{β,κ}(s): (1.1.5), r_β factors of degree 1 at time s | U_{Δ,n}: (1.1.6), r = 1, kernel λa_n h1_Δ | 1, n ≤ 2p′ | abs(l − l_s) ≥ 2 | P_l, parallel, width abs(l − l_s) − 1 ≥ 1 | h_α, h = h_{T,g} (g fixed, all T) | yes |
| P3 | Q̄_{n,n′,k,k′}: (1.1.6), r = 2, kernel w_{n,k}⊗w_{n′,k′} ∈ L²(R⁴), squares Δ_{0,k}, Δ_{0,k′} | U_{Δ,n″}, Δ ∈ L_j, abs(l) = 1 + j | n, n′, n″ ≤ 2p′ | Δ ∉ B_{3×5} ⊇ S_a | parallel, width j | h_α, every h ∈ C_E | yes |
| P4 | as P3 | U_{Δ,n″}, Δ ∈ L_j, abs(l) ≤ j | same | same | lines of constant x¹, width j | h_α, every h ∈ C_E | yes |

Degree-0 factors occur in P3 and P4 exactly as in the record: Definition N.26 admits 0 ≤ n_i, and
N.43(ii) treats a factor of degree 0. All four cases read "independent of h" over C_E (A8 Scope (d)).
P3 and P4 need that uniformity over all h_{T,g} (T ≥ 1, g ∈ C_H), which is the same uniformity
Theorem D.4 needs today.

## 3. Findings

**F1 (MINOR; material to the author's decision). The evidence for and against R1 is incomplete.**
- *Locator.* §5.3 (`sec:readings`, p. 18), ll. 1151–1157; Summary (p. 1), ll. 83–85.
- *Text.* "In favour of R2: in both theorems the approximants have one Wick factor ($r=1$), so for them
  equal times are automatic, and the sentence would be redundant if it concerned only them. The printed
  text does not decide between R1 and R2."
- *Why it falls short.* The note does not consider three printed passages.
  - (a) p. 600 (PDF 17, `gjs-proof118-17`): "Proof of Theorem 1.1.8, assuming Theorem 1.1.10. Choose
    T = 0 and B = I in Theorem 1.1.11. Then Q = 0, so Theorem 1.1.8 is a special case of Theorem 1.1.10."
    (Both occurrences of "1.1.10" are misprints for 1.1.11; the record marks them [sic], `main.tex`
    ll. 1236–1238.) p. 629
    (PDF 46): "Theorem 1.1.11 follows from this inequality, while Theorem 1.1.8 is the special case
    B = I, n = 0." So GJS derive Theorem 1.1.8 as the case A = Q(x₀), B = I of Theorem 1.1.11.
  - Theorem 1.1.8, however, is printed "For Q(x₀) of the form (1.1.5)", directly after p. 595
    introduced the ordered times x_{1,0} ≤ ··· ≤ x_{r,0}. Corollary 1.1.9 then applies "the theorem" to
    Q₁ = Q(x_{i0} − x_{10})Q(x_{10} − x_{i0})⁻, whose factors are at different times. On R2 the
    derivation of pp. 600 and 629 reaches Theorem 1.1.8 only for equal-time Q(x₀), short of the scope at
    which it is printed and used. On R1 it reaches that scope.
  - (b) p. 628 (PDF 45, `gjs-thm41-45`; rendered at 300 dpi), in the "Proof of Theorems 1.1.8 and
    1.1.11": "set Q_n(y₀) = Σ_{i=0}^n ∫d y⃗ w_i(y) ∫ :Φ(y₁)···Φ(y_i): . (By removal of the Wick
    ordering in Q_n(y₀), we may apply the norms of (1.1.8).)" (4.3) groups "terms with common values of i
    and y₀". So the approximants of Theorem 1.1.11 are built with up to n field factors at one time y₀,
    not one Wick factor. The equal-times sentence therefore has content for them, and the argument the
    note offers for R2 loses its premise.
  - (c) Weaker: p. 597, in the proof of Theorem 1.1.5, writes "θ_A is the vector (1.1.13) corresponding
    to A". (1.1.13) is the vector that p. 595 builds for ordered, possibly distinct times.
  - No printed sentence says in words that A may have factors at different times, so "does not decide"
    remains defensible in that narrow sense. But R1 is the reading under which GJS's own proofs are
    complete at p. 595 and at pp. 600 and 629. The record already reads (1.1.5) this way for its own
    objects (Definition N.26(b), l. 5750, "equal or not"; Remark N.27, l. 5783).
- *Repair.* Add (a)–(c) to "In favour of R1". Qualify the R2 argument: it rests on the statement's
  "r = 1", which the construction on p. 628 does not bear out. Keep "no sentence decides".
- *Severity.* MINOR. No result of the note changes, but the weight of the condition R1 does.

**F2 (MINOR; material). The new import is missing from the Summary and is called an "instance of A2".**
- *Locator.* Summary (p. 1), ll. 79–90; Lemma T.15(ii) (`lem:fkn`, p. 14), ll. 947–948; §7.2 (p. 23),
  ll. 1427–1428; §7.1 table, l. 1389.
- *Text.* "So Route T does not make items (1)–(4) rest only on cases the printed proof reaches: it
  trades A8(iv)-T, which no reading of the printed proof reaches, for reading R1." Also:
  "Assumption~A2 (\texttt{A:fkn}) imports this theorem", and "Simon's (V.47) with its Remark as the
  instance of A2 in Lemma~T.15".
- *Why it fails.*
  - A2 (A2, p. 13, ll. 829–835) is stated "For all bounded time-zero functions f, h′ …", "together with
    the analogous multi-time formulas on finite slabs". The record extends it to unbounded functions by
    truncation (Lemma 4.3), and only in the symmetric two-time and one-time forms.
  - Theorem V.15 (Simon p. 163) is printed for polynomially bounded functions of finitely many fields.
    Lemma T.15(ii) applies (V.47) with G₁ = G₂ = V(h) at asymmetric times, which needs the Remark on
    p. 164: "More generally, the above holds if G_j^F ∈ ∩_{p<∞} L^p(Q_F) and G_j^{s_j} = J_{s_j}G_j".
    That Remark is a printed sentence without proof, as the note itself says in §7.4, item 2.
  - So this is an import beyond A2 as the record states it, and a new dependency of items (1)–(4). The
    status lines list it, correctly as a condition. The Summary's account of the trade omits it.
- *Repair.* Summary: "it trades A8(iv)-T for reading R1 and for Simon's Remark on p. 164 (removable by
  a truncation extension of A2 in the manner of Lemma 4.3, not yet written)". Replace "the instance of
  A2" by "an extension of A2 (A2 is stated for bounded functions)". In §7.3, list "the truncation
  replacing the Remark is not written".
- *Severity.* MINOR.

**F3 (MINOR). Proposition T.17(c), R1 half: the integration is not written out, and P4's extra
presupposition is not carried forward.**
- *Locator.* Definition of "reached", p. 18, ll. 1173–1181; T.17(c) and its proof (p. 19–20), ll. 1198
  and 1214–1236; §5.5 item 3 (l. 1293); §7.2 (ll. 1429–1430).
- *Text.* (b) of the definition: "… follows from the bounds for the pairs of slices by an integration
  that is written out (as in Proposition~\ref{prop:N39})". The proof: "On R1 the two-time slice is
  admissible as $A$ … so the pair is reached." For class (T): "Slicing in the new time, as in
  Lemma~\ref{lem:slice} with the roles of the two coordinates exchanged, … the conclusion is the same as
  for class (P)."
- *Why it fails.*
  - For P3 and P4 on R1 the integration over (τ, τ′, t) is not written out. What is missing is the
    analogue of T.19(i)/(iii), with the double Bochner integral and the bounded covariance functional,
    which the note's own definition requires.
  - For P4 the slices are sharp in x¹. The record does not define such objects (Definition N.26(b) is
    sharp in time), and their construction needs the rotation covariance that the note says the record
    does not prove (ll. 1189–1191; my grep finds no rotation lemma).
  - Among P1–P4, only P4 needs the rotation. §5.5 item 3 and §7.2 list the remaining questions about the
    source "which affect every case alike" and omit this one.
  - The R2 half of (c) is unaffected.
- *Repair.* Write the integration for P3; it takes two lines, as in T.19. For P4, either write the
  x¹-sliced analogue of Lemma T.12 (for instance through N.28(e) with a rotated mollifier and the
  rotation invariance of the covariance) or state (c)-R1 for P4 as conditional on the rotation
  presupposition. Add that presupposition, for P4, to §5.5 item 3 and §7.2. Change the status of T.17
  to "proved for (a), (b), (d) and the R2 half of (c); the R1 half of (c) is sketched".
- *Severity.* MINOR. T.17 is a statement about scope, and the chain of T.2 does not use it.

**F4 (MINOR). Degree-0 pieces are reached on R2.**
- *Locator.* T.17(c), l. 1198, and its proof, ll. 1228–1230; Remark T.18, ll. 1249–1251; Summary,
  ll. 85–86.
- *Text.* "On R2 they are not reached."; "On R2 the slices with $\tau\ne\tau'$ are admissible neither as
  $A$ nor as $B$"; "On the other reading (R2) none of these new applications is reached, the parallel
  ones included"; "A time-integrated monomial with $r\ge2$ factors and a nonzero kernel in
  $L^2(\R^{2r})$ never has this property".
- *Why it fails.*
  - Lemma T.13 admits 0 ≤ n, n′ ≤ 2p′, and a factor of degree 0 is the constant 1 (N.43(ii), ll.
    6992–6993). So Q̄_{0,n′,k,k′} = (λa₀∫h′_k)·V̄_{n′,k′} is a time-integrated monomial with r = 1, and its
    pairs with U are reached on R2 after slicing, exactly as in T.19.
  - The statements hold for the pieces with n, n′ ≥ 1. These exist, since a_{2p′} ≠ 0, so the
    conclusion that P3–P4 are not reached on R2 stands.
- *Repair.* Write "the pieces with n, n′ ≥ 1 are not reached on R2", and in T.18 "r ≥ 2 factors of
  positive degree".
- *Severity.* MINOR.

**F5 (MINOR). Remark T.18 is stated more generally than it is proved.**
- *Locator.* Remark T.18 (p. 20), ll. 1253–1260; Summary, ll. 86–87; §7.1 table, ll. 1416–1417.
- *Text.* "Any route that bounds $\Mt(\lambda_0)$ or $M$ through a quadratic Euclidean observable … and
  the comparison of Lemma~D.2 around a box of fixed shape, such as $B_{3\times5}$, must apply
  Theorem~1.1.7 across transverse strips …". The Summary: "no variant that bounds a quadratic observable
  by the comparison method of Lemma~D.2 can be reached on R2". The table: "Remark T.18 & proved".
- *Why it fails.*
  - The substance is right. For charged squares in the rows of the observable outside the box, N.7(iv)
    forbids parallel strips of positive width for every rectangle.
  - But the class of "routes" is not defined, and the cited N.11(v) and N.12(b) concern B_{3×5} only.
  - The Summary also drops "around a box of fixed shape". A box that grows with supp h escapes the
    argument, though it gives up uniformity in h.
- *Repair.* Present T.18 as an argued observation about the comparison of Lemma D.2 around boxes of
  fixed shape, not as a proved statement, and restore the qualifier in the Summary.
- *Severity.* MINOR.

**F6 (MINOR). The translation question and the rotation by π do not arise for the pieces the note uses.**
- *Locator.* §5.4, ll. 1182–1187; T.17(a) proof, l. 1209; T.19(iv), l. 1359.
- *Text.* "Two further questions about the source's proof affect P1--P4 alike …: … and the translation
  onto $\{0<x^0<d\}$ moves the squares of p.~593 by a half-integer when $S$ is bounded by lattice lines."
  Also "(and a rotation by $\pi$ if the order is reversed)" and "a rotation by $\pi$ if $l<l_s$".
- *Why it overstates.*
  - In every application as the note handles it, both partners are sharp-time pieces: P1 and P2
    directly, P3 and P4 after slicing.
  - A time translation by any real amount keeps a sharp-time piece localized in the squares of the row
    of its new time and changes neither its local degrees nor its kernel norm. The record says so in
    Remark N.2(ii), l. 4289: "The choice of row changes neither the local degrees nor
    $\|w(x_0,\cdot)\|_2$, hence not the norm (1.1.8)". Lemma N.13 gives translation covariance for every
    a ∈ R².
  - (1.1.10) is symmetric in Q₁ and Q₂, so relabelling the pair replaces the rotation by π. Then P1–P3
    need no rotation at all.
- *Repair.* Say that the translation question is settled for sharp-time pieces by Remark N.2(ii) and
  Lemma N.13. Replace "a rotation by π" by "relabelling Q₁ ↔ Q₂".
- *Severity.* MINOR (over-cautious; the correction strengthens the parallel cases).

**F7 (MINOR). The account of where Theorem 5.1 enters, and the integration list, are incomplete.**
- *Locator.* §4(c) (p. 16), ll. 1058–1062; §7.3, last item, ll. 1450–1454.
- *Text.* "… and in the proof of Theorem~12.2 for item (5) (l.~3104)". "Integration would need: the
  imports paragraph of Theorem~12.2 and the ``Used in'' sentence of A8, item (iv-T) …; Lemma~10.2 split …;
  Lemmas~10.3--10.5 and Proposition~10.4 replaced, and $\Psi_{m_1}$ redefined in \S11; the new statements
  T.3--T.16; and the wording of Remark~N.39 above."
- *Why it fails.*
  - ll. 3104–3106 of the record read: "(5) is Theorem 7.8 and Theorem 5.1. These supply (G_γ) with
    γ = m₁ and (M₂), so Theorem 11.1 and Proposition 11.2 give (1)–(2)". This routes (M₂) into items
    (1)–(2), not only into (5).
  - Other record sites state the present dependency or the present rate and would also change:
    - ll. 120–124 (the "Integration of Appendix D" paragraph);
    - the strategy table, l. 251 ("incl. A8(iv)-T") and l. 257 ("(iv) LPPL/Cauchy: (G)+(M₂) ⇒ full-net
      convergence + rate");
    - the dependency graph, l. 280; Pillar 1, ll. 356–368;
    - A8 Scope (b), ll. 1373–1377 ("Theorem D.4, hence Theorem 5.1 and all that consumes M");
    - the imports paragraph of Theorem 12.2 up to l. 3099 (the rate Ψ_{m₁});
    - Proposition C.7 (`prop:discharge`, p. 57, ll. 4086–4101), the inventory of every CE2 application,
      which must add P3–P4;
    - the notation row d₀ (l. 619) and the Constants rows d₀, shell count, Ψ_γ and its tail
      (ll. 3369–3372);
    - the Discussion, l. 3291 ("super-polynomial but sub-exponential").
- *Repair.* Extend both lists.
- *Severity.* MINOR.

**F8 (MINOR). Two readings are presented as printed.**
- *Locator.* §5.1, ll. 1102–1104; §5.3, ll. 1166–1168.
- *Text.* "Corollary~1.1.9 on the same page applies Theorem~1.1.8 to ``…''"; "in the proof of their
  Theorem~1.1.1 (convergence of the Schwinger functions)".
- *Why it fails.*
  - p. 596 prints "Apply the theorem to". The identification with Theorem 1.1.8 is natural, since the
    displayed bound has its form, but it is a reading, and it sits in the list "What GJS print".
  - p. 590 (PDF 7) prints Theorem 1.1.1 as "The 𝒫(φ)₂ quantum field model exists as a limit of space
    cutoff theories and satisfies the Wightman axioms …". The application on p. 595 serves the step "the
    cutoff Schwinger functions S_h converge as h → 1".
- *Repair.* Write "applies 'the theorem' (Theorem 1.1.8, by the form of the bound)" and "(at the step
  where the cutoff Schwinger functions converge, p. 595)".
- *Severity.* MINOR.

**F9 (MINOR). An undefined label.**
- *Locator.* §5.5 (p. 20), l. 1267.
- *Text.* "\emph{The case Route T needs is (iii), dependent on a reading.}"
- *Why it fails.* No item "(iii)" is defined in the note; it seems to refer to the commission's
  categories.
- *Repair.* Spell out the category.
- *Severity.* MINOR.

**F10 (MINOR, provenance). R1 and the p. 595 observation are already in the record and the plan.**
- *Locator.* §5.3 (p. 18), ll. 1141–1169.
- *Why it fails.*
  - R1 is the "multi-time reading of (1.1.5)" that Remark N.39 names (l. 6816), applied to A in
    Theorem 1.1.11. The record's objects already carry it (Definition N.26(b), l. 5750; Remark N.27,
    l. 5783: "Case (b) admits distinct times $x_{i,0}$, the reading of p.~595").
  - `ugjs/PLAN.md`, Part 2, ll. 312–315 (at 49f2d23), already records: "Monomials of type (1.1.6) are
    reached in any orientation, after slicing, under the multi-time reading of (1.1.5). … This is how
    GJS's own use on p. 595 is covered."
  - The note presents R1 and the observation on p. 595 without these links.
- *Repair.* Add one sentence identifying R1 with that reading and citing N.26(b), N.27, N.39 and the
  plan.
- *Severity.* MINOR.

**F11 (MINOR). A path, and undated sentences.**
- *Locator.* §6 (p. 22), l. 1371; §1.1 (p. 2), ll. 116–117; §7.1 (p. 23), l. 1410.
- *Text.* "(\path{ugjs/route_t.tex}, Proposition~T.19)"; "was read on the rendered page in this
  session"; "read on the page images in this session".
- *Why it fails.* The note will live at `ugjs/route_t/route_t.tex`, and "this session" carries no date
  in an archived document.
- *Repair.* Correct the path, and write "on 23 November 2026".
- *Severity.* MINOR.

**F12 (MINOR). The status of T.19 omits the reading.**
- *Locator.* T.19 status, l. 1332; §7.1 table, l. 1418.
- *Text.* "Proved; (iv) as a statement about the source's printed proof."
- *Why it fails.* T.19(iii) applies Source Fact 2.2 to the constructed objects Q₁ and U_{Δ,n}(t), and
  (i) uses A3. This is the reading of A8 Scope (d) / Remark N.2(iv) that the status of T.14 names
  (ll. 870–873) and that the status of Theorem D.3 names (ll. 6740–6743). By AGENTS.md §2 the status is
  "proved, conditional on A8(iv) (printed scope, single-time parallel pairs), A3 and the reading of A8
  Scope (d)".
- *Repair.* Align the status with that of T.14.
- *Severity.* MINOR.

## 4. Checks run

**The GJS copy in `refs/`.**
- `pdfinfo`: 49 pages.
- `pdftotext` of PDF 1: "Source: Annals of Mathematics, Vol. 100, No. 3 (Nov., 1974), pp. 585-632";
  authors James Glimm, Arthur Jaffe and Thomas Spencer.
- Rendered at 150 dpi: PDF 2, 7, 10–14, 17, 44–46 (pp. 585, 590, 593–597, 600, 627–629). PDF 45 also
  rendered at 300 dpi.
- PDF 2 shows the contents line "1. The particle structure …585" and the start of §1. The header of
  PDF 10 reads "593". Offset: printed = PDF + 583.

**The evidence images.** I stacked the page headers of the downscaled images: `gjs-theorems-10`,
`-11`, `-12`, `gjs-thm1111-13` and `gjs-proof-14` show 593, 594, 595, 596 and 597; `simon-fkn-185`
shows 163.

**Simon's book.** Rendered PDF 5 (title page: "The P(Φ)₂ Euclidean (Quantum) Field Theory", Barry
Simon, Princeton University Press, 1974), PDF 60 (p. 38, Theorem I.22, (I.47)), PDF 160 (p. 138,
(V.6b)), PDF 185 (p. 163, Corollary V.14 and Theorem V.15, (V.47)) and PDF 186 (p. 164, the
continuation and the Remark). Offset 22 confirmed.

**Quotations.** I compared each quotation in §5.1, §5.3, §5.4 and T.15(ii) with the rendered page.
All match, apart from the points in F8 and the lowered initial capital of S9.

**The record.**
- `grep newlabel main.aux`: every record number the note cites resolves to the label and page the note
  gives (2.6, 2.7, 2.8, 3.1, 4.1, 4.3, 4.4, 5.1, 7.4, 7.8, 8.1, 8.2, 9.1–9.3, 10.1–10.5, 11.1, 11.2,
  12.1–12.3, C.2, D.1–D.4, D.c.1, D.e.4, E.5, N.1, N.2, N.5, N.7, N.10–N.13, N.15, N.17, N.18, N.20–N.28,
  N.32, N.36, N.38, N.39, N.43).
- §7 (ll. 2055–2389) grepped for `thm:M2|thm:D4|M_B|transverse|eq:M2|iv)-T|iv-T`. The output contains
  only `thm:D3`, `sf:CE2` and `lem:ce2strip` (ll. 2066, 2077, 2107, 2151, 2175, 2203, 2245, 2294).
- `thm:M2` is referenced in §§7–12 only at ll. 2776, 2921, 3061 (a comment), 3085 and 3104. `eq:M2`
  occurs at ll. 359, 400, 1852 and 3105. The symbol M occurs in §§8–12 at ll. 2765, 2776, 2800, 2822,
  2843, 2846, 2863, 2881, 2910, 2921, 3079 and 3098.
- `sf:CE2` is used in proofs at l. 2203 (Lemma 7.4), ll. 6289–6425 (Lemma D.2), l. 6773 (D.3) and
  l. 7095 (D.4). Proposition C.7 confirms that inventory.
- `rotat` gives 8 lines (ll. 1153, 1330, 1370, 3533, 4155, 7152, 7154, 7156); none is a covariance
  lemma.

**Passages read.** In the record: A2, A3, A4, A1(d), A8 (all of it), Lemmas 7.1–7.4 and Theorem 7.8,
Lemmas 9.3 and 10.1–10.2, §§11–13 (ll. 2917–3240), Theorem 5.1, Corollary 5.2, Lemma D.2, Theorem D.3
with N.36, N.38 and N.39, Theorem D.4 with N.43 and D.e.4, N.6, N.7, N.10–N.13, N.26–N.28, Proposition
C.7, and the Constants table. Also C5 items 10–12 and `ugjs/PLAN.md` ll. 296–330.

**The 22 November council record.** The cqft memo: finding N3 (its ll. 78–83) and sketch steps (a)–(d)
(ll. 45–52). The note's descriptions of both match.

**The note's build.** From the existing log, without rebuilding: `grep -cE '^!'` gives 0,
`grep -c Overfull` gives 0, `grep -icE undefined` gives 0, and `pdftotext … | grep -nE '\?\?|TODO|Hmm|wait,'`
gives nothing. `pdfinfo`: 25 pages.

**Comparison with the earlier reports**, done after my verdicts were written down (scratch file
`verdicts-before-comparison.md`).
- I grepped `ugjs/council/` (at 49f2d23) for "multi-time", "equal times", "all times", "p. 600" and
  "628". The V2 report lists as "not checked" "whether the multi-time reading of (1.1.5) lets the printed
  proof reach D.3's time-integrated partner". T.19 settles that question, and I agree with T.19.
- No earlier report uses pp. 600 and 628–629 for the reading of p. 596, so F1 is new.
- I found no disagreement with the earlier reports.

## 5. Not done, not verified, not run

**Not done.**
- The analysis of Lemmas T.3–T.13, T.15(i),(iii) and T.16 (the other auditor's part). T.19 relies on
  Lemma T.12, which I did not verify.
- The x¹-sliced analogue that P4 needs (F3).
- GJS pages other than 585, 590, 593–597, 600 and 627–629.
- Any proof of GJS.
- The KB node `import/a8-iv-t`, and the public docs and companion texts that state the dependency.
- The drafter's report.

**Not verified.**
- The Summary's "its constants are confirmed or slightly improved" (sketch of 22 November). I checked
  only that the note quotes the sketch correctly.
- That Ψ̃_{m₁} is sub-exponential (relevant to l. 3291 of the record).

**Not run.**
- `check_route_t.py`.
- Any LaTeX build. I read the existing log.

## 6. Files written

- This report: `route-t-audit-sources.md` in the council's reports directory.
- Scratch files in the council's work directory `route-t-audit-sources/`: page renders and
  `verdicts-before-comparison.md`.
- Nothing under the repository and nothing in the note's directory.

## 7. Answer to the author's question

**Now (49f2d23).** Items (1)–(4) and Corollary 12.3 are proved, conditional on:
- A1–A8, with A8(iv) used at its printed scope in Lemma 7.4 and in Theorems D.3 and D.4, including the
  transverse case A8(iv)-T, which reaches the items through Theorem D.4 → Theorem 5.1 → Lemma 10.2 and
  the rate Ψ_{m₁};
- the declared readings (the Scope paragraphs of A1, A3 and A6; A8 Scope (d); the open C5 items).

Under the stricter standard "only cases the printed proof reaches" the condition fails on every reading
of p. 596, because no reading reaches A8(iv)-T.

**After Route T** (if integrated, and if the analysis audit confirms T.3–T.16). Items (1)–(4) and
Corollary 12.3, with the new rate Ψ̃_{m₁}, are proved, conditional on:
- A1–A8, with A8(iv) used only in P1–P4. Neither A8(iv)-T nor Theorem 5.1 nor Theorem D.4 is used.
- The same declared readings. The time-integrated two-factor objects are already covered by
  Definition N.26(a).
- One new printed input: Simon's Remark on p. 164, which extends (V.47) to G_j ∈ ∩_{p<∞}L^p. It goes
  beyond A2 as the record states it, and a truncation lemma in the manner of Lemma 4.3, not yet written,
  would remove it.

Ψ̃_{m₁} still decays faster than every inverse power, and its constant still contains M_B and the
unevaluated S₂(B_{3×5}).

Under the stricter standard, items (1)–(4) are then covered if and only if one accepts reading R1 of
p. 596 (A in Theorem 1.1.11 may have factors at different times). Two further conditions come with it:
the question common to every case (the constant taken from Theorem 1.1.8 at the same h), and, for P4
alone, the rotation covariance that "rotating" presupposes. The uniform gap and the gap clause of item
(5) rest on P1 and P2, which the printed proof reaches on either reading; Proposition T.19 settles the
question that Remark N.39 left open.

R1 is not an arbitrary choice. It is the reading under which GJS's own proofs are complete: at p. 595,
and in the derivation of Theorem 1.1.8 at its printed multi-time scope as the case B = I of Theorem
1.1.11 (pp. 600 and 629), which Corollary 1.1.9 applies to a product at different times. The record
already reads (1.1.5) this way for its objects. No printed sentence states it, however. The moment
clause of item (5), Theorem 5.1 and Corollary 5.2 still rest on A8(iv)-T.

**In one line:** Route T replaces a case that no reading of the printed proof reaches by cases reached
on the reading that GJS's own proofs need. The price is one additional printed but unproved input
(Simon's Remark) and a new rate function.

## Re-check of the revision (23/24 November 2026)

Same auditor, same brief and rules. The record is `part_i/main.tex` at 49f2d23.

**Object.** The revised `ugjs/route_t/route_t.tex`: 1812 lines and 30 pages; statements T.1–T.19
keep their numbers. I also read the drafter's account (`route-t-revision.md`) and the diff against
the draft audited above (`route-t-revision.diff`, 954 lines). In this section, note locators are
lines of the revised file and pages of its PDF. The new findings continue the numbering as
F13–F18.

### 1. Outcome

- All of F1–F12 are closed except F6, which is partly closed.
- The new source claim holds: Route T adds no input beyond the record's imports. The bounded
  two-time formula at asymmetric times is an instance of A2 as stated and as printed in its
  source, and the record already uses A2 in the same way.
- Every GJS quotation and every record reference I checked is exact.
- I found six new points (F13–F18): five MINOR and one cosmetic. None is CRITICAL or MAJOR.

### 2. Verdict per finding

| finding | verdict | where now (revised note) | remark |
|---|---|---|---|
| F1 evidence for R1 | closed | §5.1 ll. 1150–1197 (pp. 18–19); §5.3 ll. 1241–1265 (p. 20) | points (a)–(d) added; the R2 argument is withdrawn, with p. 628 as the reason; "no printed sentence states R1" is kept in the narrow sense; every quotation checked (§4 below) |
| F2 new import; "instance of A2" | closed, by removing the Remark | T.15(ii) ll. 972–1027 (pp. 15–16); Summary ll. 90–93 (p. 1); T.2 status ll. 262–269; §7.1 ll. 1653–1657, 1675–1677; §7.2 ll. 1698–1699 | a grep finds neither phrase left; the source claim holds (§3); residue F13 |
| F3 T.17(c) on R1 | closed | P3: ll. 1365–1429 (pp. 22–23); P4: ll. 1431–1441 (p. 23); presupposition defined ll. 1324–1336 (pp. 21–22) | the P3 integration holds step by step (§5); P4 is now conditional, and the presupposition is carried into the T.2 status, the Summary, the T.17 statement and status, §5.5 and §§7.1–7.3; residue F14 |
| F4 degree-0 pieces | closed | T.17(c) ll. 1345–1347; proof ll. 1452–1456; T.18 ll. 1471, 1478; Summary ll. 103–104; §5.5 ll. 1514, 1527 | cosmetic residue F18 |
| F5 generality of T.18 | closed | T.18 ll. 1467–1501 (p. 24); §7.1 ll. 1682–1685; Summary ll. 104–106 | N.7(iv) holds for any rectangle of squares; the remark that D.3's box grows with g matches the record (ll. 6819–6822) |
| F6 translations; rotation by π | partly closed | "Translations" and "Rotations" items ll. 1310–1336 (pp. 21–22); relabelling at ll. 1295–1296, 1359, 1417–1418, 1624 | relabelling: closed; N.13 and N.2(ii) give what is cited (§4), but the item misses one case of P4 (F15) |
| F7 entry of Theorem 5.1; integration list | closed | §4(c) ll. 1123–1135 (p. 18); §7.3 ll. 1729–1753 (p. 29) | the quotation of ll. 3104–3106 is verbatim; every listed line checked (§4); residue F13 (A2) |
| F8 readings presented as printed | closed | ll. 1150–1152, 1167–1168, 1180–1183, 1282–1283 | |
| F9 "(iii)" | closed | §5.5 ll. 1505–1516 (p. 25) | "the commission" is still unidentified (F18) |
| F10 provenance | closed | §5.3 ll. 1267–1273 (p. 21) | all four quotations verbatim |
| F11 path; undated sentences | closed | l. 1637 (p. 27); ll. 137–138 | a grep finds no "this session" and no `ugjs/route_t.tex` left |
| F12 status of T.19 | closed | ll. 1591–1595 (p. 26); §7.1 ll. 1686–1688 | |

### 3. Item 2: does A2 cover the bounded two-time formula at asymmetric times?

**Yes, within A2 as stated and sourced.** It is not a new reading, and the note names the instance
adequately. The reasons follow.

**What A2 states.** A2 (`A:fkn`, A2, p. 13) is stated "For all bounded time-zero functions"
(ll. 828–829). Its display is the two-time formula "with the interaction over exactly the slab [0,T]
carrying the two embeddings" (l. 834). It adds "together with the analogous multi-time formulas on
finite slabs" (l. 835), without restricting where the times sit. The parenthetical (ll. 835–838,
"used in §4 in the two- and one-time forms, where the symmetric slab cutoffs h_{T,g} … enter")
describes uses, and "symmetric" refers to the slab, not to the times.

**Its printed source.** The Sources line (ll. 840–841) names Simon's Cor. V.14 and Thm V.15.
Theorem V.15 (p. 163, `simon-fkn-185`) is printed for "t_1, …, t_n > 0" with (V.47), and p. 164
(PDF 186) continues "where s_0 is arbitrary and s_j = s_{j−1} + t_j". The note's (t7) is (V.47)
with n = 3, G_0 = G_3 = 1, s_0 = −T, s_3 = T and t_1 = T+τ, t_2 = τ′−τ, t_3 = T−τ′, all positive.

**Conventions.** Simon puts the earliest time leftmost. A2 puts the later time on the left, and so
does the note's (t7), which says so at ll. 980–981. For real bounded functions the two give the same
identity, by the time reflection that preserves dμ_0 and the symmetric slab. I checked this by
writing (V.47) with G_1 = F_2 at −τ′ and G_2 = F_1 at −τ.

**The record's precedent.** The record already uses A2's multi-time formula in Lemma 4.1
(`lem:slabFKN`, 4.1, p. 25), for general bounded measurable functions:
- at two symmetric interior times, in formula (2) (`eq:fkn2`);
- at one interior time anywhere in [−T,T], in formula (3) (`eq:fkn1`).

The asymmetric two-time case combines the two. Theorem V.15 is printed only for polynomially bounded
functions of finitely many fields, whereas A2 states "all bounded time-zero functions"; that gap
belongs to A2's own import, Lemma 4.1 already relies on it, and Route T changes nothing there.

**The step to the unbounded V(h).** The extension follows Lemma 4.3(ii) (`lem:slabunbdd`, 4.3,
p. 26, ll. 1765–1776), whose clipped truncation and dominators are as the note says. The other
inputs are as cited:
- A5(i) (ll. 975–981) gives ψ_b ∈ D(V(h));
- Lemma N.32 (`aux:d2-int`, p. 88, ll. 6244–6249) states "Every X ∈ L⁴(dμ₀) lies in L²(dq_h)";
- Lemma 3.1(ii) (`lem:classes`, p. 23, ll. 1521–1523) gives h_{T,g} ∈ C_E.

The analysis of the two dominated convergences is the other auditor's part.

**Conclusion.** "Route T adds no input to the record's imports" (Summary ll. 90–93; §5.5
ll. 1531–1532) holds. The note's wording, "A2 used at two times placed asymmetrically in a slab, as
formula (3) of the record's Lemma 4.1 uses it at one", is adequate; citing formula (2) as well would
complete the precedent. Only the integration list misses A2 (F13).

### 4. Spot-checks of the quotations and references

**All GJS quotations of the revised note**, against the rendered pages (150 dpi, with 300–400 dpi
crops where the formula is small):
- **p. 590** (PDF 7), Theorem 1.1.1: verbatim; "(the statement continues)" is correct.
- **pp. 593 and 594:** unchanged, verbatim.
- **p. 595:** "As a special case, the cutoff Schwinger functions S_h converge as h → 1." is
  verbatim; the other quotations from this page are unchanged.
- **p. 596:** "Apply the theorem to Q_1 = Q(x_{i0} − x_{10})Q(x_{10} − x_{i0})⁻, where Q has the form
  (1.1.5)" is verbatim. The bound "∫Q_1dq ≤ O(1)‖Q_1‖_{K_2}" is a verbatim piece of the printed chain
  "‖Q(x_0)‖² = ∫Q_1dq ≤ O(1)‖Q_1‖_{K_2} ≤ O(1)‖Q(x_0)‖²_{2K_2}" (300 dpi crop).
- **p. 597:** "where θ_A is the vector (1.1.13) corresponding to A" is verbatim; it is printed in the
  proof of Theorem 1.1.5.
- **p. 600** (PDF 17): verbatim, with both "1.1.10" as printed; the record's [sic] marks are at
  A8(vi), ll. 1236–1238.
- **p. 628** (PDF 45): "terms with common values of i and y_0", the display
  Q_n(y_0) = Σ_{i=0}^n ∫d y⃗ w_i(y) ∫ :Φ(y_1)···Φ(y_i):, and the parenthetical are verbatim. The
  accent on y is a vector arrow (400 dpi crop), as the note writes.
- **p. 629:** both quotations verbatim, except that the uniformity sentence begins "The" in print
  (lowered at l. 1307, as in the draft).
- **Simon pp. 163–164** (T.15 Step 1, and ll. 1025–1026): verbatim.

**Record references.** I checked twenty-one; all are correct:
1. ll. 3104–3106, the quotation in §4(c);
2. A8(vi), ll. 1236–1238, the [sic] marks;
3. Remark N.39, l. 6816;
4. Definition N.26(b), l. 5750 ("equal or not");
5. Remark N.27, l. 5783;
6. `ugjs/PLAN.md`, ll. 312–315 (both quotations);
7. Lemma N.13 (i), (ii), (iv), as paraphrased at ll. 1315–1316;
8. Remark N.2(ii), l. 4289 (the quotation is verbatim; its context is the row assigned to a time on a
   lattice line, but (1.1.8) gives the same row-independence for any one-time piece);
9. Lemma N.19(v) (`aux:notation-kernel`, p. 69): G is "positive, radial";
10. Lemma N.28(e): independence of the mollifier for every even δ′ supported in the unit ball, which
    admits a radial one;
11. §13: ll. 3207–3221, 3225, 3227, 3234, and Remark 13.3 = `rem:gjs7576` ("scope of the
    phase-transition literature");
12. the imports paragraph of Theorem 12.2: l. 3085 and ll. 3097–3098;
13. the introduction: ll. 237–241, 251, 257, 280, 351, 356–368;
14. the notation rows: ll. 613, 618, 619;
15. Remark 3.3: ll. 1656–1657, 1660–1669, 1698–1701, and s = m₀/M_* (l. 1619);
16. Appendix A = `app:constants`: ll. 3369–3372 and 3378;
17. Proposition C.7: ll. 4087–4101;
18. the Discussion: l. 3291;
19. A2, ll. 825–838, and `eq:fkn1` = (3);
20. A8 (iv-T) "Used in", ll. 1166–1169, and A8 Scope (b), ll. 1369–1377;
21. Lemma N.32, Lemma 3.1(ii), A5(i) and Lemma 4.3(ii) (§3).

### 5. The written-out integration for P3 on R1 (T.17(c), ll. 1365–1429): checked

**Step 1.**
- The slices V̄_{n,k}(τ) = λa_nJ_τW_n(h′_k) lie in the n-th chaos, where the L² and L⁴ norms are
  equivalent. So the L²-Bochner representation of Lemma T.12 is also an L⁴-Bochner representation:
  the continuous linear inclusion carries the integral.
- The bounded bilinear product L⁴ × L⁴ → L² turns the two integrals into the double Bochner
  integral of the products. The products are strongly measurable on the product space, and their
  integral of norms is at most ‖β‖ ∫‖f‖ ∫‖g‖.
- N.28(c), type (b), identifies Q̄(τ,τ′) with the two-time monomial localized in Δ_{0,k} and
  Δ_{0,k′}; Definition N.26(b) admits distinct times.
- The norm (1.1.8) of Q̄(τ,τ′) is constant on [−1/2,1/2)², and its integral there equals ‖Q̄‖,
  because the time factor 1_{[−1/2,1/2)} has L² norm 1. The stated equality holds.

**Step 2.** The two bounded functionals give the iterated integral. They are bounded by A3
(Z > 0 and e^{−4U} ∈ L¹), with U and Q̄(τ,τ′) in L⁴.

**Step 3.**
- The class (P) strip, of width j, separates the squares.
- On R1 the two-time slice is admissible as A. For l < 0, after relabelling, it is admissible as B,
  which R1 also admits, and Theorem 1.1.8 is printed for general (1.1.5).
- A translation cannot raise the slice's norm: both factors start in row 0, so they can only be
  split into two squares.

**Step 4.** Integrating with T.12(ii) gives C₇e^{−m₁j}‖Q̄‖ ‖U‖, the bound of D.2(a).

**The argument is complete.** P4 on R1 is granted the rotation presupposition as defined at
ll. 1326–1329, under which both the measures and the constructed monomials transform. It then
reduces to Steps 1–4 in the rotated frame, where Lemma T.12 applies directly to the rotated kernels;
no x¹-sliced analogue is needed. "Proved, conditional on the rotation presupposition" is the right
status.

### 6. First page and Status section

**First page.**
- "Written … by an AI agent (Claude …)": correct.
- "Audited on the same day by two independent agents": correct.
- "None CRITICAL or MAJOR": correct for both reports; the analysis audit states "There are no
  CRITICAL and no MAJOR findings".
- "Nothing in it has yet been read by a human": I cannot verify it; it is consistent with the brief.
- "Under the author's supervision": see F16.
- "It is not integrated into the record: Theorem 12.2 of part_i/main.tex is unchanged": Route T is
  not integrated, and the statement of Theorem 12.2 is unchanged in the repository's working tree
  (23:21 on 23 November). That tree does reword one sentence of the theorem's imports paragraph
  ("contain the unevaluated constant S_2(B_{3×5}) of Definition … finite by Theorem …") and the title
  of Corollary 12.3 (F16).
- "The record of 23 November 2026 has the same statement numbers and different pages": correct for
  the working tree's `main.aux` at 23:21. It has the same 238 labels as 49f2d23, none renumbered and
  199 on different pages; for example `thm:MAIN` 12.2 moves from p. 41 to p. 42. The count moves
  while REPO is edited.
- The report paths `ugjs/council/route-t-audit-*.md` do not exist in REPO yet. The sentence becomes
  true once the orchestrator archives the reports there.

**Status words** (§7.1, p. 28, ll. 1652–1688):
- T.2, "proved, conditional on …": justified. Its table row, however, lists record statements "in
  §4(c) and in the status line of Theorem T.14", which misses those that T.15 now uses (F17).
- T.14, T.15, T.16 and T.19: justified.
- T.17: the statement is right, but the status line overstates one assertion on R2 (F14).
- T.18, "argued observation": justified.

**§7.2** (ll. 1695–1716) answers "what do items (1)–(4) rest on" accurately, and completely apart
from F15:
- it keeps the import standard and the strict standard apart;
- it names R1 and, for P4, the rotation presupposition;
- it states the constant question as common to every case;
- it treats the gap clause and the moment clause of item (5) separately;
- it adds §13, which I confirm (ll. 3200–3240).

The Summary (ll. 90–109) matches §7.2.

### 7. New findings (F13–F18)

**F13 (MINOR). The integration list misses A2.**
- *Locator.* §7.3, ll. 1729–1753 (p. 29).
- *Why.* In the record, A2's parenthetical (ll. 835–838: "used in §4 in the two- and one-time
  forms, where the symmetric slab cutoffs … enter") and its "Used in" line (l. 848) describe A2's
  uses. On integration, Lemma T.15(ii) adds an asymmetric two-time use, which neither mentions.
- *Repair.* Add both to the list.

**F14 (MINOR). The status of T.17 overstates one assertion on R2.**
- *Locator.* T.17 status, ll. 1353–1355 (p. 22); §7.1, ll. 1679–1681.
- *Text.* "Proved: (a), (b), (d); in (c), the assertions for P3 on R1 and the assertions on R2."
- *Why.* One of the assertions on R2 is conditional: "The pieces with a factor of degree 0 are
  reached after slicing, on either reading (for P4, granted the rotation presupposition)"
  (ll. 1346–1347).
- *Repair.* "the assertions on R2, except the reach of P4's degree-0 pieces, which is conditional on
  the rotation presupposition".

**F15 (MINOR). The "Translations" item misses a merging case in P4.**
- *Locator.* §5.4, "Translations", ll. 1310–1323 (p. 21); §5.5, item 3, ll. 1552–1554 (p. 25).
- *Text.* "Translations raise no question for the monomials the printed proof is applied to here";
  "For a two-time slice, the two factors may move into different rows of one column. That splits a
  local degree n+n′ into n and n′, which does not increase the norm (1.1.8)"; "The translation
  question … does not arise for the sharp-time pieces".
- *Why.*
  - In P1–P3 the claim holds. In P3 both factors of a slice start in row 0, so a translation can
    only split them.
  - In P4, the rotation by π/2 maps Δ_{0,k} and Δ_{0,k′} to squares of one column, in the rows
    coming from k and k′. For a piece with k ≠ k′ (adjacent columns), a two-time slice therefore has
    its factors in different rows of that column, and over part of the range their new times are
    less than 1 apart.
  - A non-integer time translation can then put both factors into one square. That raises the
    weight in (1.1.8) by (n+n′)!/(n! n′!) ≤ 2^{4p′}.
  - An integer translation preserves the lattice and every norm, at the cost of at most one unit of
    T in (1.1.16), that is, a factor e^{γ}.
  - Either way the effect is a bounded factor, the same kind of question as the constant. The
    verdict "reached on R1, granted the rotation presupposition" stands, but "raise no question" is
    too strong for P4.
  - Separately: Lemma N.13 gives the covariance of the measures. That a constructed monomial goes to
    the one with the translated kernel follows directly from Definition N.26 (Φ_κ(z)∘T_a = Φ_κ(z+a)),
    but the note does not state it. For rotations, the rotation presupposition states the analogue
    explicitly.
- *Repair.* Use integer translations for the two-time slices of P4 with k ≠ k′, or record the
  bounded factor; and add the one-line identity for the monomials.

**F16 (MINOR). Wording on the first page.**
- *Locator.* p. 1, ll. 63–72; title block, ll. 56–57.
- *Text.* "under the author's supervision"; "Theorem 12.2 of part_i/main.tex is unchanged".
- *Why.*
  - The council's brief says that the author authorised the work and that the orchestrator, an AI
    agent, supervises. Beside "Nothing in it has yet been read by a human", "under the author's
    supervision" suggests a human review that has not happened.
  - Relative to 49f2d23, the repository's working tree of 23 November rewords one sentence of
    Theorem 12.2's imports paragraph and the title of Corollary 12.3. The theorem's statement is
    unchanged.
- *Repair.* "commissioned by the author and supervised by the council's orchestrator (an AI agent)",
  or whatever the orchestrator confirms; and "Theorem 12.2 is not changed by this note".

**F17 (MINOR). The T.2 row omits record statements that T.15 uses.**
- *Locator.* §7.1, row T.2, ll. 1656–1657; compare §4(c), ll. 1118–1122.
- *Text.* "the statements of the record listed in \S\ref{sec:assembly}(c) and in the status line of
  Theorem~T.14".
- *Why.* T.15 now uses Lemmas 3.1(ii), 4.3(ii) and 4.4 of the record (its row, ll. 1675–1677). Neither
  §4(c) nor the status line of T.14 lists them. The status in the text of T.2 (ll. 266–267) points to
  the whole of §7 and is complete.
- *Repair.* "… and in the status lines of Theorem T.14 and Lemma T.15", and add the three lemmas to
  §4(c).

**F18 (cosmetic). Two loose references.**
- *Locator.* ll. 1455–1456; ll. 551, 912, 1058, 1505.
- *Why.*
  - The degree-0 pieces are said to be "reached after slicing … exactly as in Proposition T.19". In
    that case both partners are time-integrated with r = 1 and both are sliced, so the argument is
    that of Steps 1–4 with one-factor slices. T.19 slices only U.
  - "The commission", that is, the drafter's brief, is cited four times but is not identified for a
    reader of the archived note.
- *Repair.* Correct the cross-reference, and name or quote the commission where the note uses it.

### 8. Checks run for this re-check

**Documents read.**
- `route-t-revision.md` (249 lines) and `route-t-revision.diff` (954 lines).
- The revised note at every changed place, in full: ll. 50–270, 945–1080, 1094–1812.

**The revised note's build and script output** (I did not rebuild):
- `grep -cE '^!'` gives 0, `grep -c Overfull` gives 0, `grep -icE undefined` gives 0.
- `pdftotext | grep -nE '\?\?|TODO|Hmm|wait,'` gives nothing; `pdfinfo` gives 30 pages.
- `check_route_t.output.txt` ends "ALL CHECKS PASSED"; 24 lines contain "PASS" (23 PASS lines and the
  final one).
- a grep for machine-path prefixes on the note gives nothing.

**Greps on the note.**
- "this session": none. "instance of A2" and "imports this theorem": none. `ugjs/route_t.tex`: none.
- "rotation by $\pi$": only l. 1326, where the text says it is replaced.
- "commission": ll. 551, 912, 1058, 1505.

**Renders.**
- New crops: GJS p. 596 (Corollary 1.1.9, 300 dpi) and p. 628 (Q_n(y_0), 400 dpi).
- Re-read from my first pass: the renders of pp. 590, 595, 597, 600, 629 and of Simon pp. 163–164.

**The record at 49f2d23.**
- Every line listed in §4, with its `main.aux` number: `eq:fkn1` = (3), `eq:fkn2` = (2),
  `app:constants` = A, `rem:gjs7576` = 13.3, `aux:notation-kernel` = N.19, `lem:classes` = 3.1.
- Read in full: A2 (ll. 825–848), A5 (ll. 974–986), Lemma 3.1 (ll. 1518–1532), Lemma 4.3
  (ll. 1761–1800), N.19(v), N.32 (ll. 6244–6262) and Remark 3.3 (ll. 1658–1702).

**Comparisons.**
- The analysis audit, for its severities: it states "There are no CRITICAL and no MAJOR findings".
- REPO's working tree against 49f2d23: a `diff` of the block from `thm:MAIN` to `cor:canonical`
  shows exactly the two changes named in F16.
- REPO's `main.aux` against 49f2d23: 238 labels in each, no number differs, 199 pages differ.

### 9. Not done, not verified, not run

**Not done.**
- The analysis of the new proofs: T.15(ii) Steps 1–2 beyond their sources, and the measure theory of
  T.17(c) Step 1 beyond §5. This is the other auditor's part.
- A proof of the rotation presupposition.
- A check of the merging factor of F15 beyond the hand computation.

**Not verified.**
- "Nothing in it has yet been read by a human."
- The first-run FAIL record in the drafter's work directory, which I did not read.
- The drafter's count of 190 labels on different pages: at my comparison it was 199, because REPO is
  being edited.

**Not run.**
- `check_route_t.py`.
- Any LaTeX build; I read the existing log and output.

### 10. Updated answer to the author's question

**Now (49f2d23).** Items (1)–(4) and Corollary 12.3 are proved, conditional on A1–A8 and the
declared readings. A8(iv) is used in Lemma 7.4 and in Theorems D.3 and D.4, the latter also in its
transverse case A8(iv)-T. That case reaches the items through Theorem D.4 → Theorem 5.1 →
Lemma 10.2 and the rate Ψ_{m₁}. Under the standard "only cases the printed proof reaches" the items
fail on every reading, because no reading reaches A8(iv)-T.

**After Route T, as revised.** This assumes the note is integrated and the analysis auditor's
re-check of T.15(ii) and T.17(c) holds. Items (1)–(4) and Corollary 12.3 then carry the new rate
Ψ̃_{m₁} and are proved, conditional on:
- A1–A8, with A8(iv) used in P1–P4 only. Neither A8(iv)-T nor Theorem 5.1 nor Theorem D.4 is used.
- The same declared readings.
- The record's statements that the note lists.

A2 enters through its multi-time formula for bounded functions at two asymmetric times in a slab,
extended by the truncation of Lemma 4.3(ii). That use is within A2 as stated and as printed in
Simon's (V.47), and the record makes the same kind of use in its formulas (2) and (3). Simon's Remark
on p. 164 is no longer needed, so Route T adds no input to the record's imports.

**Under the stricter standard**, the items are covered if the following are accepted:
- Reading R1 of p. 596. It is the reading under which GJS's own application on p. 595, and their
  derivation of Theorem 1.1.8 from Theorem 1.1.11 (pp. 600, 629), are complete; no printed sentence
  states it.
- For P4 alone, the rotation presupposition.
- The question common to every case: the constant taken from Theorem 1.1.8 at the same h. The norm
  bookkeeping of F15 is a bounded instance of it.

The uniform gap and the gap clause of item (5) rest on P1 and P2, which the printed proof reaches on
either reading. The moment clause of item (5), Theorem 5.1 and Corollary 5.2 still rest on
A8(iv)-T.

**In one line:** Route T exchanges a case that no reading of the printed proof reaches for cases
reached on the reading that GJS's own proofs need. It costs nothing in imports, only a new rate
function.
