from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        page = browser.contexts[0].pages[-1]
        modals = page.locator(".arco-modal-wrapper, [role='dialog']").evaluate_all(
            """els => els.map((el, i) => ({
                i,
                text: (el.innerText || el.textContent || '').trim().slice(0, 3000),
                visible: !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length)
            }))"""
        )
        for modal in modals:
            print(modal)
        buttons = page.locator(".arco-modal-wrapper button, [role='dialog'] button").evaluate_all(
            """els => els.map((el, i) => ({
                i,
                text: (el.innerText || el.textContent || '').trim(),
                visible: !!(el.offsetWidth || el.offsetHeight || el.getClientRects().length)
            }))"""
        )
        print("MODAL_BUTTONS")
        for button in buttons:
            print(button)
        browser.close()


if __name__ == "__main__":
    main()
