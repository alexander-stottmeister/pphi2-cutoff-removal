# Plan: README, documentation, and an interactive figure site

Status: adopted 22 September 2026. Nothing here changes a mathematical claim. Every
number that reaches the README, the documentation or a figure is taken from
`part_i/main.tex` or from `part_i/main.aux`, never retyped from memory.

## Two constraints that shape the rest

**Figures are SVG.** `.gitignore` and `.githooks/pre-commit` both reject `*.png`,
`*.jpg`, `*.jpeg`, `*.tif`, `*.tiff`, `*.webp`, `*.gif`, `*.bmp` and `*.djvu` by
extension at any path, because that is what the citation page images arrive as. `.svg`
is in neither list, so figures pass both gates and the publication boundary is not
touched. That is the right format anyway: diagrams and plots as diffable text. Should a
raster ever be genuinely necessary, the fix is a narrow *path* exception in both files,
never the removal of an extension. GitHub sanitises SVG in READMEs -- no scripts, no
reliable SMIL -- so README figures are static stills and all motion lives on Pages.

**Pages may not serve until the repository is public.** Publishing GitHub Pages from a
private repository requires a paid plan. Deliverables 1 and 3 are unaffected; the site
is built and tested locally regardless, and goes live when the repository flips.

## Deliverable 3 (first): `docs/` as the substrate

The README and the site are views of this, so it is built first.

| file | contents |
|---|---|
| `docs/index.md` | hub: what this is, conditional status, three entry points |
| `docs/status.md` | Part I gates G0-G6, audit item C5, Part II gate (II.11) and its status list |
| `docs/notation.md` | from the notation freeze, main.tex 2.3 |
| `docs/definitions.md` | model, the three cutoff classes, `O_r`, `d(g,O)`, the plateau order |
| `docs/results.md` | every named result: number, label, statement, section, dependencies, conditionality |
| `docs/imports.md` | A1-A8 with source pages, and what U_GJS is and is not |
| `docs/provenance.md` | gates, corrections history, dossier map |
| `docs/figures/` | static SVG |
| `docs/interactive/` | the figure pages |

`results.md` is **generated**, never hand-maintained: `docs/extract.py` parses the
theorem environments, the `% src:` provenance comments and the `\ref` graph from
`part_i/main.tex`, and resolves every number through `part_i/main.aux`. The dependency
graph falls out as data, the inventory cannot drift, and "which results rest on U_GJS"
becomes a computed fact rather than a claim. The same JSON feeds the site.

## Deliverable 1: the README

Order: what this is (the AI-assisted and ongoing-verification section stays at the top)
-> the result in one picture -> the figures -> the PDFs -> build -> layout -> licence ->
citing. Each PDF gets a one-line description and its page count.

Five static SVGs, each a still of a live figure and linked to it:

1. the import DAG, with U_GJS and everything downstream in a distinct colour;
2. the light cone of the two-regime bound (Lemma 10.3);
3. the rate curve `Psi_gamma(d)` against its `(1+d)^{-N}` envelopes (Lemma 10.5);
4. the plateau net and `d(g,O)` (Definition 2.1);
5. the uniform gap `spec H(g) subset {0} u [gamma, infinity)` (Theorem 7.8).

## Deliverable 2: the interactive site

Plain HTML, vanilla JS, inline SVG and Canvas. No framework, no bundler, no Actions;
KaTeX from a CDN for formulas; one shared `assets/figure.js`. Pages serves `/docs` from
`main`: documentation markdown carries front matter and renders as site pages,
interactive `.html` carries none and is passed through verbatim. One source, two
audiences -- the docs are read on GitHub, the figures are driven on Pages.

| # | result | interaction |
|---|---|---|
| 1 | import graph (2.4, Thm 12.2) | click a node for its statement; toggle U_GJS off and watch what collapses |
| 2 | two-regime bound (Lem. 10.3) | drag `t`; the cone `O_{|t|}` expands and the bound jumps from `2M e^{-gamma r_j/4}` to `2M` as `|t|` passes `r_j/2`; drag `B_j` to change `r_j` |
| 3 | rate function (Lem. 10.5) | sliders for `gamma, M, N`; `Psi_gamma` and its envelope, with `d_0 = 4 + 2/gamma` marked |
| 4 | inverse-energy filter (Lem. 9.1) | drag `gamma`: the notch in `hat W_gamma(E) = chi(E)/E` widens, `W_gamma(t)` and the tail `T_gamma(r)` respond |
| 5 | plateau net (Def. 2.1) | drag a plateau to build `g` in the net class; the order and `d(g,O)` update |
| 6 | weak-coupling reduction (Prop. 3.2) | a point in the `(m_0, lambda)` plane slides along its dilation orbit into the printed region |
| 7 | uniform gap (Thm 7.8) | the spectrum of `H(g)` as `g` grows, the gap staying open |
| 8 | affine path (4, 8) | `alpha: 0 -> 1` along `h_1 + alpha(h_2 - h_1)`, the mechanism U_GJS is imported at |
| 9 | two-phase dichotomy (Thm 13.2) | `R_a` slider; the truncated correlator decays like `e^{-m_1 R_a / 2}`, contradicting (B1)-(B4) |

Figures 3, 4 and 7 are computed from the paper's own formulas by
`docs/figures/make_figures.py`, which emits both the static SVGs and a sampled-curve
JSON, so the pictures are checkable artifacts under the same gate discipline as the rest
of the repository rather than drawings. `m2/m2_rate.py` is the precedent.

**Honesty rules.** A persistent banner on every page: conditional on U_GJS, C5 open,
AI-assisted, verification ongoing. Every figure is labelled an illustration, not
evidence. The rate figure states that `Psi_gamma` is an upper bound, not a computed
decay of any actual state.

## Phases

- **P0 scaffolding.** Pages config, the banner, the licence fix (`LICENSE-CODE` names
  only `*.py`, `*.sh` and the style files and must cover `.js`, `.html`, `.css`), and a
  hook test proving SVG passes while PNG still does not.
- **P1 documentation.** `extract.py`, then `results.md`, then the hand-written pages.
- **P2 figures and README.** `make_figures.py`, the five SVGs, the README rewrite.
- **P3 interactive.** Spine first (1, 2, 3), then 4-9. Built before the flip; served after.
- **P4 adversarial pass.** Every number on the site checked against `main.tex`, every
  link resolved, the boundary re-audited, the clean-clone build still green.
