# Safety Rules

Current version date: 2026-05-16

## Hard Prohibitions

1. Do not modify existing old chapters.
2. Do not modify existing old summaries.
3. Do not modify existing canon files during routine daily generation.
4. Do not delete files.
5. Do not move files.
6. Do not rename files.
7. Do not overwrite existing `chapters/第XXX章_全文.md`.
8. Do not overwrite existing `chapter_summaries/第XXX章_摘要.md`.
9. Do not use legacy unsafe publish scripts in unattended automation.
10. Do not publish externally unless `auto_publish_external: true` is configured, the user explicitly asks to publish the edited target file in the current turn, and `tools/fanqie_safe_publish.py --auto-submit` is used.
11. Do not run unattended external publishing during routine chapter generation while `auto_publish_external: false`.

## Allowed Creates

Daily automation may create:

1. Missing operational directories.
2. New target chapter files only if they do not already exist.
3. New target daily output artifacts.
4. New run logs.
5. New publish logs and screenshots under `daily_output/publish_logs/`.
6. New manual revision checklists for the current target chapter.

Daily automation may not edit older chapter artifacts except the current target artifacts it created in the current run.

## Pending-Chapter Guard

If latest formal chapter is `N`, and `daily_output` contains chapter `N+1` with QA saying publish is recommended, stop before generating `N+2`.

Reason:

1. The publish-ready chapter is not formal yet.
2. Generating the next chapter would break the archive chain.
3. Automation must archive `N+1` first if formal files do not already exist.

## CDP Guard

Before feedback query or publishing:

1. Run `tools/fanqie_python_preflight.ps1 -PersistUserPath` to verify `python` and Playwright are available.
2. Check `http://127.0.0.1:9222/json/version`.
3. If unavailable, run `tools/fanqie_start_cdp_chrome.ps1`.
4. If still unavailable, log failure and stop external work.
5. Do not assume the last browser tab is correct; safe tools must verify page identity.

## Browser Bridge Guard

`automation/browser_bridge.md` defines the optional Codex Chrome extension / `@chrome` workflow.

Use it only for:

1. Login/session checks.
2. Read-only page inspection.
3. Publish failure diagnosis.
4. Identifying changed Fanqie UI text or button order.

Do not use `@chrome` as the unattended external publishing mechanism. If the browser bridge reveals a repeatable UI change, patch `tools/fanqie_safe_publish.py` and keep JSON logs and screenshots under `daily_output/publish_logs/`.

## Fanqie Publish Guard

Routine automation currently stops before this guard because `feedback/source_config.md` sets `auto_publish_external: false`.

The publish guard applies only when the user explicitly requests publishing an edited file and config is re-enabled.

Use only:

```powershell
python tools\fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX --open-publish-page --create-chapter --auto-submit
```

The publisher must validate:

1. Publish file chapter number.
2. No blank body lines.
3. Fanqie page identity.
4. Chapter number field receives Arabic digits only.
5. Title field receives title only.
6. Body editor receives body only.
7. JSON log and screenshot are written.

## Run Lock

Before a daily run:

1. If `daily_output/.run_lock` exists, stop.
2. If no lock exists, create it during execution.
3. Remove it before finishing.
4. If execution fails, leave a run note in `daily_output/automation_runs/`.

## Git Protection

After a completed run with file changes:

1. Run `git status --short --branch`.
2. Stage only files relevant to the run.
3. Commit.
4. Push to GitHub after commit unless network is unavailable.

Never use `git reset --hard`.
