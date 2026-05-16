# Fanqie Safe Tools

Current version date: 2026-05-16

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

## 2. Browser Bridge Check

Use this before escalating to Codex Chrome / `@chrome`:

```powershell
powershell -ExecutionPolicy Bypass -File tools\fanqie_browser_bridge_check.ps1 -StartCdp
```

It verifies local `python`, Chrome, CDP, Fanqie CDP tabs, and whether the Codex Chrome extension is installed in known Chrome profiles.

`-OpenExtensionStore` opens the OpenAI Chrome Web Store publisher page, not only the direct extension detail URL. Some accounts or regions may see `This item is not available` on the direct detail URL even when the OpenAI publisher page remains reachable.

The bridge is for login checks, page inspection, and failure diagnosis. It is not the unattended publish path.

## 3. Read-Only Metrics

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

## 4. Safe Publish

Routine automation must not publish externally while `feedback/source_config.md` contains:

```text
auto_publish_external: false
```

The current workflow stops at the manual revision gate so the user can edit the publish file before any platform submission.

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

Manual publish after user edits and explicitly requests submission:

```powershell
python tools\fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX --open-publish-page --create-chapter --auto-submit
```

Publishing works only when `feedback/source_config.md` contains:

```text
auto_publish_external: true
```

Continue an already-started explicit manual confirmation flow:

```powershell
python tools\fanqie_safe_publish.py --file daily_output\绗琗XX绔燺鐣寗鍙戝竷鐗?txt --expected-chapter XXX --page-url-contains <publish-page-id> --continue-submit
```

## 5. Fanqie Editor Field Rule

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
