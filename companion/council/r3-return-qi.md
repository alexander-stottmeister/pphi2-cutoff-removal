# Return file of `qi` (round R3): §3, §6, §9

23 October 2026. Sources read in this session: `companion/PLAN.md` (all parts), `companion/council/BRIEF.md`, `companion/council/labels.md` (re-read after its regeneration at 15:07:41; every number and page cited below is identical in both versions), `companion/preamble.tex` (re-read after the 15:03:56 change, which only added the TikZ library `patterns`), `companion/council/memo-qi.md`, `part_i/main.tex` (lines 1–905, 905–2760, 2930–3027), `part_i/main.pdf` (via `pdftotext`, pages 1, 3, 4, 5, 13, 15, 18, 19, 34, 35), `part_i/main.aux` (grep of every cited label), `README.md` (sections "What this is", "Status", "What is deliberately not in this repository", "Building", "How this record was produced"), `docs/status.md`, `part_i/C5_reading_record.md`, `fresh_audit_2026_08_16/render_evidence.sh` (lines 1–66 and the GJS lines), the figure drafts in `companion/figures/` and the Fig. 4 and Fig. 5 captions in `companion/companion.tex`.

## (1) Files and word counts

| file | budget (±10 %) | source count | rendered count | rendered length |
|---|---|---|---|---|
| `companion/sections/s3-architecture.tex` | 450 (405–495) | **445** (392 without inline math) | 601 | 0.95 pp (one page with the heading); Fig. 1 not included |
| `companion/sections/s6-lppl.tex` | 880 (792–968) | **836** (702 without inline math) | 1410 | ≈ 2.1 pp; Figs. 4–5 not included |
| `companion/sections/s9-record.tex` | 340 (306–374) | **374** (372 without inline math) | 396 | ≈ 0.75 pp |

- **Source count:** `.tex` minus comments, display-math environments and `\rec{..}{..}` locators; inline math counts as one word; commands stripped, text arguments kept (script `scratchpad/qi/wc.py`).
- **Rendered count:** `pdftotext` of the test build, minus running heads and page numbers (and, for §6, minus the test bibliography). It is far above the word budgets because each `\rec` renders as 5–8 tokens and inline math splits into many tokens.
- **Page budgets (Part 2):**
  - §3: 1.5 pp, of which Fig. 1 takes 0.5 → text 0.95 pp.
  - §6: 3.0 pp, of which Figs. 4–5 take 1.0 → text ≈ 2.1 pp, i.e. +5 % on the text share and within +10 % overall.
  - §9: 0.75 pp → ≈ 0.75 pp.
- **Test builds:** `/Library/TeX/texbin/pdflatex -interaction=nonstopmode`, twice, in `scratchpad/qi/` with the current preamble. Each fragment alone, and the three together, give 0 errors, 0 Overfull and 0 Underfull. The only undefined references are the expected ones: `fig:spine`, `fig:lppl` (×2), `fig:rate` and `sec:import` (×2). `pdftotext | grep -nE '\?\?|TODO|Hmm|wait,'` shows only those `??` placeholders.

## (2) Every `\rec` locator, in order of appearance

The source column says where each number and page was checked: L = `labels.md` row (and the same `\newlabel` in `main.aux`); P = rendered page of `main.pdf` (`pdftotext`), for unlabelled places.

