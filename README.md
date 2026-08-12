# Hermes Completed Work Dashboard

Static dashboard built from `/opt/data/outputs` for GitHub Pages / Cloudflare Pages.

## What it does
- indexes saved Hermes session folders under `outputs/YYYY-MM-DD/<session>/`
- surfaces `summary.md`, `notes.md`, `decisions.md`, `run-log.md`
- groups exports, CSV files, images/charts, and other artifacts
- rebuilds into a static site suitable for GitHub/Cloudflare Pages

## Rebuild
```bash
python3 build_dashboard.py
```

## Auto-sync
A sync script can rebuild, commit, and push changes:
```bash
bash scripts/sync_dashboard.sh
```
