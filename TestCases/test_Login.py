from playwright.sync_api import Page
from Pages.LoginPage import LoginPage

def test_loginPage_title_verify(setup_teardown):
    page = setup_teardown

    homeTitleVerify = LoginPage(page)
    homeTitleVerify.title_verify()


