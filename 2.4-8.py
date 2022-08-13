import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


def calc(x):
    return math.log(abs(12 * math.sin(x)))

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    price = WebDriverWait(browser, 15).until(expected_conditions.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.ID, 'book').click()
    x = browser.find_element(By.ID, 'input_value')
    inp = browser.find_element(By.ID, 'answer')
    inp.send_keys(str(calc(int(x.text))))
    btn = browser.find_element(By.ID, 'solve')
    btn.click()
    time.sleep(10)
    print(browser.switch_to.alert.text)



