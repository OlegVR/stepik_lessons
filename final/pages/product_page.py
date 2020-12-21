from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def product_name_on_the_page(self):

        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def cost_product_on_the_page(self):

        return self.browser.find_element(*ProductPageLocators.COST_PRODUCT).text

    def should_be_add_to_basket_button(self):

        assert self.is_element_present(*ProductPageLocators.SUBMIT_ADD_TO_BASKET), \
            'The page does not contain the message adding an item to the basket'

    def should_be_product_name_on_the_page(self):

        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), \
            "No product name on the page"

    def should_be_cost_product_on_the_page(self):

        assert self.is_element_present(*ProductPageLocators.COST_PRODUCT), \
            "No product cost per page"

    def should_be_product_description(self):

        assert self.is_element_present(*ProductPageLocators.DESCRIPTION_PRODUCT), \
            "No product description on the page"

    def should_be_product_reviews(self):

        assert self.is_element_present(*ProductPageLocators.PRODUCT_REVIEWS), \
            "There are no product reviews on the page"

    def check_of_all_elements_on_product_page(self):
        self.should_be_add_to_basket_button()
        self.should_be_cost_product_on_the_page()
        self.should_be_product_description()
        self.should_be_product_name_on_the_page()

    def check_name_product_on_the_page(self, name_product):

        assert name_product == self.product_name_on_the_page(), \
            "An item with the wrong name has been opened"
