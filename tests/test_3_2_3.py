import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def form_of_reg(link):
    reg = ['vasya', 'pupkin', 'pupkin_vasya@gmail.com']
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first').send_keys(reg[0])
    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second').send_keys(reg[1])
    browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third').send_keys(reg[2])
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)

    # находим элемент, записываем в переменную welcome_text текст
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    return welcome_text


class TestREG(unittest.TestCase):
    def test_reg1(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        self.assertEqual(form_of_reg(link1), "Congratulations! You have successfully registered!", "Fail")

    def test_reg2(self):
        link2 = "http://suninjuly.github.io/registration2.html"
        self.assertEqual(form_of_reg(link2), "Congratulations! You have successfully registered!", "Fail")


if __name__ == "__main__":
    unittest.main()
