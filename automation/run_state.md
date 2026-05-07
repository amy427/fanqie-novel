# Run State

Last updated: 2026-05-08

## Current Formal State

- Latest formal chapter detected in `chapters/`: 第031章
- Latest formal summary detected in `chapter_summaries/`: 第031章
- Current publish-ready daily output beyond formal archive: none detected
- Next routine chapter target: 第032章

## Current Automation State

- Local dry-run generation: enabled
- Formal archive after QA pass: enabled
- Git commit and push after completed runs: enabled
- Feedback query: enabled when CDP page is verified as Fanqie analytics/comments
- External Fanqie publishing: enabled by `feedback/source_config.md`
- CDP endpoint: `http://127.0.0.1:9222`

## Current Publish Guard

Use:

```powershell
powershell -ExecutionPolicy Bypass -File tools\fanqie_start_cdp_chrome.ps1
python tools\fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX --open-publish-page --create-chapter --auto-submit
```

Fanqie field split:

- Chapter number field: Arabic digits only, for example `32`.
- Chapter title field: title only, for example `地下钟室下层`.

## Next Human Gate

Routine human confirmation gates remain disabled because the user requested unattended automation.

Stop only if:

1. Target files already exist.
2. QA fails after one rewrite.
3. CDP cannot start or connect.
4. Fanqie login/session is invalid.
5. Fanqie page cannot be verified.
6. Safe publisher cannot verify filled content.
7. Git push fails.

## Recommended Next Step

```text
运行小说生产流程。目标：推进第032章。按 PROJECT_OS 和 OPERATING_LOOP 执行。
```
