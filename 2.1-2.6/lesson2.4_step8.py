from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

url = 'http://suninjuly.github.io/explicit_wait2.html'

with webdriver.Edge() as browser:
    browser.get(url)
    browser.implicitly_wait(5)

    WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )

    browser.find_element(By.ID, 'book').click()

    x = browser.find_element(By.ID, 'input_value').text

    browser.find_element(By.ID, 'answer').send_keys(calc(x))
    browser.find_element(By.ID, 'solve').click()
    time.sleep(15)
