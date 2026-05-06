from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


def main():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        page = browser.contexts[0].pages[-1]
        page.wait_for_load_state("domcontentloaded", timeout=15000)
        target = page.get_by_text("创建章节", exact=True).first
        target.click(timeout=15000)
        try:
            page.wait_for_load_state("networkidle", timeout=15000)
        except PlaywrightTimeoutError:
            pass
        print("URL:", page.url)
        print("TITLE:", page.title())
        browser.close()


if __name__ == "__main__":
    main()
