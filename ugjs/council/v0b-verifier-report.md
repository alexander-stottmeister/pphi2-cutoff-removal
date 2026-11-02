# V0b: re-check of the V0/V0′ repairs (fresh verifier), 31 October 2026

**Scope.** I re-checked the repairs of C1–C4 and M1–M6 of `ugjs/council/v0-verifier-report.md`
in the uncommitted working tree, and spot-checked the MINOR repairs.

**How I worked.**
- I read the files on disk only. I ran no git and no kb command, and wrote only this file.
- Every quotation the repairs touch or add was compared with the GJS page images
  (`<scratchpad>/gjs74/p-NN.png`, printed page = NN + 583) and with the text layer
  (`pdftotext` of `<scratchpad>/gjs74.pdf`).
- My builds and renders are in `<scratchpad>/v0b/`.
- Line numbers below are those of the current files.
- `<scratchpad>/main.tex.HEAD` is byte-identical to the copy of the committed file that I
  checked against `git show HEAD` in V0 (`cmp` against `<scratchpad>/head/main.tex`).

**Result.** All four CRITICAL items and five of the six MAJOR items are repaired. Two repairs
introduced a new MAJOR defect:
- item 13b of the C5 record makes the counts and enumerations of the C5 items disagree across
  seven files;
- Scope (d)(i) states something false about the source.

M5 is not fully repaired: the gate record now honestly says G-0's "0 Overfull" is not met,
and under PLAN Part 7 that blocks the status word.

Counts in this round: 2 new MAJOR, 8 new MINOR, and 5 V0 MINOR items still undone (partly or
wholly).

---

## 1. Verdicts on C1–C4 and M1–M6

### C1 — fixed
`part_i/main.tex` l. 2803–2805 now reads: "The interpolation $C(s)=sC'+(1-s)C''$ (2.0.1) is
between covariances of the family generated from $C_0$ by ``diagonalization'' with respect to
unions $Y$ of unit squares, $C_Y=YCY+(1-Y)C(1-Y)$, and convex sums (p.~600)".
- The one quoted word is printed on p. 600: "we define its diagonalization with respect to Y
  to be C_Y = YCY + (1 − Y)C(1 − Y)" (image; text layer l. 35).
- The description is also correct: "constructed from the free covariance C₀ … by the
  application of two elementary operations: Diagonalization and convex sums" (p. 600).
- "diagonalized" no longer occurs in main.tex or in the generated docs.

### C2 — fixed
- l. 863–865 now reads "…obtains its $h$-independent constant from Theorem 1.1.8 at the same
  $h$ (p.~597) while Theorem 1.1.8 is printed only ``uniformly as $h\to1$'' (p.~595)". The
  remaining quotation is verbatim on p. 595.
- l. 884–885 (Scope (c)) and l. 2777 (Appendix C intro) carry the phrase without quotation
  marks.
- The regenerated `docs/results.md` (l. 808, 829) follows.

### C3 — fixed
l. 870–871 now reads "``assembled from four pages of the source rather than read off one
theorem''". This equals `main.tex.HEAD` l. 802–803 ("assembled from four pages of the source
rather than read off one theorem"). README.md, docs/status.md and docs/imports.md quote only
"assembled from four pages", which is verbatim.

### C4 — fixed
- **Figure generator.** `docs/figures/make_figures.py` l. 369–375:
  - description: "A1-A8 and the spine of Part I. Everything whose proof chain reaches A8, the
    GJS package, rests on its printed statements (all literal since 31 October 2026).";
  - legend: "proof chain reaches A8 — rests on the GJS imports".
- **Both SVGs.** They were regenerated at 08:03:12, after the generator's 08:02:57 change,
  and carry these texts at l. 3 and l. 15.
- **Banner.** `docs/assets/figure.js` l. 52–55: "Theorem 12.2 is proved from the printed
  imports A1–A8 (U_GJS is GJS Theorem 1.1.11 as printed since 31 October 2026), the human
  page readings of audit item C5 are open, …".
