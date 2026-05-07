from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
import traceback

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import sync_playwright

from fanqie_common import (
    CDP_URL,
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


def split_chapter_title(title: str) -> tuple[int | None, str]:
    match = re.search(r"第\s*0*(\d+)\s*章\s*(.*)", title)
    if not match:
        return None, title.strip()
    chapter_no = int(match.group(1))
    chapter_title = match.group(2).strip() or title.strip()
    return chapter_no, chapter_title


def find_chapter_number_input(page):
    candidates = [
        page.locator("input.serial-input").nth(0),
        page.locator("input[type='text']").first,
    ]
    for locator in candidates:
        try:
            if locator.count() and locator.first.is_visible(timeout=2000):
                return locator.first
        except Exception:
            continue
    raise RuntimeError("Chapter number input not found")


def find_body_editor(page):
    candidates = [
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


def dismiss_known_overlays(page) -> None:
    for text in ["知道了", "我知道了", "确定"]:
        try:
            loc = page.get_by_text(text, exact=True)
            if loc.count():
                loc.last.click(timeout=3000)
                page.wait_for_timeout(500)
        except Exception:
            continue


def click_last_button_by_text(page, texts: list[str], timeout: int = 15000) -> str | None:
    for text in texts:
        loc = page.get_by_role("button", name=text)
        if loc.count() == 0:
            loc = page.get_by_text(text, exact=True)
        if loc.count():
            loc.last.click(timeout=timeout)
            return text
    return None


def click_modal_primary(modal, timeout: int = 10000) -> str | None:
    buttons = modal.locator("button.arco-btn-primary")
    if buttons.count() == 0:
        buttons = modal.locator("button")
    if buttons.count() == 0:
        return None
    button = buttons.last
    try:
        text = button.inner_text(timeout=1000).strip()
    except Exception:
        text = "<unreadable>"
    button.click(timeout=timeout)
    return text


def select_ai_yes_if_present(modal) -> bool:
    radio = modal.locator("input[type='radio'][value='1']").first
    if radio.count() == 0:
        return False
    try:
        radio.locator("xpath=ancestor::label[1]").click(timeout=10000)
    except Exception:
        radio.check(force=True, timeout=10000)
    return True


def wait_and_click_last_button_by_text(page, texts: list[str], attempts: int = 15) -> str | None:
    for _ in range(attempts):
        clicked = click_last_button_by_text(page, texts, timeout=3000)
        if clicked:
            return clicked
        page.wait_for_timeout(1000)
    return None


def safe_screenshot(page, path: Path, log_data: dict, key: str) -> None:
    try:
        page.screenshot(path=str(path), full_page=True, timeout=60000)
        log_data[key] = str(path)
    except PlaywrightTimeoutError as exc:
        log_data[f"{key}_error"] = f"{type(exc).__name__}: {exc}"


def get_page(playwright, new_page: bool, page_url_contains: str = ""):
    if page_url_contains:
        browser = playwright.chromium.connect_over_cdp(CDP_URL)
        for context in browser.contexts:
            for page in context.pages:
                if page_url_contains in page.url:
                    return browser, page
        browser.close()
        raise RuntimeError(f"No CDP page URL contains: {page_url_contains}")
    if not new_page:
        return get_last_page(playwright)
    browser = playwright.chromium.connect_over_cdp(CDP_URL)
    context = browser.contexts[0] if browser.contexts else browser.new_context()
    return browser, context.new_page()


def main() -> int:
    parser = argparse.ArgumentParser(description="Safe Fanqie publish helper with dry-run default.")
    parser.add_argument("--file", required=True, help="Path to 第XXX章_番茄发布版.txt")
    parser.add_argument("--expected-chapter", type=int, required=True)
    parser.add_argument("--fill", action="store_true", help="Fill title/body into current page, but do not submit.")
    parser.add_argument("--submit", action="store_true", help="Submit/publish after validation. Requires --fill and --confirm-submit.")
    parser.add_argument("--auto-submit", action="store_true", help="Unattended fill+submit if auto_publish_external is true in feedback/source_config.md.")
    parser.add_argument("--open-publish-page", action="store_true", help="Navigate to the configured Fanqie publish page before validation.")
    parser.add_argument("--new-page", action="store_true", help="Open a new browser tab over CDP instead of reusing the last open page.")
    parser.add_argument("--page-url-contains", default="", help="Reuse an existing CDP page whose URL contains this text.")
    parser.add_argument("--create-chapter", action="store_true", help="Click 创建章节 if present before filling.")
    parser.add_argument("--confirm-submit", default="", help="Must equal expected SHA256 to allow submit.")
    parser.add_argument("--allow-unverified-page", action="store_true")
    args = parser.parse_args()

    ensure_dirs()
    stamp = now_stamp()
    path = Path(args.file)
    title, body, full_text = read_publish_file(path)
    chapter_no_from_title, chapter_title = split_chapter_title(title)
    expected_sha = sha256_text(full_text)
    chapter_no = extract_chapter_number(title)
    if chapter_no is None:
        chapter_no = chapter_no_from_title
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
        browser, page = get_page(p, args.new_page, args.page_url_contains)
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
        dismiss_known_overlays(page)

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
            "new_page": args.new_page,
            "page_url_contains": args.page_url_contains,
            "create_chapter_requested": args.create_chapter,
            "filled": False,
            "submitted": False,
        }

        screenshot_path = PUBLISH_LOG_DIR / f"{stamp}_chapter_{args.expected_chapter:03d}_precheck.png"
        safe_screenshot(page, screenshot_path, log_data, "screenshot")

        if args.fill:
            dismiss_known_overlays(page)
            number_input = find_chapter_number_input(page)
            title_input = find_title_input(page)
            editor = find_body_editor(page)
            number_input.click(timeout=10000)
            number_input.fill(str(args.expected_chapter))
            title_input.click(timeout=10000)
            title_input.fill(chapter_title)
            editor.click(timeout=10000)
            editor.fill(body)
            page.wait_for_timeout(1000)
            number_value = number_input.input_value(timeout=10000)
            title_value = title_input.input_value(timeout=10000) if hasattr(title_input, "input_value") else ""
            editor_text = editor.inner_text(timeout=10000)
            filled_sha = sha256_text(f"第{number_value.strip()}章 {title_value.strip()}\n{editor_text.strip()}")
            if number_value.strip() != str(args.expected_chapter):
                raise RuntimeError("Filled chapter number verification failed")
            if title_value.strip() != chapter_title:
                raise RuntimeError("Filled title verification failed")
            if "".join(editor_text.split()) != "".join(body.split()):
                raise RuntimeError("Filled body verification failed")
            log_data["filled"] = True
            log_data["filled_sha256"] = filled_sha
            filled_screenshot = PUBLISH_LOG_DIR / f"{stamp}_chapter_{args.expected_chapter:03d}_filled.png"
            safe_screenshot(page, filled_screenshot, log_data, "filled_screenshot")

        if args.submit:
            dismiss_known_overlays(page)
            clicked = click_last_button_by_text(page, ["发布", "下一步"])
            if clicked is None:
                raise RuntimeError("Publish/next button not found")
            log_data["first_submit_click"] = clicked
            try:
                page.wait_for_load_state("networkidle", timeout=20000)
            except PlaywrightTimeoutError:
                pass
            page.wait_for_timeout(1500)
            modal = page.locator(".arco-modal-wrapper").last
            if modal.count():
                modal_text = modal.inner_text(timeout=10000)
                log_data["submit_modal_text_start"] = modal_text[:500]
                if select_ai_yes_if_present(modal):
                    log_data["ai_used_selected"] = True
                confirm_clicked = click_modal_primary(modal)
                if confirm_clicked is None:
                    raise RuntimeError("Confirm publish button not found")
                log_data["confirm_submit_click"] = confirm_clicked
                log_data["submitted"] = True
            else:
                second_clicked = click_last_button_by_text(page, ["确认发布", "确认提交", "提交", "发布", "确认", "确定"])
                if second_clicked:
                    log_data["second_submit_click"] = second_clicked
                    log_data["submitted"] = True
                elif clicked == "发布":
                    log_data["submitted"] = True
                else:
                    raise RuntimeError("Final publish confirmation button not found")
            page.wait_for_timeout(5000)
            submitted_screenshot = PUBLISH_LOG_DIR / f"{stamp}_chapter_{args.expected_chapter:03d}_submitted.png"
            safe_screenshot(page, submitted_screenshot, log_data, "submitted_screenshot")

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
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as exc:
        ensure_dirs()
        stamp = now_stamp()
        append_markdown_log(
            RUN_LOG,
            f"{stamp} safe publish failed before completion",
            [
                f"- Result: `failed`",
                f"- Error: `{type(exc).__name__}: {exc}`",
                "- Traceback:",
                "```text",
                traceback.format_exc().strip(),
                "```",
            ],
        )
        print("ERROR:", type(exc).__name__, exc, file=sys.stderr)
        raise SystemExit(1)
