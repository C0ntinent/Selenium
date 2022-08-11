import time

from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_language_of_browser(browser):
    browser.get(link)
    time.sleep(3)
    basket = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket625")
    assert basket, 'Нет кнопки'
