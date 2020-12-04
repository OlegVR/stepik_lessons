from selenium import webdriver


def test_new_user_registration():
    search_text = "Спасибо за регистрацию!"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page_link)

        browser.find_element_by_css_selector(button_login_or_registration).click()

        # Act
        input_email = browser.find_element_by_css_selector(input_email_locator)
        input_email.send_keys(user_email)

        input_password = browser.find_element_by_css_selector(input_password_locator)
        input_password.send_keys(user_password)

        input_repeat_password = browser.find_element_by_css_selector(input_repeat_password_locator)
        input_repeat_password.send_keys(user_password)

        browser.find_element_by_css_selector(button_registration_locator).click()

        # Assert
        success_login_msg_text = browser.find_element_by_css_selector(success_login_msg_text_locator).text
        assert search_text in success_login_msg_text, "Registration page must contain the message of successful " \
                                                     "user registration."
        print("Successfully passed the first test!")

    finally:
        browser.quit()


def test_log_in_as_a_registered_user():
    search_text = "Рады видеть вас снова"

    try:
        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(login_and_registration_page_link)

        # Act
        input_email_registered = browser.find_element_by_css_selector(input_email_registered_locator)
        input_email_registered.send_keys(user_email)

        input_password_registered = browser.find_element_by_css_selector(input_password_registered_locator)
        input_password_registered.send_keys(user_password)

        browser.find_element_by_css_selector(button_login_registered_locator).click()

        # Assert
        success_login_msg_text = browser.find_element_by_css_selector(success_login_msg_text_locator).text
        assert search_text in success_login_msg_text, "Login page must contain a successful login message"
        print("Successfully passed the second test")

    finally:
        browser.quit()


if __name__ == "__main__":
    main_page_link = "http://selenium1py.pythonanywhere.com/ru/"
    login_and_registration_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    success_login_msg_text_locator = "div.alertinner.wicon"

    user_password = "chupakabra124c"
    user_email = "chupakabra10@au.nyam"

    button_login_or_registration = "#login_link"
    input_email_locator = "input[name='registration-email']"
    input_password_locator = "input[name='registration-password1']"
    input_repeat_password_locator = "input[name='registration-password2']"
    button_registration_locator = "button[name='registration_submit']"

    input_email_registered_locator = "input[name='login-username']"
    input_password_registered_locator = "input[name='login-password']"
    button_login_registered_locator = "button[name='login_submit']"

    test_new_user_registration()
    test_log_in_as_a_registered_user()
