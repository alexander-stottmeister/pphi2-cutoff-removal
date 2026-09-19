# Part I — unified manuscript (`part_i/main.tex`)

**Repair addendum (16 August 2026; supersedes earlier unconditional closure
wording below).**  The canonical Main Theorem is an implication from the explicitly
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
  class). Fixed: "Assume 𝒫 even and …" in statement and proof.
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
(σ_{a′} defined, weight h̄, g ∈ 𝒢 stated, integration variable a′).

**Nit (14) — all fixed.** Four-cell argument via extreme indices; Lemma 7.3 slab
qualifier T ≥ t/2; Thm 7.8 parenthetical ("Step 2 fails", not "vacuous"); square-moment
parentheticals cite CE1 + Remark 6.3; Lemma 3.1 s ∈ {0,1} case + generalization to
1_I⊗g (makes §8's citations literal); App A Ψ row shows both branches; §1.3(b) rate
harmonized to poly(d)e^{−2m₁d}; §14 Part II paragraph (per-generator wording, free vacua
ω⁽⁰⁾ symbols, rate exponent ϑ); provenance parenthetical for Cor 12.3's GJ3 formula;
App C: dμ_{0,C} defined, M2 hedge restored, C₀ → C_*, λ = 0 guard, subsection titles
un-numbered; A6 dossier double-wrap; freeze-table slab row; header comment; §13 and
thm:MAIN src comments corrected.

**Accepted as-is (3) — documented, no change.** thm:MAIN(5) quantifies over 𝒞_H where
m6 stated 𝒢 (strengthening, delivered by Thms 5.1/7.8; noted in src comment); Prop C.7's
𝒢 → 𝒞_H widening (correct; matches usage); local notation shadows listed by R5 (each
locally announced, none load-bearing).

**Reviewer-verified clean:** all constant chains (M², 𝔎(p′), 9·8! = 362 880, K′, Ĉ_Q,
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
| `M_0` (variation bound, `lamport_gap_to_main.tex` ⟨1⟩3–⟨1⟩4) | `𝔪` (`\mathfrak m`) | collision with moment constant `M`; **plan amendment**: strategy.md D4 originally said `Θ`, which collides with the parity unitary `Θ = Γ(−1)`; `𝔪` adopted instead (recorded also in strategy.md) |
| `p` with `deg 𝒫 = 2p` (`m4/m2-audit.tex`) | `2p'` with `deg 𝒫 = 2p'` | m6/r2-check convention; the p-vs-2p′ change caused the v0 half-degree slip — single convention frozen |
| `𝒞` (`m6` §3, cutoff class) | `𝒞_E` | three classes named apart (`𝒞_E`, `𝒞_H`, `𝒢`) |
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
  K₁K₂^{2n}n!K₂^{2n′}n′!; both ≤ K₁K₂^{8p′}(4p′)! = 𝔎(p′) (K₂≥1, n!n′!≤(n+n′)!). ✓
- Per-pair kernel ‖h1_Δ‖₂‖h1_Δ′‖₂ ≤ 1 (‖h‖∞≤1, unit cells); 3² = 9 ordered pairs;
  ‖Q_V‖ ≤ 9𝔎(p′)λ²(Σ|aₙ|)² = M²/C₈. ✓ matches r2-check Prop. 2.1.
- φ⁴ (p′=2): (4p′)! = 8! = 40320; 9·40320 = 362880; K₂^{8p′} = K₂^16. ✓ matches
  r2-check Cor. 2.2.
- 𝔫(X_f^n)² = K₁K₂^{4n}(2n)!N_I^n‖f‖₂^{2n} = K₁(K′)^{2n}(2n)! with
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
| ⟨1⟩3 (separation) | Lemma 9.2 `lem:separation` (M₀ → 𝔪) | done |
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
  γR ≥ 1; 1+2/π < 2 ⇒ prefactor 2𝔪. Gaussian tail ∫_{|t|≥R}|f| ≤ (a/πR²)e^{−R²/(2a)}
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
  V(h)→𝒰_h (Euclidean), 𝒞→𝒞_E, compact set K→Λ (avoids K(g)/K₁/K₂ clash — logged
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

## Dossier map (assumption → `audit_2026/evidence/` images)

| assumption | images |
|---|---|
| A1 | gj2-ground-existence-08, gjii-ground-12, gj71-lower-bound-02, gj71-theorem2-04, rosen-semigroup-22, rosen-selfadjoint-23, gjs-source-05/06 |
| A2 | simon-free-fkn-111, simon-fkn-184/185, grs-fkn-39/40, simon-wrong-iii12-119 |
| A3 | simon-exp-174, simon-transfer-178/179/180 |
| A4 | simon-hyper-056, simon-timeslice-125/126 |
| A5 | gjexp-domain-165/166/167 |
| A6 | gj1-locality-06, gjexp-054/055/056, gj2-cutoff-independence-38, gj2-local-algebra-40 |
| A7 | gj2-cutoff-independence-38 |
| A8 | gjs-source-05/06, gjs-p589-06, gjs-scaling-07, gjs-theorems-10/11/12, gjs-core-11/12, gjs-uniform-46, gjs-uniformity-46, gjs-proof-14 (E54, scope of (vi)) |
