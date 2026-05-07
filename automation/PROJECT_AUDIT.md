# PROJECT_AUDIT

Audit date: 2026-05-08

## 1. Project Type

Long-form Fanqie web novel production workspace.

## 2. Core Goal

Build and run a sustainable production loop for `高武：违规者才配活着`:

1. Generate the next chapter.
2. QA it.
3. Archive it.
4. Prepare and publish the Fanqie version.
5. Track feedback.
6. Update continuity and run state.
7. Commit and push traceable changes.

## 3. Current Progress

- Latest formal chapter: 第031章
- Latest formal summary: 第031章
- Next routine target: 第032章
- External publishing: enabled
- CDP endpoint: `http://127.0.0.1:9222`

## 4. Source-Of-Truth Files

Canon:

- `00_世界观设定.md`
- `01_主角能力表.md`
- `02_角色关系表.md`
- `03_伏笔回收表.md`
- `04_副本记录表.md`
- `05_战力等级表.md`
- `06_每卷主线目标.md`
- `07_长篇控制设定表_canvas.md`

Operational:

- `PROJECT_OS.md`
- `AGENTS.md`
- `OPERATING_LOOP.md`
- `automation/run_state.md`
- `automation/safety_rules.md`
- `automation/quality_gates.md`
- `automation/daily_chapter_run.md`
- `continuity/`
- `feedback/`
- `decision_log/DECISION_LOG.md`

## 5. Process Outputs

- `daily_output/`
- `daily_output/publish_logs/`
- `daily_output/automation_runs/`
- `weekly_review/`

## 6. Forbidden-To-Overwrite Areas

Do not overwrite existing files in:

- `chapters/`
- `chapter_summaries/`
- core canon files `00_*.md` through `07_*.md`
- older `daily_output/` chapter artifacts
- `daily_output/publish_logs/`

## 7. Automation Entry Points

Daily run:

```text
运行小说生产流程。目标：推进第032章。按 PROJECT_OS 和 OPERATING_LOOP 执行。
```

CDP start:

```powershell
powershell -ExecutionPolicy Bypass -File tools\fanqie_start_cdp_chrome.ps1
```

Safe publish:

```powershell
python tools\fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX --open-publish-page --create-chapter --auto-submit
```

## 8. Risks Found And Fixed

1. Some project-entry docs were outdated or encoding-damaged.
   - Fixed by rewriting `AGENTS.md`, `README.md`, `PROJECT_OS.md`, `OPERATING_LOOP.md`, and automation docs.
2. CDP config drift existed between docs/startup script and Python common config.
   - Fixed by aligning `tools/fanqie_common.py` to `http://127.0.0.1:9222`.
3. Fanqie chapter editor requires split fields.
   - Fixed by rewriting `tools/fanqie_safe_publish.py` to fill Arabic chapter number and title separately.
4. CDP startup was manual and fragile.
   - Fixed by adding `tools/fanqie_start_cdp_chrome.ps1`.

## 9. Validation Performed

1. `python -m py_compile tools\fanqie_common.py tools\fanqie_safe_publish.py`
2. `powershell -ExecutionPolicy Bypass -File tools\fanqie_start_cdp_chrome.ps1`
3. `git diff --check`
4. Safe publisher dry-run on `daily_output\第031章_番茄发布版.txt`

Dry-run result:

- Mode: dry-run
- Title: 第031章 下层敲门
- Chapter title field: 下层敲门
- JSON log: `daily_output/publish_logs/2026-05-08_003059_chapter_031_safe_publish.json`

## 10. Remaining Gaps

1. Some older non-entry documents may still contain historical encoding damage.
2. Fanqie actual publish success should still be judged from safe-publisher JSON plus platform state after each publish.
3. Reader metrics remain dependent on a verified analytics/comments page being open over CDP.

## 11. Next Best Action

Run the next chapter production loop for 第032章.
