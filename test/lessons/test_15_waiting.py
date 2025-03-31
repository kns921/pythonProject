from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# запуск тестов без открытия браузера
options.add_argument('--headless')
g = Service()
driver = webdriver.Chrome(options=options, service=g)
bace_url = 'https://demoqa.com/dynamic-properties'
driver.get(bace_url)
driver.maximize_window()

"""Неявное ожидание"""
print('Start Test 1')
driver.implicitly_wait(60)
vis_but = driver.find_element(By.XPATH, '//*[@id="visibleAfter"]')
vis_but.click()
print('Finish Test 1')

driver.refresh()
print('refresh')

"""Явное ожидание"""
print('Start Test 2')
vis_but = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="visibleAfter"]')))
vis_but.click()
print('Finish Test 2')
