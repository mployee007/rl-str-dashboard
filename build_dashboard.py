#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
OUTPUTS_ROOT = Path('/opt/data/outputs')
DATA_DIR = REPO_ROOT / 'data'
PUBLIC_DIR = REPO_ROOT / 'public'
ARCHIVE_JSON = DATA_DIR / 'archive.json'
INDEX_HTML = REPO_ROOT / 'index.html'
NOJEKYLL = REPO_ROOT / '.nojekyll'
TEXT_EXTS = {'.md', '.txt', '.json', '.csv', '.html', '.yml', '.yaml', '.log'}
STANDARD_FILES = ['summary.md', 'notes.md', 'decisions.md', 'sources.json', 'run-log.md']

STYLE = '''
:root {
  --bg: #0d1117;
  --surface: #161b22;
  --surface2: #1c2333;
  --border: #30363d;
  --text: #e6edf3;
  --muted: #8b949e;
  --accent: #58a6ff;
  --green: #3fb950;
  --orange: #d29922;
  --purple: #bc8cff;
  --red: #f85149;
  --radius: 12px;
}
* { box-sizing: border-box; }
body { margin: 0; font-family: Inter, system-ui, -apple-system, sans-serif; background: var(--bg); color: var(--text); }
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
.layout { display: grid; grid-template-columns: 380px 1fr; min-height: 100vh; }
.sidebar { border-right: 1px solid var(--border); background: var(--surface); padding: 18px; overflow: auto; }
.main { padding: 22px; overflow: auto; }
h1, h2, h3 { margin: 0; }
.sub { color: var(--muted); font-size: 13px; margin-top: 6px; }
.stats { display: flex; gap: 10px; flex-wrap: wrap; margin: 16px 0 18px; }
.stat { background: var(--surface2); border: 1px solid var(--border); border-radius: 10px; padding: 10px 12px; min-width: 110px; }
.stat .label { color: var(--muted); font-size: 11px; text-transform: uppercase; letter-spacing: .6px; }
.stat .value { font-size: 18px; font-weight: 700; margin-top: 4px; }
input[type="search"] { width: 100%; padding: 12px 14px; border-radius: 10px; border: 1px solid var(--border); background: #0b1220; color: var(--text); }
.session-list { margin-top: 16px; display: flex; flex-direction: column; gap: 10px; }
.session-card { border: 1px solid var(--border); background: #111827; border-radius: 12px; padding: 14px; cursor: pointer; }
.session-card:hover, .session-card.active { border-color: var(--accent); background: #172033; }
.session-title { font-size: 14px; font-weight: 700; line-height: 1.3; }
.session-meta { color: var(--muted); font-size: 12px; margin-top: 6px; display: flex; justify-content: space-between; gap: 8px; }
.session-summary { color: #c7d2e0; font-size: 12px; margin-top: 8px; line-height: 1.45; }
.pillbar { display: flex; gap: 6px; flex-wrap: wrap; margin-top: 10px; }
.pill { font-size: 10px; border-radius: 999px; padding: 3px 8px; border: 1px solid var(--border); color: var(--muted); }
.topbar { display: flex; justify-content: space-between; gap: 16px; align-items: flex-start; margin-bottom: 18px; }
.hero { background: linear-gradient(180deg, #141d2d, #0f1724); border: 1px solid var(--border); border-radius: 14px; padding: 18px; }
.hero-title { font-size: 26px; font-weight: 800; line-height: 1.15; }
.hero-sub { margin-top: 8px; color: var(--muted); }
.section { margin-top: 18px; }
.section-head { display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; }
.grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; }
.panel { background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 14px; }
.panel h3 { font-size: 14px; margin-bottom: 10px; }
.preview { white-space: pre-wrap; background: #0b1220; border: 1px solid var(--border); border-radius: 12px; padding: 14px; max-height: 420px; overflow: auto; font-size: 12px; line-height: 1.5; }
.file-list { display: flex; flex-direction: column; gap: 8px; }
.file-item { display: flex; justify-content: space-between; align-items: center; gap: 10px; padding: 10px 12px; border: 1px solid var(--border); border-radius: 10px; background: #111827; }
.file-item .name { font-size: 13px; font-weight: 600; }
.file-item .meta { font-size: 11px; color: var(--muted); margin-top: 3px; }
.btnrow { display: flex; gap: 8px; flex-wrap: wrap; }
button, .alink { background: transparent; color: var(--text); border: 1px solid var(--border); border-radius: 10px; padding: 8px 12px; cursor: pointer; text-decoration: none; font-size: 12px; }
button:hover, .alink:hover { border-color: var(--accent); color: white; }
.kpi { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 10px; margin-top: 14px; }
.kpi .box { background: #111827; border: 1px solid var(--border); border-radius: 12px; padding: 12px; }
.kpi .box .v { font-size: 20px; font-weight: 800; }
.kpi .box .l { color: var(--muted); font-size: 11px; margin-top: 4px; text-transform: uppercase; }
.badge { display: inline-block; background: rgba(63,185,80,.12); color: var(--green); border: 1px solid rgba(63,185,80,.25); border-radius: 999px; padding: 4px 8px; font-size: 11px; }
.empty { color: var(--muted); padding: 20px 0; }
.footer-note { color: var(--muted); font-size: 12px; margin-top: 8px; }
@media (max-width: 980px) {
  .layout { grid-template-columns: 1fr; }
  .sidebar { border-right: none; border-bottom: 1px solid var(--border); max-height: 42vh; }
  .grid, .kpi { grid-template-columns: 1fr; }
}
'''


