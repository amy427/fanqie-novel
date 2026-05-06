from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


def main():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        page = browser.contexts[0].pages[-1]
        page.wait_for_load_state("domcontentloaded", timeout=15000)
        try:
            page.get_by_text("已保存到云端").wait_for(timeout=30000)
            print("SAVE_STATUS: 已保存到云端")
        except PlaywrightTimeoutError:
            print("SAVE_STATUS: 未等到已保存到云端，继续尝试")
        buttons = page.get_by_role("button", name="下一步")
        print("NEXT_COUNT:", buttons.count())
        if buttons.count():
            buttons.nth(buttons.count() - 1).click(timeout=15000)
        try:
            page.wait_for_load_state("networkidle", timeout=20000)
        except PlaywrightTimeoutError:
            pass
        page.wait_for_timeout(3000)
        print("URL:", page.url)
        body = page.locator("body").inner_text(timeout=10000)
        print(body[:2500])
        browser.close()


if __name__ == "__main__":
    main()
