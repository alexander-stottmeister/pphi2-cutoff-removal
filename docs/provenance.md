---
title: Provenance
---

# Provenance

How the manuscript was built, what it was built from, what was found wrong along the
way, and how to check any of it yourself.

## Frozen sources

`part_i/main.tex` is an assembly of earlier documents, each frozen at the moment it was
consumed. Every transcribed display carries a `% src:` comment naming its origin, and
`part_i/README.md` maps each section back to the draft it came from.

| file | role |
|---|---|
| `m6/main.tex` (v2, audited repair) | predecessor manuscript; statements and compressed proofs |
| `audit_2026/critical_proof_audit.tex` | independent audit, frozen against the v1 SHA-256 |
| `audit_2026/lamport_euclidean_to_gap.tex` | fully explicit proof, GJS ⟹ (M₂) + (G) |
| `audit_2026/lamport_gap_to_main.tex` | fully explicit proof, (M₂) + (G) ⟹ main theorem |
| `audit_2026/citation_screenshot_dossier.tex` + `evidence/` | page images for every import |
| `m4/r1-check.tex` | gate R1: h-uniformity of the Euclidean inputs |
| `m4/r2-check.tex` | gate R2: printed norms and exact constants, from the page image of p. 594 |
| `m0/m0.tex`, `m2/m2.tex`, `m3/m3.tex` | spectral passage; quadratic-model rate; dichotomy |
| `m4/m2-audit.tex`, `m4/g-side.tex` | superseded derivations, kept with update notices |
| `strategy.md` | the programme record: every phase, gate and adversarial round |

The two structured reconstructions follow Lamport's hierarchical proof format.

## Corrections history

The point of publishing this is that the errors are part of the record.

- **v0 → v1 merge** (9 Aug 2026): filter-transform sign corrected to +1/E; a spurious
  factor ½ removed from the one-path bound; an unnecessary g″ detour eliminated; the
  averaging identity of the canonical-vacuum corollary repaired.
- **Gate R2** (9 Aug 2026, page-image inspection of GJS p. 594): prefactor K₁ to the
  first power; local weight K₂^{2N(Δ)}; an earlier "correction" in `m4/m2-audit.tex`
  Rem. 5.3(i) was itself an **OCR artifact** and is withdrawn; a half-degree slip in the
  v0 assembly was found and fixed. The cell-pair count for (M₂) is 9, not 32.
- **Independent audit** (9 Aug 2026): severity register P1 (the two-phase corollary was
  missing premise (B4) — repaired by conditioning on Hypothesis 13.1); S1–S3 (citation
  pinpoints for FKN, hypercontractivity, domain smoothing); L1–L6 (cell count, negative-
  time norm ratio, nonnegative FKN inputs, signed and clipped truncations, exponential-
  moment prefactor, spectral-parameter range); C1 (dimensionless scaling made explicit);
  C2 (all imports enumerated as A1–A8); H1–H2 (literature claims narrowed). **No P0
  defect was found.**
- **Scope amendment** (5 Sep 2026): the status of U_GJS re-based — see
  [imports](imports.md). No proof changed; all 125 labels unmoved.

**Withdrawn routes**, kept in the record and not used: `m4/h6-attack.tex` Thm. 2.3
(UV-divergent double commutator); the gap-based (H6) proofs; wavelet-MRA-as-Polchinski
decomposition, which moved to the Part II documents.

## The citation dossiers

Every load-bearing citation is matched to an image of the page it is taken from, at the
theorem actually used. The dossier sources are in the repository; the page images are
not — they are third-party copyrighted material, and the JSTOR scans additionally carry
a watermark naming the downloading institution. Building a dossier without the corpus
gives a framed placeholder naming each missing file, with every claim, page reference
and finding intact.

To regenerate the corpus from your own copies of the sources:

```sh
sh fresh_audit_2026_08_16/render_evidence.sh
```

Each call is pinned to a one-based page number, so the images are reproducible for
anyone with legal access to the papers. The `render` lines name the file expected for
each source under `refs/`.

## Checking the inventory

The [result inventory](results.md) is generated, and can be re-derived:

```sh
cd part_i && pdflatex main.tex && pdflatex main.tex && pdflatex main.tex
cd .. && python3 docs/extract.py
```

`python3 docs/extract.py --check` exits non-zero if the committed inventory has drifted
from the manuscript. The numbers come from `part_i/main.aux`, never from hand-editing.
