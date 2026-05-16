# Feedback Source Config

Current version date: 2026-05-16

## Enabled Sources

| Source | Status | Mode | Notes |
| --- | --- | --- | --- |
| Local files | enabled | read-only | Always available |
| Feedback imports | enabled | read-only | Put exports in `feedback/imports/` |
| Fanqie browser analytics | optional | read-only CDP | Requires verified Fanqie analytics/comments page |
| GitHub repository | enabled | read-only network | Useful for repository state, not reader data |

## External Publishing

```text
auto_publish_external: false
```

This config disables unattended Fanqie publishing.

Reason:

The previous book lost traffic after insufficient human revision and was likely treated as AI filler. Future automation must stop before external publish so the user can manually revise voice, rhythm, scene texture, and anti-AI traces.

Manual publishing remains allowed only after the user explicitly requests it for a specific edited publish file.

If manual publishing is later requested, use only:

```powershell
python tools\fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX --open-publish-page --create-chapter --auto-submit
```

Automation must not run that command during routine chapter production while `auto_publish_external: false`.

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
