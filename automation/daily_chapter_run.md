# Daily Chapter Run

Current version date: 2026-05-08

## Purpose

Generate and process exactly one next chapter after the latest formal chapter, then archive and publish it only if it passes quality gates.

Read together with:

1. `PROJECT_OS.md`
2. `OPERATING_LOOP.md`
3. `automation/safety_rules.md`
4. `automation/chapter_generation_spec.md`
5. `automation/quality_gates.md`
6. `automation/run_state.md`
7. `automation/auto_decision_policy.md`
8. `automation/feedback_query.md`
9. `continuity/open_threads.md`
10. `continuity/object_state.md`
11. `continuity/character_state.md`
12. `continuity/rules_state.md`

## Execution Order

1. Confirm working directory is `D:\fanqie-novel`.
2. Confirm required operational directories exist; create missing directories only.
3. Check `daily_output/.run_lock`; if present, stop and write a run note.
4. Scan `chapters/`, `chapter_summaries/`, and `daily_output/`.
5. Determine latest formal chapter by `chapters/第XXX章_全文.md`.
6. If a publish-ready pending chapter newer than latest formal exists, archive it first if safe.
7. Otherwise target latest formal chapter + 1.
8. Stop if target formal chapter or summary already exists.
9. Read canon, recent chapters, summaries, feedback, and continuity.
10. Generate target chapter into `daily_output/` first.
11. Run quality gates.
12. If needed, rewrite once and re-run quality gates.
13. If pass, write formal chapter and formal summary.
14. If fail, do not archive; keep draft, QA, and dry-run log.
15. Generate required daily output artifacts.
16. Update continuity, decision log, feedback notes, run index, and run state.
17. Run feedback query if a verified analytics/comments CDP page is open.
18. If `auto_publish_external: true`, run the safe publisher.
19. Write dry-run log.
20. Commit local changes.
21. Push to GitHub after commit unless unavailable.

## Automatic External Publish Step

Before publishing, ensure CDP is available:

```powershell
powershell -ExecutionPolicy Bypass -File tools\fanqie_start_cdp_chrome.ps1
```

Publish command:

```powershell
python tools\fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX --open-publish-page --create-chapter --auto-submit
```

If CDP is unavailable, login has expired, the page cannot be verified, or publisher validation fails, record the failure in `daily_output/publish_logs/` and continue the local archive/commit flow. Do not retry indefinitely.

## Required Daily Output Files

For target `第XXX章`, create:

1. `daily_output/第XXX章_质检报告.md`
2. `daily_output/第XXX章_伏笔更新建议.md`
3. `daily_output/第YYY章_剧情钩子.md`, where `YYY = XXX + 1`
4. `daily_output/第XXX章_干跑日志.md`
5. `daily_output/第XXX章_番茄发布版.txt`
6. `daily_output/第XXX章_发布检查清单.md`

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
9. Whether Fanqie publish was attempted and its result.
