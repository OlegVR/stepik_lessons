import pytest
import time

from .pages.main_page import MainPage
from .pages.search_page import SearchPage
from .pages.product_page import ProductPage
from .user_authorization_setup import user_autorization_setup


name_product = "The shellcoder's handbook"


class TestSearchPageRegistredUser:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.main_link = "http://selenium1py.pythonanywhere.com/"
        user_autorization_setup(browser, self.main_link)

    def test_go_to_product_page_from_search_page(self, browser):
        # Arrange
        main_page = MainPage(browser, browser.current_url)
        main_page.open()
        main_page.search_product(name_product)

        # Act
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        search_page = SearchPage(browser, browser.current_url)
        search_page.go_to_found_product_page()
        product_page = ProductPage(browser, browser.current_url)

        # Assert
        product_page.check_of_all_elements_on_product_page()
        product_page.check_name_product_on_the_page(name_product)
