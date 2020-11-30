CORRECT_LANGUAGES_DICT = {
    "ru": "Добавить в корзину","ar": "إضافة إلى السلة", "ca": "Afegir a la cistella",
    "cs": "Přidat do košíku", "da": "Tilføj til kurv", "de": "In den Warenkorb legen",
    "en-gb": "Add to basket", "el": "Προσθήκη στο καλάθι", "es": "Añadir al carrito",
    "fi": "Lisää ostoskoriin", "fr": "Ajouter au panier", "it": "Aggiungi al carrello",
    "ko": "장바구니에 추가하기", "nl": "Toevoegen aan Carter", "pl": "Dodaj do karteru",
    "pt": "Adicionar ao Cárter", "pt-br": "Adicionar ao Cárter", "ro": "Adaugă la cutie",
    "sk": "Pridať do kľukovej skrine", "uk": "Додати в кошик", "sh-hans": "Lägg i kundvagnen"
}


def test_whether_the_add_product_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(5)
    browser.get(link)

    text_button = browser.find_element_by_css_selector("button[class='btn btn-lg btn-primary btn-add-to-basket']").text
    language = browser.find_element_by_css_selector("option[selected]").get_attribute("value")

    assert CORRECT_LANGUAGES_DICT[language] in text_button,\
        f"The search text: {CORRECT_LANGUAGES_DICT[language]} not in the text: {text_button}"
