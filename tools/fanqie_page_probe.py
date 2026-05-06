from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        contexts = browser.contexts
        pages = []
        for context in contexts:
            pages.extend(context.pages)
        if not pages:
            print("NO_PAGES")
            return
        page = pages[-1]
        page.wait_for_load_state("domcontentloaded", timeout=15000)
        print("URL:", page.url)
        print("TITLE:", page.title())
        items = page.locator("input, textarea, [contenteditable='true'], button, a").evaluate_all(
            """els => els.slice(0, 80).map((el, i) => ({
                i,
                tag: el.tagName,
                type: el.getAttribute('type') || '',
                text: (el.innerText || el.textContent || el.getAttribute('placeholder') || el.getAttribute('aria-label') || '').trim().slice(0, 80),
                placeholder: (el.getAttribute('placeholder') || '').slice(0, 80),
                aria: (el.getAttribute('aria-label') || '').slice(0, 80),
                role: (el.getAttribute('role') || '').slice(0, 40),
                editable: el.getAttribute('contenteditable') || '',
                visible: !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length)
            }))"""
        )
        for item in items:
            print(item)
        browser.close()


if __name__ == "__main__":
    main()
