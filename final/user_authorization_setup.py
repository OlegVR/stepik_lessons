from .data import USER_LOGIN_DICT
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


def user_autorization_setup(browser, main_link):
    email = USER_LOGIN_DICT["email"]
    password = USER_LOGIN_DICT["password"]

    main_page = MainPage(browser, main_link)
    main_page.open()
    main_page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.authorizing_an_existing_user(email, password)

    login_page.should_be_authorized_user()