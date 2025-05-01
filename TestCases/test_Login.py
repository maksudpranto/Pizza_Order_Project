from playwright.sync_api import Page
from Pages.LoginPage import LoginPage

def test_loginPage_title_verify(setup_teardown):
    page = setup_teardown

    homeTitleVerify = LoginPage(page)
    homeTitleVerify.title_verify()


def test_performLogin(setup_teardown):
    page = setup_teardown
    login = LoginPage(page)
    login.Login()

def test_LoginValidation(setup_teardown):
    page = setup_teardown
    titleVerify_afterLogin = LoginPage(page)
    titleVerify_afterLogin.validateLogin()
