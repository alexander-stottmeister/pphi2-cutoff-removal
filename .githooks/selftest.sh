#!/bin/sh
# selftest.sh -- prove that the publication-boundary guard still does its job.
#
# Runs entirely inside a throwaway clone under $TMPDIR: the real working tree, its
# index and both repositories are never touched.  Run it after editing .gitignore or
# pre-commit, and at the P4 gate.
#
#     sh .githooks/selftest.sh
set -eu

SRC=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
git clone -q --no-hardlinks "$SRC" "$TMP/wt"
cd "$TMP/wt"
git config core.hooksPath .githooks
git config user.email selftest@example.invalid
git config user.name selftest

pass=0; fail=0
refused() {  # refused <label> <path...>
  label=$1; shift
  git add -f -- "$@" 2>/dev/null || true
  if .githooks/pre-commit >/dev/null 2>&1; then
    echo "  FAIL  $label was ALLOWED"; fail=$((fail+1))
  else
    echo "  ok    $label refused"; pass=$((pass+1))
  fi
  git reset -q
}
allowed() {
  label=$1; shift
  git add -f -- "$@" 2>/dev/null || true
  if .githooks/pre-commit >/dev/null 2>&1; then
    echo "  ok    $label allowed"; pass=$((pass+1))
  else
    echo "  FAIL  $label was REFUSED"; fail=$((fail+1))
  fi
  git reset -q
}

echo "must be refused:"
mkdir -p refs evidence part_ii/dossier_images docs/figures
printf 'x' > refs/acquired-paper.pdf;                 refused "source PDF under refs/"        refs/acquired-paper.pdf
printf 'x' > evidence/page-001.png;                   refused "page image in evidence/"       evidence/page-001.png
printf 'x' > part_ii/dossier_images/p1.png;           refused "page image in dossier_images/" part_ii/dossier_images/p1.png
printf 'x' > docs/figures/scan.png;                   refused "PNG anywhere"                  docs/figures/scan.png
printf 'x' > docs/figures/scan.jpg;                   refused "JPG anywhere"                  docs/figures/scan.jpg
printf 'x' > docs/figures/scan.webp;                  refused "WEBP anywhere"                 docs/figures/scan.webp
printf 'x' > part_i/my-dossier.pdf;                   refused "*dossier*.pdf"                 part_i/my-dossier.pdf
printf 'x' > part_ii/acquired.pdf;                    refused "new PDF with no .tex beside it" part_ii/acquired.pdf
printf 'x' > PRIVATE.md;                              refused "PRIVATE.md"                    PRIVATE.md
git checkout -q -- PRIVATE.md 2>/dev/null || rm -f PRIVATE.md

echo "must be allowed:"
printf '<svg xmlns="http://www.w3.org/2000/svg"/>' > docs/figures/rate.svg
allowed "SVG figure under docs/figures/" docs/figures/rate.svg
printf 'console.log(1)\n' > docs/assets-test.js;      allowed "site JavaScript"  docs/assets-test.js
printf '<!doctype html>\n' > docs/interactive-test.html; allowed "site HTML"     docs/interactive-test.html
printf '# t\n' > docs/a-note.md;                      allowed "documentation markdown" docs/a-note.md
cp part_i/main.tex part_i/sibling.tex; cp part_i/main.pdf part_i/sibling.pdf
allowed "PDF rebuilt from a .tex beside it" part_i/sibling.tex part_i/sibling.pdf

echo
echo "$pass passed, $fail failed"
[ "$fail" -eq 0 ]
