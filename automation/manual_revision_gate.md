# Manual Revision Gate

Current version date: 2026-05-16

## Purpose

Routine automation must stop before Fanqie publishing.

Reason:

The previous book lost traffic after insufficient human revision and was likely judged as AI filler. The user now wants to modify the publish version manually before any external submission.

## Required Behavior

After QA passes, automation may create:

1. Formal chapter.
2. Formal summary.
3. Fanqie publish version.
4. Publish checklist.
5. Manual revision checklist.
6. Continuity and feedback updates.
7. Commit and push.

Automation must not:

1. Open the Fanqie publish flow for routine submission.
2. Fill the Fanqie editor.
3. Click next, submit, confirm, or publish.
4. Use `--auto-submit`.
5. Treat a QA-passed AI draft as externally publishable without user edits.

## Required Checklist

For each chapter prepared for publication, create:

```text
daily_output\第XXX章_人工改稿清单.md
```

The checklist must include:

1. Lines that sound generic or AI-like.
2. Places where sensory detail should be made more concrete.
3. Repeated sentence rhythms to vary.
4. Dialogue beats that need more human sharpness.
5. Opening and ending checks.
6. A final confirmation field for the user's edited version.

## Manual Publish Exception

Manual publishing is allowed only when all are true:

1. The user explicitly asks to publish the edited file in the current turn.
2. `feedback/source_config.md` has `auto_publish_external: true`.
3. The target file exists and has passed local validation.
4. The safe publisher is used.

Command:

```powershell
python tools\fanqie_safe_publish.py --file daily_output\第XXX章_番茄发布版.txt --expected-chapter XXX --open-publish-page --create-chapter --auto-submit
```
