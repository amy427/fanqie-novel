# Browser Bridge

Current version date: 2026-05-08

## Purpose

Use browser control to make Fanqie login checks, page inspection, and publish-failure diagnosis faster without weakening the unattended publish guard.

This project has two browser paths:

1. CDP + Playwright safe tools: primary path for routine automation and unattended publishing.
2. Codex Chrome extension / `@chrome`: operator-assist path for inspecting the live logged-in browser, switching tabs, confirming page state, and diagnosing changed UI.

## Priority Order

1. For unattended external publish, always use:

```powershell
python tools\fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX --open-publish-page --create-chapter --auto-submit
```

2. If the safe publisher fails, inspect `daily_output/publish_logs/` first.
3. If a Fanqie confirmation dialog is already open, continue through the safe publisher:

```powershell
python tools\fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX --page-url-contains <publish-page-id> --continue-submit
```

4. Use `@chrome` only to inspect browser state, validate login/session, identify changed button text, or check whether Fanqie shows the chapter as draft, reviewing, or published.
5. If `@chrome` discovers a repeatable UI change, patch `tools\fanqie_safe_publish.py` instead of relying on manual visual clicking.

## Local Bridge Check

Run:

```powershell
powershell -ExecutionPolicy Bypass -File tools\fanqie_browser_bridge_check.ps1 -StartCdp
```

This checks:

1. `python` on PATH.
2. Chrome executable availability.
3. CDP at `http://127.0.0.1:9222`.
4. Open Fanqie CDP tabs.
5. Whether the Codex Chrome extension is installed in local Chrome profiles.

To open the Chrome Web Store page for the Codex extension:

```powershell
powershell -ExecutionPolicy Bypass -File tools\fanqie_browser_bridge_check.ps1 -OpenExtensionStore
```

Extension installation is interactive. Do not mark it complete unless Chrome shows the extension installed and Codex App exposes the `@chrome` target.

## Codex App Usage

When the extension is installed and Codex App exposes browser access, use a direct browser mention such as:

```text
@chrome 检查番茄作者后台里第032章的审核状态，只读观察，不点击发布。
```

For publish troubleshooting:

```text
@chrome 查看当前番茄发布页停在哪个弹窗或按钮，记录按钮文案，不直接提交。
```

## Safety Boundary

The extension path is not a replacement for `tools\fanqie_safe_publish.py`.

Unattended publishing must remain auditable through JSON logs and screenshots under:

```text
daily_output/publish_logs/
```

Direct browser clicking through `@chrome` is allowed for read-only inspection and explicit human-directed troubleshooting only. Routine automation must keep using the safe publisher.