def read_text(path: Path, limit: int = 5000) -> str:
    try:
        text = path.read_text(errors='replace')
    except Exception as exc:
        return f'[error reading file: {exc}]'
    return text[:limit] + ('\n\n[truncated]' if len(text) > limit else '')


def summarize_markdown(path: Path) -> str:
    text = read_text(path, limit=1400).strip()
    if not text:
        return ''
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    body = []
    for ln in lines:
        if ln.startswith('#'):
            continue
        body.append(ln)
        if len(' '.join(body)) > 280:
            break
    return (' '.join(body)[:280].strip() or (lines[0][:280] if lines else '')).strip()


def classify_file(path: Path) -> str:
    rel = path.as_posix()
    if '/artifacts/exports/' in rel:
        return 'export'
    if '/artifacts/csv/' in rel:
        return 'csv'
    if '/artifacts/images/' in rel or '/artifacts/charts/' in rel:
        return 'image'
    if path.name in STANDARD_FILES:
        return 'standard'
    return 'other'


def ensure_dirs() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    PUBLIC_DIR.mkdir(exist_ok=True)


def clear_public_tree() -> None:
    if not PUBLIC_DIR.exists():
        return
    for p in sorted(PUBLIC_DIR.rglob('*'), reverse=True):
        if p.is_file():
            p.unlink()
        elif p.is_dir():
            try:
                p.rmdir()
            except OSError:
                pass


def mirror_text_file(src: Path, dest: Path) -> str | None:
    if src.suffix.lower() not in TEXT_EXTS:
        return None
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(read_text(src, limit=50000))
    return dest.resolve().relative_to(REPO_ROOT.resolve()).as_posix()


def collect_session(session_dir: Path, date_dir: str) -> dict:
    files = [p for p in sorted(session_dir.rglob('*')) if p.is_file()]
    exports = [p for p in files if '/artifacts/exports/' in p.as_posix()]
    csvs = [p for p in files if '/artifacts/csv/' in p.as_posix()]
    images = [p for p in files if '/artifacts/images/' in p.as_posix() or '/artifacts/charts/' in p.as_posix()]
    updated = max((p.stat().st_mtime for p in files), default=session_dir.stat().st_mtime)
    session_id = f'{date_dir}/{session_dir.name}'
    grouped = {'export': [], 'csv': [], 'image': [], 'other': []}
    standard_previews = {}
    public_dir = PUBLIC_DIR / date_dir / session_dir.name

    for p in files:
        rel = p.resolve().relative_to(session_dir.resolve()).as_posix()
        kind = classify_file(p)
        if p.name in STANDARD_FILES:
            standard_previews[p.name] = read_text(p, limit=5000)
        public_href = mirror_text_file(p, public_dir / rel)
        if kind != 'standard':
            grouped[kind].append({
                'name': p.name,
                'rel_path': rel,
                'size': p.stat().st_size,
                'updated_at': datetime.fromtimestamp(p.stat().st_mtime).isoformat(),
                'previewable': p.suffix.lower() in TEXT_EXTS,
                'public_href': public_href,
            })

    return {
        'id': session_id,
        'date': date_dir,
        'title': session_dir.name,
        'summary': summarize_markdown(session_dir / 'summary.md') if (session_dir / 'summary.md').exists() else '',
        'updated_at': datetime.fromtimestamp(updated).isoformat(),
        'file_count': len(files),
        'export_count': len(exports),
        'csv_count': len(csvs),
        'image_count': len(images),
        'path': str(session_dir),
        'status': 'completed',
        'standard_previews': standard_previews,
        'files': grouped,
    }


