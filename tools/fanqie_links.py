from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        page = browser.contexts[0].pages[-1]
        links = page.locator("a").evaluate_all(
            """els => els.map((el, i) => ({
                i,
                text: (el.innerText || el.textContent || '').trim(),
                href: el.href,
                visible: !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length)
            }))"""
        )
        for link in links:
            print(link)
        browser.close()


if __name__ == "__main__":
    main()
