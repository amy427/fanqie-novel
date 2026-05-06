from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


def click_if_present(page, text):
    try:
        loc = page.get_by_text(text, exact=True).last
        if loc.count() > 0:
            loc.click(timeout=3000)
            page.wait_for_timeout(500)
            return True
    except Exception:
        return False
    return False


def main():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        page = browser.contexts[0].pages[-1]
        page.wait_for_load_state("domcontentloaded", timeout=15000)
        print("CLOSED_TIP:", click_if_present(page, "知道了"))
        buttons = page.get_by_role("button", name="下一步")
        print("NEXT_COUNT:", buttons.count())
        if buttons.count() > 0:
            buttons.nth(buttons.count() - 1).click(timeout=15000)
        try:
            page.wait_for_load_state("networkidle", timeout=20000)
        except PlaywrightTimeoutError:
            pass
        page.wait_for_timeout(2000)
        print("URL:", page.url)
        print("TITLE:", page.title())
        text = page.locator("body").inner_text(timeout=10000)
        print(text[:2000])
        browser.close()


if __name__ == "__main__":
    main()
