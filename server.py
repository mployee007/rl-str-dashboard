#!/usr/bin/env python3
import json
import os
import sqlite3
from datetime import datetime, timezone
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
SOURCE_JSON_PATH = ROOT / 'properties.json'
DATA_DIR = Path(os.environ.get('RL_STR_DATA_DIR', os.environ.get('APP_DATA_DIR', str(ROOT)))).resolve()
DB_PATH = Path(os.environ.get('RL_STR_DB_PATH', str(DATA_DIR / 'properties.db'))).resolve()
JSON_PATH = Path(os.environ.get('RL_STR_JSON_PATH', str(DATA_DIR / 'properties.json'))).resolve()
HOST = os.environ.get('RL_STR_HOST', '0.0.0.0')
PORT = int(os.environ.get('PORT', os.environ.get('RL_STR_PORT', '8765')))
STATUSES = {'research', 'contacted', 'review', 'negotiation', 'licensing', 'active', 'hold'}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def normalize_property(payload: dict, existing_id: str | None = None) -> dict:
    payload = payload or {}
    prop_id = str(payload.get('id') or existing_id or f"p_{int(datetime.now().timestamp() * 1000)}")
    status = str(payload.get('status') or 'research').strip().lower()
    if status not in STATUSES:
        status = 'research'
    def num(key, default=0):
        value = payload.get(key, default)
        if value in ('', None):
            return default
        try:
            return float(value)
        except (TypeError, ValueError):
            return default
    def integerish(key, default=0):
        value = num(key, default)
        if int(value) == value:
            return int(value)
        return value
    return {
        'id': prop_id,
        'name': str(payload.get('name') or 'Unnamed').strip(),
        'address': str(payload.get('address') or '').strip(),
        'city': str(payload.get('city') or '').strip(),
        'state': str(payload.get('state') or '').strip(),
        'zip': str(payload.get('zip') or '').strip(),
        'rent': num('rent', 0),
        'beds': integerish('beds', 0),
        'baths': num('baths', 0),
        'sqft': integerish('sqft', 0),
        'url': str(payload.get('url') or '').strip(),
        'zpid': str(payload.get('zpid') or '').strip(),
        'estNightly': num('estNightly', 0),
        'revenue': num('revenue', 0),
        'spread': num('spread', 0),
        'status': status,
        'notes': str(payload.get('notes') or '').strip(),
        'arbitrageScore': num('arbitrageScore', 0),
    }


def row_to_property(row: sqlite3.Row) -> dict:
    item = dict(row)
    return {
        'id': item['id'],
        'name': item['name'],
        'address': item['address'],
        'city': item['city'],
        'state': item['state'],
        'zip': item['zip'],
        'rent': item['rent'],
        'beds': item['beds'],
        'baths': item['baths'],
        'sqft': item['sqft'],
        'url': item['url'],
        'zpid': item['zpid'],
        'estNightly': item['est_nightly'],
        'revenue': item['revenue'],
        'spread': item['spread'],
        'status': item['status'],
        'notes': item['notes'],
        'arbitrageScore': item['arbitrage_score'],
        'estMonthly': item['revenue'],
        'estSpread': item['spread'],
        'createdAt': item['created_at'],
        'updatedAt': item['updated_at'],
    }


