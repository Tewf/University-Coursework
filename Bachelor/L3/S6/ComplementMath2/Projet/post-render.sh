#!/usr/bin/env bash
# Post-render: move PDF to rapport/pdf/, leave HTML in place (Quarto book manages site_libs)
set -uo pipefail

RAPPORT_DIR="$(cd "$(dirname "$0")" && pwd)/rapport"
mkdir -p "$RAPPORT_DIR/pdf"

# Move PDF if it was generated at rapport root
if ls "$RAPPORT_DIR"/*.pdf 1>/dev/null 2>&1; then
  mv "$RAPPORT_DIR"/*.pdf "$RAPPORT_DIR/pdf/"
fi
