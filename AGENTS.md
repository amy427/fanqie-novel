# AGENTS.md

Guidance for AI agents working in `D:\fanqie-novel`.

## Project Identity

This is a Fanqie web novel production workspace for `高武：违规者才配活着`, a rule-horror, high-martial-arts, urban male-frequency serial.

The project is writing-first. The Markdown canon and chapter files are more important than code structure.

## Source Of Truth

- Core canon:
  - `00_世界观设定.md`
  - `01_主角能力表.md`
  - `02_角色关系表.md`
  - `03_伏笔回收表.md`
  - `04_副本记录表.md`
  - `05_战力等级表.md`
  - `06_每卷主线目标.md`
  - `07_长篇控制设定表_canvas.md`
- Formal prose archive: `chapters/`
- Summaries: `chapter_summaries/`
- Working outputs and QA artifacts: `daily_output/`
- Fanqie browser automation helpers: `tools/`
- User/project memory template: `agent-memory-starter/`

## Current State As Of 2026-04-29

- Story phase: volume 2, chapter 21-30 range, still resolving the `旧河公寓` back half.
- Latest formal archive: `chapters/第024章_全文.md`.
- Next planning file: `daily_output/第025章_剧情钩子.md`.
- Archive gap: daily output contains full drafts for chapter 022 and chapter 023, but `chapters/` and `chapter_summaries/` do not contain matching formal files as of 2026-04-29.

## Working Rules

- Preserve the user's existing creative direction. Do not normalize the story into generic fantasy or generic horror.
- Before drafting or revising a chapter, read the relevant canon, the previous chapter, and the latest QA report.
- Do not introduce major organizations, systems, cities, or power mechanics unless they are reflected in the canon files or explicitly requested.
- Keep the protagonist active: rule conflict, tactical choice, cost, and consequence should drive the scene.
- Avoid free cheats. The second-column text is a costly hint layer, not a complete answer machine.
- Keep chapter endings hook-heavy and operationally clear.
- When updating continuity, prefer editing the existing canon table over creating duplicate notes.

## File Hygiene

- Use UTF-8 for Chinese Markdown.
- Do not delete or overwrite drafts, publish versions, QA reports, or summaries unless the user explicitly asks.
- When a chapter is accepted, make sure `chapters/`, `chapter_summaries/`, and `daily_output/` agree on the chapter number and title.
- Keep handoff notes dated with absolute dates.

## Automation Caution

The scripts in `tools/` connect to Chromium over CDP at `http://127.0.0.1:9222` and often operate on the last open page. Confirm the browser page before using publishing scripts.
