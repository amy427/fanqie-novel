from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


def main():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        page = browser.contexts[0].pages[-1]
        page.wait_for_load_state("domcontentloaded", timeout=15000)

        modal = page.locator(".arco-modal-wrapper").filter(has_text="发布设置").last
        # The platform asks whether AI was used. Select "是" honestly.
        yes_text = modal.get_by_text("是", exact=True)
        if yes_text.count():
            yes_text.first.click(timeout=10000)

        confirm = modal.get_by_role("button", name="确认发布")
        if confirm.count() == 0:
            confirm = modal.get_by_text("确认发布", exact=True)
        confirm.last.click(timeout=15000)

        try:
            page.wait_for_load_state("networkidle", timeout=30000)
        except PlaywrightTimeoutError:
            pass
        page.wait_for_timeout(5000)

        print("URL:", page.url)
        print("TITLE:", page.title())
        print("BODY:", page.locator("body").inner_text(timeout=15000)[:4000])
        browser.close()


if __name__ == "__main__":
    main()
