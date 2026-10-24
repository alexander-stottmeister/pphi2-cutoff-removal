# R4 editor report: reader's companion (23 October 2026)

*Saved by the orchestrator from the editor agent's hand-back message. The editor could not
write files under `companion/council/` itself (the subagent harness returns reports as text
only); the text below is the report as delivered, unchanged.*

---

**What I read in this session:**
- `BRIEF.md`, `PLAN.md` (all of it), the three return files, `preamble.tex`, `companion.tex`, the twelve fragments and `labels.md`.
- `part_i/main.tex`: lines 55–2945 in large blocks, plus greps; per-page `pdftotext` of `main.pdf`.
- `docs/imports.md`, `docs/status.md`, `README.md` (ll. 1–80, 178–266), `part_i/C5_reading_record.md`, `part_ii/README.md` (ll. 1–8, 66–76, 236–242), `part_ii/gate_II11_scoping.tex` (abstract, ll. 95–118), `strategy.md` (ll. 2203–2232, greps for "Level 2").
- GJ3 printed pp. 210–211, rendered as page images.

**What I touched:** only `companion/sections/*.tex` and figure placement in `companion.tex`. I ran `make_bib.py` once; `bib.tex` came out byte-identical. No git or kb command, no file deleted.

**Tooling note:** in this shell, `grep` is a wrapper that skips git-ignored files, so `grep … companion.log` prints nothing. Use `command grep` for the gates.

## (1) Build and measurements

Built from `companion/` with `/Library/TeX/texbin/pdflatex -interaction=nonstopmode companion.tex`, three passes.

| check | result |
|---|---|
| `^!` (errors) | 0 |
| Overfull | 0 |
| undefined (case-insensitive) | 0 |
| `pdftotext … \| grep -nE '\?\?\|TODO\|Hmm\|wait,'` | empty |
| pages (`pdfinfo` and "Output written") | **20** |
| Underfull (not a gate) | 3, inside `figures/fig-slab.tex`; already there at R3 |

**Slack is thin.** Text on p. 20 ends at y ≈ 645 pt; full pages end at about 750–760 pt. That leaves about 115 pt (≈ 0.17 pp). The six floats and the unbreakable `checkpoint` boxes make pagination jump, so any later change of more than about eight lines needs a fresh page count.

**Start pages** (from `companion.aux`; the appendices and references from `pdftotext -bbox`):

| item | page |
|---|---|
| §1 | 1 |
| Table 1 (ledger) | 3 |
| §2 | 3 |
| Table 2 (GJ3 vs record) | 4 |
| §3 | 4 |
| Fig. 1 | 5 |
| §4 | 6 |
| Fig. 2 | 7 |
| §5 | 8 |
| Fig. 3 | 9 |
| §6 | 10 |
| Fig. 4 | 11 |
| Fig. 5 | 12 |
| §7 | 14 |
| Fig. 6 | 15 |
| §8 and §8.1 | 16 |
| §8.2 | 16 |
| §9 | 17 |
| App A | 18 |
| App B | 19 |
| References | 19–20 |

Every figure now appears at or after the start of the section that first cites it.

**Rendered extents, floats included (pp):**

| part | extent |
|---|---|
| §1 | 1.87 |
| §2 | 1.14 |
| §3 (with Fig. 1) | 1.77 |
| §4 (with Fig. 2 and the A1–A7 table) | 2.32 |
| §5 (with Fig. 3) | 2.01 |
| §6 (with Figs. 4–5) | 3.64 |
| §7 (with Fig. 6) | 1.43 |
| §8.1 | 0.48 |
| §8.2 | 0.78 |
| §9 | 0.74 |
| App A | 1.46 |
| App B | ≈ 0.37 |
| references | ≈ 0.97 |

Two sub-budgets are still exceeded, although the total is met:
- the A1–A7 table is ≈ 0.27 pp (it was 0.35; budget 0.25);
- App B is ≈ 0.37 pp including heading and preface (budget 0.3).

**Front-matter word counts** (`pdftotext` of p. 1, then `wc -w`):

| block | count | limit |
|---|---|---|
| status notice | 69 | ≤ 80 |
| how-to-read | 55 | ≤ 60 |
| abstract | **153** | ≤ 150 |

The abstract fails the literal test. pdftotext splits its formulas into separate tokens:
- "for 0 ≤ λ/m20 < εP ," becomes 7 tokens, and "P (φ)2" becomes 2;
- the closing ")" of "(for even P )" and the "," after "UGJS" each count as a word;
- the line break inside "Glimm–Jaffe–Spencer" makes 2 tokens.

