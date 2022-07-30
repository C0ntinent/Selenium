from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://www.google.ru/")
    element = browser.find_element(By.TAG_NAME, "input")
    element.send_keys("Как разобрать пылесос?")
    time.sleep(2)
    button = browser.find_element(By.CLASS_NAME, "gNO89b")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла