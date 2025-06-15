from Pages.LoginPage import LoginPage

def test_loginPage_title_verify(setup_teardown):
    page = setup_teardown
    page.goto('https://play1.automationcamp.ir/login.html')
    homeTitleVerify = LoginPage(page)
    homeTitleVerify.title_verify()


def test_performLogin(setup_teardown):
    page = setup_teardown
    page.goto('https://play1.automationcamp.ir/login.html')
    login = LoginPage(page)
    login.Login()

def test_LoginValidation(setup_teardown):
    page = setup_teardown
    page.goto('https://play1.automationcamp.ir/login.html')
    titleVerify_afterLogin = LoginPage(page)
    titleVerify_afterLogin.validateLogin()

