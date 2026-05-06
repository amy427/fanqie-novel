from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


def main():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        page = browser.contexts[0].pages[-1]
        page.wait_for_load_state("domcontentloaded", timeout=15000)

        inputs = page.locator("input")
        chapter_no = inputs.nth(0)
        chapter_no.click(timeout=10000)
        chapter_no.fill("24")

        title = page.locator("input[placeholder='请输入标题']").first
        title.click(timeout=10000)
        title.fill("轮到你进名单了")

        buttons = page.get_by_role("button", name="下一步")
        if buttons.count() == 0:
            print("NEXT_NOT_FOUND")
            return
        buttons.nth(buttons.count() - 1).click(timeout=15000)
        try:
            page.wait_for_load_state("networkidle", timeout=20000)
        except PlaywrightTimeoutError:
            pass
        page.wait_for_timeout(2500)

        print("URL:", page.url)
        print("TITLE:", page.title())
        body = page.locator("body").inner_text(timeout=10000)
        print(body[:2500])
        browser.close()


if __name__ == "__main__":
    main()
