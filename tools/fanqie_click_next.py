from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


def main():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        page = browser.contexts[0].pages[-1]
        page.wait_for_load_state("domcontentloaded", timeout=15000)
        buttons = page.get_by_role("button", name="下一步")
        count = buttons.count()
        if count == 0:
            print("NEXT_NOT_FOUND")
            return
        buttons.nth(count - 1).click(timeout=15000)
        try:
            page.wait_for_load_state("networkidle", timeout=20000)
        except PlaywrightTimeoutError:
            pass
        page.wait_for_timeout(1500)
        print("URL:", page.url)
        print("TITLE:", page.title())
        visible_buttons = page.locator("button").evaluate_all(
            """els => els.filter(el => !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length))
                .map((el, i) => ({i, text: (el.innerText || el.textContent || '').trim().slice(0, 80)}))"""
        )
        for button in visible_buttons:
            print(button)
        browser.close()


if __name__ == "__main__":
    main()
