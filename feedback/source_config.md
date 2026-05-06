# Feedback Source Config

Current version date: 2026-05-06

## Enabled Sources

| Source | Status | Mode | Notes |
| --- | --- | --- | --- |
| Local files | enabled | read-only | Always available |
| Feedback imports | enabled | read-only | Put exports in `feedback/imports/` |
| Fanqie browser analytics | optional | read-only CDP | Requires verified Fanqie analytics/comments page |
| GitHub repository | enabled | read-only network | Useful for repository state, not reader data |

## External Publishing

```text
auto_publish_external: false
```

This config enables automatic query, not automatic Fanqie publishing.

## Import Folder

Place exported reader metrics or comments here:

```text
feedback/imports/
```
