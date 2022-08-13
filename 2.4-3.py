from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://suninjuly.github.io/wait1.html')
    browser.implicitly_wait(5) # ожидаем появления всех указанных эл-тов, проверяем каждые 500мс в течение 5 сек
    btn = browser.find_element(By.ID, 'verify')
    btn.click()
    mes = browser.find_element(By.ID, 'verify_message')
    assert 'successful' in mes.text
