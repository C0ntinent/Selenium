import time, math

from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


with webdriver.Chrome() as browser:
    browser.get("https://SunInJuly.github.io/execute_script.html")
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)

    browser.find_element(By.ID, "robotCheckbox").click()

    browser.execute_script('radio = document.getElementsByName("ruler")[0]; radio.scrollIntoView(true);')
    browser.find_element(By.ID, "robotsRule").click()

    browser.execute_script('button = document.getElementsByTagName("button")[0]; button.scrollIntoView(true);')
    browser.find_element(By.TAG_NAME, "button").click()

    time.sleep(10)
    browser.quit()
