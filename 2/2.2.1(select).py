from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x, y):
    return str(int(x) + int(y))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    x = browser.find_element(By.CSS_SELECTOR, "[id='num1']").text
    y = browser.find_element(By.CSS_SELECTOR, "[id='num2']").text
    z = calc(x, y)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(z)
    time.sleep(2)
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
