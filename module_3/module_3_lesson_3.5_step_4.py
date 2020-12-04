import time
import math
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button[type='submit']")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element_by_id("input_value").text
y = calc(x)

answer = browser.find_element_by_css_selector("[id='answer']")
answer.send_keys(y)

button = browser.find_element_by_css_selector("button[type='submit']")
button.click()

time.sleep(10)
browser.quit()
