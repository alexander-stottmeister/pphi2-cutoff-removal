# Part I — unified manuscript (`part_i/main.tex`)

**Repair addendum (16 August 2026; supersedes earlier unconditional closure
wording below; itself superseded on 31 October 2026, see "Re-sourcing of A8(vi)" below; that state was superseded on 7 November 2026, see "Integration of Appendix D (2026-11-07)"; for the audit finding of 9 November 2026 see "Status review (2026-11-09 to 2026-11-11)", and for its repair "Free-field appendix (2026-11-11)").**  The canonical Main Theorem is an implication from the explicitly
enumerated construction imports and the slab-family moment hypothesis
`U_GJS` in Assumption `A:gjs`(vi).  The printed GJS theorem and p. 629 support that
interface but do not, on the audited pages alone, prove its exact working-family
quantifiers.  The title-page status, abstract, theorem, proof uses, and Appendix C
now agree on this conditional scope.  The CE2 localization and mollifier defects
are repaired.  Strategy and post-repair verification are in
`../repair_2026_08_16/`; the full Lamport reconstruction, critical audit, downloaded
sources, and citation screenshots are in `../fresh_audit_2026_08_16/`.

Canonical Part I document of record, assembled per the plan in `../strategy.md`
("Part I unification — plan (recorded 2026-08-10)"). All sources stay frozen; this
folder only adds.

## Build

```sh
pdflatex main.tex && pdflatex main.tex && pdflatex main.tex
```

Acceptance: zero unresolved references/citations in the final `.log`.

## Phase / gate log

| phase | content | gates | status |
|---|---|---|---|
| U0 | preamble, notation freeze, §1, §2 ledger (A1–A8) + immediate consequences, statements of `thm:MAIN` / `hyp:broken` / `thm:dichotomy`, App A (pending G3), App B, stubs | G0 | **done 2026-08-10** |
| U1 | §3 reduction, §4 slab, §5 (M₂), §6 norms, §7 (G) | G1, G3a | **done 2026-08-10** |
| U2 | §8 path, §9 filter/clustering, §10 LPPL, §11 limit, §12 ground/MAIN proof | G2, G3b | **done 2026-08-10** |
| U3 | §13 dichotomy proof, §14 discussion, App C; App A finalize | G4, G5 | **done 2026-08-10** |
| U4 | independent adversarial pass on the assembled file | G6 | **done 2026-08-10** |

### G0 record (2026-08-10)

- 3× pdflatex: 0 errors, 0 unresolved references/citations; 15 pages.
- Forbidden-string check: pass — every hit carries the whitelist marker
  (`grep ... | grep -v "negative-scope mention (whitelisted)"` returns empty).
- Used-in coverage: 8/8 assumptions carry a nonempty *Used in* line; every scheduled
  section stub names its consumed assumptions ("Consumes ...").
- Visual inspection: pages 1, 3, 5, 6, 11, 13 rendered and checked — no clipping.
- Layout debt for U3 polish: 13 overfull hboxes (widest ≈ 80pt, the dependency-graph
  arrays and the notation table; within the 2.9cm margin, nothing clipped).
- §2-level proofs already landed (beyond bare skeleton, all transcriptions):
  `prop:smoothing`, `prop:propagation`, `lem:covparity`.


### G6 record (2026-08-10) — adversarial pass, findings, dispositions

Five independent reviewers (fresh contexts, instructed to refute): (R1) §§3–7 vs
`lamport_euclidean_to_gap` + r2-check; (R2) §§8–12 vs `lamport_gap_to_main` + m6 v2;
(R3) ledger/§13/§14/App A/App B/bibliography vs m6/m3/audit/r1/r2; (R4) Appendix C vs
r1-check; (R5) global internal-consistency sweep of main.tex alone. All findings were
adjudicated against the file and sources; every confirmed finding is repaired and
re-verified (3× pdflatex clean, 35 pp, forbidden-string gate pass, labels stable).

