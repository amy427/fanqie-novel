from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        page = browser.contexts[0].pages[-1]
        title_values = page.locator("input").evaluate_all(
            """els => els.map((el, i) => ({
                i,
                placeholder: el.getAttribute('placeholder') || '',
                value: el.value || '',
                visible: !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length)
            }))"""
        )
        editors = page.locator("[contenteditable='true']").evaluate_all(
            """els => els.map((el, i) => ({
                i,
                text: (el.innerText || el.textContent || '').slice(0, 200),
                chars: (el.innerText || el.textContent || '').replace(/\\s/g, '').length,
                visible: !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length)
            }))"""
        )
        print("INPUTS")
        for item in title_values:
            print(item)
        print("EDITORS")
        for item in editors:
            print(item)
        browser.close()


if __name__ == "__main__":
    main()
