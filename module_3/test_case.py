import unittest
from selenium import webdriver


class TestForm1(unittest.TestCase):

    def test_first_page(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element_by_xpath("//input[@required and @placeholder='Input your first name']")
        first_name.send_keys("Мой ответ")
        last_name = browser.find_element_by_xpath("//input[@required and @placeholder='Input your last name']")
        last_name.send_keys("Мой ответ")
        email = browser.find_element_by_xpath("//input[@required and @placeholder='Input your email']")
        email.send_keys("Мой ответ")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text,
                         "Congratulations! You have successfully registered!", "Welcome text is not match")

    def test_second_page(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element_by_xpath("//input[@required and @placeholder='Input your first name']")
        first_name.send_keys("Мой ответ")
        last_name = browser.find_element_by_xpath("//input[@required and @placeholder='Input your last name']")
        last_name.send_keys("Мой ответ")
        email = browser.find_element_by_xpath("//input[@required and @placeholder='Input your email']")
        email.send_keys("Мой ответ")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text,
                         "Congratulations! You have successfully registered!", "Welcome text is not match")


if __name__ == "__main__":
    unittest.main()