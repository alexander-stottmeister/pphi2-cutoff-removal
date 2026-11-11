# Check of the documentation unit of 11 November 2026 before its commit

One agent (general-purpose, model claude-opus-5-5) that had written none of the checked text, read-only. It checked the uncommitted working tree of 11 November 2026 (the site fix in `docs/extract.py`, the notice of 11 November, the corrections of stale public text, the new record entries and the archived reports) against `part_i/main.tex`, the page images, the archived reports and GitHub. Its findings F-a to F-p were applied before the commit; the line numbers in it refer to the working tree as it was when it ran.

Returned by the agent as a message, not as a file. Saved here on 11 November 2026 by the orchestrator from the session transcript. The text is verbatim except that paths under the home directory and under the session's temporary folder are replaced: `<scratch>/` is that temporary folder, which was emptied on 10 November 2026, and paths inside this repository are written relative to its root.

---

## Report (returned 2026-11-11)

## Outcome
The site fix works: the regenerated `docs/results.md` and the other six rendered pages parse under Liquid 4.0.4, and the HEAD version still fails with the deployed error. The text, however, has one public overstatement about A1–A7, one misleading dating of the gap, one imprecise "neither … imports" for item 4, and stale page numbers on six figure pages, which the records say were all corrected. I wrote nothing in the repository. Scratch copies are in `<scratch>/` (`clone/`, `wt/`, `old_main.tex`, `results_head.md`).

## 1. Findings, most serious first

**F-a. MAJOR: `docs/imports.md` contradicts the notice, and the notice cannot be reached from it.** This file is not in the diff.
- l.7 still says: "Theorem 12.2 is proved from printed statements only, with one GJS theorem imported …". It has no notice and no link to status; its only link goes to results.md.
- l.20 says: "A1–A7 are literal quotations of printed statements". This is false against the record. A1's Scope (main.tex ll.681–684) and A6's Scope (ll.901–904) both declare a "reading" (the Fock space–Q-space dictionary).
- The A7 row says "translation covariance and parity". That contradicts notice items 2–3: A7, ll.922–929, imports only U_aK(g)U_a* = K(τ_a g), ΘH₀Θ = H₀ and ΘVΘ = V.
- Fix: add the notice line and link (as in `docs/index.md`); replace "literal quotations" with "printed statements, A1 and A6 under the declared Fock–Q-space reading"; change the A7 row to "covariance of K(g) under U_a; parity of H₀ and V(g)".

**F-b. MAJOR: "items 2 to 4 are older than the integration of 7 November"** (`README.md` notice, `docs/status.md` notice). The same point appears as "F4, F6 and F7 are in commit 910959d already" (`part_i/README.md`, Finding 3) and "three of the four MAJOR findings are older than the integration" (`strategy.md`, Finding 3).
- In `git show 910959d:part_i/main.tex`, item 1's gap is already there. l.379 uses `W(f,h)=\exp i(\varphi_0(f)+\pi_0(h))` with π₀ never defined. l.395 uses `K(g):=H_0+V(g)`, and H₀ is defined nowhere in that file either.
- Only the sentence that tries to define π₀ (ll.431–433) is new on 7 November. As written, the text suggests the integration introduced item 1, when that edit only exposed an older gap.
- Fix: "all four gaps predate the integration; the sentence of 7 November that introduces π₀ (§2.1) did not close the first" (and the same in `part_i/README.md` and `strategy.md`).

**F-c. MAJOR: notice item 4, "neither defines, derives nor imports", leaves out an import.** Assumption A8(viii) (main.tex ll.1187–1189) imports "The unitary space-time dilation of [GJS, p. 590]".
- I read the page image `audit_2026/evidence/gjs-scaling-07.png`. It prints "a unitary scaling transformation on L₂(S′(R²), dΦ) carries Φ(x,m₀)→Φ(sx,s⁻¹m₀) and V(λ,m₀)→V(s⁻²λ,s⁻¹m₀)". This is a Euclidean statement. It does not give the time-zero U_s of Remark 3.3, with U_sΩ₀ = Ω₀, its action on π₀, or U_sH₀U_s* = sH₀.
- Item 4 is therefore defensible, but a reader who checks will find a dilation import. Neither the notice nor V4f (`ugjs/council/v4f-free-field-report.md`, which never mentions A8(viii)) says why it does not cover U_s.
- Fix: add to item 4 "(A8(viii) imports GJS's Euclidean scaling on L²(S′(ℝ²)); the time-zero unitary U_s and its action on π₀, H₀ and the Fock vacuum are not imported)".

**F-d. MAJOR: records say the stale public text was all corrected, but six figure pages still carry August page numbers.** The claim is in `part_i/README.md`, Finding 2 ("All corrected on 11 November"), and `strategy.md`, Finding 2. The page subtitles still read:

