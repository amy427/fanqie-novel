# Fanqie Novel Workspace

This repository contains the long-form web novel production system for `高武：违规者才配活着`.

## Project Snapshot

- Project type: Fanqie web novel production workspace.
- Core goal: produce, QA, archive, publish, and improve a long-running rule-horror urban high-martial-arts serial.
- Protagonist: 江彻.
- Current formal archive as of 2026-05-08: 第031章.
- Next routine target: 第032章.
- GitHub remote: `https://github.com/amy427/fanqie-novel.git`.

## Directory Map

- `00_世界观设定.md` through `07_长篇控制设定表_canvas.md`: core canon and long-form control documents.
- `chapters/`: formal chapter archive. Do not overwrite existing files.
- `chapter_summaries/`: formal chapter summaries. Do not overwrite existing files.
- `daily_output/`: daily generation artifacts, QA reports, publish versions, dry-run logs, hooks, and publish logs.
- `automation/`: repeatable production rules, quality gates, safety rules, and current run state.
- `continuity/`: active story state for open threads, objects, characters, and rules.
- `feedback/`: reader metrics, query configuration, comments, and performance notes.
- `tools/`: Fanqie CDP helpers and safe publish tooling.
- `decision_log/`: dated project decisions.
- `weekly_review/`: periodic review notes.
- `.pw-fanqie-profile/`: local Chrome profile for Fanqie automation. Ignored by Git.

## Operating Entry Points

Read these before running the project:

1. `PROJECT_OS.md`
2. `OPERATING_LOOP.md`
3. `AGENTS.md`
4. `automation/run_state.md`
5. `automation/daily_chapter_run.md`
6. `tools/FANQIE_SAFE_TOOLS.md`

## Daily Chapter Flow

1. Detect latest formal chapter in `chapters/`.
2. Target only latest formal chapter + 1.
3. Read canon, recent chapters, summaries, continuity, and feedback.
4. Generate daily artifacts first under `daily_output/`.
5. Run QA and rewrite once if quality gates fail.
6. Archive to `chapters/` and `chapter_summaries/` only when QA passes.
7. Update continuity, run state, feedback notes, and decision logs.
8. If `auto_publish_external: true`, publish through the safe publisher.
9. Commit and push when the run changes files.

## Fanqie CDP Publishing

Start or verify CDP Chrome:

```powershell
powershell -ExecutionPolicy Bypass -File tools\fanqie_start_cdp_chrome.ps1
```

Safe publisher:

```powershell
python tools\fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX --open-publish-page --create-chapter --auto-submit
```

Important editor rule:

- Chapter number field: Arabic digits only, such as `32`.
- Title field: title only, such as `地下钟室下层`.

Logs and screenshots are stored in `daily_output/publish_logs/`.
