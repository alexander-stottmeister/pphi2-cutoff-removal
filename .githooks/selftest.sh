#!/bin/sh
# selftest.sh -- prove that the publication-boundary guard does its job.
#
# Tests the rules as they stand in THIS working tree -- .gitignore and
# .githooks/pre-commit, committed or not -- so run it after editing either, and at
# every gate.  Everything happens in a throwaway clone under $TMPDIR with the two
# rule files copied over from here; the real working tree, its index and both
# repositories are never touched.
#
# Both layers are tested wherever both apply.  A path the ignore file is meant to
# cover must be ignored, which is what keeps it out of `git add -A` and out of an
# unattended commit; and the hook must refuse it anyway once it is forced in with
# `git add -f`.  Allowed files must pass both.
#
#     sh .githooks/selftest.sh
set -eu
export LC_ALL=C

SRC=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
git clone -q --no-hardlinks "$SRC" "$TMP/wt"
for r in .gitignore .githooks/pre-commit; do
  cp "$SRC/$r" "$TMP/wt/$r"
  if ! git -C "$SRC" diff --quiet HEAD -- "$r" 2>/dev/null; then echo "note: testing the uncommitted $r"; fi
done
chmod +x "$TMP/wt/.githooks/pre-commit"
cd "$TMP/wt"
git config core.hooksPath .githooks
git config core.quotePath true        # git's default, whatever this machine is configured with
git config user.email selftest@example.invalid
git config user.name selftest
mkdir -p ../manifests                 # the hook reads the private manifest from ../manifests
printf 'notes/private\n' > ../manifests/glimm_jaffe-private.txt

pass=0; fail=0
ok()  { echo "  ok    $1"; pass=$((pass+1)); }
bad() { echo "  FAIL  $1"; fail=$((fail+1)); }

# refused <label> <ignored|hook> <path...>: with "ignored", .gitignore must cover
# every path; in both cases the hook must refuse the paths once they are forced in.
refused() {
  label=$1 layer=$2; shift 2
  if [ "$layer" = ignored ]; then
    for p in "$@"; do
      if ! git check-ignore -q --no-index -- "$p"; then bad "$label: .gitignore lets $p through"; fi
    done
  fi
  git add -f -- "$@"
  if git diff --cached --quiet; then bad "$label: nothing was staged, so nothing was tested"
  elif .githooks/pre-commit >/dev/null 2>&1; then bad "$label: the hook ALLOWED it"; else ok "$label refused"; fi
  git reset -q
}
# allowed <label> <path...>: neither layer may stop it.
allowed() {
  label=$1; shift
  for p in "$@"; do
    if git check-ignore -q --no-index -- "$p"; then bad "$label: .gitignore ignores $p"; fi
  done
  git add -f -- "$@"
  if git diff --cached --quiet; then bad "$label: nothing was staged, so nothing was tested"
  elif .githooks/pre-commit >/dev/null 2>&1; then ok "$label allowed"; else bad "$label: the hook REFUSED it"; fi
  git reset -q
}

# Signatures, the first bytes of each format; nothing else of the file is needed.
mk_png()  { printf '\211PNG\r\n\032\n\000\000\000\015IHDR' > "$1"; }
mk_jpeg() { printf '\377\330\377\340\000\020JFIF\000' > "$1"; }
mk_avif() { printf '\000\000\000\034ftypavif\000\000\000\000mif1' > "$1"; }
mk_heic() { printf '\000\000\000\030ftypheic\000\000\000\000' > "$1"; }
mk_jxl()  { printf '\000\000\000\014JXL \015\012\207\012' > "$1"; }
mk_jp2()  { printf '\000\000\000\014jP  \015\012\207\012' > "$1"; }
mk_zip()  { printf 'PK\003\004\024\000\000\000\010\000' > "$1"; }
mk_gz()   { printf '\037\213\010\000\000\000\000\000' > "$1"; }
# A one-page PDF whose page draws a 1x1 raster image: what a document built from the
# page-image corpus looks like to pdfimages.
mk_imgpdf() {
  printf '%%PDF-1.4\n1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj\n2 0 obj << /Type /Pages /Kids [3 0 R] /Count 1 >> endobj\n3 0 obj << /Type /Page /Parent 2 0 R /MediaBox [0 0 10 10] /Resources << /XObject << /Im1 4 0 R >> >> /Contents 5 0 R >> endobj\n4 0 obj << /Type /XObject /Subtype /Image /Width 1 /Height 1 /ColorSpace /DeviceGray /BitsPerComponent 8 /Length 1 >> stream\n\200\nendstream endobj\n5 0 obj << /Length 27 >> stream\nq 10 0 0 10 0 0 cm /Im1 Do Q\nendstream endobj\ntrailer << /Root 1 0 R >>\n%%%%EOF\n' > "$1"
}
mkdir -p refs evidence part_ii/dossier_images docs/figures notes/private

