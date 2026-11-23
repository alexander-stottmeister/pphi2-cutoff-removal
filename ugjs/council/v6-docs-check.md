# V6 documentation check: the public texts of the commit of 23/24 November 2026 (checker "docs-check")

Checker "docs-check" of the working council of 23 November 2026. I was read-only on the
repository and wrote none of the text I checked. Builds and scripts ran on copies in the
council's work directory only. Paths are relative to the repository root.

- **Object.** The working tree against HEAD 49f2d23: 38 paths, 32 modified and 6 untracked
  (`ugjs/council/v6-*.md`). At the start (23 Nov, 23:25 CET) there were 37.
  `ugjs/council/v6-repairs-check.md` appeared at 23:26. It is byte-identical (sha256 `fb3d27b7…`)
  to the council's report of that name, including its second round (§9).
- **State checked.** I hashed all 38 paths at 23:33, 23:54 and 00:00 CET (24 Nov); nothing changed.
  Key files (sha256 prefixes):

  | file | sha256 |
  |---|---|
  | `part_i/main.tex` | `254f9f0d…` |
  | `part_i/main.pdf` | `b2bd43f3…` |
  | `part_i/README.md` | `0c061811…` |
  | `README.md` | `e90f953b…` |
  | `docs/status.md` | `9231b9cc…` |
  | `docs/imports.md` | `3724bbbd…` |
  | `CITATION.cff` | `149f53e5…` |
  | `strategy.md` | `beb2cbba…` |
  | `companion/companion.pdf` | `a560cc27…` |

  HEAD is still 49f2d23, and no tag exists.
- **Locators.** Line numbers are those of the working tree. For `part_i/main.tex`, label, number
  and page come from the new `main.aux`. The mathematics of `main.tex` is outside my remit.

## 1. Outcome

The builds, the generator and the guard reproduce, and nearly every documentary sentence checks out. One public sentence is false about the record's status: `docs/imports.md` l. 20 still says that the sources of A1 work in Fock space, and it lists the declared readings of 11 November, omitting the two that A1's Scope has declared since 23 November (MAJOR). Twenty-six MINOR points remain. The most visible are:
- a page count in `docs/status.md` that still describes the 125-page record as current;
- an import-graph figure one edge behind the manuscript;
- false clauses in the gate record's G4 and G5;
- public and companion sentences that the corrections of 23 November made inaccurate.

## 2. Claims, with status word and locator

Status words for documentary claims: verified, refuted, not verified. No mathematical claim is made here.

