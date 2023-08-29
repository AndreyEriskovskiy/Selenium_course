from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    url = 'http://suninjuly.github.io/selects2.html'
    browser = webdriver.Edge()
    browser.get(url)
    op1 = browser.find_element(By.ID, 'num1').text
    op2 = browser.find_element(By.ID, 'num2').text
    browser.find_element(By.TAG_NAME, 'select').click()
    browser.find_element(By.CSS_SELECTOR, f'[value="{str(int(op1) + int(op2))}"]').click()
    browser.find_element(By.CSS_SELECTOR, '.btn').click()



finally:
    time.sleep(10)
    browser.quit()