| # | file:line | locator | page | checked against |
|---|---|---|---|---|
| 1 | s3:7 | §1.2 (five-step table) | 3 | P (table on p. 3; `sec:intro` p. 3) |
| 2 | s3:21 | §8 [for (G_γ)] | 22 | L `sec:path`, `eq:Ggamma` |
| 3 | s3:32 | Theorem 5.1, (M₂) | 16 | L `thm:M2`, `eq:M2` |
| 4 | s3:35 | Theorem 7.8, (G) | 21 | L `thm:G`, `eq:G` |
| 5 | s3:40 | Source Fact 2.2 | 10 | L `sf:CE2` |
| 6 | s3:41 | Lemma 7.4 | 19 | L `lem:ce2strip` |
| 7 | s3:42 | §7, opening sentence | 18 | L `sec:G`; P (sentence on p. 18) |
| 8 | s3:45 | Lemma 10.2 | 26 | L `lem:localize` |
| 9 | s3:49 | §11 | 28 | L `sec:limit` |
| 10 | s3:50 | Proposition 10.4, eq. (27) | 27 | L `prop:onepath`, `eq:onepath` |
| 11 | s3:59 | Theorem 11.1, eq. (31) | 28 | L `thm:cauchy`, `eq:rate` |
| 12 | s6:7 | §8 [for (G_γ)] | 22 | L |
| 13 | s6:9 | Lemma 10.5, eq. (29) | 28 | L `lem:rate`, `eq:Psidef` |
| 14 | s6:16 | Lemma 10.5 (tag of the contract) | 28 | L |
| 15 | s6:23 | Lemma 3.1(iii) | 13 | L `lem:classes`; P (clause (iii) on p. 13) |
| 16 | s6:27 | Proposition 8.2, eq. (15) | 23 | L `prop:projreg`, `eq:derivform` |
| 17 | s6:28 | Lemma 9.1 | 24 | L `lem:filter` |
| 18 | s6:33 | eq. (17) | 24 | L `eq:filterdef` |
| 19 | s6:37 | Lemma 9.1(ii), eq. (18) | 24 | L `eq:filterid` |
| 20 | s6:49 | (24) | 26 | L `eq:statederiv` |
| 21 | s6:55 | Proposition 2.7 | 12 | L `prop:propagation` |
| 22 | s6:60 | Lemma 10.2, eq. (25) | 26 | L `eq:localize` |
| 23 | s6:63 | §1.4 ("softening" quotation) | 5 | P (p. 5) |
| 24 | s6:67 | Lemma 9.2, eq. (19) | 25 | L `lem:separation`, `eq:sep` |
| 25 | s6:75 | (23) | 25 | L `eq:cluster` |
| 26 | s6:89 | Lemma 10.3, eq. (26) | 27 | L `lem:tworegime`, `eq:tworegime` |
| 27 | s6:106 | (27) | 27 | L |
| 28 | s6:112 | eq. (29) | 28 | L |
| 29 | s6:120 | (30) | 28 | L `eq:Psitail` |
| 30 | s6:127 | §1.4 (strip-analyticity remark) | 5 | P (p. 5, ll. 20–24 of `pdftotext`) |
| 31 | s6:128 | §1.3(b) | 4 | P (p. 4) |
| 32 | s6:140 | §1.4 ("does not start") | 4 | P (p. 4); L `subsec:strategy` p. 4 |
| 33 | s9:28 | App. B (P1, S1–S3, L1–L6) | 35 | P (register continues on p. 35) |
| 34 | s9:29 | App. B (gate R2) | 34 | P; L `app:provenance` p. 34 |
| 35 | s9:31 | title page (Scope amendment) | 1 | P (p. 1) |
| 36 | s9:34 | App. B (C5, External residue) | 35 | P |
| 37 | s9:41 | §2.4 | 7 | L `subsec:imports` |

Further numbers and pages appear in plain text:
- **Closing lines:**
  - §3: §1.2, p. 3; SF 2.2, p. 10; Thm 5.1, p. 16; Lemmas 7.1–7.4, pp. 18–19; Thm 7.8, p. 21; (G_γ), p. 22; Lemma 10.2, p. 26; Prop 10.4, p. 27; Thm 11.1, p. 28.
  - §6: Prop 2.7, p. 12; Lemma 3.1(iii), p. 13; (G_γ), p. 22; Prop 8.2 and eq. (15), p. 23; Lemma 9.1 and eqs. (17)–(18), p. 24; Lemmas 9.2–9.3 and eqs. (19), (23), p. 25; Lemmas 10.1–10.2 and eqs. (24)–(25), p. 26; Lemma 10.3, Prop 10.4 and eqs. (26)–(27), p. 27; Lemma 10.5 and eqs. (29)–(30), p. 28; §1.3(b), p. 4; §1.4, pp. 4–5.
  - §9: title page, p. 1; §2.4, p. 7; Appendix B, pp. 34–35.
- **Box titles:** Lemma 10.1, Lemma 9.3, Proposition 10.4, Lemma 10.5, Theorem 11.1.

All of these were checked against `labels.md` or the PDF.

## (3) Verbatim quotations and transcriptions

**In quotation marks**

| # | file:line | text | source |
|---|---|---|---|
| Q1 | s6:62–63 | "the operator-algebraic softening of the unboundedness" | `main.tex` ll. 316–317 (p. 5) |
| Q2 | s6:127–128 | "$\Psi_{m_1}$ is super-polynomial but not exponential, and this is intrinsic to the filter method used" | `main.tex` ll. 236–237 (p. 4) |
| Q3 | s6:139 | "does not start" | `main.tex` l. 264 (p. 4) |
| Q4 | s9:6 | "an experiment in open science" | `README.md` l. 9; the source has bold markup `**` between "an" and "experiment" |
| Q5 | s9:9 | "What this is" | `README.md` l. 7, the opening words of the heading "What this is: an AI-assisted, experimental open-science project" |
| Q6 | s9:30–31 | "No proof in the manuscript changed" | `main.tex` ll. 82–83 (p. 1) |