**Breaking (1) — fixed.**
- A2 (`A:fkn`) displayed the FKN identity with the symmetric slab 1_{[−T,T]}⊗g; with
  embeddings at times 0 and T the interaction slab must be [0,T]. Found independently by
  R2, R3, R5; introduced at unification (U0), no downstream propagation (Lemma 4.1 and
  §8's path formula were correct). Fixed to 1_{[0,T]}⊗g; h_{T,g} kept for the normalized
  measures.

**Moderate (5) — fixed.**
- Lattice transport (R1): Prop. 3.2's closing sentence glossed that the dilation carries
  the printed estimates to a rescaled lattice. Fixed by the WLOG convention in §2.6 and
  the new Remark 3.3 (coordinate transport dictionary) — the fourth `[new]` item,
  authorized by the U4 plan amendment in strategy.md.
- Thm 13.2 dropped the evenness premise its proof uses via MAIN(4) (R3; audit-P1 defect
  class). Fixed: "Assume `\mathcal P` even and …" in statement and proof.
- A8's "uniformly bounded degree" sentence was false for §7's observables (R5, R1).
  Settled by page image gjs-theorems-10 (printed p. 593): GJS bound only the per-factor
  degree n_i < n̄, "Q still may have an arbitrarily large degree" (printed). Fixed with
  the n̄ = 2p′+1 reading; §7's degree-1-factor families are exactly licensed.
- C_c^∞/L² class drift in Lemma 7.6 → Thm 7.7 → Thm 7.8 (R5, R1). Fixed: cylinder
  monomials defined in §6; e_j ∈ C_c^∞ dense in L²; f ∈ C_c^∞, f ≠ 0, n ≥ 1.
- App C M4 supply line overclaimed Thm C.5's scope (R4; inherited from r1-check).
  Fixed: free-measure endpoint by Thm C.5; interpolated-measure existence internal to the
  printed proof (M5: no constant depends on it); appendix headline scoped to dμ₀.

**Minor (12) — all fixed.** A3 Used-in adds §3; A3 exponent "every a<∞" → "every finite
ϱ>0"; A4 gains the abstract Γ(c) form (Simon I.17) and App C's unvetted V.9 pinpoint is
retired (derivation now two lines from A4, incl. the sum-of-chaoses step by
orthogonality); A5(ii) pinpoints (V.12/Rosen 5.3, in their audited roles — V.12 hit
whitelisted); abstract's p. 629 misattribution dropped; Lamport bib entry now cited
(App B); BDW/RZT titles added (verified against arXiv, 2026-08-10); Lemma 7.6 n = 0 case
and f = 0 excluded; Lemma 10.5 small-d covering constant Ψ_γ(0) (not Ψ_γ(d₀⁻));
truncation level renamed ℓ; prop:pathreg generic exponent renamed ϱ; Cor 12.3 rebuilt
(σ_{a′} defined, weight h̄, g ∈ `\mathcal G` stated, integration variable a′).

**Nit (14) — all fixed.** Four-cell argument via extreme indices; Lemma 7.3 slab
qualifier T ≥ t/2; Thm 7.8 parenthetical ("Step 2 fails", not "vacuous"); square-moment
parentheticals cite CE1 + Remark 6.3; Lemma 3.1 s ∈ {0,1} case + generalization to
1_I⊗g (makes §8's citations literal); App A Ψ row shows both branches; §1.3(b) rate
harmonized to poly(d)e^{−2m₁d}; §14 Part II paragraph (per-generator wording, free vacua
ω⁽⁰⁾ symbols, rate exponent ϑ); provenance parenthetical for Cor 12.3's GJ3 formula;
App C: dμ_{0,C} defined, M2 hedge restored, C₀ → C_*, λ = 0 guard, subsection titles
un-numbered; A6 dossier double-wrap; freeze-table slab row; header comment; §13 and
thm:MAIN src comments corrected.

**Accepted as-is (3) — documented, no change.** thm:MAIN(5) quantifies over `\mathcal C_H` where
m6 stated `\mathcal G` (strengthening, delivered by Thms 5.1/7.8; noted in src comment); Prop C.7's
`\mathcal G` → `\mathcal C_H` widening (correct; matches usage); local notation shadows listed by R5 (each
locally announced, none load-bearing).

**Reviewer-verified clean:** all constant chains (M², `\mathfrak K(p′)`, 9·8! = 362 880, K′, Ĉ_Q,
32M, shell count 8, d₀, exponent identities, separation optimization), the filter sign
(+1/E), all cross-references and tags, the γ/m₁ and class-quantifier regimes, App A
values, App B register, §13's clustering application, §14's factual claims incl. the
Part II liminf constant, and the abstract-to-theorem promise map.

### Post-G6 editorial additions (2026-08-10)

- **E1**: new expository subsection §1.4 "The proof strategy in operator-algebraic
  terms" (author request). No new mathematical input: every assertion cross-references
  the body; the only free-standing mathematical remark is the two-line Paley–Wiener
  obstruction to exponential filter tails (transform of an exponentially decaying kernel
  is analytic in a strip, hence cannot vanish on a real neighbourhood of 0), stated as
  context for the super-polynomial rate. Two contextual references added to the
  bibliography (Hastings 2004; Bachmann–Michalakis–Nachtergaele–Sims 2012), cited only in
  §1.4 as lattice-physics context, never as inputs. 3× pdflatex clean, 36 pp, all gates
  re-run and passing.

### Post-G6 scope amendment (2026-09-05) — status of U_GJS re-based

- **E2 (Level-1 edit, no proof touched).** A8(vi) U_GJS was framed since 16 Aug as an
  "explicit hypothesis" with a quantifier "strengthened" beyond the source. The printed
  record shows the source itself states and consumes that quantifier: (a) pp. 594–595 prove
  Thm 1.1.1 along the affine path h₁+α(h₂−h₁) for *arbitrary* cutoff functions h₁,h₂ of the
  p. 589 class, applying Thm 1.1.7 at every cutoff of the path ((1.1.11)–(1.1.12), "We apply
  Theorem 1.1.7 to each term in the sum"); (b) pp. 596–597 derive Thm 1.1.7's h-independent
  constant from Thm 1.1.8 and (1.1.16) *at the same h*, so accepting CE2 as printed at
  h_{T,g} (Lemma 7.4, Prop C.7) already commits to the h-uniform 1.1.8 constant on the same
  class; (c) p. 629 states the uniformity and identifies 1.1.8 as the case B=I, n=0.
  Edits: new unnumbered `srcfactstar` environment (amsthm `\newtheorem*`, so no counter);
  new item A8(vii′) quoting (a)–(c) verbatim from the page images (`% src:` comments point
  to gjs-theorems-11/12, gjs-proof-14, gjs-uniform-46); Scope paragraph rewritten as the
  three-step argument; title-page "Scope amendment (5 September 2026)"; abstract, overview
  table row (i), Pillar 1, sf:CE1 closing sentence, (vi) title, thm:MAIN imports paragraph,
  App B residue, App C intro reworded from "explicit/strengthened" to "imported at the
  scope at which the source states and uses it". `Assume U_GJS` stays in thm:MAIN and
  prop:discharge — the theorem is still conditional on it; only its status changed.
- **Evidence.** New page image `audit_2026/evidence/gjs-proof-14.png` (p. 597), dossier
  entry E54 + table row; E25's claim text extended by the (1.1.12) affine-path application.
- **C5 extended.** `part_i/C5_reading_record.md`: the 7 original items plus items 8 (p. 595
  affine-path application) and 9 (pp. 596–597 derivation), blank verdict fields, reader and
  date fields. C5 remains open (user-level).
- **Build.** 3× pdflatex: 0 errors, 0 undefined references; 40 pp (was 38). `.aux` diffed
  against the pre-edit baseline: all 125 labels identical in number (2.2–2.8, 3.1, 3.2,
  5.1, 6.3, 7.1, 7.4, 12.2, C.7 unchanged); only page fields and internal hyperref anchor
  names moved. Forbidden-string gate: no new hits (pre-existing whitelisted lines only).
  The overview table's pre-existing 41 pt overfull row (i) removed by the shorter wording.
- **Not done (by design).** No display-by-display h-trace of GJS pp. 598–629 (Level 2) and
  no reconstruction of the expansion (Level 3): Appendix C still audits the mechanism and
  proves two prerequisites only; U_GJS is imported, not re-derived.

### Publication preparation (2026-09-20) — no mathematical content changed

- **Title block.** `main.tex` had `\author{}` and `\date{}` empty. Now: Alexander
  Stottmeister, Institut für Theoretische Physik, Leibniz Universität Hannover,
  Appelstraße 2, 30167 Hannover. The date is pinned to **5 September 2026**, the last
  mathematical change (the A8(vi) scope amendment), not `\today`, so the title page does
  not drift between builds; a comment in the preamble says so. The PDF bytes still carry
  pdftex's build timestamp: a clean-checkout rebuild differs from the working-copy build
  in exactly 66 of 842069 bytes, all inside `/CreationDate`, `/ModDate` and `/ID`, with
  identical rendered text. `SOURCE_DATE_EPOCH=1788566400 FORCE_SOURCE_DATE=1` gives
  byte-identical output, verified by two independent builds. Rebuild: 3× pdflatex,
  0 errors, 0 undefined, 40 pp, 842069 bytes. `.aux` diff vs. the post-amendment
  baseline: all 125 labels identical, and no page number moved either.
- **Repository files added at `glimm_jaffe/` root** (for a planned public repository):
  `README.md` (status statement first: Theorem 12.2 conditional on U_GJS, C5 open with
  blank verdicts, Part II open at gate (II.11), plus the negative scope from the
  abstract), `LICENSE` (CC BY 4.0, verbatim from creativecommons.org, cross-checked
  byte-for-byte against the GitHub licenses API up to line wrapping), `LICENSE-CODE`
  (MIT, verbatim from the same API, placeholders filled), `CITATION.cff` (validated as
  YAML; ORCID, repository URL and Zenodo DOI left as marked blanks).
- **Repository created 20 September 2026, PRIVATE.**
  `github.com/alexander-stottmeister/pphi2-cutoff-removal`, one commit, 120 files,
  17.0 MiB packed. Server-side check of GitHub's own tree listing: 120 files, identical
  to the local index, and zero hits for `refs/`, `evidence/`, `dossier_images`, `*.png`,
  `*dossier*.pdf`, `.aux`, `.log` or `.DS_Store`. **Not yet public**; the flip is
  `gh repo edit --visibility public --accept-visibility-change-consequences`.
  `/glimm_jaffe/` added to the private workspace repo's `.gitignore` so the nested
  repository is never absorbed as a gitlink.
- **Three inclusion decisions (author, 20 September 2026).** Part II ships in the first
  release. AI assistance is disclosed in the README and by `Co-Authored-By` trailers.
  `output/pdf/` was to be dropped only if it were pure duplication, and it is not: of its
  16 files, 6 have rendered text identical to a document already in the tree and are
  excluded by name, while 10 are unique and are kept. Comparing MD5 alone would have
  missed one of the six, a rebuild differing only in its timestamp bytes.
- **Private companion repository (20 September 2026).** The excluded material is now
  version-controlled privately at `pphi2-cutoff-removal-sources`. The two repositories
  share the single working tree `glimm_jaffe/` and track disjoint file sets; nothing was
  moved, so every relative path, build and script is unaffected. Accounting over all 593
  files on disk: 121 public, 255 private, zero in both, and the 217 remainder are
  rebuildable LaTeX artifacts plus the six verified duplicate PDFs. Operational details
  are in `PRIVATE.md`, which the public repository does not track.
- **Not published.** Source PDFs (`refs/`) and every citation page image
  (`**/evidence/`, `part_ii/dossier_images/`) stay out of any repository: third-party
  copyright, and the JSTOR images carry a watermark naming the downloading institution.
  The dossier sources still build without them, with framed placeholders.

### Gate definitions (from strategy.md)

- **G0**: file compiles; every `\cite`/`\ref` in current text resolves; every Assumption has
  a nonempty "Used in" line, and every scheduled consumer names its assumptions.
- **G1/G2**: step maps below complete — every `⟨i⟩⟨j⟩` step of the Lamport source maps to a
  unique environment/display of `main.tex`; no unmapped step, no orphan environment.
- **G3a/G3b**: constants recomputed by hand against `m4/r2-check.tex` and
  `lamport_gap_to_main.tex`; forbidden-string check passes.
- **G4**: citation ↔ dossier bijection; regression greps pass.
- **G5**: 3× pdflatex, zero unresolved; every page rendered and inspected.
- **G6**: adversarial pass; zero confirmed findings or all fixed + re-verified.

## Notation conversion log

| frozen source symbol | unified symbol | reason |
|---|---|---|
| `M_0` (variation bound, `lamport_gap_to_main.tex` ⟨1⟩3–⟨1⟩4) | `\mathfrak m` | collision with moment constant `M`; **plan amendment**: strategy.md D4 originally said `Θ`, which collides with the parity unitary `Θ = Γ(−1)`; `\mathfrak m` adopted instead (recorded also in strategy.md) |
| `p` with `deg \mathcal P = 2p` (`m4/m2-audit.tex`) | `2p'` with `deg \mathcal P = 2p'` | m6/r2-check convention; the p-vs-2p′ change caused the v0 half-degree slip — single convention frozen |
| `\mathcal C` (`m6` §3, cutoff class) | `\mathcal C_E` | three classes named apart (`\mathcal C_E`, `\mathcal C_H`, `\mathcal G`) |
| `γ` in final statements | `m_1` | `γ` reserved for the abstract gap parameter of §§8–10; instantiated once in §11 |
| `K` (compact support region, `m4/r1-check.tex`) | `Λ` | App C only; avoids clash with `K(g)`, `K₁`, `K₂` |
| truncation level `M` (clipped truncations, sources) | `ℓ` | Lemma 4.3; avoids clash with the moment constant `M` (U4) |
| generic integrability exponent `a` (g2m ⟨1⟩1) | `ϱ` | A3 + Prop 8.1; avoids clash with `a = e^{−m₀T}` (U4) |
| `κ`/ultraviolet order (r2-check wording) | `n̄` (printed symbol) | A8(ii); per-factor degree bound per p. 593; avoids clash with App C's mollifier scale κ (U4) |
| `C₀` (mollifier constant, r1-check) | `C_*` | App C; avoids clash with the base covariance `C₀` in M5 (U4) |
| averaging weight `h` (m6 cor:canonical) | `h̄` | Cor 12.3; avoids clash with cutoff functions `h` (U4) |
| Part II rate exponent `θ` (m6 §8) | `ϑ` | §14; `θ` is frozen as the parity automorphism (U4) |

## Step map A: `lamport_euclidean_to_gap.tex` → `main.tex` (gate G1, fills in U1)

| Lamport step | unified item | status |
|---|---|---|
| ⟨1⟩1 (scaling reduction) | Prop. 3.2 `prop:scaling` | done |
| ⟨1⟩2⟨2⟩1 (slab FKN, bounded nonneg) | Lemma 4.1 `lem:slabFKN` | done |
| ⟨1⟩2⟨2⟩2 (signed bounded) | Lemma 4.2 `lem:slabsigned` | done |
| ⟨1⟩2⟨2⟩3 (unbounded/clipped) | Lemma 4.3 `lem:slabunbdd` | done |
| ⟨1⟩3 (slab vacuum) | Lemma 4.4 `lem:slabvac` | done |
| ⟨1⟩4 (moment (M)) | Thm. 5.1 `thm:M2` + Cor. 5.2 `cor:M2phi4` | done |
| ⟨1⟩5⟨2⟩1 (cell count) | Lemma 6.1 `lem:cells` | done |
| ⟨1⟩5⟨2⟩2 (norm bounds) | Prop. 6.2 `prop:gjsnorms` | done |
| ⟨1⟩5⟨2⟩3 (row independence) | Remark 6.3 `rem:row` | done |
| ⟨1⟩6⟨2⟩1 (moment transfer) | Lemma 7.1 `lem:transfer` | done |
| ⟨1⟩6⟨2⟩2 (one-point limit) | Lemma 7.2 `lem:onepoint` | done |
| ⟨1⟩6⟨2⟩3 (two-point lsc) | Lemma 7.3 `lem:twopoint` | done |
| ⟨1⟩6⟨2⟩4 (CE2 strip) | Lemma 7.4 `lem:ce2strip` | done |
| ⟨1⟩6⟨2⟩5 (semigroup decay) | Prop. 7.5 `prop:semidecay` | done |
| ⟨1⟩7⟨2⟩1 (exponential moments) | Lemma 7.6 `lem:expmom` | done |
| ⟨1⟩7⟨2⟩2–⟨2⟩4 (density) | Thm. 7.7 `thm:dense` | done |
| ⟨1⟩8 (gap) | Thm. 7.8 `thm:G` | done |

No unmapped ⟨i⟩⟨j⟩ step remains; the only §3–§7 environment not sourced from
`lamport_euclidean_to_gap.tex` is Lemma 3.1 `lem:classes`, the declared `[new]` item
(plan D8(i)). Environment numbers coincide with the plan codes (checked against
`main.aux`: 3.1, 3.2, 4.1–4.4, 5.1, 5.2, 6.1–6.3, 7.1–7.8).

### G1 record (2026-08-10)

- Step map above complete; `% src:` comments in `main.tex` name file + step/display for
  every transcribed display.
- Statement-level deviations from the sources, all repairs already present in the frozen
  sources and preserved here: none new. The audit repairs L1–L6 appear at: L1 → Lemma 6.1;
  L2 → Lemma 7.2 (sign split); L3 → Thm. 5.1 Step 5 (F₁=F₂=|V(h)|); L4 → Lemma 4.3;
  L5 → Lemma 7.6 (prefactor 2·max{1,C₈K₁}); L6 → Thm. 7.8 (0≤β<m₁).

### G3a record (2026-08-10) — constants recomputed by hand

- Step 3 weight: n+n′ ≤ 4p′; one square K₁K₂^{2(n+n′)}(n+n′)!, two squares
  K₁K₂^{2n}n!K₂^{2n′}n′!; both ≤ K₁K₂^{8p′}(4p′)! = `\mathfrak K(p′)` (K₂≥1, n!n′!≤(n+n′)!). ✓
- Per-pair kernel ‖h1_Δ‖₂‖h1_Δ′‖₂ ≤ 1 (‖h‖∞≤1, unit cells); 3² = 9 ordered pairs;
  ‖Q_V‖ ≤ 9`\mathfrak K(p′)`λ²(Σ|aₙ|)² = M²/C₈. ✓ matches r2-check Prop. 2.1.
- φ⁴ (p′=2): (4p′)! = 8! = 40320; 9·40320 = 362880; K₂^{8p′} = K₂^16. ✓ matches
  r2-check Cor. 2.2.
- `\mathfrak n(X_f^n)`² = K₁K₂^{4n}(2n)!N_I^n‖f‖₂^{2n} = K₁(K′)^{2n}(2n)! with
  K′ = K₂²N_I^{1/2}‖f‖₂ since (K₂²N_I^{1/2}‖f‖₂)^{2n} = K₂^{4n}N_I^n‖f‖₂^{2n}. ✓
- Ĉ_Q branches: t>2 gives C₇e^{2m₁}e^{−m₁t}‖Q‖²; 0≤t≤3 gives ‖ψ_Q‖² ≤
  e^{3m₁}e^{−m₁t}‖ψ_Q‖² (e^{3m₁−m₁t} ≥ 1 for t ≤ 3); branches cover [0,∞). ✓
- CE2 strip: rows at ±t/2 ⊆ [±t/2−1, ±t/2+1]; separation ≥ t−2;
  e^{−m₁(t−2)} = e^{2m₁}e^{−m₁t}. ✓
- Cell counts: N_I ≤ ⌊L⌋+2 (integer j_max−j_min−1 < L ⇒ ≤ ⌈L⌉−1 ≤ ⌊L⌋); length-2
  support meets ≤ 3 cells in positive measure (4 cells ⇒ length > 2). ✓
- Forbidden-string grep: pass (all hits whitelisted).

## Step map B: `lamport_gap_to_main.tex` → `main.tex` (gate G2, fills in U2)

| Lamport step | unified item | status |
|---|---|---|
| ⟨1⟩1⟨2⟩1 (semigroup path regularity) | Prop. 8.1 `prop:pathreg` | done |
| ⟨1⟩1⟨2⟩2–⟨2⟩3 (projection/gauge/derivatives) | Prop. 8.2 `prop:projreg` | done |
| ⟨1⟩2 (filter) | Lemma 9.1 `lem:filter` | done |
| ⟨1⟩3 (separation) | Lemma 9.2 `lem:separation` (M₀ → `\mathfrak m`) | done |
| ⟨1⟩4 (unbounded clustering) | Lemma 9.3 `lem:cluster` | done |
| ⟨1⟩5⟨2⟩1 (state derivative) | Lemma 10.1 `lem:statederiv` | done |
| ⟨1⟩5⟨2⟩2 (localization) | Lemma 10.2 `lem:localize` | done |
| ⟨1⟩6⟨2⟩2 (two-regime bound) | Lemma 10.3 `lem:tworegime` | done |
| ⟨1⟩6⟨2⟩1,⟨2⟩3–⟨2⟩5 (one path incl. shells) | Prop. 10.4 `prop:onepath` | done |
| ⟨1⟩7 (rate function) | Lemma 10.5 `lem:rate` | done |
| ⟨1⟩8 (Cauchy/limit/rate) | Thm. 11.1 `thm:cauchy` | done |
| ⟨1⟩9 (normality) | Prop. 11.2 `prop:normal` | done |
| ⟨1⟩10 (ground state, incl. α-invariance) | Prop. 12.1 `prop:spectral` | done |
| ⟨1⟩11 (translation/parity invariance) | inside proof of Thm. 12.2 `thm:MAIN` (via Lemma 2.8 `lem:covparity`) | done — consolidated, see note |
| §4 (averaged vacuum) | Cor. 12.3 `cor:canonical` | done |
| §6 ((B1)–(B4) analysis) | §13: Hyp. 13.1 + Thm. 13.2 proved; scope Remark 13.3 `rem:gjs7576` | done |

Consolidation note: the plan codes P12.2–P12.4 (α-/translation-/parity-invariance as
separate items) were realized as in the audited source `m6/main.tex` v2:
α-invariance is part of Prop. 12.1's conclusion, translation and parity invariance are
proved inside Thm. 12.2's proof from `eq:T`/`lem:covparity` and conclusion (1). No content
was dropped; the m6 v2 environment map is prop:M0-main(i) → 12.1, prop:M0-main(ii)(iii) →
Lemma 2.8 (landed in U0), thm:MAIN → 12.2, cor:canonical → 12.3.

### G2 record (2026-08-10)

- Step map above complete; every ⟨i⟩⟨j⟩ step of `lamport_gap_to_main.tex` ⟨1⟩1–⟨1⟩11 + §4
  maps to a unique environment; `% src:` comments mark each transcription.
- The audited v0→v1 repairs remain in place: filter transform is +1/E
  (`eq:filterdef`/`eq:filterid`, checked: symbol of ∫W_γ(t)e^{itH}dt is Ŵ_γ(E)=1/E on
  [γ,∞)); no spurious ½ in the one-path bound (4M × 8 shells = 32M).
- One added justification beyond the source (explicitness, not new math): C¹ of
  E_s = −T⁻¹log λ_s via λ_s = ⟨Ω_s, L_sΩ_s⟩ in Prop. 8.2's proof.

### G3b record (2026-08-10) — constants and identities recomputed by hand

- Exponents: 1/r_T+1/q_T = (1+a)/2+(1−a)/2 = 1; r_T·p_T = 2; (p′_T−1)/(p_T−1) = a⁻² =
  e^{2m₀T}; Hölder pair 1/p_T+1/p′_T = 1/(1+a)+a/(1+a) = 1. ✓
- Separation: a = R/γ ⇒ both exponentials e^{−γR/2}; 2a/(πR²) = 2/(πγR) ≤ 2/π < 1 for
  γR ≥ 1; 1+2/π < 2 ⇒ prefactor 2`\mathfrak m`. Gaussian tail ∫_{|t|≥R}|f| ≤ (a/πR²)e^{−R²/(2a)}
  via t⁻¹ ≤ t/R². ✓
- Two-regime threshold: γd₀/2 = γ(4+2/γ)/2 = 2γ+1 ≥ 1. ✓
- One-path: 2 (outer Re factor) × 2M (bracket) = 4M per j; shells: j ∈ [b+n−1, b+n+2]
  contains ≤ 4 integers, ×2 sides = 8; 4M·8 = 32M. B_j one-sided since |B_j| ≤ 2 <
  8 ≤ |O_d|. ✓
- Rate: geometric tail ratio e^{−γ/4}; T_γ(n/2) ≤ 2^q C_{q,γ}(1+n)^{−q}, q = N+2;
  ⌊d⌋ ≥ d−1 ≥ (3/5)(1+d) for d ≥ 4 (equality at d=4). ✓
- §12: |ρ_g|(ℝ) ≤ ‖A‖‖B‖ (Cauchy–Schwarz); averaged vacuum: plateau [−3n,3n] shifted by
  ≤ n contains [−2n,2n] ⇒ d ≥ 2n−R uniformly. ✓
- Forbidden-string grep: pass (all hits whitelisted).

### G4 record (2026-08-10) — citation ↔ dossier

- All 39 distinct page images named in the (A1)–(A8) *Dossier* lines exist in
  `audit_2026/evidence/` (script check; shorthand ranges expanded). Unreferenced evidence
  files are the contextual/historical images (GJ III/IV, AHZ, BDW, RZT, GJS 75/76 pages,
  Lamport method pages, covers) backing intro/§13/§14 statements; they are indexed by the
  dossier document itself.
- Regression greps: pass (all hits whitelisted).

### G5 record (2026-08-10) — certification build

- 3× pdflatex: 0 errors, 0 unresolved references/citations; 34 pages.
- All 34 pages rendered; 15 inspected page-by-page in detail (1–9 odd, 11, 13, 15, 17,
  20, 22, 24, 26, 28, 30, 32, 34), remainder spot-checked — no clipping, no garbled
  displays.
- Residual layout debt: 5 overfull hboxes, worst 23.9pt (the two dependency-graph arrays
  at `\small`, one intro paragraph, two displays) — all far inside the 82pt margin.
- Layout fixes applied during U3: printed-norm display split (`gathered`), notation and
  App-B tables converted to wrapping `p`-columns, dossier lines set ragged-right,
  `\allowbreak` after `audit_2026/` in file paths, slab-objects display split, one
  `\sloppy` paragraph in Thm. 5.1 Step 1.

### U3 content record

- §13: dichotomy proof transcribed from `m6/main.tex` cor:nobreak (v2) — uniform cutoff
  clustering via Lemma 9.3 (X = B bounded), local-norm passage, midpoint identification
  (B4), long-range order; plus Remark 13.3 (GJS 75/76 scope; audit P1 disposition).
- §14: discussion from `m6/main.tex` §8 (v2); Part II compressed to ONE paragraph per
  plan D8 (obstruction liminf + fixed-coarse status + pointer); added "Standing scope"
  paragraph.
- App C: full transcription of `m4/r1-check.tex` §§3–5 — five mechanisms M1–M5,
  Prop. C.1 structural uniformity, Lemma C.2 (Z(h) ≥ e^{−λ|a₀||Λ|}), Lemma C.3 (Wick
  lower bound, h≥0 entry), Lemma C.4 (UV difference, h≤1 entry), Thm. C.5 (h-uniform
  stability, 2q = e^{L/(4p′)}), Remark C.6, Prop. C.7 (discharge). Notation conversions:
  V(h)→`\mathcal U_h` (Euclidean), `\mathcal C`→`\mathcal C_E`, compact set K→Λ (avoids K(g)/K₁/K₂ clash — logged
  below). The chaos moment comparison ‖X‖_q ≤ (q−1)^{r/2}‖X‖₂ is derived in two lines
  from the abstract form of A4's source (P_t = Γ(e^{−t}), P_tX = e^{−rt}X) rather than
  imported blind.
- App A: all "defined in" pointers now real labels; draft-status box updated to
  "U3 complete / U4 pending".

## U0 transcriptions (statement-level, already in `main.tex`)

| unified location | source | note |
|---|---|---|
| abstract | `m6/main.tex` abstract (v2) | forward pointers adapted |
| §1.1–1.3 | `m6/main.tex` §1 (v2) | refs adapted; dependency graph added from `critical_proof_audit.tex` §3 |
| §2.1 | `m6/main.tex` §2.1 (v2) | verbatim + h-class widened to L¹∩L² compact support |
| §2 (A8)(iii) printed norms | `m4/r2-check.tex` Source Fact 1.1 | page image p.594 |
| §2 (A8)(iv)(v) CE2/CE1 | `m6/main.tex` sf:CE2/sf:CE1 (v2) | verbatim |
| §2 (A8)(vi) p.629 sentence | `m4/r1-check.tex` sf:printed | verbatim quote |
| §2 rem:conv | `m6/main.tex` rem:conv (v2) | verbatim |
| §2 prop:smoothing | `m6/main.tex` prop:standard-main(i) (v2) | proof transcribed |
| §2 prop:propagation | `m6/main.tex` prop:standard-main(ii) (v2) | proof transcribed |
| §2 lem:covparity | `m6/main.tex` prop:M0-main(ii)(iii) (v2) | proofs transcribed |
| §2.5 weak coupling | `m6/main.tex` §2.2 (v2) | verbatim |
| §12 thm:MAIN | `m6/main.tex` thm:MAIN (v2) | statement; imports paragraph re-pointed to (A1)–(A8); proof U2 |
| §13 hyp:broken + thm:dichotomy | `m6/main.tex` cor:nobreak (v2) = `m3` hyp:broken/thm:dich | statements; proof U3 |
| App A | `m4/r2-check.tex` Prop 2.1/Cor 2.2 + `lamport_gap_to_main.tex` | values pending G3a/G3b re-verification |
| App B | audit register + R1/R2 + merge history | complete |

## Forbidden strings (checked at every gate; scope: `part_i/main.tex`)

Any hit must be on a line carrying the marker `% negative-scope mention (whitelisted)`,
which is reserved for statements that explicitly record what a source does NOT provide.

```sh
grep -n "III\.12\|V\.10\|V\.12\|Theorem 7\.3\|Thm\.~7\.3\|conditional only\|e_\*" main.tex
grep -n "L+1" main.tex                     # forbidden as a cell count
grep -n "K_2^{N(" main.tex                 # single-power local weight (OCR artifact)
grep -n "(2p')!" main.tex                  # only legitimate adjacent to K_2^{4r}/(2r)! contexts, NOT with K_2^{4p'}
grep -n "32" main.tex                      # cell-pair count must be 9; 32M in §10 is legitimate (LPPL prefactor)
```

Notes: `32M` in §§10–11 and App A is the legitimate LPPL prefactor; the forbidden `32` is
only as the (M₂) cell-pair count in §5. `(2r)!`/`K_2^{4r}` in §6 is the legitimate
squared-observable weight; the forbidden pattern is `(2p')!` with `K_2^{4p'}` in §5.

### Re-sourcing of A8(vi) and documentation repairs (2026-10-31) — Phases 0′ and 0 of `ugjs/PLAN.md`

- **E3 (re-sourcing, no proof touched).** A8(vi) is read off the printed Theorem 1.1.11 of
  GJS: (1.1.16) is printed "uniformly in h" (p. 596), and GJS's own proof of Theorem 1.1.8
  on p. 600 is its specialization "Choose T = 0 and B = I in Theorem 1.1.11. Then Q = 0"
  (named again on p. 629). A new unnumbered `srcfactstar` inside item (vi) quotes pp. 596,
  600 and 629 verbatim (`% src:` comments; new evidence images `gjs-thm1111-13.png`,
  `gjs-proof118-17.png`, private corpus); a reading paragraph gives the literal basis
  (B = I, n = 0, any 0 < T < 1 inside the printed T > 0; the integer time translation;
  C_8 = O(1) K_1; the localization step; the smallness hypotheses printed with Theorem 4.1,
  p. 628, and on p. 600). The Scope paragraph is rewritten (one import standard; why the
  5 September 2026 reading stopped short; the two readings are the same mathematics; point
  (b): Theorem 1.1.7's printed proof reaches sharp-time monomials only across strips parallel
  to the time-zero line, the case Lemma 7.4 uses; point (c): the source's proof is not
  re-verified, as for A1–A7). "Assume U_GJS" is removed from Theorem 12.2 and Proposition
  C.7; the imports paragraph, title page (new dated paragraph; the two earlier ones marked
  superseded), abstract, §1.2 (quotation, table row (i), graph), §1.4 Pillar 1 and the
  density sentence, §2.6 (ε_P defined through the printed hypotheses of Theorems 1.1.7 and
  1.1.11), Lemma 4.3's wording, Appendix B (corrections entry; External residue now lists
  C5 items 1–4, 9 and 12–13 as carrying the imports and items 10–11 the disclosure) and the Appendix C introduction are reworded.
  `\date` is 31 October 2026; the pinned build epoch is 1793404800.
- **E4 (documentation repairs, PLAN Phase 0).** A8(ii) names the time-integrated monomials
  (1.1.6) and the square convention of p. 593 (finding F3); Appendix C's mechanism audit gains
  item M6 (the stability input (2.4.34)–(2.4.35) of p. 624 with K_2 ≥ K_3², cited to
  Dimock–Glimm, which items M1, M3–M5 had declared absent; finding F1, MAJOR against the
  narrative, no theorem affected), M2's "Dirichlet" becomes "decoupled" and M1's e^{τt}
  becomes e^{γt} with the script-K_2 correction (F11), Proposition C.1's limitation and
  Remark C.6 are narrowed. "uniformly as h↑1" became "h → 1" (F14).
- **Build (gate G-0/G-0′ record).** 3× pdflatex with `SOURCE_DATE_EPOCH=1793404800
  FORCE_SOURCE_DATE=1`: 0 errors, 0 undefined, 0 Overfull, 5 Underfull (unchanged), 42 pp (was
  40). The pre-edit build (commit 65e31bb) and the first Phase 0 build carried 9 Overfull boxes (widths 0.17,
  0.28, 1.47, 2.63, 9.33, 9.80, 18.87, 22.41, 23.88 pt); a layout pass on 2 November 2026
  removed them without changing any statement's number or page (the §1.2 dependency graph set
  at footnote size, one display split and one tightened, Appendix A's table with 4 pt column
  padding, four sentences reworded). `.aux` diffed against the pre-edit baseline: all 125
  labels identical in number. `grep -c 'Assume \$U_{\rm GJS}'` and the broader
  `grep -i 'assum[a-z]*[^.]*U_{\rm GJS}'` print 0 (they found 4 lines before). Forbidden
  strings: none. `main.pdf` sha256 begins 4c37f0272c8341e2. Page inspection: pp. 1, 11–13
  rendered and read by the orchestrator after the first pass; pp. 1, 11–13, 38 by the fresh
  verifier (V0), all 17 changed pages of the pre-layout build (pp. 1–5, 10–15, 18, 32, 37–39,
  41) by the verifier (V0b), and pp. 4, 9, 13, 15, 32, 33, 35, 36, 37, 39 of the current build
  by the orchestrator after the layout pass. Fresh reader, round V0/V0′
  (`ugjs/council/v0-verifier-report.md`): "can be committed after the listed fixes" — 4 CRITICAL
  (three quotation glosses, and generated figure and interactive-page texts still saying
  "conditional"), 6 MAJOR, 19 MINOR, all applied; the verifier's byte-identical rebuild of
  `main.pdf` confirmed the pinned epoch. Round V0b (`ugjs/council/v0b-verifier-report.md`):
  "Not yet" — C1–C4, M1–M4 and M6 fixed; two new MAJOR (a false clause in Scope point (d); the
  C5 counts after item 13b, since folded into item 13), M5 open (the nine boxes; five V0 MINOR
  items undone), 8 new MINOR; all applied on 2 November 2026. Round V0c
  (`ugjs/council/v0c-verifier-report.md`, 2 November 2026): N1, N2, M5(a), M5(b) and n1–n8
  fixed, the layout pass changed no mathematics (byte-identical rebuild, sha256 4c37f0272c8341e2,
  every label on its page), companion 20 pp; "Not yet" on one new item only: the gate-record
  edit had duplicated 314 lines of this file (sections repeated, the 5 September bullets inside
  this record), repaired the same day by restoring the single copy and checked by diff against
  the committed file; two of its three optional MINOR items applied (the open readings named
  beside F-0′ in README.md, docs/status.md and docs/imports.md; the "implication" sentence of
  docs/status.md reworded), the third kept (strategy.md's "G-0 now met", true once this round
  is recorded). Round V0d (V0d section of the same report, 2 November 2026): the repair
  confirmed against the verifier's saved copies of the corrupted file, the optional items
  settled; final word "commit". Gate G-0′ passed on 2 November 2026.
- **C5 extended.** `part_i/C5_reading_record.md`: item 2 extended (p. 593's "no restriction on
  r"); items 10–13 added (pp. 593/595; p. 594; pp. 596–597; pp. 600 and 628), blank verdict fields.
- **Record elsewhere.** `docs/status.md`, `docs/imports.md`, `docs/index.md`,
  `docs/_config.yml`, the README's Status section and figure paragraph, `CITATION.cff`, a
  notice in the companion; `docs/results.*` regenerated. Plan and council record:
  `ugjs/PLAN.md`, `ugjs/council/`.

### Integration of Appendix D (2026-11-07) — gate GI of `ugjs/PLAN.md`, Checkpoint 2 answered

**Decision.** The author's answers to Checkpoint 2 (PLAN Part 11), given on 7 November 2026: integrate the comparison note as Appendix D, as a dated amendment (6: yes); name the transverse case A8(iv)-T (8: yes); revise the companion now (9); update docs, README, CITATION and KB with the integration (10); apply the repairs. Question 7 (Phase C) is open; the orchestrator's recommendation is recorded in KB `glimm_jaffe:decision/checkpoint-2-integration`.

**What changed in `main.tex`.** New Appendix D (`app:comparison`) from `ugjs/comparison.tex` with `ugjs/parts/` (notation, d1–d4, quantifiers, constants A.1–A.4; the note's §1 purpose rewritten as the appendix introduction; its §8 applied in place; its Appendices A.5–A.6 and B stay in `ugjs/`); the auxiliary numbering N.k is kept (N.47 of the note's §8 omitted, `\stepcounter`), and Lemma N.23′ (`aux:notation-ident`) is new. Replaced in §§4–7 per the replacement blocks of `ugjs/parts/consequences.tex`: Lemma 4.3(ii); Theorem 5.1 (statement M := M_B; Step 1 rewritten on the constructed V(h); Steps 2–4 on GJS columns; Step 5 cites Theorem D.4); Corollary 5.2; §6 (N_I on columns; Lemma 6.1; Prop. 6.2 proof); Lemmas 7.1–7.3, 7.6; the radius in the proof of Theorem 7.7. A8: item (iv-T) added, (v) provenance, (vi) retired, Scope (a), (b), (d) and Used in rewritten; §2.6 names one theorem; Theorem 12.2's imports paragraph names one GJS theorem; Prop. C.7 restated. Repairs: Appendix C (V3 audit R1–R10 and m-1–m-9, with the deviations recorded in KB `correction/appendix-c-analytic-facts-unproved-inputs`); Wick powers constructed in A1 (time-zero) and A3 (Euclidean) from Simon pp. 10–12, 15–17, 25, 34, 38, 134–138, 152 (read on the page images; images in `audit_2026/evidence/`, private companion); the locality of V(h) proved in §2.1; "0(1)" [sic] in A8(vii′)(a) and C5 item 8(a). Front matter: dated title-page notice, `\date{7 November 2026}`, abstract, §1.2, §1.4; Appendices A and B updated. Reproducible build: `SOURCE_DATE_EPOCH=1794009600 FORCE_SOURCE_DATE=1`, three runs.

**Gate GI.**
- G0: three `pdflatex` runs: 0 errors, 0 undefined, 0 Overfull; every assumption has a Used in line.
- `.aux`: the 125 labels of the build of 2 November 2026 keep their numbers (119 numbered + 6 tagged); 105 labels are new (D.1–D.4, N.1–N.55 with N.23′, equations W.1–W.4, C.a–C.c, Appendix D's equations).
- G1/G2 step map C (`ugjs/parts/consequences.tex` → `main.tex`): block `sec6-NI` → `lem:cells`, `prop:gjsnorms`, notation table, A8(ii), Theorem 5.1 Steps 2–4; `lemma-4.3-ii` → `lem:slabunbdd`(ii); `lemma-7.1` → `lem:transfer`; `lemma-7.2` → `lem:onepoint`; `lemma-7.3` → `lem:twopoint`; `lemma-7.6` → `lem:expmom` and the radius in the proof of `thm:dense`; `theorem-5.1` → `thm:M2` (statement, Step 5; Step 1 rewritten beyond the block on the construction of V(h), see V4); `corollary-5.2` → `cor:M2phi4`. Appendix D's subsections D.a–D.g are the note's §§2–7 and Appendix A.1–A.4.
- G3: the constants of Appendix D were recomputed by hand in the note (Appendix A, independently of the drafts; re-recomputed in V2/V2b); the new constants of Appendix C (C_*, C(P), C_{p′}, b(P), c_1, A_n, B_n(R), c_2, b_0′, b_1, b_2(p), b_*) were re-derived by hand by both V4 auditors.
- G4: the new citations of Simon's book (A1, A3, A4) and of GJ2 p. 397 (A6(iii)) have page images in `audit_2026/evidence/` and in the Dossier lines of A1, A3, A4, A6; the dossier index `audit_2026/citation_screenshot_dossier.tex` is not updated (not run).
- G5: build checks as in G0; the 110 pages were not each inspected visually (not run).
- G6 = rounds V4 and V4b: see below.
- Forbidden strings: clean. GB1 grep: every surviving hit of `U_{\rm GJS}`/`UGJS`/`C_8` is provenance, history, the retired item, a comment or a negative statement of Appendix D; `\eqref{eq:UGJS}` occurs only inside A8 (vi), (vii′) and Scope (a); `grep -c 'Assume $U_{\rm GJS}'` = 0.
- `docs/results.*` and `companion/council/labels.md` regenerated (65 statements, 34 reaching A8; A1 and A3 are marked because their Scope sentences cite Assumption A8, Scope (d), and the extractor counts an assumption's own references as its uses); `docs/figures/imports-dag*.svg` regenerated.

**Audits.** V4 (7 November 2026, two fresh Opus agents that wrote nothing): (i) mathematics of the new and repaired parts (A1/A3 Wick paragraphs against the Simon page images, Appendix C, Lemmas N.19 and N.23′): every display, constant and threshold re-derived; no CRITICAL; one MAJOR, inherited (the affiliation of V(h) with A(U) asserted in §2.1 without argument; KB `correction/v-h-affiliation-unproved`), ten MINOR; all V3 items M-1–M-3, m-1–m-9 closed. (ii) Integration consistency (every replaced proof against its block; every status sentence; Appendix D against the note by a token-level diff; the mechanical checks): no CRITICAL, no MAJOR, 29 MINOR items listed (B1–B3 and M1–M26; the report's verdict line says "26 MINOR findings", counting B1 and B2 among them and M26 as optional; three of the 29 were about records not yet written: this gate record, Appendix A's G3 sentence, the dossier sentence). Every finding was fixed on 7 November 2026. V4b (the same two auditors re-checking every fix — V4b to V4e are re-checks by the V4 agents, not fresh ones; reports returned as messages): (i) mathematics: F1–F11 closed, the new Locality proof checked step by step; six new MINOR items N1–N6, fixed the same evening. N1: §2.1 stated the affiliation for intervals only, while the proof of Proposition 2.7 and Lemma 9.3 need disjoint sets that are not intervals; §2.1 now proves affiliation with the algebra M_U of the W(f,0), f ∈ C_c^∞(U), for every bounded open U ⊇ supp h, and with A(O′)′ for every bounded open interval O′ at positive distance from supp h, using only the locality of the net over intervals; the hypothesis of Lemma 9.3, its two callers (Lemma 10.3, Theorem 13.2) and the proof of Proposition 2.7 are restated accordingly. N2: A1(d) is stated for n ≥ 1, the n = 0 term being the constant ∫g. N3: the z-independence of c_κ is cited for κ ≥ 2, the only range used. N4: A2 is named among the inputs of Appendix C (and Appendix C in A2's Used in). N5: three Simon images named in the Dossier lines (simon-gaussproc-037, simon-gamman-038, simon-wickdef-156) were missing from `audit_2026/evidence/`; they were copied in before the report arrived. N6: "the only h used below" now reads "the only h for which a proof below uses V(h)". (ii) Integration: 26 of 29 items closed; B1 was this record, written the same evening; B3 closed by the same three images, named in the dossier table above; M26 partly closed (the overloaded symbols A, B′, Γ of §D.g are kept, by decision); four residual MINOR items R1–R4 fixed: Proposition C.7 says "the case the printed proof reaches" of Lemma 7.4 only and refers Theorem D.3 to Remark N.39; the A8(iv)-T heading and the Simon pages in `docs/imports.md`; §D.g's list of the new rows of Appendix A; the "What this carries" lines of C5 items 9 and 12. After these fixes: three `pdflatex` runs, 0 errors, 0 Overfull, 0 undefined, 110 pages; all 230 labels keep their numbers (15 moved by one page). V4c (the mathematics auditor re-checking the fixes of N1–N6): all six hold, the N1 repair checked step by step (components, smoothness of the pieces, the d/2-neighbourhoods, the strong-density extension in Proposition 2.7, every consumer of the affiliation); four residual MINOR items, fixed the same evening: R1, A3's Wick bound was still stated for n = 0 (now n ≥ 1, the n = 0 term the constant ∫g); R2, the locality of the net, A(O) ⊆ A(O′)′ for disjoint O, O′, was used (Lemma 9.3, Theorem 13.2, the Locality paragraph) but neither listed nor sourced — now Assumption A6(iii), from GJ2 p. 397 (proof of Theorem 3.5.1; page image `gj2-locality-37` added to the dossier), with the identification of the source's algebras (bounded functions of φ(f) and π(f)) with the A(O) of §2.1 (generated by the W(f,h)) stated as a reading, the one under which A6(i)–(ii) are imported; R3, "every h whose locality is used below is bounded"; R4, the n = 0 case in the proof of Lemma N.23′(ii). After these fixes: three `pdflatex` runs, 0 errors, 0 Overfull, 0 undefined, 110 pages; all 230 labels keep their numbers (49 moved by one page against the build of 22:52); `docs/results.*`, `companion/council/labels.md` (65 statements, 34 reaching A8) and the figures regenerated. V4d (the same auditor, on the fixes of R1–R4): all closed; the quotations of A6(iii) checked word by word against the page image; one MINOR point: the Scope paragraph called the identification of the source's algebras with A(O) "a reading", while one inclusion, A(O) ⊆ 𝔄(O), is mathematics resting on the Weyl relations, which the record neither states nor imports. Repaired the same evening by a change of presentation, not by an import: §2.1 now writes the generators of A(O) as the sources do, W(f,0) = e^{iφ₀(f)} and W(0,h) = e^{iπ₀(h)} (equivalently, the bounded Borel functions of φ₀(f) and π₀(f)), so that the only reading left is the Fock space–Q-space dictionary already recorded in A1's Scope; no proof uses another generator (the maps θ and σ_s are applied to W(f,h) in general and need only these special cases). `docs/definitions.md` follows. Rebuilt: 0 errors, 0 Overfull, 0 undefined, 110 pages; all 230 labels keep their numbers (26 moved by one page against the build of 23:07). V4e (the same auditor, on this change): the change holds — with only the dictionary reading, the source's algebra and the new A(O) coincide (both inclusions), and no proof uses a generator W(f,h) with f and h both nonzero; two MINOR points, fixed the same evening: A6's Scope said the manuscript does not use the Weyl relations, while the dilation remark of §3 (Remark 3.3) presupposes them for its scaling automorphism (now said, with the note that only its action on W(f,0), W(0,h) enters σ_s(A(O)) = A(sO)); π₀ was used without being defined (now defined in §2.1 as the sources' π(x,0) carried to Q-space by A1's dictionary). Not checked by V4e: the rest of Remark 3.3, Θπ₀(h)Θ = −π₀(h), the translation covariance of the net (all unchanged). Final build (23:19): three `pdflatex` runs, 0 errors, 0 Overfull, 0 undefined, 110 pages; 230 labels, the 125 of 2 November with unchanged numbers; no label moved after V4e. In the same pass Appendix D's "One case of Theorem 1.1.7 is used" became "A case …" (KB reviewer's note); the two history entries of 31 October that say "the one case" are kept verbatim as history.

### Status review (2026-11-09 to 2026-11-11) — site repair, stale documentation, the free-field finding (round V4f)

**Request.** On 9 November 2026 the author asked for a review of the status and of its loose ends. In this unit nothing in `part_i/` changed except this record: `main.tex` and `main.pdf` are those of 7 November.

**Checks that came out in order (9 November).**
- All repositories clean and in sync with their remotes; guard self-test "49 passed, 0 failed".
- Fresh clone of f213cc8, three passes with `SOURCE_DATE_EPOCH=1794009600 FORCE_SOURCE_DATE=1`: `part_i/main.pdf` is byte-identical to the committed file (sha256 `f1962e11…db41e`; 110 pp; 0 errors, 0 Overfull, 0 undefined; empty `??|TODO|Hmm|wait,` grep), and so is `companion/companion.pdf` (sha256 `1aeab355…53aa`; 20 pp).
- `docs/extract.py --check`: "up to date"; `companion/council/make_labels.py`: "65 statements, 230 aux labels, 34 reach A8"; every generator leaves the clone unchanged; 74 relative links, 0 unresolved.

**Finding 1 — the site was not rebuilt after the integration.** Every GitHub Pages build since commit 231b8ea failed (runs 42420438670, 42462365937, 42463067765 of 7–8 November; last success 41927520564 for 910959d). The log: "Liquid syntax error (line 425): Variable '{{:}' was not properly terminated". Cause: item (c) of A1's Wick-powers paragraph contains two opening braces in a formula; `docs/extract.py` copied it into a fenced block of `docs/results.md` (l. 429), and Liquid processes fenced blocks too. The live site kept serving the build of 4 November (commit 910959d), which carries the status of 31 October. The gate record above says "`docs/results.*` … regenerated"; that was true of the files and nobody looked at the deployed build. Fixed on 11 November: the inventory is generated inside one raw block; `docs/extract.py --check` fails on a Liquid delimiter outside a raw block in any page of `docs/`. Checked before the push with Liquid 4.0.4 (the version of the Pages toolchain, github-pages v232): the committed `results.md` reproduces the error word for word, and the regenerated file and the six other pages render. **New gate item for every push that touches `docs/`: the `pages-build-deployment` run of the pushed commit succeeds, and the live page is read.**

**Finding 2 — public text left at an earlier state.** README "Building" (42 pages for 110; epochs 1793404800 and 1792800000 for 1794009600, with which "byte for byte" was false); the banner of the figure pages (`docs/assets/figure.js`), `docs/interactive/imports.html`, `affine-path.html` and `index.html`, and the import graph (`docs/figures/make_figures.py`, both `imports-dag` SVGs), all of which still described U_GJS as an import; `docs/notation.md` (a constant C₈ the record no longer has, N_I counted on unit cells, no row for the constants of Appendix D, "Appendix A, p. 35" for p. 42); `docs/provenance.md` (no entry for 7 November); the gate table of `docs/status.md` (no row GI; G4 and G5 not marked as not re-run); `docs/imports.md` (A1–A7 called "literal quotations" although A1 and A6 are applied under a declared reading; the A7 row said "translation covariance and parity"); the page numbers printed on six figure pages (`plateau`, `weak-coupling`, `uniform-gap`, `rate`, `two-regime`, `dichotomy`), which were those of an August build. All corrected on 11 November; the page numbers of the figure pages are now filled from the `.aux` by `docs/extract.py`, and `--check` fails when they are stale. The integration auditor had listed "docs/, the root README, CITATION.cff, KB, companion" as not checked.

**Finding 3 — round V4f: the free-field layer.** Two edits of 7 November, made after round V4e, had no audit: the sentence of §2.1 that introduces π₀ (ll. 431–433) and the parenthesis on the Weyl relations in A6's Scope (ll. 904–910). V4e had also listed three items as not checked. A fresh Opus agent audited these on 9 November, read-only (`../ugjs/council/v4f-free-field-report.md`); the orchestrator re-read each finding at the source. Severities are the auditor's.

| | severity | locus (`main.tex` of 7 November) | finding |
|---|---|---|---|
| F1 | MAJOR | §2.1, ll. 431–433; l. 513 | π₀ is introduced by reference to a dictionary that A1's Scope states for V(g) only (ll. 681–684); no page, formula or property; the "Equivalently" clause needs π₀(f) self-adjoint. H₀ is used from l. 513 on and defined nowhere. |
| F2 | MINOR | l. 434; ll. 346, 667 | φ₀(f) used before its definition (ll. 599–607); Ω₀ used before its value is stated (l. 1505). |
| F3 | MINOR | l. 434 | W(f,h) written for all f, h; nothing makes φ₀(f) + π₀(h) essentially self-adjoint. |
| F4 | MAJOR | Remark 3.3, ll. 1459–1465 | The dilation unitary U_s is asserted: Weyl relations, the Fock state on W(f,h) and cyclicity of Ω₀ are not stated; the covariance identity covers the field half only. The standing assumption of §2.6 (ll. 1350–1354) rests on it. A8(viii) imports the Euclidean scaling of GJS, p. 590, on L²(S′(ℝ²)) only. |
| F5 | MINOR | ll. 1466–1469, 1482–1486 | The formulas check by hand; the V identity is justified through the Euclidean identification; the factor s in the moment constant is implicit. |
| F6 | MAJOR | A7; ll. 2892–2898, 2988, 3001–3002; Cor. 12.3 | τ_a is defined on functions only; τ_a(A(O)) = A(O + a) is used and neither derived nor imported (A7 imports U_aK(g)U_a* = K(τ_a g) alone). |
| F7 | MAJOR | ll. 2900–2902 | Θπ₀(h)Θ = −π₀(h) is used for θ(A(O)) = A(O) and neither derived nor imported. |
| F8 | MINOR | ll. 3254–3255 | "written as in the sources": GJ2 p. 397 writes bounded functions of the smeared fields, not Weyl operators. |
| F9 | MINOR | A6(i), l. 877 | "propagation speed one" is not stated as the inclusion Proposition 2.7 uses. |
| F10 | MINOR | Remark 3.3 | A(O) carries no mass label. |
| S1 | MINOR (orchestrator; not audited) | A7's source, dossier E06 | GJ2 p. 398 prints the cutoff-independence condition with ">" where the orchestrator reads "<" (compare p. 397, (3.5.1)); neither the record nor the dossier says so. The dossier names this page for A6 as well as for A7; the patching identity (P) itself is printed, with "g ≡ 1 on B_t", as Theorem 4.1.2 of GJExp (p. 42, image `gjexp-056`, read on 11 November). |

Checked and found correct by the auditor: the Trotter step of Proposition 2.7; Lemma 2.8, given τ_a = Ad U_a; σ_s(A(O)) = A(sO), given U_s. Re-read in full by the orchestrator: F1–F4, F6–F10 and the factor s of F5; the auditor's alone are F5's judgment on how the V identity is justified and its statement that §§9–10 use the net only through Proposition 2.7, the Locality paragraph and A6(iii). No step is known to be false; the four facts behind F1, F4, F6, F7 are standard properties of the free field. All four gaps are in commit 910959d already (there l. 379 uses π₀ and l. 395 uses H₀, neither defined); the sentence of 7 November that introduces π₀ did not close the first. **Standing until the repair is audited: Theorem 12.2 is proved conditional on the standard definitions of π₀ and H₀ and on the three properties behind F4, F6 and F7, and without the dilation only for m₀ = M_*, λ < λ_* (§2.6); "no other external mathematical input is used" (ll. 421–422) and "no other external input is used" (ll. 2879–2880) are inaccurate.** (Superseded later on 11 November 2026: the repair was written and audited the same day, and the status sentence of 7 November stands again; see "Free-field appendix (2026-11-11)" below. The line numbers in this section are those of f213cc8.) Sources read for the repair on 9 November: GJ2 p. 365 ((1.2.10)–(1.2.12): the Fock-space fields, self-adjointness of their closures, the Weyl relations); GJ2 p. 398 (translation of φ and of a, a*; no relation for π); Simon p. 24 (Theorem I.11: the unitary D with DΩ₀ = 1, Dφ(f)D⁻¹ = φ(f)).

**Reports archived (11 November).** The reports of rounds V4–V4e, of the integration auditor, of R7/R7b and of the companion's editor were returned as messages and kept in a temporary folder of the session, which was emptied on 10 November. They were recovered from the session transcripts: `../ugjs/council/v4-math-report.md`, `v4-integration-report.md`, `v4f-free-field-report.md`; `../companion/council/r7-verifier-report.md`, `revised-edition-editor-reports.md`.

**What the audits of 7 November did not check** (their own lists, now readable in the archived reports).
- V4, mathematics: the proofs of Simon's Theorems I.3, I.6, I.17, I.22, V.2, V.7 (statements only); whether Simon's φ_F has covariance C; whether V.7's ∫g:P(φ): is built from (V.3) (pp. 139–150 not read); the GJS and Fock-space readings; N.13, N.20, N.25, N.28 line by line; N.19(i), (iv); the downstream consumers except one range; the dossier images (it rendered the pages from `refs/`).
- V4b: edits unrelated to F1–F11 (A8's Scope and Used-in lines, the C5 items, the constants table, the S₂ remarks); Proposition 2.7, Lemmas 9.3 and 10.3 beyond their interface with the affiliation claim.
- V4c: the orientation text of Proposition C.7; the constants paragraph; Corollary 5.2's constant (re-derived by hand by the orchestrator on 9 November); Lemma 9.3, Steps 1 and 3; the Trotter part of Proposition 2.7 (checked by V4f); the uses of A5(i) in §4.
- V4d: the rest of GJ2 p. 397; the pages behind `gj1-locality-06` and `gj2-local-algebra-40` (the latter read by V4f); edits outside its items R1–R4 other than one provenance sentence.
- V4e: the three items that V4f then audited.
- Integration auditor: Simon pp. 10, 11, 17, 25, 34; GJS pages other than p. 594; the proofs of Appendix D that the integration did not change (compared with the audited note, not re-proved); §§8–14; the PDF pages visually; the numerical scripts; docs, README, CITATION, KB, companion; the new notice in `ugjs/comparison.tex`; the re-run of the gates, the step maps and `labels.md`.
- V4b–V4e were re-checks by the V4 auditors, not by fresh agents.

**Check of this unit (11 November).** Before the commit a fresh Opus agent that had written none of it checked the working tree against `main.tex`, the page images, the archived reports and GitHub (`../ugjs/council/docs-check-2026-11-11-report.md`). It confirmed the site fix (Liquid 4.0.4 on all pages; both PDFs rebuilt byte for byte; the generators leave the tree unchanged) and the loci of every row of the table above, and reported 5 MAJOR and 11 MINOR findings on the wording and on what had been missed: `docs/imports.md`; the dating of the gaps (all four are older than the integration); the Euclidean scaling import A8(viii) beside the dilation finding; the page numbers of six figure pages; an unsupported sentence about (P) in row S1. All were re-read at the source and applied. Not checked by it: whether the archived reports are verbatim copies of the transcripts; a build with Jekyll itself; the deployed site.

**Not done.** The repair of Finding 3 and its audit (done later the same day: next section). The dossier index (`audit_2026/citation_screenshot_dossier.tex` references 54 of the 85 images in `audit_2026/evidence/`). Gates G4 and G5 for the 110 pages. An independent re-check of the two R7b fixes of the companion. Waiting for the author: the About text of the repository, a tag for version 1.1.0, Phase C, the C5 readings, the reading of the revised companion.

### Free-field appendix (2026-11-11) — gate GF: Appendix E, audit rounds V5 to V5d

**Why.** Finding 3 of the status review above (round V4f, 9 November): the record named π₀, H₀, U_a and a dilation unitary and used the action of translations, parity and dilations on the fields and on the local algebras, without definitions, derivations or imports. On 11 November the author's "continue" after the review was taken by the orchestrator as the go-ahead for the repair; the public notice of that morning (commit d2b106c) is withdrawn with the publication of the repair, on 21 November 2026 (see "Documentation check" below).

**What changed in `main.tex`** (against f213cc8; 8744 lines, 125 pages).
- New Appendix E (`app:freefield`). Lemma E.1: the one-particle space in momentum variables, the orthogonal maps τ_a and d_s, the operator μ on the index space. Lemma E.2: second quantization of a unitary on Fock space. Definition E.3: the number grading i^N; π₀(h) := i^N φ₀(μh) i^{−N}; W(f,0), W(0,h); H₀ as the generator of the second-quantized one-particle group, carried to Q-space by the unitary D of Simon's Theorem I.11. Lemma E.4: transport by an orthogonal bijection of index spaces (fields, polynomials and Wick monomials, multiplication operators, positivity, uniqueness). Proposition E.5: translations, parity, dilations — their action on φ₀, π₀, the local algebras, H₀, the Wick powers and V(g). Remark E.6: the three identities of A7 and the dilation identity for K(g). Lemma E.7: the objects are those of the sources (the Fock-space fields, H₀ and U(−a) of GJ2; Simon's dΓ(μ)). The Weyl relations are not used.
- A1: new paragraph "Fock space and the free field", items (e) (Simon pp. 23–24: Fock space, essential self-adjointness of the field, Theorem I.11), (f) (Simon pp. 31–32, 78–79: dΓ(A), Example 3, H₀ = dΓ(μ)), (g) (GJ2 pp. 364–365, 398: the Fock-space objects, quoted for the identification only); Sources, Scope, Used-in and Dossier lines extended (the Scope cites Simon p. 27 for the source's Fourier normalisation); (W.1) and the uniqueness sentence of item (d) say that their test functions are real.
- §2.1: π₀ and H₀ defined (with pointers to Definition E.3), W(f,0) and W(0,h) defined as unitaries, Ω₀ := 1, the action of τ_a and θ on the net stated with a pointer.
- The introduction: what Ω₀ is, at its first occurrence; that Ψ_{m₁} and m₁ are stated in the working coordinates of §2.6, with Remark 3.3 for a general pair (m₀, λ); a dated parenthesis after the sentence on external inputs.
- A6: item (i) states the inclusion e^{itH₀}A(O)e^{−itH₀} ⊆ A(O_{|t|}) and quotes it from GJ1, eq. (3.4), p. 1948; the Scope gives the identification of the sources' algebras through the unitary of Lemma E.7, names what remains a reading, and reports the two ">" printed on GJ2 p. 398 [sic].
- A7: U_a and Θ are those of Proposition E.5; the Scope says that the three identities are now also proved in the record and reports the source's "(1.2.11)" [sic].
- Lemma 2.8 (proof: U_a* = U_{−a}; the closure K(g); positivity of Θ from Lemma E.4), Remark 3.3 (rewritten: the dilation unitary is that of Proposition E.5(D); the intertwining of the dynamics α is derived from (P) for both models; items (1)–(5) of Theorem 12.2 are transported one by one; in original coordinates the rate is Ψ_{m_{1,*}}(s d) and the moment constant carries its factor s), the proof of Theorem 12.2(4), the proof of Corollary 12.3 and Step 1 of Theorem 13.2 refer to Proposition E.5.
- Notation table (rows for φ₀, π₀, H₀, i^N, τ_a, Θ), a title-page notice (two of its sentences rewritten on 21 November after the documentation check), Appendix B (new entry in the corrections history; "External residue"), date and epoch (11 November 2026; 1794355200).
- No statement of a theorem, proposition, lemma or corollary of f213cc8 changed. A comparison of all statement environments by label (by the sources auditor on the first version of the repair; repeated by the orchestrator on the final one: 120 labelled environments before, 127 now, none removed) finds changes in Assumptions A1, A6, A7 and in Remark 3.3 only, and the seven new statements E.1–E.7.

**Gate GF.**
- G0: three `pdflatex` passes with `SOURCE_DATE_EPOCH=1794355200 FORCE_SOURCE_DATE=1`: 0 errors, 0 Overfull, 0 undefined; 125 pages; the `??|TODO|Hmm|wait,` grep prints nothing; sha256 of `main.pdf`: `87084de82564cb1a83881f7bab634300f5d436c7a26b89bd8ba3b84e980fd80e` (build of 21 November 2026, with the corrected title-page notice; the build in commit 73bbb76 was `8a52b8f6954a6afbb7bac944fb2ef53abc0a46b202781fb6bd090bc307e7710c`).
- `.aux`: all 230 labels of the build of 7 November keep their numbers (their pages move by 0 to 5). Eight labels are new: `app:freefield` (E, p. 115), E.1 (p. 115), E.2 (p. 117), E.3 and E.4 (p. 118), E.5 (p. 120), E.6 and E.7 (p. 122).
- G3: Appendix E introduces no numerical constant. Its identities with factors (the isometry of d_s, C_{m′}(sz) = C_m(z), the factor s⁻¹ of the Wick powers, λ′ = s⁻²λ and the factor s of V, the factor 2^{−1/2} in the source's fields, the signs of π₀ and of U(−a)) were re-derived by hand by the mathematics auditor. Numerical corroboration only, nothing deduced from it: `../ugjs/council/v5-numerics/freefield_check.py` (output beside it; `/usr/local/bin/python3` 3.14.7, numpy 2.5.2, scipy 1.18.1, `scipy.integrate.quad`, absolute tolerance 1e-8) compares C_{m′}(sz) with C_m(z) and with K₀(m|z|)/(2π) at nine points (largest deviation 1.1e-10), and the two sides of the isometry of d_s and of the momentum form at two parameter pairs each (6.7e-16 and 8.9e-16).
- G4: ten page images added to `audit_2026/evidence/` (private companion repository, commit 74aed8d of 21 November 2026; until then on disk only) and named in the Dossier lines of A1 and A6: `simon-fock-045`, `simon-fock-046` (pp. 23–24), `simon-fourier-049` (p. 27), `simon-dgamma-053`, `simon-dgamma-054` (pp. 31–32), `simon-freefield-100`, `simon-freefield-101` (pp. 78–79), `gj2-fock-04`, `gj2-fields-05` (pp. 364–365), `gj1-propagation-04` (p. 1948). `simon-freefield-100` shows no printed page number: p. 78 follows from the offset of the scan (PDF page = printed page + 22) and from the next page, which prints 79. The dossier index file is still not updated (**not run**).
- G5: pages 1, 2, 8, 24, 25 and 115–124 of the build of 11 November (73bbb76) (the title-page notices, §2.1, Remark 3.3, Appendix E) were rendered at 80 dpi and looked at by the orchestrator for layout: nothing outside the margins, no missing glyph (the log has no `Missing character` line). This found one defect of the repair: the new title-page notice ran on into the preceding paragraph (a blank line was missing before its `\smallskip`); fixed before the commit, and the fourteen other pages re-rendered pixel-identical. Of the two builds of 21 November, whose title-page notice is longer: pages 1–3 of the first (sha256 `85471de3…4332`) were rendered and looked at by the documentation checker in round D3b, and pages 2–4 of the final one by the orchestrator and by the checker in round D3c: the notice is its own paragraph, the abstract ends page 2, the contents run from page 3 onto page 4, and no label changes its page. The other pages were not looked at: the page-by-page inspection of the 125 pages is **not run**.
- G6 = rounds V5 to V5d (below).
- `docs/results.*` regenerated: 72 numbered statements, 34 reach A8; the page numbers of the figure pages are filled by the generator. `companion/council/labels.md` stays at the build of 7 November, which the companion describes.

**Audits.** Two fresh Opus agents that had written none of the repair, read-only; reports `../ugjs/council/v5-math-report.md` and `../ugjs/council/v5-sources-report.md`.
- V5, mathematics: no CRITICAL; one MAJOR (F-A: Remark 3.3 stated the transport of the dynamics α, and with it of items (2) and (3) of Theorem 12.2, without deriving it); 14 MINOR items, F-B to F-O (the report's summary line says fifteen); every computation of Appendix E that the auditor redid by hand came out as stated; of V4f's findings, F1 and F3–F10 closed and F2 partly (Ω₀ in the introduction).
- V5, sources and integration: no CRITICAL; two MAJOR, both about how the record describes itself (M1: the title-page notice restored the status before the audit of the repair was recorded; M2: the appendix named A1(e)–(f) as its only external inputs although it also uses A1(a), (c), (d)); nine MINOR (m1–m9). Every quotation it checked was found exact against pages the auditor rendered (its own list of what it did not check includes GJ2's definition of H(g), p. 363); its three-pass builds were byte-identical to the PDF then in the working tree and to the committed PDF of f213cc8; no label was renumbered.
- All findings were applied the same day, with two changes of the orchestrator's own: A6(i) is quoted from its printed source, GJ1 (3.4) (the first version of the repair restated it without one); and A7's Scope cites sections, not theorems, because the inventory generator follows `\ref`s.
- V5b (the same two auditors on the fixes and on the new text): mathematics — F-A to F-O all closed; the derivation of Remark 3.3, the core argument of Lemma E.1(ii) and the comparison of closures in Lemma E.7(a)(2) confirmed by hand; four new MINOR points, N-1 to N-4 (the word "real" in A1(d); the reading that the fields of GJ1 are those of GJ2; a missing sentence in the proof of Lemma E.7(a)(2); this record did not yet name the rounds). Sources — M2, m1–m6, m8, m9 closed; M1 closed on the condition that this record names the rounds and that the sentence "Standing until the repair is audited" of the status review is marked as superseded (both done in commit 73bbb76, which neither auditor saw: the documentation check below is the first independent reading of this record); m7 partly; three new MINOR points, N1–N3 (a reading presented as printed in the proof of Lemma E.4(iii); the symbol m₁ with two values, which is older than the repair; the same reading of GJ1); the quotations from GJ1 p. 1948 and Simon p. 27 exact; three-pass build of that version byte-identical (124 pages); labels unchanged.
- V5c: mathematics — N-1 to N-3 closed; the new sentences of Remark 3.3 and of the introduction accurate; two new MINOR points on the proof of Lemma E.7(a)(2) (V5c-1: the density of 𝔖 in 𝔇(N^{1/2}) was used and not stated; V5c-2: one symbol for three operators). Sources — N1–N3 and m7 closed; three-pass build byte-identical (125 pages); all 238 labels as in the V5b version; one optional remark, **not applied**: to write s·m_{1,*} in place of "m₁ :=" at the end of the proof of Proposition 3.2 (each passage now says which value of m₁ it means).
- V5d (the mathematics auditor only): V5c-1 and V5c-2 closed, nothing new. The edits of `v5-to-v6.diff` (the proof of Lemma E.7: 11 lines added, 9 removed) were seen by the mathematics auditor only; the two edits made after V5d (the round names in the title-page notice and the blank line before it, see G5) by neither auditor.

**Documentation check (12 and 21 November 2026).** Commit 73bbb76 (the repair with this section, 11 November) was not pushed until its documentation had been checked; a first attempt on 11 November was stopped unfinished at a usage limit, and this section said so until 21 November. On 12 November a fresh Opus agent that had written none of it checked the commit (`../ugjs/council/docs-check-2026-11-12-report.md`, findings D3-1 to D3-11).
- Confirmed: byte-identical rebuilds of both versions; the label comparison (230 labels, none renumbered, eight new) and the statement comparison (120 labelled environments before, 127 now; changes in A1, A6, A7 and Remark 3.3 only); the numerics; the archived reports against the transcripts; the eleven page images against the printed pages; the counts of the audit findings; the links; the commit's hygiene.
- Found: 3 MAJOR, all about this documentation. D3-1: the notice of d2b106c had been public for longer than "some hours on 11 November". D3-2: "the same auditors re-checked the repairs" overstated what they had seen, since the findings M1 and N-4 are closed by this record, which neither auditor read, and the edits after V5d were seen by neither. D3-3: the ten page images were not yet committed to the private repository. And 8 MINOR (D3-4 to D3-11): who saw the last edits; items (e)–(g) and Corollary 12.3 missing in the title-page notice of `main.tex`; summaries of the sources audit stronger than its report; the release date in `CITATION.cff`; this record's own sentence on the unfinished check; the reconstruction of `main.v6.tex`; one page image without a printed page number.
- All were applied on 21 November: the title-page notice of `main.tex` names items (e)–(g) and Corollary 12.3 and says who re-checked what; the record was rebuilt (G0 above; all 238 labels and their pages unchanged against the build of 73bbb76; `main.tex` 8744 lines); the public texts give the dates of the repair and of its publication; `CITATION.cff` gives 2026-11-21; the images are in the private repository.
- Re-check (21 November 2026, the same agent; appended to the report file). Round D3b: all eleven findings closed; four further MINOR wording points (D3b-1: the notice's sentence on who re-checked what; D3b-2: "all about the documentation" in three public texts hid that the notice of the manuscript had changed; D3b-3: the G5 line named the wrong build; D3b-4: "three of its sentences"), and the condition that every sentence dated 21 November holds only if the push is made that day (D3b-5). They were applied as the agent proposed, the sentence of the notice in its own wording, and the record was rebuilt once more (G0 above). Round D3c confirmed the four points closed and found nothing new; it rebuilt the final record byte-identically, with all 238 labels, their pages and all statement environments unchanged against 73bbb76. This sentence, the precision in the G5 line about which build was looked at, and the archived D3c report were added after that round and were not re-checked.

**Not done.** The dossier index and the page-by-page inspection of all 125 pages (G4, G5 above). A re-audit by agents other than the two V5 auditors: every re-check was made by the agent that had raised the finding. The optional remark of V5c. The companion is not revised: it is the edition of 7 November 2026 and describes the 110-page record of that date. Still open for the author: the classification of the V4f findings, Phase C, the C5 readings, the reading of the revised companion, the repository's About text and a tag.

## Dossier map (assumption → `audit_2026/evidence/` images)

| assumption | images |
|---|---|
| A1 | gj2-ground-existence-08, gjii-ground-12, gj71-lower-bound-02, gj71-theorem2-04, rosen-semigroup-22, rosen-selfadjoint-23, gjs-source-05/06; Wick powers (added 2026-11-07): simon-wickgen-032, simon-wickpair-033, simon-wickprod-034, simon-gaussproc-037, simon-gamman-038/039, simon-wickdef-156/157/158, simon-wickthm-159/160; Fock space and the free field (added 2026-11-11): simon-fock-045/046, simon-fourier-049, simon-dgamma-053/054, simon-freefield-100/101, gj2-fock-04, gj2-fields-05, gj2-cutoff-independence-38 |
| A2 | simon-free-fkn-111, simon-fkn-184/185, grs-fkn-39/40, simon-wrong-iii12-119 |
| A3 | simon-exp-174, simon-transfer-178/179/180; construction of U_h (added 2026-11-07): simon-wickdef-156/157/158, simon-wickthm-159/160, simon-secondq-047 |
| A4 | simon-hyper-056, simon-timeslice-125/126; Theorem I.22 (added 2026-11-07): simon-thm122-060 |
| A5 | gjexp-domain-165/166/167 |
| A6 | gj1-locality-06, gjexp-054/055/056, gj2-cutoff-independence-38, gj2-local-algebra-40; item (iii) (added 2026-11-07): gj2-locality-37; item (i), the printed inclusion (added 2026-11-11): gj1-propagation-04 |
| A7 | gj2-cutoff-independence-38 |
| A8 | gjs-source-05/06, gjs-p589-06, gjs-scaling-07, gjs-theorems-10/11/12, gjs-core-11/12, gjs-uniform-46, gjs-uniformity-46, gjs-proof-14 (E54, scope of (vi)), gjs-thm1111-13 (p. 596), gjs-proof118-17 (p. 600), gjs-thm41-45 (p. 628) (added 31 October 2026) |
