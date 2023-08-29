from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    url = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Edge()
    browser.get(url)
    x = browser.find_element(By.TAG_NAME, 'img').get_attribute('valuex')
    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.ID, 'robotCheckbox').click()
    browser.find_element(By.ID, 'robotsRule').click()
    browser.find_element(By.CSS_SELECTOR, '.btn').click()

finally:
    time.sleep(10)
    browser.quit()