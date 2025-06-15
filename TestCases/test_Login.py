from Pages.LoginPage import LoginPage

def test_loginPage_title_verify(login_test_fixture):
    page = login_test_fixture
    homeTitleVerify = LoginPage(page)
    homeTitleVerify.title_verify()


def test_performLogin(login_test_fixture):
    page = login_test_fixture
    login = LoginPage(page)
    login.Login()

def test_LoginValidation(login_test_fixture):
    page = login_test_fixture
    titleVerify_afterLogin = LoginPage(page)
    titleVerify_afterLogin.validateLogin()

