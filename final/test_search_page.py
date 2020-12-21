import pytest
import time

from .pages.main_page import MainPage
from .pages.search_page import SearchPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .data import USER_LOGIN_DICT


name_product = "The shellcoder's handbook"


class TestSearchPageRegistredUser:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Data
        self.main_link = "http://selenium1py.pythonanywhere.com/"
        email = USER_LOGIN_DICT['email']
        password = USER_LOGIN_DICT['password']

        # Arrange
        main_page = MainPage(browser, self.main_link)
        main_page.open()
        main_page.go_to_login_page()

        # Act
        login_page = LoginPage(browser, browser.current_url)
        login_page.authorizing_an_existing_user(email, password)

        # Assert
        main_page.should_be_authorized_user()

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
