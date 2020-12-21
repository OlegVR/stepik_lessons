import pytest
import time

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.search_page import SearchPage
from .pages.all_products_page import AllProductsPage
from .data import USER_LOGIN_DICT
from .data import NAMES_SEARCH_PRODUCTS_LIST
from .data import ALL_PRODUCTS_PAGE_DICT


class TestMainPageAuthorizationAndRegistration:

    def test_should_be_rigister_and_authorization_page(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/"

        # Arrange
        main_page = MainPage(browser, link)
        main_page.open()

        # Act
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)

        # Assert
        login_page.should_be_register_form()

    def test_register_new_user_in_main_page(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/"
        email = f"{time.time()}@fals.ru"
        password = "secretpassword198898990"

        # Arrange
        main_page = MainPage(browser, link)
        main_page.open()

        # Act
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email, password)

        # Assert
        login_page.should_be_authorized_user()
        login_page.should_be_message_of_successful_authorization()

    def test_authorizing_an_existing_user_in_main_page(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/"
        email = USER_LOGIN_DICT["email"]
        password = USER_LOGIN_DICT["password"]

        # Arrange
        main_page = MainPage(browser, link)
        main_page.open()

        # Act
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.authorizing_an_existing_user(email, password)

        # Assert
        login_page.should_be_authorized_user()
        login_page.should_be_message_of_successful_authorization()


class TestMainPageSearchProducts:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Data
        self.main_link = "http://selenium1py.pythonanywhere.com/"
        email = USER_LOGIN_DICT["email"]
        password = USER_LOGIN_DICT["password"]

        # Arrange
        main_page = MainPage(browser, self.main_link)
        main_page.open()
        main_page.go_to_login_page()

        # Act
        login_page = LoginPage(browser, browser.current_url)
        login_page.authorizing_an_existing_user(email, password)

        # Assert
        login_page.should_be_authorized_user()

    @pytest.mark.parametrize('name_product', NAMES_SEARCH_PRODUCTS_LIST)
    def test_search_product(self, browser, name_product):
        # Arrange
        main_page = MainPage(browser, self.main_link)
        main_page.open()

        # Act
        main_page.search_product(name_product)
        search_page = SearchPage(browser, browser.current_url)

        # Assert
        search_page.is_found_product_in_page()
        search_page.check_name_found_product(name_product)
        search_page.should_be_button_to_basket()


class TestMainPageAllProduct:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Data
        self.main_link = "http://selenium1py.pythonanywhere.com/"
        email = USER_LOGIN_DICT["email"]
        password = USER_LOGIN_DICT["password"]

        # Arrange
        main_page = MainPage(browser, self.main_link)
        main_page.open()
        main_page.go_to_login_page()

        # Act
        login_page = LoginPage(browser, browser.current_url)
        login_page.authorizing_an_existing_user(email, password)

        # Assert
        login_page.should_be_authorized_user()

    def test_can_go_to_all_products_page(self, browser):
        # Data
        language = browser.user_language
        header_page = ALL_PRODUCTS_PAGE_DICT[language]

        # Arrange
        main_page = MainPage(browser, self.main_link)
        main_page.open()

        # Act
        main_page.go_to_all_products_page()
        product_page = AllProductsPage(browser, browser.current_url)

        # Assert
        product_page.is_page_all_products(header_page)
