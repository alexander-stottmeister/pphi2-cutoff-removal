# Return: cqft, round R3 (§4, §5, §8.2, Appendix A, Appendix B)

23 October 2026. Everything below was read or measured in this session. Line numbers are
lines of `part_i/main.tex` unless another file is named. Pages are printed pages of
`part_i/main.pdf` (from `companion/council/labels.md`; unlabelled places checked with
`pdftotext -f p -l p part_i/main.pdf`).

Files that changed on disk while I worked, and that I re-read before relying on them:
`companion/preamble.tex` (15:03; the test builds use the current copy),
`companion/council/labels.md` (15:07; every number, title and page I use is unchanged; only
the "reaches A8" index moved from 24 to 29), `docs/status.md` and `README.md` (15:22; the
sentences I cite are unchanged, but the Part II table now sits at `docs/status.md`
l. 73–84), `companion/council/BRIEF.md` (15:22; §3 changes only the count).

## 1. Files, word counts, table sizes

Test builds: one wrapper per file plus one combined wrapper in
`…/scratchpad/cqft/`, `pdflatex -interaction=nonstopmode` three times each. Every build:
0 errors, 0 Overfull, 0 Underfull. Undefined references are only the expected ones
(`fig:quantifier`, `fig:slab`, `sec:result`, `sec:architecture`, `sec:lppl`,
`sec:identification`, plus `sec:import`, `sec:euclidean`, `sec:notclaimed` in the single
builds). Word counts by `texcount` (tables excluded; it counts math separately); page
extents measured from `pdftotext -bbox` (text height 672 pt), figures excluded.

| file | words (texcount) | without `\rec` locators | without locators and the *In the record* line | math | extent | budget |
|---|---|---|---|---|---|---|
| `s4-import.tex` | 679 | 619 | 570 | 37 inline, 2 display | 1.68 pp | 600 w ±10 %; 2.0 pp incl. Fig. 2 (0.4) and table (0.25) |
| ↳ A1–A7 table | – | – | – | – | **0.35 pp** | 0.25 pp (over) |
| `s5-euclidean.tex` | 522 | 483 | 436 | 77 inline, 4 display | **1.48 pp** | 600 w ±10 %; 1.75 pp incl. Fig. 3 (0.4) |
| `s8b-part2.tex` (text) | 207 | 198 | 188 | 2 inline | 0.67 pp (text + table) | ≤ 180 w; 0.75 pp |
| ↳ Part II table | – | – | – | – | 0.35 pp | 0.35 pp |
| `appA-pointers.tex` | – | – | – | – | 1.45 pp (heading, legend, 61 rows) | 1.5 pp |
| `appB-notation.tex` | – | – | – | – | **0.39 pp** (19 rows) | 0.3 pp (over) |

Overruns, stated plainly: the A1–A7 table (+0.10 pp), App B (+0.09 pp) and §5
(+0.13 pp against 1.35 pp of text; the four checkpoint boxes and five displays cost the
space, the prose is under its word budget). §4 as a whole is 1.68 pp + Fig. 2 = 2.08 pp
(+4 %). The §8.2 text is 188 words without locators, eight over 180 (see D1; the PLAN's
own text is 188 words by `wc`).

## 2. Every `\rec` locator, in order of appearance

