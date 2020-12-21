from .base_page import BasePage
from .locators import AllProductsPageLocators


class AllProductsPage(BasePage):

    def is_page_all_products(self, header_text):
        header_in_page = self.browser.find_element(*AllProductsPageLocators.HEADER_ALL_PRODUCTS_PAGE).text

        assert header_text in header_in_page, \
            f"The title:-> {header_text} doesn't match the title on the page:-> {header_in_page}"

    def add_first_product_on_the_page(self):
        first_product_button = self.browser.find_element(*AllProductsPageLocators.FIRST_PRODUCT_ADD_TO_BASKET)
        first_product_button.click()

    def should_be_success_message_product_add_to_basket(self):

        assert self.is_element_present(*AllProductsPageLocators.ADD_TO_BASKET_NAME_PRODUCT), \
            "There is no message about the successful addition of the product to the basket"

    def is_product_in_succes_message_add_to_basket(self):
        first_product_name = self.browser.find_element(*AllProductsPageLocators.FIRST_PRODUCT_NAME).text
        product_name_in_message = self.browser.find_element(*AllProductsPageLocators.ADD_TO_BASKET_NAME_PRODUCT).text

        assert first_product_name in product_name_in_message, \
            "The names of products added to the basket do not match"

    def should_be_button_checkout(self):

        assert self.is_element_present(*AllProductsPageLocators.BUTTON_CHECKOUT), \
            "There is no button to checkout"

    def should_not_be_success_message_add_product_to_basket(self):
        assert self.is_not_element_present(*AllProductsPageLocators.ADD_TO_BASKET_NAME_PRODUCT), \
            "Success message is presented, but should not be"

