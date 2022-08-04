import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/file_input.html")

    browser.find_element(By.NAME, "firstname").send_keys("Vasya")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("Petrov@mail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '1.txt')  # добавляем к этому пути имя файла
    browser.find_element(By.NAME, "file").send_keys(file_path)

    browser.find_element(By.TAG_NAME, "button").click()

    time.sleep(10)
    browser.quit()
