from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):

        assert "login" in self.browser.current_url, "The link is missing a string 'login'"

    def should_be_login_form(self):

        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "There is no login form on the page"

    def should_be_register_form(self):

        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "There is no registration form on the page"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL_REGISTER)
        email_input.send_keys(email)

        password_input = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD_REGISTER)
        password_input.send_keys(password)

        password_replay = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD_REPLY_REGISTER)
        password_replay.send_keys(password)

        button_register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button_register.click()

    def authorizing_an_existing_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL_AUTHOR)
        email_input.send_keys(email)

        password_input = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD_AUTHOR)
        password_input.send_keys(password)

        button_authorization = self.browser.find_element(*LoginPageLocators.BUTTON_LOGIN_AUTHOR)
        button_authorization.click()

    def should_be_message_of_successful_authorization(self):

        assert self.is_element_present(*LoginPageLocators.MESSAGE_SUCCESSFUL_AUTHORIZATION),\
            "No message about successful authorization"
