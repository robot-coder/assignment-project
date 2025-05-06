# mcp_interaction.py

import playwright
from playwright.sync_api import sync_playwright


def run_playwright_example(url):
    """
    Use Playwright to navigate to a URL and take a screenshot.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.screenshot(path='screenshot.png')
        browser.close()


if __name__ == '__main__':
    run_playwright_example('https://example.com')
