# Route T change: documentation check (24 November 2026)

Checker "route-t-docs-check" of the working council of 23-24 November 2026 (an AI agent). I am read-only on the repository, and I wrote none of what I check. I do not audit the note's mathematics.

- **Object.** The uncommitted change on HEAD 9733263:
  - new: `ugjs/route_t/` (note, PDF, script, script output, README) and four reports `ugjs/council/route-t-*.md`;
  - modified: `ugjs/council/README.md` (ll. 142-153), `strategy.md` (ll. 2614-2620), `docs/status.md` (l. 161), `docs/imports.md` (l. 34) and `README.md` (l. 286).
- **Sources.**
  - The two audit reports, `ugjs/council/route-t-audit-analysis.md` and `route-t-audit-sources.md`.
  - The revision report `ugjs/council/route-t-revision-report.md`.
  - From the note: the first page (ll. 55-90), the Summary (ll. 92-133), §1.2 with T.2 (ll. 200-292), §§4-7 (ll. 1174-1879).
  - `part_i/main.tex` at HEAD 9733263. The working-tree file is identical: `cmp` against `git show 9733263:part_i/main.tex` prints nothing.
  - `part_i/main.tex` at 49f2d23, from the frozen copy.
- **Line numbers.** Note lines are those of the current `ugjs/route_t/route_t.tex` (1924 lines). Record lines are HEAD's unless marked 49f2d23.

## 1. Outcome

There is **one MAJOR finding**: what the note says it proves about Corollary 12.3.
- The note's first page (a sentence the orchestrator added) and `ugjs/route_t/README.md` present Route T as covering the corollary as stated at 49f2d23.
- HEAD's record calls that statement "CRITICAL for that statement as written", because its proof needs 0 ≤ g ≤ 1.
- Route T's argument goes through that same proof, so it gives only the restricted corollary.

There are **seven MINOR points and one cosmetic group** (D2-D9). The most consequential is D2: the question of the constant is missing wherever "reached" is used outside the note.

Everything else holds and is no stronger than its sources:
- the status words and the claims about P3 and P4, R1, pp. 595, 600 and 629, the rotation presupposition, T.19 and N.39;
- the A2 paragraph, against A2 and Lemma 4.1 at HEAD;
- the process claims, the page counts and "23 checks pass";
- the build: three passes reproduce `ugjs/route_t/route_t.pdf` byte for byte, with 33 pages, 0/0/0 and a clean grep.

All guards pass:
- no machine path or e-mail address in the added text;
- no Liquid delimiter;
- no raster image in the PDF;
- `extract.py --check` prints "up to date";
- `git add -n ugjs/route_t` takes exactly the five intended files, no by-products.

## 2. Claims checked

