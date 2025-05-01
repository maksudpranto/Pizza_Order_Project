from playwright.sync_api import Page

class PizzaSelection:
    def __init__(self,page: Page):
        self.page = page

        #Locators
        self.pizza_size = page.locator("//input[@id='rad_medium']")
        self.pizza_flavor = page.get_by_label("Pizza Flavor")
        self.pizza_sauce = page.get_by_label("Barbeque")
        self.pizza_toppings = page.get_by_label("Onions")
        self.pizza_quantity_click = page.get_by_placeholder("How many pizza you want?")
        self.pizza_quantity_fill = page.get_by_placeholder("How many pizza you want?")
        self.add_to_cart_button =  page.get_by_role("button", name="Add to Cart")

    def select_pizza(self):
        self.pizza_size.click()
        self.pizza_flavor.select_option("Pepperoni")
        self.pizza_sauce.check()
        self.pizza_toppings.click()
        self.pizza_quantity_click.click()
        self.pizza_quantity_fill.fill("3")
        self.add_to_cart_button.click()