Counting each formula as one word gives 144. I may not edit the front matter; a fix is proposed in (6).

## (2) Changes, section by section

None of the quoted or ruled wording was reworded:
- The frozen U_GJS sentence is verbatim in §1 and §4; I compared it programmatically with PLAN l. 9.
- Rulings R16, R20, R21, R23, R25, R26, R27, R35 and R38 are verbatim.
- The Lemma 9.1(i) credit sentence is verbatim.
- The only adaptation is capitalising R38's "These" at the start of its sentence.

One quotation was removed (Q1 in §6). One GJ3-column cell was re-attributed to the record (§2).

**Throughout.**
- Run-in headings are `\emph{…}` everywhere.
- The `\medskip`/`\noindent` spacing after the italic opening sentences and before the closing lines is gone.
- Each section closes with one `\noindent\emph{In the record:}` line: full statement names in page order, consecutive pages grouped as "pp. a–b". Each item's exact page stays in its in-text `\rec`. §8 has a single closing line, at the end of §8.2.
- Doubled locators ("Lemma 7.4 [R, Lemma 7.4, p. 19]") are removed.
- "App./Thm/Prop." are spelled out, except inside fixed or ruled text: the frozen sentence, R27's "Prop C.1", App B's m₁ row, App A's reasons, and the ledger.
- Companion prose uses British spelling; titles and quotations keep the record's spelling.

**§1** (never cut; nothing removed).
- Setting: the interaction polynomial 𝒫(ξ)=Σ_{n=0}^{2p′}a_nξⁿ is now defined, because (M₂) in §5 uses a_n and p′.
- "Ψ_γ of (29) at the gap parameter γ=m₁": γ is now named.
- The claims ledger moved from a `checkpoint` box to Table 1 (B(iii)).
  - Row labels use status words: "proved, conditional on U_GJS"; "proved, independent of A8 (the GJS package)"; "proved as implications under a stated hypothesis"; "not claimed; open". Cells are unchanged.
  - New caption: "Claims ledger, read from the record's proofs. Appendix A classifies every numbered statement of the record."
- The status-words paragraph now comes first and points to Table 1 and Fig. 1.

**§2.**
- The GRS sentence is condensed: the two problems go in a parenthesis, worded "the Euclidean vacuum density" as in the record's §14.
- The selection cell is re-attributed (B(iv)). The caption adds "its last cell quotes the record".
- Rule 9: "a theorem about norm convergence of this Hamiltonian cutoff net" became "local-norm convergence".

**§3.**
- The "two numbers" box is replaced by an inline sentence with both locators, pointing to "Theorem 12.2(5) … for the cutoff Hamiltonians H(g), g∈𝒞_H (§1)" (B(v)).
- "GJS input" (the abbreviation is defined in §1). "The printed clustering estimate CE2".
- FKN is defined at first use, so R35's verbatim "slab FKN transfer" is defined.
- "The output of §§8–10" became "Their output", because bare §§ references read as companion sections.
- The (31) checkpoint stays.

**§4** (never cut; nothing removed).
- The A8 sentence now defines dq_h (h∈𝒞_E, of A3), Q(x⁰) and ‖·‖_GJS before the A8(vi) box uses them. It also glosses CE2 and CE1 as the clustering estimate and the moment bound, which is the record's own §1.4 wording.
- Doubled locators removed. Step (c) now reads "GJS p. 629, as quoted in [R, Source Fact 2.4, p. 10]".
- Level 2 attribution is corrected. `docs/imports.md` does not use the name; `strategy.md` does (ll. 2235, 2275). The sentence now reads "which strategy.md calls Level 2, is recorded in docs/imports.md: …"; the R27 wording is intact.
- The bypass is "recorded as dead in strategy.md" (l. 2229), followed by the `imports.md` quotation (l. 65).
- A1–A7 table: from 0.35 pp to ≈ 0.27 pp.
  - New layout: number, then "import: what it supplies" with the name in italics, then source pinpoint. The "(Sources line)" header is dropped.
  - A2's and A4's SimonBook pinpoints are merged into one `\cite` each; the pinpoints are the same.
  - A1 drops "existence and normalization of". A3 drops "0<Z(h)<∞ and".
  - A5: "Ω_g∈D(V_j)" became "Ω_g∈D(V(h))". V_j is first defined in §6, and A5(i) gives this inclusion (record Prop 2.6).
  - A6: its `\rec{(P)}{9}` is dropped. The quotations of A1's simplicity and A6's (P) are kept.

