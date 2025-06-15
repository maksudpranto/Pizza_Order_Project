from Pages.pizza_selection import PizzaSelection
from Pages.LoginPage import *

def test_pizza_selection(setup_teardown):
    page = setup_teardown
    page.goto('https://play1.automationcamp.ir/login.html')
    login = LoginPage(page)
    login.Login()

    pizza_selection = PizzaSelection(page)
    pizza_selection.select_pizza()

