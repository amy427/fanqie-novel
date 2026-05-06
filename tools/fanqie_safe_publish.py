from __future__ import annotations

import argparse
from pathlib import Path

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright

from fanqie_common import (
    PUBLISH_LOG_DIR,
    PUBLISH_URL,
    append_markdown_log,
    auto_publish_external_enabled,
    dump_json,
    ensure_dirs,
    extract_chapter_number,
    get_last_page,
    looks_like_fanqie_page,
    now_stamp,
    read_publish_file,
    sha256_text,
)


RUN_LOG = Path(r"D:\fanqie-novel\daily_output\publish_logs\safe_publish_log.md")


def find_title_input(page):
    candidates = [
        page.locator("input[placeholder*='标题']").first,
        page.locator("textarea[placeholder*='标题']").first,
        page.locator("input").first,
    ]
    for locator in candidates:
        try:
            if locator.count() and locator.first.is_visible(timeout=2000):
                return locator.first
        except Exception:
            continue
    raise RuntimeError("Title input not found")


def find_body_editor(page):
    candidates = [
        page.locator("[contenteditable='true']").filter(has_text="请输入正文").first,
        page.locator("[contenteditable='true']").first,
        page.locator("textarea[placeholder*='正文']").first,
    ]
    for locator in candidates:
        try:
            if locator.count() and locator.first.is_visible(timeout=2000):
                return locator.first
        except Exception:
            continue
    raise RuntimeError("Body editor not found")


