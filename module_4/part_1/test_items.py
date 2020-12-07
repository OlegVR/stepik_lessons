CORRECT_LANGUAGES_DICT = {
    "ru": "Добавить в корзину",
    "es": "Añadir al carrito",
    "fr": "Ajouter au panier",
    "en-gb": "Add to basket"
}


def test_whether_the_add_product_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(5)
    browser.get(link)

    text_button = browser.find_element_by_css_selector("button.btn.btn-add-to-basket").text
    language = browser.find_element_by_css_selector("option[selected]").get_attribute("value")

    assert CORRECT_LANGUAGES_DICT[language] in text_button,\
        f"The search text: {CORRECT_LANGUAGES_DICT[language]} not in the text: {text_button}"
