from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group>:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    SEARCH_PRODUCT_MENU = (By.CSS_SELECTOR, "#id_q")
    BUTTON_SEARCH_PRODUCT = (By.CSS_SELECTOR, "input.btn.btn-default")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_EMAIL_REGISTER = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_PASSWORD_REGISTER = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_PASSWORD_REPLY_REGISTER = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTER = (By.CSS_SELECTOR, "[name=registration_submit]")
    MESSAGE_SUCCESSFUL_AUTHORIZATION = (By.CSS_SELECTOR, "div.alertinner.wicon") # Сообщение успешной авторизации
    INPUT_EMAIL_AUTHOR = (By.CSS_SELECTOR, "#id_login-username")
    INPUT_PASSWORD_AUTHOR = (By.CSS_SELECTOR, "#id_login-password")
    BUTTON_LOGIN_AUTHOR = (By.CSS_SELECTOR, "button[name='login_submit']")


class MainPageLocators:
    ALL_PRODUCTS_LINK = (By.CSS_SELECTOR, "ul[data-navigation='dropdown-menu'] > li:nth-child(1) a")


class AllProductsPageLocators:
    FIRST_PRODUCT_ADD_TO_BASKET= (By.CSS_SELECTOR, "ol.row > :nth-child(1) form button")
    FIRST_PRODUCT_NAME = (By.CSS_SELECTOR, "ol.row > :nth-child(1) h3 a")
    HEADER_ALL_PRODUCTS_PAGE = (By.CSS_SELECTOR, ".page-header h1")
    ADD_TO_BASKET_NAME_PRODUCT =(By.CSS_SELECTOR, "#messages > :nth-child(1) strong")
    BUTTON_CHECKOUT = (By.CSS_SELECTOR, "div.alertinner p:nth-child(2) a:nth-child(2)")

class SearchPageLocators:
    NAME_FOUND_PRODUCT = (By.CSS_SELECTOR, "article>h3>a") # Имя найденного товара
    BUTTON_ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, "button.btn.btn-primary") # Кнопка добавить продукт в корзину


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages > :nth-child(1)")
    COST_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    SUBMIT_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    DESCRIPTION_PRODUCT = (By.CSS_SELECTOR, "#product_description") # Описание продукта
    PRODUCT_REVIEWS = (By.CSS_SELECTOR, "#reviews") # Отзывы о продукте

