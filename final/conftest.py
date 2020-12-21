import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help='Choose language for the browser: ru, en-GB, es, fr.')

    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language").lower()
    if user_language == "en-gb":
        user_language = "en"
    browser_name = request.config.getoption("browser_name")

    if user_language not in ['ru', 'en', 'es', 'fr']:
        raise pytest.UsageError(f"Wrong language selected: {user_language} not in: ['ru', 'en-GB', 'es', 'fr']."
                                f"Choose language for the browser: ru, en-GB, es, fr.")

    if browser_name not in ["chrome", "firefox"]:
        raise pytest.UsageError(f"Wrong browser selected: {browser_name} not in: ['chrome', 'firefox']."
                                f"Choose browser: chrome or firefox")

    if browser_name == "chrome":
        browser = chrome_options(user_language)

    else:
        browser = firefox_options(user_language)

    browser.user_language = user_language

    yield browser

    browser.quit()


def chrome_options(language):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    return webdriver.Chrome(options=options)


def firefox_options(language):
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", language)

    return webdriver.Firefox(firefox_profile=fp)