echo "must be refused, by name:"
printf 'x' > refs/acquired-paper.pdf;        refused "source PDF under refs/"           ignored refs/acquired-paper.pdf
printf 'x' > evidence/page-001.png;          refused "page image in evidence/"          ignored evidence/page-001.png
printf 'x' > part_ii/dossier_images/p1.png;  refused "page image in dossier_images/"    ignored part_ii/dossier_images/p1.png
for e in png jpg webp avif heic jxl jp2 tiff psd; do
  printf 'x' > "docs/figures/scan.$e";       refused "*.$e anywhere"                   ignored "docs/figures/scan.$e"
done
printf 'x' > part_i/my-dossier.pdf;          refused "*dossier*.pdf"                    ignored part_i/my-dossier.pdf
printf 'x' > PRIVATE.md;                     refused "PRIVATE.md"                       ignored PRIVATE.md
rm -f PRIVATE.md
printf 'x' > notes/evidence-bundle.zip;      refused "*.zip anywhere"                   ignored notes/evidence-bundle.zip
printf 'x' > notes/pages.tar.gz;             refused "*.tar.gz anywhere"                ignored notes/pages.tar.gz
printf 'x' > part_ii/acquired.pdf;           refused "new PDF with no .tex beside it"   hook part_ii/acquired.pdf
printf '%% draft\n' > part_ii/draft.tex; cp part_i/main.pdf part_ii/draft.pdf
refused "new PDF beside an untracked .tex" hook part_ii/draft.pdf
printf '%%!PS-Adobe-3.0\n%%%%Title: a paper\nshowpage\n' > part_ii/paper.ps
refused "new PostScript with no .tex beside it" hook part_ii/paper.ps
printf 'x\n' > notes/private/draft.md;       refused "a path the private manifest claims" hook notes/private/draft.md

echo "must be refused, by content, whatever the name says:"
mk_png  notes/figure.dat;                    refused "PNG named .dat"                   hook notes/figure.dat
mk_jpeg notes/scan;                          refused "JPEG with no extension"           hook notes/scan
mk_avif notes/page.bin;                      refused "AVIF named .bin"                  hook notes/page.bin
mk_heic notes/photo.txt;                     refused "HEIC named .txt"                  hook notes/photo.txt
mk_jxl  notes/page.data;                     refused "JPEG XL named .data"              hook notes/page.data
mk_jp2  notes/page2.data;                    refused "JPEG 2000 named .data"            hook notes/page2.data
mk_zip  notes/bundle.data;                   refused "zip archive named .data"          hook notes/bundle.data
mk_gz   notes/bundle2.data;                  refused "gzip archive named .data"         hook notes/bundle2.data
printf '%%PDF-1.4\n1 0 obj\n<< >>\nendobj\ntrailer << >>\n%%%%EOF\n' > notes/paper.txt
refused "PDF named .txt" hook notes/paper.txt
printf '%%!PS-Adobe-3.0\nshowpage\n' > notes/paper2.txt
refused "PostScript named .txt" hook notes/paper2.txt
cp part_i/main.tex part_i/scan-note.tex; mk_imgpdf part_i/scan-note.pdf
refused "PDF that embeds a raster image, .tex beside it" hook part_i/scan-note.tex part_i/scan-note.pdf
printf '<svg xmlns="http://www.w3.org/2000/svg"><image href="data%simage/png;base64,iVBORw0KGgo="/></svg>\n' ':' > docs/figures/annotated.svg
refused "SVG carrying a PNG as a data URI" hook docs/figures/annotated.svg
printf '<!doctype html>\n<img src="data%simage/jpeg;base64,/9j/4AAQ">\n' ':' > docs/embed-test.html
refused "HTML carrying a JPEG as a data URI" hook docs/embed-test.html

