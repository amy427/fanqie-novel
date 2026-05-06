from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


PUBLISH_URL = "https://fanqienovel.com/main/writer/7628203489469942846/publish/?enter_from=newchapter_0"


def main():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9222")
        page = browser.contexts[0].pages[-1]
        page.goto(PUBLISH_URL, wait_until="domcontentloaded", timeout=45000)
        try:
            page.wait_for_load_state("networkidle", timeout=15000)
        except PlaywrightTimeoutError:
            pass
        print("URL:", page.url)
        print("TITLE:", page.title())
        browser.close()


if __name__ == "__main__":
    main()
