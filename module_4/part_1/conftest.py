import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from module_4.language_data import CORRECT_LANGUAGES_DICT


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help='Choose language for the browser: ru, en-GB, es, fr')


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    if user_language not in CORRECT_LANGUAGES_DICT:
        raise pytest.UsageError(f"Wrong language selected: {user_language} not in: ['ru', 'en-GB', 'es', 'fr']")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