def ensure_db() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with get_conn() as conn:
        conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS properties (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                address TEXT DEFAULT '',
                city TEXT DEFAULT '',
                state TEXT DEFAULT '',
                zip TEXT DEFAULT '',
                rent REAL DEFAULT 0,
                beds REAL DEFAULT 0,
                baths REAL DEFAULT 0,
                sqft REAL DEFAULT 0,
                url TEXT DEFAULT '',
                zpid TEXT DEFAULT '',
                est_nightly REAL DEFAULT 0,
                revenue REAL DEFAULT 0,
                spread REAL DEFAULT 0,
                status TEXT NOT NULL DEFAULT 'research',
                notes TEXT DEFAULT '',
                arbitrage_score REAL DEFAULT 0,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            '''
        )
        conn.commit()


def list_properties() -> list[dict]:
    with get_conn() as conn:
        rows = conn.execute('SELECT * FROM properties ORDER BY city, name, id').fetchall()
    return [row_to_property(r) for r in rows]


def export_json() -> None:
    JSON_PATH.write_text(json.dumps(list_properties(), indent=2))


def seed_from_json_if_empty() -> None:
    with get_conn() as conn:
        count = conn.execute('SELECT COUNT(*) FROM properties').fetchone()[0]
        if count:
            return
        seed_path = JSON_PATH if JSON_PATH.exists() else SOURCE_JSON_PATH
        if not seed_path.exists():
            return
        raw = json.loads(seed_path.read_text())
        now = utc_now()
        for payload in raw:
            prop = normalize_property(payload)
            conn.execute(
                '''
                INSERT OR REPLACE INTO properties (
                    id, name, address, city, state, zip, rent, beds, baths, sqft, url, zpid,
                    est_nightly, revenue, spread, status, notes, arbitrage_score, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''',
                (
                    prop['id'], prop['name'], prop['address'], prop['city'], prop['state'], prop['zip'],
                    prop['rent'], prop['beds'], prop['baths'], prop['sqft'], prop['url'], prop['zpid'],
                    prop['estNightly'], prop['revenue'], prop['spread'], prop['status'], prop['notes'],
                    prop['arbitrageScore'], now, now,
                ),
            )
        conn.commit()
    export_json()


def upsert_property(payload: dict, existing_id: str | None = None) -> dict:
    prop = normalize_property(payload, existing_id=existing_id)
    now = utc_now()
    with get_conn() as conn:
        existing = conn.execute('SELECT created_at FROM properties WHERE id = ?', (prop['id'],)).fetchone()
        created_at = existing['created_at'] if existing else now
        conn.execute(
            '''
            INSERT OR REPLACE INTO properties (
                id, name, address, city, state, zip, rent, beds, baths, sqft, url, zpid,
                est_nightly, revenue, spread, status, notes, arbitrage_score, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''',
            (
                prop['id'], prop['name'], prop['address'], prop['city'], prop['state'], prop['zip'],
                prop['rent'], prop['beds'], prop['baths'], prop['sqft'], prop['url'], prop['zpid'],
                prop['estNightly'], prop['revenue'], prop['spread'], prop['status'], prop['notes'],
                prop['arbitrageScore'], created_at, now,
            ),
        )
        conn.commit()
        row = conn.execute('SELECT * FROM properties WHERE id = ?', (prop['id'],)).fetchone()
    export_json()
    return row_to_property(row)


def delete_property(prop_id: str) -> bool:
    with get_conn() as conn:
        cur = conn.execute('DELETE FROM properties WHERE id = ?', (prop_id,))
        conn.commit()
        deleted = cur.rowcount > 0
    if deleted:
        export_json()
    return deleted


class Handler(BaseHTTPRequestHandler):
    def log_message(self, format: str, *args):
        return

    def _read_json(self):
        length = int(self.headers.get('Content-Length', '0') or '0')
        if length == 0:
            return {}
        raw = self.rfile.read(length).decode('utf-8')
        return json.loads(raw) if raw else {}

    def _send_json(self, payload, status=200):
        body = json.dumps(payload).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(body)

    def _send_file(self, path: Path, content_type: str):
        if not path.exists():
            self.send_error(404, 'Not found')
            return
        body = path.read_bytes()
        self.send_response(200)
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        if path == '/api/health':
            self._send_json({'ok': True, 'db_path': str(DB_PATH), 'count': len(list_properties())})
            return
        if path == '/api/properties':
            self._send_json(list_properties())
            return
        if path == '/api/export':
            body = json.dumps(list_properties(), indent=2).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.send_header('Content-Disposition', 'attachment; filename="properties-export.json"')
            self.send_header('Content-Length', str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if path == '/':
            self._send_file(ROOT / 'index.html', 'text/html; charset=utf-8')
            return
        if path == '/properties.json':
            self._send_file(JSON_PATH, 'application/json; charset=utf-8')
            return
        self.send_error(404, 'Not found')

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path != '/api/properties':
            self.send_error(404, 'Not found')
            return
        try:
            payload = self._read_json()
            item = upsert_property(payload)
            self._send_json(item, status=201)
        except Exception as exc:
            self._send_json({'error': str(exc)}, status=400)

    def do_PUT(self):
        parsed = urlparse(self.path)
        parts = [p for p in parsed.path.split('/') if p]
        if len(parts) != 3 or parts[:2] != ['api', 'properties']:
            self.send_error(404, 'Not found')
            return
        prop_id = parts[2]
        try:
            payload = self._read_json()
            payload['id'] = prop_id
            item = upsert_property(payload, existing_id=prop_id)
            self._send_json(item)
        except Exception as exc:
            self._send_json({'error': str(exc)}, status=400)

    def do_DELETE(self):
        parsed = urlparse(self.path)
        parts = [p for p in parsed.path.split('/') if p]
        if len(parts) != 3 or parts[:2] != ['api', 'properties']:
            self.send_error(404, 'Not found')
            return
        deleted = delete_property(parts[2])
        if deleted:
            self._send_json({'ok': True})
        else:
            self._send_json({'error': 'Not found'}, status=404)


def main():
    ensure_db()
    seed_from_json_if_empty()
    export_json()
    last_error = None
    for port in [PORT, PORT + 1, PORT + 2]:
        try:
            server = ThreadingHTTPServer((HOST, port), Handler)
            print(f'R&L STR dashboard running on http://{HOST}:{port}')
            print(f'SQLite DB: {DB_PATH}')
            server.serve_forever()
            return
        except OSError as exc:
            last_error = exc
            continue
    raise last_error if last_error else RuntimeError('Unable to bind server port')


if __name__ == '__main__':
    main()