| # | file | locator | page |
|---|---|---|---|
| 1 | s4 | §2.4 | 7 |
| 2 | s4 | (U_GJS) | 10 |
| 3 | s4 | Source Fact 2.3 | 10 |
| 4 | s4 | §4 | 15 |
| 5 | s4 | A8(vi) | 10 |
| 6 | s4 | Theorem 12.2 | 30 |
| 7 | s4 | A8(vii′) | 10–11 |
| 8 | s4 | A8, Scope (a) | 11 |
| 9 | s4 | Lemma 7.4 | 19 |
| 10 | s4 | A8, Scope (b) | 11–12 |
| 11 | s4 | Source Fact 2.4 | 10 |
| 12 | s4 | A8, Scope (c) | 12 |
| 13 | s4 | Proposition C.7 | 38 |
| 14 | s4 | Proposition C.1 | 36 |
| 15 | s4 | Lemma C.2 | 37 |
| 16 | s4 | Theorem C.5 | 38 |
| 17 | s4 | App. C | 35 |
| 18 | s4 | App. B, "External residue" | 35 |
| 19 | s4 | §2.4 | 7 |
| 20 | s4 | (P) | 9 |
| 21 | s5 | §4 | 15 |
| 22 | s5 | Lemma 4.1 | 15 |
| 23 | s5 | A1, Scope | 7 |
| 24 | s5 | (2) | 15 |
| 25 | s5 | Lemma 4.4 | 16 |
| 26 | s5 | A8(ii) | 9 |
| 27 | s5 | Theorem 5.1, eq. (5) | 17 |
| 28 | s5 | eq. (6) | 17 |
| 29 | s5 | (M₂) | 16 |
| 30 | s5 | Lemmas 7.1–7.3 | 18–19 |
| 31 | s5 | Lemma 7.4 | 19 |
| 32 | s5 | Proposition 7.5 | 20 |
| 33 | s5 | A8(ii) | 9 |
| 34 | s5 | Theorem 7.7 | 21 |
| 35 | s5 | Theorem 7.8 | 21 |
| 36 | s5 | (G) | 21 |
| 37 | s8b | §14 | 33 |
| 38 | s8b | §1.3(d) | 4 |
| 39 | s8b | §14 | 33 |
| 40 | s8b | §14 | 33 |
| 41 | appB | §2.1 (rows 𝓗/m₀, 𝔄, V(h), K/E/H, Ω/ω, β) | 6 (six times) |
| 42 | appB | A6 | 9 |
| 43 | appB | Definition 2.1 (two rows) | 6 |
| 44 | appB | §2.3 (two rows) | 7 |
| 45 | appB | A2 | 8 |
| 46 | appB | A3 | 8 |
| 47 | appB | A8(iii) | 10 |
| 48 | appB | A8(iv) | 10 |
| 49 | appB | §2.6 | 13 |
| 50 | appB | Theorem 5.1 | 16 |
| 51 | appB | §8 | 22 |
| 52 | appB | Lemma 9.1 | 24 |
| 53 | appB | Lemma 10.5 | 28 |
| 54 | appB | Prop. 10.4 | 27 |
| 55 | appB | Theorem 11.1 | 28 |

App A uses no `\rec`; its page column is labels.md's. The *In the record* lines (§4, §5,
§8.2) give the same numbers and pages in plain text.

Unlabelled pages, checked with `pdftotext`: §1.3(d) p. 4; A1 Scope p. 7; A1–A7 Sources
lines pp. 7–9 (A1 p. 7; A2, A3, A4 p. 8; A5, A6, A7 p. 9); A8(ii) p. 9; (U_GJS), SF 2.2–2.4,
the (vii′) heading p. 10, its passages (a)–(c) p. 11; Scope paragraph pp. 11–12 (steps (a)
and the start of (b) on p. 11; the end of (b), (c) and the conclusion on p. 12); App. B
"External residue" p. 35 (App. B begins p. 34); App. C introduction p. 35; §14 "Part II"
paragraph p. 33.

## 3. Verbatim quotations and transcriptions

