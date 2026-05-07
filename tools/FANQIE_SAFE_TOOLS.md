# Fanqie Safe Tools

Current version date: 2026-05-08

## 1. CDP Startup

All Fanqie browser tools require Chromium CDP at:

```text
http://127.0.0.1:9222
```

Start or verify the CDP Chrome session:

```powershell
powershell -ExecutionPolicy Bypass -File tools\fanqie_start_cdp_chrome.ps1
```

This uses the local profile:

```text
D:\fanqie-novel\.pw-fanqie-profile
```

If login is expired, the script can open the page, but publishing must stop until the session is valid.

## 2. Read-Only Metrics

```powershell
python tools\fanqie_readonly_metrics.py
```

Behavior:

1. Connects to Chromium CDP.
2. Reads the last open page only.
3. Verifies that it looks like a Fanqie analytics or comments page.
4. Saves page text and candidate metrics to `feedback/imports/`.
5. Appends result to `feedback/query_log.md`.
6. Does not click or edit anything.

If the page is not verified, it exits without saving page content unless `--allow-unverified` is passed.

## 3. Safe Publish

Dry-run validation:

```powershell
python tools\fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX
```

Fill but do not submit:

```powershell
python tools\fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX --fill
```

Manual submit requires explicit SHA confirmation:

```powershell
python tools\fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX --fill --submit --confirm-submit <SHA256>
```

Unattended automatic publish:

```powershell
python tools\fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX --open-publish-page --create-chapter --auto-submit
```

Automatic publishing works only when `feedback/source_config.md` contains:

```text
auto_publish_external: true
```

## 4. Fanqie Editor Field Rule

Do not paste the full line `第XXX章 标题` into the title field.

Correct split:

1. The field between `第` and `章`: Arabic digits only, for example `32`.
2. The title field after `章`: title only, for example `地下钟室下层`.
3. The body editor: body only, without the chapter title line.

The safe publisher validates:

1. Chapter number.
2. Title field.
3. Body text.
4. No blank lines in the publish file.
5. Fanqie page identity.

Logs and screenshots are written to:

```text
daily_output/publish_logs/
```