- **`docs/interactive/imports.html`:**
  - l. 40–44: "Turn off A8. … its item (vi), U_GJS, is since 31 October 2026 read off the
    printed Theorem 1.1.11 (it was a named hypothesis before)…";
  - l. 87: toggle "A8 granted (the GJS package available)";
  - l. 136–140: "…reach A8 and rest on its printed statements…" / "…stand without it…";
  - l. 153: tag "reaches A8".
- **Other pages.** `dichotomy.html` l. 28–29: "resting on the same imports as Theorem 12.2 —
  so it reaches A8". `index.html` l. 13: "Withdraw A8 and watch what falls."
- **Grep.** Searching these files for "conditional on U_GJS", "inherits the conditionality",
  "conditional on the imported interface" and "unconditionally" finds nothing. The only
  remaining "conditional" is Theorem 13.2's own title ("conditional exclusion of a
  two-phase…") at SVG l. 91, which is correct.
- **One page outside the brief** carries a stale basis (n7 below).

### M1 — fixed
`docs/imports.md` l. 63–65 now reads: "…which is planned to prove (conjectured until written and
audited) the uniform local moment from the printed clustering theorem (GJS Theorem 1.1.7)…".

### M2 — fixed; the deviation is acceptable
- **The new texts:**
  - `companion/companion.tex` l. 19–27 (page-1 notice): "The companion describes the record of
    24 October 2026 (40 pages), whose Theorem~12.2 was proved conditional on the imported
    hypothesis $\UGJS$ (Assumption A8(vi)); since 31 October 2026 the record imports that item
    as the printed GJS Theorem~1.1.11 (its title page; \texttt{ugjs/PLAN.md}), so the abstract,
    \S1's ledger, \S4 and Figures~1--2 below describe the earlier reading. … Statement numbers
    and pages refer to the 40-page \texttt{part\_i/main.tex}".
  - l. 31: "A reading guide to the 40-page record of 24 October 2026".
  - `sections/s4-import.tex` l. 4–6: "…(the reading as of 24 October 2026; see page~1)".
  - l. 71–80: "nine then, thirteen since 31 October 2026"; the h-trace sentence.
- **The circular pointer is gone.**
- **The notice is true.** "The record of 24 October 2026 (40 pages)" holds: the page column of
  `companion/council/labels.md` (generated 23 October) equals the committed build's page
  numbers for all 61 statements, and the committed build has 40 pages (measured in V0).
- **Judgement on the deviation.** There is no separate paragraph at the head of §4. I accept
  this. The page-1 notice names §4 among the parts that describe the earlier reading. §4's
  first sentence carries the date and points to page 1. The `\rec` page locators are declared
  to refer to the 40-page build. The companion stays at 20 pages.
- **Residue.** One defect remains in the §4 paragraph (n6), and the count "thirteen" is now
  off by item 13b (N1).

### M3 — fixed
- README.md l. 27 "(`part_i/main.tex`, 42 pp, document of record)", l. 146 "| 42 pp |" and
  l. 230 "A clean build is 42 pages with zero errors and zero undefined references." My scratch
  rebuild confirms all three: 42 pages, 0 errors, 0 undefined.
- docs/index.md l. 45 "(42 pp, document of record)".
- README.md l. 176 "its Phases 0′ and 0 were executed on 31 October 2026, Phases A and B are
  next". This is consistent with strategy.md's new Checkpoint-1 record (Q1′ "yes").

### M4 — fixed, but introduces a new defect (N1, MAJOR)
What was repaired, all in `part_i/C5_reading_record.md`:
- Item 9 now has "What this carries (since 31 October 2026): (1.1.16) "uniformly in h" is the
  literal basis of A8(vi), together with items 12–13; the derivation of Theorem 1.1.7's
  constant from Theorem 1.1.8 **at the same h** is recorded in the Scope paragraph,
  point (c)…". This is accurate against main.tex l. 884–886.
- The site pointers of items 1 (l. 43–44), 5 (l. 83–85) and 8 are updated and accurate.
- Item 6 (l. 97) still names "Appendix C intro" (n3).
- docs/status.md l. 67 now reads "all thirteen verdict fields".

