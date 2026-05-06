from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


def visible_buttons(page):
    return page.locator("button").evaluate_all(
        """els => els.filter(el => !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length))
            .map((el, i) => ({i, text: (el.innerText || el.textContent || '').trim().slice(0, 80)}))"""
    )


def click_text(page, text, timeout=10000):
    loc = page.get_by_role("button", name=text)
    if loc.count() == 0:
        loc = page.get_by_text(text, exact=True)
    if loc.count() == 0:
        return False
    loc.last.click(timeout=timeout)
    return True


def main():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        page = browser.contexts[0].pages[-1]
        page.wait_for_load_state("domcontentloaded", timeout=15000)

        steps = []
        for _ in range(8):
            body = page.locator("body").inner_text(timeout=10000)
            buttons = visible_buttons(page)
            print("URL:", page.url)
            print("BUTTONS:", buttons)
            print("BODY_HEAD:", body[:1200])

            if "提交成功" in body or "发布成功" in body or "已发布" in body:
                steps.append("done")
                break

            clicked = False
            for text in ["提交", "确认提交", "确认", "确定", "发布", "下一步"]:
                if any(b["text"] == text or text in b["text"] for b in buttons):
                    click_text(page, text, timeout=15000)
                    steps.append(text)
                    clicked = True
                    try:
                        page.wait_for_load_state("networkidle", timeout=20000)
                    except PlaywrightTimeoutError:
                        pass
                    page.wait_for_timeout(2500)
                    break
            if not clicked:
                break

        print("STEPS:", steps)
        print("FINAL_URL:", page.url)
        print("FINAL_BODY:", page.locator("body").inner_text(timeout=10000)[:2500])
        browser.close()


if __name__ == "__main__":
    main()