echo "must be refused, however the name is spelt:"
printf 'x' > "refs/Glimm–Jaffe–Spencer 1974.pdf"
refused "source PDF under refs/, non-ASCII name" ignored "refs/Glimm–Jaffe–Spencer 1974.pdf"
printf 'x' > "docs/figures/Seite-ü.png"
refused "PNG with a non-ASCII name" ignored "docs/figures/Seite-ü.png"
# A name of its own: on a case-insensitive disk SCAN.PNG would be scan.png above.
printf 'x' > docs/figures/PAGE.PNG;          refused "upper-case .PNG"                  hook docs/figures/PAGE.PNG
printf 'x' > 'docs/we"ird.md';               refused "a name git must quote"            hook 'docs/we"ird.md'

echo "must be allowed:"
printf '<svg xmlns="http://www.w3.org/2000/svg"/>' > docs/figures/rate.svg
allowed "SVG figure under docs/figures/" docs/figures/rate.svg
printf 'console.log(1)\n' > docs/assets-test.js;          allowed "site JavaScript"          docs/assets-test.js
printf '<!doctype html>\n' > docs/interactive-test.html;  allowed "site HTML"                docs/interactive-test.html
printf '# t\n' > docs/a-note.md;                          allowed "documentation markdown"   docs/a-note.md
printf 'Figures may carry data%simage/svg+xml;utf8,<svg/> and nothing raster.\n' ':' > docs/data-uri-note.md
allowed "text naming an SVG data URI" docs/data-uri-note.md
printf 'BMP files are refused by name and by content.\n' > docs/bm-note.md
allowed "text that starts with BM" docs/bm-note.md
printf '%%PDF-1.5 is what pdflatex writes here.\n\\relax\n' > part_i/pdfnote.tex
allowed "a .tex whose first line mentions %PDF-1.5" part_i/pdfnote.tex
printf '# Übersicht\n' > "docs/Übersicht.md";             allowed "a harmless non-ASCII name" "docs/Übersicht.md"
cp part_i/main.tex part_i/sibling.tex; cp part_i/main.pdf part_i/sibling.pdf
if command -v pdfimages >/dev/null 2>&1; then
  allowed "PDF rebuilt from a .tex beside it" part_i/sibling.tex part_i/sibling.pdf
  printf '\n' >> part_i/main.pdf
  allowed "a rebuilt part_i/main.pdf" part_i/main.pdf
  git checkout -q -- part_i/main.pdf
else
  echo "  note  pdfimages (poppler) is missing, so this machine's hook refuses every PDF"
  refused "PDF rebuilt from a .tex beside it, without pdfimages" hook part_i/sibling.tex part_i/sibling.pdf
fi

echo "end to end, through core.hooksPath and git commit:"
before=$(git rev-parse HEAD)
git add -f -- docs/figures/scan.png
if git commit -q -m selftest >/dev/null 2>&1 || [ "$(git rev-parse HEAD)" != "$before" ]; then
  bad "git commit of a PNG went through"
else
  ok "git commit of a PNG refused"
fi
git reset -q
git add -f -- docs/a-note.md
if git commit -q -m selftest >/dev/null 2>&1 && [ "$(git rev-parse HEAD)" != "$before" ]; then
  ok "git commit of a markdown file went through"
else
  bad "git commit of a markdown file was refused"
fi

echo
echo "$pass passed, $fail failed"
[ "$fail" -eq 0 ]
