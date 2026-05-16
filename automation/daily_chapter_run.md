# Daily Chapter Run

Current version date: 2026-05-16

## Purpose

Generate and process exactly one active target, then archive/package it and prepare it for manual revision. Routine automation must stop before external publish.

Read together with:

1. `PROJECT_OS.md`
2. `OPERATING_LOOP.md`
3. `automation/safety_rules.md`
4. `automation/chapter_generation_spec.md`
5. `automation/quality_gates.md`
6. `automation/run_state.md`
7. `automation/auto_decision_policy.md`
8. `automation/feedback_query.md`
9. `automation/browser_bridge.md`
10. `continuity/open_threads.md`
11. `continuity/object_state.md`
12. `continuity/character_state.md`
13. `continuity/rules_state.md`

## Execution Order

1. Confirm working directory is `D:\fanqie-novel`.
2. Confirm required operational directories exist; create missing directories only.
3. Check `daily_output/.run_lock`; if present, stop and write a run note.
4. Scan `chapters/`, `chapter_summaries/`, and `daily_output/`.
5. Read `PROJECT_OS.md` and `automation/run_state.md` to determine the active project.
6. If the old book is stopped/archive status, do not target old-book 第037章 unless the user explicitly reactivates that serial.
7. If new-book setup is active and required new-book files are incomplete, create or update only the missing new-book setup artifacts.
8. When external publishing is enabled and explicitly requested, verify the Fanqie author backend with `python tools\fanqie_verify_publish_state.py` and treat the latest externally published chapter as the publish target anchor.
9. Determine latest formal chapter by `chapters/第XXX章_全文.md` only for local continuity and drafting support.
10. If Fanqie latest is behind local formal archive and manual publishing was explicitly requested, publish the next external chapter first; do not skip ahead just because later local chapters exist.
11. If a publish-ready pending chapter newer than latest formal exists, archive it first if safe.
12. Otherwise target latest active serial formal chapter + 1 for local generation.
13. Stop if target formal chapter or summary already exists and the task is local drafting; for explicit external catch-up, use existing local publish artifacts.
14. Read canon, recent chapters, summaries, feedback, and continuity.
15. Generate target chapter into `daily_output/` first when local drafting is needed.
16. Run quality gates.
17. If needed, rewrite once and re-run quality gates.
18. If pass, write formal chapter and formal summary.
19. If fail, do not archive; keep draft, QA, and dry-run log.
20. Generate required daily output artifacts.
21. Update continuity, decision log, feedback notes, run index, and run state.
22. Run feedback query if a verified analytics/comments CDP page is open.
23. If `auto_publish_external: false`, do not open the Fanqie publish flow and do not run the safe publisher.
24. Generate the manual revision checklist and mark the publish file as waiting for user edits.
25. If `auto_publish_external: true` and the user explicitly requested publishing in the current turn, run the safe publisher for the next external chapter.
26. Re-check Fanqie chapter management only after an explicitly requested publish.
27. Write dry-run log.
28. Commit local changes.
29. Push to GitHub after commit unless unavailable.

## Manual Revision Gate

Routine runs stop here:

```text
QA passed -> formal archive -> Fanqie publish version generated -> manual revision checklist generated -> no external publish
```

Reason:

The previous book lost traffic after insufficient human revision and was likely treated as AI filler. The user must revise prose before any external submission.

Automation must create:

```text
daily_output\第XXX章_人工改稿清单.md
```

The checklist should focus on:

1. Rewriting generic transitions into author-specific phrasing.
2. Adding concrete sensory and action details.
3. Cutting repetitive rule-explanation rhythm.
4. Varying paragraph cadence and dialogue beats.
5. Ensuring the opening and ending sound hand-edited.
6. Flagging lines likely to read as AI filler.

## Manual External Publish Step

Run this only when the user explicitly asks to publish an edited file and `auto_publish_external: true` is restored.

Before publishing, ensure CDP is available:

```powershell
powershell -ExecutionPolicy Bypass -File tools\fanqie_python_preflight.ps1 -PersistUserPath
powershell -ExecutionPolicy Bypass -File tools\fanqie_start_cdp_chrome.ps1
```

Publish command:

```powershell
python tools\fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX --open-publish-page --create-chapter --auto-submit
```

If CDP is unavailable, login has expired, the page cannot be verified, or publisher validation fails, record the failure in `daily_output/publish_logs/` and continue the local archive/commit flow. Do not retry indefinitely.

## Browser-Control Escalation

Use `automation/browser_bridge.md` when a publish or feedback query failure needs live browser inspection.

Allowed escalation:

1. Run `tools\fanqie_browser_bridge_check.ps1 -StartCdp` to verify CDP, Chrome, and extension state.
2. Use Codex Chrome / `@chrome` for read-only inspection of login state, current tab, visible dialog text, and chapter status.
3. If a submit confirmation is already open, continue through `tools\fanqie_safe_publish.py --continue-submit`.
4. If `@chrome` reveals a repeatable Fanqie UI change, patch the safe publisher before the next unattended run.

Do not use browser-control visual clicking as the routine unattended publish mechanism.

## Required Daily Output Files

For target `第XXX章`, create:

1. `daily_output/第XXX章_质检报告.md`
2. `daily_output/第XXX章_伏笔更新建议.md`
3. `daily_output/第YYY章_剧情钩子.md`, where `YYY = XXX + 1`
4. `daily_output/第XXX章_干跑日志.md`
5. `daily_output/第XXX章_番茄发布版.txt`
6. `daily_output/第XXX章_发布检查清单.md`
7. `daily_output/第XXX章_人工改稿清单.md`

Optional if passed:

1. `daily_output/第XXX章_完整正文_备份.md`

Formal outputs only if passed:

1. `chapters/第XXX章_全文.md`
2. `chapter_summaries/第XXX章_摘要.md`

## Final Automation Reply

Do not paste the full chapter.

Report only:

1. Latest formal chapter number.
2. Target chapter number.
3. Whether formal chapter was written.
4. Whether formal summary was written.
5. Generated daily output files.
6. Missing files, if any.
7. Whether automatic rewrite was triggered.
8. Whether local dry run completed.
9. Whether Fanqie publish was attempted. In routine runs this should be `not attempted; stopped at manual revision gate`.
