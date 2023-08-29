from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    url = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Edge()
    browser.get(url)
    x = browser.find_element(By.ID, 'input_value').text
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.ID, 'robotCheckbox').click()
    btn = browser.find_element(By.CSS_SELECTOR, '.btn')
    browser.execute_script('return arguments[0].scrollIntoView(true);', btn)
    browser.find_element(By.ID, 'robotsRule').click()
    btn.click()


finally:
    time.sleep(10)
    browser.quit()