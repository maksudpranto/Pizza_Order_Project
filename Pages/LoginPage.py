from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.username_inputbox = page.locator("//input[@id='user']")
        self.password_inputbox = page.locator("//input[@id='password']")
        self.login_button = page.locator("//button[@id='login']")

    def title_verify(self):
        actual_title = self.page.title()
        expected_title = "Login"

    def Login(self):
        self.username_inputbox.fill("admin")
        self.password_inputbox.fill("admin")
        self.login_button.click()


