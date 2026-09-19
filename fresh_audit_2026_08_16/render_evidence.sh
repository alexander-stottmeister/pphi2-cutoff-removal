#!/bin/sh
set -eu

# Fresh page-image corpus for the 16 August 2026 audit.  Each invocation of
# pdftoppm is pinned to one one-based PDF page.  The images are deliberately
# regenerated from the acquired source PDFs; no image from an older dossier is
# copied into this directory.

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
OUT="$ROOT/fresh_audit_2026_08_16/evidence"
mkdir -p "$OUT"
GJS74=$(find "$ROOT/refs" -maxdepth 1 -type f -name 'Glimm et al. - 1974 - The Wightman Axioms*' -print)
GJS74=${GJS74#"$ROOT/"}

render() {
  source_pdf=$1
  page=$2
  output_name=$3
  pdftoppm -f "$page" -l "$page" -r 144 -png -singlefile \
    "$ROOT/$source_pdf" "$OUT/$output_name"
}

# Proof notation.
render 'refs/audit_2026/Lamport_How_to_Write_a_21st_Century_Proof.pdf' 10 lamport-010
render 'refs/audit_2026/Lamport_How_to_Write_a_21st_Century_Proof.pdf' 16 lamport-016

# Part I: constructive P(phi)_2 sources.
render 'refs/Glimm und Jaffe - 1968 - A λ{Φ^4}_2 Quantum Field Theory without Cutoffs. I.pdf' 1 gj1-001
render 'refs/Glimm und Jaffe - 1968 - A λ{Φ^4}_2 Quantum Field Theory without Cutoffs. I.pdf' 5 gj1-005
render 'refs/Glimm und Jaffe - 1968 - A λ{Φ^4}_2 Quantum Field Theory without Cutoffs. I.pdf' 6 gj1-006

render 'refs/Glimm und Jaffe - 1970 - The λ(φ4)_2 quantum field theory without cutoffs .pdf' 1 gj2-001
render 'refs/Glimm und Jaffe - 1970 - The λ(φ4)_2 quantum field theory without cutoffs .pdf' 8 gj2-008
render 'refs/Glimm und Jaffe - 1970 - The λ(φ4)_2 quantum field theory without cutoffs .pdf' 12 gj2-012
render 'refs/Glimm und Jaffe - 1970 - The λ(φ4)_2 quantum field theory without cutoffs .pdf' 38 gj2-038
render 'refs/Glimm und Jaffe - 1970 - The λ(φ4)_2 quantum field theory without cutoffs .pdf' 40 gj2-040

render 'refs/Glimm und Jaffe - 1970 - The λ{Φ^4}_2 Quantum Field Theory without Cutoffs..pdf' 1 gj3-001
render 'refs/Glimm und Jaffe - 1970 - The λ{Φ^4}_2 Quantum Field Theory without Cutoffs..pdf' 8 gj3-008
render 'refs/Glimm und Jaffe - 1970 - The λ{Φ^4}_2 Quantum Field Theory without Cutoffs..pdf' 9 gj3-009
render 'refs/Glimm und Jaffe - 1972 - The λ{Φ^4}_2 Quantum Field Theory without Cutoffs..pdf' 1 gj4-001

render 'refs/Glimm und Jaffe - 1971 - Positivity and self adjointness of the $P(phi)_{2.pdf' 1 gj71-001
render 'refs/Glimm und Jaffe - 1971 - Positivity and self adjointness of the $P(phi)_{2.pdf' 2 gj71-002
render 'refs/Glimm und Jaffe - 1971 - Positivity and self adjointness of the $P(phi)_{2.pdf' 4 gj71-004

render 'refs/Rosen - 1970 - A λφ2 n field theory without cutoffs.pdf' 1 rosen-001
render 'refs/Rosen - 1970 - A λφ2 n field theory without cutoffs.pdf' 22 rosen-022
render 'refs/Rosen - 1970 - A λφ2 n field theory without cutoffs.pdf' 23 rosen-023

render 'refs/Glimm & Jaffe - Quantum Field Theory and Statistical Mechanics - Expositions.pdf' 1 gjexp-001
render 'refs/Glimm & Jaffe - Quantum Field Theory and Statistical Mechanics - Expositions.pdf' 54 gjexp-054
render 'refs/Glimm & Jaffe - Quantum Field Theory and Statistical Mechanics - Expositions.pdf' 55 gjexp-055
render 'refs/Glimm & Jaffe - Quantum Field Theory and Statistical Mechanics - Expositions.pdf' 56 gjexp-056
render 'refs/Glimm & Jaffe - Quantum Field Theory and Statistical Mechanics - Expositions.pdf' 165 gjexp-165
render 'refs/Glimm & Jaffe - Quantum Field Theory and Statistical Mechanics - Expositions.pdf' 166 gjexp-166
render 'refs/Glimm & Jaffe - Quantum Field Theory and Statistical Mechanics - Expositions.pdf' 167 gjexp-167

render "$GJS74" 1 gjs74-001
render "$GJS74" 5 gjs74-005
render "$GJS74" 6 gjs74-006
render "$GJS74" 7 gjs74-007
render "$GJS74" 10 gjs74-010
render "$GJS74" 11 gjs74-011
render "$GJS74" 12 gjs74-012
render "$GJS74" 46 gjs74-046

render 'refs/Guerra et al. - 1975 - The P(φ)2 Euclidean Quantum Field Theory as Classical Statistical Mechanics - Part 1.pdf' 39 grs1-039
render 'refs/Guerra et al. - 1975 - The P(φ)2 Euclidean Quantum Field Theory as Classical Statistical Mechanics - Part 1.pdf' 40 grs1-040
render 'refs/Guerra et al. - 1975 - The P(φ)2 Euclidean Quantum Field Theory as Classical Statistical Mechanics - Part 2.pdf' 16 grs2-016
render 'refs/Guerra et al. - 1975 - The P(φ)2 Euclidean Quantum Field Theory as Classical Statistical Mechanics - Part 2.pdf' 17 grs2-017
render 'refs/Guerra et al. - 1975 - The P(φ)2 Euclidean Quantum Field Theory as Classical Statistical Mechanics - Part 2.pdf' 18 grs2-018
render 'refs/Guerra et al. - 1975 - The P(φ)2 Euclidean Quantum Field Theory as Classical Statistical Mechanics - Part 2.pdf' 19 grs2-019

render 'refs/Simon - The P(\Phi)_2 Euclidean (Quantum) Field Theory.pdf' 1 simon-001
render 'refs/Simon - The P(\Phi)_2 Euclidean (Quantum) Field Theory.pdf' 48 simon-048
render 'refs/Simon - The P(\Phi)_2 Euclidean (Quantum) Field Theory.pdf' 53 simon-053
render 'refs/Simon - The P(\Phi)_2 Euclidean (Quantum) Field Theory.pdf' 55 simon-055
render 'refs/Simon - The P(\Phi)_2 Euclidean (Quantum) Field Theory.pdf' 56 simon-056
render 'refs/Simon - The P(\Phi)_2 Euclidean (Quantum) Field Theory.pdf' 57 simon-057
render 'refs/Simon - The P(\Phi)_2 Euclidean (Quantum) Field Theory.pdf' 111 simon-111
render 'refs/Simon - The P(\Phi)_2 Euclidean (Quantum) Field Theory.pdf' 119 simon-119
render 'refs/Simon - The P(\Phi)_2 Euclidean (Quantum) Field Theory.pdf' 125 simon-125
render 'refs/Simon - The P(\Phi)_2 Euclidean (Quantum) Field Theory.pdf' 126 simon-126
render 'refs/Simon - The P(\Phi)_2 Euclidean (Quantum) Field Theory.pdf' 174 simon-174
render 'refs/Simon - The P(\Phi)_2 Euclidean (Quantum) Field Theory.pdf' 178 simon-178
render 'refs/Simon - The P(\Phi)_2 Euclidean (Quantum) Field Theory.pdf' 179 simon-179
render 'refs/Simon - The P(\Phi)_2 Euclidean (Quantum) Field Theory.pdf' 180 simon-180
render 'refs/Simon - The P(\Phi)_2 Euclidean (Quantum) Field Theory.pdf' 184 simon-184
render 'refs/Simon - The P(\Phi)_2 Euclidean (Quantum) Field Theory.pdf' 185 simon-185

render 'refs/Albeverio et al. - 1989 - Uniqueness and global Markov property for Euclidean fields The case of general polynomial interacti.pdf' 1 ahz-001
render 'refs/Albeverio et al. - 1989 - Uniqueness and global Markov property for Euclidean fields The case of general polynomial interacti.pdf' 24 ahz-024
render 'refs/audit_2026/BDW_arXiv_2504.08606.pdf' 1 bdw-001
render 'refs/audit_2026/RZT_arXiv_2505.13030.pdf' 1 rzt-001
render 'refs/audit_2026/Hastings_cond-mat_0305505.pdf' 1 hastings-001
render 'refs/audit_2026/BMNS_arXiv_1102.0842.pdf' 1 bmns-001

render 'refs/Glimm et al. - 1975 - Phase Transitions for φ_2^4 Quantum Fields.pdf' 1 gjs75-001
render 'refs/Glimm et al. - 1975 - Phase Transitions for φ_2^4 Quantum Fields.pdf' 2 gjs75-002
render 'refs/Glimm et al. - 1975 - Phase Transitions for φ_2^4 Quantum Fields.pdf' 3 gjs75-003
render 'refs/Glimm et al. - 1976 - A Convergent Expansion about Mean Field Theory. I..pdf' 1 gjs76i-001
render 'refs/Glimm et al. - 1976 - A Convergent Expansion about Mean Field Theory. I..pdf' 2 gjs76i-002
render 'refs/Glimm et al. - 1976 - A Convergent Expansion about Mean Field Theory. I..pdf' 5 gjs76i-005
render 'refs/Glimm et al. - 1976 - A Convergent Expansion about Mean Field Theory. II.pdf' 1 gjs76ii-001
render 'refs/Glimm et al. - 1976 - A Convergent Expansion about Mean Field Theory. II.pdf' 37 gjs76ii-037
render 'refs/Glimm et al. - 1976 - A Convergent Expansion about Mean Field Theory. II.pdf' 38 gjs76ii-038
render 'refs/Glimm et al. - 1976 - A Convergent Expansion about Mean Field Theory. II.pdf' 39 gjs76ii-039

# Part II: wavelet/OAR and scope sources.
render 'refs/part_ii/MMST_scaling_limits_wavelets_2010.11121.pdf' 1 mmst-001
render 'refs/part_ii/MMST_scaling_limits_wavelets_2010.11121.pdf' 7 mmst-007
render 'refs/part_ii/MMST_scaling_limits_wavelets_2010.11121.pdf' 13 mmst-013
render 'refs/part_ii/MMST_scaling_limits_wavelets_2010.11121.pdf' 16 mmst-016
render 'refs/part_ii/MMST_scaling_limits_wavelets_2010.11121.pdf' 20 mmst-020
render 'refs/part_ii/MMST_scaling_limits_wavelets_2010.11121.pdf' 21 mmst-021
render 'refs/part_ii/MMST_scaling_limits_wavelets_2010.11121.pdf' 25 mmst-025
render 'refs/part_ii/MMST_scaling_limits_wavelets_2010.11121.pdf' 26 mmst-026
render 'refs/part_ii/MMST_scaling_limits_wavelets_2010.11121.pdf' 28 mmst-028
render 'refs/part_ii/MMST_scaling_limits_wavelets_2010.11121.pdf' 29 mmst-029
render 'refs/part_ii/MMST_scaling_limits_wavelets_2010.11121.pdf' 35 mmst-035
render 'refs/part_ii/MMST_scaling_limits_wavelets_2010.11121.pdf' 36 mmst-036
render 'refs/part_ii/MMST_scaling_limits_wavelets_2010.11121.pdf' 38 mmst-038
render 'refs/part_ii/MMST_scaling_limits_wavelets_2010.11121.pdf' 54 mmst-054
render 'refs/part_ii/Battle_Federbush_1987_ondelettes_vindication.pdf' 1 bf87-001
render 'refs/part_ii/Battle_Federbush_1987_ondelettes_vindication.pdf' 2 bf87-002
render 'refs/part_ii/Battle_Federbush_1987_ondelettes_vindication.pdf' 3 bf87-003
render 'refs/part_ii/SMMT_operator_algebraic_renormalization_2002.01442.pdf' 5 smmt-005
render 'refs/part_ii/NRSS_Lieb_Robinson_0712.3820.pdf' 19 nrss-019

printf 'Rendered %s fresh evidence images into %s\n' "$(find "$OUT" -type f -name '*.png' | wc -l | tr -d ' ')" "$OUT"