def build_archive() -> dict:
    ensure_dirs()
    clear_public_tree()
    sessions = []
    for date_dir in sorted([p for p in OUTPUTS_ROOT.iterdir() if p.is_dir()], reverse=True):
        if date_dir.name == 'incoming':
            continue
        for session_dir in sorted([p for p in date_dir.iterdir() if p.is_dir()], key=lambda p: p.name.lower()):
            sessions.append(collect_session(session_dir, date_dir.name))
    sessions.sort(key=lambda x: x['updated_at'], reverse=True)
    archive = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'source_root': str(OUTPUTS_ROOT),
        'session_count': len(sessions),
        'sessions': sessions,
    }
    ARCHIVE_JSON.write_text(json.dumps(archive, indent=2))
    NOJEKYLL.write_text('')
    return archive


def render_index(archive: dict) -> str:
    data_json = json.dumps(archive)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Hermes Completed Work Dashboard</title>
<style>{STYLE}</style>
</head>
<body>
<div class="layout">
  <aside class="sidebar">
    <h2>Hermes Completed Work</h2>
    <div class="sub">Static dashboard generated from saved outputs. Cloudflare Pages ready.</div>
    <div class="stats" id="stats"></div>
    <input id="search" type="search" placeholder="Search sessions, summaries, notes..." />
    <div class="session-list" id="sessionList"></div>
  </aside>
  <main class="main">
    <div class="topbar">
      <div>
        <div class="badge">auto-synced archive</div>
        <div class="footer-note" id="generatedAt"></div>
      </div>
      <div class="btnrow">
        <a class="alink" href="data/archive.json" target="_blank">Open archive.json</a>
      </div>
    </div>
    <div id="content"></div>
  </main>
</div>
<script>
const ARCHIVE = {data_json};
let sessions = ARCHIVE.sessions || [];
let activeId = sessions.length ? sessions[0].id : null;

