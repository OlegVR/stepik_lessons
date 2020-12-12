from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_empty_basket(self):
        is_product_in_the_basket = self.is_element_present(*BasketPageLocators.PRODUCT_IN_THE_BASKET)

        assert not is_product_in_the_basket, "Basket must be empty"

    def message_in_empty_basket(self, message):
        assert message in self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET).text, \
            f"No message:{message} on the page basket"
