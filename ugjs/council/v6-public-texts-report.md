# Working council of 23 November 2026: report of the editor "public-texts"

Paths are relative to the repository root. `<scratch>` is the session scratchpad named in
`BRIEF.md` (not in the repository). Line numbers of `part_i/main.tex` are FROZEN's (= 49f2d23)
unless marked "working tree". Nothing was committed; no git command that changes state was run.

## 1. Outcome

All authorised items are applied: the false `part_ii/README.md` sentence (A1), the wording
corrections B1–B6, and the companion's dated notice (C). There is also a proposed About text
(A2). The companion stays at 20 pages with 0 errors, 0 Overfull, 0 undefined. This needed one
change the brief did not foresee: any notice on p. 1, even a single line, pushed the references
onto p. 21, so shortening alone could not work. The notice's space was therefore taken from
p. 1 only, and pp. 2–20 are pixel-identical to the committed PDF of 7 November.

## 2. Claims, with status word and locator

All claims are about documents, so the words are verified/refuted (AGENTS.md §2). I made no
mathematical claim.

| # | claim | status | locator | how checked |
|---|---|---|---|---|
| 1 | The record the companion describes is `part_i/main.tex` of 7 Nov (110 pp). It is identical at 231b8ea (7 Nov 23:23), b79d2d8 and f213cc8; f213cc8 itself is dated 8 Nov 2026 09:28 +0100. | verified | `git log`; `git show f213cc8:part_i/main.pdf` (pdfinfo: 110 pp); `\date{7 November 2026}` (f213cc8 l. 81); `git diff --stat 231b8ea f213cc8 -- part_i/main.*` empty | read |
| 2 | Audit of 9 Nov: the record named π₀, H₀, the translation and dilation unitaries, and used how translations, parity and dilations act, "without defining these objects by a formula and without deriving or importing those actions" | verified | `main.tex` ll. 139–145 (title-page notice) | read |
| 3 | Record dated 11 Nov: 125 pp; Appendix E gives the definitions and the proofs; A1(e)–(g) are new | verified | `main.tex` l. 81, ll. 145–148, l. 705; `main.aux` app:freefield = E, p. 115; FROZEN `main.pdf` 125 pp | read; pdfinfo |
| 4 | Published 21 Nov | verified (this clone's remote-tracking reflog; not GitHub itself) | `git reflog show origin/main`: d2b106c pushed 2026-11-11 10:39 UTC; 49f2d23 (carrying 73bbb76) pushed 2026-11-21 13:32 +0100 | read |
| 5 | "With this addition the status sentence of 7 November 2026 above stands." | verified | `main.tex` ll. 156–157 | read |
| 6 | Companion §§1 and 4 quote that status sentence verbatim | verified | `companion/sections/s1-result.tex` ll. 72–76; `s4-import.tex` ll. 18–22; `main.tex` ll. 121–124 | compared |
| 7 | Statement numbers unchanged since 7 Nov | verified | `companion/council/labels.md` (7 Nov build) vs FROZEN `main.aux`: 230 common labels, 0 number differences | script |
| 8 | Pages moved by 0–5 for every one of the 230 labels, none earlier; A8 moved from p. 14 to p. 17 | verified | same comparison: histogram {0: 1, 1: 9, 2: 18, 3: 69, 4: 49, 5: 84}; `newlabel{A:gjs}{{A8}{17}...}` | script; grep |
| 9 | Declared readings: A1 Scope ll. 802–804; A3 Scope ll. 922–927; A6 Scope ll. 1030–1046; A8 Scope (d) ll. 1381–1399 | verified | `main.tex` at those lines (A1 p. 10, A3 p. 13, A6 p. 15, A8 p. 17 from `main.aux`) | read |
| 10 | A7 imports U_aK(g)U_a* = K(τ_a g), ΘH₀Θ = H₀, ΘV(g)Θ = V(g) for even 𝒫; "Only the displayed operator identities are imported" | verified | `main.tex` ll. 1061–1070, 1077; `docs/imports.md`, A7 row | read |
| 11 | Rate Ψ_{m₁}(d) and gap m₁ are stated in the working coordinates of §2.6; Remark 3.3 gives their form for general (m₀, λ) | verified | `main.tex` ll. 241–243 and 1698–1701; subsec:weak = 2.6, p. 22; rem:wlog = 3.3, p. 24 | read; aux |
| 12 | C5's checklist covers the GJS pages only; it is the only checklist file in the tree | verified | `part_i/C5_reading_record.md` title and ll. 3–11; `main.tex` ll. 3527–3528; `git ls-files` | read |
| 13 | A1–A7 and Appendix E also rest on non-GJS sources: Simon (A1–A5, A1(e)–(f)), GJ1 (A6), GJ2 (A1(g), A5, A6, A7), GJ71, GJExp, Rosen70, GRS75 | verified | Sources lines `main.tex` ll. 751–757, 840, 909, 951, 986, 1015–1017, 1072 | read |
| 14 | `audit_2026/citation_screenshot_dossier.tex` shows 54 of the 95 images. The 41 it does not show include all 27 images added on 31 Oct, 7 Nov and 11 Nov; all 27 are named in the Dossier lines of `main.tex` and in the Dossier map | verified | exact match of `{name.png}` arguments against `ls audit_2026/evidence`; Dossier map `part_i/README.md` ll. 592–603 | script |
| 15 | The Dossier map names 67 images, all present; 19 images shown by the dossier `.tex` are outside the map (contextual pages); 9 cover pages are in neither | verified | same | script |
| 16 | `fresh_audit_2026_08_16/render_evidence.sh` writes to `fresh_audit_2026_08_16/evidence` | verified | its l. 10 | read |
| 17 | The README's five pictures carry no links; the site has eight interactive figure pages, among them one for each of the five pictures | verified | `README.md` ll. 127–188 (no `<a`, no `href`); `docs/interactive/index.html` ("All eight are ...") and page titles | grep; read |
| 18 | A1 and A3 cite A8 directly in their Scope paragraphs; the generated inventory lists `A:gjs` among their uses | verified | `main.tex` ll. 804, 926; `docs/results.json` | grep; script |
| 19 | A8 is byte-identical between f213cc8 and 49f2d23 | verified | A8 = f213cc8 ll. 943–1261 and 49f2d23 ll. 1096–1414 (319 lines each), `diff` empty; no hunk of `git diff f213cc8 49f2d23 -- part_i/main.tex` falls in new ll. 1096–1414 | diff |
| 20 | Today's working tree changes A8 (opening of its Scope paragraph) | verified as of the working tree at 13:21 | `git diff HEAD -- part_i/main.tex`, hunk `@@ -1343,11 +1366,13 @@` | diff |
| 21 | GJS p. 588 prints "Fock space 𝓕 = L₂(𝒮′(R¹), dφ) is defined by the Gaussian measure dφ with mean zero and covariance μ⁻¹ = (− d²/dx₁² + m₀²)^{−1/2}, see [1]. Also : : denotes Wick ordering with respect to dφ." | verified | `audit_2026/evidence/gjs-source-05.png`, viewed and enlarged | image |
| 22 | The record's covariance is C = (2μ)⁻¹, μ = (−∂ₓ² + m₀²)^{1/2} | verified | `main.tex` ll. 457–458 (subsec:model = 2.1, p. 8) | read; aux |
| 23 | Machine paths in the tracked tree: 9 lines before my edits, 0 after | verified | `git grep` (section 4) | grep |
| 24 | Any notice in the p. 1 box, even one line, gives 21 pages unless its space is recovered on p. 1 | verified | test builds (section 4) | build |
| 25 | The final companion: 20 pp, 0/0/0/0; pp. 2–20 identical in text and in pixels (72 dpi) to the committed PDF | verified | section 4 | build; pdftotext; pixel compare |
| 26 | Reference [R] with the commit added runs to 9 rendered lines instead of 8, for four accurate wordings | verified | section 4 | build |
| 27 | `make_bib.py` leaves `companion/bib.tex` unchanged, against both FROZEN's and the working tree's `main.tex` | verified | run in scratch copies only | cmp |

## 3. Changes, findings and deviations

### 3.1 Every change (locus, before, after, how verified)

**A1. `part_ii/README.md` ll. 243–245.**
- Before: "**Open residues (explicit, none a hidden gap):** the eta symbol collision (V2/V4, by-hand rename); Part I is conditional on the U_GJS interface (stated on its title page) with item C5 (second human reader for the GJS page images) outstanding."
- After: "**Open residues (explicit, none a hidden gap):** the eta symbol collision (V2/V4, by-hand rename); Part I's Theorem 12.2 is an implication from printed imports, with one GJS theorem imported (Theorem 1.1.7, including its transverse case A8(iv)-T), and its audit item C5 (second human reader for the GJS page images) is open (`../README.md`, Status)."
- Verified against: `README.md` l. 25 (heading "the main theorem is an implication from printed imports"), ll. 20 and 76 (status sentence); `main.tex` l. 127 ("A8(vi) is retired"); C5 record title. The rest of the file is unchanged.

**A2. About text (proposal; the orchestrator applies it).** Built from `docs/_config.yml` l. 5, with the C5 clause of the root README added.
- Proposal (305 characters; 307 UTF-8 bytes): "Manuscript, working notes and adversarial audit trail. Theorem 12.2 is an implication from printed imports (A1–A8), with one GJS theorem imported (Theorem 1.1.7, including its transverse case A8(iv)-T); the human page readings of audit item C5 are open; nothing is refereed; human verification is ongoing."
- Alternative naming the subject (345 characters; 350 UTF-8 bytes, at the limit if GitHub counts bytes): "Spatial cutoff removal for weakly coupled P(φ)₂: manuscript, working notes, adversarial audit trail. Theorem 12.2 is an implication from printed imports (A1–A8), with one GJS theorem imported (Theorem 1.1.7, including its transverse case A8(iv)-T); human page readings (audit item C5) open. AI-assisted, not refereed; human verification ongoing."
- Counted with Python `len()` and `len(s.encode())`.

**B1. Scope of C5.**
- `README.md` l. 19.
  - Before: "open audit item C5 (a second human reader for the source page images, see below) is"
  - After: "open audit item C5 (a second human reader for the GJS page images, see below) is"
- `README.md` ll. 97–99.
  - Before: "**Open audit item C5.** No second human reader has yet checked the source page images against the transcriptions in §2. The itemized checklist is `part_i/C5_reading_record.md`; all thirteen verdict fields are still blank. Since"
  - After: "**Open audit item C5.** No second human reader has yet checked the GJS page images against the transcriptions in §2. The itemized checklist is `part_i/C5_reading_record.md`; all thirteen verdict fields are still blank. C5 covers the GJS pages only: the transcriptions from the other sources of A1–A7 and Appendix E (Simon's book and the Glimm–Jaffe papers among them) have no human checklist, and on record only agents have compared them with the page images (`part_i/README.md`). Since"
- `docs/status.md` ll. 97–100.
  - Before: "**No second human reader has yet checked the source page images against the transcriptions in §2.** The itemized checklist is [`part_i/C5_reading_record.md`](…); all thirteen verdict fields are blank."
  - After: "**No second human reader has yet checked the GJS page images against the transcriptions in §2.** The itemized checklist is [`part_i/C5_reading_record.md`](…); all thirteen verdict fields are blank. C5 covers the GJS pages only: the transcriptions from the other sources of A1–A7 and Appendix E (Simon's book and the Glimm–Jaffe papers among them) have no human checklist, and on record only agents have compared them with the page images ([`part_i/README.md`](https://github.com/alexander-stottmeister/pphi2-cutoff-removal/blob/main/part_i/README.md))." The link pattern is the page's own.
- Verified: claims 12–13. "Compared ... by agents" is from `part_i/README.md` ll. 504, 578 and 585 (V4, V4d, V5 sources, D3). I wrote "on record" because the author's private line-by-line check (README l. 18) is not documented.

**B2. `part_i/C5_reading_record.md`.**
- ll. 26–28.
  - Before: "... and the unnumbered source fact of the retired item (vi). Since 7 November 2026, items 1–4 ..."
  - After: "... and the unnumbered source fact of the retired item (vi). Assumption A8 is unchanged in the version of 11 November 2026 (Appendix E). Since 7 November 2026, items 1–4 ..."
  - Verified: claim 19. I did not add "or 23 November": claim 20 shows A8's Scope changing in today's working tree.
- Item 7, "To confirm".
  - Before: "... the ground eigenvalue is simple (record the exact statement and any citation the source gives for it)."
  - After: "... the ground eigenvalue is simple (record the exact statement and any citation the source gives for it); and (added 23 November 2026) the sentence that defines Fock space, "Fock space 𝓕 = L₂(𝒮′(R¹), dφ) is defined by the Gaussian measure dφ with mean zero and covariance μ⁻¹ = (− d²/dx₁² + m₀²)^{−1/2}, see [1]. Also : : denotes Wick ordering with respect to dφ." (transcribe exactly what `gjs-source-05.png` prints). The record's Gaussian measure dφ₀ has covariance C = (2μ)⁻¹ with μ = (−∂ₓ² + m₀²)^{1/2} (`main.tex` §2.1), and Assumption A1, Scope, records that the identification of the sources' V(g), defined by normal ordering in Fock space, with the record's V(g) is not proved in the manuscript and remains a reading."
  - Format kept as in item 2's dated addition. Every verdict field is still blank.
  - Verified: claims 21, 22; A1 Scope `main.tex` ll. 802–804 (in the working tree that sentence is at ll. 818–820, unchanged).

**B3. Dossier index and regeneration.**
- `README.md` ll. 249–251.
  - Before: "... has no render script; its page list is the dossier's own `.tex`. The script names ..."
  - After: "... has no render script; its index `audit_2026/citation_screenshot_dossier.tex` shows 54 of its 95 images and none of the pages added since 31 October 2026, which are listed in the Dossier line of each assumption in `part_i/main.tex` and in the "Dossier map" at the end of `part_i/README.md`. The render script names ..."
- `docs/provenance.md` l. 22.
  - Before: "| `audit_2026/citation_screenshot_dossier.tex` + `evidence/` | page images for every import |"
  - After: "| `audit_2026/citation_screenshot_dossier.tex` + `evidence/` | page images for every import; the `.tex` shows 54 of the 95 images and none of the pages added since 31 October 2026, which are listed in the Dossier line of each assumption in `part_i/main.tex` and in the "Dossier map" at the end of `part_i/README.md` |"
- `docs/provenance.md` ll. 94–102.
  - Before: "To regenerate the corpus from your own copies of the sources:" [code block] "... The `render` lines name the file expected for each source under `refs/`."
  - After: "To regenerate the corpus of the 16 August 2026 audit, `fresh_audit_2026_08_16/evidence/`, from your own copies of the sources:" [code block unchanged] "... The `render` lines name the file expected for each source under `refs/`. The older dossier `audit_2026/evidence/`, the one `part_i/main.tex` cites, has no render script; its page images behind the imports are listed in the Dossier line of each assumption in `part_i/main.tex` and in the "Dossier map" at the end of `part_i/README.md`."
- Verified: claims 14–16; `main.tex` ll. 633–634 (§2.4 names the folder). I dropped the brief's "only" (finding F3).

**B4. README sentences.**
- l. 117.
  - Before: "Each figure links to an interactive version. One of them, ..."
  - After: "Each figure has an interactive version on the documentation site (see Documentation below); the pictures in this file carry no links. One of them, ..."
- ll. 139–140.
  - Before: "Assumptions A1 and A3 are shaded since 7 November 2026 only because their Wick-power paragraphs refer to Appendix D, which applies A8 — an effect of the mechanical index;"
  - After: "Assumptions A1 and A3 are shaded since 7 November 2026 because their Scope paragraphs cite Assumption A8, Scope (d), and the index counts an assumption's own references as its uses — an effect of the mechanical index;"
- ll. 210–211.
  - Before: "..., where the eight figures below are interactive."
  - After: "..., where eight figures are interactive: the five pictures above and three more."
- Verified: claims 17 and 18; `part_i/README.md` l. 502.

**Companion row, `README.md` l. 200** (a sentence the notice would make false).
- Before: "... its page numbers are those of that build, and it does not mention Appendix E |"
- After: "... its page numbers are those of that build, and only a dated notice of 23 November 2026 in the box on its first page mentions Appendix E |"

**B5. Machine paths.** Each machine path is replaced and nothing else on its line changes. The originals are at 49f2d23. Below, a removed path is written as ‹path›, because this report is archived.
- `ugjs/council/BRIEF.md` l. 140: "`<scratch> = ‹path›`:" → "`<scratch> = <session scratch directory>`:"
- `ugjs/council/ab-drafting-brief.md`:
  - l. 5: "`‹path›/glimm_jaffe/`." → "`<ws>/glimm_jaffe/`."
  - l. 6: "`‹path›/phaseAB/`" → "`<scratch>/phaseAB/`"
  - l. 26: "4. `‹path›/AGENTS.md`, §§1–4: ..." → "4. `<ws>/AGENTS.md`, §§1–4: ..."
- `ugjs/council/r3-verifier-brief.md` l. 5: "scratchpad is `<scratch> = ‹path›`;" → "scratchpad is `<scratch> = <session scratch directory>`;"
- `ugjs/council/v1-brief.md`:
  - l. 4: "`WORK/` = `‹path›/phaseAB/`." → "`WORK/` = `<scratch>/phaseAB/`."
  - l. 6: "Record: `‹path›/glimm_jaffe/part_i/main.tex`" → "Record: `part_i/main.tex`"
  - l. 11: "(`‹path›/AGENTS.md`)" → "(`<ws>/AGENTS.md`)"
- `ugjs/council/v2-report.md` l. 6: "`WORK/` = `‹path›/phaseAB/`." → "`WORK/` = `<scratch>/phaseAB/`."
- `ugjs/council/README.md`, new last section "## Machine paths (23 November 2026)": "On 23 November 2026 the machine paths in five archived files of this folder (`BRIEF.md`, `ab-drafting-brief.md`, `r3-verifier-brief.md`, `v1-brief.md`, `v2-report.md`) were replaced by paths relative to the repository root and by two placeholders, `<scratch>` for the session's scratch directory and `<ws>/` for the folder on the author's machine that holds this repository and `AGENTS.md`; nothing else on those lines changed, and the git history keeps the originals."
- Where a line defines `<scratch>` itself, writing `<scratch> = <scratch>` would say nothing, so I used `<session scratch directory>`. `<ws>/` is defined in the README sentence because it is not defined in the public tree.

**B6. `companion/council/README.md` ll. 102–113.**
- Before: "... published on 21 November), and those sentences hold again. The companion itself is unchanged: it is the edition of 7 November 2026 ... label table of that build, and the companion does not mention Appendix E. A third edition is not scheduled."
- After: "... published on 21 November), and those sentences hold of the repaired record (125 pages), not of the record of 7 November that the companion describes. The companion's text was not changed for the repair: it is the edition of 7 November 2026 ... label table of that build, and the companion's body does not mention Appendix E."
- Followed by a new paragraph "*23 November 2026, dated notice.*" (full text in `<scratch>/c2/reports/public-texts.diff`). It summarises the notice, gives the reason for the p. 1 typography, and says that pp. 2–20, the edition, its date, its epoch and [R] are unchanged. It records that "a third edition waits for the author's decision on Phase C", and that no agent that did not write the notice has checked it yet.
- I kept the dated paragraph of 11 November true as history and put today's facts into a new dated paragraph, which is how this file records later changes.

**C. The companion's dated notice (`companion/companion.tex`; `companion/companion.pdf` rebuilt).**
- Inside the p. 1 box (`statusnotice`), after the unchanged "Read this first" paragraph (75 words), verbatim:
  > \smallskip
  > \emph{Notice of 23~November 2026.} The record of 7~November is that of commit f213cc8. An audit of 9~November found it using the momentum field, the free Hamiltonian and the action of translations, parity and dilations without defining, deriving or importing them; the record of 11~November (125~pages, published 21~November) does so in Appendix~E, and the status sentence quoted in \S\S1 and 4 stands for it. Statement numbers are unchanged; the pages cited here are up to five pages too early. \S4's table and Fig.~1 predate A1(e)--(g); read their ``literal imports'' with the readings declared in the Scope paragraphs of A1, A3, A6 and A8, and A7's row as the covariance of $K(g)$ and the parity of $H_0$ and, for even $\mathscr P$, of $V(g)$. \S1's rate and gap are in the record's working coordinates (\S2.6; general form: Remark~3.3). A third edition waits for the author's decision on Phase~C.
- It renders as 156 words (`pdftotext | wc -w`). Each clause rests on these claims:
  - commit: claim 1;
  - audit, Appendix E, publication, status: claims 2–6;
  - numbers and pages: claims 7–8;
  - A1(e)–(g): claim 3;
  - readings: claim 9 (all four Scope paragraphs verified, so all four are named);
  - A7: claim 10;
  - working coordinates: claim 11;
  - third edition: see "Not verified".
- Typography, confined to p. 1 (reason: F1):
  - `\begin{statusnotice}\footnotesize` (the whole box, both paragraphs, in footnote size; no word of the old paragraph changed);
  - a local `\@maketitle`, article.cls's own with `\kern-40pt` at its top and the skips 1.5em, 1em, 1.5em changed to .75em, .25em, 0em;
  - `\kern-6pt` after `\maketitle`, `\kern-8pt` after the box, `\kern-14pt` before `\paragraph*{How to read.}`;
  - three header comment lines that say so.
- Date and epoch: I kept `\date{7 November 2026}` and `SOURCE_DATE_EPOCH=1794009600`. The edition is unchanged. The companion's precedent, the notice of 2 November 2026 (commit 4166883), kept `\date{24 October 2026}` and that edition's epoch: the PDFs at 3233fdc and 4166883 both carry CreationDate 24 Oct 2026 02:00 CEST. `README.md` ll. 310–313 and the header of `companion.tex` name 1794009600, so both stay true. One consequence: the PDF's metadata date is still 7 November, and only the notice's own text carries 23 November.
- Reference [R] is unchanged (F2).
- What I cut from the brief's wording, for space:
  - "(A8 moved from p. 14 to p. 17)", which is verified (claim 8) but cost a line;
  - "110 pp", already in the "Read this first" paragraph;
  - "dated ... 2026" and "on" in the dates;
  - Remark 3.3 compressed to "(§2.6; general form: Remark 3.3)".
- Wording I changed after verifying:
  - "The record of 7 November is that of commit f213cc8", because f213cc8 is dated 8 November (claim 1);
  - "predate A1(e)–(g)", not "lack", because Fig. 1 lists no items of A1;
  - "for even 𝒫" added to A7, as A7 states it.
- I checked the notice against the companion's banned words (`companion/PLAN.md` Part 4, rule 10): none occurs. The quotation marks enclose only the companion's own words "literal imports" (`s4-import.tex` l. 114; `figures/fig-spine.tex` l. 32).

### 3.2 Findings

- **F1 (companion budget; MINOR; resolved).**
  - Locus: `companion/companion.tex`, the p. 1 box.
  - What happens: the base build's p. 1 has no free space; its last baseline sits at the foot of the text block. A notice of any size, from a heading-only line to 13 lines, gave 21 pages. A one-line notice already shifts every page break after p. 1, and the references spill onto p. 21.
  - Why the brief's remedy fails: shortening the notice cannot repair this.
  - Repair: recover the notice's height on p. 1 alone, as described under C, so that p. 1 ends at the same line, "(coupling λ, C-Wick". Pages 2–20 are then pixel-identical.
  - Deviations from `companion/PLAN.md`: its front-matter budget "notice ≤ 80 words" (l. 78, Part 8 item 12) is now exceeded (75 + 156 words in the box), and the box is set in footnote size.
- **F2 ([R]; MINOR; left unchanged).**
  - Locus: `companion/make_bib.py` ll. 31–35 → `companion/bib.tex` l. 3, currently 8 rendered lines.
  - Test: "…, version of 7 November 2026, commit f213cc8, …", "…, 7 November 2026, at commit f213cc8, …", "…, of 7 November 2026, commit f213cc8, …" and "…, version of 7 November 2026 at commit f213cc8, …" each render as 9 lines.
  - Why not "commit f213cc8 of 7 November": that would be false (claim 1).
  - Result: the brief's condition fails, and the notice now carries the commit instead.
- **F3 (brief's B3 wording; MINOR).**
  - "listed only in the Dossier lines ... and the Dossier map" is false. Three of the post-31-October GJS images are also named in C5 items 12–13, and all of them appear in `docs/results.*`.
  - Repair: I wrote "listed in" without "only".
- **F4 (brief's B1 list; MINOR).**
  - Besides A1, A3, A4, A6 and Appendix E, the imports A2 (Simon; GRS75), A5 (GJExp; Simon; Rosen70; GJ2) and A7 (GJ2) also rest on non-GJS transcriptions (claim 13).
  - Repair: I wrote "the other sources of A1–A7 and Appendix E".
- **F5 (brief's B2 reason clause; MINOR).**
  - Text in the brief: "the dictionary between the two is a declared reading (A1 Scope)".
  - At FROZEN, A1's Scope declares as a reading only the V(g) identification for the Fock-space sources; the covariance of GJS p. 588 is not addressed (cqft N1 of 22 Nov).
  - Repair: the C5 sub-item states what is true at FROZEN and in the working tree.
  - Follow-up: the working tree now adds to A1's Scope the sentence "Literally μ⁻¹ = 2C; reading μ⁻¹ as the inner product 2⟨f, Cg⟩ of ℋ_C ... is a reading of the kind recorded in Assumption A8, Scope (d)" (other editor's hunk `@@ -794,8 +802,16 @@`). Once that is committed, the orchestrator may cite it in item 7.
- **F6 (C5 record and A8; note).** Today's working tree rewords the opening of A8's Scope paragraph (claim 20). "A8 was not changed on 23 November" would therefore be false, and I did not write it. After the record is committed, the orchestrator may add a dated clause naming what changed.
- **F7 (record text; MINOR; not my file).** Yesterday's N7 also applies inside the record:
  - `main.tex` ll. 633–634, "(audit_2026/evidence/, index in audit_2026/citation_screenshot_dossier.tex)";
  - `main.tex` l. 3398 (table of frozen sources), "... + evidence/ & page images for every import".
- **F8 (hygiene; no action).**
  - Ten untracked LaTeX recorder files, `part_ii/*.fls`, hold machine paths in their `PWD` line. They are ignored by `.gitignore` l. 98 (`*.fls`) and are not in git.
  - No tracked file holds a machine path after the edits.
- **F9 (archiving; note).**
  - The exact diff the brief asks for, `<scratch>/c2/reports/public-texts.diff`, necessarily contains the 9 removed lines with the old machine paths.
  - If a diff is archived in the repository, use `<scratch>/c2/reports/public-texts.masked.diff`, in which those paths are masked (not an applyable patch).

## 4. Checks run, with output

- **Companion build in the repository.** Three passes of `SOURCE_DATE_EPOCH=1794009600 FORCE_SOURCE_DATE=1 /Library/TeX/texbin/pdflatex -interaction=nonstopmode companion.tex` in `companion/`. `make_bib.py` was not run in the repository, because `part_i/main.tex` is being edited (claim 27).
  - Exit codes 0, 0, 0.
  - `grep -cE '^!' companion.log` → 0; `grep -c Overfull` → 0; `grep -icE undefined` → 0; `grep -c Underfull` → 0.
  - `pdftotext companion.pdf - | grep -nE '\?\?|TODO|Hmm|wait,'` → nothing.
  - `pdfinfo`: Pages 20; CreationDate Sat Nov 7 01:00:00 2026 CET.
  - `pdfimages -list`: 0 images.
  - `shasum -a 256 companion/companion.pdf` → `e978c315414cca83e34d67cc93710ed61b74c89d72aed76534a5e508d7aabefe`.
  - The same hash came from a clean scratch build (aux removed, three passes).
  - The committed PDF before my change was `1aeab355cc719a0bbb3bc44d648f13c3610af9b2ab4b43c6ab34a8b130d353aa`, reproduced byte for byte in scratch before editing.
- **Pages 2–20 against the committed PDF.**
  - `pdftotext -layout` of each page compared: 19/19 identical.
  - `pdftoppm -r 72`, PIL `ImageChops.difference`: 0 pages with a pixel difference.
  - Positions on p. 1 (pdftotext -bbox): "How to read" at y = 559.9 (base 559.8); §1 heading at 630.6 (base 630.6); last line "… (coupling λ, C-Wick" as in the base.
- **Renders.** p. 1 at 100 dpi and the box at 200 dpi, looked at.
  - The notice is legible and inside the box; the box is inside the margins.
  - The title's top is at y = 87.9 pt, inside the text block, which begins at 85.04 pt.
  - Ties keep "9 November" and "125 pages" together.
  - No other page moved.
- **Budget tests (scratch).**
  - Filler notices of 1, 2, …, 8 lines, a heading-only line and the full 178-word draft: all 21 pages.
  - Compensation variants: E1, H1, H2, J1–J3 and K1 gave 20 pages with pp. 2–20 identical; the final source is K1 with ties.
- **[R] tests (scratch).** Four accurate wordings with the commit; each gives 9 rendered lines against the current 8. The page count stayed 20, but the references rebalance.
- **Label tables.**
  - `labels.md` vs FROZEN `main.aux`: common 230, number differences 0, page shifts {0: 1, 1: 9, 2: 18, 3: 69, 4: 49, 5: 84}, none negative.
  - The same against the working tree's `main.aux` (other editor's build, 13:21; 125 pp; `\date{11 November 2026}`): shifts {0: 1, 1: 9, 2: 11, 3: 72, 4: 34, 5: 103}, none negative.
- **`.aux` greps (FROZEN).** subsec:model 2.1 p. 8; subsec:imports 2.4 p. 10; A1 p. 10; A3 p. 13; A6 p. 15; A7 p. 16; A8 p. 17; subsec:weak 2.6 p. 22; rem:wlog 3.3 p. 24; thm:MAIN 12.2 p. 41; app:freefield E p. 115; E.5 p. 120; E.6, E.7 p. 122.
- **A8 diff.** No hunk of `git diff f213cc8 49f2d23 -- part_i/main.tex` falls in new ll. 1096–1414: the last hunk before A8 ends at l. 1091 and the next starts at l. 1476. The extracted environments (319 lines each) are identical.
- **Dossier counts.**
  - 95 files in `audit_2026/evidence/`, all `.png`.
  - 54 distinct `{name.png}` in the dossier `.tex`, all present.
  - 41 not shown, including the 27 dated 31 Oct, 7 Nov and 11 Nov, all named in `main.tex` Dossier lines and in the Dossier map (slash forms expanded).
  - Map: 67 names, 0 missing.
- **Machine-path grep.**
  - Before, `git grep -n` for the two machine-path prefixes (the home directory and the temporary directory) in `ugjs companion docs part_i part_ii README.md strategy.md`: 9 lines, namely `ugjs/council/BRIEF.md:140`, `ab-drafting-brief.md:5,6,26`, `r3-verifier-brief.md:5`, `v1-brief.md:4,6,11`, `v2-report.md:6`. The whole tracked tree, also searched for the hyphen-encoded form of the home-directory path, for its parent folder names, and for `/var/folders` and `/home/`, gave the same 9 lines; no binary file matched.
  - After: 0 in the prescribed scope; 0 in the whole tracked tree for all those patterns (the patterns themselves are omitted here because they spell out the machine layout). A plain `grep -r` over the working directory finds only the 10 ignored `part_ii/*.fls` (F8).
- **Liquid delimiters** (`{{`, `{%`, `%}`, `}}`) in `docs/status.md` and `docs/provenance.md`: 0 at HEAD, 0 now.
- **Old wordings** ("eight figures below", "page list is the", "source page images", "Each figure links", "conditional on the U_GJS interface", "page images for every import |", "To regenerate the corpus from", "hold again", "A third edition is not scheduled"): no hit in the edited files. README l. 71 is untouched.
- **`make_bib.py`.** Run with `python3 -I` in two scratch copies (FROZEN `main.tex`; working-tree `main.tex`): "[R] + 16 entries", and `bib.tex` byte-identical to the repository's.
- **About text.** Character counts as given in 3.1 (A2).

## 5. Not done, not verified, not run

- **Not done:**
  - [R] (F2).
  - The "23 November" clause about A8 in the C5 record (F6).
  - Sentences in files outside my list, now the orchestrator's:
    - `part_i/README.md` l. 590, "The companion is not revised: it is the edition of 7 November 2026 and describes the 110-page record of that date." — after the notice, add that a dated notice was added on 23 November 2026.
    - `companion/PLAN.md` has no record of the notice. A Part 11.2 could record it and the budget deviation (F1).
    - `main.tex` ll. 633–634 and l. 3398 (F7).
    - `strategy.md` l. 2598 stays true ("a third edition of the companion, which still describes the record of 7 November"), but has no entry for today.
    - `CITATION.cff` and `docs/index.md` need nothing.
  - The About text itself (the orchestrator applies it).
  - The optional mapping line for the new item-7 sentence in the C5 record's "What a completed record closes".
- **Not verified:**
  - That a third edition waits for the author's decision on Phase C. This rests on the orchestrator's message and on `SYNTHESIS.md` of 22 Nov (item 5); no file records the author's own words.
  - "Published 21 November" rests on this clone's remote-tracking reflog, not on GitHub.
  - Whether GitHub counts the About limit in characters or in bytes (the proposal fits either way).
  - How the edited docs pages render on the live site.
  - Whether the other editor's final `main.tex` keeps 125 pages and shifts of at most 5. As of 13:21 it did; re-check the notice's "125 pages" and "up to five pages" against the committed build.
- **Not run:**
  - A Jekyll or site build.
  - `docs/extract.py --check`, because `main.tex` is changing under the other editor.
  - `make_bib.py` in the repository.
  - An independent check of the notice by an agent that did not write it.

## 6. Files written

- **Repository**, none committed:
  - `README.md`
  - `part_ii/README.md`
  - `docs/status.md`
  - `docs/provenance.md`
  - `part_i/C5_reading_record.md`
  - `ugjs/council/BRIEF.md`, `ab-drafting-brief.md`, `r3-verifier-brief.md`, `v1-brief.md`, `v2-report.md`, `README.md`
  - `companion/companion.tex`
  - `companion/council/README.md`
  - `companion/companion.pdf`, rebuilt
  - `companion/companion.aux`, `.log`, `.out`: untracked build products, rewritten by the build
- **Unchanged:** `companion/bib.tex`, `companion/make_bib.py`, `companion/preamble.tex`, and every section and figure file.
- **Outside the repository:**
  - `<scratch>/c2/reports/public-texts.md` (this report)
  - `<scratch>/c2/reports/public-texts.diff` (exact `git diff -- . ':!part_i/main.tex' ':!part_i/main.pdf' ':!companion/companion.pdf'`, 397 lines, 13 files)
  - `<scratch>/c2/reports/public-texts.masked.diff`
  - working files under `<scratch>/c2/work/public-texts/`

## Follow-up (23 November 2026, after the record's second pass)

Paths are relative to the repository root. Line numbers of `part_i/main.tex` are those of the
working tree at 13:49:36; the file had not changed when this section was written (14:11). Nothing
was committed.

### F.1 Outcome

All five follow-up items are done.
- The companion's bibliography was regenerated: only the MMST entry changed. [R] still describes the 110-page record of 7 November.
- The notice was rewritten at its old length (nine lines in the box) and is verified clause by clause.
- The companion is still 20 pages with 0 errors, 0 Overfull, 0 undefined. Pages 2–19 are identical to the committed PDF of 7 November, and p. 20 differs only in the last line of the MMST entry.
- The council README, the README row and the C5 record are updated.
- Three sentences I wrote this morning have since become false and lie outside this follow-up's scope (G1). They are reported for the orchestrator, with the repair.

### F.2 Claims, with status word and locator

| # | claim | status | locator | how checked |
|---|---|---|---|---|
| 1 | The record is dated 23 November 2026, built with epoch 1795392000, and has 127 pages | verified | `main.tex` ll. 81–82; `pdfinfo part_i/main.pdf`: 127 pp, CreationDate 23 Nov 2026 01:00 CET | read |
| 2 | Corollary 12.3 now reads: "Let 𝒫(ξ)=ξ⁴, and let the cutoff g of [GJ3, (2.3)] be chosen in 𝒢, that is, with 0≤g≤1. Then every w* limit point of the averaged states ω_n of [GJ3, (2.4)] and of the unaveraged states ω_{g_n}, g_n=g(·/n), coincides on each 𝔄(O) with ω_∞; …". At FROZEN it had no restriction ("Every w* limit point of the (averaged or unaveraged) finite-volume ground states constructed in [GJ3, §2] coincides …"). | verified | cor:canonical = 12.3, p. 43, `main.tex` ll. 3172–3181 (FROZEN: 12.3, p. 42, l. 3126) | diff of the environment |
| 3 | Theorem 12.2: items (1)–(5) unchanged. Only the last sentence of its imports paragraph is reworded, now "the unevaluated constant S₂(B₃ₓ₅) of Definition N.14, finite by Theorem C.5". The title-page notice says "Theorem 12.2 and every other theorem are unchanged in substance". | verified | thm:MAIN = 12.2, p. 42; diff of the environment; `main.tex` l. 167 | diff; read |
| 4 | The notices of 16 Aug–11 Nov, the status sentence of 7 Nov and "With this addition the status sentence of 7 November 2026 above stands" are unchanged. The new notice "Audit of 23 November 2026; corrections" is ll. 161–178. | verified | REPO ll. 87–158 identical to FROZEN ll. 86–157 | diff |
| 5 | All 230 labels of `companion/council/labels.md` keep their numbers. Their pages move by 0–7 ({0: 1, 1: 5, 2: 9, 3: 21, 4: 81, 5: 3, 6: 55, 7: 55}), none earlier. | verified | `labels.md` vs REPO `part_i/main.aux` (13:50:01) | script |
| 6 | The MMST entry of the record is "Comm. Math. Phys. 387 (2021) 299--360; arXiv:2010.11121". The arXiv abstract page, fetched today with a generic client, gives the journal-ref "Commun. Math. Phys. 387, 299-360 (2021)", the four authors, the title and DOI 10.1007/s00220-021-04152-5. `refs/part_ii/MMST_scaling_limits_wavelets_2010.11121.pdf` is arXiv v2 (26 Oct 2021) and prints no journal pages. | verified | `main.tex` ll. 8848–8850; arxiv.org/abs/2010.11121 | read |
| 7 | A8 (`A:gjs`, A8, p. 17): only the opening of its Scope paragraph changed (the sentence on Theorem 1.1.8, which cited pp. 597 and 595 and now also p. 629, and the sentence on a stricter standard). No item (i)–(viii) and no point (a)–(d) changed. | verified | environment diff FROZEN (319 lines) vs REPO (321 lines): one hunk, environment lines 251–255 → 251–257 (REPO l. 1389 contains "A stricter standard") | diff |
| 8 | A1's Scope now records "Literally μ⁻¹=2C; reading μ⁻¹ as the inner product 2⟨f, Cg⟩ of ℋ_C … is a reading of the kind recorded in Assumption A8, Scope (d), not proved here". The V(g) sentence ("They define V(g) by normal ordering in Fock space; …") is unchanged; it now follows the sentence naming GJ2, GJ71 and Rosen70 as the Fock-space sources. | verified | `main.tex` ll. 822–829 ("Literally" at l. 825), l. 835; A1 p. 11 | read |
| 9 | A3, A6 and A7 are unchanged | verified | environment diffs, 0 lines each | diff |
| 10 | The rate and gap are stated in working coordinates; Remark 3.3 gives the general form | verified | `main.tex` ll. 263–265, 1740–1743 | read |
| 11 | The companion cites Corollary 12.3 in §1 (`s1-result.tex` ll. 82–84, Table 1 l. 111, closing line l. 142), §2 (Table 2, `s2-open.tex` ll. 64–65; l. 95), §7 (`s7-identification.tex` ll. 59–60, l. 66), Appendix A (`appA-pointers.tex` l. 90) and Fig. 1 (`figures/fig-spine.tex` l. 109). Where it states the corollary (§1 ll. 82–84, Table 2, §7 ll. 59–60, Fig. 1), it states it without the new restriction. | verified | as listed | read |
| 12 | `audit_2026/evidence/` now holds 97 images. The two new ones (23 Nov 13:32), `simon-semibounded-163` and `simon-hg-168`, are named only in A5's Dossier line (`main.tex` ll. 1036–1037), not in the Dossier map of `part_i/README.md` (A5 row, l. 600; file unchanged since 21 Nov) and not in the dossier `.tex` (still 54 images shown) | verified | `ls`, `grep` | read |

### F.3 Changes (before and after, verbatim)

**1. `companion/bib.tex`.** Regenerated with `cd companion && python3 make_bib.py`, as `README.md` (Building) prescribes. Output: "bib.tex: [R] + 16 entries (GJ1, GJ2, GJ3, GJ4, GJ71, GJExp, GJS, GRS75, Rosen70, SimonBook, AHZ, BDW, RZT, Hastings, BMNS, MMST)". The diff, in full:
```
@@ -69,7 +69,7 @@ Comm.\ Math.\ Phys.\ \textbf{309} (2012) 835--871.
 \bibitem{MMST} V.~Morinelli, G.~Morsella, A.~Stottmeister, Y.~Tanimoto,
 \emph{Scaling limits of lattice quantum fields by wavelets},
-Comm.\ Math.\ Phys.\ \textbf{387} (2021) 1299--1367.
+Comm.\ Math.\ Phys.\ \textbf{387} (2021) 299--360; arXiv:2010.11121.
```
- [R] is unchanged: it is a constant in `make_bib.py` ll. 31–35 and reads "110 pp., version of 7 November 2026".
- Nothing else in the file changed.
- Besides the pages, the arXiv number now appears; it comes from the same bibitem of `main.tex` and is verified (claim 6).
- Before running the script in the repository, I ran it on a scratch copy to see its diff.

**2. The notice** (`companion/companion.tex`, inside `statusnotice`).
- Before (source): "\emph{Notice of 23~November 2026.} The record of 7~November is that of commit f213cc8. An audit of 9~November found it using the momentum field, the free Hamiltonian and the action of translations, parity and dilations without defining, deriving or importing them; the record of 11~November (125~pages, published 21~November) does so in Appendix~E, and the status sentence quoted in \S\S1 and 4 stands for it. Statement numbers are unchanged; the pages cited here are up to five pages too early. \S4's table and Fig.~1 predate A1(e)--(g); read their ``literal imports'' with the readings declared in the Scope paragraphs of A1, A3, A6 and A8, and A7's row as the covariance of $K(g)$ and the parity of $H_0$ and, for even $\mathscr P$, of $V(g)$. \S1's rate and gap are in the record's working coordinates (\S2.6; general form: Remark~3.3). A third edition waits for the author's decision on Phase~C."
- After (source), verbatim:
```
\emph{Notice of 23~November 2026.} An audit of 9~November found the record described here
(commit f213cc8) using its free-field layer (momentum field, free Hamiltonian, translations,
parity, dilations) without stating it; since 11~November Appendix~E supplies it, and the
status sentence quoted in \S\S1 and 4 stands. The current record (23~November, 127~pages)
restricts Corollary~12.3 (\S\S1, 2, 7, Fig.~1 here) to $\mathscr P(\xi)=\xi^4$ and cutoffs
$0\le g\le1$ in \cite[(2.3)]{GJ3}; Theorem~12.2 is unchanged in substance. Statement numbers
are unchanged; cited pages are up to seven too early. \S4's table and Fig.~1 predate
A1(e)--(g); read their ``literal imports'' with the readings declared in A1, A3, A6 and A8,
and A7's row as the covariance of $K(g)$ and the parity of $H_0$ and, for even $\mathscr P$,
of $V(g)$. \S1's rate and gap are in working coordinates (general form: Remark~3.3). A third
edition waits for the author's decision on Phase~C.
```
- Rendered: "Notice of 23 November 2026. An audit of 9 November found the record described here (commit f213cc8) using its free-field layer (momentum field, free Hamiltonian, translations, parity, dilations) without stating it; since 11 November Appendix E supplies it, and the status sentence quoted in §§1 and 4 stands. The current record (23 November, 127 pages) restricts Corollary 12.3 (§§1, 2, 7, Fig. 1 here) to 𝒫(ξ) = ξ⁴ and cutoffs 0 ≤ g ≤ 1 in [3, (2.3)]; Theorem 12.2 is unchanged in substance. Statement numbers are unchanged; cited pages are up to seven too early. §4's table and Fig. 1 predate A1(e)–(g); read their "literal imports" with the readings declared in A1, A3, A6 and A8, and A7's row as the covariance of K(g) and the parity of H₀ and, for even 𝒫, of V(g). §1's rate and gap are in working coordinates (general form: Remark 3.3). A third edition waits for the author's decision on Phase C."
- 161 words in nine lines, as before (previously 156 words in nine lines). [3] is GJ3 in the companion's list.
- Each clause rests on these claims:
  - free-field audit and Appendix E: claims 2–4 of section 2, and claim 4 here;
  - "without stating it": the root README's own summary ("used without being stated"), see the README's free-field paragraph;
  - Corollary 12.3: claims 2 and 11 here;
  - Theorem 12.2: claim 3;
  - numbers and pages: claim 5;
  - readings: claims 7–9 here, and claim 9 of section 2;
  - A7: claim 9 here, and claim 10 of section 2;
  - working coordinates: claim 10.
- (c) I dropped the clause on the record of 11 November (125 pages, published 21 November). The notice now names the record described (commit f213cc8) and "the current record (23 November, 127 pages)".
- To stay at nine lines I also made these changes:
  - "the momentum field, the free Hamiltonian and the action of translations, parity and dilations without defining, deriving or importing them" became "its free-field layer (momentum field, free Hamiltonian, translations, parity, dilations) without stating it";
  - "in the Scope paragraphs of" became "in";
  - "(the record's §2.6; general form: …)" became "(general form: …)".
- The list of places where the companion cites Corollary 12.3 adds Fig. 1, which the follow-up's list omitted (claim 11).
- Wordings I tried and rejected:
  - eleven-line versions with the 11 November clause;
  - a ten-line version with "the record described here is that of commit f213cc8";
  - "symmetry actions", rejected because dilations change the mass and are not a symmetry of one model.
  Each of these gave 21 pages or was inexact.

**3. `companion/companion.tex` header comment.**
- Before: "... three kerns), so that pp. 2-20 keep their layout."
- After: "... three kerns), so that pp. 2-20 keep their layout; on % p. 20 only the MMST entry differs (bib.tex regenerated on 23 November 2026)."
- The edition date (`\date{7 November 2026}`), the epoch (1794009600) and the p. 1 typography are unchanged.

**4. `companion/council/README.md`.**
- 11 November paragraph.
  - Before: "Since 11 November the record has 125 pages;"
  - After: "From 11 to 23 November the record had 125 pages;" (now false otherwise).
- The paragraph "*23 November 2026, dated notice.*" is rewritten. Full text in `<scratch>/c2/reports/public-texts.diff`. It now says:
  - the notice has 161 words and nine lines, and was rewritten after the record's second pass;
  - the new clauses: Corollary 12.3 restricted, stated without restriction in §§1, 2, 7 and Fig. 1; Theorem 12.2 unchanged in substance; up to seven pages, from the 0–7 shifts;
  - the bibliography was regenerated by `make_bib.py`, and only MMST changed (pages 299–360 for 1299–1367, plus its arXiv number);
  - pp. 2–19 are those of 7 November, and p. 20 differs only in the last line of the MMST entry;
  - the edition, its date, its epoch and [R] are unchanged;
  - no agent that did not write the notice has checked it yet.

**5. `README.md`, the companion row (one row, l. 207 of the working tree).**
- Before: "... statement numbers are unchanged since, its page numbers are those of that build, and only a dated notice of 23 November 2026 in the box on its first page mentions Appendix E |"
- After: "... statement numbers are unchanged since and its page numbers are those of that build. Only a dated notice of 23 November 2026 in the box on its first page mentions Appendix E and that the record of that date restricts Corollary 12.3, which the companion states without restriction, to P(ξ) = ξ⁴ and to cutoffs 0 ≤ g ≤ 1 of GJ3 |"
- I re-read the README first: it had changed at 13:33 (the orchestrator's l. 71). Nothing else in the README was touched.

**6. `part_i/C5_reading_record.md`.**
- The A8 sentence (ll. 28–32).
  - Before: "Assumption A8 is unchanged in the version of 11 November 2026 (Appendix E)."
  - After: "Assumption A8 is unchanged in the version of 11 November 2026 (Appendix E); in the version of 23 November 2026 only the opening of its Scope paragraph is reworded (the sentence on Theorem 1.1.8, pp. 595 and 597, now also citing p. 629, and the sentence on a stricter standard), and no item (i)–(viii) and no point (a)–(d) of the Scope changed."
  - Verified: claim 7.
- Item 7, the reason sentence of the 23 November sub-item.
  - Before: "... (`main.tex` §2.1), and Assumption A1, Scope, records that the identification of the sources' V(g), defined by normal ordering in Fock space, with the record's V(g) is not proved in the manuscript and remains a reading."
  - After: "... (`main.tex` §2.1), and Assumption A1, Scope, records that the printed μ⁻¹ is literally 2C and that reading it as the inner product 2⟨f, Cg⟩ of ℋ_C is a reading not proved in the manuscript (since 23 November 2026), and that the identification of the Fock-space sources' V(g), defined by normal ordering, with the record's V(g) is not proved in the manuscript and remains a reading."
  - Verified: claim 8. "Fock-space sources'" follows the record's new attribution: GJS works in Q-space; GJ2, GJ71 and Rosen70 work in Fock space.
  - Every verdict field is still blank.

### F.4 Findings

- **G1 (MINOR; three of my first-task sentences, now false; outside this follow-up's scope).**
  - The loci:
    - `README.md` ll. 257–262, "its index … shows 54 of its 95 images and none of the pages added since 31 October 2026, which are listed in the Dossier line of each assumption in `part_i/main.tex` and in the "Dossier map" at the end of `part_i/README.md`";
    - `docs/provenance.md` l. 22, the same sentence;
    - `docs/provenance.md` ll. 103–106, "its page images behind the imports are listed in the Dossier line … and in the "Dossier map" …".
  - Why they fail: the folder now holds 97 images, and the two added today for A5(ii) are not in the Dossier map (claim 12).
  - Repair:
    - add `simon-semibounded-163, simon-hg-168` to the A5 row of the Dossier map (`part_i/README.md` l. 600), which makes the three sentences true again for the listing;
    - change "95" to "97" in `README.md` l. 258 and `docs/provenance.md` l. 22.
  - If the map is not updated, write instead "listed in the Dossier line of each assumption in `part_i/main.tex` (and, up to 11 November, in the Dossier map …)".
- **G2 (note).**
  - The companion's box of Theorem 12.2 quotes the record of 7 November verbatim (`s1-result.tex` ll. 62–63: "contain the finite, unevaluated constant S₂(B₃ₓ₅) of Theorem C.5"). The record of 23 November rewords that sentence (claim 3).
  - The notice's "unchanged in substance" covers this, and the body is not touched.
- **G3 (for the orchestrator; not my loci).** Sentences that the 127-page record makes stale:
  - `README.md` ll. 60, 64, 205 and 292 ("125 pages", "125 pp") and ll. 305, 309 (epoch 1794355200, "11 November 2026"); the record now uses 1795392000 (`main.tex` l. 81);
  - `docs/status.md` l. 47 ("The record has 125 pages"), l. 62 ("since 11 November 2026 it has 125"), the gate row GF at l. 84 and l. 90 ("for the 125 pages");
  - `part_i/README.md` l. 590 (reported this morning).
- **G4 (for the orchestrator).** `companion/PLAN.md` does not record the notice or the regeneration of `bib.tex`. It was outside both scopes.
- **G5 (note on the diff).** The prescribed `git diff -- . ':!part_i/main.tex' ':!part_i/main.pdf' ':!companion/companion.pdf'` now also contains other agents' changes:
  - `CITATION.cff`, `docs/imports.md` and `docs/index.md`, all at 13:33;
  - the README hunk at l. 71.
  - All other hunks are mine.
  - `docs/status.md` and `docs/provenance.md` carry only my hunks (mtimes 13:19 and 13:22).

### F.5 Checks run, with output

- **`make_bib.py`.**
  - Scratch copy against the current `main.tex`: the diff is MMST l. 72 only.
  - In the repository: the same output and the same diff; `git diff --stat -- companion/bib.tex`: 1 insertion, 1 deletion.
- **Notice trials** (scratch, build of the current companion with the candidate notice; pass condition: "Abstract" at y = 400.3, i.e. nine lines):
  - N2a, N2b: 11 lines, 21 pages;
  - N6, N7: 10 lines, 21 pages;
  - N5, N8, N9: nine lines, 20 pages, only p. 20 differing from the committed PDF;
  - N8 is the final text.
- **Repository build.** Three passes of `SOURCE_DATE_EPOCH=1794009600 FORCE_SOURCE_DATE=1 /Library/TeX/texbin/pdflatex -interaction=nonstopmode companion.tex` in `companion/`, run twice (after the notice, and after the comment edit):
  - exit codes 0, 0, 0;
  - `grep -cE '^!'` → 0; `grep -c Overfull` → 0; `grep -icE undefined` → 0; `grep -c Underfull` → 0;
  - `pdftotext | grep -nE '\?\?|TODO|Hmm|wait,'` → nothing;
  - Pages 20; CreationDate Sat Nov 7 01:00:00 2026 CET; `pdfimages -list`: 0 images.
- **`shasum -a 256 companion/companion.pdf`** → `a560cc2700706ab235b206126ce80add436e84c766c33493d5e2b055f7cf2a29`. It is the same after both repository builds and from a clean scratch build (aux removed, three passes).
- **Against the committed PDF of 7 November** (`1aeab355…53aa`):
  - `pdftotext -layout`: pp. 2–19 identical. On p. 20 one line differs: "(2021) 1299–1367." → "(2021) 299–360; arXiv:2010.11121."
  - `pdftoppm -r 72` with PIL: pp. 2–19 pixel-identical; p. 20 differs only inside the box x 354–464 pt, y 607–616 pt, which is that line of [16] in the right column; no reflow.
- **p. 1 positions** (pdftotext -bbox):
  - title top y = 87.9 pt, inside the text block (85.04 pt);
  - "Read" 227.6, "Notice" 285.4, "Abstract" 400.3, "How to read" 559.9, §1 heading 630.6;
  - the last line is "… (coupling λ, C-Wick", unchanged.
- **Renders.** p. 1 at 100 dpi, the box at 200 dpi, and p. 20 at 100 dpi, all looked at:
  - the notice is legible, inside the box and the margins;
  - p. 20: [16] reads "Comm. Math. Phys. 387 (2021) 299–360; arXiv:2010.11121." on its old lines, [R] still reads "110 pp., version of 7 November 2026", and the page is not crowded.
- **Label shifts:** see claim 5.
- **Environment diffs:** see claims 2, 3, 7, 8 and 9.
- **Masked diff:** 0 machine paths (`grep`); the exact diff contains the 9 removed lines, as before.

### F.6 Not done, not verified, not run

- **Not done:**
  - G1 (outside the follow-up's scope);
  - G3 and G4 (not my files);
  - [R] (unchanged, as accepted).
- **Not verified:**
  - Whether the independent re-check running now changes `main.tex` again. If it does, re-check the notice's "127 pages", "up to seven" and the Corollary 12.3 clause against the final build.
  - That a third edition waits for the author's decision on Phase C (as before).
- **Not run:**
  - an independent check of the rewritten notice by an agent that did not write it;
  - a site build;
  - `docs/extract.py --check`.

### F.7 Files written in this follow-up

- `companion/bib.tex` (by `make_bib.py`)
- `companion/companion.tex`
- `companion/companion.pdf`, and the untracked `companion/companion.{aux,log,out}`
- `companion/council/README.md`
- `README.md` (the companion row only)
- `part_i/C5_reading_record.md` (the A8 sentence and the item-7 sentence)
- Outside the repository:
  - `<scratch>/c2/reports/public-texts.diff` (overwritten, 474 lines, 17 files; see G5)
  - `<scratch>/c2/reports/public-texts.masked.diff` (overwritten)
  - this section, appended to `<scratch>/c2/reports/public-texts.md`
