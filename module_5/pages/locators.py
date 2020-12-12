from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_PASSWORD_REPLY = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "[name=registration_submit]")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    COST_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    SUBMIT_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages > :nth-child(1)")
    NAME_PRODUCT_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > :nth-child(1) strong")
    MESSAGE_COST_IN_BASKET = (By.CSS_SELECTOR, "#messages > :nth-child(3)")
    COST_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > :nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > :nth-child(1)")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group>:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
    PRODUCT_IN_THE_BASKET = (By.CSS_SELECTOR, ".basket-items")
