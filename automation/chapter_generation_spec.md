# Chapter Generation Spec

Current version date: 2026-05-06

## Directories

Formal chapters:

```text
D:\fanqie-novel\chapters\
```

Formal summaries:

```text
D:\fanqie-novel\chapter_summaries\
```

Daily output:

```text
D:\fanqie-novel\daily_output\
```

## Latest Chapter Detection

1. Primary source: `chapters/第XXX章_全文.md`.
2. `chapter_summaries/` is auxiliary only.
3. `daily_output` drafts are not formal chapters.
4. A `daily_output` chapter with QA saying `是否建议人工发布：是` is publish-ready but still not formal.
5. If a publish-ready chapter exists after the latest formal chapter, do not generate a later chapter until that pending chapter is resolved.
6. Never overwrite existing formal chapter or formal summary files.

## Required Reading

Always read:

1. `00_世界观设定.md`
2. `01_主角能力表.md`
3. `02_角色关系表.md`
4. `03_伏笔回收表.md`
5. `04_副本记录表.md`
6. `05_战力等级表.md`
7. `06_每卷主线目标.md`
8. `07_长篇控制设定表_canvas.md`
9. All available `chapter_summaries/`
10. Recent three formal chapter files from `chapters/`

If summaries are missing, use corresponding formal chapter text or daily output draft only as support.

Priority when sources conflict:

1. Recent three formal chapters.
2. `07_长篇控制设定表_canvas.md`.
3. Existing chapter summaries.
4. Earlier formal chapters.
5. `00` to `06` base canon.

Do not explain source conflicts inside the chapter. Record conflicts in the QA report.

## Target Chapter Requirements

1. 4000 to 5000 Chinese characters, excluding title whitespace.
2. Complete prose, not outline or summary.
3. Fanqie male-frequency urban high-martial-arts plus rule-horror plus dungeon suspense.
4. Protagonist is 江彻.
5. Open directly with conflict.
6. Include opening conflict, middle pressure, active protagonist decision, clear rule-based payoff, clear cost, and strong ending hook.
7. Payoff should come from rule reversal, evidence chains, and tactical choice, not sudden power gain.
8. Do not add major organizations, cities, high-level systems, or power mechanics.
9. Do not give 江彻 a free cheat.
10. Do not let second-column text solve the chapter for him.
11. Do not fully resolve a main crisis in one chapter.

## Prose Hard Rules

1. Dialogue, broadcasts, intercoms,诱导声, and mimic voices must use Chinese double quotes.
2. Narrative text should not use quotation marks.
3. Do not use em dashes.
4. Do not use bold text.
5. Rules, files, lists, system prompts, and archive entries should be isolated on their own lines.
6. Keep paragraphs short.
7. One line should complete one action, judgment, or information beat.
8. Do not write `以下是正文`.
9. Do not write `承接上一章`.
10. Do not include author explanation.

## No-Blank-Line Rule

Applies to:

1. `chapters/第XXX章_全文.md`
2. `daily_output/第XXX章_番茄发布版.txt`
3. `daily_output/第XXX章_完整正文_备份.md`, if created

Rules:

1. No blank line after title.
2. No blank line between paragraphs.
3. A line containing only spaces or tabs counts as a blank line.
4. Markdown reports may keep normal Markdown spacing; this no-blank-line rule only applies to novel prose and publish text.

## Summary Requirements

When a chapter passes QA, write:

```text
chapter_summaries/第XXX章_摘要.md
```

Summary must contain:

1. Chapter title.
2. Core plot, 300 to 600 Chinese characters.
3. New information.
4. Old foreshadowing advanced.
5. New foreshadowing.
6. Character state changes.
7. Chapter ending hook.
8. Next chapter must-follow point.
