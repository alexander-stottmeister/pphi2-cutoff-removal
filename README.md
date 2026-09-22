# Removal of the spatial cutoff for weakly coupled P(φ)₂

Manuscript, working notes, and the full adversarial audit trail for a Hamiltonian proof
that the net of spatially cutoff P(φ)₂ ground states converges in norm on every local
algebra. This is a research record, not a published paper.

## What this is: an AI-assisted, experimental open-science project

This repository is an **experiment in open science, and the work in it is AI-assisted.**
The manuscript, the working notes and the audit documents were drafted by the author
working with Anthropic's Claude as an interactive assistant, and the entire working
method — every phase, gate and adversarial round, including the rounds that found errors
in earlier rounds' repairs — is published alongside the result rather than discarded.
That is the experiment: the record of how the proof was arrived at is part of what is
being released.

**Human verification of the output is ongoing.** Nothing here has been refereed, and the
author's own line-by-line check of the machine-assisted material is still in progress:
open audit item C5 (a second human reader for the source page images, see below) is
unclosed, and the main theorem is conditional on an imported hypothesis. Read every
statement in this repository as a claim under active verification, not as a settled
result, and check anything you intend to rely on against the cited sources yourself.
Direction, mathematical judgement and final responsibility are the author's.

## Status: the main theorem is conditional. Please read this first.

**Part I** (`part_i/main.tex`, 40 pp, document of record) proves Theorem 12.2. In the
Glimm–Jaffe–Spencer weak-coupling region 0 ≤ λ/m₀² < ε_𝒫, the full net (ω_g) of cutoff
ground states, with no subnets and no space averaging, converges in norm on every local
algebra 𝔄(O),

    lim_{g∈𝒢} ‖(ω_g − ω_∞)|_{𝔄(O)}‖ = 0,

with an explicit super-polynomial rate in dist(O, {g < 1}). The limit is locally normal,
translation invariant, ℤ₂ invariant for even 𝒫, and a ground state of the Glimm–Jaffe
dynamics (𝔄, α) in the spectral sense.

The proof is an implication from the imports A1–A8 enumerated in §2. **It is not a proof
of those imports.** One of them is not a literal quotation of a printed theorem:

- **A8(vi), written U_GJS**, is the cutoff-uniform form of the Glimm–Jaffe–Spencer moment
  estimate (Ann. of Math. **100** (1974), Thm. 1.1.8) on the slab family used here. Since
  the scope amendment of 5 September 2026 it is documented as imported at the scope at
  which the source itself states and uses it, with the relevant passages on pp. 594–597
  and 629 quoted verbatim in item A8(vii′), rather than as a quantifier strengthened
  beyond the source. It remains a named hypothesis of Theorem 12.2. This manuscript does
  not re-derive the cluster expansion: Appendix C audits the source mechanism and proves
  two analytic prerequisites only.

**Open audit item C5.** No second human reader has yet checked the source page images
against the transcriptions in §2. The itemized checklist is
`part_i/C5_reading_record.md`; all nine verdict fields are still blank.

**Part II** is open at gate (II.11). Its preparatory scoping pass is
`part_ii/gate_II11_scoping.tex`, and phases V0–V4 are recorded in `strategy.md`. Nothing
in Part I depends on Part II.

The manuscript states its own negative scope in the abstract: no uniqueness of ω_∞ among
all locally normal ground states, no sharp exponential rate, and no claim outside the
weak-coupling region.

## Layout

| path | what it is |
|---|---|
| `part_i/` | document of record, its `README.md` with gates G0–G6 and step maps, and the C5 reading record |
| `part_ii/` | the open programme, gate (II.11) scoping, phases V0–V4 |
| `m0/`–`m6/` | historical working drafts, superseded by `part_i/main.tex` and kept for provenance |
| `audit_2026/` | citation screenshot dossier and the 2026 critical proof audit |
| `fresh_audit_2026_08_16/` | independent audit, Lamport-style reconstruction, evidence ledgers |
| `repair_2026_08_16/` | post-repair checks and artifact hashes |
| `output/pdf/` | compiled snapshots of the documents above |
| `strategy.md` | the living plan and chronological record of every phase and gate |

## What is deliberately not in this repository

Source PDFs (`refs/`) and every page image used as citation evidence (`**/evidence/`,
`part_ii/dossier_images/`) are third-party copyrighted material and are not
redistributed here. Two consequences:

- The dossier sources still build. Missing page images are replaced by framed
  placeholders, and every claim, page reference, and finding remains in the text.
- `fresh_audit_2026_08_16/render_evidence.sh` regenerates the audit's page-image corpus
  from your own copies of the sources. Each call is pinned to a one-based page number, so
  the images are reproducible for anyone with legal access to the papers. The script
  names the file it expects for each source, under `refs/`; those names are the script's
  own contract, and the simplest way to satisfy it is to read the `render` lines and put
  your PDFs where they point.

Short quotations from the sources appear in the manuscript with page citations, as usual
in scholarly work, and each transcribed display carries a `% src:` comment naming its
origin.

The boundary is enforced mechanically rather than by care alone. `.gitignore` excludes
the source and image paths, and every raster format a page image could arrive in;
`.githooks/pre-commit` then refuses any commit that stages one regardless. Enable the
hook in a fresh clone with

```sh
git config core.hooksPath .githooks
```

## Building

No external dependencies, no BibTeX, no graphics. Three passes resolve all references.

```sh
cd part_i && pdflatex main.tex && pdflatex main.tex && pdflatex main.tex
```

A clean build is 40 pages with zero errors and zero undefined references.

The three citation dossiers (`audit_2026/`, `fresh_audit_2026_08_16/`, `part_ii/`) build
the same way, from their own directory. Without the page-image corpus each image is
replaced by a framed placeholder naming the missing file, and the build still completes
with zero errors.

The printed date is pinned in the preamble to the last mathematical change, so it does
not drift between builds. The PDF bytes would otherwise still carry pdftex's own build
timestamp, so the committed `part_i/main.pdf` is built with that timestamp pinned too:

```sh
SOURCE_DATE_EPOCH=1788566400 FORCE_SOURCE_DATE=1 pdflatex main.tex   # x3
```

Three passes of this command reproduce the committed PDF byte for byte under pdfTeX
1.40.29 (TeX Live 2026).

## License

Manuscript, notes, and all prose: [CC BY 4.0](LICENSE).
Scripts (`*.py`, `*.sh`) and the LaTeX style files: [MIT](LICENSE-CODE).
Quoted third-party material remains under its own copyright and is used as citation.

## How this record was produced

As stated at the top, this is an AI-assisted research record. Concretely, the assistant
drafted and transcribed source passages, recomputed constants by hand and by machine, ran
the adversarial verification passes recorded in `strategy.md`, and maintained the citation
dossiers. Direction, mathematical judgement and final responsibility are the author's.
Commits where the assistant contributed carry a `Co-Authored-By` trailer, so the git
history shows the division of labour.

Because the output is machine-assisted, the verification standard applied to it is higher
than usual, not lower: every imported statement is pinned to a page of a source, the
dossiers reproduce those pages, and `part_i/README.md` records which gate each section
passed. That verification is still running — see the note at the top of this file.

The working method is itself part of the record. `strategy.md` logs every phase, gate
and adversarial round, including the rounds that found errors in earlier rounds' repairs,
and `part_i/README.md` maps each section of the manuscript back to the working draft it
came from.

## Citing

See `CITATION.cff`. If you cite the theorem, please cite it as conditional on U_GJS.
