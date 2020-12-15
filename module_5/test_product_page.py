import pytest
import time

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .data import BASKET_EMPTY_MESSAGE_DICT


class TestProductPage:
    @pytest.mark.parametrize('link',
                             ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param(
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  marks=pytest.mark.xfail),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_guest_can_add_product_to_basket(self, browser, link):
        # Arrange
        page = ProductPage(browser, link)
        page.open()
        name_product = page.product_name_on_the_page()
        cost_product = page.cost_product_on_the_page()

        # Act
        page.add_product_to_the_bascket()
        page.solve_quiz_and_get_code()

        # Assert
        page.should_add_to_basket_message()
        page.check_is_product_in_message(name_product)
        page.should_message_cost_of_a_basket()
        page.check_cost_product_in_message(cost_product)

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.add_product_to_the_bascket()

        # Assert
        page.should_not_be_success_message()

    def test_quest_cant_see_success_message(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Assert
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.add_product_to_the_bascket()

        # Assert
        page.should_be_success_message()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Assert
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page (self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)

        # Assert
        login_page.should_be_login_form()
        login_page.should_be_register_form()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # Data
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)

        # Assert
        basket_page.is_empty_basket()
        basket_page.message_in_empty_basket(message=BASKET_EMPTY_MESSAGE_DICT['en'])


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Data
        login_link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        self.product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        email = f"{time.time()}@fakemail.org"
        password = "passnumber1"

        # Arrange
        page = LoginPage(browser, login_link)
        page.open()

        # Act
        page.register_new_user(email, password)

        # Assert
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        # Arrange
        page = ProductPage(browser, self.product_link)
        page.open()

        # Assert
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, self.product_link)
        page.open()
        name_product = page.product_name_on_the_page()
        cost_product = page.cost_product_on_the_page()

        # Act
        page.add_product_to_the_bascket()
        page.solve_quiz_and_get_code()

        # Assert
        page.should_add_to_basket_message()
        page.check_is_product_in_message(name_product)
        page.should_message_cost_of_a_basket()
        page.check_cost_product_in_message(cost_product)