function esc(s) {{
  return String(s ?? '').replace(/[&<>\"']/g, m => ({{'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;',"'":'&#39;'}}[m]));
}}
function fmtDate(s) {{ try {{ return new Date(s).toLocaleString(); }} catch {{ return s || ''; }} }}
function previewHtml(text) {{ return `<div class="preview">${{esc(text || 'Missing')}}</div>`; }}
function filteredSessions() {{
  const q = document.getElementById('search').value.trim().toLowerCase();
  if (!q) return sessions;
  return sessions.filter(s => JSON.stringify(s).toLowerCase().includes(q));
}}
function renderStats() {{
  const stats = document.getElementById('stats');
  const total = sessions.length;
  const exportsCount = sessions.reduce((a, s) => a + (s.export_count || 0), 0);
  const files = sessions.reduce((a, s) => a + (s.file_count || 0), 0);
  stats.innerHTML = `
    <div class="stat"><div class="label">sessions</div><div class="value">${{total}}</div></div>
    <div class="stat"><div class="label">completed</div><div class="value">${{total}}</div></div>
    <div class="stat"><div class="label">exports</div><div class="value">${{exportsCount}}</div></div>
    <div class="stat"><div class="label">files</div><div class="value">${{files}}</div></div>`;
  document.getElementById('generatedAt').textContent = `Generated ${{fmtDate(ARCHIVE.generated_at)}} from ${{ARCHIVE.source_root}}`;
}}
function renderSessionList(items) {{
  const list = document.getElementById('sessionList');
  if (!items.length) {{ list.innerHTML = '<div class="empty">No sessions found.</div>'; return; }}
  list.innerHTML = items.map(s => `
    <div class="session-card ${{s.id === activeId ? 'active' : ''}}" onclick="openSession('${{encodeURIComponent(s.id)}}')">
      <div class="session-title">${{esc(s.title)}}</div>
      <div class="session-meta"><span>${{esc(s.date)}}</span><span>${{s.export_count || 0}} exports</span></div>
      <div class="session-summary">${{esc(s.summary || 'No summary available yet.')}}</div>
      <div class="pillbar">
        <span class="pill">completed</span>
        <span class="pill">${{s.file_count || 0}} files</span>
        <span class="pill">updated ${{esc(fmtDate(s.updated_at))}}</span>
      </div>
    </div>`).join('');
}}
function fileGroup(title, files) {{
  if (!files || !files.length) return `<div class="panel"><h3>${{title}}</h3><div class="empty">None</div></div>`;
  return `<div class="panel"><h3>${{title}}</h3><div class="file-list">${{files.map(f => `
    <div class="file-item">
      <div>
        <div class="name">${{esc(f.name)}}</div>
        <div class="meta">${{esc(f.rel_path)}} • ${{Math.max(1, Math.round((f.size||0)/1024))}} KB • ${{esc(fmtDate(f.updated_at))}}</div>
      </div>
      <div class="btnrow">
        ${{f.public_href ? `<a class="alink" href="${{f.public_href}}" target="_blank">Open</a>` : ''}}
      </div>
    </div>`).join('')}}</div></div>`;
}}
function renderContent(s) {{
  const standard = s.standard_previews || {{}};
  document.getElementById('content').innerHTML = `
    <div class="hero">
      <div class="hero-title">${{esc(s.title)}}</div>
      <div class="hero-sub">${{esc(s.date)}} • source folder: ${{esc(s.path)}}</div>
      <div class="kpi">
        <div class="box"><div class="v">${{s.file_count || 0}}</div><div class="l">Files</div></div>
        <div class="box"><div class="v">${{s.export_count || 0}}</div><div class="l">Exports</div></div>
        <div class="box"><div class="v">${{s.csv_count || 0}}</div><div class="l">CSV</div></div>
        <div class="box"><div class="v">${{s.image_count || 0}}</div><div class="l">Images/Charts</div></div>
      </div>
    </div>
    <div class="section">
      <div class="section-head"><h2>Core session documents</h2></div>
      <div class="grid">
        <div class="panel"><h3>summary.md</h3>${{previewHtml(standard['summary.md'])}}</div>
        <div class="panel"><h3>notes.md</h3>${{previewHtml(standard['notes.md'])}}</div>
        <div class="panel"><h3>decisions.md</h3>${{previewHtml(standard['decisions.md'])}}</div>
        <div class="panel"><h3>run-log.md</h3>${{previewHtml(standard['run-log.md'])}}</div>
      </div>
    </div>
    <div class="section">
      <div class="section-head"><h2>Artifacts and deliverables</h2></div>
      <div class="grid">
        ${{fileGroup('Exports', s.files.export)}}
        ${{fileGroup('CSV data', s.files.csv)}}
        ${{fileGroup('Images / charts', s.files.image)}}
        ${{fileGroup('Other files', s.files.other)}}
      </div>
    </div>`;
}}
function openSession(id) {{
  activeId = decodeURIComponent(id);
  renderSessionList(filteredSessions());
  const s = sessions.find(x => x.id === activeId);
  if (s) renderContent(s);
}}
document.getElementById('search').addEventListener('input', () => renderSessionList(filteredSessions()));
renderStats();
renderSessionList(filteredSessions());
if (sessions.length) renderContent(sessions[0]);
</script>
</body>
</html>'''


def main() -> None:
    archive = build_archive()
    INDEX_HTML.write_text(render_index(archive))
    print(json.dumps({
        'generated_at': archive['generated_at'],
        'session_count': archive['session_count'],
        'index_html': str(INDEX_HTML),
        'archive_json': str(ARCHIVE_JSON),
    }, indent=2))

if __name__ == '__main__':
    main()
