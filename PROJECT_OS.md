# PROJECT_OS

Current version date: 2026-05-08

## 1. Project Type

`D:\fanqie-novel` is a writing-first production system for the Fanqie serial `高武：违规者才配活着`.

The project should behave like a small publishing operation:

1. Maintain canon and continuity.
2. Generate the next chapter only.
3. QA the chapter against fixed gates.
4. Archive passed output.
5. Prepare and publish the Fanqie version when authorized.
6. Track feedback and improve the next run.
7. Commit and push reproducible state.

## 2. Current State

- Latest formal chapter in `chapters/`: 第031章.
- Latest formal summary in `chapter_summaries/`: 第031章.
- Next routine target: 第032章.
- External publishing: enabled by `feedback/source_config.md`.
- Git branch: `main`.
- GitHub remote: `https://github.com/amy427/fanqie-novel.git`.

## 3. Source Of Truth

Canon source:

- `00_世界观设定.md`
- `01_主角能力表.md`
- `02_角色关系表.md`
- `03_伏笔回收表.md`
- `04_副本记录表.md`
- `05_战力等级表.md`
- `06_每卷主线目标.md`
- `07_长篇控制设定表_canvas.md`

Production source:

- `chapters/`
- `chapter_summaries/`
- `continuity/`
- `automation/run_state.md`
- `decision_log/DECISION_LOG.md`
- `feedback/`

Process outputs:

- `daily_output/`
- `daily_output/publish_logs/`
- `daily_output/automation_runs/`
- `weekly_review/`

## 4. Forbidden Actions

Do not delete, move, rename, or overwrite:

1. Existing formal chapters.
2. Existing formal summaries.
3. Existing canon files.
4. Existing publish versions.
5. Existing QA reports.
6. Existing drafts.
7. Existing publish logs.
8. Browser profile data.

Exceptions require explicit user instruction.

## 5. Automatic Actions

The system may automatically:

1. Create missing operational directories.
2. Create artifacts for the current target chapter.
3. Run QA and one automatic rewrite.
4. Archive a passed target chapter if formal files do not already exist.
5. Update continuity and run-state files.
6. Query Fanqie metrics when a verified analytics/comments page is open.
7. Publish when `auto_publish_external: true` and the safe publisher passes validation.
8. Commit and push completed operational changes.

## 6. Human Gates

Routine confirmation is disabled for local chapter production and external publishing because the user explicitly requested unattended automation.

The system must still stop and report if:

1. Target formal chapter already exists.
2. Target summary already exists.
3. QA fails after one rewrite.
4. CDP cannot be reached.
5. Fanqie page cannot be verified.
6. Login/session is invalid.
7. Publish script cannot verify filled chapter number, title, or body.
8. Git push fails.

## 7. Quality Definition

A chapter is publishable only if:

1. It targets exactly latest formal chapter + 1.
2. It has 4000 to 5000 non-whitespace body characters.
3. It has no blank lines in formal prose or Fanqie publish text.
4. It opens with conflict.
5. It has middle pressure escalation.
6. 江彻 makes active tactical decisions.
7. The payoff comes from rule handling, not a free power jump.
8. A visible cost is paid.
9. It ends with a concrete hook.
10. QA says publish is recommended.

## 8. Fanqie Publish Rule

CDP endpoint:

```text
http://127.0.0.1:9222
```

Start CDP Chrome if needed:

```powershell
powershell -ExecutionPolicy Bypass -File tools\fanqie_start_cdp_chrome.ps1
```

Safe publish command:

```powershell
python tools\fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX --open-publish-page --create-chapter --auto-submit
```

Fanqie editor field split:

- `第 __ 章`: Arabic digits only.
- Title field after `章`: chapter title only.

## 9. Next Best Action

For routine continuation:

```text
运行小说生产流程。目标：推进第032章。按 PROJECT_OS 和 OPERATING_LOOP 执行。
```
