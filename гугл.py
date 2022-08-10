from selenium import webdriver
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as browser:
    browser.get("https://www.google.ru/")
    browser.implicitly_wait(10)
    browser.find_element(By.TAG_NAME, "input").send_keys("Как гуглить?")
    browser.find_element(By.CLASS_NAME, "gNO89b").click()
    time.sleep(10)
    browser.quit()