§4 (`s4-import.tex`)
- Opening sentence: PLAN.md Part 2, table row §4 (verbatim).
- recordbox "Assumption A8(vi)": main.tex l. 694–705 (the display l. 700–705; tag shown as `\rec{(U_GJS)}{10}`).
- The frozen U_GJS sentence: PLAN.md, top. A programmatic comparison after removing the LaTeX markup returns EQUAL.
- "stated uniformly as the source cutoff tends to one": l. 687 (Source Fact 2.3).
- "deliberately limited to the audited mechanisms": l. 2742–2743 (Proposition C.1, proof).
- "a verdict on the printed record, not a no-go theorem": `docs/imports.md` l. 65.
- R27 wording "an h-trace of the printed expansion on GJS pp. 598–629, completing Prop C.1 (not scheduled)": PLAN.md Part 5, R27.
- A1 cell: "has $E(g)=\inf\spec K(g)$ as a \emph{simple} eigenvalue": l. 463.
- A6 cell: (P), transcribed inline without quotation marks: l. 596–597.
- "what it supplies" column: `docs/imports.md` l. 13–19. Verbatim for A2 (l. 14), A3 (l. 15) and A7 (l. 19); A1 (l. 13) verbatim plus the l. 463 quotation; A6 (l. 18) verbatim with the bold dropped, plus (P). A4 (l. 16) and A5 (l. 17) were rewritten (see D2).
- "source pinpoint" column: the Sources lines, l. 468–470 (A1), 502–504 (A2), 525 (A3), 550–551 (A4), 575–577 (A5), 601 (A6), 624 (A7). Citations transcribed; the descriptive words ("existence and uniqueness of the cutoff vacuum:" and so on) and A7's "the transformation of Wick powers under Γ(−1) is the parity of the polynomial" are dropped.
- Paraphrased without quotation marks, with their sources: Scope (a)–(c), l. 784–799; Prop. C.7 and its proof, l. 2919–2939; App. C introduction, l. 2653–2663; the C5 paragraph, l. 2639–2648; `part_i/C5_reading_record.md` (items 1–9, each "Verdict: ________"); `docs/status.md` l. 57–65 (C5, now; earlier l. 52–60); `docs/imports.md` l. 54–65 (Level 2 and the bypass).

§5 (`s5-euclidean.tex`)
- Opening sentence: PLAN.md Part 2, table row §5.
- Checkpoint I: eq. (2), l. 1054–1055. Lemma 4.4: "$\hat\psi_s\to\Om_g$ in norm, $\|\psi_s\|\downarrow c_g$" (l. 1124) and "No isolation of the ground-state eigenvalue is used." (l. 1126). The hypotheses before the display are my paraphrase of l. 1051–1052, without quotation marks.
- Checkpoint II: Theorem 5.1, l. 1158–1167, verbatim.
- Checkpoint III: Proposition 7.5, l. 1473–1478, verbatim.
- Checkpoint IV: Theorem 7.8, l. 1586–1591, verbatim.
- Paraphrased from: §4 preamble l. 1036–1038; A1 Scope l. 472–475; Lemma 4.4 proof l. 1129–1151; Thm 5.1 Steps 1–6, l. 1171–1240; A8(ii) l. 643–654; Lemmas 7.1–7.3 l. 1329–1426; Lemma 7.4 l. 1427–1469; Lemma 7.6, Thm 7.7, Thm 7.8 and their proofs, l. 1504–1620.

§8.2 (`s8b-part2.tex`)
- Text: PLAN.md §6.3, verbatim apart from the corrected clause (D1). A word-level diff against PLAN shows only that clause and the locator markup.
- "no mathematical dependence in either direction": l. 2531–2532.
- "proves no part of (II.11)": `part_ii/gate_II11_scoping.tex` l. 73 (abstract).
- Gate (II.11) paraphrase: `part_ii/gate_II11_scoping.tex` l. 98–117 (Definition 1.1, "the gate").
- Free-model sentence: l. 2533–2540.
- Table: `docs/status.md` l. 73 (header), l. 75–84 (ten rows). A programmatic comparison after mapping the LaTeX back (`\textbf`→`**`, `---`→—, `--`→–, `$P(\varphi)_2$`→P(φ)₂, `$V'\in L^1(\R)$`→V′ ∈ L¹(ℝ), `$(1-s)H_N+sH$`→(1−s)H_N + sH) returns ALL EQUAL.
- The three claims of the inconsistency sentence, as read at their files:
  - `strategy.md` l. 2205–2209: "**GATE STATUS.** V4's ledger now records: "A6, A7, A8 proved; (II.11) closed; Weyl criterion and identification invoked; … Part II's fixed-coarse program is complete at the stated import scope and under the standing parameter hypotheses." … I concur with that formulation".
  - V4's ledger, `part_ii/v4_assembly.tex` l. 1005–1011: "*Phase V4 gate:* A6, A7, A8 proved; (II.11) closed; Weyl criterion and identification invoked; erratum register updated. … Thus Part II's fixed-coarse program is complete at the stated import scope and under the standing parameter hypotheses." Its ledger table, l. 947: "Gate (II.11), pointwise in M,ξ & **proved**".
  - `part_ii/README.md` l. 3–4: "**Repair addendum (16 August 2026; supersedes all earlier phase-closure and open-residue statements below).**"; l. 70: "Lemma 3.1 ⟹ **gate (II.11) closed** pointwise in M, ξ" (12 August addendum); l. 74: "**Phase closure: NOT yet reached.**" (same addendum); l. 238–240: "**Status:** V4's ledger records (II.11) closed and the independent adversarial pass complete; Part II's fixed-coarse program is complete at the stated import scope and under the standing parameter hypotheses …"; l. 145–148 and l. 205–206 keep identification "open".
  - `README.md` l. 54: "**Part II** is open at gate (II.11)." (unchanged by the 15:22 edit).

App A: numbers, titles and pages from labels.md Part 1, in order. The reasons in the last column are sub-phrases of PLAN Part 1's Tier 3 table.
App B: the m₁ wording is the assignment's; everything else is paraphrase with locators.

## 4. `\cite` keys used

`GJS`, `GJ1`, `GJ2`, `GJ71`, `GJExp`, `Rosen70`, `SimonBook`, `GRS75` (§4: the text and
the A1–A7 table; `GJS` also in App A and App B) and `MMST` (§8.2). They are main.tex
`\bibitem`s at l. 2944 (GJ1), 2948 (GJ2), 2963 (GJ71), 2967 (GJExp), 2971 (GJS),
2984 (GRS75), 2988 (Rosen70), 2992 (SimonBook) and 3017 (MMST).

## 5. App A, column *depends on* (final)

- **U**: 5.1, 5.2, 7.1, 7.2, 7.3, 7.5, 7.6, 7.7, 7.8, 10.2, 10.3, 10.4, 10.5, 11.1, 11.2, 12.2, 12.3, 13.2, C.7.
- **G_γ**: 8.2, 9.3, 10.1.
- **P**: 3.2, 3.3, 6.2, **6.3**, 7.4.
- **import**: A1–A8, 2.2, 2.3, 2.4.
- **–**: 2.1, 2.5, 2.6, 2.7, 2.8, 3.1, 4.1, 4.2, 4.3, 4.4, 6.1, 8.1, 9.1, 9.2, 12.1, 13.1, 13.3, C.1, C.2, C.3, C.4, C.5, C.6.

**One change against the plan: Remark 6.3, "–" → "P".** Rem. 6.3 (l. 1313–1320) is a
statement about the printed GJS norm of a sharp-time monomial: changing the sharp time
changes "not the spatial cell assignments, local degrees, kernel norms, or the product of
weights" of that norm. That norm is the printed A8 item (iii), eq. (1) (l. 656–667), and the
remark uses no statement of class U. Under the plan's definition (P: "uses a printed A8
item — CE2, the norms, or the dilation — and nothing of class U") it is P, exactly as
Prop. 6.2, whose proof (l. 1294–1310) also uses only (1) and (1.1.9).

Entries I checked against their proofs and kept, including the ones R5 must re-derive:
- 3.2 P: the proof's only external input is the dilation, "as stated in \cite[p.~590]{GJS}" (l. 983).
- 3.3 P (a judgement; flag for R5). Rem. 3.3's argument (l. 995–1031) uses the dilation and Rem. 2.5 only. Its sentence "Every conclusion of Theorem 12.2, proved in the working (scaled) coordinates, therefore holds for the original model" (l. 1018–1020) transports conclusions that are themselves class U. But §2.6 (l. 892–897) invokes Rem. 3.3 *before* Theorem 12.2 to justify working coordinates, so the remark is an input to Theorem 12.2 for the original model; classifying it U would make the dependence circular. If R5 reads it as a corollary of Theorem 12.2, it becomes U.
- 4.3 –: the statement carries its own hypotheses ("Whenever Fψ_a ∈ ℋ", l. 1090; "whenever the two square moments are finite", l. 1101). The proof only says that (U_GJS) supplies them at the later applications (l. 1109–1116).
- 5.2 U: the displayed arithmetic consumes nothing by itself, but the corollary is the φ⁴ instance of the constant M of (M₂), Thm 5.1 (l. 1243–1250). Kept U as proposed.
- 6.2 P (l. 1283–1311), 7.4 P (l. 1427–1469: Source Fact 2.2, (1.1.9), Rem. 6.3 only).
- 8.2 G_γ: the proof uses (G_γ) at l. 1748 and l. 1775. 9.3 G_γ: assumed in the statement (l. 1909) and used at l. 1927. 10.1 G_γ: the filter is "admissible by (G_γ)" (l. 1979).
- 10.2 U: Theorem 5.1 is applied to g_s (l. 2011). 10.5 U: its last assertion combines Prop. 10.4 (l. 2126–2127).
- 12.1 –: the proof uses (P) (l. 2246, 2257) and spec H(g) ⊆ [0,∞); its hypothesis is norm convergence along (g_n).
- 13.2 U: uses Thm 12.2(1) (l. 2445) and (3)–(4) (l. 2454). 13.3 –: a literature-scope remark (l. 2480–).
- C.6 –: "This is the structural content of Source Fact 2.4" (l. 2916) interprets the source fact and deduces nothing from it; SF 2.4 is A8(vii), not CE2, the norms or the dilation. (The updated extractor now flags C.6; that is reference-reachability, not consumption.)
- C.7 U: stated under "Assume $U_{\rm GJS}$" (l. 2921).

Last column ("treated in, or why routine"): the § number wherever PLAN Part 2 places the
statement in a body section, and otherwise a reason of at most eight words, a sub-phrase
of the Tier 3 table. Where Part 2 treats a statement that Part 1 lists in Tier 3 without
†, I gave the section: Lemma 3.1 (§6, Part 2 §6 item 2), and Lemmas 7.1–7.3 and 7.6 (§5,
pieces III–IV). Shortened reasons: 2.5 "Wick order equals C-order"; 2.6 "Ω_g ∈ Ran e^{−tK(g)}, two
lines"; 3.2 "dilation into the printed region"; 3.3 "on working coordinates"; 4.2
"bounded, then signed"; 4.3 "unbounded, by truncation"; 5.2 "φ⁴ arithmetic"; 6.1 "cell
counting"; 6.2 and 6.3 "GJS norms"; 8.1 "Hölder bookkeeping"; C.3 and C.4 "not consumed
by Thm 12.2"; C.6 "source-mechanism audit". Hyp. 13.1, Thm 13.2 and Rem. 13.3 point to
§8.1 (`sec:notclaimed`). No count of any class is printed.

## 6. Unknowns, inconsistencies noticed (not fixed), departures

**Unknowns:** none.

**Inconsistencies or unclear wording in the record (none of them appears in the companion):**
- N1 (MINOR). `docs/imports.md` l. 16, A4: "the L^p smoothing used in the moment estimates". A4's "Used in" line (l. 557–558) is "§8 (the pairing bound), Appendix C (tail estimate)"; A4 does not enter (M₂). In a companion that calls (M₂) "the moment", the phrase misleads.
- N2 (MINOR). `docs/imports.md` l. 17, A5: "a core on which the algebra acts". A5(ii) (l. 571–573) is a common core for all K(g_s) on which K(g_s)ξ = K(g_{s₀})ξ + (s−s₀)V(g′−g)ξ.
- N3 (MINOR, Part II). `part_ii/README.md` contradicts itself: l. 74 "Phase closure: NOT yet reached" against l. 70 "gate (II.11) closed" and l. 238–240 "V4's ledger records (II.11) closed …". Its l. 3–4 says the 16 August addendum supersedes all earlier phase-closure statements. PLAN §6.3 and BRIEF §3 cite only l. 74.
- N4 (MINOR). The A8 Scope paragraph runs over pp. 11–12. PLAN Part 2 §4.3, the R5 checklist ("Scope, p. 11") and Fig. 2's caption (`\rec{A8, Scope paragraph}{11}`) give p. 11 only. A8(vii′) runs over pp. 10–11; PLAN says p. 10.
- N5 (MINOR). App. B's C5 paragraph ("External residue") is on p. 35. PLAN Part 2 §4.6 says "App B, p. 34", which is where App. B begins.
- N6 (MINOR). Source Fact 2.3 (l. 689) says that the source uses the quantifier "on pp. 595–597". The scope-amendment note (l. 79), the abstract (l. 110), the (vii′) source fact (l. 728), App. C (l. 2656) and the frozen sentence say "pp. 594–597", and (vii′)(a) quotes pp. 594–595.
- N7 (tooling). `\rec` prints "p." also for ranges ("p. 10–11", "p. 18–19"). A "pp." variant would need a preamble change, which I did not make.
- N8 (already in the register, untouched). F18: l. 780 "h↑1"; I avoided it as R24 directs. F2: l. 1349 `le`; not used.

