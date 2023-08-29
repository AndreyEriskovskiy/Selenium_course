from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    url = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Edge()
    browser.get(url)
    input_fields = browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]')

    for field in input_fields:
        field.send_keys('some text')

    file_field = browser.find_element(By.CSS_SELECTOR, 'input[type="file"]')

    file_path = os.path.abspath(os.path.dirname(__file__))
    file = os.path.join(file_path, 'file.txt')
    file_field.send_keys(file)

    browser.find_element(By.CSS_SELECTOR, '.btn').click()

finally:
    time.sleep(10)
    browser.quit()