The new item 13b (l. 201–207) has verbatim text (p. 628, image and text layer), and its image
`audit_2026/evidence/gjs-thm41-45.png` exists. It is byte-identical to `gjs74/p-45.png`. But the
item makes the C5 record count fourteen fields ("All fourteen `MATCHES` (items 1–13 and 13b)",
l. 213), and the other files were not adjusted. See N1.

### M5 — not fixed
- **What is now right.** `part_i/README.md` l. 448–460 ("Build (gate G-0/G-0′ record)") is
  complete and honest about the build. It also records the V0 verdict correctly ("can be
  committed after the listed fixes" is a verbatim substring of my V0 verdict line).
- **(a) The gate is unmet while the status word is used.** The record says: "G-0's
  "0 Overfull" is therefore **not met**, by the committed build either, and is left for a
  layout pass." PLAN Part 7 says: "A status word below may be used only once the gate of the
  phase that produces it has passed". G-0′ requires "Three pdflatex runs clean, with the checks
  of G-0", and G-0's "0 Overfull" comes from AGENTS §7.1 ("Deliver only when … `grep -c
  Overfull <f>.log` … print[s] 0"). So the record now states that the gate is unmet while every
  public file uses the Phase 0′ status word. **Remedy:** either the layout pass now, or the
  author's explicit waiver recorded in the gate record. Neither exists; the brief says no
  waiver exists. The nine boxes in the current main.log are:
  - l. 203–207, 217 and 230: the §1.2 table and dependency graph, p. 4;
  - l. 560–562: A4 "Sources";
  - l. 856–859: A8(viii);
  - l. 1186–1190;
  - l. 2469;
  - l. 2663–2684: the Appendix A table;
  - l. 2840: M5's display.
- **(b) "Every item applied" is not true yet.** The record says "every item applied before the
  commit", but five V0 MINOR items are partly or wholly undone (§4 below). **Remedy:** apply
  them, or reword to "every CRITICAL and MAJOR item applied; MINOR items … open".
- **(c) The page inspection is now complete.** G-0 asks that "every changed page [be] rendered
  and inspected". I rendered all seventeen pages of the current `main.pdf` that carry a
  changed passage: pp. 1–5, 10–15, 18, 32, 37–39, 41. I found no layout defect beyond the nine
  pre-existing boxes. The gate record can cite this round for the item.

### M6 — fixed, but introduces a new defect (N2, MAJOR; and n2, MINOR)
`part_i/main.tex` l. 887–897, "(d) Three readings made explicit". On the coordinator's three
questions:
- **(i), first clause: false as written.** l. 888–889 reads "is read over the class of
  p.~589 (compact support, $0\le h\le1$), the only class of cutoff functions the source
  defines". But p. 588 defines a second class, for (1.6): "We choose λ𝒫(·) bounded from below
  and 0 ≦ g(·) ≦ 1 with g measurable and of compact support." The record's own A8(i)
  (l. 649–651) cites it: "the Hamiltonian cutoff class of \cite[(1.6), p.~588]{GJS} is
  $\CH$". p. 589 also uses "rectangular cutoffs" (a sequence inside the class, for (1.9)), and
  p. 629 names "a periodic space cutoff" as an alternative. What is true is that p. 589's class
  is the only class of **space-time cutoffs h of the measures dq_h** the source defines. See N2.
- **(i), second clause: holds.** "independent of h" is printed on p. 594 ("constants 0 < m₁
  and O(1) independent of h, Q₁ and Q₂"). The record reads it over 𝒞_E:
  - Source Fact 2.2 states it for dq_h with h ∈ 𝒞_E (A8(i));
  - Lemma 7.4 applies it at h_{T,g} ∈ 𝒞_E^slab;
  - the proof of Proposition C.7 says "Source Fact 2.2 quantifies over its cutoff directly".

  The p. 629 quotation "in the space cutoff $h$" is verbatim ("are uniform in the space cutoff
  h").
- **(ii): does not overstate pp. 628–629.** p. 628 prints the norm identities
  "‖Q_n(t)B_T‖ = e^{γt}‖Q_n(t)‖₀‖B‖₀, ‖w_r‖ = K₁e^{γT}|w_r|, ‖AB_T‖ = K₁⁴‖A‖₀‖B‖₀"; the
  exponent 4 was read on a 220-dpi render. p. 629 closes with the inequality, bounded by
  ‖AB_T‖ = K₁⁴‖A‖₀‖B‖₀, from which "Theorem 1.1.11 follows". So the proof's constant is a power
  of K₁, independent of A, B, T and h, once Theorem 4.1's thresholds (which depend on n and ε)
  hold. (ii) presents this as a reading and the proof supports it. Optional: cite pp. 628–629
  as that support.
- **(iii): correct.** Theorem 1.1.7's printed proof rests on Theorems 1.1.8 and 1.1.11 (p. 597),
  whose proofs carry (2.4.34).

---

## 2. Every quotation the repairs touch or add

| where | quotation | source | result |
|---|---|---|---|
| main.tex l. 2804 (C1) | "diagonalization" | p. 600 | verbatim |
| l. 864 (C2) | — (marks removed) | — | correctly unquoted |
| l. 870–871 (C3) | "assembled from four pages of the source rather than read off one theorem" | committed main.tex l. 802–803 | verbatim |
| l. 737–738 | "In the next two results, we take all times x_{1,0}=t=⋯=x_{r,0} equal in Q(x_0). To indicate this restriction, we write Q(t) in place of Q(x_0)." | p. 596 | verbatim; centred dots render correctly; the omission mark before it is spurious (n1) |
| l. 841–842 | "Take n=0 in Theorem 1.1.11 Then Q is a polynomial of degree zero, i. e., a constant." | pp. 596–597 | verbatim (the silent period is gone) |
| l. 849 | "…e^{−γT}, uniformly in h." | p. 596 | verbatim (comma restored) |
| l. 887–891 | "uniformly in h"; "independent of h"; "in the space cutoff h" | pp. 596, 594, 629 | verbatim |
| l. 2864 | "m₀, K₂, K₁, and then λ" | p. 616 | verbatim |
| l. 2870–2873 | "where the volume of interaction, denoted Vol, is the area of the set of points within unit distance of suppt h. Here we use (2.4.34), (2.4.35) and a Schwarz inequality to factor out vertices" | p. 625 | verbatim |
| C5 item 12 | p. 596 equal-times sentence | p. 596 | verbatim |
| C5 item 13b | Theorem 4.1 sentence; "Proof of Theorems 1.1.8 and 1.1.11. Divide (4.3) by ∫e^{−V}dΦ_{C₀} and set" | p. 628 | verbatim |
| s4-import.tex l. 79 | "a verdict on the printed record, not a no-go theorem" | docs/imports.md l. 75 | verbatim |
| part_i/README.md l. 457 | "can be committed after the listed fixes" | V0 report, verdict line | verbatim |

The unquoted locators that the repairs changed are all correct:
- the abstract's "(pp. 600 and 629)";
- Appendix B's "($T=0$ on p.~600), $n=0$ (named on p.~629)";
- the reading paragraph's "(B=I, T=0)" for p. 600 and "(B=I, n=0)" for p. 629;
- "pp. 628–629" for the proof of Theorems 1.1.8 and 1.1.11;
- M1's "$K_1^{\nu}e^{\gamma t}$ ((2.4.3), p. 613)";
- docs/imports.md l. 7 "(§2.4, pp. 8–13)": A1 is on p. 8, A8 runs to p. 13 and §2.5 starts
  on p. 13;
- docs/notation.md "Appendix A, p. 35";
- the docs/provenance.md entry of 31 October.

---

## 3. New defects introduced by the repairs

### N1 (MAJOR): item 13b makes the C5 counts and enumerations disagree
The C5 record now says:
- l. 28–30: "Items 1–4, 9, 12, 13 and 13b carry the imports of A8 … items 10–11 carry the Scope
  paragraph's disclosure of the transverse case";
- l. 213: "All fourteen `MATCHES` (items 1–13 and 13b)".

strategy.md l. 2525 agrees ("items 1–4, 9, 12, 13, 13b; items 10–11 for the disclosure"). The
other files do not:
- **README.md:**
  - l. 53–55: "all thirteen verdict fields are still blank";
  - l. 43–44: "The human page readings of audit item C5 (items 1–4 and 9–13) are open".
- **docs/status.md:**
  - l. 26–27: "(items 1–4 and 9–13)";
  - l. 67–70: "all thirteen verdict fields are blank … items 10–13 on 31 October 2026";
  - l. 75–76: "items 1–4 and 9–13 carry the imports of A8, items 5–8 are corroboration". This
    also contradicts the record's own split, in which items 10–11 carry the disclosure.
- **docs/imports.md** l. 28–29: "(items 1–4 and 9–13)".
- **main.tex** l. 2755–2760 (External residue): "items 12--13 (…) carry the imports … items
  10--11 … carry the disclosure". There is no 13b.
- **companion** `s4-import.tex` l. 72–73: "(nine then, thirteen since 31 October 2026)".
- **part_i/README.md:**
  - l. 438–439: "External residue now lists C5 items 1–4 and 9–13 as load-bearing";
  - l. 462: "items 10–13 added (pp. 593/595; p. 594; pp. 596–597; p. 600), blank verdict
    fields". p. 628 is missing.

**Repair (smallest).** Fold 13b into item 13 as a second confirmation, with the p. 628
sentences next to p. 600's "convergence of our expansions …". Then:
- "thirteen" and "items 1–4 and 9–13" become true as they stand;
- C5 l. 28–30 becomes "Items 1–4, 9, 12 and 13", l. 213 "All thirteen";
- strategy.md l. 2525 drops "13b";
- docs/status.md l. 75–76 takes the record's split ("items 1–4, 9, 12–13 carry the imports;
  items 10–11 the disclosure; items 5–8 corroboration") and l. 70/72 lose the duplicated
  sentence;
- part_i/README.md l. 438–439 and 462 follow.

Keeping 13b instead means "fourteen" and "1–4, 9–13 and 13b" in all of these places. The
companion line needs a rebuild either way unless it is left at "thirteen" after the fold.

### N2 (MAJOR): Scope (d)(i) states something false about the source
`part_i/main.tex` l. 888–889 says the class of p. 589 is "the only class of cutoff functions
the source defines". This is false: p. 588 defines the class of g for (1.6), and A8(i), l. 650,
cites it.

**Repair:** "…over the class of p.~589 (compact support, $0\le h\le1$), the only class of
space-time cutoffs $h$ of the measures $dq_h$ that the source defines (its rectangular cutoffs
of (1.9) lie in it; the spatial cutoffs $g$ of (1.6), p.~588, are those of $H(g)$), exactly as
…". Then regenerate `docs/results.*`.

### MINOR
- **n1.** main.tex l. 736: "…localized at times $\ge T$.'' [\dots] ``In the next two
  results…''". On p. 596 the two passages are consecutive paragraphs, so this first "[\dots]"
  marks an omission that does not exist. The second, before Theorem 1.1.11, correctly omits
  Theorem 1.1.10. Delete the first.
- **n2.** main.tex l. 865–866: "Three points of scope are recorded." Four points (a)–(d)
  follow. Write "Four points".
- **n3.** C5 item 6, l. 97, lists "Appendix C intro" among the sites of p. 629. The
  introduction no longer cites p. 629; Remark C.6 (via Source Fact 2.4) and Scope (d) do.
- **n4.** The A8 dossier line, main.tex l. 905–909, lists `gjs-thm1111-13` and
  `gjs-proof118-17` but not `gjs-thm41-45` (p. 628), which l. 731 and l. 980 cite. The dossier
  map's A8 row, `part_i/README.md` l. 479, lists none of the three new images.
- **n5.** `ugjs/council/README.md` l. 7–9: "…on 31 October 2026 the plan's Phases 0′ and 0 were
  executed (see `../PLAN.md` and `../../docs/status.md`)". `ugjs/PLAN.md` (unchanged since
  30 October) still says "It is written for the author's approval. Nothing in it has been
  executed." (l. 13). Point to strategy.md / part_i/README.md instead, or date a line in
  PLAN.md.
- **n6.** `companion/sections/s4-import.tex` l. 75–77: "Until the council of 28--30 October 2026
  (\texttt{ugjs/PLAN.md}) found cheaper routes, \texttt{docs/imports.md} recorded an $h$-trace
  of the printed expansion (GJS pp.~600--631; …) as the only proportionate one."
  - The committed docs/imports.md gave "pp. 598–629"; the sentence silently substitutes the
    corrected range.
  - "found cheaper routes" overstates: the box comparison is conjectured.
  - Suggested: "…recorded an h-trace of the printed expansion (there 'pp. 598–629'; the argument
    runs to p. 631) as the only proportionate one, until the council … proposed other routes
    (the re-sourcing, applied; a comparison argument, conjectured)". Rebuild and check 20 pp.
- **n7.** `docs/interactive/affine-path.html` l. 26–31: "This is also where U_GJS lives. … The
  cutoff-uniform quantifier the manuscript imports as A8(vi) is the one the printed proof uses
  here, which is what the scope amendment of 5 September 2026 records." This presents the
  superseded basis as current. Add that it is corroboration since 31 October 2026, when A8(vi)
  was re-based on GJS Theorem 1.1.11. I did not read this page in V0, so it was not on that
  list.
- **n8.** docs/status.md l. 68–76: "…items 10–13 on 31 October 2026." is followed at once by
  "Items 10–13 were added on 31 October 2026 (…)". This is a duplicate; fold it into N1's
  repair.

---

## 4. Spot-check of the V0 MINOR list

**Applied** (verified at the lines given):

| item | where | what is there now |
|---|---|---|
| m1 | l. 773 | "a fixed $\varepsilon\in(0,1)$" |
| m2 | l. 767–768 | "By (1.1.7)--(1.1.8), … the kernel is the constant $1$" |
| m3 | l. 780–783 | "with kernel of bounded support", plus the equal-times clause |
| m4 | l. 785 and l. 985 | "pp.~628--629"; "the same hypotheses" |
| m5 | l. 737–738 and C5 item 12 | the equal-times sentence (with n1's extra mark) |
| m6 | l. 2790, 2795, 2803–2805, 2833 | M1 and M5 titles; $K_1^{\nu}$; the M2 description |
| m7 | l. 2873–2875, 2742, part_i/README E4 | "M1 and M3–M5" consistent in all three; date 9 August |
| m8 | src comments l. 728–731, 979–980, 2766–2767, 2787–2788, 2851–2853, 2878, 3070, 2392, 99–100 | dated and complete; n4 remains |
| m9 | l. 661–663 | the count-bound wording |
| m11 | README l. 43–44; docs/imports.md l. 28–29 | items named (see N1) |
| m12 (main.tex part) | l. 841–842, 849 | verbatim |
| m13 (part) | C5 item 2; External residue; README l. 53–55 | "rests in part"; the 10–11/12–13 split |
| m14 (main.tex part) | abstract, App B, reading paragraph | locators corrected |
| m15 | l. 184, 210 | "$U_{\rm GJS}$ (Thm 1.1.11)" |
| m16 (part) | docs/imports.md l. 7; docs/notation.md l. 36 | page numbers corrected |
| m17 | council README; part_i/README.md l. 3–4; dichotomy.html; index.html; docs/provenance.md l. 49–54 | updated (n5 remains) |
| m18 | strategy.md, "Checkpoint 1" paragraph | the interpretation of "start with the plan" recorded |
| m19 | l. 58 | "(verified 31 October 2026)" |

**Not applied, or only partly:**
- **m10.** F-0′ still follows compatible paraphrases at its first mention: README l. 20, 25,
  27, 38; docs/status.md l. 12; docs/imports.md l. 7. I found no record that this was accepted.
- **m12, C5 part.** Item 9(d) still lacks the printed comma ("…e^{−γT}, uniformly in h",
  p. 596). Item 9(b) has "i.e.," where p. 597 prints "i. e.,".
- **m13, closing list.** C5 "What a completed record closes" still maps "items 9, 12, 13 → the
  re-sourcing of A8(vi)", without item 2 (or 13b).
- **m14, CITATION.cff.** The file is unchanged since 07:20. Its abstract still reads "the
  moment estimate of Theorem 1.1.11 in the specialization they print as their proof of
  Theorem 1.1.8", without the literal basis 0 < T < 1.
- **m16, README.md l. 237.** It still says "The printed date is pinned in the preamble to the
  last mathematical change". main.tex l. 54–56 now says "the last change of the mathematics or
  of an import's status".

---

## 5. Checks run in this round

- **main.log.**
  - 0 `^!`, 0 "undefined", 5 Underfull.
  - 9 Overfull, with the same widths as the HEAD build: 0.17433, 0.27504, 1.47302, 2.6312,
    9.32993, 9.80121, 18.87297, 22.4121, 23.88007 pt.
- **Labels.** 125 `\newlabel`. The label→number lists are identical to
  `<scratchpad>/main.aux.baseline` and to the HEAD build (`diff` empty).
- **Rebuild.** 3 passes of `main.tex` in `<scratchpad>/v0b/build` with
  `SOURCE_DATE_EPOCH=1793404800 FORCE_SOURCE_DATE=1`:
  - byte-identical to `part_i/main.pdf`;
  - sha256 begins `41dd2a1a95a1ad25`;
  - 42 pages; 9 Overfull.
- **PDF text scan.** `pdftotext main.pdf | grep -nE '\?\?|TODO|Hmm|wait,'` finds nothing.
- **Grep gates.** `grep -c 'Assume \$U_{\rm GJS}'` gives 0; `grep -n -i
  'assum[a-z]*[^.]*U_{\rm GJS}'` prints nothing.
- **Inventory.** `python3 docs/extract.py --check` prints "up to date", and the mtimes of
  `docs/results.*` are unchanged afterwards. The inventory holds 61 statements: 29 import A8
  and 23 cite U_GJS.
- **Companion** (not rebuilt):
  - `pdfinfo` gives 20 pages; `companion.log` gives 0 errors, 0 Overfull, 0 Underfull,
    0 undefined and 0 LaTeX warnings;
  - sha256 begins `aaa54a90dc0dc66a`;
  - the PDF (08:08:10) is newer than its sources (08:07:51);
  - epoch 1792800000 = 24 October 2026 00:00 UTC, matching CreationDate;
  - page 1's text layer carries the new notice.
- **Pages inspected.** pp. 1–5, 10–15, 18, 32, 37–39 and 41 of the current main.pdf, at
  70 dpi.
- **Trap-phrase scan** of the changed files: the only hits are the pre-existing Part II
  "unconditionally" (docs/status.md l. 88; main.tex l. 2641).

## 6. What I could not check

- The KB nodes, and strategy.md's claim that "the only proportionate route" was corrected in
  the KB. The brief forbade kb commands.
- The author's words "start with the plan", and their reading as approval of Checkpoint 1.
- The companion was not rebuilt. Of its text I re-read only the page-1 notice, the abstract
  and §4.
- `evidence/gjs-theorems-10.png` and `-11.png` were not opened (as in V0).
- Pages of main.pdf other than the seventeen listed.
- Whether the nine Overfull boxes can be removed without moving a label (not attempted).
- The rendered GitHub Pages site.

---

**Not yet:**
1. N2: Scope (d)(i)'s "the only class of cutoff functions the source defines" is false (p. 588
   defines the class of g, which the record's own A8(i) cites).
2. N1: item 13b makes the C5 counts and enumerations disagree across README.md,
   docs/status.md, docs/imports.md, main.tex's External residue, the companion and
   part_i/README.md.
3. M5: the gate record states G-0's "0 Overfull" as not met, and PLAN Part 7 allows the
   Phase 0′ status word only after the gate passes. So the nine boxes need the layout pass or
   the author's recorded waiver, and "every item applied" needs the five remaining MINOR items
   or a reword.
