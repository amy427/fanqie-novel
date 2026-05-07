# AGENTS.md

Guidance for AI agents working in `D:\fanqie-novel`.

## Project Identity

This is a Fanqie web novel production workspace for `高武：违规者才配活着`, a rule-horror, high-martial-arts, urban male-frequency serial.

The project is writing-first. Canon Markdown, formal chapters, summaries, continuity files, QA artifacts, and publish logs are more important than generic code structure.

## Read First

Before doing project work, read these files in order:

1. `PROJECT_OS.md`
2. `OPERATING_LOOP.md`
3. `automation/run_state.md`
4. `automation/safety_rules.md`
5. `automation/quality_gates.md`
6. `automation/daily_chapter_run.md`
7. Relevant continuity files under `continuity/`

Before drafting or revising a chapter, also read:

1. The latest 3 formal chapters in `chapters/`
2. Matching recent summaries in `chapter_summaries/`
3. The latest QA report and hook files in `daily_output/`
4. Core canon files `00_*.md` through `07_*.md`

## Source Of Truth

Core canon:

- `00_世界观设定.md`
- `01_主角能力表.md`
- `02_角色关系表.md`
- `03_伏笔回收表.md`
- `04_副本记录表.md`
- `05_战力等级表.md`
- `06_每卷主线目标.md`
- `07_长篇控制设定表_canvas.md`

Operational truth:

- Formal prose archive: `chapters/`
- Chapter summaries: `chapter_summaries/`
- Working outputs and QA artifacts: `daily_output/`
- Continuity state: `continuity/`
- Automation state: `automation/run_state.md`
- Decision history: `decision_log/DECISION_LOG.md`
- Reader feedback and metrics: `feedback/`
- Fanqie browser automation helpers: `tools/`

## Current State As Of 2026-05-08

- Latest formal chapter detected in `chapters/`: 第031章
- Latest formal summary detected in `chapter_summaries/`: 第031章
- Next routine chapter target: 第032章
- Story phase: volume 2, still resolving the late `旧河公寓` / `十三号线` pressure chain.
- External publish automation is enabled by `feedback/source_config.md` with `auto_publish_external: true`.
- Fanqie CDP must be available at `http://127.0.0.1:9222` before publish or feedback scripts run.

## Working Rules

- Preserve the user's existing creative direction. Do not normalize the story into generic fantasy, generic horror, or pure leveling fiction.
- Keep 江彻 active: rule conflict, tactical choice, cost, and consequence should drive the scene.
- Avoid free cheats. The second-column text is a costly hint layer, not a complete answer machine.
- Do not introduce major organizations, systems, cities, or power mechanics unless reflected in canon or explicitly requested.
- Keep chapter endings hook-heavy and operationally clear.
- When continuity needs updating, prefer existing canon/continuity tables over duplicate notes.

## File Hygiene

- Use UTF-8 for Chinese Markdown.
- Do not delete, move, rename, or overwrite existing old chapters, summaries, canon files, publish versions, QA reports, or drafts unless the user explicitly asks.
- New daily chapter runs may only create the current target chapter artifacts and supporting logs.
- When a chapter is accepted, make sure `chapters/`, `chapter_summaries/`, `daily_output/`, `continuity/`, `feedback/`, and `automation/run_state.md` agree on chapter number and title.
- Keep handoff notes dated with absolute dates.

## Fanqie Automation Caution

Use only the safe publisher for unattended publishing:

```powershell
python tools\fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX --open-publish-page --create-chapter --auto-submit
```

If CDP is unavailable, start Chrome with:

```powershell
powershell -ExecutionPolicy Bypass -File tools\fanqie_start_cdp_chrome.ps1
```

Fanqie editor field rule:

- The small field between `第` and `章` must receive Arabic digits only, for example `32`.
- The title field after `章` must receive the chapter title only, for example `地下钟室下层`.
- Do not fill `第032章 地下钟室下层` into the title field.

Publishing scripts must write JSON logs and screenshots under `daily_output/publish_logs/`.
