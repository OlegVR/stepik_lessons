import time
import math
from selenium import webdriver

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://SunInJuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

x = browser.find_element_by_id("input_value").text
y = calc(x)

answer = browser.find_element_by_css_selector("[id='answer']")
answer.send_keys(y)

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

checkbox = browser.find_element_by_css_selector("[id='robotCheckbox']")
checkbox.click()

radiobutton = browser.find_element_by_css_selector("[id='robotsRule']")
radiobutton.click()

button.click()

time.sleep(15)
browser.quit()