| # | claim (locus) | checked against | verdict |
|---|---|---|---|
| 1 | "`route_t.tex` (33 pages)" (README l. 3; also the council README l. 144, strategy.md l. 2616, docs l. 161 / l. 34, README.md l. 286) | `pdfinfo`, and my rebuild | holds: 33 |
| 2 | Commissioned by the author on 23 Nov, after the status council of 22 Nov proposed Route T as the content of C3 (README ll. 3-4); "from the sketch of the status council's constructive-QFT member" (strategy.md l. 2616) | the council brief (item 3, "authorised"); the 22 Nov council record: `SYNTHESIS.md` l. 55 ("Route T note (Phase C, C3 content)") and `memo-cqft.md` row 9 ("My sketch below; steps (a)–(d)") | holds ("commissioned" stands for the brief's "authorised", as the analysis auditor noted in its §10.4) |
| 3 | Written by "an AI agent (Claude Opus)" (README l. 4); "an Opus agent", "Two fresh Opus agents" (strategy.md l. 2616) | the note says "Claude" (ll. 57, 67); no report names a model (grep for "Opus") | **not verified** |
| 4 | Audited the same day by two agents that wrote none of it; revised; re-checked by both; revised again for the re-checks' MINOR points; confirmed by one of them on 24 Nov (README ll. 5-7; council README ll. 149-150; strategy.md l. 2616) | analysis audit header, §§9 and 10; sources audit header and its re-check; revision report, "Second round" | holds. The analysis auditor states "I wrote nothing of the note" (§9.4). The sources report calls both agents independent. The confirmation's checks "ran between 23:48 on 23 November and 00:02 on 24 November 2026" (§10). |
| 5 | Not integrated; `part_i/main.tex` and its Theorem 12.2 unchanged by it (README ll. 7-8; first page ll. 81-82) | `git status`: no `part_i/` path in the change; diff of the Theorem 12.2 block, 49f2d23 against HEAD | holds. The block differs only in one sentence of the imports paragraph, and the corollary title has changed. |
| 6 | "Not read by a human" (README l. 7; first page l. 80; council README l. 144; strategy.md l. 2620; docs) | — | **not verifiable**; consistent with the brief |
| 7 | T.2 "proved, conditional on" A1–A8 and the declared readings, by the two audits; items (1)–(4) and Cor. 12.3 with the same state and a new rate decaying faster than every inverse power; without Thm 5.1, Thm D.4 and A8(iv)-T (README ll. 12-16; strategy.md l. 2618) | T.2 (`thm:routeT`, T.2, p. 5, ll. 251-267) and its status (ll. 285-292); the analysis audit's final line (§10); the sources audit's re-check §10 | (1)–(4) hold. **Cor. 12.3: D1 (MAJOR).** The conditions list is incomplete: D6. |
| 8 | M replaced by a resolvent-weighted quantity, bounded through a time-integrated copy of D.4 (README ll. 16-17) | Summary ll. 97-102; T.1, T.14, T.16 | holds |
| 9 | "No input beyond the record's imports is added" (README ll. 17-18; strategy.md l. 2618) | analysis audit §9.5, R1 ("'adds no input' stands"); sources audit re-check §§1, 3, 10 | holds |
| 10 | The added applications pair two time-integrated monomials (P3, P4) and lie within the printed statement (README ll. 20-22; strategy.md; docs) | T.2(c) (ll. 261-265); §5.2 table (ll. 1285-1303); sources audit §1, rows A1-A4 | holds |
| 11 | The printed proof reaches them only if p. 596 is read as R1; R1 is the reading under which GJS's own proofs are complete (pp. 595, 600, 629); no printed sentence states it; for P4 the rotation covariance is presupposed; "exchanges a case that no reading … reaches for cases reached on that reading" (README ll. 22-26; strategy.md; docs) | §5.3 (ll. 1308-1352); T.17 and its status (ll. 1432-1449); §5.5 (ll. 1600-1653); sources audit re-check §10, including its "In one line" | holds in the note's sense of "reached". The third remaining question is missing: **D2**. The words "observable A": D9. |
| 12 | Moment clause of (5), Thm 5.1 and Cor. 5.2 still rest on A8(iv)-T (README ll. 27-28; strategy.md; docs) | §7.2 (ll. 1809-1811); §7.3 (ll. 1823-1824); sources audit, row D7 | holds |
| 13 | T.19 settles Remark N.39's question; the parallel pairs behind the gap are reached after slicing, on either reading (README ll. 28-30; strategy.md) | T.19 and its status (ll. 1664-1693); ll. 1730-1739; sources audit rows N1-N5 (N5: "holds, subject to the questions common to every case") | holds as a statement about scope; the qualifier is missing: **D2** |
| 14 | A2 is stated for all bounded time-zero functions; V.15 and GRS II.16 print the interior functions as functions of finitely many fields; for other functions the printed basis is the unproved Remark; Lemma 4.1 relies on this; the approximation argument closes it and is not yet in the record (README ll. 48-53; strategy.md l. 2620) | A2 (`A:fkn`, A2, p. 13, ll. 858-887) and Lemma 4.1 (`lem:slabFKN`, 4.1, p. 26, ll. 1767-1790) at HEAD; analysis audit §9.5 (R1) and §10.1; note §7.3 (ll. 1859-1863) | holds, except that "closes it" is a little stronger than the auditor's "would serve"; strategy.md's version is incomplete: **D5** |
| 15 | Statement numbers of the record of 23 Nov equal 49f2d23's, pages differ (README l. 36; first page ll. 84-85) | HEAD's working-tree `main.aux` (written at 23:21, the same minute as the tracked `main.pdf`, which equals HEAD's; I did not rebuild the record) against the frozen `main.aux` | holds: 238 labels each, 0 renumbered, 199 on other pages. But the *statement* of Cor. 12.3 differs: D1. |
| 16 | "The record of 23 November 2026 (127 pages)"; it restricts Cor. 12.3 to ξ⁴ and 0 ≤ g ≤ 1 and rewords one sentence of 12.2's imports paragraph (first page ll. 84-87) | `pdfinfo part_i/main.pdf`: 127; corollary ll. 3172-3181; block diff | holds. HEAD is commit 9733263, dated 24 Nov 00:08:58 +0100, containing the work of 23 Nov. |
| 17 | The argument "covers the restricted corollary as well, since the corollary's proof uses Theorem 12.2(1) only through its rate" (first page ll. 87-89) | HEAD proof ll. 3183-3214 ("For the unaveraged net this is Theorem 12.2(1)"; "≤Ψ_{m_1}(2n−R)⟶0"); analysis audit §10.6, C2 | the reason holds; "as well" fails: **D1** |
| 18 | The three points of the confirmation (two MINOR, one cosmetic) "are not applied" / "are open"; "the next item but one" (first page ll. 75-79; README ll. 43-44; strategy.md l. 2616) | analysis audit §10.6 (C1-C3); first page ll. 83-89 | C1 and C3 hold; C2 has been taken up: **D3** |
| 19 | All MINOR points of the audits and the re-checks applied; none CRITICAL or MAJOR (README ll. 42-43; council README; strategy.md; first page ll. 73-75) | analysis audit §§1, 9.2, 10.2-10.3; sources audit §1 and re-check §§1-2. F6 was "partly closed"; its residue F15 was applied and confirmed (analysis audit §10.2). | holds |
| 20 | "(23 checks pass)" (README l. 37) | `check_route_t.output.txt`: 23 lines begin with `PASS`, and the last line reads "ALL CHECKS PASSED" | holds (the word "identities": D7) |
| 21 | Drafter's report on the first draft (25 pages); revision report on the two revisions (council README ll. 148, 151) | drafter report §1 ("25 pages"); revision report §1 and "Second round", item 1 | holds |
| 22 | Reports archived as written except three lines (council README l. 153) | `diff` against the originals in the council reports directory | holds: exactly 3 lines differ (sources l. 739, drafter l. 69, revision l. 194); the analysis report is identical |
| 23 | Build: three passes reproduce the PDF under pdfTeX 1.40.29 (TeX Live 2026); 33 pages, no errors, overfull boxes or undefined references (README ll. 55-62) | my rebuild (section 4) | holds ("the committed PDF" becomes true with the commit) |
| 24 | "since 24 November 2026" (README.md l. 286) | — | a dated sentence: true only if pushed today, which the orchestrator checks. "its audit reports": D7. |

## 3. Findings

### D1 (MAJOR). Corollary 12.3: the 49f2d23 statement is presented as covered

**Loci.**
- (a) `ugjs/route_t/route_t.tex`, first page, item "Which record", ll. 87-89. The orchestrator wrote it after the last audit. Quotation: "This note states Corollary~12.3 as at 49f2d23; by the auditor's confirmation, the argument given for it here covers the restricted corollary as well, since the corollary's proof uses Theorem~12.2(1) only through its rate."
- (b) `ugjs/route_t/README.md`, ll. 13-14: "items (1)–(4) of Theorem 12.2 and Corollary 12.3 hold with the same limit state and a different rate function". Read together with l. 36: "it refers to the record at commit 49f2d23 (statement numbers are those of the record of 23 November 2026 as well; pages differ)".

**Why it fails.**
- **The 49f2d23 statement.** `cor:canonical` (12.3, p. 42 at 49f2d23) reads: "Every $w^*$ limit point of the (averaged or unaveraged) finite-volume ground states constructed in \cite[\S2]{GJ3} coincides on each $\A(O)$ with $\omega_\infty$". The note claims this statement in T.2(b) (l. 258) and in §7.2 (l. 1797).
- **HEAD rejects it as written.**
  - The notice at ll. 3596-3599 says: "The statement of Corollary~\ref{cor:canonical} covered every cutoff of \cite[\S2]{GJ3}, while its proof needs $0\le g\le1$ (CRITICAL for that statement as written; no other result uses it)".
  - The front matter (ll. 161-167) calls it "one statement that claimed more than its proof".
- **Route T adds no argument of its own.** It obtains the corollary only by substitution. §4(b), ll. 1192-1193: "its proof uses (1) in the form $\Psi_{m_1}(2n-R)\to0$, which holds for $\Psit_{m_1}$". So it proves what the record's proof proves: the restricted corollary (12.3, p. 43, ll. 3172-3181). By its "as well", the first-page sentence says the argument covers the 49f2d23 statement too. That is stronger than the record at HEAD.
- **The auditor did not settle this.** C2 (analysis audit §10.6) found only that the substitution "applies to both versions. Correctness is unaffected". It did not consider that the 49f2d23 statement does not follow from its own proof.
- **An extra reading.** The restricted corollary rests on a reading that HEAD names (ll. 3216-3219): "rests on the reading recorded in the Scope of Assumption~\ref{A:cutoff}, applied to \cite{GJ3}, which is not among the sources listed there". The README's list "(Scope paragraphs of A1, A3, A6 and A8)" does not say that, for the corollary, the A1 reading is applied to a source outside its list.
- **The mathematics of Route T is unaffected.** By C2, the restricted corollary follows.

**Repair.** These texts make the audited body read correctly without editing it. If the orchestrator edits T.2(b), §4(b), §7.2 or the Summary instead, that change needs its own check.

- (a) First page. Replace ll. 84-89, from "The record of 23 November 2026 (127 pages)" to "only through its rate.", by:
  > The record of 23 November 2026 (commit 9733263, 127 pages) has the same statement numbers as 49f2d23, and different pages; it rewords one sentence of the imports paragraph of Theorem~12.2. It also restricts Corollary~12.3 to $\mathscr P(\xi)=\xi^4$ and to cutoffs $0\le g\le1$: its audit found that the statement at 49f2d23, which covered every cutoff of GJ3, goes beyond its proof, which needs $0\le g\le1$. This note obtains Corollary~12.3 from that proof with $\Psit_{m_1}$ in place of $\Psi_{m_1}$ (\S\ref{sec:assembly}(b)), so it gives the restricted corollary only, and Corollary~12.3 is to be read so wherever this note names it. By the auditor's confirmation (point C2), the argument applies to the restricted corollary, whose proof uses Theorem~12.2(1) only through its rate. The restricted corollary also rests on the reading of A1's Scope applied to GJ3, which the record of 23 November names after it.
- (b) README ll. 13-15. Replace "items (1)–(4) of Theorem 12.2 and Corollary 12.3 hold with the same limit state and a different rate function, which still decays faster than every inverse power," by:
  > items (1)–(4) of Theorem 12.2 hold with the same limit state and a different rate function, which still decays faster than every inverse power, and so does Corollary 12.3 in its restricted form of 23 November (𝒫(ξ) = ξ⁴, cutoffs 0 ≤ g ≤ 1; it rests in addition on the reading of A1's Scope applied to GJ3, which the record names after it). The note's Theorem T.2(b) repeats the statement of 49f2d23, which covered every cutoff of GJ3 and which the record's audit of 23 November found to go beyond its proof (see the note's first page).
- (c) README l. 36. Replace the parenthesis by:
  > (statement numbers are those of the record at 9733263 as well; pages differ, and so does the statement of Corollary 12.3)
- (d) Not a finding. In `docs/status.md` l. 161, `docs/imports.md` l. 34 and `strategy.md` l. 2618, "Corollary 12.3" denotes HEAD's restricted corollary, and those sentences are true by C2. Writing "Corollary 12.3 (in its restricted form)" there would remove the ambiguity for a reader who follows the link into the note.

### D2 (MINOR). "Reached" without its definition, and without the question of the constant

**Loci.**
- README ll. 25-26: "So Route T exchanges a case that no reading of the printed proof reaches for cases reached on that reading."
- README ll. 28-30: "the parallel pairs behind the uniform gap are reached by the printed proof after slicing in time, on either reading."
- strategy.md l. 2618, last two sentences.
- `docs/status.md` l. 161: "The printed proof of Theorem 1.1.7 reaches those pairs only if …".

**Reason.**
- In the note, "reached" is a defined term about the *scope* of the printed proof, "not its correctness" (§5.4, ll. 1368-1382).
- The note leaves one question open for every case. ll. 1384-1388: "The constant. The printed proof takes its constant ``from Theorem 1.1.8'' at the same $h$ (p.~597) … This question is common to P1--P4 and to every use of Theorem~1.1.7 in the record; it is not decided here". It repeats this in §5.5, item 3 (ll. 1648-1652), and in §7.2 (ll. 1806-1807).
- The sources auditor names it among the three conditions "under the stricter standard" (re-check §10: "The question common to every case: the constant taken from Theorem 1.1.8 at the same h"). It qualifies the gap claim "holds, subject to the questions common to every case" (§2, row N5).
- The README names R1 and the rotation presupposition, but not this third condition. Neither do strategy.md and `docs/status.md`. `docs/imports.md` states it in the sentence before.

**Why MINOR.** The question affects the record's present applications in the same way as Route T's, so no comparison in these texts changes. But a reader who does not know the note's definition takes "reached" to settle more than the note claims.

**Repair.**
- README, after "…that rotating the setting is covariant." (l. 25), insert:
  > ("Reached" is the note's term for the scope of the printed proof, not its correctness. One question remains for every application alike, in the record as here: the printed proof takes its constant from Theorem 1.1.8 at the same h, p. 597.)
- README l. 30: append ", subject to that common question".
- strategy.md l. 2618, after "is presupposed as well.", insert:
  > ("Reached" concerns the scope of the printed proof; the question of the constant taken from Theorem 1.1.8 at the same h remains for every case alike, as in the record.)
- `docs/status.md` l. 161, after "that rotating the setting is covariant.", insert:
  > As for every application in the record, the printed proof takes its constant from Theorem 1.1.8 at the same h (p. 597).

### D3 (MINOR). The second point of the confirmation has been taken up, and the pointer to it is off

**Loci.**
- First page, ll. 75-79: "the three points of that confirmation (two MINOR, one cosmetic; section 10 of the first report) are not applied: … the second point is the next item but one; and three wordings."
- README ll. 43-44: "Three points of the last confirmation (two MINOR, one cosmetic) are open and named on the note's first page."
- strategy.md l. 2616: "all MINOR points applied except three of the last confirmation".

**Reason.**
- C2's repair is an addition to "Which record" (analysis audit §10.6). The orchestrator's sentences at ll. 85-89 carry it out, in a wording that D1 corrects. So C2 is not open.
- Counting from "Audits", "the next item but one" is "Not integrated" (l. 81). The text is in "Which record" (l. 83), one item later.
- strategy.md counts the cosmetic C3 as a MINOR point.

**Repair.**
- First page ll. 76-79:
  > …and confirmed it. Of the three points of that confirmation (two MINOR, one cosmetic; section 10 of the first report), the second, on the record of 23 November, is taken up in the item ``Which record'' below; the other two are not applied: Simon's class $F$ on p.~163 is fixed by his own notation and is not a reading, as the proof of Lemma~T.15 calls it; and three wordings.
- README ll. 43-44:
  > Of the three points of the last confirmation (two MINOR, one cosmetic), the second (on the record of 23 November) is taken up on the note's first page; the other two are open and named there.
- strategy.md l. 2616:
  > all MINOR points applied except one MINOR and one cosmetic point of the last confirmation (its other MINOR point is taken up on the note's first page)

### D4 (MINOR). "were not checked" goes out of date once this check is archived

**Locus.** README ll. 44-46: "The first-page sentences about the last confirmation and about Corollary 12.3 were written by the orchestrating agent after that confirmation and were not checked."

**Reason.** The sentence was true when written. This check has since read both passages against §10 of the analysis audit and against HEAD's record (D1, D3).

**Repair.** If this report is archived:
> …were written by the orchestrating agent after that confirmation; only the documentation check of 24 November (`../council/<archived name of this report>`) read them, and they were corrected for its findings.

If it is not archived, the sentence may stay.

### D5 (MINOR). The point on A2: "closes it", and the shorter version in strategy.md

**Loci.**
- README ll. 52-53: "The approximation argument in the proof of Lemma T.15 of the note closes it; it is not yet in the record."
- strategy.md l. 2620: "A2 is stated for all bounded time-zero functions, its printed sources give the interior functions as functions of finitely many fields; the approximation argument in the note's Lemma T.15 closes this and is not yet in the record."

**Reason.**
- **Checked at HEAD.**
  - A2 (ll. 858-871) is stated "For all bounded time-zero functions $f,h'$, $T>0$, and $g\in\CH$", "together with the analogous multi-time formulas on finite slabs". Its sources are Simon's Cor. V.14 and Thm. V.15, and "equivalently" GRS, Thms. II.14 and II.16.
  - Lemma 4.1 (ll. 1767-1778) is stated for "bounded nonnegative measurable functions $F_1,F_2$ of the time-zero field" at the times ∓t/2 and at s ∈ [−T, T]. Its proof (ll. 1780-1790) invokes A2.
  - The first three sentences of the README paragraph therefore agree with the record and with R1 (analysis audit §9.5: the Remark "is still the printed basis of A2's function class … the record's Lemma 4.1 makes the same extension").
- **"Closes it" is a little strong.** The auditors checked the argument for (t7) only: two times strictly inside the slab, with G_0 = G_3 = 1 (§9.5, the R1 repair; §10.1, item (2)). For Lemma 4.1 the auditor wrote only "The same sentence would serve the record's Lemma 4.1", and the note says "applies equally" (ll. 1859-1863). Nobody checked the argument at Lemma 4.1's own cases (one time; t = 0; t = 2T).
- **strategy.md is incomplete.** It omits that, for other functions, Simon prints the Remark on p. 164 without proof. It also omits that Lemma 4.1 is the record's statement concerned.

**Repair.**
- README ll. 52-53:
  > Step 1 of the proof of Lemma T.15(ii) of the note derives the two-time case it uses from the bounded case of Theorem V.15 by approximation; by the auditor's remark the same argument would serve the record's Lemma 4.1. It is not yet in the record.
- strategy.md l. 2620, last sentence:
  > A point for the record from its audit: A2 is stated for all bounded time-zero functions, while the theorems it cites (Simon V.15, GRS II.16) print the interior functions as functions of finitely many fields, and for other functions Simon prints only the Remark on p. 164, without proof; the record's Lemma 4.1 rests on this. The approximation in Step 1 of the proof of the note's Lemma T.15(ii) derives the case the note needs from the bounded case of V.15 and, by the auditor's remark, would serve Lemma 4.1; it is not yet in the record.

### D6 (MINOR). The "conditional on" lists are shorter than the auditors'

**Loci.**
- README ll. 12-13: "'proved, conditional on' the imports A1–A8 of the record and the readings the record declares (Scope paragraphs of A1, A3, A6 and A8), by the two audits".
- strategy.md l. 2618: "conditional on A1–A8 and the declared readings".

**Reason.**
- Both audits end their lists with the record's statements, "used as the record states them". See the analysis audit's final line in §10, item 3, and the sources audit's re-check §10, "The record's statements that the note lists".
- The note's status (ll. 285-290; §7.1, row T.2) also lists the open items of `part_i/C5_reading_record.md`, and restricts the imports: "A8(iv) used only in the cases P1–P4 and A8(iv)-T not used, and … A2 used at two times placed asymmetrically in a slab".
- The record's statements rest on A1–A8 and the declared readings, so no condition from outside the record is lost. Hence MINOR.

**Repair.**
- README ll. 12-13:
  > Its Theorem T.2 is "proved, conditional on" the imports A1–A8 of the record (A8(iv) used only in the cases P1–P4, A8(iv)-T not used, A2 used at two times placed asymmetrically in a slab), the readings the record declares (Scope paragraphs of A1, A3, A6 and A8, with the open items of `../../part_i/C5_reading_record.md`) and the record's statements the note lists, used as the record states them, by the two audits:
- strategy.md:
  > conditional on A1–A8, the declared readings and the record's statements that the note lists

### D7 (MINOR). Paths and descriptions in the tables

- **README l. 38.** `route-t-revision-report.md` does not resolve from `ugjs/route_t/`. Replace it by `../council/route-t-revision-report.md`. Every other code-span path in the new texts resolves.
- **Council README l. 149: "every step holds".** The analysis auditor's part is §§1-4 (T.1–T.16 and the proof of T.2), plus the hunks of the second round. T.17 and T.19 were checked by the sources auditor. Replace by:
  > every step of its part (§§1–4: T.1–T.16 and the proof of T.2) holds
- **README.md l. 286: "with its audit reports in `ugjs/council/route-t-*.md`".** The glob matches four files, two of them the drafter's. Replace by:
  > with the drafter's and the auditors' reports in `ugjs/council/route-t-*.md`
- **README l. 37: "numerical corroboration of its elementary identities".** Several checks test inequalities (Lemma T.11; the Gaussian tail; ∫‖w(t,·)‖dt ≤ ‖w‖; E[V̄²] ≤ E[V²]; note, Appendix A, ll. 1886-1900). Replace by:
  > of its elementary identities and inequalities

### D8 (MINOR). strategy.md: "the record and its status sentences are unchanged"

**Locus.** strategy.md l. 2620.

**Reason.** This commit adds a passage to the status page `docs/status.md` (l. 161) and to `docs/imports.md` (l. 34). The status of Theorem 12.2 is unchanged in both, but "its status sentences are unchanged" can be read as covering those pages.

**Repair.**
> the record (`part_i/main.tex`) and the status of Theorem 12.2 are unchanged; `docs/status.md` and `docs/imports.md` gain one passage on the note.

### D9 (cosmetic)

- **"the observable A of Theorem 1.1.11".** It occurs in README ll. 22-23, `docs/status.md` l. 161, `docs/imports.md` l. 34 and strategy.md l. 2618. GJS (p. 596, as the note quotes it at ll. 1251-1253) and the note itself (Summary ll. 117-118) say "monomial". Replace by "the monomial A".
- **Source comment, `route_t.tex` l. 3.** "Audited by two independent agents and re-checked on 23 November 2026" omits the confirmation, and both re-checks are headed "23/24 November 2026". Replace by:
  > Audited by two independent agents on 23 November 2026, re-checked by both (23/24 November) and confirmed by one on 24 November; revised for their findings.
- **Drafter's report, archived l. 69.** Besides naming the prefixes in words, the replaced line dropped the grep's file arguments. The council README's description of the change (l. 153) remains true.
- **Strategy.md ll. 1667 and 1748.** These lines contain `~/.claude/projects/...` paths. They are already in HEAD and are not part of this change.

## 4. Checks actually run

- **Rebuild.** I built a copy of `ugjs/route_t/route_t.tex` in the council scratch directory `work/route-t-docs-check/build/`. The source has no `\input`, `\include` or `\includegraphics`. I ran three passes of `SOURCE_DATE_EPOCH=1795392000 FORCE_SOURCE_DATE=1 /Library/TeX/texbin/pdflatex -interaction=nonstopmode route_t.tex`.
  - All three passes exited 0.
  - `pdflatex --version` prints "pdfTeX 3.141592653-2.6-1.40.29 (TeX Live 2026)".
  - Log of the third pass: `grep -cE '^!'` 0, `grep -c Overfull` 0, `grep -icE undefined` 0.
  - `grep -i rerun` gives 5 lines, all package-load lines or the `rerunfilecheck` line "File `route_t.out' has not changed"; there is no rerun request.
  - `pdfinfo`: Pages 33.
  - `pdftotext route_t.pdf - | grep -nE '\?\?|TODO|Hmm|wait,'` printed nothing (exit 1).
  - `cmp` against `ugjs/route_t/route_t.pdf` printed nothing. Both files have SHA-1 1e88ba6e2a653d55bfbedaeeb87cfe792b1bd53d, so the build does not depend on the directory.
  - `date -u -r 1795392000` gives 23 Nov 2026 00:00:00 UTC; the PDF's CreationDate is "Mon Nov 23 01:00:00 2026 CET".
- **Script output.** In `check_route_t.output.txt`, `grep -c '^PASS'` gives 23, `grep -c PASS` gives 24, and there is no `FAIL`. The last line is "ALL CHECKS PASSED". I did not run the script.
- **Record at HEAD.**
  - `git show 9733263:part_i/main.tex | cmp - part_i/main.tex`: identical. `git diff --quiet HEAD -- part_i/main.pdf`: identical.
  - `pdfinfo part_i/main.pdf`: 127 pages.
  - Labels of `part_i/main.aux` (23:21) against the frozen `main.aux`: 238 and 238, none only on one side, 0 numbers differ, 199 pages differ. Samples: `thm:MAIN` 12.2, p. 41 → p. 42; `cor:canonical` 12.3, p. 42 → p. 43; `A:fkn` A2, p. 13 → p. 13; `lem:slabFKN` 4.1, p. 25 → p. 26; `aux:d3-orient` N.39, p. 96 → p. 98.
  - A diff of the block from `thm:MAIN` to the `cor:canonical` label, 49f2d23 against HEAD, shows two changes: the sentence on S₂ in the imports paragraph, and the corollary's title.
  - I read the corollary, its proof and the reading after it (ll. 3172-3219), the notice of 23 November (ll. 3593-3599), the front matter (ll. 158-178), A2 (ll. 858-887) and Lemma 4.1 (ll. 1767-1790).
- **Reports.** I read `route-t-audit-analysis.md` §§1-3, 5-8 and 9-10 in full, and `route-t-audit-sources.md` §§1-2, 5-7 and its re-check §§1-10. I diffed the four archived reports against the originals in the council reports directory: 3 lines differ, the analysis report is identical.
- **Guards.**
  - Patterns for machine paths and e-mail addresses (the absolute prefixes of home, temporary and volume directories, home-relative paths into the documents and agent folders, and an address pattern):
    - `git grep` on the five modified files: only strategy.md ll. 1667 and 1748, both already in HEAD;
    - the added lines of `git diff`: none;
    - the untracked files (note, README, script, output, four reports): none;
    - `strings` of the PDF: none.
  - Liquid delimiters (`{{ {% %} }}`) in `docs/status.md` and `docs/imports.md`: none.
  - `python3 docs/extract.py --check` prints "up to date" (exit 0). I read its `--check` branch first: it writes nothing.
  - `pdfimages -list ugjs/route_t/route_t.pdf`: header only, no images.
  - `git add -n ugjs/route_t` takes `README.md`, `check_route_t.output.txt`, `check_route_t.py`, `route_t.pdf` and `route_t.tex`. `git check-ignore -v` shows `.aux`, `.log`, `.out` and `.toc` ignored by `.gitignore` ll. 93, 94, 95 and 97.
  - Every path named in the new texts was tested with `-e`. The only path that is missing and is not explicitly a working name is `route-t-revision-report.md`, as seen from `ugjs/route_t/` (D7).
  - The new `docs/status.md` link uses the same `github.com/.../blob/main/` pattern as the page's ten other absolute links (eight distinct targets).
  - `git status --short` and `git diff --stat` were the same before and after my checks.
- **Provenance of Route T.** I grepped the 22 November council record (`SYNTHESIS.md`, `memo-cqft.md`) for "Route T".

## 5. Not done, not verified, not run

- **Not done.**
  - The mathematics of the note (not my task).
  - Any comparison of the note's citations of A1 and A8 Scope, given at 49f2d23, with HEAD's reworded Scope paragraphs. HEAD's front matter, ll. 171-174, says "the Scope paragraphs of A1 and A8" were reworded.
- **Not verified.**
  - The model names "Claude Opus" and "Opus" (README l. 4; strategy.md l. 2616): no file names a model.
  - "Not read by a human", wherever it occurs.
  - That the sources auditor wrote none of the note: its report calls both agents independent but does not say so in words.
  - Simon's p. 164 and the GRS pages: I rely on the auditors' renders and did not render them myself.
- **Not run.**
  - `check_route_t.py`.
  - Any build of `part_i/main.tex`: I used its existing `main.aux` and the tracked `main.pdf`.
  - Any git command that changes state.

## 6. Files written

- This report: `reports/route-t-docs-check.md` in the council scratch directory.
- Scratch, in the council scratch directory `work/route-t-docs-check/`, not in the repository:
  - `main-HEAD.tex`;
  - `thm-frozen.txt` and `thm-head.txt`;
  - `build/`: a copy of `route_t.tex`, its build by-products, and `pass1.out`-`pass3.out`.
- A redirect slip wrote a file named `x` in the system temporary directory, outside the scratch area, and deleted it in the same command. I had not checked whether a file of that name existed before.
- Nothing under the repository.