| file:line | page shown | page in `main.aux` |
|---|---|---|
| `docs/interactive/plateau.html:8` | page 6 | 8 (def:classes) |
| `docs/interactive/weak-coupling.html:8` | page 13 | 21 (prop:scaling) |
| `docs/interactive/uniform-gap.html:8` | page 21 | 30 (thm:G) |
| `docs/interactive/rate.html:8–9` | p. 24, p. 28 | 32, 36 (lem:filter, lem:rate) |
| `docs/interactive/two-regime.html:8` | page 27 | 35 (lem:tworegime) |
| `docs/interactive/dichotomy.html:8` | page 31 | 40 (thm:dichotomy) |

Fix: correct the six subtitles, or soften "All corrected".

**F-e. MAJOR: S1 row (`part_i/README.md`, new table): "(P) does not rest on that page" is unsupported.**
- The page image `gj2-cutoff-independence-38.png` (GJ2 p.398) does print "provided that g(y)=λ for |x−y|>|t|", so the reported ">" misprint is confirmed.
- But the record's A6, which states (P), lists "[§§3.5–3.6]{GJ2}" among its Sources and `gj2-cutoff-independence-38` (E06) in its Dossier (main.tex ll.890, 917–919). The second clause of (P) is exactly this cutoff-independence statement.
- Fix: delete that sentence, or say "the dossier names this page for A6 as well as A7; whether (P) depends on it is not checked".

**F-f. MINOR: the location of "no other external input is used" is wrong** (`README.md` notice, `docs/status.md` notice).
- The text says "(§2 and Theorem 12.2)". The first sentence is at main.tex l.421, before `\section{Setting…}` at l.425, so it is in §1 (Introduction, "Provenance and relation to the frozen sources").
- It also reads "no other external *mathematical* input is used". `part_i/README.md` quotes both sentences correctly, with ll.421–422 and 2879–2880.
- Fix: "(§1 and Theorem 12.2)".

**F-g. MINOR: section mislabelled** (`part_i/README.md`, F4 row). "The standing assumption of §3 (ll. 1350–1354)": those lines are in §2.6 (`subsec:weak` = 2.6, p.20; §3 starts at l.1358). Fix: "§2.6".

**F-h. MINOR: "conditional on these four facts"** (`README.md`, `docs/status.md`, `strategy.md`). Item 1 is a missing definition (π₀, H₀), not a fact, so until it is supplied the objects A(O) in the theorem's statement are not specified. Suggested wording: "conditional on the standard definitions of π₀ and H₀ and on three properties of the free field".

**F-i. MINOR: "only for pairs (m₀, λ) that satisfy the printed GJS hypotheses themselves" is vaguer than the record.** The record's form (§2.6, ll.1350–1354) is "(m₀=M_* and λ<λ_*)". GJS print only "m₀ … sufficiently large, λ sufficiently small" (p.594), so the set is not otherwise defined. Fix: append "(m₀ = M_*, λ < λ_*, §2.6)".

**F-j. MINOR: other public text without the notice.**
- `docs/_config.yml:5`: the site description used in the page meta tags is the unqualified status sentence.
- `README.md:329–333` ("Citing") asks readers to cite the theorem as an implication from A1–A8 but omits the new request that CITATION.cff now makes.
- `docs/definitions.md:11–25` presents π₀ and W(f,h) as defined, with no notice.
- The repository's About text (from `gh repo view`) still reads "Main theorem conditional on the imported U_GJS interface". The records already list this as waiting for the author.

**F-k. MINOR: `docs/status.md` GI row says "audit rounds V4–V4e".** The GI record (`part_i/README.md` l.500) says "G6 = rounds V4 and V4b". Align the two.

**F-l. MINOR: "a display".** `strategy.md` Finding 1 says "the two opening braces of a display in A1's Wick-powers paragraph"; `part_i/README.md` says the same. The text is inline math, `$\{{:}\phi(f_1)…$` (main.tex, item (c), l.~628). Fix: "a formula".

**F-m. MINOR: `liquid_hazards()` has limits.** All of them are on the fail-safe side except the last two, which are misses.
- A raw block that is opened and never closed is not reported, although Liquid raises an error for it. Tested: `'{% raw %}\n{{ never closed'` returns no hazard.
- It scans files that Jekyll does not render (`docs/PLAN.md`, which `_config.yml` excludes), so it can report false positives.
- It treats any file starting with `---` as front matter.
- It ignores rendered file types other than .md and .html (for example .xml, .css or .txt with front matter). None exist in `docs/` today.
- Suggested fix: report `raw` still open at end of file, and skip paths listed under `exclude`.

**F-n. MINOR: archive headers say machine paths were replaced, but some remain.** The headers say "absolute paths of the machine are replaced". Generic system paths are still there: `/Library/TeX/texbin/pdflatex` (`v4-math-report.md` ll.186, 288, 376, 444, 511), `/usr/local/bin/python3` (l.194), and `/usr/bin/grep` (`v4f-free-field-report.md` ll.75–76). None of them is personal. Fix: "paths under the home directory and the session's temporary folder are replaced".

**F-o. MINOR: `ugjs/council/README.md` V4f paragraph says "the gate record lists them with what was confirmed".** The table in `part_i/README.md` lists the findings with their severity, but says nothing per finding about what was confirmed.

**F-p. MINOR (cosmetic): `docs/index.md`.** The notice joins the preceding blockquote paragraph (no blank `>` line between them), and "See [status](status.md)." now appears twice in a row.

