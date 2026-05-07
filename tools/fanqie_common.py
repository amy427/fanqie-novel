from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DAILY_OUTPUT_DIR = PROJECT_ROOT / "daily_output"
FEEDBACK_DIR = PROJECT_ROOT / "feedback"
FEEDBACK_IMPORTS_DIR = FEEDBACK_DIR / "imports"
PUBLISH_LOG_DIR = DAILY_OUTPUT_DIR / "publish_logs"
# Dedicated long-novel Chromium CDP endpoint. Keep short-story automation on 9222.
CDP_URL = "http://127.0.0.1:9223"
PUBLISH_URL = "https://fanqienovel.com/main/writer/7628203489469942846/publish/?enter_from=newchapter_0"
SOURCE_CONFIG_PATH = FEEDBACK_DIR / "source_config.md"


def now_stamp() -> str:
    return datetime.now().strftime("%Y-%m-%d_%H%M%S")


def ensure_dirs() -> None:
    FEEDBACK_IMPORTS_DIR.mkdir(parents=True, exist_ok=True)
    PUBLISH_LOG_DIR.mkdir(parents=True, exist_ok=True)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def read_publish_file(path: Path) -> tuple[str, str, str]:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    lines = text.split("\n")
    while lines and lines[-1] == "":
        lines.pop()
    if not lines:
        raise ValueError(f"Publish file is empty: {path}")
    title = lines[0].strip()
    body_lines = lines[1:]
    blank_lines = [i + 2 for i, line in enumerate(body_lines) if not line.strip()]
    if blank_lines:
        raise ValueError(f"Publish file has blank body lines at: {blank_lines[:20]}")
    body = "\n".join(body_lines)
    return title, body, "\n".join([title, *body_lines])


def extract_chapter_number(title: str) -> int | None:
    import re

    match = re.search(r"第\s*0*(\d+)\s*章", title)
    return int(match.group(1)) if match else None


def dump_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def append_markdown_log(path: Path, heading: str, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    existing = path.read_text(encoding="utf-8") if path.exists() else "# Log\n"
    block = ["", f"## {heading}", *lines, ""]
    path.write_text(existing.rstrip() + "\n" + "\n".join(block), encoding="utf-8")


def get_last_page(playwright):
    browser = playwright.chromium.connect_over_cdp(CDP_URL)
    pages = []
    for context in browser.contexts:
        pages.extend(context.pages)
    if not pages:
        browser.close()
        raise RuntimeError("No Chromium pages found over CDP")
    return browser, pages[-1]


def looks_like_fanqie_page(url: str, title: str, body_text: str) -> bool:
    haystack = f"{url}\n{title}\n{body_text[:3000]}".lower()
    markers = [
        "fanqie",
        "番茄",
        "作家",
        "章节",
        "作品",
        "数据",
        "评论",
    ]
    return any(marker.lower() in haystack for marker in markers)


def looks_like_analytics_or_comments(url: str, title: str, body_text: str) -> bool:
    haystack = f"{url}\n{title}\n{body_text[:6000]}".lower()
    page_markers = ["数据", "阅读", "评论", "书评", "追读", "收益", "分析", "analytics", "comment"]
    return looks_like_fanqie_page(url, title, body_text) and any(
        marker.lower() in haystack for marker in page_markers
    )


def auto_publish_external_enabled() -> bool:
    if not SOURCE_CONFIG_PATH.exists():
        return False
    text = SOURCE_CONFIG_PATH.read_text(encoding="utf-8").lower()
    return "auto_publish_external: true" in text
