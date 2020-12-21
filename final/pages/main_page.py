from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def go_to_all_products_page(self):
        button_all_product_page = self.browser.find_element(*MainPageLocators.ALL_PRODUCTS_LINK)
        button_all_product_page.click()
