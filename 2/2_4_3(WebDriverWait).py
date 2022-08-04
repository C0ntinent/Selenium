import time
import math
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = browser.find_element(By.ID, "price").text

    WebDriverWait(browser, 50).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element(By.ID, "book").click()

    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)

    browser.find_element(By.ID, "solve").click()

    time.sleep(10)
    browser.quit()
