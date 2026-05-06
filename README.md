# Fanqie Novel Workspace

This workspace contains the long-form web novel project `高武：违规者才配活着`.

## Project Snapshot

- Title: `高武：违规者才配活着`
- Pen name: `饮血独行`
- Genre: urban male-frequency fiction, high martial arts, rule-horror, dungeon suspense, progression, class reversal
- Current protagonist: `江彻`
- Core publishing target: long-running Fanqie serial, strong retention in the first 20 chapters, scalable beyond 200 chapters
- Current story phase as of 2026-04-29: volume 2, chapters 21-30, finishing the second half of the `旧河公寓` arc before moving into black-market martial qualification

## Directory Map

- `00_世界观设定.md` through `07_长篇控制设定表_canvas.md`: core canon and long-form control documents.
- `chapters/`: formal chapter archive. It currently contains chapters 001-021 and chapter 024.
- `chapter_summaries/`: chapter summaries. It currently contains summaries for chapters 001-020 and chapter 024.
- `daily_output/`: daily generation artifacts, including full drafts, Fanqie publish versions, QA reports, foreshadowing suggestions, and hooks for chapters 021-025.
- `tools/`: Playwright helper scripts for navigating and publishing in the Fanqie author interface through an existing Chromium CDP session.
- `agent-memory-starter/`: local personal/project memory template for preserving user profile, principles, tasks, and daily logs.
- `.pw-fanqie-profile/`: browser profile data for Fanqie automation. Treat as local state.
- `123/`: empty trusted Codex workspace folder as of 2026-04-29.

## Current Chapter State

- Chapter 024 is the latest formally archived chapter in `chapters/`.
- `daily_output/第025章_剧情钩子.md` contains the next planning material.
- `daily_output/第022章_完整正文.md` and `daily_output/第023章_完整正文.md` exist, but matching formal archives and summaries are not present in `chapters/` or `chapter_summaries/` as of 2026-04-29.

Before continuing chapter 025, decide whether to backfill chapter 022 and chapter 023 into the formal archive and summary folders.

## Writing Rules

- Do not rely on vague emotion words, routine shock reactions, or repeated mechanical power fantasy beats.
- Push scenes through rules, space, action, judgment, cost, and concrete consequence.
- The protagonist should solve problems through rule conflicts and active decisions, not free external cheats.
- Every major gain should carry an explicit cost, especially through recognition-line pollution, object damage, identity risk, or relationship risk.
- Maintain short paragraphs, high pressure, clear chapter hooks, and rule-based reversals.

## Chapter Workflow

1. Read the relevant canon files before drafting:
   - `00_世界观设定.md`
   - `02_角色关系表.md`
   - `03_伏笔回收表.md`
   - `06_每卷主线目标.md`
   - `07_长篇控制设定表_canvas.md`
2. Read the previous chapter and its summary.
3. Draft into `daily_output/第NNN章_完整正文.md`.
4. Produce or update:
   - `daily_output/第NNN章_质检报告.md`
   - `daily_output/第NNN章_伏笔更新建议.md`
   - `daily_output/第NNN章_发布检查清单.md`
   - `daily_output/第NNN章_剧情钩子.md` for the next chapter
5. If the chapter passes QA, archive it to `chapters/` and create/update the matching file in `chapter_summaries/`.

## Fanqie Automation Notes

The scripts in `tools/` assume Chromium is already running with CDP available at `http://127.0.0.1:9222`.

Common flow:

```powershell
python tools/fanqie_open_publish_page.py
python tools/fanqie_fill_chapter.py
python tools/fanqie_submit_until_done.py
python tools/fanqie_verify_published.py
```

Inspect script contents before use, because several scripts operate on the most recent browser page in the connected Chromium context.

## Handoff Notes

- This is not a Git repository as of 2026-04-29.
- Treat all Markdown canon files as source-of-truth story documents.
- Do not overwrite user-authored chapter files without checking the matching daily output, QA report, and summary state.
- Keep absolute dates in handoff notes. Avoid vague relative time labels.