| # | claim (where made) | status | locator / how checked |
|---|---|---|---|
| 1 | Three passes with epoch 1795392000 give 127 pp, 0 errors, 0 Overfull, 0 undefined, empty `??\|TODO\|Hmm\|wait,` grep, sha256 `b2bd43f3…7271` (`part_i/README.md` l. 611; README "Building") | verified | scratch build, byte-identical to `part_i/main.pdf`; `main.aux`, `main.toc` identical to the repository's |
| 2 | 1795392000 is 23 Nov 2026 00:00 UTC; `\date{23 November 2026}` | verified | `date -u -r`; `main.tex` l. 82 |
| 3 | 238 labels keep their numbers, none added or removed; 199 change page, 113 by one, 86 by two (`part_i/README.md` l. 612) | verified | script over both `main.aux`; FROZEN's `main.aux` and `main.pdf` reproduced by my own build (epoch 1794355200, 125 pp) |
| 4 | Thirteen labelled statement environments differ, the list as given; only an attribution sentence changed in Theorems 12.2 and D.4; no item (1)–(5) of 12.2 changed (l. 605) | verified | script over 127 labelled + 2 unlabelled environments; word diffs |
| 5 | The abstract now ends on p. 3 (l. 612) | verified | `pdftotext`: "Abstract" p. 2; "We do not claim" and "Contents" p. 3 |
| 6 | 8858 lines, 127 pages (l. 600) | verified | `wc -l`; `pdfinfo` |
| 7 | `docs/results.*` regenerated: 72 numbered statements, 34 reach A8, as before (l. 617); six figure pages changed in their page numbers (l. 617) | verified | `extract.py --check`: "up to date"; `results.json` 72/34 at HEAD and now; word diff of `docs/interactive/*.html`: page spans only |
| 8 | Before the last edits the generator read Lemmas 9.1 and 10.1 as reaching A8 and lost the proof of Corollary 12.3 (l. 604) | verified | `extract()` run in scratch on the checked text (sha256 `3da06407…`): 35 reach A8, 9.1 and 10.1 flagged, `cor:canonical` without proof; on the final text: 34, proof present |
| 9 | The README's import graph "is generated from the manuscript's own reference graph" (README ll. 170–171, 182–183) | refuted for the committed SVGs | D2 |
| 10 | e4389a8 (private repository, 23 Nov 2026) adds `simon-semibounded-163` (p. 141) and `simon-hg-168` (p. 146), rendered at 150 dpi; with `simon-transfer-180` they are in A5's Dossier line and the map (ll. 614, 637) | verified | `gjp log`/`show --stat`: 2026-11-23 23:07:41 +0100, the two files; `sips`: 826×1234 px, 150 dpi; both images viewed; `main.tex` ll. 1036–1037 |
| 11 | The dossier index shows 54 of the 97 images and none of the pages added since 31 October; those are in the Dossier lines and the map (l. 614; README ll. 300–305; `docs/provenance.md` l. 22) | verified | script: 97 PNG, 54 named in `audit_2026/citation_screenshot_dossier.tex` (last changed 22 Sep 2026); the 29 images added on or after 31 Oct (private log) are absent from it and present in both lists |
| 12 | Simon pp. 140, 159–161, GJ3 p. 205 and the GJ71/Rosen70 pages read from the PDFs have no page image (l. 614) | verified, except as in D4 | evidence listing |
| 13 | GJ2 p. 400 has no page image; GJ3 p. 210 has a part "beyond `gjiii-08`" (l. 614) | refuted | D4 |
| 14 | The re-checker's F2 and F4 were applied in the last edits, F1 and F3 are open; its second round covers the four edits (ll. 604, 608) | verified | `ugjs/council/v6-repairs-check.md` §9 |
| 15 | The re-check has "four MINOR findings and nine observations" (l. 608) | refuted after its second round (ten) | D6 |
| 16 | The four last edits' pages "were not looked at again" (l. 615) | refuted | D5 |
| 17 | Appendix E audit: E.1–E.7 hold; twenty images; the three passages hold; F1–F3 as summarised; not compared: A1(a) p. 10, A1(d) pp. 137–138, A6's GJExp p. 42 (l. 597) | verified | `ugjs/council/v6-appendix-e-audit.md` §§1, 3, 4(5), 5 |
| 18 | Chain audit: the listed passages hold; eleven findings F-A to F-K; F-A's double severity and the GJ3 p. 210 quotation (l. 598) | verified | `ugjs/council/v6-chain-audit.md`; `gjiii-08.png` viewed: "For concreteness, we take g(x) to be a nonnegative C_0^∞ function equal to one on the interval [−3, 3]"; "h(·) ≥ 0 is C^∞" |
| 19 | Status council of 22 Nov: three Opus agents; no CRITICAL/MAJOR; ten MINOR; no third agent on Appendix E; no full audit since August of Theorem 13.2 Steps 2–4 and §14 (l. 594) | verified | 22-Nov synthesis and orchestrator notes; KB node `glimm_jaffe:problem/loose-ends-after-checkpoint-2` (file read, no `kb` command) |
| 20 | The ten MINOR findings were "about wording" (README ll. 65–66; status ll. 52–53; `strategy.md` l. 2604) | refuted | D8 |
| 21 | Status sentences ("Theorem 12.2 is proved from printed statements only, …") unchanged and word for word the notice of 7 November | verified | script: identical to `main.tex` ll. 122–125 with `\ref` resolved; same counts at HEAD and now in README, `docs/status.md`, `docs/imports.md` |
| 22 | The new paragraph is identical in README.md (ll. 64–106) and `docs/status.md` (ll. 51–93) | verified | `cmp` |
| 23 | `CITATION.cff` parses as YAML; version "1.2.1", date-released "2026-11-24" | verified | Ruby 4.0.6 `YAML.safe_load` (PyYAML not installed) |
| 24 | [MMST] is Comm. Math. Phys. 387 (2021) 299–360 (l. 602) | verified on the arXiv page; Crossref not verified | the editor's saved copy of arxiv.org/abs/2010.11121 (fetched 23 Nov 13:36): title, four authors, journal-ref "Commun. Math. Phys. 387, 299-360 (2021)", DOI 10.1007/s00220-021-04152-5 |
| 25 | The wrong range remains in the Part II notes, `m6/` and the archived audit copies (l. 627) | verified | `git grep 1299`: four files in `part_ii/`, `m6/main.tex`, three in `fresh_audit_2026_08_16/lamport/` |
| 26 | Tags v1.1.0 and v1.2.0 not yet created (l. 627) | verified now | `git tag -l` empty |
| 27 | Companion: 20 pp, 0/0/0, built with epoch 1794009600; pages 2–19 those of 7 November; only the MMST line differs on p. 20; `bib.tex` regenerated by `make_bib.py` (l. 623; README "Building"; council README) | verified | scratch build byte-identical (`a560cc27…`); per-page `pdftotext` and 72-dpi `pdftoppm` against HEAD's PDF; `make_bib.py` in a scratch tree gives the repository's `bib.tex` |
| 28 | Notice: 161 words, nine lines; box 236 words (council README l. 116; PLAN Part 12) | verified | `pdftotext -f 1 -l 1`: 75 + 161 words; nine notice lines |
| 29 | Cited pages "up to seven too early"; statement numbers unchanged | verified | `labels.md` against the new `main.aux`: 230/230 labels; numbers equal up to brace formatting; shifts {0:1, 1:5, 2:9, 3:21, 4:81, 5:3, 6:55, 7:55}, none negative |
| 30 | The companion states Corollary 12.3 without restriction in §§1, 2, 7 and Fig. 1; only the notice mentions Appendix E | verified | `s1-result.tex` ll. 82–84, `s2-open.tex` l. 65, `s7-identification.tex` ll. 59–60, `fig-spine.tex` l. 109; grep |
| 31 | C5's checklist covers the GJS pages only (README l. 145; status l. 148) | verified | `part_i/C5_reading_record.md` title and "Source" |
| 32 | A1 and A3 are shaded because their Scope paragraphs cite A8 Scope (d) (README ll. 189–191) | verified | `results.json`: both list `A:gjs` |
| 33 | Eight interactive figures; the README's pictures carry no links | verified | `docs/interactive/` (8 pages + index); no `<a` in README |
| 34 | Nine machine-path lines in five archived files made relative (l. 624; `ugjs/council/README.md`) | verified | masked word diff: only the paths changed; none remain (§4, "Machine paths and e-mail") |
| 35 | The archived reports are "as the agents wrote them, except … `<scratch>`" (`ugjs/council/README.md` l. 139) | refuted | D24 |
| 36 | The repository's About text was corrected on 23 November (l. 620; `strategy.md` l. 2610) | not verified | no `gh` |
| 37 | "All agents were Opus"; "the orchestrator re-read each finding at its source" (l. 594; council README) | not verified | — |
| 38 | "A third edition waits for the author's decision on Phase C" (notice; PLAN Part 12; council README) | not verified | no file records the author's words |

## 3. Findings

### 3.1 MAJOR

**D1 (MAJOR). `docs/imports.md` l. 20 states the sources and the declared readings of A1 as they were before 23 November.**
- *Locator.* `docs/imports.md` l. 20, the paragraph after the table. The record: `A:cutoff`, A1, p. 11, Scope sentences `main.tex` ll. 822–837 (PDF p. 13); `A:stability`, A3, p. 14, Scope.
- *Text.* "The sources of A1 and A6 work in Fock space; since 11 November 2026 the dictionary between their Fock space and Q-space is written out (Appendix E, Lemma E.7: a unitary that carries their vacuum, time-zero fields, free Hamiltonian and translation unitaries to those of the record). What remains declared readings of the sources (Scope paragraphs of A1 and A6): that this unitary carries their interaction to the V(g) of the record; that the time-zero fields of GJ2 p. 397 and the fields of the 1968 paper are those of GJ2 (1.2.1)–(1.2.11), with real test functions; and that for negative times the region O_t of (3.4) is O expanded by |t|."
- *Why it fails.* Since 23 November, A1's Scope says three things that contradict this paragraph.
  - It says "Of the sources of the cutoff construction, \cite{GJS} works in $Q$-space". It also says "Literally $\mu^{-1}=2C$; reading $\mu^{-1}$ as the inner product $2\ip f{Cg}$ of $\HH_C$, which makes $d\phi$ our $d\phi_0$ …, is a reading of the kind recorded in Assumption~\ref{A:gjs}, Scope~(d), not proved here" (ll. 822–829).
  - It claims the dictionary of Lemma E.7 for "the Fock space of \cite{GJ2}" only.
  - It adds "that \cite{GJ71,Rosen70} use the same objects is a reading of those sources" (l. 834).

  So the paragraph's first clause is false for GJS, A1's first source. Its second clause claims Lemma E.7 for more sources than the record does. Its list of readings omits both readings declared on 23 November, and also the A3 Scope reading, an omission since 7 November that the 22-November register noted.

  This page says of itself that it records each import's status. The pending status word is "proved, conditional on the declared readings" of A1, A3, A6 and A8 Scope (d) (`part_i/README.md` l. 627), so this list is part of the record's status. The file changed today only at l. 32.
