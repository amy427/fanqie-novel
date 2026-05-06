# Fanqie Safe Tools

Current version date: 2026-05-06

## Read-Only Metrics

```powershell
python tools/fanqie_readonly_metrics.py
```

Behavior:

1. Connects to Chromium CDP at `http://127.0.0.1:9222`.
2. Reads the last open page only.
3. Verifies that it looks like a Fanqie analytics or comments page.
4. Saves page text and candidate metrics to `feedback/imports/`.
5. Appends result to `feedback/query_log.md`.
6. Does not click or edit anything.

If the page is not verified, it exits without saving page content unless `--allow-unverified` is passed.

## Safe Publish

Dry-run validation:

```powershell
python tools/fanqie_safe_publish.py --file daily_output\第029章_番茄发布版.txt --expected-chapter 29
```

Fill but do not submit:

```powershell
python tools/fanqie_safe_publish.py --file daily_output\第029章_番茄发布版.txt --expected-chapter 29 --fill
```

Submit requires explicit SHA confirmation:

```powershell
python tools/fanqie_safe_publish.py --file daily_output\第029章_番茄发布版.txt --expected-chapter 29 --fill --submit --confirm-submit <SHA256>
```

Logs and screenshots are written to:

```text
daily_output/publish_logs/
```

Default automation must not use `--submit`.