## 2. Checked and found correct
- **Notice items 1–3 against `main.tex`:**
  - π₀ is introduced only by reference to A1's dictionary (ll.431–433), and that dictionary covers V(g) only (ll.681–684).
  - H₀ is first used at l.513 and never defined. Searches for H_0, `\pi_0`, momentum, `\pi(`, implement and Ad U_a over the whole file, appendices included, find no definition. A2 and A4 use the free semigroup only implicitly.
  - τ_a is defined on functions only (l.923; l.4475 is the ℝ² case). It is used on operators at ll.2895–2897, 2988 and 3001–3002.
  - Θπ₀Θ = −π₀ is used at ll.2900–2902 and justified nowhere.
  - U_s is asserted at ll.1459–1465.
  - Theorem 13.2's use of translation (Steps 1, 2 and 4) and of parity (through 12.2(3)–(4) in Step 3) is as described.
- **Line numbers of every F-table row** (F1–F10, S1) in `part_i/README.md`, apart from F-g.
- **V4f report:** 4 MAJOR and 6 MINOR. The table's severities, loci and "checked and correct" list match it.
- **Sources read on 9 November:** Simon p.24, Theorem I.11 (unitary D with DΩ₀ = 1) confirmed in the refs PDF, at PDF page 46. GJ2 p.398 confirmed from its page image: translation of φ and of a, a*, and no relation for π.
- **Companion sentences:** "proved from printed statements" is at companion.tex l.38 (abstract), `sections/s1-result.tex` l.72 and `sections/s4-import.tex` l.18.
- **Numbers and dates:**
  - `pdfinfo`: main.pdf 110 pages, companion.pdf 20 pages.
  - 1794009600 is Sat 7 Nov 2026 00:00 UTC; the comment at main.tex l.80 and the epoch at the top of companion.tex agree.
  - The dossier references 54 of the 85 images (system grep).
  - `aux:notation-squares` is N.1 (p.55); `app:constants` is A (p.42).
  - Appendix A no longer lists C₈.
  - All `docs/notation.md` rows match the record's table at ll.551–575.
- **Byte-for-byte rebuild:** three passes of HEAD with the pinned epoch, from a `git archive` copy, reproduce both PDFs. Hashes: main.pdf f1962e11…db41e, companion.pdf 1aeab355…53aa. Log counts: 0 errors, 0 Overfull, 0 undefined.
- **GitHub:**
  - Failed runs 42420438670 (231b8ea), 42462365937 (b79d2d8) and 42463067765 (f213cc8).
  - Last success 41927520564 (910959d, 4 Nov).
  - Log: "Liquid syntax error (line 425): Variable '{{:}' was not properly terminated …"; github-pages v232; liquid-4.0.4.
  - Line 429 of the HEAD results.md is item (c).
  - The status page at 910959d carries the status of 31 October.
- **Code:**
  - `python3 docs/extract.py --check` prints "up to date" and exits 0.
  - The Liquid 4.0.4 test passes all 8 `docs/*.md` (results.md "braces preserved"). The HEAD `results.md` fails with the deployed error word for word.
  - No HTML or asset file in `docs/` has front matter.
  - Regex cases checked: a raw tag and a delimiter on the same line, in both orders; `{%- raw -%}` / `{%- endraw -%}`; `{%raw%}`; doubled spaces.
  - The HTML-comment wrapping leaves empty `<!--  -->` comments, harmless for kramdown. jekyll-relative-links and titles-from-headings are unaffected, since the title is in front matter.
  - Running `extract.py`, `make_figures.py` and `make_labels.py` in a scratch copy of the working tree leaves it unchanged (SVGs and results files consistent; 65 statements, 230 labels, 34 reach A8).
- **Archives:**
  - No home-directory or `/private` paths, e-mail addresses, session URLs or UUIDs.
  - Part counts match the headers and READMEs: math 5 (V4, V4b–V4e), integration 2, V4f 1, R7 2, editor 3.
  - The "not checked" lists in `part_i/README.md` match the reports, apart from small omissions: the integration auditor's "comparison.tex notice, step maps, labels.md", and V4d's "edits outside R1–R4".
- **Links and dates:** 38 relative Markdown links in tracked plus new .md files, 0 unresolved. The section titles named in quotes exist. `ugjs/PLAN.md` was last changed on 30 Oct (git log). lem:cluster = 9.3, lem:tworegime = 10.3, cor:canonical = 12.3.

## 3. Not checked
- Whether the archives are verbatim copies of the transcripts.
- The guard self-test ("49 passed").
- The "74 relative links" count: my count, with a different method, is 38 with 0 unresolved.
- The orchestrator's hand re-derivation of Corollary 5.2's constant.
- GJ2 p.365.
- The mathematical truth of the four facts.
- A live Jekyll build: I parsed with Liquid only, not kramdown or the theme.
- The deployed site after a push.
- The KB.

Condition for the push: the five untracked reports must be in the same commit, because the README and status pages link to `ugjs/council/v4f-free-field-report.md`.
