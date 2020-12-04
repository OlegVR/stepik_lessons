import os
import time
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

name = browser.find_element_by_name("firstname")
name.send_keys("Олег")

last_name = browser.find_element_by_name("lastname")
last_name.send_keys("Резвов")

email = browser.find_element_by_name("email")
email.send_keys("olegrezvov@yandex.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, '../file.txt')
sumbmit_file = browser.find_element_by_css_selector("[type='file']")
sumbmit_file.send_keys(file_path)

button = browser.find_element_by_css_selector("button[type='submit']")
button.click()

time.sleep(10)
browser.quit()
