import time
import math
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize("link", ["https://stepik.org/lesson/236895/step/1",
                                  "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1",
                                  "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1",
                                  "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"])
def test_link_inoplanet_stepik(browser, link):
    search_text = "Correct!"
    browser.implicitly_wait(5)
    browser.get(link)
    input_text = browser.find_element_by_css_selector(".textarea")
    answer = math.log(int(time.time()))
    input_text.send_keys(str(answer))
    browser.find_element_by_css_selector(".submit-submission").click()
    find_text = browser.find_element_by_css_selector(".smart-hints__hint").text
    assert search_text in find_text, f"{search_text} not in {find_text}"
