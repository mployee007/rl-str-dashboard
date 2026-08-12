# Railway deployment guide for rl-str-dashboard

## Repo
- https://github.com/mployee007/rl-str-dashboard
- Commit: `f241fa6818b700a19eafc37ef83853b13b575f4e`

## What is already done
- Dockerfile exists at repo root, so Railway can auto-detect and build the service.
- The app listens on `PORT` and `0.0.0.0`.
- The app can persist SQLite data by setting `APP_DATA_DIR=/data`.
- Health endpoint exists at `/api/health`.

## Railway setup steps
1. In Railway, create a new project.
2. Choose **Deploy from GitHub repo**.
3. Select `mployee007/rl-str-dashboard`.
4. Add a **Volume** and mount it at `/data`.
5. In Variables, set:
   - `APP_DATA_DIR=/data`
6. Open the service **Networking** tab and generate a domain.
7. After deploy, verify:
   - `/api/health` returns JSON
   - the dashboard loads in live mode

## Optional CLI flow
```bash
cd /opt/data/rl-str-dashboard
npx @railway/cli login
npx @railway/cli init
npx @railway/cli up
```

## Important
- Without a Railway volume, SQLite data will be ephemeral.
- GitHub Pages can remain your read-only static board; Railway should be the editable admin app.
