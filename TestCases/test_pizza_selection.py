from Pages.pizza_selection import PizzaSelection
from Pages.LoginPage import *

def test_pizza_selection(setup_teardown):
    page = setup_teardown
    login = LoginPage(page)
    login.Login()

    pizza_selection = PizzaSelection(page)
    pizza_selection.select_pizza()

