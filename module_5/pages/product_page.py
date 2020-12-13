from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_the_bascket(self):
        button = self.browser.find_element(*ProductPageLocators.SUBMIT_ADD_TO_BASKET)
        button.click()

    def product_name_on_the_page(self):

        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def cost_product_on_the_page(self):

        return self.browser.find_element(*ProductPageLocators.COST_PRODUCT).text

    def should_add_to_basket_message(self):

        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), \
            'The page does not contain the message adding an item to the basket'

    def check_is_product_in_message(self, product_name):
        assert product_name == self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_MESSAGE).text, \
            "Product names don't match"

    def should_message_cost_of_a_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_COST_IN_BASKET), \
            "No message about the cost of the shopping basket"

    def check_cost_product_in_message(self, cost_product):
        assert cost_product == self.browser.find_element(*ProductPageLocators.COST_IN_MESSAGE).text, \
            "The cost of the product in the message does not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"
