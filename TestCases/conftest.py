import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='function')
def setup_teardown():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        # page.goto('https://play1.automationcamp.ir/login.html')
        yield page
        context.close()
        browser.close()





