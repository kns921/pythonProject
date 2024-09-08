import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# запуск тестов без открытия браузера
options.add_argument('--headless')
g = Service()
driver = webdriver.Chrome(options=options, service=g)
bace_url = 'https://demoqa.com/dynamic-properties'
driver.get(bace_url)
driver.maximize_window()

"""Вариант с паузой"""
# time.sleep(6)
"""Вариант try / except"""
try:
    visible_button = driver.find_element(By.XPATH, '//*[@id="visibleAfter"]')
    visible_button.click()
except NoSuchElementException as exception:
    print('NoSuchElementException exception')
    time.sleep(6)
    print('Click Button')
