from __future__ import annotations

import argparse
import re

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright

from fanqie_common import CDP_URL, PUBLISH_LOG_DIR, dump_json, ensure_dirs, now_stamp


WORK_ID = "7628203489469942846"
BOOK_NAME = "高武：违规者才配活着"
WRITER_HOME_URL = "https://fanqienovel.com/main/writer/"
CHAPTER_MANAGE_URL = (
    f"https://fanqienovel.com/main/writer/chapter-manage/{WORK_ID}&"
    "%E9%AB%98%E6%AD%A6%EF%BC%9A%E8%BF%9D%E8%A7%84%E8%80%85%E6%89%8D%E9%85%8D%E6%B4%BB%E7%9D%80?type=1"
)
DRAFT_URL = CHAPTER_MANAGE_URL.replace("type=1", "type=2")


def parse_recent_update(text: str) -> dict[str, object] | None:
    match = re.search(r"最近更新：第\s*0*(\d+)\s*章\s*([^\n]+)", text)
    if not match:
        return None
    return {"chapter": int(match.group(1)), "title": match.group(2).strip()}


def parse_chapter_rows(text: str) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    pattern = re.compile(
        r"第\s*0*(\d+)\s*章\s*([^\n]+)\s+([0-9\\-]+)\s+([0-9\\-]+)\s+([^\n]+)\s+([0-9]{4}-[0-9]{2}-[0-9]{2}[^\n]*)",
        re.M,
    )
    for match in pattern.finditer(text):
        rows.append(
            {
                "chapter": int(match.group(1)),
                "title": match.group(2).strip(),
                "word_count": match.group(3).strip(),
                "typos": match.group(4).strip(),
                "status": match.group(5).strip(),
                "time": match.group(6).strip(),
            }
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify Fanqie external publish state from the author backend.")
    parser.add_argument("--expect-next", type=int, default=0, help="Optional expected next chapter to publish.")
    parser.add_argument("--json-only", action="store_true")
    args = parser.parse_args()

    ensure_dirs()
    stamp = now_stamp()
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(CDP_URL)
        context = browser.contexts[0] if browser.contexts else browser.new_context()
        page = context.pages[-1] if context.pages else context.new_page()

        page.goto(WRITER_HOME_URL, wait_until="domcontentloaded", timeout=45000)
        try:
            page.wait_for_load_state("networkidle", timeout=15000)
        except PlaywrightTimeoutError:
            pass
        page.wait_for_timeout(3000)
        home_text = page.locator("body").inner_text(timeout=15000)
        recent = parse_recent_update(home_text)

        page.goto(CHAPTER_MANAGE_URL, wait_until="domcontentloaded", timeout=45000)
        try:
            page.wait_for_load_state("networkidle", timeout=15000)
        except PlaywrightTimeoutError:
            pass
        page.wait_for_timeout(3000)
        manage_text = page.locator("body").inner_text(timeout=15000)
        published_rows = parse_chapter_rows(manage_text)
        latest_published = max(
            (row for row in published_rows if row.get("status") == "已发布"),
            key=lambda row: int(row["chapter"]),
            default=None,
        )
        audit_rows = [row for row in published_rows if row.get("status") != "已发布"]

        page.goto(DRAFT_URL, wait_until="domcontentloaded", timeout=45000)
        try:
            page.wait_for_load_state("networkidle", timeout=15000)
        except PlaywrightTimeoutError:
            pass
        page.wait_for_timeout(3000)
        draft_text = page.locator("body").inner_text(timeout=15000)
        draft_rows = parse_chapter_rows(draft_text)

        result = {
            "timestamp": stamp,
            "book": BOOK_NAME,
            "writer_home_url": WRITER_HOME_URL,
            "chapter_manage_url": CHAPTER_MANAGE_URL,
            "recent_update": recent,
            "latest_published": latest_published,
            "audit_or_pending_rows": audit_rows,
            "draft_rows": draft_rows,
            "expect_next": args.expect_next or None,
        }
        if args.expect_next:
            external_latest = int(latest_published["chapter"]) if latest_published else None
            result["expectation_passed"] = external_latest is not None and external_latest + 1 == args.expect_next

        json_path = PUBLISH_LOG_DIR / f"{stamp}_fanqie_publish_state.json"
        dump_json(json_path, result)
        if not args.json_only:
            print(f"JSON: {json_path}")
            print(f"Recent update: {recent}")
            print(f"Latest published: {latest_published}")
            print(f"Audit/pending rows: {audit_rows[:5]}")
            print(f"Draft rows: {draft_rows[:5]}")
            if args.expect_next:
                print(f"Expectation passed: {result['expectation_passed']}")
        browser.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
