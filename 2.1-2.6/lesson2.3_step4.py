from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

url = 'http://suninjuly.github.io/alert_accept.html'

with webdriver.Edge() as browser:
    browser.get(url)
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
    time.sleep(15)

