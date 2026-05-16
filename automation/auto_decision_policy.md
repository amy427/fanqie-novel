# Auto Decision Policy

Current version date: 2026-05-16

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

Codex may not automatically publish externally in routine runs. It must stop at the manual revision gate.

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

Codex must not publish to Fanqie or any external platform unless all are true:

1. A dedicated safe publisher is configured.
2. `feedback/source_config.md` contains `auto_publish_external: true`.
3. The user explicitly requests publishing for the edited target file in the current turn.

Current status:

```text
auto_publish_external: false
```

Reason:

The previous book lost traffic after insufficient human revision and was likely treated as AI filler. Routine automation must generate local artifacts only and stop before external publishing so the user can revise.

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

To submit manually, the caller may still provide the exact printed SHA256:

```powershell
python tools/fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX --fill --submit --confirm-submit <SHA256>
```

Unattended automation must not publish while `auto_publish_external: false`.

If the user later explicitly enables publishing and requests a specific chapter submission, the guarded command is:

```powershell
python tools/fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX --open-publish-page --create-chapter --auto-submit
```

This still requires `auto_publish_external: true` in `feedback/source_config.md` at execution time.

## Manual Revision Gate

After QA passes, automation must:

1. Generate `daily_output\第XXX章_番茄发布版.txt`.
2. Generate `daily_output\第XXX章_发布检查清单.md`.
3. Generate `daily_output\第XXX章_人工改稿清单.md`.
4. Mark the chapter as `待人工改稿`.
5. Stop before browser publish, fill, submit, or external upload.

The user edits the publish version manually. Automation may later QA or package the edited file if asked.
