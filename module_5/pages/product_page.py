from .base_page import BasePage
from .locators import ProductPageLoctors


class ProductPage(BasePage):
    def add_product_to_the_bascket(self):
        product_name = self.browser.find_element(*ProductPageLoctors.PRODUCT_NAME).text
        cost_product = self.browser.find_element(*ProductPageLoctors.COST_PRODUCT).text

        self.browser.find_element(*ProductPageLoctors.SUBMIT_ADD_TO_BASKET).click()

        self.solve_quiz_and_get_code()
        self.should_add_to_basket_message()
        self.check_is_product_in_message(product_name)
        self.should_message_cost_of_a_basket()
        self.check_cost_product_in_message(cost_product)

    def should_add_to_basket_message(self):
        assert self.is_element_present(*ProductPageLoctors.ADD_TO_BASKET_MESSAGE), \
            'The page does not contain the message adding an item to the cart'

    def check_is_product_in_message(self, product_name):
        assert product_name == self.browser.find_element(*ProductPageLoctors.NAME_PRODUCT_IN_MESSAGE).text, \
            "Product names don't match"

    def should_message_cost_of_a_basket(self):
        assert self.is_element_present(*ProductPageLoctors.MESSAGE_COST_IN_BASKET), \
            "No message about the cost of the shopping cart"

    def check_cost_product_in_message(self, cost_product):
        assert cost_product == self.browser.find_element(*ProductPageLoctors.COST_IN_MESSAGE).text, \
            "The cost of the product in the message does not match"
