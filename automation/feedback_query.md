# Feedback Query

Current version date: 2026-05-06

## Purpose

Automatically query configured read-only sources before weekly review and, when possible, before daily chapter generation.

## Source Priority

1. Local repository files.
2. `feedback/source_config.md`.
3. Fanqie metrics export files placed in `feedback/imports/`.
4. Read-only browser/CDP query scripts, if explicitly configured.
5. GitHub repository metadata, if network is available.

## Output Files

Query results should update:

1. `feedback/chapter_metrics.md`
2. `feedback/reader_comments.md`
3. `feedback/title_performance.md`
4. `feedback/retention_notes.md`
5. `feedback/query_log.md`

## Rules

1. Query is read-only.
2. Do not publish.
3. Do not edit Fanqie backend.
4. Do not click destructive or submit buttons.
5. If a source is unavailable, record it in `feedback/query_log.md` and continue.
6. Never block chapter generation solely because feedback query failed.

## Fanqie Query Modes

### Mode A: Manual Export Import

If the user exports metrics/comments to `feedback/imports/`, automation may parse the files and update feedback tables.

Supported expected file types:

1. `.csv`
2. `.txt`
3. `.md`
4. `.json`

### Mode B: Browser Read-Only Query

Only allowed when all are true:

1. Chromium CDP is running at `http://127.0.0.1:9222`.
2. Current page is visibly a Fanqie author analytics or comments page.
3. The query script only reads page text and does not click publish/save/delete/submit controls.
4. Query result is stored locally.

If the page cannot be verified, skip browser query.

Implementation:

```powershell
python tools/fanqie_readonly_metrics.py
```

This script:

1. Connects to Chromium over CDP.
2. Reads only URL, title, body text, and visible page content.
3. Verifies that the page appears to be a Fanqie analytics/comments page.
4. Writes JSON and page text to `feedback/imports/`.
5. Updates `feedback/query_log.md`.
6. Does not click, publish, save, submit, or edit anything.

## Missing Data Policy

When real metrics are missing, keep placeholders and record:

```text
Source unavailable; no data imported.
```
