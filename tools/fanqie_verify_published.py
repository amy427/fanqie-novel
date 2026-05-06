from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


def main():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        page = browser.contexts[0].pages[-1]
        try:
            page.wait_for_load_state("networkidle", timeout=20000)
        except PlaywrightTimeoutError:
            pass
        text = page.locator("body").inner_text(timeout=15000)
        markers = [
            "第24章",
            "轮到你进名单了",
            "审核",
            "已发布",
            "待审核",
            "草稿",
        ]
        print("URL:", page.url)
        print("TITLE:", page.title())
        for marker in markers:
            print(f"HAS_{marker}:", marker in text)
        idx = text.find("第24章")
        if idx == -1:
            idx = text.find("轮到你进名单了")
        snippet = text[max(0, idx - 300): idx + 700] if idx != -1 else text[:1000]
        print("SNIPPET_START")
        print(snippet.encode("utf-8", errors="replace").decode("utf-8", errors="replace"))
        print("SNIPPET_END")
        browser.close()


if __name__ == "__main__":
    main()
