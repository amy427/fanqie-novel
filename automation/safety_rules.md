# Safety Rules

Current version date: 2026-05-06

## Hard Prohibitions

1. Do not modify existing old chapters.
2. Do not modify existing old summaries.
3. Do not modify existing canon files during daily generation.
4. Do not delete files.
5. Do not move files.
6. Do not rename files.
7. Do not overwrite existing `chapters/第XXX章_全文.md`.
8. Do not overwrite existing `chapter_summaries/第XXX章_摘要.md`.
9. Do not use legacy unsafe publish scripts in unattended automation.
10. Do not publish through external platforms unless `auto_publish_external: true` is configured and `tools/fanqie_safe_publish.py --auto-submit` is used.

## Allowed Creates

Daily automation may create:

1. Missing directories: `chapter_summaries/`, `daily_output/`, `daily_output/automation_runs/`.
2. New target chapter files only if they do not already exist.
3. New target daily output artifacts.
4. New run logs.
5. New publish logs and screenshots under `daily_output/publish_logs/`.

Daily automation may not edit older chapter artifacts except the target chapter artifacts it created in the current run.

## Pending-Chapter Guard

If latest formal chapter is `N`, and `daily_output` contains chapter `N+1` with QA saying `是否建议人工发布：是`, stop before generating `N+2`.

Reason:

1. The publish-ready chapter is not formal yet.
2. Generating the next chapter would break the archive chain.
3. Automation must archive `N+1` first if formal target files do not already exist.

## Run Lock

Before a daily run:

1. If `daily_output/.run_lock` exists, stop.
2. If no lock exists, create it during execution.
3. Remove it before finishing.
4. If execution fails, leave a run note in `daily_output/automation_runs/`.

## Git Protection

After a completed run with file changes:

1. Run `git status --short --branch`.
2. Stage only created files for this run.
3. Commit.
4. Push to GitHub after commit unless network is unavailable.

Suggested commit messages:

```text
Auto dry run chapter XXX
```

or, if quality gates failed:

```text
Save failed chapter XXX dry run
```
