#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
PORT="${PORT:-4173}"

python3 scripts/check.py
echo
echo "United We Co-op local V1"
echo "http://localhost:${PORT}"
echo "Ctrl+C to stop."
echo
exec python3 -m http.server "${PORT}" --bind 127.0.0.1
