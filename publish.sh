#!/usr/bin/env bash
# Publish Instagram Stats to GitHub Pages (https://harpreetsbajwa92.github.io/instagram-stats/)
set -e
cd "$(dirname "$0")"
git add -A
if git diff --cached --quiet; then echo "no changes"; exit 0; fi
git commit -qm "Update stats $(date '+%Y-%m-%d %H:%M')"
git push -q origin main
echo "published"
