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
9. Do not open browser.
10. Do not access Fanqie backend.
11. Do not publish.
12. Do not upload.

## Allowed Creates

Daily automation may create:

1. Missing directories: `chapter_summaries/`, `daily_output/`, `daily_output/automation_runs/`.
2. New target chapter files only if they do not already exist.
3. New target daily output artifacts.
4. New run logs.

Daily automation may not edit older chapter artifacts except the target chapter artifacts it created in the current run.

## Pending-Chapter Guard

If latest formal chapter is `N`, and `daily_output` contains chapter `N+1` with QA saying `是否建议人工发布：是`, stop before generating `N+2`.

Reason:

1. The publish-ready chapter is not formal yet.
2. Generating the next chapter would break the archive chain.
3. Human or post-publish archival workflow must resolve it first.

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
4. Do not push to GitHub during the dry run unless the user explicitly enables network upload.

Suggested commit messages:

```text
Auto dry run chapter XXX
```

or, if quality gates failed:

```text
Save failed chapter XXX dry run
```