**§5** (rule 11).
- Opening: dropped "§3 says where each uniformity … comes from". Also dropped "Lemmas 4.1 and 4.4 use no part of A8, Lemma 7.4 only printed CE2"; Pieces I and III and App A carry that.
- Piece I:
  - dropped the redefinition of h_{T,g};
  - defined Ω₀≡1 (the free vacuum) and the Euclidean field Φ, both used in Checkpoint I;
  - condensed the simplicity step;
  - dropped "Isolation of E(g) is not imported (A1, Scope)": the opening and Checkpoint I's Lemma 4.4 quotation say it, and the A1-Scope entry left the closing line.
- Piece II: adds "constants K₁ and K₂≥1 [R, A8(iii), p. 10]".
- Piece III: condensed; names CE2's constants C₇, m₁ with the Source Fact 2.2 locator.
- Piece IV:
  - the Lemma 7.6 sentence is condensed;
  - "under |Ω_g|²dφ₀" became "in the vector state of Ω_g", since dφ₀ is undefined;
  - added `\rec{Lemma~7.6}{20}`.
- All four checkpoints are unchanged.

**§6** (rule 11).
- Display (30) moved into the opening contract checkpoint; both are Lemma 10.5. The separate rate box is gone, and the rate paragraph says "Together they give (30), the second display of the contract above."
- The Fig. 4 sentence is shortened to "draws the three moves that prove it".
- W_γ is now "the inverse Fourier transform of Ŵ_γ" with the (17) locator; that is the record's own term.
- Light cone: "from A6(i)".
- The cells sentence is condensed.
- **Q1 is removed:** "the operator-algebraic softening of the unboundedness". It was qi's addition, not in PLAN; removed for budget.
- Lemma 9.3: "by the spectral separation [R, Lemma 9.2, eq. (19)]".
- "Here χ is fixed once in (17);" is removed. R38 now sits right after (30), so "these constants" refers to C_{q,γ} and C_{N,γ,M}.
- The final Fig. 5 sentence is shortened.
- Context box: "The machinery of [Hastings, BMNS] 'does not start' here … (§2; [R, §1.4, p. 4])". This drops the "quasi-adiabatic/automorphic-equivalence" wording and no longer repeats §2's box. R3 and "no Lieb–Robinson bound is needed" are kept.
- `\par\nopagebreak` after the opening sentence keeps the section heading from being stranded at a page foot.

**§7.**
- The (31) box is removed; it was the third display of (31), after §1's item (1) and §3's checkpoint. Step 3 now ends "this is the checkpoint (31) displayed at the end of §3 [R, (31), p. 28]". Steps 1–3 stay within three steps.
- `equation` + `\tag*` became `equation*`; no visible change.

**§8** (never cut).
- §8.1 is unchanged except that its closing line moved to the end of §8.2.
- §8.2 text is unchanged; cqft's D1 correction is accepted.
- The status table is now a `longtable` with a repeated header. The unbreakable version left ≈ 95 pt empty at a page foot.
- The cells are unchanged: all ten rows equal `docs/status.md` ll. 75–84 character for character after mapping the LaTeX back, checked programmatically.
- The table currently breaks 8 + 2 across pp. 16–17.

**§9.**
- The C5 paragraph no longer repeats §4: "Audit item C5 (§4) is open [R, Appendix B, p. 35]: all nine verdicts of … are blank."
- The render script is now named through README.md. Its path, `fresh_audit_2026_08_16/render_evidence.sh`, is not in the bibliography's file list, and `make_bib.py` is not mine to edit.
- "U_GJS (A8(vi); §4)".
- `\allowbreak` in the C5 path fixes an 81 pt overfull box.

**App A.**
- Column widths: title 6.3→7.1 cm, last column 5.0→4.2 cm. Wrapped rows drop from 8 to 4. No class changed.
- "Treated in": A6 is now §§4, 6, 7; Source Fact 2.2 is now §§3, 4, 5.
- 2.6's reason is now "Ω_g∈D(V(h)) in two lines", a PLAN Tier-3 sub-phrase.

**App B.**
- 19 → 15 rows. Removed τ_a/θ, C₇/C₈/K₁/K₂, γ/g_s and W_γ/T_γ; each is defined in the body where it is used.
- 𝒫 is added to the V(h) row.
- Now a `longtable`. The m₁ row keeps the prescribed wording.

