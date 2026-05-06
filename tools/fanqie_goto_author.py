from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        context = browser.contexts[0]
        page = context.pages[-1] if context.pages else context.new_page()
        page.goto("https://fanqienovel.com/author", wait_until="domcontentloaded", timeout=45000)
        print("URL:", page.url)
        print("TITLE:", page.title())
        browser.close()


if __name__ == "__main__":
    main()
