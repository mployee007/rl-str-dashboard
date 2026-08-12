#!/usr/bin/env bash
set -euo pipefail
cd /opt/data/rl-str-dashboard
python3 build_dashboard.py >/tmp/hermes-dashboard-build.json
git add index.html data/archive.json public .nojekyll build_dashboard.py README.md
if git diff --cached --quiet; then
  exit 0
fi
stamp=$(date -u +"%Y-%m-%d %H:%M:%S UTC")
git commit -m "Sync completed work dashboard - ${stamp}" >/dev/null
git push origin main >/dev/null
echo "Dashboard synced to GitHub at ${stamp}"
