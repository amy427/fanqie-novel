# Daily Chapter Run

Current version date: 2026-05-06

## Purpose

Run a local dry run that generates the next chapter after the latest formal chapter, then archives it only if it passes quality gates.

This is a daily automation instruction file. It should be read together with:

1. `automation/safety_rules.md`
2. `automation/chapter_generation_spec.md`
3. `automation/quality_gates.md`
4. `automation/run_state.md`
5. `automation/auto_decision_policy.md`
6. `automation/feedback_query.md`
7. `NOVEL_OS.md`
8. `OPERATING_LOOP.md`
9. `continuity/open_threads.md`
10. `continuity/object_state.md`
11. `continuity/character_state.md`
12. `continuity/rules_state.md`

## Execution Order

1. Confirm working directory is `D:\fanqie-novel`.
2. Confirm `chapter_summaries/`, `daily_output/`, and `daily_output/automation_runs/` exist; create missing directories only.
3. Check for `daily_output/.run_lock`; if present, stop and write only a short automation run note in `daily_output/automation_runs/`.
4. Scan `chapters/`, `chapter_summaries/`, and `daily_output/`.
5. Run feedback query according to `automation/feedback_query.md`; if unavailable, log and continue.
6. Determine the latest formal chapter by `chapters/第XXX章_全文.md`.
7. Check whether any `daily_output/第YYY章_质检报告.md` for a chapter newer than the latest formal chapter says `是否建议人工发布：是`.
8. If such a newer publish-ready chapter exists, archive it automatically before generating later chapters, as long as target formal files do not already exist.
9. If no pending publish-ready chapter exists, target chapter is latest formal chapter number + 1.
10. If target formal chapter or target summary already exists, stop. Do not overwrite.
11. Read required canon, summaries, recent chapters, feedback, and continuity files according to `chapter_generation_spec.md`.
12. Generate target chapter into daily output first.
13. Run quality gates.
14. If pass, write formal chapter and formal summary automatically.
15. If fail, keep only daily output draft, QA report, and dry-run log.
16. Generate required `daily_output` artifacts.
17. Update `continuity/`, `decision_log/`, `feedback/`, `automation/run_index.md`, and `automation/run_state.md`.
18. If `feedback/source_config.md` contains `auto_publish_external: true`, publish the passed chapter through the safe publisher.
19. Write dry-run log.
20. Commit changes locally when files were created.
21. Push to GitHub after commit unless network is unavailable.

## Automatic External Publish Step

Only run after the target chapter has passed QA and the target publish file exists.

Command format:

```powershell
python tools/fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX --open-publish-page --create-chapter --auto-submit
```

If CDP is unavailable, login has expired, the page cannot be verified, or the publisher fails validation, record the failure in `daily_output/publish_logs/` and continue the local archive/commit flow. Do not retry in a loop.

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