**Transcribed displays (checkpoint boxes and tagged displays; verbatim up to markup)**

§3:
- (M₂) $\|V(h)\Om_g\|\le M$: l. 1162. The box quantifiers are from Thm 5.1, ll. 1158–1160, worded as in Thm 12.2(5), ll. 2313–2314 ("real $h$ … supported in an interval of length 2", without "measurable").
- (G): l. 1588, with its quantifier from l. 1586.
- (31): ll. 2166–2167.
- (G_γ), stated in prose: ll. 1628–1629.

§6:
- Contract: ll. 2126–2127, without the opening words "In particular".
- (18): ll. 1800–1803. The trailing l. 1806, "a norm-convergent Bochner integral", is omitted (R26).
- (24): ll. 1960–1966.
- (23): display ll. 1913–1914; hypotheses from ll. 1909–1911, condensed ("for a bounded interval $O$" dropped).
- (26): $C_{j,s}$ at ll. 2016–2021, display at ll. 2024–2028.
- (27): ll. 2053–2058.
- (30): ll. 2121–2123.

Transcriptions in prose (§6):
- (15): ll. 1740, 1743.
- χ and (17): ll. 1785–1790.
- $T_\gamma$: l. 1797.
- (25) and the partition of unity: ll. 1994–2000.
- (29), "max{2, the same expression}": l. 2117.
- Prop 2.7: ll. 845–846; its proof's free speed one and Trotter formula: A6(i), ll. 590–592.
- Lemma 3.1(iii): ll. 914–916.
- $d_0:=4+2/\gamma$: l. 2053.
- $\gamma r_j/2\ge2\gamma+1$: l. 2066.
- Shell count: ll. 2084–2090.
- Exponential summand bound: ll. 2131–2133.

Transcriptions in prose (§3):
- §7 opening sentence: ll. 1325–1326.
- Instantiation of γ: ll. 2153–2155.
- Lemma 10.2 calling Thm 5.1: ll. 2010–2011.
- "Plateaus are cofinal and local duals are complete": l. 270, used unquoted.

Paraphrased from files other than main.tex (§9):
- `README.md` ll. 9–13, 17, 179, 187, 240–241.
- `docs/status.md`: gate table ll. 40–45; C5 note ll. 54–60.
- `part_i/C5_reading_record.md`: items 1–9, verdict lines 42–139, all blank.
- `main.tex` App B: l. 2620 (R2) and ll. 2625–2633 (P1, S1–S3, L1–L6), which read "Independent audit"; the companion avoids the word; C5 at ll. 2641–2648; §2.4 at ll. 455–458.

**PLAN wording used verbatim, without quotation marks**
- The three sentences to retain.
- The Fig. 1 legend wording.
- Rulings R16 (s6:91–93), R20 (s6:123–124), R25 (s6:124–127), R26 (s6:39), R31 (s3:39–45, as three sentences with their locators), R34 (s6:7–10), R35 (s3:13–15), R38 (s6:129–131) and R3 (s6:140).
- The Lemma 9.1(i) credit sentence (s6:113–114), followed by "; this controls the filter-tail summand."

## (4) `\cite` keys

- `Hastings` and `BMNS` (s6:139, in the `context` box only); `main.tex` `\bibitem`s at ll. 3009 and 3013.
- No other keys.
- The record itself is cited only through `\rec`. Files are cited by path: `README.md`, `docs/status.md`, `part_i/C5_reading_record.md`, `strategy.md`, `part_i/main.tex`, `part_i/main.aux`, and `fresh_audit_2026_08_16/render_evidence.sh` (new for the O3 list).

## (5) Unknowns, observations on the record, departures

**`unknown`:** none. No value was missing.

**Typos and inconsistencies noticed in the record.** None is fixed or mentioned in the companion.
1. l. 1349: `\|le` prints "le" (F2, already registered).
2. l. 1806: "a norm-convergent Bochner integral" (F11). Avoided by R26.
3. ll. 301–303: "as $\widehat W_\gamma$ must" (F9). Avoided by R25; my quotation Q2 is from §1.3(b), not §1.4.
4. l. 235: "true rate" (F10). Q2 starts after it.
5. Notation (new, MINOR): §1.4 l. 299 writes the filter identity with $P_0$; Lemma 9.1(ii) l. 1803 writes $P_{\ker H}$.
6. Render script (new, MINOR, documentation).
   - `README.md` l. 179 says `fresh_audit_2026_08_16/render_evidence.sh` "regenerates the audit's page-image corpus".
   - The script writes to `fresh_audit_2026_08_16/evidence/` (its l. 10). For GJS it renders PDF pages 1, 5, 6, 7, 10, 11, 12, 46 only (its ll. 59–66). By C5's "printed page = PDF page + 583", that excludes printed pp. 596–597, the pages of C5 item 9 and A8(vii′)(b).
   - No script in the repository regenerates `audit_2026/evidence/`, the dossier that `main.tex` §2.4 (ll. 456–458) names.
   - §9 states only what the script does.