**companion.tex** (figure placement only).
- Fig. 4: `[htbp]` → `[t]`. It is 0.854 of the text height and had formed a float page alone, with about 7 lines empty, placed before §6.
- Fig. 6: moved after `\input{sections/s7-identification}`, with `[t]`. It now sits on p. 15, inside §7.
- Captions, front matter and the title block are untouched.

## (3) Decisions B(i)–(viii)

**B(i) Where the frozen U_GJS sentence stands.**
- It is verbatim at the only two places that describe U_GJS: §1 ("The import.") and §4 (after the A8(vi) box).
- Everywhere else U_GJS is named, never described. It appears either as the hypothesis in "conditional on U_GJS", or as what a proof uses (§3's R31 sentences, §5's "(U_GJS) at h_{T,g}", §8.1's R23 wording).
- Where a section names it outside the qualifier (§§3, 5, 9), the first naming carries the pointer "(A8(vi); §4)".
- No other sentence says what U_GJS is, at what scope it is imported, or whether it is strengthened. §9's "re-based the status of U_GJS" is the record's title-page wording about its history.
- Repeating the sentence in §§3, 5, 6, 9 would cost about 95 words each and add nothing. R5 should therefore check "first description", not "first mention".

**B(ii) Run-in headings.** `\emph{…}` throughout. `\paragraph` adds vertical space and a second visual register, and most drafts already used `\emph`.

**B(iii) Claims ledger.**
- It is a booktabs float, Table 1 `[ht]`, on p. 3, still inside §1.
- It is not a `checkpoint` or `recordbox`: rule 1 reserves those for transcriptions from main.tex that carry `\rec`, and the ledger is the companion's own classification.
- Row labels use status words; the contents are as drafted.
- The caption points to App A because the ledger is not exhaustive: 5.2, 7.1–7.3, 7.5–7.7 and C.7 are class U but not listed.

**B(iv) GJ3 "selection" row.**
- Kept, and re-attributed: "the record's reading: compactness 'selects a state but proves neither convergence nor canonicity' [R, §1.4, p. 4]" (main.tex l. 255).
- "none" is gone. It was a negative claim about GJ3 that R5 cannot confirm at pp. 210–211.
- The `% (R5)` marker stays, with a source comment saying R5 checks this cell against main.tex rather than GJ3.
- Kept because the row carries the record's news (Corollary 12.3).

**B(v) qi's extra checkpoints.**
- The §3 "two numbers" box is removed and replaced by an inline sentence pointing to Theorem 12.2(5). It was the third display of (M₂)/(G), after §1, which is on the 15-minute path, and §5's Checkpoints II and IV.
- The §6 (30) box is merged into the opening contract box.
- §7's (31) box gives way to §3's.

**B(vi) §7 identity display.**
- Verbatim: main.tex ll. 2248–2250, ending "= G_g(t) .".
- G_g and ρ_g are defined in the next sentence, paraphrasing ll. 2243–2245.
- PLAN's merged form is not verbatim, and a display tagged `\rec{proof of Proposition~12.1}{29}` must transcribe. Fig. 6's inset can keep the merged form.

**B(vii) App A.**
- The "treated in" entries were checked against the edited text; three changed (see (2)).
- Remark 6.3 as class P is accepted. Its statement concerns the printed GJS norm (A8(iii)) and uses nothing of class U, like Proposition 6.2.
- R5 should re-derive 6.3 together with the Part 8 item 9 list, and look at cqft's flag on Remark 3.3.

**B(viii) Other items in the return files.**
- **Locators.** Accepted after checking with pdftotext: (1.1.11) on p. 11; the Scope paragraph on pp. 11–12 ((a) p. 11, (b) pp. 11–12, (c) p. 12); App B's C5 paragraph on p. 35.
- **cqft D1 (§8.2 correction).** Accepted. I verified `part_ii/README.md` l. 70, l. 74 and ll. 238–240. The §8.2 text is 188 words against 180; §8 is never cut.
- **cqft D2 (A4/A5 cells).** Accepted, after checking A4's "Used in" (main.tex l. 557) and A5(ii) (ll. 571–573).
- **Quotations Q1 and Q2 (qi).** Q2, the §1.3(b) quotation, is kept because R25 asks for it. Q1 is removed.
- **Page ranges.** All now use `\recpp`.
- **Kept as drafted.** aqft items 3–6, 10, 11 and 13; qi items 3, 6, 8, 9 and 12; cqft D7, D10 and D11. `\varepsilon_{\mathscr P}` stays in the body.
- **Sub-budgets.** App B and the A1–A7 table remain slightly over their sub-budgets. With them as they stand the total is 20 pages, and further cuts would cost the reader more than the 0.1 pp they save.

## (4) Banned-word grep (rule 10)

Run over the rendered text of all 20 pages, including captions, figure labels and the bibliography; case-insensitive, with hyphenated line breaks joined. I added "vacuum", "unique(ness)" and "independent(ly) audit" to the rule-10 list.

**Zero hits** for: unique vacuum, the vacuum, mass gap, gapped limit, exponential rate, exponential convergence, exponential clustering, verified, solves, settles, strongest, compactness-free, no compactness, purely Hamiltonian, quasi-adiabatic, Bochner, true rate, then-stuck, swallow, trivial bound survives, clearly, obviously, standard, independent(ly) audit.

**Hits, each in an allowed context:**

| term | page and context | why allowed |
|---|---|---|
| unconditional | p. 16, "proved unconditionally" | cell of the verbatim `docs/status.md` table |
| first | p. 1, "Read this first." | fixed status notice; not a priority claim |
| spectral flow | p. 11, Fig. 4 caption | mandatory Part 3 sentence stating what is not done |
| spectral flow | p. 14, §6 context box | stating what is not done |
| automorphic | p. 20, BMNS title | verbatim `\bibitem` |
| Lieb | p. 11, Fig. 4(a) "no Lieb–Robinson bound is needed" | the allowed phrase |
| Lieb | p. 14, §6 context box, same phrase | the allowed phrase |
| Lieb | p. 16, "Lieb–Robinson" | verbatim status table |
| Lieb | p. 20, "Lieb–Schultz–Mattis" | Hastings title |
| vacuum (8 hits) | §2 opening "gave Glimm and Jaffe a vacuum" | PLAN-fixed sentence |
| | "vacuum expectation values" | context of a record quotation |
| | "the Euclidean vacuum density" | the record's §14 wording |
| | "Ω₀≡1 the free vacuum" | names Ω₀, not ω_∞ |
| | two App A titles; two bibitem titles | verbatim titles |
| unique | p. 16, "Not unique, not sharp, …" | PLAN-fixed §8 opening, a negation |
| uniqueness (10 hits) | non-claims; AHZ/BDW as the record describes them; "Fourier uniqueness"; bibitem titles | — |

None of the "vacuum" hits denotes ω_∞.

**Rule 9 checked the same way:**
- Every "ground state" carries "in the spectral sense", or names a cutoff or lattice ground vector. Those are the A1 cell, the PLAN-fixed §5 and §7 openings, the verbatim §8.2 text and table, and record titles.
- Every norm-convergence phrase carries "on every 𝔄(O)", "in each 𝔄(O)*", "on 𝔄(O_T)" or "local-norm", except inside the verbatim table.
- Both mentions of item (5) say "the cutoff Hamiltonians H(g), g∈𝒞_H".
- m₁ is used only for the GJS constant; the quadratic model's mass is m.
- The abstract's "in a spectral sense" is in (6).

## (5) Locators and quotations after the edit

**(5a) Locators.** There are 158 `\rec`/`\recpp` occurrences: 139 in the fragments and 19 in captions. Every labelled number and page was checked against `labels.md`, and every unlabelled place against the `pdftotext` of that page of `main.pdf`. Line numbers below are lines of the edited files.

Labelled items, all agreeing with `labels.md`:

| file | line: locator, page |
|---|---|
| appB | 33, 35: Def 2.1, 6 · 36: A2, 8 · 37: A3, 8 · 31: A6, 9 · 39: A8(iii), 10 · 43: Thm 5.1, 16 · 44: Lem 10.5, 28 · 45: Prop 10.4, 27 · 46: Thm 11.1, 28 |
| s1 | 18: Def 2.1, 6 · 31: (M₂), 16 · 32: (29), 28 · 61: Prop 3.2, 13 · 80: Cor 12.3, 31 · 83: Prop 12.1, 29 |
| s2 | 36: Thm 12.2, 30 · 41: Thm 12.2(1), 30 · 47: Thm 11.1, 28 · 51: Prop 11.2, 29 · 57: Prop 12.1, 29 · 63: Cor 12.3, 31 |
| s3 | 31: Thm 5.1/(M₂), 16 · 32: Thm 7.8/(G), 21 · 35: SF 2.2, 10 · 36: Lem 7.4, 19 · 40: Lem 10.2, 26 · 45: Prop 10.4/(27), 27 · 54: Thm 11.1/(31), 28 |
| s4 | 22: (U_GJS), 10 · 34: SF 2.3, 10 · 38: Thm 12.2, 30 · 54: SF 2.4, 10 · 60: Prop C.7, 38 · 66: Prop C.1, 36 · 67: Lem C.2, 37 · 67: Thm C.5, 38 |
| s5 | 15: Lem 4.1, 15 · 26: (2), 15 · 29: Lem 4.4, 16 · 37: Thm 5.1, eq. (5), **17** (`eq:QVnorm` is p. 17; the theorem itself is p. 16) · 38: eq. (6), 17 · 50: (M₂), 16 · 57: Lemmas 7.1–7.3, pp. 18–19 · 58: SF 2.2, 10 · 61: Lem 7.4, 19 · 69: Prop 7.5, 20 · 75: Lem 7.6, 20 · 77: Thm 7.7, 21 · 79: Thm 7.8, 21 · 85: (G), 21 |
| s6 | 9: Lem 10.5/(29), 28 · 16: Lem 10.5, 28 · 21: (30), 28 · 28: Lem 3.1(iii), 13 · 32: Prop 8.2/(15), 23 · 33: Lem 9.1, 24 · 37: (17), 24 · 41: Lem 9.1(ii)/(18), 24 · 53: (24), 26 · 59: Prop 2.7, 12 · 64: Lem 10.2/(25), 26 · 69: Lem 9.2/(19), 25 · 77: (23), 25 · 92: Lem 10.3/(26), 27 · 109: (27), 27 · 115: (29), 28 |
| s7 | 9: Thm 11.1, 28 · 11: (32), 28 · 16: (31), 28 · 20: Prop 11.2, 29 · 25: A6, 9 · 32: proof of Prop 12.1, 29 · 55: Lem 2.8, 12 · 56: proof of Thm 12.2, 30 · 59: Cor 12.3, 31 |
| s8a | 13: Prop 12.1, 29 · 25: Rem 13.3, 32 |
| captions (`companion.tex`) | 87–90: Lem 4.1/(2), 15; Lem 7.4, 19; Lem 4.4, 16; Prop 7.5, 20; Thm 7.8, 21 · 103–107: Lem 10.1/(24), 26; Prop 10.4 Step 2, 27; Lem 10.2, 26; Prop 10.4 Step 3, 27; Lem 10.3, 27; Prop 2.7, 12 · 118–120: Lem 9.1/(17), 24; Lem 9.1(i), 24; Lem 10.5/(29), 28 · 144, 148, 149: A6, 9; A6/(P), 9; Prop 12.1, 29 |

For the two proof locators I confirmed the page text: "Exact identity" is on p. 29, and "order isomorphism of G" on p. 30.

Unlabelled items, checked on the page:

| file | line: locator, page |
|---|---|
| appB | 22, 24, 26, 27, 29, 30: §2.1, 6 · 40: A8(iv), 10 · 42: §2.6, 13 |
| s1 | 12: §2.1, 6 · 12: A6, 9 · 26: §2.6, 13 · 30: §2.3, 7 · 30: A8(iv), 10 · 67: A8(vi), 10 · 83: §1.3, 4 |
| s2 | 12, 72, 85: §1.1, 3 · 18: §14, 32 (GRS paragraph) · 61, 77, 81: §1.4, 4 · 75: A8(vii′)(a), 11 |
| s3 | 7: §1.2, 3 · 21: §8, 22 · 37: §7 opening sentence, 18 · 44: §11, 28 |
| s4 | 7, 81: §2.4, 7 · 35: §4, 15 · 36: A8(vi), 10 · 41: A8(vii′), pp. 10–11 · 48: Scope (a), 11 · 53: Scope (b), pp. 11–12 · 56: Scope (c), 12 · 68: App C, 35 · 71: App B "External residue", 35 |
| s5 | 8: §4, 15 · 34, 76: A8(ii), 9 · 36: A8(iii), 10 |
| s6 | 7: §8, 22 · 124: §1.4, 5 · 125: §1.3(b), 4 · 131: §1.4, 4 |
| s8a | 14: §1.3(a), 4 · 14: §14 Uniqueness, 33 · 17: §1.3(b), 4 · 18: §14 Sharpness, 33 · 24: §1.3(c), 4 · 26: §13, 31 ("load-bearing" is on p. 31) · 33: abstract, 2 |
| s8b | 7, 10, 15: §14, 33 · 10: §1.3(d), 4 |
| s9 | 28, 33: App B, 35 · 29: App B, 34 (R2) · 31: title page, 1 · 40: §2.4, 7 |
| captions (`companion.tex`) | 60: §1.2, 3 · **73: "A8, Scope paragraph", 11; the paragraph runs pp. 11–12, see (6)** |

**(5b) Quotations in quotation marks** (23; each found verbatim in main.tex up to markup, or in the named file):

| file:line | quotation | source |
|---|---|---|
| s2:12 | "was not proved there" | main.tex l. 135 |
| s2:13 | "has not been proved" | ll. 136–137 |
| s2:17 | "the printed problems must not be read as an unqualified current open-problem claim" | l. 2503 |
| s2:60 | "selects a state but proves neither convergence nor canonicity" | l. 255 |
| s2:76 | "lives in the wrong topology" | ll. 265–266 |
| s2:76 | "there is no soft passage from moments to norms on local von Neumann algebras" | ll. 266–267 |
| s2:81 and s6:130 | "does not start" | l. 264 |
| s2:91 | "in the references reviewed here" | l. 151 |
| s4:33 | "stated uniformly as the source cutoff tends to one" | l. 687 |
| s4:65 | "deliberately limited to the audited mechanisms" | ll. 2742–2743 |
| s4:71 | "External residue" | l. 2639, subsection title |
| s4:78 | "a verdict on the printed record, not a no-go theorem" | `docs/imports.md` l. 65 |
| s4:93 | "has E(g)=inf spec K(g) as a simple eigenvalue" | l. 463 |
| s5:28 | "ψ̂_s→Ω_g in norm, ‖ψ_s‖↓c_g" | l. 1124 |
| s5:29 | "No isolation of the ground-state eigenvalue is used." | l. 1126 |
| s6:124 | "Ψ_{m₁} is super-polynomial but not exponential, and this is intrinsic to the filter method used" | ll. 236–237 |
| s8a:17 | "an additional resolvent or Combes–Thomas input not supplied here" | ll. 2512–2513 |
| s8b:7 | "no mathematical dependence in either direction" | ll. 2531–2532 |
| s8b:13 | "proves no part of (II.11)" | `part_ii/gate_II11_scoping.tex` l. 73, inside the abstract (ll. 53–75) |
| s9:6 | "an experiment in open science" | `README.md` l. 9; source has bold markup |
| s9:9 | "What this is" | `README.md` l. 7, heading |
| s9:30 | "No proof in the manuscript changed" | main.tex ll. 82–83, p. 1 |

Removed in R4: "the operator-algebraic softening of the unboundedness" (main.tex ll. 316–317).

**(5c) Transcribed boxes and displays** (verbatim up to markup; shortened only where noted):

| place | content | main.tex lines (or source) |
|---|---|---|
| §1 | Thm 12.2 box | 2295–2315, then "[…]", then 2324–2325 |
| §1 | (R5) GJ3 context sentence | PLAN 6.1; I read GJ3 pp. 210–211 myself and it matches |
| §3 | checkpoint (31) | 2166–2167 |
| §4 | A8(vi) box | 694–705 |
| §5 | Checkpoint I | (2) at 1054–1055; hypotheses shortened from 1051–1052 (s dropped); quotations 1124, 1126 |
| §5 | Checkpoint II | Thm 5.1, 1158–1167 |
| §5 | Checkpoint III | Prop 7.5, 1473–1478 |
| §5 | Checkpoint IV | Thm 7.8, 1586–1591 |
| §6 | contract box | 2126–2127 (without "In particular") and (30) at 2121–2124 |
| §6 | display (18) | 1800–1805; l. 1806 omitted per R26 |
| §6 | checkpoint (24) | 1960–1966 |
| §6 | checkpoint (23) | 1908–1915; hypotheses condensed, with H=H(g), Ω=Ω_g and (G_γ) in the preceding sentence |
| §6 | display (26) | C_{j,s} at 2019–2020; display 2023–2030 |
| §6 | checkpoint (27) | 2053–2058 |
| §7 | identity display | 2248–2250 |
| §7 | Prop 12.1 box | 2228–2236 |
| §8.2 | status table | `docs/status.md` ll. 73, 75–84 |
| §4 | A1–A7 source pinpoints | the Sources lines of A1–A7 (read at ll. 455–640) |

**PLAN wordings used verbatim, without quotation marks:**
- the frozen sentence (§1, §4);
- R16, R20, R25, R26 and R38 (§6), R21 and R23 (§8.1), R27 (§4), R35 (§3);
- the Lemma 9.1(i) credit sentence;
- the Fig. 1 legend (§3);
- the nine sentences to retain;
- the §8.2 text, with D1;
- the Cor 12.3 clause (§7).

## (6) Requests to the orchestrator

1. **Fig. 2 caption.** Change `\rec{A8, Scope paragraph}{11}` to `\recpp{A8, Scope paragraph}{11--12}`. The paragraph starts on p. 11; steps (b)–(c) and its conclusion are on p. 12 (checked with pdftotext).
2. **Abstract.**
   - (a) It counts 153 tokens with `pdftotext | wc -w`, over the 150 limit. Replacing "for $0\le\lambda/m_0^2<\varepsilon_P$," with "at weak coupling," gives 149; §1 states the region.
   - (b) The abstract writes ε_P and "(for even P)" while main.tex, the body and App B write ε_𝒫 and 𝒫 (rule 12).
   - (c) "in a spectral sense" should be "in the spectral sense" (rule 9).
3. **Fig. 1 caption.** "read from the record's proofs" appears in two consecutive sentences. The second is mandatory; the first could end at "arrows say what each proof consumes."
4. **Fig. 4 caption.** Its mandatory sentence "No automorphism or spectral flow is constructed" uses a rule-10 term outside the §6 context box. It states what is not done, so R5 should accept it. I did not touch it.
5. **Preamble, optional.** `checkpoint` is unbreakable, and that is what makes pagination jump. Adding `breakable` would make the layout more robust, at some cost in looks; your call.
6. **Fragility after R5 edits.** Rebuild and check four things:
   - the page count (≈ 115 pt of slack);
   - Fig. 4 is not on a page before §6 starts;
   - Fig. 6 is still within §7;
   - the §8.2 longtable break (8 + 2 rows now; keeping the table unbroken costs ≈ 0.15 pp).
7. **Bibliography.** Its "files cited by path" list is complete for the current text; §9 now refers to the render script only through README.md.

## (7) Noticed in the record or its files, not yet in PLAN Part 7/7.1

None of these is fixed or mentioned in the companion. All are MINOR.

- **N1 (`docs/imports.md` l. 16, A4).** It says A4 supplies "the L^p smoothing used in the moment estimates". A4's "Used in" (main.tex ll. 557–558) is §8 (the pairing bound) and App C (tail estimate); Thm 5.1, the moment, does not use A4. Documentation; cqft's N1, verified.
- **N2 (`docs/imports.md` l. 17, A5).** "a core on which the algebra acts". A5(ii) (ll. 571–573) is a common core for all K(g_s) on which K(g_s)ξ=K(g_{s₀})ξ+(s−s₀)V(g′−g)ξ. Documentation; cqft's N2, verified.
- **N3 (`part_ii/README.md`).** It contradicts itself: l. 70 "gate (II.11) closed" and ll. 238–240 "V4's ledger records (II.11) closed …" stand against l. 74 "Phase closure: NOT yet reached." Its ll. 3–4 say the 16 August addendum supersedes earlier phase-closure statements. F23 cites only l. 74. Part II; verified.
- **N4 (page of the affine-path application of Thm 1.1.7).** main.tex App B l. 2644 and `docs/status.md` l. 61 both say "on p. 595". A8(vii′)(a) gives "pp. 594–595", and so does C5 item 8 (`C5_reading_record.md` l. 106). Same family as F25.
- **N5 (scope of the uniqueness non-claim).** It differs between places: abstract ll. 117–118 "among all locally normal ground states"; §1.3(a) ll. 233–234 "every locally normal ground state"; §14 ll. 2516–2517 "every locally normal translation-invariant ground state". Not a contradiction, but a wording inconsistency (aqft's observation 2, verified).

## Not done, not verified, not run

- **Not done:**
  - The report file could not be written (harness refusal); its full text is above.
  - App B and the A1–A7 table were not cut down to their sub-budgets.
- **Not verified:**
  - The App A classes of Rem 3.3 and Rem 6.3 (left to R5).
  - Everything on the figures beyond their captions' locators: the `.dat` files, panel contents, colour classes.
- **Not run:** no git, no kb, no R5 checklist items 6–9.
- **Files changed:** `companion/sections/{s1-result,s2-open,s3-architecture,s4-import,s5-euclidean,s6-lppl,s7-identification,s8a-boundaries,s8b-part2,s9-record,appA-pointers,appB-notation}.tex` and `companion/companion.tex` (placement of Figs. 4 and 6 only). Build artefacts are in `companion/`.
- **Pre-edit copies:** kept in the session scratchpad (`scratchpad/editor/orig/`), outside the repository.
