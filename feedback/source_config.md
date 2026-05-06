# Feedback Source Config

Current version date: 2026-05-06

## Enabled Sources

| Source | Status | Mode | Notes |
| --- | --- | --- | --- |
| Local files | enabled | read-only | Always available |
| Feedback imports | enabled | read-only | Put exports in `feedback/imports/` |
| Fanqie browser analytics | optional | read-only CDP | Requires verified Fanqie analytics/comments page |
| GitHub repository | enabled | read-only network | Useful for repository state, not reader data |

## External Publishing

```text
auto_publish_external: true
```

This config enables automatic query and unattended Fanqie publishing through `tools/fanqie_safe_publish.py`.

Automatic publishing remains guarded by:

1. Chapter number validation.
2. No-blank-line publish file validation.
3. Fanqie page verification.
4. Fill-and-read-back body verification.
5. Publish log and screenshots.
6. Local JSON audit record.

## Read-Only Query Tool

```powershell
python tools/fanqie_readonly_metrics.py
```

This tool may run automatically when a verified analytics or comments page is open in the CDP-connected Chromium session.

If the page cannot be verified, it skips and records the reason.

## Import Folder

Place exported reader metrics or comments here:

```text
feedback/imports/
```
