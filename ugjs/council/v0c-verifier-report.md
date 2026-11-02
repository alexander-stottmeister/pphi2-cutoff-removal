# V0c: re-check of the V0b repairs (fresh verifier), 2 November 2026

**Scope and method.**
- I read the files on disk only. I ran no git and no kb command, and wrote only this file.
- main.tex was diffed against my V0b copy of it (`<scratchpad>/v0b/build/main.tex`, taken on
  31 October).
- The only GJS quotations that moved in this round are the merged C5 item 13 (pp. 600 and
  628). I re-checked them against the text layer of the paper in `refs/` (sha256 prefix
  `e0a08c9438ff5c69f6d5`, 1,362,944 bytes). That is the same file as the scratchpad copy used
  in V0, which no longer exists. They also match the images read in V0b (`gjs74/p-17.png`,
  `p-45.png`, still present). No other GJS quotation changed.
- Line numbers below are those of the current files.

## Verdicts

| item | verdict | evidence |
|---|---|---|
| N2 (Scope (d)(i)) | **fixed** | main.tex l. 888–889: "the only class of space-time cutoffs $h$ of the measures $dq_h$ that the source defines". This is true: p. 589 defines h, and p. 588's class is for g. The regenerated `docs/results.md` l. 832 matches. |
| N1 (C5 counts) | **fixed** | C5 has 13 items and 13 verdict fields. Header l. 28: "Items 1–4, 9, 12 and 13 carry the imports". Item 13 merges p. 600 and p. 628, with both quotations verbatim. Closing: "All thirteen `MATCHES` (items 1–13)". These agree with: strategy.md l. 2525; main.tex External residue l. 2756–2762; docs/status.md l. 66 and 71–76; the E3 line of part_i/README.md (l. 439); README l. 43–44 and 53; docs/imports.md l. 28–29; companion §4 l. 72–73 ("its thirteen items (nine before 31 October 2026)"). No "13b" or "fourteen" remains except one historical mention in the gate record. |
| M5 (a), the nine boxes | **fixed** | My 3-pass rebuild with epoch 1793404800 is byte-identical to `part_i/main.pdf` (sha256 `4c37f0272c8341e2`): 0 errors, 0 undefined, **0 Overfull**, 5 Underfull, 42 pages; the PDF text scan finds no `??` or TODO. All 125 labels keep their number **and page** against my V0b build. Their numbers are also identical to `main.aux.baseline`. |
| M5 (a), no mathematics changed | **confirmed** | The diff against the V0b copy touches only: two words in the §1.2 sentence and `\small`→`\footnotesize`; A4 "Sources" wording; "↦"→"to" in (viii); "$F_1,F_2$"→"$F_1$ and $F_2$"; the Corollary 12.3 align split after its second "=", with the same three expressions; `\tabcolsep` in Appendix A; four spacing commands (`\,` ×3 and `\;+\;`→`+`) in the M5 display, with the same terms. No quotation was touched. |
| M5 (a), legibility | **confirmed** | p. 4 rendered at 110 dpi: the footnote-size graph is legible and reads exactly as in V0b. pp. 33 and 38 (split align; M5 display) render correctly. |
| M5 (b), five V0 MINOR items | **fixed** | m10: F-0′ now opens README l. 20, docs/status.md l. 12 and docs/imports.md l. 7. m12: C5 item 9(b) "i. e.,", 9(d) "e^{−γT}, uniformly in h". m13: item 2 is in the closing mapping. m14: the CITATION.cff abstract names (1.1.16) at B = I, n = 0, 0 < T < 1. m16: README l. 237–238. |
| M5 (c), gate record | **not fixed: new defect, MAJOR** | See G below. |
| n1 | fixed | l. 736: the spurious "[\dots]" is gone; the second one, before Theorem 1.1.11, stays. |
| n2 | fixed | l. 865: "Four points of scope are recorded." |
| n3 | fixed | C5 item 6 sites: "Scope paragraph points (a) and (d), Remark C.6 (via Source Fact 2.4)". All three are accurate. |
| n4 | fixed | main.tex l. 908–909 and the part_i/README.md dossier map, A8 row (l. 801), list `gjs-thm41-45` (p. 628). That image exists and is byte-identical to the p. 628 render. |
| n5 | fixed | ugjs/council/README.md l. 9 points to the gate record and to strategy.md, and explains PLAN.md's "Nothing in it has been executed". Its target section currently exists twice (G). |
| n6 | fixed | s4-import.tex l. 75–78: "(there ``pp.~598--629''; the argument runs to p.~631)" matches the committed docs/imports.md; "proposed others: the re-sourcing, applied, and a comparison argument, conjectured". The companion was rebuilt: 20 pages, log 0/0/0/0, sha256 `11b4ddbc12f6d5c7`. |
| n7 | fixed | affine-path.html l. 26–32: the 5 September reading, with the corroboration status since 31 October. |
| n8 | fixed | docs/status.md l. 66–76: the duplicate is gone. |

**Checks also re-run:**
- `grep -c 'Assume \$U_{\rm GJS}'` gives 0, and `grep -n -i 'assum[a-z]*[^.]*U_{\rm GJS}'`
  prints nothing.
- `python3 docs/extract.py --check` prints "up to date" and leaves `results.*` untouched
  (61 statements, 29 import A8, 23 cite U_GJS).
- Both SVGs still carry the new legend.

## G (MAJOR, new): `part_i/README.md` is corrupted, and the gate record contradicts itself

