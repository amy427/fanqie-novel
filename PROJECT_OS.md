# PROJECT_OS

Current version date: 2026-05-16

## 1. Project Type

`D:\fanqie-novel` is a writing-first production system for Fanqie web-novel production.

The previous serial `高武：违规者才配活着` is now treated as a stopped/archive project. New book incubation lives under `new_book/`.

The project should behave like a small publishing operation:

1. Maintain canon and continuity.
2. Generate the next chapter only.
3. QA the chapter against fixed gates.
4. Archive passed output.
5. Prepare the Fanqie version for human revision.
6. Track feedback and improve the next run.
7. Commit and push reproducible state.

## 2. Current State

- Old-book latest formal chapter in `chapters/`: 第036章.
- Old-book latest formal summary in `chapter_summaries/`: 第036章.
- Old-book latest verified Fanqie chapter: 第035章.
- Old-book status: stopped/archive, no routine continuation unless explicitly requested.
- New-book status: incubation under `new_book/`.
- External publishing: disabled by `feedback/source_config.md`.
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
7. Stop at the manual revision gate before external publish.
8. Commit and push completed operational changes.

## 6. Human Gates

Routine confirmation is disabled for local chapter production only.

External publishing is not routine. The user must revise the generated publish version and explicitly request publishing later.

The system must still stop and report if:

1. Target formal chapter already exists.
2. Target summary already exists.
3. QA fails after one rewrite.
4. Git push fails.

## 7. Quality Definition

A chapter is locally package-ready only if:

1. It targets exactly the active serial's latest formal chapter + 1.
2. It has 4000 to 5000 non-whitespace body characters.
3. It has no blank lines in formal prose or Fanqie publish text.
4. It opens with conflict.
5. It has middle pressure escalation.
6. 江彻 makes active tactical decisions.
7. The payoff comes from rule handling, not a free power jump.
8. A visible cost is paid.
9. It ends with a concrete hook.
10. QA says the local publish package is recommended.

This does not authorize external Fanqie publication. External submission still requires the user's edited text and explicit later request.

## 8. Fanqie Publish Rule

Routine automation must not publish while:

```text
auto_publish_external: false
```

CDP endpoint for later manual publish or diagnostics:

```text
http://127.0.0.1:9222
```

Start CDP Chrome if needed:

```powershell
powershell -ExecutionPolicy Bypass -File tools\fanqie_start_cdp_chrome.ps1
```

Manual publish command, only after user-edited text and explicit request:

```powershell
python tools\fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX --open-publish-page --create-chapter --auto-submit
```

Fanqie editor field split:

- `第 __ 章`: Arabic digits only.
- Title field after `章`: chapter title only.

## 9. Next Best Action

For new-book incubation:

```text
创建新书生产系统。先确定题材、卖点、开篇钩子和反AI水文改稿规则。自动化只到发布前人工改稿闸门。
```
