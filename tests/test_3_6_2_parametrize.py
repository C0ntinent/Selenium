import time
import math

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(phrase)


@pytest.fixture(scope="function")
def answer():
    return str(math.log(int(time.time())))


phrase = ''


@pytest.mark.parametrize('number', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_guest_should_see_login_link(browser, number, answer):
    global phrase
    link = f"https://stepik.org/lesson/236{number}/step/1/"
    browser.implicitly_wait(10)
    browser.get(link)
    browser.find_element(By.TAG_NAME, "textarea").send_keys(answer)
    browser.find_element(By.CLASS_NAME, "submit-submission").click()
    word = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    try:
        assert word == 'Correct!', f'Not correct, your word is {word}'
    except AssertionError:
        phrase += word
