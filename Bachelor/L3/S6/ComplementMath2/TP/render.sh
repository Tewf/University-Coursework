#!/usr/bin/env bash
# Render Correction QMDs to PDF (pdf/) and HTML (html/)
# Usage:
#   ./render.sh          # render all
#   ./render.sh 6        # render TP6 only
#   ./render.sh 6 7      # render TP6 and TP7
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

export QUARTO_R="~/miniforge3/envs/r_env/bin/R"
QUARTO="/usr/local/bin/quarto"
PDF_DIR="pdf"
HTML_DIR="html"

mkdir -p "$PDF_DIR" "$HTML_DIR"

render_one() {
  local src="$1"
  local dir base base_dash
  dir="$(dirname "$src")"
  base="$(basename "$src" .qmd)"
  base_dash="${base// /-}"  # quarto uses dashes for PDF filenames

  echo "──── Rendering $src ────"

  (cd "$dir" && "$QUARTO" render "$(basename "$src")" --to pdf  2>&1)
  (cd "$dir" && "$QUARTO" render "$(basename "$src")" --to html 2>&1)

  # PDF: quarto may use dashes or spaces — try both
  if [ -f "$dir/$base_dash.pdf" ]; then
    mv -f "$dir/$base_dash.pdf" "$PDF_DIR/$base.pdf"
  elif [ -f "$dir/$base.pdf" ]; then
    mv -f "$dir/$base.pdf" "$PDF_DIR/$base.pdf"
  else
    echo "  WARNING: PDF not found in $dir/"
  fi

  # HTML: quarto keeps the original name with spaces
  if [ -f "$dir/$base.html" ]; then
    mv -f "$dir/$base.html" "$HTML_DIR/$base.html"
  elif [ -f "$dir/$base_dash.html" ]; then
    mv -f "$dir/$base_dash.html" "$HTML_DIR/$base.html"
  else
    echo "  WARNING: HTML not found in $dir/"
  fi

  echo "  -> $PDF_DIR/$base.pdf"
  echo "  -> $HTML_DIR/$base.html"
  echo
}

if [ $# -eq 0 ]; then
  # Render all
  find TP* -maxdepth 1 -name 'Correction*.qmd' -print0 | sort -z | while IFS= read -r -d '' src; do
    render_one "$src"
  done
else
  # Render specified TPs
  for n in "$@"; do
    src="$(find "TP${n}" -maxdepth 1 -name 'Correction*.qmd' -print -quit 2>/dev/null || true)"
    if [ -z "$src" ]; then
      echo "ERROR: No Correction QMD found in TP${n}/"
      exit 1
    fi
    render_one "$src"
  done
fi

echo "Done."
