from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators

class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)

        except NoSuchElementException:
            return False

        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))

        except TimeoutException:
            return True

        return False

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_authorized_user(self):

        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def go_to_basket(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def search_product(self, name_product):
        input_menu_search = self.browser.find_element(*BasePageLocators.SEARCH_PRODUCT_MENU)
        button_search = self.browser.find_element(*BasePageLocators.BUTTON_SEARCH_PRODUCT)

        input_menu_search.send_keys(name_product)
        button_search.click()
