from selenium import webdriver
import time


def test_new_user_registration():
    search_text = "Спасибо за регистрацию!"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        browser.find_element_by_css_selector(search_button_login_or_registration_in_main_page_locator).click()

        # Act
        search_input_new_user_email = browser.find_element_by_css_selector(
            search_input_new_user_email_locator
        )
        search_input_new_user_email.send_keys(user_email)

        search_input_new_user_password = browser.find_element_by_css_selector(
            search_input_new_user_password_locator
        )
        search_input_new_user_password.send_keys(user_password)

        search_input_repeat_password_new_user = browser.find_element_by_css_selector(
            search_input_repeat_password_new_user_locator
        )
        search_input_repeat_password_new_user.send_keys(user_password)
        browser.find_element_by_css_selector(search_button_registration_locator).click()

        # Assert
        search_thank_you_text = browser.find_element_by_css_selector(search_thank_you_text_locator).text
        assert search_text in search_thank_you_text, "Registration page must contain the message of successful " \
                                                     "user registration."
        print("Successfully passed the first test!")

    finally:
        time.sleep(5)
        browser.quit()


def test_log_in_as_a_registered_user():
    search_text = "Рады видеть вас снова"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(login_and_registration_page_link)

        # Act
        search_input_email_registered_user = browser.find_element_by_css_selector(
            search_input_email_registered_user_locator
        )
        search_input_email_registered_user.send_keys(user_email)

        search_input_password_registered_user = browser.find_element_by_css_selector(
            search_input_password_registered_user_locator
        )
        search_input_password_registered_user.send_keys(user_password)
        browser.find_element_by_css_selector(search_button_login_registered_user_locator).click()

        # Assert
        search_thank_you_text = browser.find_element_by_css_selector(search_thank_you_text_locator).text
        assert search_text in search_thank_you_text, "Login page must contain a successful login message"
        print("Successfully passed the second test")

    finally:
        time.sleep(5)
        browser.quit()


if __name__ == "__main__":
    main_page_link = "http://selenium1py.pythonanywhere.com/ru/"
    login_and_registration_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    search_thank_you_text_locator = "div.alertinner.wicon"

    user_password = "chupakabra124c"
    user_email = "chupakabra6@au.nyam"

    search_button_login_or_registration_in_main_page_locator = "#login_link"
    search_input_new_user_email_locator = "input[name='registration-email']"
    search_input_new_user_password_locator = "input[name='registration-password1']"
    search_input_repeat_password_new_user_locator = "input[name='registration-password2']"
    search_button_registration_locator = "button[name='registration_submit']"

    search_input_email_registered_user_locator = "input[name='login-username']"
    search_input_password_registered_user_locator = "input[name='login-password']"
    search_button_login_registered_user_locator = "button[name='login_submit']"

    test_new_user_registration()
    test_log_in_as_a_registered_user()
