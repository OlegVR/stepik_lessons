import pytest

from .pages.main_page import MainPage
from .pages.all_products_page import AllProductsPage
from .user_authorization_setup import user_autorization_setup


class TestAllProductsPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.main_link = "http://selenium1py.pythonanywhere.com/"
        user_autorization_setup(browser, self.main_link)

    def test_is_not_be_success_message_add_product_to_basket(self, browser):
        # Arrange
        main_page = MainPage(browser, self.main_link)
        main_page.open()

        # Act
        main_page.go_to_all_products_page()
        products_page = AllProductsPage(browser, browser.current_url)

        # Assert
        products_page.should_not_be_success_message_add_product_to_basket()

    def test_add_first_product_to_basket(self, browser):
        # Arrange
        main_page = MainPage(browser, self.main_link)
        main_page.open()

        # Act
        main_page.go_to_all_products_page()
        product_page = AllProductsPage(browser, browser.current_url)
        product_page.add_first_product_on_the_page()

        # Assert
        product_page.should_be_success_message_product_add_to_basket()
        product_page.is_product_in_succes_message_add_to_basket()
        product_page.should_be_button_checkout()
