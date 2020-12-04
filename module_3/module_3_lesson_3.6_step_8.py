from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button[id='book']")
price = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))


button.click()

x = browser.find_element_by_id("input_value").text
y = calc(x)

answer = browser.find_element_by_css_selector("[id='answer']")
answer.send_keys(y)

button = browser.find_element_by_css_selector("button[type='submit']")
button.click()

time.sleep(10)
browser.quit()
