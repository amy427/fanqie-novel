from __future__ import annotations

import argparse
import re
from pathlib import Path

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright

from fanqie_common import (
    FEEDBACK_IMPORTS_DIR,
    append_markdown_log,
    dump_json,
    ensure_dirs,
    get_last_page,
    looks_like_analytics_or_comments,
    now_stamp,
)


QUERY_LOG = Path(r"D:\fanqie-novel\feedback\query_log.md")


def parse_metric_candidates(text: str) -> dict[str, list[str]]:
    patterns = {
        "阅读": r"(?:阅读|阅读量|浏览|展现|曝光)[^\n]{0,20}",
        "追读": r"(?:追读|完读|留存)[^\n]{0,20}",
        "收藏": r"(?:收藏|加入书架)[^\n]{0,20}",
        "评论": r"(?:评论|书评|段评)[^\n]{0,20}",
        "收益": r"(?:收益|收入)[^\n]{0,20}",
    }
    results: dict[str, list[str]] = {}
    for key, pattern in patterns.items():
        matches = [m.group(0).strip() for m in re.finditer(pattern, text)]
        results[key] = list(dict.fromkeys(matches))[:20]
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only Fanqie metrics/comments page scraper.")
    parser.add_argument("--cdp", default="http://127.0.0.1:9222", help="Chromium CDP endpoint; kept for CLI clarity.")
    parser.add_argument("--allow-unverified", action="store_true", help="Save page text even if page type is not verified.")
    parser.add_argument("--max-chars", type=int, default=60000)
    args = parser.parse_args()

    ensure_dirs()
    stamp = now_stamp()
    try:
        with sync_playwright() as p:
            browser, page = get_last_page(p)
            try:
                page.wait_for_load_state("domcontentloaded", timeout=15000)
            except PlaywrightTimeoutError:
                pass
            url = page.url
            title = page.title()
            body = page.locator("body").inner_text(timeout=15000)
            verified = looks_like_analytics_or_comments(url, title, body)
            if not verified and not args.allow_unverified:
                append_markdown_log(
                    QUERY_LOG,
                    f"{stamp} Fanqie read-only query skipped",
                    [
                        "- Result: skipped",
                        "- Reason: current page was not verified as Fanqie analytics/comments page",
                        f"- URL: `{url}`",
                        f"- Title: `{title}`",
                    ],
                )
                print("SKIPPED_UNVERIFIED_PAGE")
                print("URL:", url)
                print("TITLE:", title)
                browser.close()
                return 2

            body_limited = body[: args.max_chars]
            metrics = parse_metric_candidates(body_limited)
            json_path = FEEDBACK_IMPORTS_DIR / f"{stamp}_fanqie_readonly_metrics.json"
            text_path = FEEDBACK_IMPORTS_DIR / f"{stamp}_fanqie_readonly_page.txt"
            dump_json(
                json_path,
                {
                    "timestamp": stamp,
                    "url": url,
                    "title": title,
                    "verified": verified,
                    "metric_candidates": metrics,
                    "body_chars_saved": len(body_limited),
                },
            )
            text_path.write_text(body_limited, encoding="utf-8")
            append_markdown_log(
                QUERY_LOG,
                f"{stamp} Fanqie read-only query",
                [
                    "- Result: saved",
                    f"- Verified: `{verified}`",
                    f"- URL: `{url}`",
                    f"- Title: `{title}`",
                    f"- JSON: `{json_path}`",
                    f"- Text: `{text_path}`",
                ],
            )
            print("SAVED_JSON:", json_path)
            print("SAVED_TEXT:", text_path)
            browser.close()
            return 0
    except Exception as exc:
        append_markdown_log(
            QUERY_LOG,
            f"{stamp} Fanqie read-only query failed",
            ["- Result: failed", f"- Error: `{type(exc).__name__}: {exc}`"],
        )
        print("ERROR:", type(exc).__name__, exc)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

