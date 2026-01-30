# links expert

Self-hosted bookmark manager: minimal, fast, easy to set up with Docker. Fork of [linkding](https://github.com/sissbruecker/linkding).

## Features

- Bookmarks with tags and full-text search
- REST API and browser extension
- Catppuccin themes (latte, frappe, macchiato, mocha, auto) via `LD_THEME`
- Bundles, archiving, backups, OIDC/auth proxy support

## Requirements

- **Production:** Docker and Docker Compose
- **Development:** Python 3.13+, Node.js, npm

## Quick start

1. Copy [.env.sample](.env.sample) to `.env` and adjust (e.g. `LD_SUPERUSER_NAME`, `LD_SUPERUSER_PASSWORD`, `LD_THEME`, `LD_CONTEXT_PATH`).
2. Run:

   ```bash
   docker-compose up -d
   ```

3. Open the app at `http://localhost:9090` (or the port set in `LD_HOST_PORT`).

## Build and development

- Install dependencies: `npm install`, `uv sync` (or `pip install -r …`).
- Build frontend: `npm run build`.
- Run dev server: `uv run manage.py runserver` (see [Makefile](Makefile) for `make serve`, `make test`, etc.).
- Static files: `uv run manage.py collectstatic --no-input` when preparing for production.
- Tests: `uv run pytest` (see [pytest.ini](pytest.ini) / [pyproject.toml](pyproject.toml)).

## Documentation

See the [docs](docs/) directory for installation, options, API, browser extension, and more.

## Credits

Based on [linkding](https://github.com/sissbruecker/linkding) by sissbruecker. Developed by [runawaydevil](https://github.com/runawaydevil) — 2026. Contact: [runawaydevil@pm.me](mailto:runawaydevil@pm.me).