**Departures from PLAN or BRIEF, with reasons:**
- D1. §8.2: I corrected the second claim of the inconsistency sentence, from "`part_ii/README.md` says that phase closure was not reached" to "`part_ii/README.md` says both that phase closure was not yet reached and that V4's ledger records (II.11) closed". The file says both (l. 74 and l. 238–240, quoted in §3). The original clause is literally true but presents a self-contradicting file as holding one position. Claims 1 and 3 are kept as they stand. The correction adds nine words, so the text is 188 words without locators, against ≤ 180.
- D2. A1–A7 table, "what it supplies": A4 and A5 rewritten from main.tex (N1, N2; rule 14: paraphrase the record's mathematics without the unclear phrase). A1 adds the quotation of A1's simplicity and A6 adds (P), as Part 1's Tier 3 row asks ("quoting only A1's simplicity and A6's (P)"). Page numbers were dropped from the import column for space.
- D3. Locators that differ from the plan: Scope (b) pp. 11–12 and (c) p. 12; A8(vii′) pp. 10–11; App. B "External residue" p. 35 (N4, N5).
- D4. App A: the number column holds bare numbers as labels.md gives them, under the header "no." for width. "U" entries are set in the `cond` violet. The last column follows the rule stated in §5 above.
- D5. Sizes: App B 0.39 pp (budget 0.3), with 19 one-line rows (ψ_s, ψ̂_s, c_g are left to §5, which defines them); A1–A7 table 0.35 pp (budget 0.25); §5 1.48 pp of text. App A, the Part II table and §8.2 are within budget.
- D6. §5 does not repeat the frozen sentence. It only mentions U_GJS, as "(A8(vi), §4)". I read rule 6 as binding the *description* of U_GJS, which §5 does not give. If the editor reads the rule as applying to every section that names U_GJS, the sentence would have to be added (75 words).
- D7. Rule 5 ("conditional on U_GJS" at the first mention of each class-U statement). §5 names all its class-U statements in one sentence that carries `\condtext`. In App A the legend carries it. In App B a preface sentence carries it, so that the m₁ row keeps exactly the prescribed wording. In §4, Theorem 12.2 carries `\condtext`, and Prop. C.7, Theorem 5.1 and Lemmas 7.1–7.3 carry it in plain text.
- D8. I added an *In the record* line at the end of `s8b` (rule 2). Since §8 is `s8a` + `s8b`, the editor may merge it with the line of §8.1.
- D9. Naming: "Level 2" comes from PLAN and `strategy.md` (`docs/imports.md` gives no name). "recorded as dead" is PLAN's wording; `docs/imports.md` says "found closed". The reason in parentheses ("g-uniform local moments were open in the 1970–71 literature") is from `docs/imports.md` l. 62–64.
- D10. Hits of the rule-10 grep that remain, all deliberate: "proved unconditionally" and "Lieb–Robinson" inside the verbatim `docs/status.md` table (§8.2); `\endfirsthead` (a LaTeX command) in App A; "vacuum" in the record's titles of Lemma 4.4 and Cor. 12.3 in App A. "ground state" occurs only for cutoff or lattice ground vectors (Ω_g of H(g), the mandated §5 opening, the A1 cell from `docs/imports.md`, App B, the lattice ground states of §8.2), never for the ground-state property of ω_∞ (rule 9, R32).
- D11. Mentions of the record's own sections ("§4", "§8", "§14", "§2.4") appear only inside `\rec` or with "the record's", so that they are not read as companion sections.
