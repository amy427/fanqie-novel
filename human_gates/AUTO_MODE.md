# AUTO_MODE

Current version date: 2026-05-16

## Status

Human confirmation gates are disabled for local repository operations only.

Codex may automatically decide:

1. Chapter title.
2. Whether to archive a QA-passed chapter.
3. Whether to generate the next chapter hook.
4. Whether to update continuity state.
5. Whether to update feedback scaffolds.
6. Whether to commit and push.

## External Publishing

External Fanqie publishing is not enabled in unattended mode.

Current repository config is:

```text
auto_publish_external: false
```

To enable a later manual publish, the user must edit the publish file and explicitly request publication for that target. The config must also be changed to:

```text
auto_publish_external: true
```

Until then, this folder records that human gates are removed for local production, not for unsafe platform submission.
