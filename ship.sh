#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

python3 scripts/check.py
git diff --check
git add -A

if ! git diff --cached --quiet; then
  git commit -m "${1:-Ship United We Co-op V1}"
else
  echo "No new changes to commit."
fi

git branch -M main
git push -u origin main

echo "Shipped to https://github.com/cleverIdeaz/united-we-coop"
