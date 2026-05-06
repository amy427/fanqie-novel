from pathlib import Path
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


CHAPTER_PATH = Path(r"D:\fanqie-novel\daily_output\第024章_番茄发布版.txt")


def main():
    text = CHAPTER_PATH.read_text(encoding="utf-8").replace("\r\n", "\n")
    lines = text.split("\n")
    title = lines[0].strip()
    body = "\n".join(lines[1:]).strip()
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        page = browser.contexts[0].pages[-1]
        page.wait_for_load_state("domcontentloaded", timeout=15000)

        try:
            page.get_by_text("知道了", exact=True).click(timeout=3000)
        except PlaywrightTimeoutError:
            pass

        title_input = page.locator("input[placeholder='请输入标题']").first
        title_input.click(timeout=10000)
        title_input.fill(title)

        editor = page.locator("[contenteditable='true']").filter(has_text="请输入正文").first
        if editor.count() == 0:
            editor = page.locator("[contenteditable='true']").first
        editor.click(timeout=10000)
        editor.fill(body)

        page.wait_for_timeout(1000)
        title_value = title_input.input_value()
        editor_text = editor.inner_text(timeout=10000)
        print("TITLE_SET:", title_value)
        print("BODY_CHARS:", len(editor_text.replace("\n", "")))
        print("BODY_START:", editor_text[:80].replace("\n", "\\n"))
        print("URL:", page.url)
        browser.close()


if __name__ == "__main__":
    main()
