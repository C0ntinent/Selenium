import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    x_element = browser.find_element(By.CSS_SELECTOR, "label [id='input_value']")
    x = x_element.text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, "input[id='answer']").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "input[id='robotCheckbox']").click()
    browser.find_element(By.CSS_SELECTOR, "input[id='robotsRule']").click()
    time.sleep(2)
    browser.find_element(By.TAG_NAME, "button").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
