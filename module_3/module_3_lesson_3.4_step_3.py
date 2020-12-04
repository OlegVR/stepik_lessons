import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

value1 = browser.find_element_by_id("num1").text
value2 = browser.find_element_by_id("num2").text

sum_values = str(int(value1) + int(value2))

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(sum_values)

button = browser.find_element_by_css_selector("button[type='submit']")
button.click()
time.sleep(10)
browser.quit()
