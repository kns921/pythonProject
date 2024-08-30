import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# запуск тестов без открытия браузера
# options.add_argument('--headless')
g = Service()
driver = webdriver.Chrome(options=options, service=g)
bace_url = 'https://the-internet.herokuapp.com/javascript_alerts'
driver.get(bace_url)
driver.maximize_window()

click_allert_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')
click_allert_button.click()
print('click_allert_button')

time.sleep(3)

driver.switch_to.alert.accept()
print('alert.accept')
