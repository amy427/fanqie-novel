# Automation

This folder turns the long daily-generation prompt into a maintainable local operating system.

## Core Rules

1. `chapters/` is the only source for completed formal chapters.
2. `daily_output/` may contain publish-ready work, but it is not formal until archived.
3. Daily automation must pass safety checks before writing any formal chapter or summary.
4. Failed runs stay in `daily_output/` and must not touch `chapters/` or `chapter_summaries/`.
5. Existing old chapters, summaries, canon files, QA reports, publish versions, and drafts are never overwritten.
6. Routine external publishing is disabled; manual publishing is allowed only through `tools/fanqie_safe_publish.py` after explicit user request.

## Files

- `daily_chapter_run.md`: daily automation task.
- `chapter_generation_spec.md`: chapter generation and output rules.
- `quality_gates.md`: pass/fail checks before formal archival.
- `safety_rules.md`: filesystem, CDP, publish, and Git protections.
- `run_state.md`: current automation state snapshot.
- `run_index.md`: historical run index.
- `feedback_query.md`: feedback query rules.
- `auto_decision_policy.md`: unattended decision policy.
- `manual_revision_gate.md`: stop-before-publish workflow for user edits.

## Current Entry

Routine continuation now targets new-book setup and manual revision workflow:

```text
运行小说生产流程。按 PROJECT_OS 和 OPERATING_LOOP 执行；旧书不继续外发，生成内容停在人工改稿闸门。
```

CDP startup:

```powershell
powershell -ExecutionPolicy Bypass -File tools\fanqie_start_cdp_chrome.ps1
```
