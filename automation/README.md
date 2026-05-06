# automation

This folder turns the long daily-generation prompt into a maintainable local operating system.

Core idea:

1. `chapters/` is the only source for completed formal chapters.
2. `daily_output/` may contain publish-ready work, but it is not formal until archived.
3. Daily automation must pass safety checks before writing any formal chapter or summary.
4. Failed runs stay in `daily_output/` and must not touch `chapters/` or `chapter_summaries/`.
5. Existing old chapters, summaries, and canon files are never overwritten.

Files:

- `daily_chapter_run.md`: daily automation task.
- `chapter_generation_spec.md`: chapter generation and output rules.
- `quality_gates.md`: pass/fail checks before formal archival.
- `safety_rules.md`: filesystem and overwrite protections.
- `run_state.md`: current automation state snapshot.
