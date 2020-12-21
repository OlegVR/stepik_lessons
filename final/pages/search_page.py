from .base_page import BasePage
from  .locators import SearchPageLocators


class SearchPage(BasePage):
    def is_found_product_in_page(self):

        assert self.is_element_present(*SearchPageLocators.NAME_FOUND_PRODUCT), \
            "The product was not found, but should be"

    def check_name_found_product(self, name_product):
        name_found_product = self.browser.find_element(*SearchPageLocators.NAME_FOUND_PRODUCT).text

        assert name_product == name_found_product, \
            "The product names didn't match"

    def go_to_found_product_page(self):
        name_found_product = self.browser.find_element(*SearchPageLocators.NAME_FOUND_PRODUCT).text

        link_found_product = self.browser.find_element_by_link_text(name_found_product)
        link_found_product.click()

    def should_be_button_to_basket(self):

        assert self.is_element_present(*SearchPageLocators.BUTTON_ADD_PRODUCT_TO_BASKET), \
            "There is no button to add an item to the basket"