7. The record calls the 9 August 2026 audit "independent" (ll. 192, 354, 2390, 2598, 2625), while `README.md` ll. 10–11 says the audit documents were drafted with the assistant. The companion never uses "independent" for an audit (Part 6.2 rule).
8. `labels.md` regenerated during this session: its header now reads "29 reach A8", where it read 24 at 10:24; `docs/status.md`, the README and BRIEF §3 say 24. My sections print no count.
9. The gate table in `docs/status.md` has six rows for eight gate names (G1/G2, G3a/G3b), so §9 gives no count of gates.

**Departures from PLAN or BRIEF, and decisions the editor should know about**
1. **No frozen U_GJS sentence in §§3, 6, 9.** None of these sections describes U_GJS.
   - They name it as "U_GJS (A8(vi))", with a pointer to §4.
   - They say where it is used (R31: "used at one fixed g, uniformly in T", "makes M independent of g").
   - §9 says its status was "re-based" and that closing C5 "does not change the status of U_GJS" (`docs/status.md` l. 59).
   - My reading is that rule 6 binds the first *description*. If R5 reads "first mention" instead, the frozen sentence must be added (about 95 words) to each of the three sections.
2. **Extra checkpoints.**
   - §3 has a box "the two numbers" with (M₂) and (G), which satisfies item 2 (the four checkpoints) and the three-step rule. (27) is stated in words in §3 and displayed in §6.
   - §6 has a box for (30), so that the rate paragraph stays within three steps.
3. **R31, bullet 1.** "applied across a horizontal strip" (Lemma 7.4's title) replaces "of width t − 2", because t is undefined in §3.
4. **"Not exponential" in §6.** I quote the record's own sentence (Q2, §1.3(b)) instead of inferring it from R25, and I keep R25's sentence verbatim. This reports "intrinsic to the filter method used" as the record's statement and adds no argument.
5. **Additional quotation in §6.** Q1, "the operator-algebraic softening of the unboundedness", which the qi role card names. It is not listed in PLAN §6.
6. **Order in piece VI.** Light cone → cells (25) → separation (19) → clustering (23), so that the piece ends at (23), as the plan says.
7. **Style, for consistency with the other drafts.**
   - Run-in italic heads "V.", "VI.", "VII.", "The rate." match `s5-euclidean.tex` ("I." … "IV.", which also says "Pieces I–III").
   - The closing lines use the "X, p. N;" format of `s5`/`s7`.
   - §9 uses run-in italic heads.
8. **Class-U qualifier.** "Conditional on U_GJS" is also attached to Lemma 10.2, Lemma 10.3 and Lemmas 7.1–7.3 (App A's U column, which R5 item 3 checks), not only to the rule-5 list.
9. **§9, corrections.**
   - P1 is phrased "a missing premise, now (B4) of Hypothesis 13.1", following App B l. 2626 and the plan's "audit P1 → Hyp 13.1 with (B4)". This avoids naming Theorem 13.2 (class U) without its qualifier.
   - "Re-based" and "No proof in the manuscript changed" come from `main.tex` p. 1 (ll. 76, 82–83), because neither App B nor the README states that no proof changed.
10. **§9, adversarial passes.** "which the README says the assistant ran" is the plan's phrase. It appears without quotation marks because it is not README text; the README's wording is at ll. 240–241.
11. **Macro note for the orchestrator.** `\rec` always prints "p.", so a page range renders as "p. 34–35". I split App. B into p. 34 and p. 35. Other drafts may contain `\rec{…}{a--b}`.
12. **Figure references.**
    - Fig. 4 panels (a), (b), (c) and the content of Fig. 5 follow the captions now in `companion.tex`.
    - The text says only that Fig. 5 draws the trivial bound (author decision of 23 Oct); it gives no heights, decay laws or values.
13. **Banned-word grep.** Case-insensitive, over all rule-10 items plus "proved", "ground state" and "independent audit".
    - The only hits are in the §6 `context` box: "quasi-adiabatic/automorphic-equivalence" (the record's l. 263 wording, as what does not start), "spectral flow" (R3, as what is not done) and "no Lieb–Robinson bound is needed".
    - The one "ground state" (s3:12) carries "in the spectral sense (Proposition 12.1)".
    - "Converges in norm" (s3:24, s3:53) carries "on every local algebra $\A(O)$" and "in each $\A(O)^*$" respectively.