The file grew from 33,867 bytes (V0b) to 57,591 bytes (801 lines). Its sections from "Publication preparation
(2026-09-20)" through "Forbidden strings" now occur twice: l. 159–419 and again l. 481–741.
So does the heading "Re-sourcing of A8(vi) and documentation repairs (2026-10-31)", at l. 420
and at l. 742.

The two 31 October sections disagree:
- **First section, l. 448–468.** "0 Overfull … Round V0c: pending".
- **Directly after it, l. 469–479.** The three closing bullets of the 5 September section
  (already at l. 147–157) appear again: "C5 extended … items 8 … and 9", "Build … 40 pp (was
  38)" and "Not done … GJS pp. 598–629". They now read as part of the 31 October gate record.
- **Second section, l. 742–788.** This is the stale V0b-era text: l. 773 "G-0's "0 Overfull" is
  therefore **not met**"; l. 781 "every item applied before the commit".
- **What is lost.** The 31 October "C5 extended" bullet ("items 10–13 added (… pp. 600 and
  628)") and the "Record elsewhere" bullet survive only inside that stale copy (l. 783–788).

**Repair.**
1. Keep l. 1–468.
2. Follow them with the 31 October "C5 extended" and "Record elsewhere" bullets (now
   l. 783–788).
3. Then the dossier map (l. 790–801).
4. Delete l. 469–479 and l. 481–782.
5. Diff against the committed file to confirm that only the 31 October section and the A8 row
   of the dossier map differ.

## MINOR (new, optional)

- **docs/status.md l. 12 and docs/imports.md l. 7.** F-0′ now carries "proved" there, but the
  open readings are named only at l. 25–26 and l. 28–29. Part 7 asks for them "beside" the
  word. Add "(open human readings: C5 items 1–4 and 9–13)" after F-0′, as README l. 19–20
  already does in effect.
- **docs/status.md l. 12.** "It is proved as an *implication* from the imports A1–A8 enumerated
  in §2.4, not a proof of those imports." reads as if the theorem were "not a proof". Suggested:
  "The proof is an implication from …; it is not a proof of those imports."
- **strategy.md l. 2527.** "(G-0 now met)" is written before G-0's fresh-reader item (this
  round) is recorded. Say "G-0's build conditions now met", or update it after recording V0c.

## Not checked

- The KB, and the author's Checkpoint-1 words.
- Rendered pages other than pp. 4, 33 and 38 of the current build. The other changes of the
  layout pass are text-only, and I read them in the diff.
- `docs/index.md` and the interactive pages other than affine-path.html. They are unchanged
  since V0b, by mtime.
- The rendered website.

**Not yet.** One blocking item remains: repair `part_i/README.md` (G) — remove the duplicated
block and the stale second 31 October section, and keep the updated gate record. With that done
and the V0c line recorded in the gate record, nothing else found here blocks the commit.

---

## V0d: confirmation of the repair, 2 November 2026

**Method.** I read the files on disk only. I ran no git and no kb command, and wrote nothing
except this section.

**What changed since V0c.** Only four files, all at 15:50: `part_i/README.md`, `README.md`,
`docs/status.md` and `docs/imports.md`. Everything else is as I verified it in V0c:
- `part_i/main.tex` is byte-identical to my V0c copy;
- `main.pdf` sha256 begins `4c37f0272c8341e2` and `companion.pdf` sha256 begins
  `11b4ddbc12f6d5c7`, the files rebuilt byte-identically in V0c;
- the companion sources, the C5 record, CITATION.cff, `docs/index.md`, `docs/results.*` and
  strategy.md have unchanged mtimes.

**G (the corruption of `part_i/README.md`): repaired.**
- The file now has 495 lines and every heading occurs once, in the original order. The
  31 October section is at l. 420 and the dossier map at l. 484. No line longer than 70
  characters occurs twice.
- I compared the restored text with the copies of the corrupted file that I saved in V0c:
  - l. 159–419 equal the corrupted first copy, and also the second copy (the two were exact
    duplicates);
  - l. 420–467 equal the corrupted l. 420–467;
  - l. 477–482 equal the corrupted l. 783–788 (the 31 October "C5 extended" and "Record
    elsewhere" bullets).
- The 5 September bullets now occur only in their own section (l. 147–157).
- The stale second gate record ("not met"; "every item applied before the commit") is gone.
- The gate record (l. 448–476) now records rounds V0, V0b and V0c, and ends "Round V0d
  (confirmation of the repair): pending".
- **Not checked:** the diff against the committed file. I have no copy of it, and git was
  excluded.

**The three optional MINOR items:**
- **Readings named beside F-0′: applied.** F-0′ is now followed directly by "The human page
  readings of audit item C5 (items 1–4 and 9–13) are open." at README.md l. 20,
  docs/status.md l. 12 and docs/imports.md l. 7.
- **The "implication" sentence: applied.** docs/status.md l. 12 now reads "It is an
  *implication* from the imports A1–A8 enumerated in §2.4; the record is not a proof of those
  imports."
- **strategy.md's "(G-0 now met)": kept, and accepted.** With this round recorded, G-0's last
  item (the fresh reader) is met: 0 errors, 0 undefined and 0 Overfull, no `??`, the changed
  pages inspected, the 125 labels unmoved, and the changed sentences checked against the page
  images.

**One wording fix, not blocking.** The gate record's V0c sentence (l. 474–476) says "its three
optional MINOR items applied" but names two. The third, strategy.md's "G-0 now met", was kept.
Write "two of its three optional MINOR items applied (…); the third kept" when the V0d line
replaces "pending".

**Final word: commit.** Before committing, replace "Round V0d (confirmation of the repair):
pending" in the gate record with this verdict, and correct the wording noted above in the same
edit.