def main() -> int:
    parser = argparse.ArgumentParser(description="Safe Fanqie publish helper with dry-run default.")
    parser.add_argument("--file", required=True, help="Path to 第XXX章_番茄发布版.txt")
    parser.add_argument("--expected-chapter", type=int, required=True)
    parser.add_argument("--fill", action="store_true", help="Fill title/body into current page, but do not submit.")
    parser.add_argument("--submit", action="store_true", help="Submit/publish after validation. Requires --fill and --confirm-submit.")
    parser.add_argument("--auto-submit", action="store_true", help="Unattended fill+submit if auto_publish_external is true in feedback/source_config.md.")
    parser.add_argument("--open-publish-page", action="store_true", help="Navigate to the configured Fanqie publish page before validation.")
    parser.add_argument("--create-chapter", action="store_true", help="Click 创建章节 if present before filling.")
    parser.add_argument("--confirm-submit", default="", help="Must equal expected SHA256 to allow submit.")
    parser.add_argument("--allow-unverified-page", action="store_true")
    args = parser.parse_args()

    ensure_dirs()
    stamp = now_stamp()
    path = Path(args.file)
    title, body, full_text = read_publish_file(path)
    expected_sha = sha256_text(full_text)
    chapter_no = extract_chapter_number(title)
    if chapter_no != args.expected_chapter:
        raise SystemExit(f"Chapter mismatch: title chapter={chapter_no}, expected={args.expected_chapter}")
    if args.auto_submit:
        if not auto_publish_external_enabled():
            raise SystemExit("Auto submit refused: auto_publish_external is not true in feedback/source_config.md")
        args.fill = True
        args.submit = True
    if args.submit and not args.fill:
        raise SystemExit("Submit refused: requires fill")
    if args.submit and not args.auto_submit and args.confirm_submit != expected_sha:
        raise SystemExit("Submit refused: requires --confirm-submit equal to content SHA256")

    with sync_playwright() as p:
        browser, page = get_last_page(p)
        if args.open_publish_page:
            page.goto(PUBLISH_URL, wait_until="domcontentloaded", timeout=45000)
            try:
                page.wait_for_load_state("networkidle", timeout=15000)
            except PlaywrightTimeoutError:
                pass
        try:
            page.wait_for_load_state("domcontentloaded", timeout=15000)
        except PlaywrightTimeoutError:
            pass

        if args.create_chapter:
            create = page.get_by_text("创建章节", exact=True).first
            if create.count():
                create.click(timeout=15000)
                try:
                    page.wait_for_load_state("networkidle", timeout=15000)
                except PlaywrightTimeoutError:
                    pass
                page.wait_for_timeout(1000)

        url = page.url
        page_title = page.title()
        body_text = page.locator("body").inner_text(timeout=15000)
        verified = looks_like_fanqie_page(url, page_title, body_text)
        if not verified and not args.allow_unverified_page:
            browser.close()
            raise SystemExit(f"Current page not verified as Fanqie author page: {url} | {page_title}")

        screenshot_path = PUBLISH_LOG_DIR / f"{stamp}_chapter_{args.expected_chapter:03d}_precheck.png"
        page.screenshot(path=str(screenshot_path), full_page=True)

        log_data = {
            "timestamp": stamp,
            "mode": "submit" if args.submit else "fill" if args.fill else "dry-run",
            "file": str(path),
            "expected_chapter": args.expected_chapter,
            "title": title,
            "body_non_whitespace_chars": len("".join(body.split())),
            "sha256": expected_sha,
            "url": url,
            "page_title": page_title,
            "verified_page": verified,
            "auto_submit": args.auto_submit,
            "opened_publish_page": args.open_publish_page,
            "create_chapter_requested": args.create_chapter,
            "screenshot": str(screenshot_path),
            "filled": False,
            "submitted": False,
        }

        if args.fill:
            title_input = find_title_input(page)
            editor = find_body_editor(page)
            title_input.click(timeout=10000)
            title_input.fill(title)
            editor.click(timeout=10000)
            editor.fill(body)
            page.wait_for_timeout(1000)
            title_value = title_input.input_value(timeout=10000) if hasattr(title_input, "input_value") else ""
            editor_text = editor.inner_text(timeout=10000)
            filled_sha = sha256_text(title_value.strip() + "\n" + editor_text.strip())
            if title_value.strip() != title:
                raise RuntimeError("Filled title verification failed")
            if "".join(editor_text.split()) != "".join(body.split()):
                raise RuntimeError("Filled body verification failed")
            log_data["filled"] = True
            log_data["filled_sha256"] = filled_sha
            filled_screenshot = PUBLISH_LOG_DIR / f"{stamp}_chapter_{args.expected_chapter:03d}_filled.png"
            page.screenshot(path=str(filled_screenshot), full_page=True)
            log_data["filled_screenshot"] = str(filled_screenshot)

        if args.submit:
            publish_buttons = page.get_by_role("button", name="发布")
            if publish_buttons.count() == 0:
                publish_buttons = page.get_by_text("发布", exact=True)
            if publish_buttons.count() == 0:
                raise RuntimeError("Publish button not found")
            publish_buttons.last.click(timeout=15000)
            page.wait_for_timeout(1000)
            modal = page.locator(".arco-modal-wrapper").last
            if modal.count():
                modal_text = modal.inner_text(timeout=10000)
                log_data["submit_modal_text_start"] = modal_text[:500]
                yes_text = modal.get_by_text("是", exact=True)
                if yes_text.count():
                    yes_text.first.click(timeout=10000)
                confirm = modal.get_by_role("button", name="确认发布")
                if confirm.count() == 0:
                    confirm = modal.get_by_text("确认发布", exact=True)
                if confirm.count() == 0:
                    raise RuntimeError("Confirm publish button not found")
                confirm.last.click(timeout=15000)
            log_data["submitted"] = True
            page.wait_for_timeout(5000)
            submitted_screenshot = PUBLISH_LOG_DIR / f"{stamp}_chapter_{args.expected_chapter:03d}_submitted.png"
            page.screenshot(path=str(submitted_screenshot), full_page=True)
            log_data["submitted_screenshot"] = str(submitted_screenshot)

        json_path = PUBLISH_LOG_DIR / f"{stamp}_chapter_{args.expected_chapter:03d}_safe_publish.json"
        dump_json(json_path, log_data)
        append_markdown_log(
            RUN_LOG,
            f"{stamp} chapter {args.expected_chapter:03d} safe publish",
            [
                f"- Mode: `{log_data['mode']}`",
                f"- Title: `{title}`",
                f"- SHA256: `{expected_sha}`",
                f"- Verified page: `{verified}`",
                f"- JSON: `{json_path}`",
                f"- Screenshot: `{screenshot_path}`",
                f"- Submitted: `{log_data['submitted']}`",
            ],
        )
        print("MODE:", log_data["mode"])
        print("TITLE:", title)
        print("SHA256:", expected_sha)
        print("JSON:", json_path)
        print("SCREENSHOT:", screenshot_path)
        browser.close()
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
