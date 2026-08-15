#!/usr/bin/env bash
# Render scripts/resume.html -> assets/Vanga-Akash-Reddy-Resume.pdf
#
# resume.html is the single source of truth for the resume. Edit that, run
# this, and commit both. Uses headless Chrome so there is nothing to install
# (the previous fpdf-based Python generator could not run on a PEP 668
# system Python).
#
#   ./scripts/build-resume.sh [extra-output.pdf ...]
#
# Any paths passed as arguments get a copy of the same PDF.

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$ROOT/scripts/resume.html"
OUT="$ROOT/assets/Vanga-Akash-Reddy-Resume.pdf"

CHROME=""
for candidate in \
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  "/Applications/Chromium.app/Contents/MacOS/Chromium" \
  "$(command -v google-chrome || true)" \
  "$(command -v chromium || true)"; do
  if [ -n "$candidate" ] && [ -x "$candidate" ]; then
    CHROME="$candidate"
    break
  fi
done

if [ -z "$CHROME" ]; then
  echo "error: no Chrome/Chromium found — install one, or open $SRC and print to PDF." >&2
  exit 1
fi

mkdir -p "$(dirname "$OUT")"

"$CHROME" \
  --headless \
  --disable-gpu \
  --no-pdf-header-footer \
  --print-to-pdf="$OUT" \
  "file://$SRC" 2>/dev/null

if [ ! -s "$OUT" ]; then
  echo "error: Chrome produced no output at $OUT" >&2
  exit 1
fi

echo "Wrote $OUT ($(du -h "$OUT" | cut -f1))"

for extra in "$@"; do
  cp "$OUT" "$extra"
  echo "Copied to $extra"
done
