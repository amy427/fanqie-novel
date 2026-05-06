# Auto Decision Policy

Current version date: 2026-05-06

## Purpose

Remove routine human confirmation from the local production pipeline.

This file does not authorize unsafe browser actions by itself. It authorizes Codex to make local project decisions when the relevant quality gates are satisfied.

## Default Policy

Codex may automatically:

1. Select the publish title from market/title analysis.
2. Generate the target chapter.
3. Rewrite once if quality gates require it.
4. Archive a passed chapter to `chapters/`.
5. Generate the formal summary in `chapter_summaries/`.
6. Generate the next chapter hook.
7. Update continuity tracking files.
8. Update decision logs.
9. Update feedback and metrics files from configured read-only sources.
10. Commit and push repository changes when the run completes.

## Automatic Title Selection

When multiple titles exist, choose by this order:

1. Clear concrete image.
2. Strong immediate conflict.
3. No major spoiler for the final hook.
4. Short enough for chapter list scanning.
5. Matches recent chapter title style.

Record the reason in:

```text
decision_log/DECISION_LOG.md
feedback/title_performance.md
```

## Automatic Archive

If QA says `是否建议人工发布：是`, and formal target files do not already exist, Codex may write:

1. `chapters/第XXX章_全文.md`
2. `chapter_summaries/第XXX章_摘要.md`

No separate human confirmation is required.

## Automatic Next-Chapter Progression

If latest formal chapter is `N`, and there is no pending failed QA for `N+1`, automation may target `N+1`.

If `N+1` already has a passed QA in `daily_output`, automation must archive it first before generating `N+2`.

## External Platform Boundary

Codex may query configured external sources in read-only mode.

Codex must not publish to Fanqie or any external platform unless a dedicated safe publisher is configured and the automation prompt explicitly says `auto_publish_external: true`.

Current status:

```text
auto_publish_external: false
```

Reason:

The existing `tools/` scripts operate on the last open Chromium page over CDP. This is acceptable for supervised publishing, but not yet safe enough for unattended external publishing.

## Safe Publisher Tool

The supervised safe publisher is:

```powershell
python tools/fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX
```

Default mode is dry-run. It validates the file, chapter number, page identity, content hash, and writes screenshots/logs.

To fill but not submit:

```powershell
python tools/fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX --fill
```

To submit, the caller must provide the exact printed SHA256:

```powershell
python tools/fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX --fill --submit --confirm-submit <SHA256>
```

Unattended automation must not pass `--submit` unless `auto_publish_external: true` is explicitly configured in `feedback/source_config.md`.
