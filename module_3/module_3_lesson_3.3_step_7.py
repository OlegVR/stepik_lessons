import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element_by_id("treasure")
valuex = x.get_attribute("valuex")
y = calc(valuex)

answer = browser.find_element_by_css_selector("[id='answer']")
answer.send_keys(y)

checkbox = browser.find_element_by_css_selector("[id='robotCheckbox']")
checkbox.click()

radiobutton = browser.find_element_by_css_selector("[id='robotsRule']")
radiobutton.click()

button = browser.find_element_by_css_selector("button[type='submit']")
button.click()

time.sleep(15)
browser.quit()