- *Repair.* Replace everything from "The sources of A1 and A6" to "expanded by |t|." with:
  > Of the sources of A1, GJS works in Q-space: its "Fock space" is L₂(𝒮′(R¹), dφ), with covariance printed as μ⁻¹, literally 2C (p. 588); GJ2, GJ71 and Rosen70 work in Fock space. Since 11 November 2026 the dictionary between the Fock space of GJ2 and Q-space is written out (Appendix E, Lemma E.7: a unitary that carries GJ2's vacuum, time-zero fields, free Hamiltonian and translation unitaries to those of the record). What remains declared readings of the sources (Scope paragraphs of A1, A3 and A6): that GJS's dφ is the record's dφ₀, μ⁻¹ being read as the inner product 2⟨f, Cg⟩, and that GJ71 and Rosen70 use the objects of GJ2 (both since 23 November 2026); that the unitary carries the Fock-space sources' interaction to the V(g) of the record; that Simon's ∫g:P(φ): of Theorem V.7 is the V(h) of GJS (1.8), p. 589 (A3); that the time-zero fields of GJ2 p. 397 and the fields of the 1968 paper are those of GJ2 (1.2.1)–(1.2.11), with real test functions; and that for negative times the region O_t of (3.4) is O expanded by |t|.
- *Severity.* MAJOR: a public sentence that is false about the record's status.

### 3.2 MINOR

**D2. The import-graph figure is one edge behind the manuscript.**
- *Locator.* `docs/figures/imports-dag.svg` and `imports-dag-dark.svg`, unchanged since d2b106c (11 Nov). README.md ll. 182–183: "Generated from `part_i/main.tex`: the nodes are the spine of Part I, the edges are its own `\ref` graph".
- *Why.* A5's new Scope sentence refers to A1 ("$\phi_F$ as in the Scope of~\ref{A:cutoff}"), so the regenerated inventory has the new spine edge A:domain → A:cutoff.
  - I ran the figure's own builder (`fig_dag` of `docs/figures/make_figures.py`) in scratch on the new `docs/results.json`. Both themes differ from the committed SVGs by exactly this edge: one `<path>` in the assumptions row, from x = 58 to x = 386.
  - On HEAD's `results.json` the builder reproduces the committed SVGs byte for byte.
  - The shading is unchanged, and `extract.py --check` does not cover figures.
- *Repair.* Regenerate with `python3 docs/figures/make_figures.py` and commit the two `imports-dag` files, checking that the other outputs are unchanged. Alternatively, add to README l. 183: "(drawn from the record of 11 November 2026; since 23 November Assumption A5 also refers to A1)".

**D3. `docs/status.md` l. 107 still describes the 125-page record as current.**
- *Text.* "The record of that date has 110 pages; since 11 November 2026 it has 125."
- *Why.* The record has 127 pages, as l. 105 and the new paragraph of the same page say.
- *Repair.* "The record of that date has 110 pages; from 11 November 2026 it had 125, and since 23 November 2026 it has 127."

**D4. Gate record G4: two clauses are false and one page is missing.**
- *Locator.* `part_i/README.md` l. 614.
- *Text.* "Simon pp. 140 and 159–161, GJ3 pp. 205 and 210 beyond `gjiii-08`, GJ2 p. 400 and the pages of GJ71 and Rosen70 that the editor and the re-checker read from the source PDFs have no page image."
- *Why.*
  - `audit_2026/evidence/gj2-local-algebra-40.png` is GJ2 p. 400. I viewed it: page header "400" and the display σ_a(A) = U(−α)e^{itH(g)}Ae^{−itH(g)}U(+α). The re-checker cites it in its C4.
  - `gjiii-08.png` is the whole of GJ3 p. 210 (viewed), so no part of p. 210 lies "beyond" it.
  - Simon p. 145 (PDF page 167), which pass 1 rendered and read (wording report, claim 11), has no image either and is not named.
  - Of the GJ71 pages read, only p. 255 lacks an image.
- *Repair.* "Simon pp. 140, 145 and 159–161, GJ3 p. 205, GJ71 p. 255 and Rosen70 p. 158 (with Rosen70's §2 and Theorem 2.1, read as text), which the editor and the re-checker read from the source PDFs, have no page image; GJ3 p. 210 is `gjiii-08`, and GJ2 p. 400, which the re-checker used for its F3, is `gj2-local-algebra-40`."
- The error understates the dossier and does not affect the status.

**D5. Gate record G5 understates what was looked at.**
- *Locator.* `part_i/README.md` l. 615; also `docs/status.md` l. 138.
- *Text.* "the four last edits moved no label and their pages were not looked at again."
- *Why.* The re-check's §9 says: "I read the rendered text of the four loci with pdftotext (pp. 36, 43, 45), and rendered p. 43 at 80 dpi and looked at it."
- *Repair.* "the four last edits moved no label (`main.aux` byte-identical); of their pages, the re-checker's second round rendered p. 43 at 80 dpi and looked at it and read pp. 36 and 45 as text."

**D6. Gate record, Re-check paragraph: a count and a misquotation.**
- *Locator.* `part_i/README.md` l. 608.
- *Text.* "four MINOR findings and nine observations"; "the record does not state that V_* equals its explicit bound, so "explicit in S₂ and the GJS constants" leaves out V_* and the filter, which Appendix A names".
- *Why.*
  - The second round adds O10 (§9), so the report now has ten observations.
  - The quoted words are not in the record. The notice prints "the rate and $M$ are explicit in $S_2$ and the unevaluated GJS constants" (`main.tex` ll. 173–174), and the abstract prints "explicit in the imported theorem's unevaluated constants and one stability constant" (ll. 195–196).
  - F1 has two parts: the summaries omit V_* and the filter, and calling V_* explicit rests on an equality the record does not state. "So" turns the first part into a consequence of the second.
- *Repair.* "four MINOR findings and nine observations (a tenth, O10, in its second round)". For the second sentence: "two are open: the notice's "explicit in S₂ and the unevaluated GJS constants" and the abstract's description leave out V_* and the filter, which Appendix A names, and the record does not state that V_* equals its explicit bound; and the proof of Corollary 12.3 identifies GJ3's translation automorphisms with τ without a source."

**D7. The new public paragraph overstates the Appendix E audit's comparison of quotations.**
- *Locator.* README.md ll. 70–71; `docs/status.md` ll. 57–58.
- *Text.* "Appendix E (E.1–E.7, each quotation it uses compared with its page image)".
- *Why.* The audit's §5, "Not verified", lists A1(a) p. 10, A1(d) pp. 137–138 and A6's GJExp p. 42. It adds: "Appendix E's own steps use none of these, except that E.5 inherits A1(d)'s existence statement for the Wick powers." The gate record (l. 597) keeps the exceptions; the public paragraph drops them.
- *Repair.* "Appendix E (E.1–E.7; every quotation it uses compared with its page image, except A1(d)'s, Simon pp. 137–138, which E.5 inherits)".

**D8. "Ten minor ones about wording."**
- *Locator.* README.md ll. 65–66; `docs/status.md` ll. 52–53; `strategy.md` l. 2604 ("ten MINOR ones about wording").
- *Why.* The register of 22 November describes the ten as "wording, sourcing, notation, machine paths". Among them are item (1), a false public sentence; item (4), machine paths; item (8), the unquoted source of A5(ii); and item (9), the missing dictionary between GJS's covariance and C, whose repair today added a declared reading.
- *Repair.* "ten minor ones (wording, sourcing, notation, machine paths)", in all three places.

**D9. The scope of the second audit.**
- *Locator.* README.md ll. 67–69; `docs/status.md` ll. 54–56 and l. 105 ("an audit of the single-checker passages").
- *Text.* "…and, for the first time since August in full, the passages on the path to Theorems 12.2 and 13.2 that only one agent had checked since their last change".
- *Why.*
  - The chain audit (§3.3) found that some of its passages had been examined by none of the four earlier reports: "Prop. 12.1 as a whole, Cor. 12.3's scope, Thm 13.2 Steps 2-4 and (B2), Remark 13.3's sources, and §14".
  - Others had been checked in V4 and V5: the Locality paragraph, Proposition 2.7, Lemma 2.8, Lemma 9.3 Step 2 and Theorem 13.2 Step 1.
  - "No full audit since August" was recorded only for Theorem 13.2 Steps 2–4 and §14 (l. 594).
  - `strategy.md` l. 2608 already says "one agent or none".
- *Repair.* "…and the passages on the path to Theorems 12.2 and 13.2 that one agent or none had checked since their last change, among them Theorem 13.2, Steps 2–4, and §14, which had had no full audit since August". For l. 105: "an audit of the passages on the path to Theorems 12.2 and 13.2 that one agent or none had checked since their last change".

**D10. "Theorem 12.2 is unchanged" and "changed in wording".**
- *Locator.*
  - README.md ll. 76–77 and 103–105;
  - `docs/status.md` ll. 63–64, 90–92, l. 105 ("Theorem 12.2 is unchanged.") and l. 130 (row GA, "thirteen statement environments changed in wording, among them the statement of Corollary 12.3 (restricted)").
- *Why.*
  - The same paragraph names "the attribution sentences inside Theorems 12.2 and D.4" among the changed environments. The record says "unchanged in substance" (`main.tex` ll. 167–168).
  - A restricted statement has changed in more than wording.
  - "Remark 13.3 and N.46" lacks the plural.
- *Repair.*
  - "and Theorem 12.2 is unchanged in substance (only an attribution sentence inside it changed)";
  - "thirteen statement environments changed their text (…, Remarks 13.3 and N.46, …)";
  - l. 105: "Theorem 12.2 is unchanged in substance.";
  - row GA: "thirteen statement environments changed their text, among them the statement of Corollary 12.3 (restricted)".

**D11. "Identifying the two is a declared reading."**
- *Locator.* README.md ll. 91–92; `docs/status.md` ll. 78–79; `part_i/README.md` l. 601.
- *Text.* "(GJS p. 588 works on Q-space, and its printed covariance μ⁻¹ is twice the record's C; identifying the two is a declared reading)".
- *Why.* "The two" reads as μ⁻¹ and C. Identifying them would contradict the factor 2 that the same sentence states. The declared reading is "reading $\mu^{-1}$ as the inner product $2\ip f{Cg}$ …, which makes $d\phi$ our $d\phi_0$" (`main.tex` ll. 825–829).
- *Repair.* "(GJS p. 588 works on Q-space; its printed covariance μ⁻¹ is literally twice the record's C, and reading μ⁻¹ as the inner product 2⟨f, Cg⟩, so that GJS's measure is the record's dφ₀, is a declared reading)". Use the same wording in `part_i/README.md` l. 601.

**D12. "Which `part_ii/README.md` contradicts."**
- *Locator.* README.md ll. 100–101; `docs/status.md` ll. 87–88.
- *Why.* `part_ii/README.md` agrees with §14 at l. 148 ("remains open") and l. 206 ("open exactly at the coarse Weyl characteristic-functional limit"). It contradicts §14 at ll. 238–239 ("V4's ledger records (II.11) closed … Part II's fixed-coarse program is complete"). The chain audit's F-H is that Part II's record contradicts itself, as the gate record says (l. 606).
- *Repair.* "…which `part_ii/README.md` both repeats (ll. 148, 206) and contradicts (ll. 238–239: gate (II.11) closed); this is for the author to settle."

**D13. The public descriptions of the rate's constants repeat the summary that the re-check's open F1 concerns.**
- *Locator.* README.md ll. 88–90 and 115–118; `docs/status.md` ll. 75–77; `docs/index.md` l. 37; `CITATION.cff` ll. 18–20.
- *Text* (README ll. 115–118). "given by an explicit formula in constants that are not evaluated: those of the imported GJS Theorem 1.1.7, which the source prints only as existing or as thresholds, and the stability constant S₂ (Definition N.14), finite by Theorem C.5".
- *Why.* Appendix A (`app:constants`, A, p. 46; `main.tex` l. 3451) names two more inputs: "in $V_*$ (explicitly bounded, Lemma~\ref{aux:notation-wick}) and, for $\Psi_\gamma$, in the filter of Lemma~\ref{lem:filter}". The record does not state V_* = V̄_* (re-check F1, open by decision). The public sentences are true by the re-check's C11 but say less than the record's own Appendix A.
- *Repair.* Either close F1 in the record and add "and the filter of Lemma 9.1", or append to each sentence "; Appendix A also names V_*, which the record bounds explicitly, and the filter of Lemma 9.1". For `CITATION.cff`: "…, those of the imported clustering theorem, one finite stability constant, an explicitly bounded constant and the chosen filter".

**D14. `docs/status.md` l. 103 and l. 155 keep the attribution the record corrected.**
- *Text.*
  - l. 103, the dated entry of 7 November: "M now contains the finite, unevaluated constant of Theorem C.5, so the rate of Theorem 12.2(1) is explicit up to that constant."
  - l. 155: "The constant of Theorem C.5 is finite and not evaluated."
- *Why.* Since 23 November the record reads that phrase as S₂ of Definition N.14 (notice, `main.tex` ll. 171–174). It also says the rate is a formula in the unevaluated GJS constants (Appendix A). Line 155 is in the present tense. Line 103 is dated but has no pointer to the correction, unlike the record's own notice of 7 November. Pass 1 flagged l. 103 (wording report, W3).
- *Repair.*
  - l. 155: "S₂ (Definition N.14) is finite by Theorem C.5 and not evaluated, and neither are the constants of GJS Theorem 1.1.7 (Appendix A)."
  - l. 103: append "(read since 23 November 2026: the constant is S₂ of Definition N.14, finite by Theorem C.5, and the rate is also a formula in the unevaluated constants of GJS Theorem 1.1.7)".

**D15. The free-field paragraphs identify more objects with the sources than the record now does.** This is the analogue of the Appendix E audit's F3.
- *Locator.* README.md ll. 45–46; `docs/status.md` ll. 31–32; `docs/provenance.md` ll. 73–75.
- *Text.* "and identifies the objects with those of the Fock-space sources"; "the objects identified with those of the Fock-space sources".
- *Why.* "The objects" include the dilation unitary, which has no counterpart in the sources; Appendix B now says so (`main.tex` ll. 3578–3580). Lemma E.7 identifies the objects with those of GJ2; for GJ71 and Rosen70 that is now a declared reading (l. 834).
- *Repair.* README and status: "and, except for the dilation unitary, which has no counterpart in the sources, identifies the objects with those of GJ2 (for GJ71 and Rosen70 a declared reading since 23 November 2026)". Provenance: "the objects, except the dilation unitary, identified with those of GJ2".

**D16. A sentence of 11 November now reads as current.**
- *Locator.* README.md ll. 60–62; `docs/status.md` ll. 47–49.
- *Text.* "That record had 125 pages. No numbered statement changed its number, and no statement of a theorem, proposition, lemma or corollary changed; Assumptions A1, A6 and A7 and Remark 3.3 did."
- *Why.* It stands directly above the paragraph that reports a changed corollary, and "That record" anchors only the page count.
- *Repair.* "That record had 125 pages; in that repair no numbered statement changed its number, and no statement of a theorem, proposition, lemma or corollary changed (Assumptions A1, A6 and A7 and Remark 3.3 did)."

**D17. Three new pinpoint citations have no page image, which two public sentences deny.**
- *Locator.*
  - The citations: `main.tex` l. 830 (`\cite[p.~255]{GJ71}`, `\cite[p.~158]{Rosen70}`, A1 Scope, PDF p. 13) and l. 3217 (`\cite[(1.10), p.~205]{GJ3}`, after the proof of `cor:canonical`, PDF p. 43).
  - The sentences: `docs/imports.md` l. 41 ("each citation is matched to a page image in the dossiers") and `docs/provenance.md` l. 87 ("Every load-bearing citation is matched to an image of the page it is taken from").
- *Why.* `audit_2026/evidence/` holds no image of these three pages, as G4 itself says, and A1's Dossier line names none.
- *Repair.* Render GJ3 PDF p. 3, GJ71 PDF p. 3 and Rosen70 PDF p. 2 into the private evidence folder and name them in A1's Dossier line and the map. Alternatively, add to both sentences: "except GJ3 p. 205, GJ71 p. 255 and Rosen70 p. 158, cited since 23 November 2026 (`part_i/README.md`, gate GA, G4)".

**D18. The corrections history in `docs/provenance.md` has no entry for 23 November.**
- *Locator.* `docs/provenance.md` ll. 31–79.
- *Why.* The page states "The point of publishing this is that the errors are part of the record". The record's Appendix B carries the entry (`main.tex` l. 3593), including "CRITICAL for that statement as written".
- *Repair.* After the free-field entry, add:
  > **Audit of 23 Nov 2026** (published 24 Nov): the statement of Corollary 12.3 covered every cutoff of GJ3 §2, while its proof needs 0 ≤ g ≤ 1 (CRITICAL for that statement as written; no other result uses it); restricted to cutoffs 0 ≤ g ≤ 1 and P(ξ) = ξ⁴. Also: Proposition E.5(T) states the strong continuity of translations; Hypothesis 13.1 fixes the sense of "ground state"; the Scope paragraphs of A1 and A8, the source of A5(ii), the description of the rate's constants and smaller wording — see [status](status.md) and `part_i/README.md`, "Audit and corrections (2026-11-23)".

**D19 (optional). The site's front page does not mention the restriction.**
- *Locator.* `docs/index.md` ll. 11–24 ("Read this first", latest dated item 21 November).
- *Repair.* Add the line: "> **24 November 2026.** An audit of 23 November restricted Corollary 12.3 to cutoffs 0 ≤ g ≤ 1 and P(ξ) = ξ⁴; Theorem 12.2 is unchanged in substance. See [status](status.md)."

**D20. `strategy.md` l. 2608: the counts do not fit together.**
- *Text.* "fourteen MINOR points besides. All but three were applied (not applied: the Part II sentence of §14, and two points of the re-check)".
- *Why.* Besides F-A, the two audits have thirteen MINOR findings: F1–F3 and F-B to F-K. That makes fourteen only if the observation O4 is counted. Of those, only F-H was not applied. The two open points are the re-check's F1 and F3, which are not among the fourteen.
- *Repair.* "thirteen MINOR findings besides (F1 to F3 of the first audit, F-B to F-K of the second) and one observation (O4), all applied except the Part II sentence of §14 (F-H); the re-check raised four MINOR findings, two applied and two open."

**D21. `strategy.md` l. 2612: status wording and the Route T note.**
- *Text.* "Corollary 12.3 holds for cutoffs 0 ≤ g ≤ 1 and φ⁴." and "(the Route T note, written and audited on 23 November, is recorded separately)".
- *Why.*
  - "Holds" is not a status word. The corollary is proved for those cutoffs, conditional on the A1-Scope reading applied to GJ3 (`main.tex` ll. 3216–3219). It also uses an identification of GJ3's σ_α that the record does not source (re-check F3, open).
  - The note was revised after its two audits (council report "Route T note: revision after the two audits"). No file in this commit says where it is "recorded".
- *Repair.* "Corollary 12.3 is proved for cutoffs 0 ≤ g ≤ 1 and φ⁴, conditional on the A1-Scope reading applied to GJ3 (named after the corollary)." For the note: "(the Route T note was written and audited on 23 November and revised after the audits; it is not part of this commit)".

**D22. Attribution of the status-word ruling.**
- *Locator.* `part_i/README.md` l. 627 ("the status council's ruling that Theorem 12.2 is "proved, conditional on the declared readings" of A1, A3, A6 and A8 Scope (d)"); `strategy.md` l. 2604 ("The council's ruling").
- *Why.* The three members gave different lists. The A1/A3/A6/A8 (d) list is the orchestrating agent's ruling: the KB register's summary says "all three members attach declared readings, with different lists; the orchestrating agent's ruling: …", and the 22-November notes correct the same point after the KB review.
- *Repair.* "the ruling of the status council's orchestrating agent (the three members attached declared readings with different lists) that Theorem 12.2 is …".

**D23. G3: "M = 0 and Ψ = 0 at λ = 0".**
- *Locator.* `part_i/README.md` l. 613.
- *Why.* By (eq:Psidef) (`lem:rate`, 10.5, p. 40; `main.tex` ll. 2918–2929), Ψ_γ(d) = max{2, ·} for 0 ≤ d < d₀. At λ = 0 it vanishes only for d ≥ d₀, as both the editor (claim 7) and the re-checker (C10) wrote.
- *Repair.* "M = 0, and Ψ_{m₁}(d) = 0 for d ≥ d₀, at λ = 0".

**D24. `ugjs/council/README.md` l. 139 misdescribes the archiving.**
- *Text.* "The reports are archived as the agents wrote them, except that the paths of the session's scratch directory are written `<scratch>`."
- *Why.*
  - Five of the six files are byte-identical to the agents' files (`cmp`).
  - The sixth, `v6-public-texts-report.md`, differs in one line (l. 238). There a `git grep` command spelling out two machine-path prefixes was replaced by words; no `<scratch>` substitution was made, and that agent wrote `<scratch>` itself.
  - The reports also name files that are not archived, or refer to themselves under other names: `wording-main.md`, `repairs-main.md`, `public-texts.md`, the diffs, `PASS2.md`, and the brief of 23 November. `BRIEF.md` in this folder is the brief of 28 October.
- *Repair.*
  > The reports are archived as the agents wrote them, except one line of `v6-public-texts-report.md` (§4, machine-path grep), where a command that spelled out two machine-path prefixes now names them in words. Inside the reports, `wording-main.md`, `repairs-main.md` and `public-texts.md` are the files archived here as `v6-wording-main-report.md`, `v6-repairs-main-report.md` and `v6-public-texts-report.md`; the diffs they name, `PASS2.md` and the council's brief of 23 November are not archived (`BRIEF.md` in this folder is the brief of 28 October).

**D25. `companion/council/README.md` ll. 132–133.**
- *Text.* "Nothing else in the companion changed."
- *Why.* The next sentences describe the typographic changes on p. 1.
- *Repair.* "Nothing else in the companion's text changed."

**D26. The companion's body repeats three sentences that the record of 23 November corrected, and nothing says so.**
- *Locator.*
  - `companion/sections/s8a-boundaries.tex` ll. 16–17 ("$\Psi_{m_1}$ is super-polynomial but not exponential") and ll. 26–27 ("whose four items (B1)--(B4) are all load-bearing"), §8.1, PDF p. 16;
  - `s8b-part2.tex` ll. 8–9 ("§14 of the record states that the two problems have "no mathematical dependence in either direction""), p. 16;
  - `s6-lppl.tex` ll. 128–129 ("The record states that "$\Psi_{m_1}$ is super-polynomial but not exponential, and this is intrinsic to the filter method used""), p. 14.
- *Why.*
  - The record now says that (B2) "is not used" (§13), that Part II re-uses one argument of Appendix C (§14), and "for $\lambda>0$, not exponential" (§1.3(b), §14).
  - The two "the record states" sentences no longer quote the current record, and "(B1)–(B4) are all load-bearing" is the chain audit's F-C.
  - The notice covers Corollary 12.3 only, and README l. 251 and the council README mention only that.
- *Repair.* The notice is at its line budget. Add to the council README's paragraph of 23 November and to README's companion row:
  > The companion also repeats three sentences of the record of 7 November that the record of 23 November corrects: "(B1)–(B4) are all load-bearing" (§8.1; (B2) is not used), "no mathematical dependence in either direction" (§8.2; Part II re-uses an argument of Appendix C) and "not exponential" (§§6, 8.1; for λ > 0 only).

**D27. Small points.**
- (a) `part_i/README.md` l. 4: "for the audits of 23 November 2026, which restricted Corollary 12.3". The audits found the problem; the corrections restricted the corollary. Repair: "for the audits and corrections of 23 November 2026 (Corollary 12.3 restricted)".
- (b) `docs/notation.md` l. 38: "(Appendix A, p. 45 of the build of 11 November 2026)". This is dated and true, but the linked PDF has Appendix A on p. 46. Repair: "(Appendix A, p. 46 of the build of 23 November 2026)".
- (c) `ugjs/council/v6-public-texts-report.md` ll. 73–74: the quoted links "[`part_i/C5_reading_record.md`](…)" render on GitHub as links to "…", which do not resolve. The report is archived as written, so this is acceptable as is.
- (d) `companion/PLAN.md` l. 868: the heading "## Part 12 — …" differs from "## 11. Revised edition …". Repair: "## 12. Dated notice of 23 November 2026 (not a revision)".
- (e) `docs/status.md` ll. 56, 84, 88, 92: the new paragraph gives report paths as code spans, while the rest of the page links to GitHub. The site renders `docs/` alone, so these paths are not links there. Style only.
- (f) `CITATION.cff` l. 23 (pre-existing, in the edited abstract): "translation and Z_2 invariant". The record, README l. 118 and `docs/index.md` l. 38 say ℤ₂-invariant for even P. Repair: "translation invariant, Z_2 invariant for even P".

### 3.3 Dates (the push on 24 November 2026)

**Sentences that say "published … 24 November"** become false if the push slips:
- README.md l. 64;
- `docs/status.md` l. 51, l. 105 and l. 130 (row GA, "published 24 Nov 2026");
- `strategy.md` l. 2612;
- `CITATION.cff` l. 35 (date-released "2026-11-24");
- D19's line, if adopted.

**Sentences false if the push happens on 24 November: none found.**
- No added sentence says "published on 23 November", "today" or the like.
- The other dates (22–23 November) date events. Every one of the 38 paths was last modified on 23 November, and private commit e4389a8 is dated 2026-11-23 23:07:41 +0100.
- The re-check (§5) reached the same result for the record's own dated sentences.

**Sentences that a later action makes false, whatever the date:**
- `part_i/README.md` l. 627, "Tags v1.1.0 (f213cc8) and v1.2.0 (49f2d23) are not yet created", and `strategy.md` l. 2612, "Open: … tags": false once the commissioned tags exist. None exists now.
- `companion/council/README.md` ll. 139–140, "no agent that did not write it has checked it yet": false once this check, which covers the notice (§2 rows 27–30), is accepted.
- `main.tex` ll. 175–176, "The repairs were re-checked by an agent that wrote none of them": true for sha256 `254f9f0d…`. Any further edit to `main.tex` needs a re-check, or the sentence must be confined (re-check §9, final line).
- "The record is dated 23 November 2026" (README l. 102; status l. 89; strategy l. 2608): stays true unless a statement or an import's status changes on 24 November, which is the rule of the `\date` comment (`main.tex` ll. 76–79). None of my repairs touches `main.tex`.

### 3.4 Sentences that rest on `ugjs/council/v6-repairs-check.md`

The file was not in the tree when I started; it has been there since 23:26, with its second round. The sentences that rest on it:
- `part_i/README.md` ll. 604, 608 and 627;
- README.md ll. 97–100 and `docs/status.md` ll. 84–87;
- `docs/status.md` l. 130;
- `strategy.md` l. 2608;
- the table row in `ugjs/council/README.md`;
- `main.tex` ll. 175–176.

All agree with the report, except "nine observations" (D6).

### 3.5 Observations (no finding)

- The chain audit's "Not verified" item on GJExp Theorem 4.1.2 is not carried into the gate record's open items. The item concerns the class of cutoffs for which that theorem is printed: p. 42 says only "let g ≡ 1 on B_t", which matters for (P) with g ∈ 𝒢. The gate record lists the Appendix E audit's unverified pages but not this one.
- The status sentences and the record's notice of 7 November are untouched, as required.

## 4. Checks actually run, with output

- **Tree.**
  - `git status --short`: 37 paths at 23:25, then 38 (32 M, 6 ??) from 23:26.
  - sha256 of all 38 paths at 23:33, 23:54 and 00:00: identical.
  - `git log -1`: 49f2d23. `git tag -l`: empty.
- **Manuscript build** (scratch copy; three passes of `SOURCE_DATE_EPOCH=1795392000 FORCE_SOURCE_DATE=1 /Library/TeX/texbin/pdflatex -interaction=nonstopmode main.tex`; pdfTeX 3.141592653-2.6-1.40.29, TeX Live 2026):
  - exit 0, 0, 0;
  - `grep -cE '^!'` 0; `grep -c Overfull` 0; `grep -icE undefined` 0;
  - `pdftotext | grep -nE '\?\?|TODO|Hmm|wait,'`: no output (exit 1);
  - `pdfinfo`: 127 pages, CreationDate Mon Nov 23 01:00:00 2026 CET;
  - sha256 `b2bd43f31ce15ad5863ddac7746fff067bc0b51221521bed4e7d3bfd85d17271`; `cmp` with `part_i/main.pdf`: identical; `main.aux`, `main.toc`: identical.
- **FROZEN build** (epoch 1794355200, three passes): 125 pages; `main.aux` and `main.pdf` byte-identical to FROZEN's.
- **Epochs.** `date -u -r 1795392000`: Mo 23 Nov 2026 00:00:00 UTC. `date -u -r 1794009600`: Sa 7 Nov 2026 00:00:00 UTC.
- **Labels script** (brace-aware parser over `\newlabel`): 238 and 238; added none, removed none, renumbered none; 199 page changes {+1: 113, +2: 86}; FROZEN pages 9–122.
- **Statement environments** (theorem … aux*, compared by label, whitespace-normalised, with and without comments):
  - 127 labelled and 2 unlabelled before and after; the unlabelled ones are equal.
  - Changed: A:cutoff, A:domain, A:gjs, lem:filter, lem:cluster, prop:spectral, thm:MAIN, cor:canonical, hyp:broken, rem:gjs7576, thm:D4, aux:d4-not, prop:ff-symmetries.
  - Word diff of thm:MAIN and thm:D4: "finite," removed and "Definition~\ref{aux:notation-S2def}, finite by" inserted, nothing else. A:gjs: only the opening of the Scope.
- **`python3 -I docs/extract.py --check`** (reads only): "up to date", exit 0.
  - `results.json`: 72 statements, 34 `imports_A8`, at HEAD and now; no flag changed.
  - Scratch run of `extract()` on the checked text (`3da06407…` with its `.aux`): 35, with `lem:filter` and `lem:statederiv` flagged and `cor:canonical` without proof. On the final text: 34.
- **Figure pages.** Word diff of the six `docs/interactive/*.html`: `data-page` spans only. The prose of all nine pages was read; nothing contradicts the record.
- **Import graph.** `fig_dag` of `make_figures.py` run in scratch (python3 3.14.7, numpy 2.5.2, scipy 1.18.1):
  - on the new `results.json`, both SVGs differ from the committed ones by one `<path>`;
  - on HEAD's `results.json`, both are equal;
  - the spine-edge diff is +(A:domain, A:cutoff) and no shading change.
- **Companion build** (scratch copy of `companion/` with subfolders; three passes, epoch 1794009600):
  - exit 0 ×3; errors 0, Overfull 0, undefined 0, Underfull 0; grep empty;
  - 20 pages, CreationDate Sat Nov 7 01:00:00 2026 CET; sha256 `a560cc27…2a29`, byte-identical; `pdfimages -list`: 0 images.
  - `make_bib.py` in a scratch tree: "bib.tex: [R] + 16 entries (…, MMST)", byte-identical to `companion/bib.tex`. Its diff against HEAD is the MMST line only.
  - Against HEAD's PDF: `pdftotext -layout` per page has pp. 2–19 identical, and on p. 20 only "(2021) 1299–1367." → "(2021) 299–360; arXiv:2010.11121."; `pdftoppm -r 72`: pp. 2–19 byte-identical, pp. 1 and 20 differ.
  - p. 1: "Read this first" 75 words, notice 161 words in nine lines, box 236.
- **Label table.** `companion/council/labels.md` against the new `main.aux`: 230/230; shifts as in §2 row 29; max 7, min 0.
- **Evidence.**
  - 97 PNG files. The dossier `.tex` (last commit 6b3937a, 22 Sep) names 54, all present; 43 are not named.
  - `../gjp log --diff-filter=A`: 68 images (35c5059), 3 on 31 Oct, 14 on 7 Nov, 10 on 21 Nov and 2 on 23 Nov. None of the 29 dated 31 Oct or later is in the `.tex`; all are in the Dossier lines and the map.
  - `../gjp show --stat e4389a8`: the two new images. Branch main = origin/main.
  - No image for Simon PDF pp. 162, 167 or 181–183.
  - Viewed: `gj2-local-algebra-40`, `gjiii-08`, `simon-hg-168`, `simon-semibounded-163`, and a crop of `gj71-1` (first page, abstract).
- **Reports.** `cmp` of the six archived files with the council's originals: five identical; `v6-public-texts-report.md` differs at l. 238 only.
- **Status sentence.** Script: the 7-November notice sentence and the next two sentences occur unchanged at HEAD and now (README 2×, `docs/status.md` 1×, `docs/imports.md` 1×).
- **The two paragraphs.** `cmp` of README.md ll. 64–106 with `docs/status.md` ll. 51–93: identical.
- **CITATION.cff.** Ruby `YAML.safe_load`: keys as expected; version "1.2.1"; date "2026-11-24". `python3 -c "import yaml"`: ModuleNotFoundError.
- **Machine paths and e-mail.** `git grep -I --untracked` for the home and temporary-directory prefixes, their hyphen-encoded and session forms, `/var/folders` and `/home/`:
  - one hit, `v6-public-texts-report.md` l. 238, which names the generic prefixes "/var/folders" and "/home/" in prose;
  - e-mail pattern: only `selftest@example.invalid` (`.githooks/selftest.sh` l. 31).
  - Masked word diff of the five path-cleaned files: nine changes, paths only.
- **Liquid.** I scanned every `.md` and `.html` under `docs/` (excluded ones too) for `{{`, `{%`, `%}` and `}}` outside raw blocks: none. `extract.py --check` covers only `{{` and `{%`, in `.md` pages and front-matter HTML not excluded by `docs/_config.yml`.
- **Guard.**
  - `sh .githooks/selftest.sh` (it works in a throwaway clone under `$TMPDIR`; read first): 49 passed, 0 failed; the tree still had 38 entries afterwards.
  - Scratch clone with the 38 paths staged (6 A, 32 M): `.githooks/pre-commit` exit 0.
  - `file`: no image or archive. Both PDFs are tracked at HEAD and contain 0 images.
- **Links.** All `[..](..)`, `href` and `src` targets in the 24 changed or added Markdown files: 60 checked, 58 resolve, and 2 are the elided "…" of D27(c). The code-span paths to the six reports resolve from their files (`../ugjs/council/…`, `../../part_i/README.md`) or from the root.
- **Other reads.**
  - The public texts' diffs in full;
  - the six reports;
  - the 22-November synthesis and orchestrator notes, and the KB node file (read only);
  - `part_ii/README.md` ll. 1–20, 140–246;
  - `companion/` sections where Corollary 12.3 and the corrected sentences occur;
  - `companion/PLAN.md` Parts 2, 8, 11, 12;
  - `docs/*.md`;
  - `ugjs/PLAN.md` (C3 exists).

## 5. Not done, not verified, not run

- **Not done:**
  - the mathematics of `main.tex` (by instruction);
  - a page-by-page look at the 127 pages; companion pages other than 1 and 20 were compared by text and pixels with HEAD, not looked at;
  - the Route T note;
  - the content of `docs/results.md` beyond `--check`.
- **Not verified:**
  - the GitHub About text (no `gh`);
  - "all agents were Opus" and "the orchestrator re-read each finding at its source";
  - the Crossref record of the MMST DOI;
  - "a third edition waits for the author's decision on Phase C";
  - whether the revised Route T note was audited again;
  - "read by the orchestrator" for the two new images (only their 150-dpi metadata and content);
  - the printed page number of `gj71-1` (I saw its first-page abstract only);
  - the live site.
- **Not run:**
  - a Jekyll or site build;
  - `make_figures.py` in the repository (only `fig_dag`, in scratch);
  - any git command that changes a repository; `gh`; `kb`; network access.

## 6. Files written

- This report: `v6-docs-check.md` in the council's reports directory (`<scratch>/c2/reports/`).
- Scratch files in my work directory (not deliverables): build copies of `main.tex`, FROZEN `main.tex` and `companion/`, comparison scripts, page renders and crops, hash snapshots.
- Nothing under the repository.
