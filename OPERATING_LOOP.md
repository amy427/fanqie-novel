# OPERATING_LOOP

Current version date: 2026-05-08

## 1. Closed Loop

Each routine run follows this loop:

```text
state check
-> target decision
-> input reading
-> chapter generation or repair
-> QA
-> market/publish packaging
-> formal archive
-> continuity update
-> feedback query
-> Fanqie publish if authorized
-> Git commit and push
-> next hook and run state
```

## 2. State Check

Required checks:

1. Current working directory is `D:\fanqie-novel`.
2. Git worktree status.
3. Latest formal chapter in `chapters/`.
4. Latest formal summary in `chapter_summaries/`.
5. Pending publish-ready daily output.
6. Latest QA report.
7. Latest next-chapter hook.
8. CDP state if feedback query or publishing is requested.

Output:

- Update `automation/run_state.md`.
- Add a dated note to `decision_log/DECISION_LOG.md` when the state changes.

## 3. Target Decision

Default target is latest formal chapter + 1.

Stop if:

1. Target formal chapter already exists.
2. Target summary already exists.
3. A newer daily output is publish-ready but not archived.
4. There is a run lock at `daily_output/.run_lock`.

## 4. Input Reading

Read in priority order:

1. Latest 3 formal chapters.
2. `07_长篇控制设定表_canvas.md`.
3. Recent chapter summaries.
4. Continuity files under `continuity/`.
5. Relevant QA and hook files under `daily_output/`.
6. Core canon files `00_*.md` through `06_*.md`.
7. Feedback files under `feedback/`.

## 5. Generation

Generate only the target chapter.

Rules:

1. 4000 to 5000 non-whitespace body characters.
2. Open directly in conflict.
3. Keep paragraphs short.
4. No blank lines in formal prose or Fanqie publish text.
5. Rule conflict drives payoff.
6. 江彻 must choose, pay, and push the scene.
7. No free cheat.
8. No unauthorized major setting expansion.

## 6. QA

Run `automation/quality_gates.md`.

If QA fails:

1. Rewrite once.
2. Re-run QA.
3. If still failing, do not archive.
4. Keep failed draft, QA report, and dry-run log in `daily_output/`.

If QA passes:

1. Write formal chapter to `chapters/`.
2. Write summary to `chapter_summaries/`.
3. Write publish version and checklist to `daily_output/`.

## 7. Feedback

Run feedback query only when CDP page is verified as Fanqie analytics or comments.

If unavailable:

1. Log the skip reason in `feedback/query_log.md`.
2. Continue local production.

## 8. Publish

Publish only through `tools/fanqie_safe_publish.py`.

Before publishing:

1. Ensure `feedback/source_config.md` contains `auto_publish_external: true`.
2. Ensure CDP is reachable at `http://127.0.0.1:9222`.
3. If not reachable, run `tools/fanqie_start_cdp_chrome.ps1`.
4. Ensure the target publish file exists.

Fanqie field split:

1. Chapter number field between `第` and `章`: Arabic digits only.
2. Title field after `章`: chapter title only.

## 9. Versioning

After successful operational changes:

```powershell
git status --short --branch
git add <changed files>
git commit -m "Update project operating system"
git push
```

Never use `git reset --hard`.

## 10. Final Reply

Do not paste chapter prose.

Report only:

1. Current project state.
2. What changed.
3. Key files updated.
4. QA result.
5. Git commit/push result.
6. Remaining gaps.
7. Next best action.
